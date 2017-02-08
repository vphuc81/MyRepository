# -*- coding: utf-8 -*-

import urllib,urllib2, re, os, json, xbmc
from common import Paths
mycacheDir = Paths.cacheDir

def linkValid(item,hd={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	def check(url):
		req=urllib2.Request(url,data,hd)
		try:b=urllib2.urlopen(req,timeout=timeout);link=b.geturl();b.close()
		except:link=''
		return link
	link=''
	if type(item) in (str,unicode):link=check(item)
	elif type(item)==list:
		try:
			for href,title in item:
				link=check(href)
				if link:break
		except:infoDialog('**Link checked fail!','[COLOR red]linkValid[/COLOR]', time=3000)
	return link

def pacget(url,hd={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	try:res=urllib2.urlopen(urllib2.Request(url,data,hd),timeout=timeout)
	except:res=None
	return res

def pacsearch(pattern,string,group=1,flags=0,result=''):
	try:s=re.search(pattern,string,flags).group(group)
	except:s=result
	return s

def pacrw(fn,s='',a='w'):
	if len(fn) < 20:fn=os.path.join(mycacheDir,fn)
	try:
		if s and a=='w':s=s.replace('\r\n','\n');f=open(fn,a);f.write(s)
		elif s:f=open(fn,a);f.write(s)
		else:f=open(fn);s=f.read().replace('\r\n','\n')
		f.close()
	except:s=''
	return s
	
def pacread(url,headers={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	req=urllib2.Request(url,data,headers)
	try:
		res=urllib2.urlopen(req, timeout=timeout)
		hd=dict(res.headers.items())
		cookie=hd.get('set-cookie','')
		encoding=hd.get('content-encoding','')
		if encoding=='gzip':
			import StringIO,gzip
			buf=StringIO.StringIO(res.read())
			f=gzip.GzipFile(fileobj=buf)
			b=f.read()
		else:b=res.read()
		res.close()
	except:b=''
	return b

class vtvgovn:
	def __init__(self):
		self.hd={'User-Agent':'Mozilla/5.0','Cookie':pacrw('vtvgo.cookie')}
		self.urlhome='http://vtvgo.vn/'

	def liveGoList(self,url):
		def e(i):return i.get('name').encode('utf-8'),i.get('id').encode('utf-8'),i.get('thumbnailUrl').encode('utf-8')
		b=pacread(url,self.hd)
		try:j=json.loads(b)
		except:j=[{},[]]
		return [e(i) for i in j[1]]
	
	def vodList(self,url):
		def e(i):return i.get('name').encode('utf-8'),i.get('downloadUrl').encode('utf-8'),i.get('thumbnailUrl').encode('utf-8')
		b=pacread(url,self.hd)
		try:j=json.loads(b)
		except:j=[{},[]]
		return [e(i) for i in j[1]]
	
	def liveList(self):
		def detail(s):return pacsearch('title="(.+?)"',s),pacsearch('href="(.+?)"',s),pacsearch('src="(.+?)"',s)
		b=pacget(self.urlhome)
		if b and b.getcode()==200:
			pacrw('vtvgo.cookie',b.headers.get('Set-Cookie'));b=b.read()
			if pacsearch("else window.location.href = '(.+?)'",b):
				b=pacread(pacsearch("else window.location.href = '(.+?)'",b))
		else:b=''
		
		title=pacsearch('title content="(.+?)"',b)
		href=pacsearch('url content="(.+?)"',b)
		img=pacsearch('image content="(.+?)"',b)
		items=[self.detail(i) for i in b.split('class="item"') if 'class="play-icon"' in i]
		if href!="http://vtvgo.vn/" and href not in items:items.append((title,href,img))
		return sorted(items, key=lambda k: k[1])
	
	def live(self,id):
		url='http://vtvgo.vn/get-program-channel?epg_id=%s&type=1'%id
		try:link=json.loads(pacread(url,self.hd)).get('data','')
		except:link=''
		print link
		return link

	def getStream(self,url):
		stream = ""
		try:
			id=pacsearch('-(\d+)\.html',url)
			if id =="": id = "3"
			stream = self.live(id)
			xbmc.sleep(3)
		except: pass
		return stream
		
	def getStreamTvnet(self,id):
		stream = ""
		token = ".smil&t=l"
		chid = ["vtv1","vtv2","vtv3","vtv4","ttxvn","htv9","vtc1","vtc10","vtc16","hn1"]
		jsonHost = "http://118.107.85.21:1337/get-stream.json?p=smil:"
		if id in chid:
			try:
				url = jsonHost + id + token
				req = urllib2.urlopen(url)
				req = json.load(req)
				stream = req[1]["url"]
				#stream = req[0]["url"]
			except: pass			
		return stream
	
	def detail(self,s):
		title=pacsearch('title="(.+?)"',s)
		if not title:title=pacsearch('alt="(.+?)"',s)
		href=pacsearch('href="(.+?)"',s)
		img=pacsearch("data-bg='(.+?)'",s)
		if not img:img=pacsearch('src="(.+?)"',s)
		return title,href,img

		