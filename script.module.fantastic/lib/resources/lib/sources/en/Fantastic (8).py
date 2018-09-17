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

import re,urllib,urlparse,json,base64, random

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser
from resources.lib.modules import log_utils
from resources.lib.modules import debrid



class source:
	def __init__(self):
		self.priority = 1
		self.language = ['en']
		self.domains = ['watchseriesfree.to','seriesfree.to']
		self.base_link = 'https://seriesfree.to/'
		self.search_link = 'https://seriesfree.to/search/%s'
		self.ep_link = 'https://seriesfree.to/episode/%s.html'
		self.max_conns = 10 
		self.min_srcs = 3

	def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
		try:
			url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
			url = urllib.urlencode(url)
			log_utils.log('tvshow url: %s' % url)
			return url
		except:
			failure = traceback.format_exc()
			log_utils.log('WATCHSERIES - Exception: \n' + str(failure))
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
			failure = traceback.format_exc()
			log_utils.log('WATCHSERIES - Exception: \n' + str(failure))
			return


	def sources(self, url, hostDict, hostprDict):
		try:
			sources = []
			if url == None: return sources

			data = urlparse.parse_qs(url)		  
			data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])   
			
			

			req	= '%s s%s e%s' % (data['tvshowtitle'], int(data['season']), int(data['episode']))
			req = req.replace('\'','').lower()
			req = self.ep_link % re.sub('\W+','_',req)

			for i in range(3):
				result = client.request(req, timeout=10)
				if not result == None: break
				
			dom = dom_parser.parse_dom(result, 'div', attrs={'class':'links', 'id': 'noSubs'})
			result = dom[0].content		
			links = re.compile('<i class="fa fa-youtube link-logo"></i>([^<]+).*?href="([^"]+)"\s+class="watch',re.DOTALL).findall(result)
			random.shuffle(links)

			hostDict = hostDict + hostprDict
			
			conns = 0 
			for pair in links:

				if conns > self.max_conns and len(sources) > self.min_srcs: break	 

				

				host = pair[0].strip()	  
				link = pair[1]
				
				
				valid, host = source_utils.is_host_valid(host, hostDict)
			
				if not valid: continue

				link = urlparse.urljoin(self.base_link, link)
				for i in range(2):
					result = client.request(link, timeout=3)
					conns += 1
					if not result == None: break	 
				
				
			
				try:
					link = re.compile('href="([^"]+)"\s+class="action-btn').findall(result)[0]
				except: 
			
					continue
				try:
					u_q, host, direct = source_utils.check_directstreams(link, host)
				except:
					
					continue				
				link, quality = u_q[0]['url'], u_q[0]['quality']

				
				sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'direct': direct, 'debridonly': False})
					
			return sources
		except:
			failure = traceback.format_exc()
			log_utils.log('WATCHSERIES - Exception: \n' + str(failure))
			return sources


	def resolve(self, url):
		return url
