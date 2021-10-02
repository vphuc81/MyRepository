# -*- coding: utf-8 -*-

'''
    PlayScrapers module
'''

import re

#import requests

from six import ensure_text

from playscrapers import cfScraper
from playscrapers import parse_qs, urljoin, urlencode
from playscrapers.modules import cleantitle
from playscrapers.modules import client
from playscrapers.modules import debrid
from playscrapers.modules import source_utils
from playscrapers.modules import log_utils

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['bt4g.org']
        self.base_link = custom_base or 'https://bt4g.org'
        self.search_link = '/movie/search/%s/byseeders/1'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urlencode(url)
            return url
        except:
            log_utils.log('bt4g0 - Exception', 1)
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except:
            log_utils.log('bt4g1 - Exception', 1)
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
            log_utils.log('bt4g2 - Exception', 1)
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if debrid.status() is False:
                return sources

            if url is None:
                return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            query = '%s s%02de%02d' % (data['tvshowtitle'], int(data['season']), int(data['episode']))\
                                       if 'tvshowtitle' in data else '%s %s' % (data['title'], data['year'])
            query = re.sub(u'(\\\|/| -|:|;|\*|\?|"|\'|<|>|\|)', ' ', query).lower()

            url = urljoin(self.base_link, self.search_link % query)

            #r = client.request(url)
            #r = requests.get(url).content
            r = cfScraper.get(url).content
            r = ensure_text(r, errors='replace').replace('&nbsp;', ' ')
            r = client.parseDOM(r, 'div', attrs={'class': 'col s12'})
            posts = client.parseDOM(r, 'div')[1:]
            posts = [i for i in posts if 'magnet/' in i]
            for post in posts:
                try:
                    links = client.parseDOM(post, 'a', ret='href')[0]
                    url = 'magnet:?xt=urn:btih:' + links.lstrip('magnet/')
                    try:
                        name = client.parseDOM(post, 'a', ret='title')[0]
                        if not query in cleantitle.get_title(name): continue
                    except:
                        name = ''

                    quality, info = source_utils.get_release_quality(name, name)
                    try:
                        size = re.findall(r'<b class="cpill .+?-pill">(.+?)</b>', post)[0]
                        dsize, isize = source_utils._size(size)
                    except:
                        dsize, isize = 0.0, ''

                    info.insert(0, isize)

                    info = ' | '.join(info)

                    sources.append({'source': 'Torrent', 'quality': quality, 'language': 'en', 'url': url, 'info': info,
                                    'direct': False, 'debridonly': True, 'size': dsize, 'name': name})
                except:
                    pass

            return sources
        except:
            log_utils.log('bt4g3 - Exception', 1)
            return sources

    def resolve(self, url):
        return url
