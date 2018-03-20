# -*- coding: utf-8 -*-

'''
    Fantastic Add-on

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

import requests
import json,sys
from resources.lib.modules import control
import inspect

class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domain =  'xmovies8.es'
        self.domains = 'https://xmovies8.es'
        self.search_link = 'http://xmovies8.es/search/auto?q='
        self.movie_link = 'http://xmovies8.es/movies/getMovieLink?'
        self.login_link = 'http://xmovies8.es/session/login?return_url=/index'
        self.tv_link = 'http://xmovies8.es/series/getTvLink?'
        self.login_payload = {'username': control.setting('http://xmovies8.es.username'),'password':control.setting('http://xmovies8.es.password')}

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = tvshowtitle
            return url
        except:
            print("Unexpected error in  http://xmovies8.es Script:", sys.exc_info()[0])
            return ""

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        with requests.Session() as s:
            try:
                if (self.login_payload['username'] == '' and self.login_payload['password'] == ''): return ''
                p = s.post(self.login_link, self.login_payload)
                search_text = url
                p = s.get(self.search_link + search_text)
                show_dict = json.loads(p.text)
                for i in show_dict:
                    if i['title'].lower() == search_text.lower():
                        show_dict = i
                        break
                url = {'title': search_text, 'id': show_dict['id'], 'season': season, 'episode': episode}
                link = self.tv_link + "id=%s&s=%s&e=%s" % (url["id"], url['season'], url['episode'])
                p = s.post(link)
                url = json.loads(p.text)
                sources = []
                for i in url:
                    video = {}
                    p = s.get(self.base_link + i['file'], stream=True, timeout=2)
                    if p.history:
                        video['url'] = p.url
                        video['quality'] = i['label']
                        video['source'] = 'gvideo'
                        video['debridonly'] = False
                        video['language'] = 'en'
                        video['info'] = i['type']
                        video['direct'] = True
                        sources.append(video)
                    else:
                        pass
                return sources
            except Exception as e:
                print("Unexpected error in Chillax episode Script:")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print(exc_type, exc_tb.tb_lineno)
                return ""

    def sources(self, url, hostDict, hostprDict):
        return url

    def resolve(self, url):
            return url

#url = source.tvshow(source(), '', '', 'Vikings','','' '','2016')
#url = source.episode(source(),url,'', '', '', '', '4', '1')
#sources = source.sources(source(),url,'','')
