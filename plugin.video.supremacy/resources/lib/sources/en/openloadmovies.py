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

import re
import urllib
import urlparse
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import proxy


class source:
	def __init__(self):
		self.priority = 1
		self.language = ['en']
		self.domains = ['openloadmovie.org']
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