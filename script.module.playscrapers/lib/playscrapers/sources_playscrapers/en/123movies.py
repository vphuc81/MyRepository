# -*- coding: utf-8 -*-
'''
    seriesonline scraper for PressPlay forks.
    Nov 9 2018 - Checked
    Oct 10 2018 - Cleaned and Checked

    Updated and refactored by someone.
    Originally created by others.
'''

import re

from six import ensure_text

from playscrapers import cfScraper
from playscrapers import parse_qs, urljoin, urlparse, urlencode
from playscrapers.modules import cleantitle
from playscrapers.modules import client
from playscrapers.modules import directstream
from playscrapers.modules import log_utils

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['www2.seriesonline8.co']
        self.base_link = custom_base or 'https://www11.123movie.movie'
        self.search_link = '/movie/search/%s'

    def matchAlias(self, title, aliases):
        try:
            for alias in aliases:
                if cleantitle.get(title) == cleantitle.get(alias['title']):
                    return True
        except:
            return False

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': title})
            url = {'imdb': imdb, 'title': title, 'year': year, 'aliases': aliases}
            url = urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': tvshowtitle})
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'aliases': aliases}
            url = urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urlencode(url)
            return url
        except:
            return

    def searchShow(self, title, season, aliases):
        try:
            #title = cleantitle.normalize(title)
            search = '%s Season %01d' % (title, int(season))
            url = urljoin(self.base_link, self.search_link % cleantitle.geturl(search))
            r = cfScraper.get(url).content
            r = ensure_text(r, errors='ignore')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a', ret='title'))
            r = [(i[0], i[1], re.findall('(.*?)\s+-\s+Season\s+(\d)', i[1])) for i in r]
            r = [(i[0], i[1], i[2][0]) for i in r if len(i[2]) > 0]
            url = [i[0] for i in r if self.matchAlias(i[2][0], aliases) and i[2][1] == season][0]
            url = urljoin(self.base_link, '%s/watching.html' % url)
            return url
        except:
            log_utils.log('123movies1 exception', 1)
            return

    def searchMovie(self, title, year, aliases):
        try:
            #title = cleantitle.normalize(title)
            url = urljoin(self.base_link, self.search_link % cleantitle.geturl(title))
            r = cfScraper.get(url).content
            r = ensure_text(r, errors='ignore')
            r = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
            r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a', ret='title'))
            results = [(i[0], i[1], re.findall('\((\d{4})', i[1])) for i in r]
            try:
                r = [(i[0], i[1], i[2][0]) for i in results if len(i[2]) > 0]
                url = [i[0] for i in r if self.matchAlias(i[1], aliases) and (year == i[2])][0]
            except:
                url = None
                pass

            if url == None:
                url = [i[0] for i in results if self.matchAlias(i[1], aliases)][0]

            url = urljoin(self.base_link, '%s/watching.html' % url)
            return url
        except:
            log_utils.log('123movies2 exception', 1)
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:

            if url == None: return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            aliases = eval(data['aliases'])

            if 'tvshowtitle' in data:
                ep = data['episode']
                url = '%s/film/%s-season-%01d/watching.html?ep=%s' % (self.base_link, cleantitle.geturl(data['tvshowtitle']), int(data['season']), ep)
                r = client.request(url, timeout='10', output='geturl')

                if url == None:
                    url = self.searchShow(data['tvshowtitle'], data['season'], aliases)

            else:
                url = self.searchMovie(data['title'], data['year'], aliases)

            if url == None: raise Exception()

            r = cfScraper.get(url).content
            r = ensure_text(r, errors='ignore')
            r = client.parseDOM(r, 'div', attrs={'class': 'les-content'})
            if 'tvshowtitle' in data:
                ep = data['episode']
                links = client.parseDOM(r, 'a', attrs={'episode-data': ep}, ret='player-data')
            else:
                links = client.parseDOM(r, 'a', ret='player-data')

            for link in links:
                try:
                    if link.startswith('//'):
                        link = 'https:' + link
                    host = re.findall('([\w]+[.][\w]+)$', urlparse(link.strip().lower()).netloc)[0]
                    if not host in hostDict: raise Exception()
                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')

                    if 'load.php' not in link:
                        sources.append({'source': host, 'quality': '720p', 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
                except:
                    pass

            return sources
        except:
            log_utils.log('123movies0 exception', 1)
            return sources

    def resolve(self, url):
        if "google" in url:
            return directstream.googlepass(url)
        else:
            return url
