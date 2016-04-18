from __future__ import unicode_literals
from resources.lib.modules import client,webutils,convert
import re,urlparse,json



class info():
    def __init__(self):
    	self.mode = 'fullmatchtv'
        self.name = 'fullmatchtv.com '
        self.icon = 'fullmatchtv.png'
        self.paginated = False
        self.categorized = False
        self.multilink = False


class main():
	
	def __init__(self,url = 'http://fullmatchtv.com/football'):
		self.base = 'http://fullmatchtv.com'
		self.url = url

	def items(self):
		html = client.request(self.url)
		html = convert.unescape(html.decode('utf-8'))
		items = re.findall('<div class="td-module-thumb"><a href="(.+?)" rel="bookmark" title="(.+?)"><img.+?class="entry-thumb" src="(.+?)"',html)
		out = []
		urls=[]
		for item in items:
			url = item[0]
			title = item[1].encode('utf-8', 'xmlcharrefreplace')
			img = item[2]
			
			item = (title,url,img)
			if url not in urls:
				urls+=[url]
				out.append(item)

		return out

	def resolve(self,url):
		html = client.request(url)
		urls = re.findall('<iframe.+?src=[\'"](.+?)[\'"]',html)
		import urlresolver
		for url in urls:
			resolved = urlresolver.resolve(url)
			if resolved:
				return resolved
				break

