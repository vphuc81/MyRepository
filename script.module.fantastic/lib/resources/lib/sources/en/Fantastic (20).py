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
import re
import urllib
import urlparse
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import proxy
from resources.lib.modules import debrid

class source:
	def __init__(self):
		self.priority = 1
		self.language = ['en']
		self.domains = ['openloadmovie.org','openloadmovie.ws']
		self.base_link = 'https://openloadmovie.org'

	def movie(self, imdb, title, localtitle, aliases, year):
		try:
			title = cleantitle.geturl(title)
			url = self.base_link + '/movies/%s-%s' % (title,year)
			return url
		except:
			return
			
	def sources(self, url, hostDict, hostprDict):
		try:
			sources = []
			r = client.request(url)
			match = re.compile('<iframe class="metaframe rptss" src="(.+?)"').findall(r)
			for url in match: 
				sources.append({'source': 'Openload','quality': 'HD','language': 'en','url': url,'direct': False,'debridonly': False})
		except Exception:
			return
		return sources

	def resolve(self, url):
		return url