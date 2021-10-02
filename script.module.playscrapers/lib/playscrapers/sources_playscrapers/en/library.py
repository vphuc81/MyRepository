# -*- coding: utf-8 -*-

'''
    PressPlay Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import simplejson as json

from six import ensure_str, ensure_text

from playscrapers import urlparse, urlencode, parse_qs
from playscrapers.modules import cleantitle, control#, log_utils

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en', 'de', 'fr', 'gr', 'ko', 'pl', 'pt', 'ru']
        self.domains = []

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            return urlencode({'imdb': imdb, 'title': title, 'localtitle': localtitle,'year': year})
        except:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            return urlencode({'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'localtvshowtitle': localtvshowtitle, 'year': year})
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url is None:
                return

            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url.update({'premiered': premiered, 'season': season, 'episode': episode})
            return urlencode(url)
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []

        try:
            if url is None:
                return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            content_type = 'episode' if 'tvshowtitle' in data else 'movie'

            years = (data['year'], str(int(data['year'])+1), str(int(data['year'])-1))

            if content_type == 'movie':
                title = cleantitle.get(data['title'])
                localtitle = cleantitle.get(data['localtitle'])
                ids = [data['imdb']]

                r = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties": ["imdbnumber", "title", "originaltitle", "file"]}, "id": 1}' % years)
                r = ensure_text(r, 'utf-8', errors='ignore')
                r = json.loads(r)['result']['movies']

                r = [i for i in r if str(i['imdbnumber']) in ids or title in [cleantitle.get(ensure_str(i['title'])), cleantitle.get(ensure_str(i['originaltitle']))]]
                r = [i for i in r if not ensure_str(i['file']).endswith('.strm')][0]

                r = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovieDetails", "params": {"properties": ["streamdetails", "file"], "movieid": %s }, "id": 1}' % str(r['movieid']))
                r = ensure_text(r, 'utf-8', errors='ignore')
                r = json.loads(r)['result']['moviedetails']
            elif content_type == 'episode':
                title = data['tvshowtitle']
                localtitle = data['localtvshowtitle']
                season, episode = data['season'], data['episode']

                r = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties": ["imdbnumber", "title"]}, "id": 1}' % years)
                r = ensure_text(r, 'utf-8', errors='ignore')
                r = json.loads(r)['result']['tvshows']

                r = [i for i in r if title in (ensure_str(i['title']))][0]

                r = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodes", "params": {"filter":{"and": [{"field": "season", "operator": "is", "value": "%s"}, {"field": "episode", "operator": "is", "value": "%s"}]}, "properties": ["file"], "tvshowid": %s }, "id": 1}' % (str(season), str(episode), str(r['tvshowid'])))
                r = ensure_text(r, 'utf-8', errors='ignore')
                r = json.loads(r)['result']['episodes']

                r = [i for i in r if not ensure_str(i['file']).endswith('.strm')][0]

                r = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodeDetails", "params": {"properties": ["streamdetails", "file"], "episodeid": %s }, "id": 1}' % str(r['episodeid']))
                r = ensure_text(r, 'utf-8', errors='ignore')
                r = json.loads(r)['result']['episodedetails']

            url = ensure_str(r['file'])

            try: qual = int(r['streamdetails']['video'][0]['width'])
            except: qual = -1

            if qual >= 2160: quality = '4K'
            elif 1920 <= qual < 2000: quality = '1080p'
            elif 1280 <= qual < 1900: quality = '720p'
            elif qual < 1280: quality = 'SD'

            info = []

            try:
                f = control.openFile(url) ; s = f.size() ; f.close()
                s = '%.2f GB' % (float(s)/1024/1024/1024)
                info.append(s)
            except: pass

            try:
                c = r['streamdetails']['video'][0]['codec']
                if c == 'avc1': c = 'h264'
                info.append(c)
            except: pass

            try:
                ac = r['streamdetails']['audio'][0]['codec']
                if ac == 'dca': ac = 'dts'
                if ac == 'dtshd_ma': ac = 'dts-hd ma'
                info.append(ac)
            except: pass

            try:
                ach = r['streamdetails']['audio'][0]['channels']
                if ach == 1: ach = 'mono'
                if ach == 2: ach = '2.0'
                if ach == 6: ach = '5.1'
                if ach == 8: ach = '7.1'
                info.append(ach)
            except: pass

            info = ' | '.join(info)

            sources.append({'source': '', 'quality': quality, 'language': 'en', 'url': url, 'info': info, 'local': True, 'direct': True, 'debridonly': False})

            return sources
        except:
            #log_utils.log('lib_scraper_fail0', 1)
            return sources

    def resolve(self, url):
        return url


