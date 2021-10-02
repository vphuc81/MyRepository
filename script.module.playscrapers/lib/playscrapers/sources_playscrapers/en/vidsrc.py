# -*- coding: utf-8 -*-

'''
    PlayScrapers module
'''


import re

from playscrapers import parse_qs, urljoin, urlencode
from playscrapers.modules import client
from playscrapers.modules import dom_parser
from playscrapers.modules import source_utils
from playscrapers.modules import log_utils

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['vidsrc.me', 'v2.vidsrc.me']
        self.base_link = custom_base or 'https://v2.vidsrc.me'
        self.movie_link = '/embed/%s'
        self.tv_link = '/embed/%s/%s-%s'
        self.headers = {'User-Agent': client.agent(), 'Referer': self.base_link}

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            url = urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except:
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
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if url is None:
                return sources

            hostDict = hostprDict + hostDict

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            if not data['imdb'] or data['imdb'] == '0':
                return sources

            if 'tvshowtitle' in data:
                query = self.tv_link % (data['imdb'], data['season'], data['episode'])
            else:
                query = self.movie_link % data['imdb']

            url = urljoin(self.base_link, query)
            #log_utils.log('VIDSRC url: ' + repr(url))

            r = client.r_request(url)
            #log_utils.log('VIDSRC r: ' + r)
            items = dom_parser.parse_dom(r, 'div', req='data-hash')
            for item in items:
                url = 'https://v2.vidsrc.me/src/%s' % item.attrs['data-hash']
                #log_utils.log('VIDSRC url: ' + repr(url))
                host = client.parseDOM(item.content, 'div')[0]
                #log_utils.log('VIDSRC host: ' + repr(host))
                host = host.lower().replace('vidsrc', '').strip()
                if host == 'pro': # other sources are javascripted
                    host = 'direct'
                    sources.append({'source': host, 'quality': '720p', 'language': 'en', 'url': url, 'direct': True, 'debridonly': False})
            return sources
        except:
            log_utils.log('VIDSRC Exception', 1)
            return sources

    def resolve(self, url):
        data = client.r_request(url)
        #log_utils.log('VIDSRC data: ' + data)
        try: link = re.findall("'player' src='(.+?)'", data)[0]
        except: link = re.findall('"file": "(.+?)"', data)[0]
        link = link + '|Referer=https://vidsrc.me'
        url = link if link.startswith('http') else 'https:{0}'.format(link)
        #log_utils.log('VIDSRCurl: ' + repr(url))
        return url
