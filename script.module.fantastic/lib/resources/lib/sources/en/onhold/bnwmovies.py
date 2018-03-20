# -*- coding: UTF-8 -*-
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

import re,urllib,urlparse,base64
import requests

from resources.lib.modules import client

class source:
    def __init__(self):
        self.priority = 0
        self.language = ['en']
        self.domains = ['xmovies8.es']
        self.base_link = 'https://xmovies8.es'
        self.search_link = '/?s='

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'title': title, 'year': year, 'imdb': imdb}
            return urllib.urlencode(url)
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            if url == None: return sources

            urldata = urlparse.parse_qs(url)
            urldata = dict((i, urldata[i][0]) for i in urldata)
            title = urldata['title']
            year = urldata['year']

            start_url=self.base_link+self.search_link+title.replace(' ','+')
            html = client.request(start_url)
            match = re.compile('<div class="post">.+?href="(.+?)".+?rel="bookmark">(.+?)</a>',re.DOTALL).findall(html)
            for url,alt in match:
                if title.lower() == alt.lower():
                    html2 = client.request(url)

                    match = re.compile('<title >(.+?)</title>',re.DOTALL).findall(html2)
                    for rel in match:
                        if year in rel:
                            Link = re.compile('<source.+?src="(.+?)"',re.DOTALL).findall(html2)[-1] 
                            playlink = Link
                            sources.append({'source':'BNW','quality':'SD','language': 'en','url':playlink,'info':[],'direct':True,'debridonly':False})
            return sources
        except:
            return sources

    def resolve(self, url):
        return url