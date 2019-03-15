# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Yoda
# Addon id: plugin.video.Yoda
# Addon Provider: Supremacy


import re
import requests
import traceback
from datetime import datetime
from bs4 import BeautifulSoup, NavigableString
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import xbmc

from resources.lib.modules.client import randomagent
from resources.lib.modules import cleantitle
from resources.lib.modules import jsunpack


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['primewire.gr']
        self.BASE_URL = 'http://m.primewire.gr'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            lowerTitle = title.lower()
            possibleTitles = set(
                (lowerTitle, cleantitle.getsearch(lowerTitle))
                + tuple((alias['title'].lower() for alias in aliases) if aliases else ())
            )
            return self._getSearchData(lowerTitle, possibleTitles, year, self._createSession(), isMovie=True)
        except:
            self._logException()
            return None


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            lowerTitle = tvshowtitle.lower()
            possibleTitles = set(
                (lowerTitle, cleantitle.getsearch(lowerTitle))
                + tuple((alias['title'].lower() for alias in aliases) if aliases else ())
            )
            return self._getSearchData(lowerTitle, possibleTitles, year, self._createSession(), isMovie=False)
        except:
            self._logException()
            return None


    def episode(self, data, imdb, tvdb, title, premiered, season, episode):
        try:
            seasonsPageURL = data['pageURL']

            session = self._createSession(data['UA'], data['cookies'], data['referer'])
            xbmc.sleep(1000)
            r = self._sessionGET(seasonsPageURL, session)
            if r.ok:
                soup = BeautifulSoup(r.content, 'html.parser')
                mainDIV = soup.find('div', {'class': 'tv_container'})
                firstEpisodeDIV = mainDIV.find('div', {'class': 'show_season', 'data-id': season})
                episodeDIV = next(
                    (
                        element for element in firstEpisodeDIV.next_siblings
                        if not isinstance(element, NavigableString) and next(element.a.strings, '').strip('E ') == episode
                    ),
                    None
                )
                if episodeDIV:
                    return {
                        'pageURL': self.BASE_URL + episodeDIV.a['href'],
                        'UA': session.headers['User-Agent'],
                        'referer': seasonsPageURL,
                        'cookies': session.cookies.get_dict()
                    }
            return None
        except:
            self._logException()
            return None


    def sources(self, data, hostDict, hostprDict):
        try:
            session = self._createSession(data['UA'], data['cookies'], data['referer'])
            pageURL = data['pageURL']

            xbmc.sleep(1000)
            r = self._sessionGET(pageURL, session)
            if not r.ok:
                self._logException('PRIMEWIRE > Sources page request failed: ' + data['pageURL'])
                return None

            sources = [ ]

            soup = BeautifulSoup(r.content, 'html.parser')
            mainDIV = soup.find('div', class_='actual_tab')
            for hostBlock in mainDIV.findAll('tbody'):
                if 'onclick' in hostBlock.a.attrs:
                    onClick = hostBlock.a['onclick']
                    if 'Promo' in onClick:
                        continue 

                    hostName = re.search('''['"](.*?)['"]''', onClick).group(1)
                    qualityClass = hostBlock.span['class']
                    quality = 'SD' if ('cam' not in qualityClass and 'ts' not in qualityClass) else 'CAM'
                    unresolvedData = {
                        'pageURL': self.BASE_URL + hostBlock.a['href'], 
                        'UA': data['UA'],
                        'cookies': session.cookies.get_dict(),
                        'referer': pageURL
                    }
                    sources.append(
                        {
                            'source': hostName,
                            'quality': quality,
                            'language': 'en',
                            'url': unresolvedData,
                            'direct': False,
                            'debridonly': False
                        }
                    )
            return sources
        except:
            self._logException()
            return None


    def resolve(self, data):
        try:
            hostURL = None
            DELAY_PER_REQUEST = 1000 # In milliseconds.

            startTime = datetime.now()
            session = self._createSession(data['UA'], data['cookies'], data['referer'])
            r = self._sessionGET(data['pageURL'], session, allowRedirects=False)
            if r.ok:
                if 'Location' in r.headers:
                    hostURL = r.headers['Location'] 
                else:
                   
                    try:
                        hostURL = re.search(r'''go\(\\['"](.*?)\\['"]\);''', jsunpack.unpack(r.text)).group(1)
                    except:
                        pass
            elapsed = int((datetime.now() - startTime).total_seconds() * 1000)
            if elapsed < DELAY_PER_REQUEST:
                xbmc.sleep(max(DELAY_PER_REQUEST - elapsed, 100))

            return hostURL
        except:
            self._logException()
            return None


    def _getSearchData(self, query, possibleTitles, year, session, isMovie):
        try:
            searchURL = self.BASE_URL + ('/?' if isMovie else '/?tv=&') + urlencode({'search_keywords': query})
            r = self._sessionGET(searchURL, session)
            if not r.ok:
                return None

            bestGuessesURLs = [ ]

            soup = BeautifulSoup(r.content, 'html.parser')
            mainDIV = soup.find('div', role='main')
            for resultDIV in mainDIV.findAll('div', {'class': 'index_item'}, recursive=False):
                match = re.search(r'(.*?)(?:\s\((\d{4})\))?$', resultDIV.a['title'].lower().strip())
                resultTitle, resultYear = match.groups()
                if resultTitle in possibleTitles:
                    if resultYear == year: 
                        bestGuessesURLs.insert(0, resultDIV.a['href'])
                    else:
                        bestGuessesURLs.append(resultDIV.a['href'])

            if bestGuessesURLs:
                return {
                    'pageURL': self.BASE_URL + bestGuessesURLs[0],
                    'UA': session.headers['User-Agent'],
                    'referer': searchURL,
                    'cookies': session.cookies.get_dict(),
                }
            else:
                return None
        except:
            self._logException()
            return None


    def _sessionGET(self, url, session, allowRedirects=True):
        try:
            return session.get(url, allow_redirects=allowRedirects, timeout=8)
        except:
            return type('FailedResponse', (object,), {'ok': False})


    def _createSession(self, userAgent=None, cookies=None, referer=None):
        session = requests.Session()
        session.headers.update(
            {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'User-Agent': userAgent if userAgent else randomagent(),
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': referer if referer else self.BASE_URL + '/',
                'Upgrade-Insecure-Requests': '1',
                'DNT': '1'
            }
        )
        if cookies:
            session.cookies.update(cookies)
        return session


    def _debug(self, name, val=None):
        xbmc.log('PRIMEWIRE Debug > ' + name + (' %s' % repr(val) if val else ''), xbmc.LOGWARNING)


    def _logException(self, text=None):
        return 
        if text:
            xbmc.log(text, xbmc.LOGERROR)
        else:
            xbmc.log(traceback.format_exc(), xbmc.LOGERROR)