from __future__ import unicode_literals
from resources.lib.modules import client,webutils,convert
from resources.lib.modules.log_utils import log
import re,urlparse,json,sys,os, json
import requests

from addon.common.addon import Addon
addon = Addon('plugin.video.castaway', sys.argv)

AddonPath = addon.get_path()
IconPath = AddonPath + "/resources/media/"
def icon_path(filename):
    return os.path.join(IconPath, filename)

class info():
    def __init__(self):
    	self.mode = 'fullmatchesandshows'
        self.name = 'thefootballcouch.com'
        self.icon = icon_path('tfc.png')
        self.paginated = True
        self.categorized = True
        self.multilink = True


class main():
	def __init__(self,url = 'http://thefootballcouch.com'):
		self.base = 'http://thefootballcouch.com'
		self.url = url


	def categories(self):
		cats = [('http://thefootballcouch.com/category/england-football/', 'England', 'http://zizo.entejsites.com/wp-content/uploads/2015/04/barclays-premier-league-fixtures1.jpg'),
				('http://thefootballcouch.com/category/football-italia/', 'Italy','http://zizo.entejsites.com/wp-content/uploads/2015/04/serie-a-27-giornata-risultati-e-classifica_1_big1.jpg'),
				('http://thefootballcouch.com/category/german-league-football-highlights-shows-and-full-matches/','Germany','http://zizo.entejsites.com/wp-content/uploads/2015/04/bundesliga1.png'),
				('http://thefootballcouch.com/category/spanish-football-highlights/', 'Spain','http://zizo.entejsites.com/wp-content/uploads/2015/04/la-liga-20151.jpg'),
				('http://thefootballcouch.com/category/french-football/','France', 'http://worldsoccertalk.com/wp-content/uploads/2013/10/ligue-1-logo.jpg'),
				('http://thefootballcouch.com/category/rest-of-the-world-football-highlights/', 'Rest Of The World', 'http://the9gag.com/images/pictuers/the_football_league_shows.jpg'),
				('http://thefootballcouch.com/category/international-football/', 'International Football', 'http://the9gag.com/images/pictuers/the_football_league_shows.jpg'),
				('http://thefootballcouch.com/category/uefa-highlights/', 'UEFA', 'http://zizo.entejsites.com/wp-content/uploads/2015/04/gun__1381310671_uefa_champions_league1.jpg'),
				('http://thefootballcouch.com/category/football-shows/', 'Football Shows', 'http://www.fullmatchesandshows.com/wp-content/uploads/2015/01/EUROPEAN-FOOTBALL-SHOW.png')
				]
		return cats

	def items(self):
		html = client.request(self.url,referer=self.base)
		html = convert.unescape(html.decode('utf-8'))
		html = client.parseDOM(html,'div', attrs={'class':'wpb_wrapper'})[0]
		items = re.findall('<img width="300" height="160" src="(.+?)" class="entry-thumb.+?">\s*<span class="td-video-play-ico">\s*<img width="40" class="td-retina".+?alt="video"/>\s*</span>\s*</a>\s*</div>\s*</div>\s*<h3 class="entry-title td-module-title" itemprop="name">\s*<a rel="bookmark" href="(.+?)" itemprop="url">(.+?)</a> ',html, flags=re.UNICODE)
		out = []
		for item in items:
			img = item[0]
			title = item[2].encode('utf-8', 'xmlcharrefreplace')
			url = item[1]
			item_x = (title,url,img)
			out.append(item_x)

		return out

	
	def links(self, url):
		out=[]
		html = client.request(url)
		links = re.findall('callvideo\([\'\"](\d+)[\'\"]\)">([^<]+)<',html)
		for link in links:
			urlx = url + '?id=' + link[0]
			title = link[1].upper()
			img = re.findall('class="entry-thumb td-modal-image" src="(.+?)"',html)[0]
			out.append((title,urlx,img))
		return out

	def resolve(self,url):
		ref = url
		headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With':'XMLHttpRequest','Referer':ref, 'Origin':'http://thefootballcouch.com', 'Host':'thefootballcouch.com'}
		s = requests.Session()

		video_id = re.findall('id=(\d+)',url)[0]
		url = url.replace('?id=%s'%video_id,'')
		html = client.request(url)
		post_id = re.findall("action: 'playwirevideos',\s*postid:[\'\"](.+?)[\'\"]",html)[0]
		post_data = "action=playwirevideos&postid=%s&serialid=%s"%(post_id,video_id)
		result = s.post('http://thefootballcouch.com/wp-admin/admin-ajax.php', data=post_data, headers=headers).content
		url = 'http:' + re.findall('(\/\/config\.playwire\.com\/[^\'\"]+)',result)[0]


		result = client.request(url)
		result = json.loads(result)
		try:
			f4m=result['content']['media']['f4m']
		except:
			reg=re.compile('"src":"(http://.+?.f4m)"')
			f4m=re.findall(reg,html)[0]
			

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

	def next_page(self):
		
		try:
			html = client.request(self.url)
			soup = webutils.bs(html)
			next = soup.find('a',{'class':'last'}).findNext('a')['href']
		except:
			next = None
		return next

#<a href="#" class="td-ajax-next-page" id="next-page-td_uid_1_56cadcda8cbf3" data-td_block_id="td_uid_1_56cadcda8cbf3">