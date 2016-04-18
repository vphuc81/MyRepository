from __future__ import unicode_literals
from resources.lib.modules import client, webutils
from resources.lib.modules.log_utils import log
import urllib, requests
import re,sys,xbmcgui,os
from addon.common.addon import Addon
addon = Addon('plugin.video.castaway', sys.argv)


class info():
    def __init__(self):
    	self.mode = 'streamlive'
        self.name = 'Streamlive.to'
        self.icon = 'streamlive.png'
        self.paginated = True
        self.categorized = True
        self.multilink= False


class main():
	def __init__(self, url = 'http://www.streamlive.to/channels/?sort=1'):
		self.base = 'http://www.streamlive.to/'
		self.url = url


	def categories(self):
		html = client.request(self.url)
		soup = webutils.bs(html)
		items = soup.find('select', {'name':'category'}).findAll('option')
		cats = []
		ic = info().icon
		for item in items:
			name = item['value']
			url = self.base + urllib.quote(name)
			if name =='': name = 'All'
			cats.append((url, name, ic))
		return cats



	def channels(self, url):
		self.url = url.replace(' ','%20')
		html = client.request(self.url,referer=self.base)
		channels = webutils.bs(html).findAll('li')
		events = self.__prepare_channels(channels)
		return events

	def __prepare_channels(self,channels):
		new=[]
		for channel in channels:
			try:
				url = channel.find('a')['href']
				img = 'http:' + re.findall('img.+?src="(.+?)"',str(channel.find('img')))[0]
				title = channel.find('img')['alt'].encode('utf-8')
				if 'premium' in channel.getText().lower() and addon.get_setting('streamlive_show_premium')=='false':
					continue
				else:
					new.append((url,title,img))
				
			except:
				pass
		return new

	def next_page(self):
		html = client.request(self.url, headers={'referer':self.base})
		try: 
			next = re.compile('>\s\d+\s<a href="(.+?)">').findall(html)[0]
			return next
		except:
			return




	def resolve(self,url):

		import liveresolver
		return liveresolver.resolve(url)
		