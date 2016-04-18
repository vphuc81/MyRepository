from __future__ import unicode_literals
from resources.lib.modules import client,webutils, control
import re,urlparse, os, xbmcvfs, urllib, urllib2

torrent_path = os.path.join(control.dataPath, 'myTorrent.torrent')

class info():
    def __init__(self):
    	self.mode = 'torrent'
        self.name = 'Football torrents (full replays)'
        self.icon = 'torrent.png'
        self.paginated = True
        self.categorized = False
        self.multilink = False


class main():
	def __init__(self,url = 'http://www.sport-video.org.ua/americanfootball.html'):
		self.base = 'http://www.sport-video.org.ua/'
		self.url = url

	def items(self):
		html = client.request(self.url)
		out=[]
		items = reversed(re.findall('href="./(.+?[^"\']+)["\']',  html, flags=re.DOTALL))
		for i in items:
			if 'torrent' in i:
				title = i.replace('.torrent','')
				url = self.base + urllib.quote(i)
				out+=[[title,url,info().icon]]

		return out


	




	def resolve(self,url):
		if not xbmcvfs.exists(os.path.dirname(torrent_path)):
			try: xbmcvfs.mkdirs(os.path.dirname(torrent_path))
			except: os.mkdir(os.path.dirname(torrent_path))

		file = urllib2.urlopen(url)
		output = open(torrent_path,'wb')
		output.write(file.read())
		output.close()
		return "plugin://plugin.video.yatp/?action=play&torrent=" + torrent_path



	def next_page(self):
		try:
			page = re.findall('americanfootball(\d+).html',self.url)[0]
			next_page = self.url.replace('americanfootball%s.html'%(page),'americanfootball%s.html'%(int(page)+1))
		except:
			next_page = self.url.replace('americanfootball.html','americanfootball1.html')
		return next_page


