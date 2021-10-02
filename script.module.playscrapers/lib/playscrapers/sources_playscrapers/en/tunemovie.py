# -*- coding: utf-8 -*-

import re, random

import simplejson as json
from playscrapers import parse_qs, urljoin, urlencode, quote_plus

from playscrapers.modules import client
from playscrapers.modules import cleantitle
from playscrapers.modules import directstream
from playscrapers.modules import source_utils
from playscrapers.modules import log_utils

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['tunemovie.com', 'xmovies.is', 'pubfilmfree.com', '123movies.sc']
        self.base_link = custom_base
        self.search_link = '/search/%s.html'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year, 'aliases': aliases}
            url = urlencode(url)
            return url
        except:
            log_utils.log('tunemovie movie Exception', 1)
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except Exception:
            log_utils.log('tunemovie tvshow Exception', 1)
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url is None: return

            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urlencode(url)
            return url
        except:
            log_utils.log('tunemovie episode Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            #log_utils.log('tunemovie self.base_linkS: \n' + repr(self.base_link))
            if url == None:
                return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['tvshowtitle'] if 'tvshowtitle' in data else data['title']
            imdb = data['imdb']

            check = cleantitle.get(title)
            query = self.search_link % quote_plus(title)

            r, self.base_link = client.list_request(self.base_link or self.domains, query)
            #log_utils.log('tunemovie self.base_link: \n' + repr(self.base_link))

            if not 'tvshowtitle' in data:
                if '123movies.sc' in self.base_link:
                    r0 = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
                    u = [(client.parseDOM(i, 'a', ret='href')[0], client.parseDOM(i, 'a', ret='title')[0], client.parseDOM(i, 'div', attrs={'class': 'jt-info'})[0]) for i in r0]
                else:
                    r0 = client.parseDOM(r, 'div', attrs={'class': 'item_movie'})
                    u = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title'), re.findall('(\d{4})', i)) for i in r0]
                    u = [(i[0][0], i[1][0], i[2][0]) for i in u if len(i[0]) > 0 and len(i[1]) > 0 and len(i[2]) > 0]
                url = [i[0] for i in u if check == cleantitle.get(i[1]) and data['year'] == i[2]][0]

            else:
                if '123movies.sc' in self.base_link:
                    r0 = client.parseDOM(r, 'div', attrs={'class': 'ml-item'})
                    u = [(client.parseDOM(i, 'a', ret='href')[0], client.parseDOM(i, 'a', ret='title')[0]) for i in r0]
                else:
                    r0 = client.parseDOM(r, 'div', attrs={'class': 'item_movie'})
                    u = [(client.parseDOM(i, 'a', ret='href'), client.parseDOM(i, 'a', ret='title')) for i in r0]
                    u = [(i[0][0], i[1][0]) for i in u if len(i[0]) > 0 and len(i[1]) > 0]
                url = [i[0] for i in u if check in cleantitle.get(i[1]) and ('Season %s' % data['season']) in i[1]][0]
                url += '?episode=%01d' % (int(data['episode']))

            try:
                url, episode = re.findall('(.+?)\?episode=(\d*)$', url)[0]
            except:
                episode = None
            #ref = url
            url += '?play=1'
            ref = url
            #log_utils.log('tunemovie sources starting url: \n' + repr(url))
            result = client.request(url)
            if episode == None and not imdb in result:
                return sources
            if not episode == None:
                result = client.parseDOM(result, 'div', attrs={'id': 'ip_episode'})[0]
                ep_url = client.parseDOM(result, 'a', attrs={'data-name': str(episode)}, ret='href')[0]
                result = client.request(ep_url)
            if '123movies.sc' in url:
                r = client.parseDOM(result, 'ul', attrs={'id': 'ip_server'})[0]
                r = client.parseDOM(r, 'li')
            else:
                r = client.parseDOM(result, 'div', attrs={'class': '[^"]*server_[^"]*'})
            for u in r:
                try:
                    url = urljoin(self.base_link, '/ip.file/swf/plugins/ipplugins.php')
                    p1 = client.parseDOM(u, 'a', ret='data-film')[0]
                    p2 = client.parseDOM(u, 'a', ret='data-server')[0]
                    p3 = client.parseDOM(u, 'a', ret='data-name')[0]
                    post = {'ipplugins': 1, 'ip_film': p1, 'ip_server': p2, 'ip_name': p3, 'fix': "0"}
                    post = urlencode(post)
                    for i in range(3):
                        result = client.request(url, post=post, XHR=True, referer=ref, timeout='10')
                        if not result == None:
                            break
                    result = json.loads(result)
                    u = result['s']
                    try:
                        s = result['v']
                    except:
                        s = result['c']
                    url = urljoin(self.base_link, '/ip.file/swf/ipplayer/ipplayer.php')
                    for n in range(3):
                        try:
                            post = {'u': u, 'w': '100%', 'h': '420', 's': s, 'n': n}
                            post = urlencode(post)
                            result = client.request(url, post=post, XHR=True, referer=ref)
                            src = json.loads(result)['data']
                            #log_utils.log('tunemovie sources src 1 list: \n' + repr(src))
                            if not src:
                                continue
                            if type(src) is list:
                                src = [i['files'] for i in src]
                                #log_utils.log('tunemovie sources src 1 list: \n' + repr(src))
                                for i in src:
                                    sources.append({'source': 'gvideo', 'quality': directstream.googletag(i)[0]['quality'], 'language': 'en', 'url': i, 'direct': True, 'debridonly': False})
                            else:
                                link = "https:" + src if not src.startswith('http') else src
                                #log_utils.log('tunemovie sources src link: \n' + repr(link))
                                if 'tunestream.net' in link:
                                    for source in self.tunestream(link, hostDict):
                                        sources.append(source)
                                else:
                                    valid, host = source_utils.is_host_valid(link, hostDict)
                                    if valid:
                                        sources.append({'source': host, 'quality': 'HD', 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
                        except:
                            log_utils.log('tunemovie Exception', 1)
                            pass
                except:
                    log_utils.log('tunemovie Exception', 1)
                    pass
            return sources
        except Exception:
            log_utils.log('tunemovie sources Exception', 1)
            return sources


# UnUsed Result, Needs Coded.
# 'https://waaw.tv/watch_video.php?v=e78cLgr5c392'


    def resolve(self, url):
        if 'google' in url:
            url = directstream.googlepass(url)
        return url


    def tunestream(self, url, hostDict):
        sources = [] # 'https://tunestream.net/embed-f1m4uqrfm987.html'
        try:
            header = {'User-Agent': client.agent(), 'Referer': 'https://tunestream.net'}
            page = client.request(url, headers=header)
            results = re.compile('sources\s*:\s*\[(.+?)\]').findall(page)[0]
            items = re.findall(r'''{(.+?)}''', results)
            for item in items:
                link = re.findall(r'''file:"(.+?)"''', item)[0]
                #log_utils.log('tunemovie tunestream: \n' + repr(link))
                try:
                    label = re.findall(r'''label:"(.+?)"''', item)[0]
                except:
                    label = 'SD'
                quality, info = source_utils.get_release_quality(label, link)
                link += '|%s' % urlencode(header)
                sources.append({'source': 'tunestream', 'quality': quality, 'language': 'en', 'info': info, 'url': link, 'direct': True, 'debridonly': False})
            return sources
        except Exception:
            log_utils.log('tunemovie Exception', 1)
            return sources


