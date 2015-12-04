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

import urllib,urllib2,re,os
import xbmcplugin,xbmcgui,xbmcaddon

mysettings=xbmcaddon.Addon(id='plugin.video.phim3s')
profile=mysettings.getAddonInfo('profile')
home=mysettings.getAddonInfo('path')
fanart=xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon=xbmc.translatePath(os.path.join(home, 'icon.png'))
logos=xbmc.translatePath(os.path.join(home, 'logos\\'))
mode_opt=int(mysettings.getSetting('Mode_Number'))
anhtrang='http://phim.anhtrang.org/'
m_anhtrang='http://m.anhtrang.org/'
hd_caphe='http://phim.hdcaphe.com/'
phim3s='http://phim3s.net/'
dchd='http://dangcaphd.com/'
pgt='http://phimgiaitri.vn/'
fptplay='http://fptplay.net'
megaboxvn='http://megabox.vn/'
hayhd='http://phimhayhd.vn/'
zui='http://zui.vn/'

def makeRequest(url):
  try:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    response=urllib2.urlopen(req, timeout=120)
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
 
def main():
  addDir('[COLOR yellow]Phim 3S[/COLOR]',phim3s,2,logos+'phim3s_1.png')
  #addDir('[COLOR orange]Phim Ánh Trăng[/COLOR]',anhtrang,2,logos+'anhtrang.png')  
  #addDir('[COLOR violet]Phim Megabox[/COLOR]',megaboxvn,2,logos+'megabox.png')  
  #addDir('[COLOR lightgreen]Phim Hay HD[/COLOR]',hayhd,2,logos+'hayhd.png')
  #addDir('[COLOR lightblue]Phim HD Cafe[/COLOR]',hd_caphe+'camera-quan-sat.html',2,logos+'hdcaphe.png')  
  #addDir('[COLOR cyan]Phim giải trí VN[/COLOR]',pgt,5,logos+'pgt.png')
  #addDir('[COLOR lime]Đẳng cấp HD[/COLOR]',dchd,2,logos+'dchd_1.png')  
  #addDir('[COLOR magenta]FPT Play[/COLOR]',fptplay,2,logos+'fptplay.png')
  #addDir('[COLOR silver]zui.vn[/COLOR]',zui,2,logos+'zui.png')   
 
def megavn(url):
  content = makeRequest(url)
  if 'tvonline' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR yellow]' + title + '[/COLOR]', url, 13, logos + 'megabox.png')
  elif 'phim-le' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)[6:]
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR lime]' + title + '[/COLOR]', url, 15, logos + 'megabox.png')  
  elif 'phim-bo' in url:
    match = re.compile('<div class="infoC"> <a href="(.+?)" >\s*<h4>(.+?)<span>\((\d+)\)<\/span>').findall(content)[5:]
    for url, title, inum in match:
      if inum == '0':
        pass
      else:
        addDir('[COLOR yellow]' + title + '[/COLOR]', url, 13, logos + 'megabox.png')  

def search():
  try:
    keyb=xbmc.Keyboard('', '[COLOR yellow]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    if 'phim3s' in name:  
      url=phim3s+'search?keyword='+searchText
      print "Searching URL: "+url	  
      index(url)
    elif 'dangcaphd' in name:
      url=dchd+'movie/search.html?key='+searchText+'&search_movie=0'
      print "Searching URL: "+url	  
      index(url)
    elif 'Tìm Phim Lẻ' in name:
      url=pgt+'result.php?type=search&keywords='+searchText
      print "Searching URL: "+url	  
      index(url)
    elif 'FPTPLAY' in name:
      url=fptplay+'/Search/'+searchText
      print "Searching URL: "+url	      
      try:
        mediaList(url)  # Fast - no thumbs + 1 more click
      except:  
        fpt_img(url)    # Slow - thumbs + 1 less click
    elif 'zui' in name:
      url='http://zui.vn/tim-kiem-nc/'+searchText+'.html'
      print "Searching URL: "+url	  
      mediaList(url)
    elif 'hdcaphe' in name:		
      url=hd_caphe+'search-result.html?keywords='+searchText
      print "Searching URL: "+url	  
      mediaList(url)
    elif 'anhtrang' in name:		
      url=anhtrang+'tim-kiem='+searchText+'.html'
      print "Searching URL: "+url	  
      anhtrang_mediaList(url)
    elif 'megabox' in name:	
      url = megaboxvn + 'home/search/index/key/' + searchText
      print "Searching URL: "+url	 	
      megaListEps(url)
      otherMegaList(url)
    elif 'phimhayhd' in name:	
      url = hayhd + 'tim-kiem.html?query=' + searchText
      print "Searching URL: "+url	 	
      hayhd_bo(url)
  except: pass

def hayhd_bo(url):
  content = makeRequest(url)
  match = re.compile('href="([^"]*)">\s*<img.+?data-src="([^"]+)" alt.+?title="([^"]*)"').findall(content)
  for url, thumbnail, name in match:
    link = makeRequest(url)
    eps = re.compile('href="(.+?)" class="episode.+?">(.+?)<').findall(link)
    for vlink, title in eps:
      add_Link('[COLOR cyan]' + title + '[COLOR lime] - ' + name + '[/COLOR]',vlink,thumbnail)  
    
def categories(url):
  content=makeRequest(url)
  if 'phim3s' in url:
    addDir('[COLOR lime]Tìm kiếm Phim[/COLOR]',phim3s,1,logos+'phim3s_1.png')
    match=re.compile("<a href=\"the-loai([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',('%sthe-loai%s' % (phim3s, url)),3,logos+'phim3s_2.png')					
    match=re.compile("<a href=\"quoc-gia([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',('%squoc-gia%s' % (phim3s, url)),3,logos+'phim3s_3.png')					
    match=re.compile("<a href=\"danh-sach([^\"]*)\" title=\"([^\"]+)\">.+?<\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lightblue]'+name+'[/COLOR]',('%sdanh-sach%s' % (phim3s, url)),3,logos+'phim3s_4.png')					
  elif 'dangcaphd' in url:
    addDir('[COLOR yellow]dangcaphd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR lightgreen]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',dchd+'',1,logos+'dchd_1.png')
    match=re.compile("<a href=\"([^\"]*)\" class='menutop' title='([^']+)'>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,3,logos+'dchd_2.png')  
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/cat(.+?)\" title=\"([^\"]*)\">").findall(content)[0:28]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',dchd+'cat'+url,3,logos+'dchd_3.png')
    match=re.compile("<li><a href=\"http:\/\/dangcaphd.com\/country(.+?)\" title=\"([^\"]+)\">").findall(content)[0:12]
    for url,name in match:
      addDir('[COLOR orange]'+name+'[/COLOR]',dchd+'country'+url,3,logos+'dchd_1.png')
    match=re.compile("<a href=\"http:\/\/dangcaphd.com\/movie(.+?)\"><span>(.*?)<\/span><\/a>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',dchd+'movie'+url,3,logos+'dchd_2.png')					
  elif 'phimgiaitri' in url:
    addDir('[COLOR lime]phimgiaitri[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim Lẻ[/COLOR]',pgt,1,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Lẻ(.+?)\'><span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20L%E1%BA%BB'+url.replace(' ','%20'),3,logos+'pgt.png')
  elif 'fptplay' in url:
    addDir('[COLOR lime]Nhấn vô đây, [COLOR yellow]chọn cách bắt links [COLOR cyan]nhanh [COLOR yellow]hay [COLOR cyan]chậm[/COLOR]',url,17,logos+'fptplay.png')
    addDir('[COLOR blue]FPTPLAY[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR blue]Tìm Video[/COLOR]',fptplay,1,logos+'fptplaysearch.png')    
    match=re.compile("<li ><a href=\"(.+?)\" class=\".+?\">(.+?)<\/a><\/li>").findall(content)
    for url,name in match:
		  if 'livetv' in url:
			  pass
		  else:
			  addDir('[COLOR magenta]'+name+'[/COLOR]',fptplay+url,6,logos+'fptplay.png')				
  elif 'zui' in url:
    addDir('[COLOR magenta]zui[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR magenta]Tìm Phim[/COLOR]',zui,1,logos+'zui.png') 
    match=re.compile("<li><a title=\".+?\" href=\"([^\"]*)\">([^>]+)<\/a><\/li>").findall(content)[0:3]
    for url,name in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',url,7,logos+'zui.png')	  
    match=re.compile("<li><a href='([^']*)'><b class=\"larrow\"><\/b>(.+?)<\/a><\/li>").findall(content)[0:17]
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\'><b class="larrow"><\/b>([^>]*)<\/a><\/li>').findall(content)[17:28]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',url,7,logos+'zui.png')
    match=re.compile('<li><a href=\'([^\']*)\' style=.+?<\/b>(\d+)<\/a><\/li>').findall(content)
    for url,name in match:
      addDir('[COLOR lightgreen]'+name+'[/COLOR]',url,7,logos+'zui.png')	
  elif 'hdcaphe' in url:
    addDir('[COLOR yellow]hdcaphe[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',hd_caphe,1,logos+'hdcaphe.png')
    match = re.compile("<li class=\"sibling\"><a href=\"([^\"]*)\"   title=\"([^\"]+)\"").findall(content)[3:7]
    for url,name in match:	
      addDir('[COLOR lime]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match = re.compile("<li class=\"first\"><a href=\"(.+?)\"   title=\"(.+?)\"").findall(content)[0:4]
    for url,name in match:	
      addDir('[COLOR orange]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match = re.compile("<li class=\"last\"><a href=\"(.+?)\"   title=\"(.+?)\"").findall(content)[0:-1]
    for url,name in match:	
      addDir('[COLOR cyan]'+name+'[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    addDir('[COLOR violet]PHIM HOẠT HÌNH[/COLOR]',hd_caphe+'PHIM_HD_IPHONE_MAY_TINH_BANG_TABLET.html',7,logos+'hdcaphe.png')  	
  elif 'anhtrang' in url:  
    addDir('[COLOR yellow]anhtrang[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim[/COLOR]',anhtrang,1,logos+'anhtrang.png')
    #content=makeRequest(anhtrang)
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]*)\" >\s*<span>(.+?)<\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')  
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[0:7]
    for url,name in match:
      addDir('[COLOR cyan]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')
    match=re.compile("<a class=\"link\" href=\"http:\/\/.+?\/([^\"]+)\">\s*<span>(.+?)<\/span>").findall(content)[7:19]
    for url,name in match:
      addDir('[COLOR orange]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png')	
    match=re.compile('<li class="item27">\s*<a class="topdaddy link" href="http:\/\/.+?\/([^"]*)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR magenta]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png') 
    match=re.compile('<li class="item28">\s*<a class="topdaddy link" href="http:\/\/.+?\/(.+?)">\s*<span>(.+?)<\/span>').findall(content)
    for url,name in match:
      addDir('[COLOR lightblue]'+name+'[/COLOR]',anhtrang + url,12,logos+'anhtrang.png') 
  elif 'megabox' in url:  
    #addDir('[COLOR cyan]megabox[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR cyan]Tìm Phim[/COLOR]',megaboxvn,1,logos+'megabox.png')
    match = re.compile("href=\"tvonline\/(.+?)\">([^>]*)<").findall(content)[:3]  
    for url, name in match: 
      if 'the-loai' in url:  
        addDir('[COLOR yellow]TV - ' + name + '[/COLOR]', ('%stvonline/%s' % (megaboxvn, url)), 11, logos + 'megabox.png')
      else:	  
        addDir('[COLOR yellow]TV - ' + name + '[/COLOR]', ('%stvonline/%s' % (megaboxvn, url)), 13, logos + 'megabox.png')
    addDir('[COLOR lime]Phim Lẻ - Mới Nhất[/COLOR]', megaboxvn + 'phim-le/moi-nhat.html', 15, logos + 'megabox.png')	  
    match = re.compile("href=\"phim-le\/(.+?)\">([^>]*)<").findall(content)[:3] 
    for url, name in match: 
      if 'the-loai' in url:  
        addDir('[COLOR lime]Phim Lẻ - ' + name + '[/COLOR]', megaboxvn + 'phim-le/' + url, 11, logos + 'megabox.png')
      else:
        addDir('[COLOR lime]Phim Lẻ - ' + name.replace('Phim ', '') + '[/COLOR]', megaboxvn + 'phim-le/' + url, 15, logos + 'megabox.png')	  
    addDir('[COLOR lime]Phim Lẻ - Dành Cho Bạn[/COLOR]', megaboxvn + 'for_you_movies.html', 15, logos + 'megabox.png')
    addDir('[COLOR yellow]Phim Bộ - Mới Nhất[/COLOR]', megaboxvn + 'phim-bo/moi-nhat.html', 13, logos + 'megabox.png')  
    match = re.compile("href=\"phim-bo\/(.+?)\">([^>]*)<").findall(content)[:4] 
    for url, name in match:
      if 'the-loai' in url:  
        addDir('[COLOR yellow]Phim Bộ - ' + name + '[/COLOR]', ('%sphim-bo/%s' % (megaboxvn, url)), 11, logos + 'megabox.png')	
      else:
        addDir('[COLOR yellow]Phim Bộ - ' + name + '[/COLOR]', ('%sphim-bo/%s' % (megaboxvn, url)), 13, logos + 'megabox.png')		
    match = re.compile("href=\"video-clip\/(.+?)\">([^>]*)<").findall(content)[1:5]
    for url, name in match:  
      addDir('[COLOR lime]Videos - ' + name + '[/COLOR]', megaboxvn + 'video-clip/' + url, 15, logos + 'megabox.png')	
  elif 'phimhayhd' in url:
    addDir('[COLOR yellow]phimhayhd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim Lẻ[/COLOR]', hayhd, 9, logos + 'hayhd.png')
    addDir('[COLOR lime]phimhayhd[B]   [COLOR lime]>[COLOR cyan]>[COLOR orange]>[COLOR magenta]>   [/B][COLOR lime]Tìm Phim Bộ[/COLOR]', hayhd, 1, logos + 'hayhd.png')  
    content = makeRequest(hayhd) 
    match = re.compile('href=".+?the-loai([^"]*)">([^>]+)<').findall(content)[0:16]  
    for url, name in match:  
      addDir('[COLOR cyan]Phim Lẻ - [COLOR yellow]' + name.replace('Phim ','') + '[/COLOR]', ('%sthe-loai%s' % (hayhd, url)), 3, logos + 'hayhd.png')
    match = re.compile('href=".+?phim-bo([^"]*)">([^>]+)<').findall(content)[0:4] 
    for url, name in match: 
      addDir('[COLOR orange]Phim Bộ - [COLOR lime]' + name + '[/COLOR]', ('%sphim-bo%s' % (hayhd, url)), 7, logos + 'hayhd.png')	
  
def megaListEps(url):	
  content = makeRequest(url)
  if 'phim-bo' in url:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s.*\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      addDir('[COLOR yellow]' + title + '[/COLOR]',url,8,thumbnail + '?.jpg')  
  else:	  
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s*\s.+\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      if 'victorias-secret-fashion-show' in url:
        add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')
      else:		
        addDir('[COLOR yellow]' + title + '[/COLOR]',url,8,thumbnail + '?.jpg')
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
	#them dong nay vao de hien thi thumbnail
	  
def index(url):
  content=makeRequest(url)
  if 'phim3s' in url:
    match=re.compile("<div class=\"inner\"><a href=\"(.*?)\" title=\"([^\"]*)\"><img src=\"(.+?)\"").findall(content)
    for url,name,thumbnail in match:
      addDir('[COLOR yellow]'+name+'[/COLOR]',('%s%sxem-phim' % (phim3s, url)),4,thumbnail)					
    match=re.compile("<span class=\"item\"><a href=\"([^\"]*)\">(\d+)<\/a><\/span>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',('%s%s' % (phim3s, url)),3,logos+'phim3s_4.png')					
  elif 'dangcaphd' in url:
    match=re.compile('<a href="(.+?)" title="(.+?)">\s*<img src="(.+?)"').findall(content)
    for url,name,thumbnail in match:
      if 'Trailer' in name:
        pass
      else:      
        add_Link('[COLOR yellow]'+name+'[/COLOR]',(url.replace('movie','watch')),thumbnail) 
    match=re.compile("<a href=\"([^\"]+)\">&lt;&lt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang Đầu[/COLOR]',url.replace('amp;',''),3,logos+'dchd_1.png')
    #match=re.compile("<a href=\"([^\"]*)\">&lt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR cyan]Trang Trước[/COLOR]',url.replace('amp;',''),3,logos+'dchd_3.png')	
    match=re.compile("<a href=\"([^>]*)\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',url.replace('amp;',''),3,logos+'dchd_2.png')
    #match=re.compile("<a href=\"(.+?)\">&gt;<\/a>").findall(content)
    #for url in match:
      #addDir('[COLOR blue]Trang Sau[/COLOR]',url.replace('amp;',''),3,logos+'dchd_1.png')
    match=re.compile("<a href=\"([^\"]*)\">&gt;&gt;<\/a>").findall(content)
    for url in match:
      addDir('[COLOR red]Trang Cuối[/COLOR]',url.replace('amp;',''),3,logos+'dchd_3.png')
  elif 'phimgiaitri' in url:
    match=re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font>').findall(content)
    for url,thumbnail,name in match:
      add_Link('[COLOR yellow]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',pgt+thumbnail)					
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),3,logos+'pgt.png')					
  elif 'phimhayhd' in url:
    match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?">(.+?)</span>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
    for thumbnail, cat, url, name in match:
      add_Link('[COLOR cyan]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, thumbnail)   
    match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
    for thumbnail, url, name in match:
      add_Link('[COLOR yellow]' + name + '[/COLOR]', url,thumbnail)
    match = re.compile('href="(.+?)">Trang đầu<').findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang đầu[/COLOR]', url, 2, logos + 'hayhd.png')
    match = re.compile("href='(.+?)'>(\d+)<").findall(content)
    for url, inum in match:
      if url=='#':
        pass
      else:  
        addDir('[COLOR lightgreen]Trang ' + inum + '[/COLOR]', url, 2, logos + 'hayhd.png')
    match = re.compile('href="([^"]*)">Trang cuối<').findall(content)
    for url in match:
      addDir('[COLOR red]Trang cuối[/COLOR]', url, 2, logos + 'hayhd.png')
   
def videoLinks(url,name):
  content=makeRequest(url)
  thumbnail=re.compile("<meta property=\"og:image\" content=\"([^\"]*)\"").findall(content)[0]		
  match=re.compile("data-type=\"watch\" data-episode-id.+?href=\"([^\"]*)\" title=\"(.*?)\"").findall(content)
  for url,title in match:
    addLink(('%s   -   %s' % ('[COLOR lime]'+title+'[/COLOR]',name )),('%s%svideo.mp4' % (phim3s, url)),thumbnail)
	
def pgtri():
  #addDir('[COLOR cyan]Phimgiaitri[/COLOR]',pgt,5,logos+'pgt.png')
  content=makeRequest(url)
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[0]  
  addDir('[COLOR yellow]'+match+'[/COLOR]',pgt,2,logos+'pgt.png')			
  match=re.compile('<li class="has-sub"><a href=\'#\'><span>(.+?)<\/span><\/a>').findall(content)[1]		
  addDir('[COLOR lime]'+match+'[/COLOR]',pgt,6,logos+'pgt.png')	
 
def dirs(url):
  content=makeRequest(url) 
  if 'phimgiaitri' in url:
    addDir('[COLOR yellow]phimgiaitri[B]   [COLOR lime]>[COLOR orange]>[COLOR blue]>[COLOR magenta]>   [/B][COLOR yellow]Tìm Phim Bộ[/COLOR]',pgt,9,logos+'pgt.png')
    match=re.compile('<a href=\'result.php\?type=Phim Bộ(.+?)\'><span>(.+?)<\/span>').findall(content) 
    for url,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+'result.php?type=Phim%20B%E1%BB%99'+url.replace(' ','%20'),7,logos+'pgt.png')
  elif 'fptplay' in url:
    match=re.compile("<h3><a href=\"(.+?)\">(.+?)<\/a><\/h3>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name+'[/COLOR]',fptplay+url,mode_opt,logos+'fptplay.png')
	  
def mediaList(url):
  content=makeRequest(url)
  if 'phimgiaitri' in url:  
    match=re.compile('href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><div class=\'text\'>\s*<p>.+?<\/p>\s*<\/div>.+?>([^<]*)\s*<\/').findall(content)
    for url,thumbnail,name in match:
      addDir('[COLOR lime]'+name+'[/COLOR]',pgt+url+'/Tap-1.html',8,pgt+thumbnail)				
    match=re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',pgt+url.replace(' ','%20'),7,logos+'pgt.png')
  elif 'fptplay' in url:
    match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
    for url,thumbnail,name in match:	
      addDir('[COLOR lime]'+name.replace('amp;','')+'[/COLOR]',fptplay+url,8,thumbnail)
    match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,7,logos+'fptplay.png')
  elif 'zui' in url:
    match=re.compile('<a data-tooltip=".+?" href="(.+?)" title="(.+?)".+?>\s*<img src="(.+?)"').findall(content)
    if 'phim-bo' in url:
      for url,name,thumbnail in match:
        addDir('[COLOR yellow]'+name+'[/COLOR]',url,8,thumbnail)
      match=re.compile("<a href=\"([^\"]*)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước').replace(' &raquo;','[COLOR magenta]Kế Tiếp')+'[/COLOR]',url,7,logos+'zui.png')	  
    else:
      for url,name,thumbnail in match:
        add_Link('[COLOR yellow]'+name+'[/COLOR]',url,thumbnail)
      match=re.compile("<a href=\"([^\"]+)\" title='.+?'>([^>]*)<\/a><\/li>").findall(content)
      for url,name in match:
        addDir('[COLOR lime]Trang '+name.replace('&laquo;','[COLOR cyan]Kế Trước').replace(' &raquo;','[COLOR magenta]Kế Tiếp')+'[/COLOR]',url,7,logos+'zui.png')
  elif 'hdcaphe' in url:
    match=re.compile("a style=\"position: relative;display: block;\" href=\"(.+?)\">\s*<img class=\"imgborder\" width=\"165\" src=\"(.+?)\"").findall(content)		
    for url,thumbnail in match:
      addDir('[COLOR lime][UPPERCASE]'+url.replace('detail/movies/','').replace('-',' ').replace('.html','')+'[/UPPERCASE][/COLOR]',hd_caphe+url.replace('detail','video').replace('.html','/play/clip_1.html'),8,hd_caphe+thumbnail)
    match=re.compile("<span class=\"next\"><a href=\"(.+?)\" class=\"next\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+' >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
    match=re.compile("<span class=\"last\"><a href=\"(.+?)\" class=\"last\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]'+name.replace('Go to page','Trang')+'[COLOR cyan][B] = [/B][COLOR red]Trang cuối cùng >>>>[/COLOR]',hd_caphe+url,7,logos+'hdcaphe.png')
  elif 'phimhayhd' in url:
    match = re.compile('data-src="(.+?)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=.+?>(.+?)</span>\s*<span class=".+?"></span>\s*\s*<span class=".+?">\s*(.+?)</span>\s*</div>\s*<div class=".+?">\s*<a href="(.+?)" class="title">(.+?)<').findall(content)
    for thumbnail, cat, temp, url, name in match:
      addDir('[COLOR orange]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, 8, thumbnail)      
    match = re.compile('data-src="(.+?)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?"></span>\s*\s*<span class=".+?">\s*(.+?)</span>\s*</div>\s*<div class=".+?">\s*<a href="(.+?)" class="title">(.+?)<').findall(content)
    for thumbnail, temp, url, name in match:
      addDir('[COLOR lime]' + name + '[/COLOR]', url, 8, thumbnail)
    match = re.compile('href="(.+?)">Trang đầu<').findall(content)
    for url in match:
      addDir('[COLOR cyan]Trang đầu[/COLOR]', url, 7, logos + 'hayhd.png')
    match = re.compile("href='(.+?)'>(\d+)<").findall(content)
    for url, inum in match:
      if url=='#':
        pass
      else:
        addDir('[COLOR lightgreen]Trang ' + inum + '[/COLOR]', url, 7, logos + 'hayhd.png')
    match = re.compile('href="([^"]*)">Trang cuối<').findall(content)
    for url in match:
      addDir('[COLOR red]Trang cuối[/COLOR]', url, 7, logos + 'hayhd.png')
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
	#them dong do de hien thi thumbnail
  
def anhtrang_mediaList(url):
  content=makeRequest(url)
  match=re.compile("<a href=\"([^\"]*)\" title=\"([^\"]+)\"><img src=\"(.+?)\"").findall(content)		
  for url,name,thumbnail in match:
    addDir('[COLOR yellow]'+name+'[/COLOR]',url,14,thumbnail)
  match=re.compile("<a class=\"pagelink\" href=\"(.+?)\">(.+?)<\/a>").findall(content)
  for url,name in match:	
    addDir('[COLOR lime]Trang '+name+'[COLOR cyan] >>>>[/COLOR]',url,12,logos+'anhtrang.png')
  match=re.compile("<a class=\"pagelast\" href=\"([^\"]*)\">(.+?)<\/a>").findall(content)
  for url,name in match:	
    addDir('[COLOR red]Trang '+name.replace('Cuối','[COLOR red]Cuối[COLOR magenta] >>>>')+'[/COLOR]',url,12,logos+'anhtrang.png')

def fpt_img(url):
  content=makeRequest(url)
  match=re.compile("<div class=\"col\">\s*<a href=\"([^\"]+)\">\s*<img src=\"([^\"]*)\" alt=\"(.+?)\"").findall(content)
  for url1,thumbnail,name in match:	
    name=name.replace('amp;','')
    content1=makeRequest(fptplay+url1)	
    match1=re.compile('data="([^"]*)" href.*?onclick.+?<a>(\d+)<').findall(content1)
    for url2,inum in match1:
      #add_Link('%s - %s' % ('[COLOR cyan]Tập '+inum,'[COLOR lime]'+name+'[/COLOR]'),'%s%s' % (fptplay,url2),thumbnail)
      add_Link(('%s - %s' % ('[COLOR cyan]Tập '+inum,'[COLOR lime]'+name+'[/COLOR]')).replace('Tập 1 - ',''),'%s%s' % (fptplay,url2),thumbnail)          
  match=re.compile("<li><a href=\"(.+?)\">(\d+)<\/a><\/li>").findall(content)
  for url,name in match:	
    addDir('[COLOR yellow]Trang '+name+'[/COLOR]',fptplay+url,16,logos+'fptplay.png')         
    
def episodes(url,name):
  content=makeRequest(url)
  if 'phimgiaitri' in url:    
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)
    add_Link('[COLOR yellow]Tập 1  -  [/COLOR]'+name,url,thumbnail[0])
    match=re.compile("<a href=\"(.+?)\" page=(\d+)>").findall(content)
    for url,title in match:
      add_Link('[COLOR yellow]Tập '+title+'  -  '+name+'[/COLOR]',url,thumbnail[0])
  elif 'fptplay' in url:
    title=re.compile('<title>([^\']+)</title>').findall(content)[-1].replace('amp;','')		
    match=re.compile('data="([^"]*)" href.*?onclick.+?<a>(\d+)<').findall(content)
    for url,inum in match:
      add_Link(('%s - %s' % ('[COLOR lime]Tập '+inum,'[COLOR yellow]'+title+'[/COLOR]')).replace('Tập 1 - ',''),('%s%s' % (fptplay, url)),logos+'fptplay.png')
  elif 'zui' in url:
    thumbnail=re.compile("<meta property=\"og:image\" content=\"(.+?)\"").findall(content)[0]		
    match=re.compile('<a id=\'.+?\' href=\'(.+?)\'  >(.+?)<\/a><\/li>').findall(content)
    for url,episode in match:
      add_Link(('%s   -   %s' % ('[COLOR lime]Tập '+episode+'[/COLOR]',name )),zui+url,'http://vncdn.zui.vn'+thumbnail)					
  elif 'hdcaphe' in url:
    add_Link(name,url,logos+'hdcaphe.png')  
    match=re.compile("<a style=\"margin-left:10px\" href=\"(.+?)\"  >(\d+)<\/a>").findall(content)
    for url,title in match:
      add_Link('[COLOR yellow]Tập '+title+'[/COLOR]',hd_caphe+url,logos+'hdcaphe.png')  
  elif 'megabox' in url:
    thumbnail = re.compile ('<link rel="image_src" href="(.+?)"').findall(content)[-1]
    match = re.compile('<option selected="selected"  value="(.+?)">(.+?)<\/option>').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR magenta] - ' + name + '[/COLOR]',megaboxvn + url,thumbnail + '?.jpg')     
    match = re.compile('<option  value="(.+?)">(.+?)<\/option>').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR magenta] - ' + name + '[/COLOR]',megaboxvn + url,thumbnail + '?.jpg') 
  elif 'phimhayhd' in url:
    thumbnail = re.compile('img class="thumbnail" src="(.+?)"').findall(content)[0]
    match = re.compile('href="(.+?)" class="episode.+?">(.+?)<').findall(content)
    for url, title in match:
      add_Link('[COLOR cyan]' + title + '[COLOR lime] - ' + name + '[/COLOR]',url,thumbnail) 
 
def otherMegaList(url):	
  content = makeRequest(url)
  if 'video-clip' in url:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s*\s.+\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')  
  else:
    match = re.compile("title = '(.+?)' href='(.+?)'.+\s.+\s.*\s.+src=\"(.+?)\"").findall(content)
    for title,url,thumbnail in match:
      add_Link('[COLOR lime]' + title + '[/COLOR]',url.replace('/phim-', '/xem-phim-'),thumbnail + '?.jpg')
   
def anhtrang_eps(url,name):
  thumb=makeRequest(url)
  thumbnail=re.compile('meta property="og:image" content="(.+?)"').findall(thumb)[0]
  newurl=url.replace(anhtrang,m_anhtrang)
  content=makeRequest(newurl)  
  add_Link('[COLOR lime]Tập 1'+'[COLOR cyan][B]  -  [/B][/COLOR]'+name,newurl,thumbnail)
  match=re.compile('<a href="(.+?)" class="ep">(.+?)<\/a>').findall(content)
  for url,title in match:
    add_Link('[COLOR lime]Tập '+title+'[COLOR cyan][B]  -  [/B][/COLOR]'+name,url,thumbnail)   
  
def inquiry():
  try:
    keyb=xbmc.Keyboard('', '[COLOR lime]Enter search text[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    if 'Tìm Phim Bộ' in name:  
      url=pgt+'result.php?type=search&keywords='+searchText
      print "Searching URL: "+url	  
      mediaList(url)
    elif 'phimhayhd' in name:
      url = hayhd + 'tim-kiem.html?query=' + searchText
      print "Searching URL: "+url	  
      hayhd_le(url)
  except: pass

def hayhd_le(url):	
  content = makeRequest(url)
  match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*<span class=".+?">(.+?)</span>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
  for thumbnail, cat, url, name in match:
    add_Link('[COLOR cyan]' + name + ' - [COLOR magenta]' + cat + '[/COLOR]', url, thumbnail)   
  match = re.compile('data-src="([^"]*)".+?\s*/>\s*<div class=".+?"></div>\s*</a>\s*\s*</div>\s*<div class=".+?">\s*<a href="([^"]+)" class="title">([^>]*)<').findall(content)
  for thumbnail, url, name in match:
    add_Link('[COLOR yellow]' + name + '[/COLOR]', url,thumbnail)
  
def resolveUrl(url):
  if 'fptplay' in url:
    req=urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
    req.add_header('Referer', fptplay)
    response=urllib2.urlopen(req, timeout=120)
    link=response.read()
    response.close()    
    mediaUrl=link 
  elif 'dangcaphd' in url:
    content=makeRequest(url)
    try:	
	    mediaUrl=re.compile('<a _episode="1" _link="(.+?)_\d_\d+.mp4"').findall(content)[0].replace('demophimle','phimle2112')+'.mp4'	  
    except:
      mediaUrl=re.compile('<a _episode="1" _link="(.+?)"').findall(content)[0].replace(' ','%20')
  elif 'phimgiaitri' in url:
    content=makeRequest(url)	
    match = re.compile('file: "rtmpe:\/\/5318b6e71a98f.streamlock.net(.+?)"').findall(content)[0]  
    if '/media1/' in match:
      mediaUrl = 'http://phimgiaitri.vn/phimtxn/' + match.replace('/media1/mp4:','')
    else:
      mediaUrl = 'http://phimgiaitri.vn:81/phimtxn/' + match.replace('/media2/mp4:','') 
  elif 'zui' in url:
    content=makeRequest(url)
    mediaUrl='rtmp'+re.compile("'rtmp(.+?)'").findall(content)[0]#+'/playlist.m3u8'
  elif 'hdcaphe' in url:
    content=makeRequest(url)	
    mediaUrl=re.compile('\'http.startparam\':\'start\',\s*file: \'(.+?)\'').findall(content)[0].replace(' ','%20')	
  elif 'anhtrang' in url:
    content=makeRequest(url)
    try:
      mediaUrl=re.compile("<source src=\"([^\"]*)\"").findall(content)[0]
    except: 
      mediaUrl=re.compile("var video_src_mv=\"(.+?)\"").findall(content)[0]
  elif 'megabox' in url:
    content=makeRequest(url)
    videoUrl = re.compile('file: "(.+?)"').findall(content)[0]
    if 'youtube' in videoUrl:
      mediaUrl = videoUrl.replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/?action=play_video&videoid=')
    else:
      mediaUrl = videoUrl 
  elif 'phimhayhd' in url:
    content=makeRequest(url)
    mediaUrl = re.compile('"film":{"url":"(.+?)m3u8"').findall(content)[0].replace('\\','')+'m3u8'  
  else:
    mediaUrl = url  
  item=xbmcgui.ListItem(path=mediaUrl)
  xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
  return

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
				  
def addDir(name,url,mode,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  return ok
    
def add_Link(name,url,iconimage):
  u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=10"  
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  liz.setProperty('IsPlayable', 'true')  
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  
  
def addLink(name,url,iconimage):
  ok=True
  liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
  liz.setInfo( type="Video", infoLabels={ "Title": name } )
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
  return ok
                     
params=get_params()
url=None
name=None
mode=None

try:
  url=urllib.unquote_plus(params["url"])
except:
  pass
try:
  name=urllib.unquote_plus(params["name"])
except:
  pass
try:
  mode=int(params["mode"])
except:
  pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)


if mode==None or url==None or len(url)<1:
  #main()
  categories(phim3s)
  #dong nay de goi categories o phan dau
  #xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  #khong duoc them vao dong nay!
elif mode==1:
  search()
		
elif mode==2:
  categories(url)
  
	
elif mode==3:
  index(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
        
elif mode==4:
  videoLinks(url,name)
  #xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  #cai nay hien thi thumbnail phan tap phim

elif mode==5:
  pgtri()
  
elif mode==6:
  dirs(url)
  
elif mode==7:
  mediaList(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  
elif mode==8:
  episodes(url,name)
  
  
elif mode==9:
  inquiry()
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)

elif mode==10:
  resolveUrl(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
 
elif mode==11:
  megavn(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  
  
elif mode==12:
  anhtrang_mediaList(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  

elif mode==13:
  megaListEps(url) 
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  
elif mode==14:
  anhtrang_eps(url,name)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
 

elif mode==15:
  otherMegaList(url)
  xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)

elif mode==16:
  fpt_img(url)

  
elif mode==17:
  mysettings.openSettings()
  
xbmcplugin.endOfDirectory(int(sys.argv[1]))