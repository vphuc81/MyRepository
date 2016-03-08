# -*- coding: utf-8 -*-

import xbmc,  xbmcplugin,  xbmcgui, urllib, sys, os, re
from resources.lib import urlfetch

class viettv24:
	def __init__(self):
		self.session = urlfetch.Session(headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'})

	def fetch(self, url, data=''):
		try:response = self.session.fetch(url, data=data)
		except:response = None
		return response
	
	def get_home(self):
		url='http://www.viettv24.com/main/sub_channels_new.php';items=[];body='';response=self.fetch(url)
		if response and not re.search('id="(\w+?-).+?\'Click\'.{1,5}\'(.+?)\'.+?src="(.+?)"',response.body):
			response=urlfetch.get(url, proxies={'http':'198.169.246.30'})
		if response:body=response.body
		response=self.fetch('http://www.viettv24.com/main/home_new.php')
		if response:body+=response.body
		items=re.findall('id="(\w+?-).+?\'Click\'.{1,5}\'(.+?)\'.+?src="(.+?)"',body);temp=['','','']
		for i in items: 
			if 'Hai' in i[1]:temp[0]=i
			elif 'Dong Giao' in i[1]:temp[1]=i
			elif 'Viet Sun' in i[1]:temp[2]=i
			else:temp.append(i)
		items=[]
		for i in temp:
			if i:items.append(i)
		print items
		return items
		
	def get_link(self,url):
		data={'strname':url}
		response=self.fetch('http://www.viettv24.com/main/getStreamingServerWeb.php?ReturnFormat=json',data=data)
		try:
			js=response.json[0]
			link='%s%s/playlist.m3u8?%s'%(js['streamApp'],js['streamName'],js['key'])
		except:link=''
		return link

def addLink(name,url,img):
	u=os.path.dirname(sys.argv[0])+"?name="+urllib.quote_plus(name)+"&url="+urllib.quote_plus(url.strip())+"&img="+urllib.quote_plus(img)
	item=xbmcgui.ListItem(name, iconImage=img, thumbnailImage=img)
	item.setInfo( type="Video", infoLabels={ "Title": name } )
	item.setProperty('IsPlayable', 'true')
	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
	
def get_params():
	param=[];paramstring=sys.argv[2]
	if len(paramstring)>=2:
		params=sys.argv[2];cleanedparams=params.replace('?','')
		if (params[len(params)-1]=='/'):params=params[0:len(params)-2]
		pairsofparams=cleanedparams.split('&');param={}
		for i in range(len(pairsofparams)):
			splitparams={};splitparams=pairsofparams[i].split('=')
			if (len(splitparams))==2:param[splitparams[0]]=splitparams[1]
	return param

params=get_params();url=name=img=None

try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:img=urllib.unquote_plus(params["img"])
except:pass
print url,name,img


vtv = viettv24()
if not url:
	urlhome='http://www.viettv24.com/main/';items=vtv.get_home()
	if items:
		for id,name,img in items:
			img=urlhome+(urllib.quote(img) if 'product_thumb.php' not in img else img)
			addLink(name,id.strip(),img)
		xbmc.executebuiltin ( 'Container.SetViewMode(500)' )
else:item=xbmcgui.ListItem(path=vtv.get_link(url));xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
xbmcplugin.endOfDirectory(int(sys.argv[1]))
