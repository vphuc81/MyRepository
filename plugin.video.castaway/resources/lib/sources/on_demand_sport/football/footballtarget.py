from __future__ import unicode_literals
from resources.lib.modules import client,webutils,convert
import re,urlparse,json,xbmcgui



class info():
    def __init__(self):
    	self.mode = 'footballtarget'
        self.name = 'Footballtarget.com (full matches)'
        self.icon = 'footballtarget.png'
        self.paginated = True
        self.categorized = False
        self.multilink = True


class main():
	def __init__(self,url = 'http://www.footballtarget.com/match-replay/'):
		self.base = 'http://www.footballtarget.com/match-replay/'
		self.url = url

	def items(self):
		html = client.request(self.url)
		html = convert.unescape(html.decode('utf-8'))
		soup = webutils.bs(html)
		items = soup.find('div',{'id':'cat-container'}).findAll('li')
		out = []
		for item in items:
			url = item.find('a')['href']
			title = item.find('a')['title'].replace('Full Match: ','').encode('utf-8', 'xmlcharrefreplace')
			img = item.find('img')['src']
			out.append((title,url,img))

		return out

	def links(self,url):
		html = client.request(url)
		urls = re.findall('(\/\/config\.playwire\.com\/[^\'\"]+)',html)
		i=1
		out=[]
		for url in urls:
			url = 'http:' + url
			title = 'Part %s'%i
			i+=1
			out.append((title,url))
		return out





	def resolve(self,url):
		try:
			result = client.request(url)
			html = result
			result = json.loads(result)
			try:
				f4m=result['content']['media']['f4m']
			except:
				reg=re.compile('"src":"http://(.+?).f4m"')
				f4m=re.findall(reg,html)[0]
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
		soup = webutils.bs(html)
		try:
			next = soup.find('span',{'class':'page-numbers current'}).findNext('a')['href']
		except:
			next = None
		return next


