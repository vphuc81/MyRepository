'''
	
    ***FSPM was here*****

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

import re,traceback,urllib,urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import log_utils
from resources.lib.modules import debrid

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['freemoviedownloads6.com']
        self.base_link = 'http://freemoviedownloads6.com/'
        self.search_link = '%s/search?q=freemoviedownloads6.com+%s+%s'
        self.goog = 'https://www.google.co.uk'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            scrape = title.lower().replace(' ','+').replace(':', '')

            start_url = self.search_link %(self.goog,scrape,year)

            html = client.request(start_url)
            results = re.compile('href="(.+?)"',re.DOTALL).findall(html)
            for url in results:
                if self.base_link in url:
                    if 'webcache' in url:
                        continue
                    if cleantitle.get(title) in cleantitle.get(url):
                        chkhtml = client.request(url)
                        chktitle = re.compile('<title>(.+?)</title>',re.DOTALL).findall(chkhtml)[0]
                        if cleantitle.get(title) in cleantitle.get(chktitle):
                            if year in chktitle:
                                return url
            return
        except:
            failure = traceback.format_exc()

            return

    def sources(self, url, hostDict, hostprDict):
        try:
            if url == None: return
            sources = []
            html = client.request(url)
            html = html.split("type='video/mp4'")[1]
            match = re.compile('href="(.+?)"',re.DOTALL).findall(html)
            for link in match:
                if '1080' in link:
                    quality = '1080p'
                elif '720' in link:
                    quality = '720p'
                elif '480' in link:
                    quality = '480p'
                else:
                    quality = 'SD'
                if '.mkv' in link:
                    sources.append({'source': 'DirectLink', 'quality': quality, 'language': 'en', 'url': link, 'direct': True, 'debridonly': False})
                if '.mp4' in link:
                    sources.append({'source': 'DirectLink', 'quality': quality, 'language': 'en', 'url': link, 'direct': True, 'debridonly': False})
            return sources
        except:
            failure = traceback.format_exc()

            return

    def resolve(self, url):
        return url