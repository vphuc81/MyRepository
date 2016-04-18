from __future__ import unicode_literals
from resources.lib.modules import client,webutils,convert,constants
import re,urlparse,json,urllib2,cookielib,xbmc,urllib
from resources.lib.modules.log_utils import log



class info():
    def __init__(self):
    	self.mode = 'sport2life'
        self.name = 'life2sport.com'
        self.icon = 'life2sport.jpg'
        self.paginated = True
        self.categorized = False
        self.multilink = True


class main():
	
	def __init__(self,url = 'http://www.life2sport.com/category/basketbol/nba'):
		self.base = 'http://www.life2sport.com/category/basketbol/nba'
		self.url = url

	def items(self):
		html = client.request(self.url)
		soup = webutils.bs(html)
		out=[]
		items = soup.find('div',{'id':'archive-area'})
		items = items.findAll('li')
		for item in items:
			url = item.find('a')['href']
			title = item.find('a')['title']
			title = title.split('/')
			title = '%s (%s)'%(title[-1].strip(),title[-2].strip())
			img = item.find('img')['srcset'].split(',')[0].replace(' 300w','')
			item = (title,url,img)
			out.append(item)

		return out

	def links(self,url, img=' '):
		out=[]
		ref=url
		orig_title = xbmc.getInfoLabel('ListItem.Title')
		html = client.request(url)
		link = re.findall("src='(https://videoapi.my.mail.ru/.+?)'",html)[0]
		link = link.replace('https://videoapi.my.mail.ru/videos/embed/mail/','http://videoapi.my.mail.ru/videos/mail/')
		link = link.replace('html','json')
		cookieJar = cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar), urllib2.HTTPHandler())
		conn = urllib2.Request(link)
		connection = opener.open(conn)
		f = connection.read()
		connection.close()
		js = json.loads(f)
		for cookie in cookieJar:
			token = cookie.value
		js = js['videos']
		for x in js:
			url = x['url'] 
			host  = urlparse.urlparse(url).netloc
			url = url + '|%s'%(urllib.urlencode({'Cookie':'video_key=%s'%token, 'User-Agent':client.agent(), 'Referer':ref, 'Host':host, 'X-Requested-With':constants.get_shockwave()} ))
			title = orig_title + ' ' + x['key']
			out.append((title,url,img))
		return out

	def resolve(self,url):
		# ref=url
		# html = client.request(url)
		# link = re.findall("src='(https://videoapi.my.mail.ru/.+?)'",html)[0]
		# link = link.replace('https://videoapi.my.mail.ru/videos/embed/mail/','http://videoapi.my.mail.ru/videos/mail/')
		# link = link.replace('html','json')
		# cookieJar = cookielib.CookieJar()
		# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar), urllib2.HTTPHandler())
		# conn = urllib2.Request(link)
		# connection = opener.open(conn)
		# f = connection.read()
		# connection.close()
		# js = json.loads(f)
		# for cookie in cookieJar:
		# 	token = cookie.value
		# url = js['videos'][-1]['url'] + '|Cookie=video_key=%s&User-agent=%s&Referer=%s'%(token,client.agent(),ref)
		return url

	def next_page(self):
		html = client.request(self.url)
		try:
			next = re.findall('<a href="(.+?)">Next',html)[0]
		except:
			next = False
		return next


