from __future__ import unicode_literals
from resources.lib.modules import client,webutils
import re,urlparse,json,sys,os, json

from addon.common.addon import Addon
addon = Addon('plugin.video.castaway', sys.argv)

AddonPath = addon.get_path()
IconPath = AddonPath + "/resources/media/"
def icon_path(filename):
    return os.path.join(IconPath, filename)

class info():
    def __init__(self):
    	self.mode = 'zizo'
        self.name = 'zizo.entejsites.com (full matches & highlights)'
        self.icon = icon_path('zizo.jpg')
        self.paginated = True
        self.categorized = True
        self.multilink = True


class main():
	def __init__(self,url = 'http://zizo.entejsites.com'):
		self.base = 'http://zizo.entejsites.com'
		self.url = url


	def categories(self):
		cats = [('http://zizo.entejsites.com/category/premier-league-full-matches-online/', 'Premier League', 'http://zizo.entejsites.com/wp-content/uploads/2015/04/barclays-premier-league-fixtures1.jpg'),
				('http://zizo.entejsites.com/category/seria-a-full-matches-online/', 'Seria A','http://zizo.entejsites.com/wp-content/uploads/2015/04/serie-a-27-giornata-risultati-e-classifica_1_big1.jpg'),
				('http://zizo.entejsites.com/category/bundesliga-full-matches-online/','Bundesliga','http://zizo.entejsites.com/wp-content/uploads/2015/04/bundesliga1.png'),
				('http://zizo.entejsites.com/category/la-liga-full-matches-online/', 'La Liga','http://zizo.entejsites.com/wp-content/uploads/2015/04/la-liga-20151.jpg'),
				('http://zizo.entejsites.com/category/champions-league-full-matches-online/', 'Champions League', 'http://zizo.entejsites.com/wp-content/uploads/2015/04/gun__1381310671_uefa_champions_league1.jpg'),
				('http://zizo.entejsites.com/category/europa-league-full-matches-online/','Europa League', 'http://zizo.entejsites.com/wp-content/uploads/2015/04/336792_11-1024x576.jpg')]
		return cats

	def items(self):
		html = client.request(self.url)
		items = re.findall('<div class="entry-thumbnail"><img src\s*="(.+?)" alt="(.+?)">\s*<div class="overlay"></div>\s*<div class="links"><a href="(.+?)" class="link"',html, flags=re.UNICODE)
		out = []
		for item in items:
			img = item[0]
			title = item[1].decode('utf-8').replace('Highlights and Full Match Watch Online','')
			url = item[2]
			out.append((title.encode('utf-8'),url,img))

		return out

	
	def links(self, url):
		out=[]
		html = client.request(url)
		links = re.findall('data-config="(//config.playwire.com/.+?zeus.json)"',html)
		for link in links:
			url = 'http:' + link
			hm = client.request(url)
			title = re.findall('"title"\s*:\s*"(.+?)"',hm)[0]
			img = re.findall('"poster"\s*:\s*"(.+?)"',hm)[0]
			out.append((title,url,img))
		return out




	def resolve(self,url):
		try:
			result = client.request(url)
			js = json.loads(result)
			try:
				f4m=js['content']['media']['f4m']
			except:
				reg=re.compile('"(?:src|f4m)":"https?://(.+?).f4m"')
				f4m=re.findall(reg,result)[0]
				f4m='http://'+pom+'.f4m'

			result = client.request(f4m)
			soup = webutils.bs(result)
			try:
				base=soup.find('baseURL').getText()+'/'
			except:
				base=soup.find('baseurl').getText()+'/'

			linklist = soup.findAll('media')
			choices,links=[],[]
			for link in linklist:
				url = base + link['url']
				bitrate = link['bitrate']
				choices.append(bitrate)
				links.append(url)
				if len(links)==1:
					return links[0]
				if len(links)>1:
					import xbmcgui
					dialog = xbmcgui.Dialog()
					index = dialog.select('Select bitrate', choices)
				if index>-1:
					return links[index]
			return


		except:
			return



	def next_page(self):
		html = client.request(self.url)
		try:
			next = re.findall("<link rel='next' href='(.+?)'",html)[0]
		except:
			next = None
		return next


