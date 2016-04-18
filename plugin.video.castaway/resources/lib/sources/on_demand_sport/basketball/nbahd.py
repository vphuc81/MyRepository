from __future__ import unicode_literals
from resources.lib.modules import client,webutils
from resources.lib.modules.log_utils import log
from random import shuffle
import re,urlparse



class info():
    def __init__(self):
    	self.mode = 'nbahd'
        self.name = 'NBA GO (full replays)'
        self.icon = 'nbastream.png'
        self.paginated = True
        self.categorized = False
        self.multilink = True


class main():
	def __init__(self,url = 'http://nbahd.com'):
		self.base = 'http://nbahd.com'
		self.url = url

	def items(self):
		html = client.request(self.url)
		soup = webutils.bs(html)
		items=soup.findAll('div',{'class':'thumb'})
		out=[]
		for item in items:
			url=item.find('a')['href']
			title=item.find('a')['title'].encode('utf-8')
			thumb=item.find('img')['src'].encode('utf-8')

			out+=[[title,url,thumb]]

		return out

	def links(self,url, img=' '):
		html = client.request(url)
		soup = webutils.bs(html)
		tags=soup.find('div',{'class':'entry-content rich-content'}).findAll('p')
		tags.pop(0)
		out=[]
		tag=tags[0]
		parts=tag.findAll('a')
		i = 1
		for part in parts:
			url = part['href']
			title = 'Part %s'%i
			img = ' '
			i+=1
			out.append((title,url,img))

		if len(out)==0:
			links=re.findall('<p><img src="(.+?)"/>\s*</p>\s*<p>\s*<a href="(.+?)" target="_blank">\s*<img src=".+?"/></a>\s*<a href="(.+?)" target="_blank">\s*<img src=".+?"/></a>\s*<a href="(.+?)" target="_blank">\s*<img src=".+?"/></a>\s*<a href="(.+?)" target="_blank">\s*<img src=".+?"/></a>\s*',html)
			i = 1
			pos = 0
			for link in links:
				img = link[0]
				for i in range(4):
					url = link[i+1]
					title = 'Part %s'%(i+1)
					out.append((title,url,img))


		return out





	def resolve(self,url):
		ref = url
		html=client.request(url)
		urls = re.findall('data-link=[\"\']([^\"\']+)[\"\']',html)
		url = 'http://play.wtutor.net/wp-admin/admin-ajax.php?action=ts-ajax&p=%s&n=1'%urls[0]
		html = client.request(url,referer=ref)
		
		try:
			video = re.findall('file\s*:\s*[\"\']([^\"\']+)[\"\']',html)[0]
		except:
			video = re.findall('src=[\"\']([^\"\']+)[\"\']',html)[0]
		if 'google' in video:
			return video
		else:
			import urlresolver
			return urlresolver.resolve(url)




	def next_page(self):
		html = client.request(self.url)
		soup = webutils.bs(html)
		try:
			next_page=soup.find('div',{'class':'wp-pagenavi'}).find('a',{'class':'nextpostslink'})['href']
		except:
			next_page=None
		return next_page

