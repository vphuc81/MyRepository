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

import urllib,urllib2,re,os,sys,json,base64
import xbmcplugin,xbmcgui,xbmcaddon,xbmc
import autorun, visitor
from BeautifulSoup import BeautifulSoup

addon = xbmcaddon.Addon(id='plugin.video.itvplus')
profile = addon.getAddonInfo('profile')
home = addon.getAddonInfo('path')
icon = xbmc.translatePath( os.path.join( home, 'icon.png' ))
dataPatch = xbmc.translatePath(os.path.join(home, 'resources')) 
logos = xbmc.translatePath(os.path.join(dataPatch, 'logos\\'))
fanart = xbmc.translatePath(os.path.join(dataPatch, 'art\\'))
template = xbmc.translatePath(os.path.join(fanart, "temp.jpg"))
remote = addon.getSetting('remote_patch')
local = addon.getSetting('local_patch')
Temp_mode = addon.getSetting('temp_mode')
OO0OO0O0O0 = addon.getSetting('name_account')
O00OO0O0O0 = addon.getSetting('pass_account')
O00OO0OOO0 = addon.getSetting('use_fanart')


dict = {'&amp;':'&', '&acirc;':'â', '&Aacute;':'Á', '&agrave;':'à', '&aacute;':'á', '&atilde;':'ã', '&igrave;':'ì', '&iacute;':'í', '&uacute;':'ú', '&ugrave;':'ù', '&oacute;':'ó', '&ouml;':'ö', '&ograve;':'ò', '&otilde;':'õ', '&ocirc;':'ô', '&Ocirc;':'Ô', '&eacute;':'é', '&egrave;':'è', '&ecirc;':'ê', '&Yacute;':'Ý', '&yacute;':'ý', "&rsquo;":"'", '&quot;':'"','m34':'m22', 'm35':'m22', '4.bp.blogspot.com':'lh3.googleusercontent.com', '3.bp.blogspot.com':'lh3.googleusercontent.com', '2.bp.blogspot.com':'lh3.googleusercontent.com', '1.bp.blogspot.com':'lh3.googleusercontent.com', 'http://www.youtube.com/watch?v=':'plugin://plugin.video.youtube/play/?video_id=', 'https://www.youtube.com/watch?v=':'plugin://plugin.video.youtube/play/?video_id='}

reg = '|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0'

def replace_all(text, dict):
	try:
		for a, b in dict.iteritems():
			text = text.replace(a, b)
		return text
	except:
		pass

def read_file(file):
	try:
		f = open(file, 'r')
		content = f.read()
		f.close()
		return content	
	except:
		pass		

def notify():
    wdlg = xbmcgui.WindowDialog()
    img = xbmcgui.ControlImage( 0, 0, 1280, 720, template)
    wdlg.addControl(img)
    wdlg.doModal()
		
def III():
    O000O0OOO0 = addon.getSetting('view_mode')
    if O000O0OOO0 == 'List':
      try:  
        xbmc.executebuiltin('Container.SetViewMode(502)')
      except:
	    pass
    elif O000O0OOO0 == 'Thumbnails':  
      try:  
        xbmc.executebuiltin('Container.SetViewMode(500)')
      except:
	    pass

def alert(message,title="Thông báo!"):
    xbmcgui.Dialog().ok(title,"",message)		

def notification(message, timeout=10000):
    xbmc.executebuiltin((u'XBMC.Notification("%s", "%s", %s, %s)' % ('Super Movies', message, icon, timeout)).encode("utf-8"))

def I1iI1(object,group):
	return object.group(group) if object else ''	
	
def OOo000():
    if Temp_mode == 'true':
        if os.path.exists(template):
            notify()

    url = IIiIiII11i
    content = makeRequest(I1IiiI(url))
    match = re.findall('<channel>\s*<name>(.+?)</name>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>',I1IiiI(content))
    for iII111ii,iiIi,thumbnail in match:
	    addDir(iII111ii,url,iiIi,logos+thumbnail,fanart+'main.jpg')
    III()
    if 9 - 9: i111IiI + iIIIiI11 . iII111ii
		
def Ii11I1Ii(name,url):
    name = name
    content = makeRequest(I1IiiI(url))
    match = re.findall('<channel>\s*<name>' + name + '</name>((?s).+?)</channel>',I1IiiI(content))
    for O00o in match:
        item = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>').findall(O00o)
        for title, url, iiIi, thumbnail in item:		
            addDir(title,url,iiIi,thumbnail,fanart+'cat2.jpg')
    III()
    if 20 - 20: Ooooo0Oo00oO0 % OooO0o0Oo . O00 % iII11i

def Ii11I(name):
    if 'PHIM TRUYỆN' in name:
        content = makeRequest(I1IiiI(IIiIiiI11i))
        match = re.findall('<server>\s*<name>(.+?)</name>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>',I1IiiI(content))
        for iIIIiI11,iiIi,thumbnail in match:
	        addDir(iIIIiI11,IIiIiiI11i,iiIi,thumbnail,fanart+'main.jpg')
    elif 'MY TUBE' in name:
        content = makeRequest(I1IiiI(IIiIIiI11i))
        match = re.findall('<channel>\s*<name>(.+?)</name>\s*<thumbnail>(.*?)</thumbnail>',I1IiiI(content))
        for iII111ii,thumbnail in match:
	        addDir(iII111ii,IIiIIiI11i,16,thumbnail,fanart+'main.jpg')
    elif 'GÓC CỦA BÉ' in name:
        content = makeRequest(I1IiiI(IiIiIiI11i))
        match = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>').findall(content)
        for title,url,iiIi,thumbnail in match:
	        addDir(title,url,iiIi,thumbnail,fanart+'main.jpg')
    elif 'VUI TẾT' in name:
        content = makeRequest(I1IiiI(IiIIIiI11i))
        match = re.compile('<channel>\s*<name>(.+?)</name>\s*<thumbnail>(.*?)</thumbnail>').findall(content)
        for iII111ii,thumbnail in match:
	        addDir(iII111ii,IiIIIiI11i,17,thumbnail,fanart+'2016.jpg')
    III()	
    if 16 - 16: iIIIiI11 % OooO0o0Oo . O00 % iII111ii
	
def iii1Ii11ii(name,url):	
    name = name
    content = makeRequest(I1IiiI(url))
    match = re.findall('<server>\s*<name>' + name + '</name>((?s).+?)</server>',I1IiiI(content))	
    for O00o in match:
            item = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>').findall(O00o)
            for title, url, iiIi, thumbnail in item:		
                addDir(title,url,iiIi,logos+thumbnail,fanart+'cat2.jpg')				
    III()
    if 10 - 10: I111IiIi + oO0o0ooO0
	
def I1ii11iIi11i(url):
    if '.m3u' in url:
        OoI1Ii11I1I = makeRequest(url)	
        match = re.compile('#EXTINF.+,(.+)\s(.+?)\s').findall(OoI1Ii11I1I)
        for name,url in match:
	        addLink( name.replace('TVSHOW - ','').replace('MUSIC - ',''), url, 100, iconimage)
    elif '.txt' in url:
        OoI1Ii11I1I = makeRequest(url)	
        match = re.compile('"channelName": "(.+?)",\s*"channelNo": "(\d+)",\s*"channelURL": "(.+?)",').findall(OoI1Ii11I1I)
        for name,no,url in match:
	        addLink( no + ' . '  +name, url, 100, 'http://truyenhinhfpthanoi.com/uploads/logo.png')
    xbmc.executebuiltin('Container.SetViewMode(502)')			
    if 37 - 37: ooo / II1Ii11 % O0Oooo00 - OOO0Ooo
    if 90 - 90: i11iIiiIii11 . oo / iii1II11ii * Oooo % iiIIIII1i1iI111 % OOO0O
		
def I1Ii11iIi11i(name,url):
    name = name	
    OoI1Ii11I1Ii1i = makeRequest(url)
    match = re.compile('<channel>\s*<name>' + name + '</name>((?s).+?)</channel>').findall(OoI1Ii11I1Ii1i)
    for O00o in match:	
        item = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>').findall(O00o)
        for title,url,thumbnail in item:
	        if '/channel/' in url or '/user/' in url:
	            addDir( title, url, '', thumbnail, fanart+'cat2.jpg')
	        else:
	            addLink( title, url, 100, thumbnail)
    III()
    if 95 - 95: II1Ii . OOO0O
    if 78 - 78: OOO0O - O0o00 * i11iII1iiI + ii1II11I1ii1I + o0ooo + o0ooo
	
def I1II11iII11i(name,url):
    name = name	
    OoI1Ii11I1Ii1i = makeRequest(I1IiiI(url))
    match = re.findall('<channel>\s*<name>' + name + '</name>((?s).+?)</channel>',I1IiiI(OoI1Ii11I1Ii1i))
    for O00o in match:	
        item = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>').findall(O00o)
        for title,url,thumbnail in item:
	        addDir( title, url, '', thumbnail, fanart+'cat2.jpg')			
    III()
    if 100 - 100: i11iIiiIii / iI1Ii11111iIi % I111IiIi - oO0o0ooO0 / iiIIIII1i1iI

def I1II11iiI11i(name,url):
    name = name	
    OoI1Ii11I1Ii1i = makeRequest(I1IiiI(url))
    match = re.compile('<channel>\s*<name>' + name + '</name>((?s).+?)</channel>').findall(OoI1Ii11I1Ii1i)
    for O00o in match:	
        item = re.compile('<title>(.*?)</title>\s*<link>(.*?)</link>\s*<mode>(.*?)</mode>\s*<thumbnail>(.*?)</thumbnail>').findall(O00o)
        for title,url,iiIi,thumbnail in item:
	        addLink( title, url, iiIi, thumbnail)
    III()	
    if 16 - 16: i11iIiiIii / iI1Ii11111iIi % I111IiIi - oO0o0ooO0 / iiIIIII1i1iI
	
def I1Ii11iII11i(url):
    OoI1Ii11I1Ii1i = makeRequest(url)
    match = re.compile('<channel>\s*<name>(.+?)</name>\s*<thumbnail>(.*?)</thumbnail>').findall(OoI1Ii11I1Ii1i)
    for iII111ii, thumbnail in match:
	    addDir( iII111ii, url, 5, thumbnail, fanart+'cat2.jpg')		
    III()
    if 52 - 52: O0Oooo00 + II1Ii - i11iII1iiI / ii1II11I1ii1I + iii1II11ii . oOo0O0Ooo
    if 63 - 63: O0o00 - Oooo - Oooo
		
def iI1Ii11111iIi(name,url):
    if 'TIVI XEM LẠI' in name:
        content = makeRequest(tvreplay)
        match = re.compile('href="(\d+)/">(\d+)/<').findall(content)
        for url,name in match:
            namey = name[:4]
            namet1 = name[4:]
            namet = namet1[:2]
            namen = name[6:]
            time = '[COLOR blue]'+ namen + '[/COLOR]' + ' - ' + '[COLOR gold]'+ namet + '[/COLOR]' + ' - ' + '[COLOR red]'+ namey + '[/COLOR]'
            addDir( time, tvreplay+url, 10, iconimage, fanart+'cat2.jpg')
    elif 'woim' in url:
        content = makeRequest(url)
        match=re.compile('<li>\s*<a href="([^"]*)" title="([^"]+)".+?src="(.+?)&w').findall(content)
        for url,name,thumb in match:
            addDir( '[COLOR red]Album[/COLOR] : ' + name, url, 10, thumb, fanart+'cat2.jpg')
    elif 'chiasenhac' in url:
        content = makeRequest(url)
        match=re.compile("<a href=\"hd(.+?)\" title=\"([^\"]*)\"").findall(content)[1:8]
        for url,name in match:
	        addDir(name.replace('Video','[COLOR ffff0000]Video[/COLOR]'),csn+'hd'+url, 10,iconimage, fanart+'cat2.jpg')
    elif 'nhaccuatui' in url:
        content = makeRequest(nct+'mv.html')
        match=re.compile("href=\"http:\/\/m.nhaccuatui.com\/mv\/(.+?)\" title=\"([^\"]*)\"").findall(content)[:23]
        for url,name in match:		
            if 'Cách Mạng' in name:pass
            else:addDir( name, nct+'mv/'+url, 10, iconimage, fanart+'cat2.jpg')
    elif 'f.vp9.tv' in url:
        content = makeRequest(url)
        match=re.compile('href="(.*?)">(.*?)/<').findall(content)[1:]
        for url,name in match:
            name=name.replace('nhac_au_my','Nhạc Âu Mỹ').replace('nhac_han','Nhạc Hàn').replace('nhac_tre','Nhạc Trẻ').replace('nhac_vang','Nhạc Vàng').replace('thieu_nhi','Nhạc Thiếu Nhi').replace('tru_tinh','Nhạc Trữ Tình')
            if 'music_channel' in name:pass
            else:addDir( name, vmusic + url, 10, iconimage, fanart+'cat2.jpg')
    elif 'phim3s' in url:
        content = makeRequest(url)
        match = re.compile('<div class="inner"><a href="(.+?)" title="(.+?)"><img src="(.+?)".+?</a><div class="info">.+?</a>(.+?)</div>').findall(content)
        for url, title, thumbnail, year in match:
	        addDir( title + ' ' + year, phim3s + url + 'xem-phim/', 9, thumbnail, thumbnail)
        match = re.compile('<span class="item"><a href="(.+?)">(.+?)</a>').findall(content)
        for url, page in match:
            if page == 'Next':
	            addDir( '[COLOR red]Trang Tiếp Theo >>>[/COLOR]', phim3s + url, 7, logos+'NEXT.png','')
    elif 'phimhd365' in url:
        content = makeRequest(url)
        match=re.compile('<a data-tooltip=".+?" href="(.+?)">\s*<img alt="(.+?)" src="/template/img/grey.gif" class="lazy" data-original="(.+?)" width="140" height="190">').findall(content)
        for url, name, thumbnail in match:
	        name=name.split('-')
	        name = name[0] + ' [COLOR lime]-[/COLOR] ' + '[COLOR orange]' + name[-1] + '[/COLOR]'
	        name = replace_all(name, dict)		
	        addDir(name,phimhd365+url,10,thumbnail,thumbnail)
        match=re.compile('<a class="next page-numbers" href="\s*(.+?)">&rsaquo;</a>').findall(content)[1:2]
        for url in match:
	        addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',phimhd365+url,7,logos +'NEXT.png','')
    elif 'phimgiaitri' in url:
        content = makeRequest(url)	
        match = re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font><br \/><font style.+?#F63\'>(.+?)</font>').findall(content)
        for url,thumbnail,name,oname in match:
            addLink(name+' - '+oname,pgt+url+'/Tap-1.html',100,pgt+thumbnail)
        match = re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)</b>').findall(content)
        for url,thumbnail,name in match:
            addLink(name,pgt+url+'/Tap-1.html',100,pgt+thumbnail)	
        match = re.compile('<a href="(.+?)">>').findall(content)[0:1]
        for url in match:
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',pgt+url.replace(' ','%20'),7,logos + 'NEXT.png','')
    elif 'hplus.com.vn' in url:
        content = makeRequest(url)
        match=re.compile('<a class="tooltips" href=".+?" style=".+?url\(\'(.+?)\'\)" data-content-tooltips=".+?">\s*.+?\s*</div>\s*<h3>\s*<a href="(.+?)">(.+?)<').findall(content)
        for thumbnail,url,name in match:
	        addDir(name,hplus+url,10,thumbnail+'?.png',thumbnail)
        match = re.compile('<div class="next button"><a href="(.+?)">&nbsp;</a></div>').findall(content)
        for url in match:
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',url,7,logos + 'NEXT.png','')
    elif 'phimtienganh' in url:
        content = makeRequest(url)
        match = re.compile('href="(.+?)" >\s*<img src="(.+?)"\s*alt="(.+?)"').findall(content)
        for url, thumbnail, name in match:
            addDir(name, url, 10, thumbnail, thumbnail)
        match = re.compile('href="(.+?)">(.+?)<').findall(content)
        for url, page in match:
            if page=='&gt;':
                addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', url.replace('amp;',''), 7, logos+'NEXT.png','')
    elif 'kephim' in url:
        content = makeRequest(url)
        match=re.compile('<a class="movie-item m-block" href="(.+?)" title="(.+?)"><div class="block-wrapper"><div class=".+?"><div class=".+?"><span class=".+?"><span class=".+?">(.+?)</span></span><img src="(.+?)"').findall(content)
        for url, title, res, thumbnail in match:
	        addDir(title.replace("&#39","'")+' [COLOR green]< '+res+' >[/COLOR]',url,10, thumbnail, thumbnail)
        match=re.compile("<a title='(.+?)' href='(.+?)'>").findall(content)[5:6]
        for title, url in match:
	        addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',kphim+url,7,logos+'NEXT.png','')
    elif 'xuongphim' in url:
        if '?' in url:
            url = url.split('?')[0]
            content = makeRequest(url)
            match = re.compile('<a href="(.+?)" .+? src="(.+?)" .+? alt="(.+?)"></span>').findall(content)
            for url, thumbnail, name in match:
                name = replace_all(name, dict)
                addDir( name, xuongphim + url, 10, thumbnail, thumbnail)
        else:
            content = makeRequest(url)
            match = re.compile('<a href="(.+?)" class="jt bxitem-link" data-jtip=".+?">\s*.+?\s*<span class=".+?">\s*<img src="(.+?)".+?alt="(.+?)">').findall(content)
            for url, thumbnail, name in match:
	            name = replace_all(name, dict)
	            addDir( name, xuongphim + url, 10, thumbnail, thumbnail)
            match=re.compile('<a rel=".+?" href="(.+?)">(.+?)</a>').findall(content)
            for url, page in match:
                if page == 'Next':
	                addDir( '[COLOR red]Trang Tiếp Theo >>>[/COLOR]', xuongphim + url, 7, logos+'NEXT.png','')
    elif 'phim.clip' in url:
        content = makeRequest(url)
        match = re.compile('<a href="(.+?)" class="item">\s*.+?\s*<div class=".+?" data-title="(.+?)" data-title-o=".+?" .+? data-year="(.+?)" .+?">\s*.+? src="(.+?)"').findall(content)
        for url, title, year, thumbnail in match:
	        addDir(title + ' - ' + year, phimclip+url, 10, thumbnail, thumbnail)
        match = re.compile('<li class="next"><a href="/(.+?)">.+?</a></li>').findall(content)
        for url in match:
	        addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', phimclip+url, 7,logos+'NEXT.png','')
    elif 'ssphim' in url:
        content = makeRequest(url)	
        match=re.compile('<a href="(.+?)" title=".+?">\s*<div class=".+?">\s*<h4>.+?</h4>\s*.+?\s*.+?\s*</div>\s*<img class="img-thumbnail" src="(.+?)" alt="(.+?)">\s*</a>').findall(content)
        for url, thumbnail, name in match:
	        thumbnail = thumbnail.replace(' ','%20')
	        name = name.split('-')
	        name = '[COLOR FF0084EA]' + name[0] + '[/COLOR]' + ' [COLOR gold]-[/COLOR] ' +  name[-1]
	        addDir(name, url, 10, thumbnail, thumbnail)
        match = re.compile('<a href="(.+?)"><i class="fa fa-angle-double-right"></i></a>').findall(content)
        for url in match:
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', url, 7, logos+'NEXT.png','')
    elif 'phim7' in url:
        content = makeRequest(url)
        match = re.compile('href="(.+?)" title="(.+?)"><span class="poster">\s*<img src=".+?" alt="" />\s*<img class=".+?" src=".+?" data-original="(.+?)"').findall(content)
        for url, name, thumbnail in match:
            addDir(name, phim7 + url.replace('/phim/', '/xem-phim/'), 9, replace_all(thumbnail, dict), thumbnail)
        match = re.compile("<a href='(.+?)' >&#187;&#187;</a>").findall(content)		
        for url in match:
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', phim7 + url, 7, logos + 'NEXT.png','')
    elif 'megabox' in url:
	    content = makeRequest(url)
	    match = re.compile('src="(.+?)">\s*.*<span class="features">\s*</span>\s*</a>\s*<div class="meta">\s*<h3 class="H3title">\s*<a href="(.+?)">(.+?)</a>').findall(content)
	    for thumbnail, href, title in match:
	        if 'phim-bo' in url:
		        addDir(title, href, 10, thumbnail, thumbnail)
	        else:	
		        try:
		            addLink(title, href, 100, thumbnail)
		        except: 
		            pass
	    try:	
	        match = re.compile('class="next"><a href="(.+?)">').findall(content)
	        addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', 'http://phim.megabox.vn/' + match[0], 7, logos + 'NEXT.png','')	
	    except: 
	        pass
    III()			
    if 39 - 39: i11iII1iiI
    if 89 - 89: I111IiIi . i11iIiiIii - ii1II11I1ii1I

def II1Ii11111iIi(url):
    content = makeRequest(url)
    match = re.compile("<a style='text-decoration:none' href='(.+?).html'>\s*<img style='.+?' src=(.+?) ><div class='text'>\s*<p>(.+?)</p>\s*</div><table style='.+?'><tr><td style='.+?'><b><font style='.+?:0px'>(.+?)\s*</font><br /><font style='.+?:#F63'> (.+?)</font>").findall(content)  
    for url,thumbnail,epi,name,oname in match:
        addDir(name+' - '+oname+' '+'[COLOR green]'+epi+'[/COLOR]',pgt+url+'/Tap-1.html',10,pgt+thumbnail,pgt+thumbnail)
    match = re.compile("<a style='text-decoration:none' href='(.+?).html'>\s*<img style='.+?' src=(.+?) ><div class='text'>\s*<p>(.+?)</p>\s*</div><table style='.+?'><tr><td style='.+?'><b><font style='.+?:0px'>(.+?)</b>").findall(content)  
    for url,thumbnail,epi,name in match:	
        addDir(name+'[COLOR green]'+epi+'[/COLOR]',pgt+url+'/Tap-1.html',10,pgt+thumbnail,pgt+thumbnail)	
    match = re.compile('<a href="(.+?)">>').findall(content)[0:1]
    for url in match:
        addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',pgt+url.replace(' ','%20'),8,logos + 'NEXT.png','')
    III()
    if 73 - 73: Oooo / I1ii11iIi11i - i11iII1iiI - oo
	
def II1ii11111iIi(url):
    if 'phim3s' in url:
        content = makeRequest(url)
        match = re.compile('<div class="server"><div class="label"><i></i>(.+?)</div><ul class="episodelist">').findall(content)
        for server in match:
	        addDir( server, url, 10, iconimage, iconimage)
    elif 'phim7' in url:
        content = makeRequest(url)
        match = re.compile('<p class=".+?"><b>(.+?)</b>').findall(content)
        for server in match:
	        addDir(server, url, 10, iconimage, iconimage)	
    III()
    if 56 - 56: OoooOOOOOOoo / I1ii11iIi11i - i11iII1iiI - IIII
	
def Ii1ii11111IIi(url,name,iconimage):
    content = makeRequest(url)
    if 'wezatv' in url:
        match=re.compile('<div class="tv"><a href="(.+?)" title="(.+?)"><img src="../(.+?)".+?</div>').findall(content)
        for href, title, thumb in match:
            title = href.split('/')[-1]
            title = title.replace('.php','').replace('channel','')
            addLink( title.upper(), href, 100, 'http://www.wezatv.com/' + thumb)
    elif 'tvcatchup' in url:
        match=re.compile('href="(.+?)">(.+?)\.mp4</a>(.+?)\n').findall(content)
        for href, name, info in match:
            name = name.split('-')[0]
            nname = name.replace('ANTV','[COLOR red]ANTV[/COLOR]').replace('TODAYTV','[COLOR orange]TODAYTV[/COLOR]').replace('STARWORLDHD','[COLOR violet]STARWORLDHD[/COLOR]').replace('STARMOVIESHD','[COLOR gold]STARMOVIESHD[/COLOR]').replace('HTV9','[COLOR green]HTV9[/COLOR]').replace('THVL1','[COLOR cyan]THVL1[/COLOR]').replace('VTV1','[COLOR crimson]VTV1[/COLOR]').replace('VTV2','[COLOR yellowgreen]VTV2[/COLOR]').replace('VTV3','[COLOR deeppink]VTV3[/COLOR]').replace('VTV6','[COLOR blue]VTV6[/COLOR]')	  
            info = info.replace('                     ','').replace('                    ','').replace('              ','').replace('             ','')
            info = info.split(':')[0].replace(' ','') +' : '+ info.split(':')[-1][:2]
            times = info[:11] + ' [COLOR lime]'+info[11:]+'[/COLOR]'
            addLink( nname +'   '+ times, url+'/'+href, 100,logos+name+'.png')
    elif 'woim' in url:
        thumb = re.compile('img itemprop="image" src="(.+?)&w').findall(content)[0]
        match = re.compile('ascii" value="([^"]*)".+?\s.+\s.+\s.+\s.+\s*\s.+href=".+?download/(.+?).html').findall(content)
        for name,url in match:
            url = urllib2.urlopen(woim+'ma/'+url)
            link = url.geturl()         
            url.close()
            link = urllib.unquote (link)
            link = link[40:len(link)-23]
            content = makeRequest(link)
            match = re.compile('location="(.+?)"').findall(content)[-1]  
            addLink( name.upper(), match, 100, thumb)
    elif 'chiasenhac' in url:		
        match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(content)
        for url,name,thumbnail in match:
            addLink(name,(csn+url),100,thumbnail)
        match=re.compile("<a href=\"hd\/video\/([a-z]-video\/new[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
        for url,name in match:
            addDir('[COLOR lime]Trang Mới Chia Sẻ '+name+'[/COLOR]',csn+'hd/video/'+url+'.html',10,logos+'NEXT.png', fanart+'cat2.jpg')
        match=re.compile("<a href=\"hd\/video\/([a-z]-video\/down[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
        for url,name in match:
            addDir('[COLOR red]Trang Download Mới Nhất '+name+'[/COLOR]',csn+'hd/video/'+url+'.html',10,logos+'NEXT.png', fanart+'cat2.jpg')
    elif 'nhaccuatui' in url:
        match=re.compile("href=\"http:\/\/m.nhaccuatui.com\/video\/([^\"]*)\" title=\"([^\"]+)\"><img alt=\".+?\" src=\"(.*?)\"").findall(content)		
        for url,name,thumbnail in match:
            addLink( name, nct+'video/'+url, 100, thumbnail)
        match=re.compile("href=\"([^\"]*)\" class=\"next\" titlle=\"([^\"]+)\"").findall(content)
        for url,page in match:	
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]', url, 10, logos+'NEXT.png', fanart+'cat2.jpg')			
    elif 'f.vp9.tv' in url:
        match=re.compile('href="(.*?)">(.*?)/<').findall(content)
        for href,name in match:
	        if 'upload' in name:pass
	        else:addLink(name.replace('-',' [COLOR ffff0000]-[/COLOR] ').replace('_',' ').replace('.',' '),url+href,100,logos+'VMUSIC.png')
				
    elif 'phimhd365' in url:	
        match=re.compile('<div style=".+?: 5px;" class=".+?" data-href="(.+?)"').findall(content)
        for url in match:
	        addLink('[[COLOR gold]1[/COLOR]] '+name,url,100,iconimage)  
        match=re.compile('<a href="(.+?)">(\d+)</a>').findall(content)
        for url, epi in match:
	        addLink('[[COLOR gold]'+epi+'[/COLOR]] '+name,phimhd365+url,100,iconimage)
    elif 'phimgiaitri' in url:
        thumbnail = re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)
        addLink('Tập [COLOR yellow]1[/COLOR]',url,100,thumbnail[0])
        match = re.compile("<a href=\"(.+?)\" page=(\d+)>").findall(content)
        for url,epi in match:
            addLink('Tập ' + '[COLOR yellow]' +epi +'  [/COLOR]',url,100,thumbnail[0])
    elif 'hplus.com.vn' in url:
        match=re.compile('<a href="(.+?)" onclick=".+?;\s*.+?;">VN</a>').findall(content)
        for url in match:
	        addLink('[COLOR gold]' + name + '[/COLOR]',url,100,iconimage)
        content = makeRequest(url) 	  
        match=re.compile('style="background-image: url\(\'(.*?)\'\)">\s*.*\s*.*\s*.<h3>\s*.*<a href="(.*?)">(.*?)</a>').findall(content)
        for thumbnail,url,epi in match:
	        addLink(name + ' - ' + epi,url,100,iconimage)
        match=re.compile("ajax_get\('(.*?)',").findall(content)
        if len(match) > 0:
            url_segments = match[0].split("/")
            first_page = url_segments[len(url_segments)-1]
            url_segments = match[len(match)-1].split("/")
            last_page = url_segments[len(url_segments)-1]
            url_segments[len(url_segments)-1] = ''
            page_url = "/".join(url_segments)
            for p in range(int(first_page),int(last_page) + 1):
                url = page_url + str(p)
                content=makeRequest(url)    
                match=re.compile('style="background-image: url\(\'(.*?)\'\)">\s*.*\s*.*\s*.<h3>\s*.*<a href="(.*?)">(.*?)</a>').findall(content)
                for thumbnail,url,epi in match:
                    addLink(name + ' - ' + epi,url,100,iconimage)
    elif 'phimtienganh' in url:
        match = re.compile('<a style=\'.+?:5px\' class=".+?"\s*_episode=".+?" _link="(.+?)" _sub=""\s*href=".+?" >(.+?)</a>').findall(content)
        for url, epi in match:
	        addLink( '[[COLOR gold]' + epi + '[/COLOR]] ' + name, url.replace(' ','%20'),100, iconimage)
    elif 'kephim' in url:
        match=re.compile('<a class="btn btn-lg bg-purple-studio" title="(.+?)" href="(.+?)">').findall(content)
        for title, url1 in match:
            content1 = makeRequest(url1)
            match = re.compile('<a class="current" href="(.+?)" title="(.+?)">').findall(content1)
            for url2, title in match:	
                addLink(title.replace('Tập',' - '),url2,100,iconimage)
        content2=makeRequest(url1)
        match = re.compile('<a class="btn btn-sm bg-purple-soft" role="button" id=".+?" href="(.+?)" title="(.+?)">').findall(content2)
        for url3, title in match:	
            addLink(title.replace('Xem phim ','').replace('tập',' - '),url3,100,iconimage)
    elif 'phim.clip' in url:
        match=re.compile('<a class="episode-f full"\s*href="(.+?)"\s*title=".+?"\s*onClick=".+?;\s*.+?;" >\s*(.+?)<i class="clip-icons-vip"></i>\s*</a>').findall(content)
        for url, epi in match:
	        addLink('[' + epi.replace('Bản full ','[COLOR red]VIP Full[/COLOR]') +'] '+name,url,101,iconimage)
        match=re.compile('<a href="(.+?)" title=".+?" class=".+?" title=".+?"\s*style=".+?: 10px;"><i class=".+?">.+?</i></a>').findall(content)
        for url in match:
	        addLink('[1] '+name,url,101,iconimage)
        match=re.compile('<a class="episode.+?"\s*href="(.+?)"\s*title=".+?">\s*(.+?)\s*</a>').findall(content)[1:]
        for url, epi in match:
	        addLink('[' + epi+'] '+name,url,101,iconimage)
    elif 'ssphim' in url:
        addLink('[[COLOR gold]1[/COLOR]] '+name,url,101,iconimage)
        match=re.compile('<a href="(.+?)" class="btn.+?" data-toggle=".+?" title="">(.+?)</a>').findall(content)[1:]
        for url, epi in match:
	        addLink('[[COLOR gold]' + epi +'[/COLOR]] '+name,url,101,iconimage)
    elif 'megabox' in url:
	    match = re.compile("href='(.+?)' >(\d+)<").findall(content)
	    for url, epi in match:
	        addLink('Tập ' + epi, url,100, iconimage)
    elif 'phim7' in url:
        match = re.compile('<p class=".+?"><b>' + name + '</b>((?s).+?)</p>').findall(content)
        for slink in match:
            match = re.compile('href="(.+?)" title="(.+?)" class=".+?">(.+?)<').findall(slink)
            for url, title, epi in match:
	            title=title.split('online tập')
	            title = title[0].replace('Xem phim ','')
	            addLink('[[COLOR gold]'+epi+'[/COLOR]] ' + title, phim7 + url,100, iconimage)
    elif 'hdonline' in url:
	    match = re.compile('<a href="(.+?)" .+?"><span>(.+?)</span></a>').findall(content)
	    for url, epi in match:						
		    addir('[[COLOR lime]'+str(epi)+'[/COLOR]] '+name,url,img,'',mode=102,isFolder=False)
    elif 'phim3s' in url:
        match = re.compile('<div class="server"><div class="label"><i></i>' + name + '</div><ul class="episodelist">((?s).+?)</div>').findall(content)
        for slink in match:
            match = re.compile('<li><a data-id=".+?" data-type="watch" data-episode-id=".+?" href="(.+?)" title=".+?">(.+?)</a></li>').findall(slink)
            for url, title in match:
	            addLink( title, phim3s + url, 100, iconimage)
    elif 'xuongphim' in url:
        if '?' not in url:
            title = name
            id = re.search('-(\d{1,6})\.html',url).group(1)
            url = 'http://xuongphim.tv/?film=%s&episode=&page=1&searchep=' % id
        else:
            title = re.search('name=(.+?)\Z',url).group(1)
            url = url.split('?name=')[0]
        content = makeRequest(url)
        match = re.compile('<a title="(.+?)" id="(.+?)".+?href="/(.+?)">.+?</a>').findall(content)
        for epi,id,href in match:
            if not re.search('\.\d{1,6}\.html',href):
                href = os.path.splitext(href)[0]+'.%s'%id+os.path.splitext(href)[1]
            addLink(title + ' - ' + epi,xuongphim+href,101,iconimage)
        trangtiep = re.search('<span class="active" >.+?</span><span onclick="loadEpisode\(.+?\)">(.+?)</span>',content)
        if trangtiep:
            trangtiep = trangtiep.group(1)
            url = re.sub('page=\d{1,3}&','page=%s&'%trangtiep,url)
            addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',url+'?name='+name,10,logos+'NEXT.png','')
	
    III()
    if 98 - 98: i11iII1iiI

def iii1Ii11Ii(url):
    if 'URL Patch' in name:
        if '.m3u' in remote:
            content = makeRequest(remote)
            match = re.compile('#EXTINF.+,(.+)\s(.+?)\s').findall(content)
            for title,url in match:
                addLink(title,url,100,iconimage)
        elif '.xml' in remote:
            content = makeRequest(remote)
            match = re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
            for title,url,thumbnail in match:
                addLink(title,url,100,thumbnail)
    elif 'LOCAL Patch' in name:
        if '.m3u' in local:
            try:
                content = read_file(local)
                match = re.compile('#EXTINF.+,(.+)\s(.+?)\s').findall(content)
                for title,url in match:
	                addLink(title,url,100,iconimage)	  
            except:
                pass
        elif '.xml' in local:
            try:
                content = read_file(local)
                match = re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
                for title,url,thumbnail in match:
	                addLink(title,url,100,thumbnail)	  
            except:
                pass
    if 14 - 14: iiII1i1iI - OOO0Ooo0ooO0oOOOOo - II1Ii - i11iII1iiI . oOo0Ooo / Oooo
				
def iIi1II11ii(url,name):
    if 'CLIP HOT' in name:
        content = makeRequest('http://hplus.com.vn/vi/categories/hot-clips')
        match = re.compile("href='http://hplus.com.vn/vi/genre/index(.+?)'>(.+?)<").findall(content)
        for url, title in match:
            if 'Xem tất cả' in title:pass
            else: addDir( title, hplus+'vi/genre/index'+url, 7, logos+'TheLoai.png', fanart+'cat2.jpg')			
    elif 'woim' in url:
        content = makeRequest(url)
        match = re.compile('href="/the-loai(.+?)">(.+?)<').findall(content)
        for url,name in match:
            addDir(name, '%sthe-loai%s' % (woim,url), 7,iconimage, fanart+'cat2.jpg')
        match = re.compile('href=".+?/nhac-cu(.+?)">(.+?)<').findall(content)
        for url,name in match:
            addDir(name, '%snhac-cu%s' % (woim,url), 7,iconimage, fanart+'cat2.jpg')
    elif 'phimhd365' in url:
        if 'Thể Loại' in name:	
            content = makeRequest(url)
            match = re.compile('<li><a href="\s*\s*(.+?)">(.+?)</a></li>').findall(content)[0:12] 
            for url, title in match:  
                addDir(title, phimhd365+url, 7, iconimage,'')	
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('<li><h4><a title=".+?" href="\s*\s*/phim-bo(.+?)">(.+?)</a></h4></li>').findall(content)
            for url, title in match:  
                addDir(title.replace('Phim ','').replace('khác','Quốc Gia Khác'), ('%s/phim-bo%s' % (phimhd365, url)), 7, iconimage,'')
    elif 'hplus.com.vn' in url:
        content = makeRequest(url)	
        match = re.compile("href='http://hplus.com.vn/vi/genre/index(.+?)'>(.+?)<").findall(content)
        for url, title in match:
            if 'Xem tất cả' in title: pass 
            else: addDir(title,hplus+'vi/genre/index'+url,7,iconimage,'')
    elif 'phimhayhd' in url:
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile('href=".+?the-loai([^"]*)">([^>]+)<').findall(content)[0:16]  
            for url, name in match:  
               addDir(name.replace('Phim ',''), ('%sthe-loai%s' % (hayhd, url)), 7, iconimage,'') 
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('href=".+?phim-bo([^"]*)">([^>]+)<').findall(content)[0:4] 
            for url, name in match: 
                addDir(name, ('%sphim-bo%s' % (hayhd, url)), 7, iconimage,'')
    elif 'kephim' in url:
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(content)
            for url, title in match:
	            if 'the-loai' in url:
	                addDir(title,kphim+url,7, iconimage,'')
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('<a title=".+?" href="(.+?)">(.+?)</a>').findall(content)
            for url, title in match:
	            if 'quoc-gia' in url:
	                addDir(title,kphim+url,7, iconimage,'')
        else:
            content = makeRequest(url)
            match = re.compile('<a href="(.+?)" title="(.+?)">.+?</a>').findall(content)[3:24]
            for url, title in match:
	            if 'phim-nam' in url:
	                addDir(title,url,7, '','')
    elif 'phim.clip' in url:
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile('href="/the-loai/(.+?)">(.+?)<').findall(content)
            for url, title in match:  
                addDir(title, ('%sthe-loai/%s' % (phimclip, url)), 7, iconimage,'')
        elif 'Quốc Gia' in name:
            content=makeRequest(url)
            match = re.compile('href="/quoc-gia/(.+?)">(.+?)<').findall(content)
            for url, title in match:  
                addDir(title, ('%squoc-gia/%s' % (phimclip, url)), 7, iconimage,'')
    elif 'ssphim' in url:
        if 'Thể Loại' in name:
            addDir('Phim 18+','http://ssphim.com/movie/tags-phim-nguoi-lon/',7, iconimage,'')
            content = makeRequest(url)
            match = re.compile('<a href=".+?movie(.+?)" title="(.+?)">.+?</a>').findall(content)[0:17]
            for url, title in match:
                title = title.replace(', phim xhđ hay','')	
                addDir(title, ('%smovie%s' % (ssphim, url)), 7, iconimage,'')
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('<a href=".+?movie(.+?)" title=".+?">(.+?)</a>').findall(content)[20:]
            for url, title in match:
                if 'Phim' in title:pass
                else:addDir(title, ('%smovie%s' % (ssphim, url)), 7, iconimage,'')
    elif 'phim7' in url:		  
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile("<a href='/the-loai(.+?)' title='.+?'>(.+?)</a>").findall(content)[17:34]  
            for url, name in match:  
                addDir(name, ('%s/the-loai%s' % (phim7, url)), 7, iconimage,'') 
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile("<a href='/quoc-gia(.+?)' title='.+?'>(.+?)</a>").findall(content)[8:16]  
            for url, name in match:  
                addDir(name, ('%s/quoc-gia%s' % (phim7, url)), 7, iconimage,'')
        elif 'Năm Sản Xuất' in name:
            content = makeRequest(url)
            match = re.compile('<a href="/nam-san-xuat(.+?)" title=".+?">(.+?)</a>').findall(content)[19:39]  
            for url, name in match:
                if 'span' in name:pass	
                else:addDir('Phim năm ' + name, ('%s/nam-san-xuat%s' % (phim7, url)), 7, iconimage,'')
    elif 'megabox' in url:		  
	    if 'phim-le' in url:
	        content = makeRequest(url)
	        match = re.compile("href='phim-le(.+?)'>(.+?)<").findall(content) 
	        for href, name in match:
	            if 'Phim'in name:pass
	            else:addDir('Phim '+name, url + href, 7, iconimage,'')		
	    elif 'phim-bo' in url:
	        content = makeRequest(url)
	        match = re.compile("href='phim-bo(.+?)'>(.+?)<").findall(content) 
	        for href, name in match:
	            if 'Phim'in name:pass
	            else:addDir('Phim '+name, url + href, 7, iconimage,'')
    elif 'xuongphim' in url:
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(content)[:24]
            for url, title in match:
	            if 'xem-phim' in url:
	                addDir( title, xuongphim + url, 7, iconimage, '')  
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(content)
            for url, title in match:
	            if 'phim-bo' in url or 'quoc-gia' in url:
	                addDir( title, xuongphim + url, 7, iconimage, '')
    elif 'phim3s' in url:
        if 'Thể Loại' in name:
            content = makeRequest(url)
            match = re.compile('<li><a href="the-loai(.+?)" title=".+?">(.+?)</a></li>').findall(content)
            for url, name in match:
	            addDir( name, ('%sthe-loai%s' % (phim3s, url)), 7, iconimage,'')	
        elif 'Quốc Gia' in name:
            content = makeRequest(url)
            match = re.compile('<li><a href="quoc-gia(.+?)" title=".+?">(.+?)</a></li>').findall(content)
            for url, name in match:
	            addDir( name, ('%squoc-gia%s' % (phim3s, url)), 7, iconimage,'') 
        elif 'Phim Lẻ' in name:
            content = makeRequest(url)
            match = re.compile('<a href="danh-sach/phim-le(.+?)" title="(.+?)">.+?</a>').findall(content)[:4]
            for url, name in match:
	            addDir( name, ('%sdanh-sach/phim-le%s' % (phim3s, url)), 7, iconimage,'')
        elif 'Phim Bộ' in name:
            content = makeRequest(url)
            match = re.compile('<a href="danh-sach/phim-bo(.+?)" title="(.+?)">.+?</a>').findall(content)[:4]
            for url, name in match:
	            addDir( name, ('%sdanh-sach/phim-bo%s' % (phim3s, url)), 7, iconimage,'')	
        elif 'Phim Chiếu Rạp' in name:
            content = makeRequest(url)
            match = re.compile('<a style=".+?" href="danh-sach/phim-chieu-rap(.+?)" title="(.+?)">.+?</a>').findall(content)[:4]
            for url, name in match:
	            addDir( name, ('%sdanh-sach/phim-chieu-rap%s' % (phim3s, url)), 7, iconimage,'')	
    III()	
    if 30 - 30: iiIIIII1i1iI - OOO0Ooo0ooO0oOOOOo - II1Ii - i11iII1iiI . oOo0O0Ooo / Oooo
    if 5 - 5: Oooo + o0ooo
	
def oOiIi1IIIi1(url):
    try:
        keyb=xbmc.Keyboard('', '[COLOR red]Nhập nội dung cần tìm kiếm...[/COLOR]')
        keyb.doModal()
        if (keyb.isConfirmed()):
            searchText=urllib.quote_plus(keyb.getText())
        if 'timvideo' in url:  
            url = csn+'search.php?s=' + searchText + '&cat=video'      
            oOiii1IIIi1(url)
        elif 'timalbum' in url:  
            url = 'http://www.woim.net/search/album/%s.html' + urllib.quote_plus(searchText)      
            oOiii1IIIi1(url)
        elif 'timphim1' in url:  
            url = 'http://phim3s.net/search/%s/' % urllib.quote_plus(searchText)      
            iI1Ii11111iIi(name,url)	  
        elif 'timphim2' in url:  
            url = 'http://phimhd365.com/search.htm?keyword=%s' % searchText      
            oOiii1IiIi1(url)
        elif 'timphim3' in url:  
            url = pgt+'result.php?type=search&keywords=' + searchText      
            oOiii1IiIi1(url)	  
        elif 'timphim4' in url:  
            url = 'http://hplus.com.vn/vi/search/content?keyword=' + searchText      
            oOiii1IiIi1(url)
        elif 'timphim5' in url:
            url = 'http://phim.megabox.vn/search/index?keyword=' + searchText.replace('+', '-')      
            iI1Ii11111iIi(name,url)
        elif 'timphim6' in url:
            url = 'http://xuongphim.tv/tim-kiem/%s.html' % urllib.quote_plus(searchText) +'?'
            iI1Ii11111iIi(name,url)
        elif 'timphim7' in url:
            url = 'http://hdonline.vn/tim-kiem/'+searchText.replace('+', '-')+'.html'
            Ii1ii11111Iii(url, query='', mode='')
        elif 'timphim8' in url:
            url = 'http://phim7.com/tim-kiem/tat-ca/' + searchText.replace('+', '-') + '.html'
            oOiii1IiIi1(url)	  
        elif 'timphim9' in url:
            url = 'http://phim.clip.vn/search?p=1&keyword=' + searchText + '/'
            oOiii1IiIi1(url)
        elif 'timphim10' in url:
            url = 'http://ssphim.com/movie/tags-' + searchText + '/'
            oOiii1IiIi1(url)	  
    except:
        pass

def oOiii1IIIi1(url):
    content = makeRequest(url)
    if 'chiasenhac' in url:	
        match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(content)
        for url,name,thumbnail in match:
            addLink(name.replace(';',' +'),(csn+url),100,thumbnail)
        match=re.compile("href=\"(.+?)\" class=\"npage\">(\d+)<").findall(content)
        for url,name in match:
            addDir( '[COLOR red]Trang '+name+'[/COLOR]', url.replace('&amp;','&'), 51, logos+'NEXT.png', fanart+'cat2.jpg')
    elif 'woim' in url:
        match=re.compile('<a href="(.+?)" title="(.+?)" target="_blank"><img src="(.+?)" alt=.+?</a>').findall(content)
        for url, name, thumb in match:
            addDir( name, url, 10, thumb)
    III()
			
def OOiii1IiIi1(url):	
  try:
    keyb=xbmc.Keyboard('', '[COLOR red]Nhập nội dung cần tìm kiếm...[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
        searchText=urllib.quote_plus(keyb.getText())
    try:	  
        url = 'http://phimhd365.com/search.htm?keyword=%s' % searchText
        oOiii1IiIi1(url)
        try:	  
            url = pgt+'result.php?type=search&keywords=' + searchText
            oOiii1IiIi1(url)
            try:
                url = 'http://hplus.com.vn/vi/search/content?keyword=' + searchText
                oOiii1IiIi1(url)
                try:
                    url = 'http://xuongphim.tv/tim-kiem/%s.html' % urllib.quote_plus(searchText)
                    oOiii1IiIi1(url)
                    try:
                        url = 'http://phim3s.net/search/%s/' % urllib.quote_plus(searchText)
                        oOiii1IiIi1(url)
                        try:
                            url = 'http://phim7.com/tim-kiem/tat-ca/' + searchText.replace('+', '-') + '.html'
                            oOiii1IiIi1(url)
                            try:
                                url = 'http://phim.clip.vn/search?p=1&keyword=' + searchText + '/'
                                oOiii1IiIi1(url)
                                try:
                                    url = 'http://ssphim.com/movie/tags-' + searchText + '/'
                                    oOiii1IiIi1(url)
                                except:pass 									
                            except:pass 								
                        except:pass							
                    except:pass  						
                except:pass					
            except:pass			  
        except:pass		
    except:pass	  
  except:pass

def oOiii1IiIi1(url):	
    content = makeRequest(url)

    match = re.compile('<div class="inner"><a href="(.+?)" title="(.+?)"><img src="(.+?)".+?</a><div class="info">.+?</a>(.+?)</div>').findall(content)
    for url, title, thumbnail, year in match:
	    addDir('[COLOR lime]Server 1 [/COLOR]' + title + ' ' + year, phim3s + url + 'xem-phim/', 9, thumbnail, thumbnail)	
	
    match=re.compile('<a data-tooltip=".+?" href="(.+?)">.*\s.*data-original="(.+?)"  alt="(.+?)"').findall(content)
    for url, thumbnail, name in match:
	    name = replace_all(name, dict)
	    addDir('[COLOR red]Server 2 [/COLOR]'+name,phimhd365+url,10,thumbnail,thumbnail)

    match = re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font><br \/><font style.+?#F63\'>(.+?)</font>').findall(content)
    for url,thumbnail,name,oname in match:
        addLink('[COLOR blue]Server 3 [/COLOR]'+name+' - '+oname,pgt+url+'/Tap-1.html',100,pgt+thumbnail)
    match = re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)</b>').findall(content)
    for url,thumbnail,name in match:
        addLink('[COLOR blue]Server 3 [/COLOR]'+name,pgt+url+'/Tap-1.html',100,pgt+thumbnail)	  

    match = re.compile("<a style='text-decoration:none' href='(.+?).html'>\s*<img style='.+?' src=(.+?) ><div class='text'>\s*<p>(.+?)</p>\s*</div><table style='.+?'><tr><td style='.+?'><b><font style='.+?:0px'>(.+?)\s*</font><br /><font style='.+?:#F63'> (.+?)</font>").findall(content)  
    for url,thumbnail,epi,name,oname in match:
        addDir('[COLOR blue]Server 3 [/COLOR]'+name+' - '+oname+' '+'[COLOR green]'+epi+'[/COLOR]',pgt+url+'/Tap-1.html',10,pgt+thumbnail,pgt+thumbnail)
    match = re.compile("<a style='text-decoration:none' href='(.+?).html'>\s*<img style='.+?' src=(.+?) ><div class='text'>\s*<p>(.+?)</p>\s*</div><table style='.+?'><tr><td style='.+?'><b><font style='.+?:0px'>(.+?)</b>").findall(content)  
    for url,thumbnail,epi,name in match:	
        addDir('[COLOR blue]Server 3 [/COLOR]'+name+'[COLOR green]'+epi+'[/COLOR]',pgt+url+'/Tap-1.html',10,pgt+thumbnail,pgt+thumbnail)
	  
    match=re.compile('<a class="tooltips" href=".+?" style=".+?url\(\'(.+?)\'\)" data-content-tooltips=".+?"></a>\s*</div>\s*<h3>\s*<a href="(.+?)" title=".+?">(.+?)<').findall(content)
    for thumbnail,url,name in match:
	    addDir('[COLOR lime]Server 4 [/COLOR]'+name,hplus+url,10,thumbnail+'?.png',thumbnail)
	  
    #match=re.compile('<a class="movie-item m-block" href="(.+?)" title="(.+?)"><div class="block-wrapper"><div class=".+?"><div class=".+?"><span class=".+?"><span class=".+?">(.+?)</span></span><img src="(.+?)"').findall(content)
    #for url, title, res, thumbnail in match:
	    #addDir('[COLOR orange]Server 6 [/COLOR]'+title.replace("&#39","'")+' [COLOR green]< '+res+' >[/COLOR]',url,10, thumbnail, thumbnail)	  

    match=re.compile('<a href="(.+?)" .+? src="(.+?)" .+? alt="(.+?)"></span>').findall(content)
    for url, thumbnail, name in match:
	    name = replace_all(name, dict)		
	    addDir('[COLOR orange]Server 6 [/COLOR]' + name, xuongphim +url, 10, thumbnail, thumbnail)
		
    match = re.compile('href="(.+?)" >\s*<img src="(.+?)"\s*alt="(.+?)"').findall(content)
    for url, thumbnail, name in match:
        addDir('[COLOR firebrick]Server 7 [/COLOR]'+name, url, 10, thumbnail, thumbnail)	  

    match = re.compile('href="(.+?)" title="(.+?)"><span class="poster">\s*<img src=".+?" alt="" />\s*<img class=".+?" src=".+?" data-original="(.+?)"').findall(content)
    for url, name, thumbnail in match:
        addDir('[COLOR gold]Server 8 [/COLOR]' + name, phim7 + url.replace('/phim/', '/xem-phim/'), 9, thumbnail, thumbnail)	  
	  
    match=re.compile('<a href="(.+?)" class="item">\s*.+?\s*<div class=".+?" data-title="(.+?)" data-title-o=".+?" .+? data-year="(.+?)" .+?">\s*.+?\s* src="(.+?)"').findall(content)[:1]
    for url, title, year, thumbnail in match:
	    addDir('[COLOR green]Server 9 [/COLOR]' + title + ' - ' + year, url, 10, thumbnail, thumbnail)

    match=re.compile('<a href="(.+?)" title=".+?">\s*<div class=".+?">\s*<h4>.+?</h4>\s*.+?\s*.+?\s*</div>\s*<img class="img-thumbnail" src="(.+?)" alt="(.+?)">\s*</a>').findall(content)
    for url, thumbnail, name in match:
	    thumbnail = thumbnail.replace(' ','%20')
	    addDir('[COLOR deeppink]Server 10 [/COLOR]' + name, url, 10, thumbnail, thumbnail)
	  
    III()

def Ii1Ii11111Iii(url, mode=''):
    Ii1ii11111Iii(url, query='', mode='')	

def Ii11i1Ii(url):
	link = visitor.GetContent("http://hdonline.vn/")
	link = ''.join(link.splitlines()).replace('\'','"')
	try:
		link =link.encode("UTF-8")
	except: pass
	vidcontent=re.compile('<nav class="tn-gnav">(.+?)</nav> ').findall(link)
	vidcontentlist=[]
	if(len(vidcontent)>0):
		addDir('[COLOR red]Tìm Kiếm[/COLOR]','timphim7',50,logos+'timkiem.png','')
		vidcontentlist=re.compile('<li>(.+?)</div>\s*</div>\s*</li>').findall(vidcontent[0])
		for vidcontent in vidcontentlist:
			mainpart=re.compile('<a href="(.+?)"> <span class="tnico-(.+?)"></span>(.+?)</a>').findall(vidcontent)
			mainname=mainpart[0][2]
			href=mainpart[0][0]
			if 'hdonline.vn' not in href:href='http://hdonline.vn'+mainpart[0][0]
			vidlist=re.compile('<li><a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a></li>').findall(vidcontent)
			if 'TIN' in mainname : mainname = "MORE";href='http://hdonline.vn/danh-sach/phim-moi.html'
			addDir('[COLOR lime][B]'+mainname+'[/B][/COLOR]',href,41,logos+'All.png','')	
			for vurl,vname in vidlist:
				if 'Mỹ' in vname : vname = vname.replace('Phim Mỹ','Phim Âu - Mỹ')
				if mainname == "MORE" : vurl = 'http://hdonline.vn'+vurl
				if(vurl.find("javascript:") ==-1 and len(vurl) > 3):
					addDir(vname,vurl,41,logos+'TheLoai.png','')	
	III()	

def Ii1ii11111Iii(url, query='', mode=''):
	search_string = iii1II11ii(query)
	if search_string=='-':search_string=''	
	if 'hdonline.vn' in url:
		content = visitor.GetContent(url)
		content = ''.join(content.splitlines()).replace('\'','"')
		try:
			content = content.encode("UTF-8")
		except: pass
		movielist=re.compile('<li>\s*<div class="tn-bxitem">(.+?)</li>').findall(content)
		for idx in range(len(movielist)):
			vcontent = movielist[idx]				
			items=re.compile('<a href="(.+?)"(.+?)<img src="(.+?)".+?<p class="name-vi">(.+?)</p>\s*<p class="name-en">(.+?)</p>').findall(vcontent)
			for url, episodes, img, nameen, namevn in items :
				name = namevn + ' - ' + nameen							
				if iiI1II11ii(search_string) in iiI1II11ii(name) or search_string == '' :
					isFolder=True;v_query=nameen
					if 'episodes' in episodes :														
						v_mode='bo'
						name = '[HDOnline] ' + name if query!='' else name
					else :						
						v_mode='le'
						if query!='':name = '[HDOnline] ' + name
					if v_mode == 'le' :
						v_mode = 102;isFolder = False						
					else :
						v_mode = 10;url = 'http://m.hdonline.vn' + url
					addir(name,url,img,fanart='fanart',mode=v_mode,page=1,query=v_query,isFolder=isFolder)
		if query=='':
			pagecontent=re.compile('<ul class="pagination">(.+?)</ul>').findall(content)
			if(len(pagecontent)>0):
				pagelist=re.compile('<li><a [^>]*href=["\']?([^>^"^\']+)["\']?[^>]*>(.+?)</a></li>').findall(pagecontent[0])
				for vurl,vpage in pagelist:
					if 'Trang Sau' in vpage:
					    addDir('[COLOR red]Trang Tiếp Theo >>>[/COLOR]',vurl,42,logos+'NEXT.png','')
	III()

	
def iii1II11ii(string):
	string = string.replace('+','-').replace(' ','-')	
	string = string.replace('?','').replace('!','').replace('.','').replace(':','').replace('"','')
	string = string.replace('&amp;','and').replace('&','and').replace("&#39;","")
	i = 1
	while i < 10:
		string = string.replace('(Season '+str(i)+'','Season '+str(i))
		i += 1
	string = string.replace('- Season','Season')	
	string = string.strip()
	return string	
	
def iiI1II11ii(string):
	string = string.replace('+','-').replace(' ','-')	
	string = string.replace('?','').replace('!','').replace('.','').replace(':','')	
	string = string.replace('&amp;','and').replace('&','and').replace("&#39;","")
	string = string.upper()
	string = string.strip()
	return string

def I1ii1(url):
    alert(u'Đang xây dựng!'); return	
	
def I1Ii1():
	if len(OO0OO0O0O0) < 1:
			d = xbmcgui.Dialog().yesno('Thông báo!', '', 'Bạn chưa đăng nhập tài khoản!\nHãy vào menu cài đặt nhập [COLOR gold]Tên đăng nhập[/COLOR] và [COLOR red]Password[/COLOR] để không hiện thông báo này nữa.\nNhấn [COLOR lime]OK[/COLOR] để vào menu cài đặt', '', 'Exit', 'OK')
			if d:
			    addon.openSettings()
			sys.exit()
	if len(O00OO0O0O0) < 1:
			alert(u'Chưa có password!'); addon.openSettings()
			if 1 - 1: O0o00 % Oo0ooO0oo0oO * ooo0Oo0			
	if OO0OO0O0O0 != I1IiiI(OOO0O):
			alert(u'Tên đăng nhập và password chưa đúng!'); sys.exit()
			if 2 - 2: i11Ii11I1Ii1i + I1i1iI1i - iII111iiiii11 / OOoO			
	if O00OO0O0O0 != I1IiiI(O0O0O) :
			alert(u'Tên đăng nhập và password chưa đúng!'); sys.exit()
			if 3 - 3: i11Ii11I1Ii1i + I1i1iI1i * iII111iiiii11
	else:
		OOo000()	
		if 100 - 100: I1i1iI1i % I1IiiI / i1 - ooO - OO0OO0O0O0 / iii1I1I	
	
def I11111iII11i(url):
	if 'htvonline' in url:
		content = makeRequest(url)	
		mediaUrl = re.compile('data\-source=\"([^\"]*)\"').findall(content)[0]
	elif 'wezatv' in url:
		content = makeRequest(url)
		try:
		    mediaUrl = 'http:' + re.compile("file: '(.+?)',").findall(content)[0]
		except:
		    mediaUrl = 'http:' + re.compile('source type="application/x-mpegurl" src="(.+?)"').findall(content)[0]
	elif 'truelifetv' in url:
		content = makeRequest(url)	
		mediaUrl = re.compile('"path":"(.+?)"').findall(content)[0]
	elif 'vtvplus' in url:
		content = makeRequest(url)
		subvideoUrl = re.compile('var responseText = "(.+?)";').findall(content)[0].split(',http:')
		videoUrl = subvideoUrl[0]		  
		mediaUrl = videoUrl
	elif 'chiasenhac' in url:
		content = makeRequest(url)
		try:
		  mediaUrl = re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(content)[0].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
		except:
		  mediaUrl = re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(content)[-1].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
	elif 'nhaccuatui' in url:
		content = makeRequest(url)	
		mediaUrl = re.compile("title=\".+?\" href=\"([^\"]*)\"").findall(content)[0]
	elif 'f.vp9.tv' in url:
		content = makeRequest(url)
		try:
		    try:
		        mediaUrl = url + re.compile('<a href="(.*?)HV.mp4"').findall(content)[0]+'HV.mp4'
		    except:
		        mediaUrl = url + re.compile('<a href="(.*?)mvhd.mp4"').findall(content)[0]+'mvhd.mp4'
		except:
		    mediaUrl = url + re.compile('<a href="(.*?)mv.mp4"').findall(content)[0]+'mv.mp4'
	elif 'phim3s' in url:
		content = makeRequest(url)
		mediaUrl = re.compile("videoUrl = '(.+?)mp4';").findall(content)[0] + 'mp4'
	elif 'profile1' in url:		  
		mediaUrl = url.replace('encry','channel')		
	elif 'phimhd365' in url:
		content = makeRequest(url)
		mediaUrl = re.compile('poster=".+?"\s*src="(.+?)"\s*').findall(content)[-1].replace('&amp;','&')
	elif 'hplus' in url:
	    try:
		    content = makeRequest(url)
		    mediaUrl = re.compile('var link_stream = iosUrl = "(.+?)";').findall(content)[0]		
	    except:
		    alert(u'Nội dung này chưa được Addon hỗ trợ!'); return 
	elif 'phimhayhd' in url:
		content = makeRequest(url)
		try:
		    mediaUrl = re.compile('file":"(.+?)","title":.+?').findall(content)[-1].replace('\\','')		  
		except:
		    videoUrl = re.compile('"url":"(.+?)","status":"ok"').findall(content)[0].replace('\\','')
		    mediaUrl = videoUrl.replace('http://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id=').replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id=')
	elif 'phimgiaitri' in url:
		try:	
		    xbmc.log(url)	
		    arr = url.split('/')
		    phimid = arr[len(arr) - 3]
		    tap = arr[len(arr) - 1]
		    tap2 = tap.split('-')
		    tap3 = tap2[1].split('.')
		    tap = tap3[0]
		    url2 = 'http://120.72.85.195/phimgiaitri/mobile/service/getep3.php?phimid=' + phimid
		    content = makeRequest(url2)
		    content = content[3:]
		    infoJson = json.loads(content)
		    tapindex = int(tap) -1
		    link = infoJson['ep_info'][tapindex]['link']
		    link = link.replace('#','*')
		    url3 ='http://120.72.85.195/phimgiaitri/mobile/service/getdireclink.php?linkpicasa=' + link
		    content = makeRequest(url3)
		    content = content[3:]
		    linkJson = json.loads(content)
		    mediaUrl = linkJson['linkpi'][0]['link720'] or linkJson['linkpi'][0]['link360']
		except:
		    content = makeRequest(url)
		    mediaUrl = re.compile('file: "(.+?)"').findall(content)[0]
	elif 'kephim' in url:
		content = makeRequest(url)
		try:
		    try:
		        mediaUrl = 'https://redirector' + re.compile('source src="https://redirector(.+?)" type="video/mp4" data-res="1080"').findall(content)[-1]
		    except:
		        videoUrl = re.compile('"src": "(.+?)"').findall(content)[0]
		        mediaUrl = videoUrl.replace('http://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id=').replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id=')
		except:
		    mediaUrl = re.compile('source src="(.+?)"').findall(content)[0]
	elif 'megabox' in url:
		content = makeRequest(url)
		try:
		    try:
		        mediaUrl = re.compile('var iosUrl = "(.+?)"').findall(content)[0].replace('http://media21.megabox.vn','http://113.164.28.48').replace('http://media22.megabox.vn','http://113.164.28.48') + reg
		    except:
		        mediaUrl = re.compile('var iosUrl = "(.+?)"').findall(content)[0].replace('http://media21.megabox.vn','http://113.164.28.47').replace('http://media22.megabox.vn','http://113.164.28.47') + reg
		except:
		    mediaUrl = re.compile('var iosUrl = "(.+?)"').findall(content)[0].replace('http://media21.megabox.vn','http://113.164.28.46').replace('http://media22.megabox.vn','http://113.164.28.46') + reg
	elif 'phim7' in url:
		content = makeRequest(url)
		try:
		    try:
		        mediaUrl = 'https://redirector' + re.compile('file: "https://redirector(.+?)", label:".+?", type: "video/mp4"').findall(content)[-1]
		    except:
		        mediaUrl = re.compile('file: "(.+?)", label:".+?", type: "video/mp4"').findall(content)[-1]
		except:
		    mediaUrl = re.compile('source src="(.+?)"').findall(content)[0]
	else:	
		mediaUrl = url	
	item = xbmcgui.ListItem( path = mediaUrl )
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return 	
	if 101 - 101: i11iII1iiI - iiIIIII1i1iI . O0Oooo00 . ooooo00000OOOO / iii1II11ii + O0Oooo00
	
def I11111iIi11i(url):
	if 'phim.clip' in url:
		content = makeRequest(url)
		mediaUrl = re.compile("file':'(.+?)','label':'.+?'").findall(content)[0]
		OOoO = OOoO0O00o0(content)
	elif 'ssphim' in url:
		content = makeRequest(url)
		mediaUrl = re.compile('source src="(.+?)" type="video/mp4" data-res="HD"').findall(content)[0]
		OOoO = OOoO0O0Oo0(content)
	elif 'phimtienganh' in url:
		content = makeRequest(url)
		mediaUrl = url
		OOoO = OOoO0O0OoO(content)
	elif 'xuongphim' in url:
		content = makeRequest(url)
		videoUrl = re.compile('file: "(.+?)",.+?type:').findall(content)
		if '.mp4' in videoUrl:
		    mediaUrl = videoUrl[-1]
		else:
		    mediaUrl = replace_all(videoUrl[-1], dict)
		OOoO = OOoOOO0OoO(content)
	else:	
		mediaUrl = url	
	item = xbmcgui.ListItem( path = mediaUrl )
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
	if len(OOoO) > 0:
	    try:
	        xbmc.sleep(5000)
	        xbmc.Player().setSubtitles(OOoO)
	        print OOoO;notification(u'[COLOR red]Load Sub Thành Công[/COLOR]');
	    except:
	        pass
	return	
	if 71 - 71: i11iII1iiI - iiIIIII1i1iI . O0Oooo00 . ooooo00000OOOO / iii1II11ii + O0Oooo00

def I11111IIi11i(url):
	fid = I1iI1(re.search('-(\d{1,5}).html',url),1)
	url = 'http://hdonline.vn/frontend/episode/loadxmlconfigorder?ep=1&fid='+str(fid)
	content = visitor.GetContent(url)
	vurl=re.compile('<jwplayer:file>(.+?)</jwplayer:file>').findall(content)[0]
	if(vurl.find("http") == -1):
		vurl = visitor.decodevplug(vurl)
	vsubtitle=re.compile('<jwplayer:vplugin.subfile>(.+?)</jwplayer:vplugin.subfile>').findall(content)
	suburl=""
	if(len(vsubtitle)>0 and vsubtitle[0].find("http")>-1):
		suburl=vsubtitle[0]
	elif(len(vsubtitle)>0):
		suburl=decodevplug(vsubtitle[0])
	for item in suburl.split(','):
		if 'VIE' in item:suburl=item
	if 'phimhd3s' in vurl:
		link = vurl
	else:
	    link= 'plugin://plugin.program.gdrive?mode=streamURL&url=' + vurl.replace('view?usp=sharing','edit')
	subtitle=suburl
	listitem = xbmcgui.ListItem(path=link)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)
	if len(subtitle) > 0:
	    subtitlePath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
	    subfile = xbmc.translatePath(os.path.join(subtitlePath, "temp.sub"))
	    try:
		    if os.path.exists(subfile):
		        os.remove(subfile)
		    f = urllib2.urlopen(subtitle)
		    with open(subfile, "wb") as code:
		        code.write(f.read())
		    xbmc.sleep(5000)
		    xbmc.Player().setSubtitles(subfile);notification(u'[COLOR red]Load Sub Thành Công[/COLOR]');
	    except:
		    notification(u'[COLOR gold]Load Sub Không Thành Công[/COLOR]');
	elif 'TM' not in vurl:
	    notification(u'[COLOR lime]Phim Thuyết Minh Không Có Sub Rời[/COLOR]');
	if 105 - 105: i11iII1iiI - iiIiiII1i1iI . O0Oooo00 . ooooo00000OOOO / iii1II11ii + O0Oooo00

def OOoO0O00o0(content):
    OOoO = re.search("'file':'(http://v2.cdn.clip.vn/.+?)','kind':'captions','label':'Tiếng Việt'",content)
    if OOoO:OOoO = OOoO.group(1)
    else:OOoO =''
    return OOoO

def OOoO0O0Oo0(content):
    OOoO = re.search('kind="captions" src="(.+?)"',content)
    if OOoO:OOoO = OOoO.group(1)
    else:OOoO =''
    return OOoO

def OOoO0O0OoO(content):
    OOoO = re.search('label="Vietnamese" srclang="vi" src="(.+?)"',content)
    if OOoO:OOoO = OOoO.group(1)
    else:OOoO =''
    return OOoO
	
def OOoOOO0OoO(content):
    OOoO = re.search('file: "(.+?)".*\s.*kind: "captions"',content)
    if OOoO:OOoO = OOoO.group(1)
    else:OOoO =''
    return OOoO
	
def makeRequest(url):
    try:
        req=urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')	
        response=urllib2.urlopen(req)
        link=response.read()
        response.close()  
        return link
    except urllib2.URLError, e:
        print 'We failed to open "%s".' % url
        if hasattr(e, 'code'):
            print 'We failed with error code - %s.' % e.code	
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason			
			
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
   
def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name})
    liz.setProperty('mimetype', 'video/x-msvideo')
    liz.setProperty("IsPlayable","true")
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz, isFolder=False)
    return ok  

def addDir(name,url,mode,iconimage,fanart):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    if O00OO0OOO0 == 'true':	
        liz.setProperty('Fanart_Image',fanart)
    if ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok
    if 'plugin://' in url:
        u = url
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
    if 'Kho Phim Fshare' in name:	
        u = 'plugin://plugin.video.itv.fshare'		
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok		
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def addir(name,link,img='',fanart='',mode=0,page=0,query='',isFolder=False):
	ok=True
	item=xbmcgui.ListItem(name,iconImage=img,thumbnailImage=img)
	item.setInfo(type="Video", infoLabels={"title":name})
	item.setProperty('Fanart_Image',fanart)
	u=sys.argv[0]+"?url="+urllib.quote_plus(link)+"&img="+urllib.quote_plus(img)+"&fanart="+urllib.quote_plus(fanart)+"&mode="+str(mode)+"&page="+str(page)+"&query="+query+"&name="+name
	if not isFolder:
	    item.setProperty('IsPlayable', 'true')
	ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item,isFolder=isFolder)
	return ok	

mphim = 'http://mphim.net'	
phimhd365 = 'http://phimhd365.com'
pgt = 'http://phimgiaitri.vn/'
hplus = 'http://hplus.com.vn/'
hayhd='http://phimhayhd.vn/'
kphim = 'http://kephim.com'
phimclip = 'http://phim.clip.vn/'
ssphim = 'http://ssphim.com/'
phim7 = 'http://phim7.com'
phim3s = 'http://phim3s.net/'
xuongphim = 'http://xuongphim.tv/'
tvreplay = 'http://113.160.49.39/tvcatchup/'
woim = 'http://www.woim.net/'
csn = 'http://chiasenhac.com/'
nct = 'http://m.nhaccuatui.com/'
vmusic = 'http://f.vp9.tv/music/'

IIiIiII11i = 'aHR0cDovL3hibWMuaXR2\4\n\cGx1cy5uZXQvU09VUkVDRS9NQUlOLnhtbA=\?\=\1'
if 22 - 22: OOO0O * IIiIiII11i
IIiIiiI11i = 'aHR0cDovL3hibWMuaXR2\6\n\cGx1cy5uZXQvU09VUkVDRS9NZW51TS54bWw\?\='
if 44 - 44: IIiIiII11i + i11iIiiIii
IIiIIiI11i = 'aHR0cDovL3hibWMuaXR2\n\a\cGx1cy5uZXQvU09VUkVDRS9NZW51VC54bWw\?\=\3'
if 66 - 66: O0Oooo00 . IIiIiII11i + oOo0O0Ooo . ii1II11I1ii1I * O0Oooo00
IiiIIiI11i = 'SMOgbmggxJHhu\n\3\5luZyBs4bqleSBjb2RlIGPhu6dhIG5nxrDhu51pIGtow6FjIGzDoCBraMO0bmcgdOG7kXQ\?\=\4'
if 16 - 16: O0Oooo00 . IIiIiII11i + oOo0O0Ooo * O0Oooo00
IiIIIiI11i = 'aHR0cDovL3hibWMuaXR2\n\6\cGx1cy5uZXQvU09VUkVDRS9NZW51WC54bWw\?\=\4'
if 33 - 33: oOo0O0Ooo
IiIiIiI11i = 'aHR0cDovL3hibWMuaXR2\n\4\cGx1cy5uZXQvU09VUkVDRS9NZW51Sy54bWw\?\=\5'
if 88 - 88: IIiIiII11i . i11iIiiIii - ii1II11I1ii1I	
OOO0O = 'aXR2\3\b\cGx1czIwMTU=\n\?'
if 48 - 48: Oooo
if 11 - 11: O0Oooo00 + II1Ii - i11iII1iiI / ii1II11I1ii1I + iii1II11ii . oOo0O0Ooo
if 41 - 41: O0o00 - Oooo - Oooo
O0O0O = 'aXR2\7\a\cGx1c25ldA=\n\=\3'
if 45 - 45: iiIIIII1i1iI - O0O0O - II1Ii - i11iII1iiI . oOo0O0Ooo / O0O0O
if 51 - 51: O0O0O + o0ooo
if 8 - 8: iiIIIII1i1iI * iI1Ii11111iIi - O0o00 - i11iII1iiI * oo % I1ii11iIi11i		
I1IiiI = base64.b64decode
if 6 - 6: OoOOo / i11iIiiIii + o0ooo * I1IiiI
if 80 - 80: oOo0O0Ooo
if 83 - 83: O0Oooo00 . i11iIiiIii + oOo0O0Ooo . ii1II11I1ii1I * O0Oooo00
if 53 - 53: I1IiiI

#xbmcplugin.setContent(int(sys.argv[1]), 'movies')	
params = get_params()
url = None
name = None
mode = None
iconimage = None
page=0

try:mode=int(params["mode"])
except:pass
try:url=urllib.unquote_plus(params["url"])
except:pass
try:name=urllib.unquote_plus(params["name"])
except:pass
try:iconimage=urllib.unquote_plus(params["iconimage"])
except:pass
try:img=urllib.unquote_plus(params["img"])
except:pass
try:page=int(urllib.unquote_plus(params["page"]))
except:pass
#try:fanart=urllib.unquote_plus(params["fanart"])
#except:pass

sysarg=str(sys.argv[1])

if mode==None or url==None or len(url)<1:
	I1Ii1() #I1iI1

elif mode==1:Ii11I1Ii(name,url)

elif mode==2:Ii11I(name)
	
elif mode==3:iii1Ii11ii(name,url)

elif mode==4:I1ii11iIi11i(url)	

elif mode==5:I1Ii11iIi11i(name,url)

elif mode==6:I1Ii11iII11i(url)

elif mode==7:iI1Ii11111iIi(name,url)

elif mode==8:II1Ii11111iIi(url)

elif mode==9:II1ii11111iIi(url)

elif mode==10:Ii1ii11111IIi(url,name,iconimage)

elif mode==11:iii1Ii11Ii(url)

elif mode==15:iIi1II11ii(url,name)

elif mode==16:I1II11iII11i(name,url)

elif mode==17:I1II11iiI11i(name,url)

elif mode==20:I1ii1(url)

#elif mode==30:Ii11i1II()

#elif mode==31:Ii1Ii11i11()

#elif mode==32:Ii1Ii11I11()

elif mode==40:Ii11i1Ii(url)

elif mode==41:Ii1Ii11111Iii(url, mode='')

elif mode==42:Ii1ii11111Iii(url, query='', mode='')

elif mode==50:oOiIi1IIIi1(url)

elif mode==51:oOiii1IIIi1(url)

elif mode==60:OOiii1IiIi1(url)

elif mode==61:oOiii1IiIi1(url)

elif mode==100:
    O0OO0O = xbmcgui.DialogProgress()
    O0OO0O.create('***ITV Plus***', 'Đang tải. Vui lòng chờ trong giây lát...')
    I11111iII11i(url)
    O0OO0O.close()
    del O0OO0O

elif mode==101:
    O0OO0O = xbmcgui.DialogProgress()
    O0OO0O.create('***ITV Plus***', 'Đang tải. Vui lòng chờ trong giây lát...')
    I11111iIi11i(url)
    O0OO0O.close()
    del O0OO0O	

elif mode==102:
    O0OO0O = xbmcgui.DialogProgress()
    O0OO0O.create('***ITV Plus***', 'Đang tải. Vui lòng chờ trong giây lát...')
    I11111IIi11i(url)
    O0OO0O.close()
    del O0OO0O	
	
elif mode==500:addon.openSettings();end='ok'
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))