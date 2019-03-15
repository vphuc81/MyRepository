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

import re,urllib,urlparse,json

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import cfscrape
from resources.lib.modules import dom_parser


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['xmovies8.tv', 'xmovies8.ru', 'xmovies8.es', 'xmovies8.nz']
        self.base_link = 'https://xmovies8.pl'
        self.search_link = '/movies/search?s=%s'
        self.scraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': title})
            url = {'imdb': imdb, 'title': title, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            aliases.append({'country': 'us', 'title': tvshowtitle})
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'aliases': aliases}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return
            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urllib.urlencode(url)
            return url
        except:
            return

    def searchShow(self, title, season, year, aliases, headers):
        try:
            clean_title = cleantitle.geturl(title).replace('-','+')

            url = urlparse.urljoin(self.base_link, self.search_link % ('%s+Season+%01d' % (clean_title, int(season))))
            r = self.scraper.get(url).content

            r = client.parseDOM(r, 'div', attrs={'class': 'list_movies'})
            r = dom_parser.parse_dom(r, 'a', req='href')
            r = [(i.attrs['href']) for i in r if '%s - Season %01d' % (title, int(season)) in i.content]

            return r[0]
        except:
            return

    def searchMovie(self, title, year, aliases, headers):
        try:
            clean_title = cleantitle.geturl(title).replace('-','+')

            url = urlparse.urljoin(self.base_link, self.search_link % ('%s' %clean_title))
            r = self.scraper.get(url).content

            r = client.parseDOM(r, 'div', attrs={'class': 'list_movies'})
            r = dom_parser.parse_dom(r, 'a', req='href')
            r = [(i.attrs['href']) for i in r if i.content == '%s (%s)' %(title,year)]

            return r[0]
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            data = urlparse.parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])
            aliases = eval(data['aliases'])
            headers = {}

            if 'tvshowtitle' in data:
                episode = int(data['episode'])
                url = self.searchShow(data['tvshowtitle'], data['season'], data['year'], aliases, headers)
            else:
                episode = 0
                url = self.searchMovie(data['title'], data['year'], aliases, headers)

            if url == None: return sources

            #url = urlparse.urljoin(self.base_link, url)
            url = re.sub('/watching.html$', '', url.strip('/'))
            url = url + '/watching.html'

            p = self.scraper.get(url).content

            if episode > 0:
                r = client.parseDOM(p, 'div', attrs={'class': 'ep_link.+?'})[0]
                r = zip(client.parseDOM(r, 'a', ret='href'), client.parseDOM(r, 'a'))
                r = [(i[0], re.findall('Episode\s+(\d+)', i[1])) for i in r]
                r = [(i[0], i[1][0]) for i in r]
                url = [i[0] for i in r if int(i[1]) == episode][0]
                p = self.scraper.get(url, headers=headers).content

            referer = url
            headers = {
                'User-Agent': client.randomagent(),
                'Referer': url
            }

            id = re.findall('load_player\(.+?(\d+)', p)[0]
            r = urlparse.urljoin(self.base_link, '/ajax/movie/load_player_v3?id=%s' % id)
            r = self.scraper.get(r, headers=headers).content

            url = json.loads(r)['value']

            if url.startswith('//'):
                url = 'https:' + url

            r = self.scraper.get(url, headers=headers).content

            headers = '|' + urllib.urlencode(headers)

            source = str(json.loads(r)['playlist'][0]['file']) + headers

            sources.append({'source': 'CDN', 'quality': 'HD', 'language': 'en', 'url': source, 'direct': True, 'debridonly': False})

            return sources
        except:
            return sources

    def resolve(self, url):
        return url
