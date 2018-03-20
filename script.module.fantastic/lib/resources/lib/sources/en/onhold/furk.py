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

import requests, json, sys
from resources.lib.modules import cleantitle, control, source_utils

accepted_extensions = ['mkv','mp4','avi', 'm4v']

class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domain =  ['xmovies8.es']
        self.meta_search_link = "/api/plugins/metasearch?api_key=%s&q=%s"
        self.base_link = 'https://xmovies8.es'
        self.api_key = control.setting('furk.api')

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = tvshowtitle
            return url
        except:
            pass

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            url = {'tvshowtitle': url, 'season': season, 'episode': episode}
            return url
        except:
            pass

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if len(url['episode']) == 1:
                url['episode'] = "0" + url['episode']
            if len(url['season']) == 1:
                url['season'] = "0" + url['season']
            s = requests.Session()
            url = url['tvshowtitle'] + "+S" + url['season'] + "e" + url['episode']
            url = (self.base_link + self.meta_search_link % (self.api_key, url.replace(' ', '+')))
            print("info - " + url)
            p = s.get(url)
            p = json.loads(p.text)
            files = p['files']
            for i in files:
                if not int(i['files_num_video_player']) > 1:
                    name = i['name']
                    id = i['id']
                    url_dl = ''
                    for x in accepted_extensions:
                        if 'url_dl' in i:
                            if i['url_dl'].endswith(x):
                                url_dl = i['url_dl']
                                quality = source_utils.get_release_quality(name , url_dl)
                                print('info - ' + str(quality) + " link " + url_dl + " name " + name)
                                sources.append({'source': host, 'quality': quality[0], 'language': "en", 'url': url_dl, 'info': quality[1],
                             'direct': True, 'debridonly': False})
                            else:
                                continue
                        else:
                            continue
                    if url_dl == '':
                        continue
                else:
                    continue
            for i in sources:
                print("info - sources - " + str(i))
            return sources
        except:
            print("Unexpected error in Furk Script: source", sys.exc_info()[0])
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            pass


    def resolve(self, url):
            return url