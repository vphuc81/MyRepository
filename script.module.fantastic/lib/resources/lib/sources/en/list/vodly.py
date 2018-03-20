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

'''ta
# Addon Provider: MuadDib

import re, urlparse, urllib, base64

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import cache
from resources.lib.modules import dom_parser2
from resources.lib.modules import source_utils

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['vodly.us', 'vodly.unblocked.tv']
        self.base_link = 'http://vodly.us'
        #self.search_link = '/search?s=%s'
        self.search_link = '%s/search?q=vodly.us+%s+%s'
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
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            result = client.request(url)
            res_chk = re.compile('<title>(.+?)</title>',re.DOTALL).findall(result)[0]
            r = client.parseDOM(result, 'tbody')
            r = client.parseDOM(r, 'tr')
            r = [(re.findall('<td>(.+?)</td>', i)[0], client.parseDOM(i, 'a', ret='href')[0]) for i in r]

            if r:
                for i in r:
                    try:
                        hostchk = i[0]
                        if 'other'in hostchk: continue

                        vid_page = urlparse.urljoin(self.base_link, i[1])
                        html = client.request(vid_page)
                        vid_div = re.compile('<div class="wrap">(.+?)</div>',re.DOTALL).findall(html)[0]
                        vid_url = re.compile('href="(.+?)"',re.DOTALL).findall(vid_div)[0]
                        quality,info = source_utils.get_release_quality(res_chk, vid_url)
                        host = vid_url.split('//')[1].replace('www.','')
                        host = host.split('/')[0].lower()
                        sources.append({
                            'source': host,
                            'quality': quality,
                            'language': 'en',
                            'url':vid_url,
                            'info':info,
                            'direct': False,
                            'debridonly': False
                        })
                    except:
                        pass
            return sources
        except Exception:
            return

    def resolve(self, url):
        if self.base_link in url:
            url = client.request(url)
            url = client.parseDOM(url, 'div', attrs={'class': 'wrap'})
            url = client.parseDOM(url, 'a', ret='href')[0]
        return url