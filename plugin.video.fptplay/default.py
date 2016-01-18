# -*- coding: utf-8 -*-

'''
Copyright (C) 2014                                                     

This program is free software: you can redistribute it and/or modify   
it under the terms of the GNU General Public License as published by   
the Free Software Foundation, either version 3 of the License, or      
(at your option) any later version.                                    

This program is distributed in the hope that it will be useful,        
but WITHOUT ANY WARRANTY; without even the implied warranty of         
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          
GNU General Public License for more details.                           

You should have received a copy of the GNU General Public License      
along with this program. If not, see <http://www.gnu.org/licenses/>  
'''                                                                           

import urllib,urllib2,re,os,json
import xbmcplugin,xbmcgui,xbmcaddon

addon = xbmcaddon.Addon(id='plugin.video.fptplay')
profile = addon.getAddonInfo('profile')
home = addon.getAddonInfo('path')

homeUrl = 'http://fptplay.net/livetv'
getUrl = 'http://fptplay.net/show/getlinklivetv?id=%s&type=newchannel&quality=1&mobile=web'

dict = {'&amp;':'&', '&acirc;':'â', '&Aacute;':'Á', '&agrave;':'à', '&aacute;':'á', '&atilde;':'ã', '&igrave;':'ì', '&iacute;':'í', '&uacute;':'ú', '&ugrave;':'ù', '&oacute;':'ó', '&ouml;':'ö', '&ograve;':'ò', '&otilde;':'õ', '&ocirc;':'ô', '&Ocirc;':'Ô', '&eacute;':'é', '&egrave;':'è', '&ecirc;':'ê', '&Yacute;':'Ý', '&yacute;':'ý', "&#039;":"'"}

def main():
    content = make_request(homeUrl)
    match = re.compile('<a class="tv_channel.+?".+?title="([^>]+)".+?onclick=".+?".+?data-href="([^"]*)".+?>\s*\s*<img class="lazy" data-original="([^"]*)".+?/>\s*</a>').findall(content)
    for title, url, thumb in match:
        title = replace_all(title, dict)	
        addLink( title, url, 100, thumb)		
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(52)')  
    else:
        xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
		
def resolveUrl(url):
	params = url.split('/')
	id = params[len(params) - 1]
	data = { 'id':id, 'quality': addon.getSetting('quality'), 'mobile':'web'}
	content = make_request(getUrl,data)
	jsonObject = json.loads(content)
	mediaUrl = jsonObject['stream']
	item = xbmcgui.ListItem(path = mediaUrl)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)		
	return    		
		
def make_request(url, params=None, headers=None):
    if headers is None:
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        		   'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        		   'X-Requested-With': 'XMLHttpRequest',
                   'Referer' : 'http://fptplay.net'}
    try:
    	if params is not None:
    		params = urllib.urlencode(params)
        req = urllib2.Request(url,params,headers)
        f = urllib2.urlopen(req)
        body=f.read()
        return body
    except:
    	pass

def replace_all(text, dict):
	try:
		for a, b in dict.iteritems():
			text = text.replace(a, b)
		return text
	except:
		pass
		
def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name})
    liz.setProperty('mimetype', 'video/x-msvideo')
    liz.setProperty("IsPlayable","true")
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=False)
    return ok 
	  	
def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]
    return param
   
params=get_params()
url=None
name=None
mode=None
iconimage=None

try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:mode=int(params["mode"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass

if mode==None or url==None or len(url)<1:main()
elif mode==100:
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('FPTPlay', 'Đang tải. Vui lòng chờ trong giây lát...')
    resolveUrl(url)
    dialogWait.close()
    del dialogWait
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))