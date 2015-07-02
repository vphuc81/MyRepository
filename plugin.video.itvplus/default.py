#!/usr/bin/python
#coding=utf-8
import xbmc,xbmcaddon,xbmcplugin,xbmcgui,sys,urllib,urllib2,re,os,codecs,unicodedata,base64
import simplejson as json

addonID = 'plugin.video.itvplus'
addon = xbmcaddon.Addon(addonID)
pluginhandle = int(sys.argv[1])
home = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
logos = xbmc.translatePath(os.path.join(home,"logos\\"))
dataPath = xbmc.translatePath(os.path.join(home, 'resources'))
csn    = 'http://chiasenhac.com/'
hdcaphe = 'http://phim.hdcaphe.com/'
megaboxvn = 'http://phim.megabox.vn/'
pgt = 'http://phimgiaitri.vn/'
vp9 = 'http://f.vp9.tv/music/'
tvreplay = 'http://113.160.49.39/tvcatchup/'
woim = 'http://www.woim.net/'

def Home():
    content = Get_Url(DecryptData(homeurl))
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)	
    for title,url,thumbnail in match:
        if 'tvcatchup' in url:
          addDir(title,url,'medialist',logos+thumbnail)
        elif 'MYPLAYLIST' in url:
          pass		  
        else:	
          addDir(title,url,'menu_group',logos+thumbnail)
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(51)')	  
    else:
        xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
		
def Menu_Group(url):
    if 'MenuTV' in url:
      content = Get_Url(url)
      match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
      for title,url,thumbnail in match:	
        addDir(title,url,'indexgroup',thumbnail)
      skin_used = xbmc.getSkinDir()	  
      if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(52)')
      else:
        xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)		
    elif 'MenuShows' in url:
      content = Get_Url(url)
      match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
      for title,url,thumbnail in match:
	    if 'xml' in url:
	      addDir(title,url,'index_group',thumbnail)
	    elif 'm3u' in url:
	      addDir(title,url,'get_m3u',thumbnail)
    elif 'MenuMusic' in url:
      content = Get_Url(url)
      match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
      for title,url,thumbnail in match:
	    if 'LIVESHOWS' in url:
	      addDir(title,url,'index_group',thumbnail)
	    elif 'm3u' in url:
	      addDir(title,url,'get_m3u',thumbnail)
	    elif 'ott.thuynga' in url:
	      addDir(title,url,'categories',thumbnail)
	    else:
	      addDir(title,url,'medialist',thumbnail)		  
    elif 'MenuMovie' in url:
      content = Get_Url(url)
      match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(content)
      for title,url,thumbnail in match:
	    addDir(title,url,'categories',thumbnail)	  
    elif 'MenuTube' in url:
	  content = Get_Url(url)
	  names = re.compile('<name>(.+?)</name>\s*<thumbnail>(.+?)</thumbnail>').findall(content)
	  for name,thumb in names:
	    addDir(name, url+"?n="+name, 'index', thumb)	  
    elif 'SEARCH' in url:
	  addDir('Tìm Video Nhạc','TimVideo','search',logos+'MUSIC.png')
	  addDir('Tìm Album Nhạc Không Lời','TimAlbum','search',logos+'MUSIC.png')	  
	  addDir('Tìm Phim (Kho Phim 1)','TimPhim1','search',logos+'MOVIE.png')
	  addDir('Tìm Phim (Kho Phim 2)','TimPhim2','search',logos+'MOVIE.png')
	  addDir('Tìm Phim (Kho Phim 3)','TimPhim3','search',logos+'MOVIE.png')	  

def Categories(url):
    if 'megabox' in url:	  
      match=menulist(dataPath+'/data/Categories.xml')
      for title,url,thumbnail in match:
        if 'phim-lenew' in url:
          addDir(title,url.replace('new',''),'episodes',thumbnail)
        elif 'phim-bonew' in url:
          addDir(title,url.replace('new',''),'episodes',thumbnail)
        elif 'chieu-rap' in url:
          addDir(title,url,'episodes',thumbnail)		  
        elif 'phim-le' in url:
          addDir(title,url,'medialist',thumbnail)
        elif 'phim-bo' in url:
          addDir(title,url,'medialist',thumbnail)
        else:
          pass		  
    elif 'hdcaphe' in url:    
      match=menulist(dataPath+'/data/Categories.xml')
      for title,url,thumbnail in match:
        if 'hdcaphe' in url:
          addDir(title,url,'medialist',thumbnail)
        else:
          pass
    elif 'phimgiaitri' in url:    
      match=menulist(dataPath+'/data/Categories.xml')
      for title,url,thumbnail in match:
        if 'phimgiaitri' in url:
          addDir(title,url,'medialist',thumbnail)
        else:
          pass		  
    elif 'ott.thuynga' in url:
      match=menulist(dataPath+'/data/Categories.xml')
      for title,url,thumbnail in match:	  
        if 'ott.thuynga' in url:
          addDir(title,url,'episodes',thumbnail)
        else:
          pass

def Search(url): 	
  try:
    keyb=xbmc.Keyboard('', '[COLOR lime]Nhập nội dung cần tìm kiếm[/COLOR]')
    keyb.doModal()
    if (keyb.isConfirmed()):
      searchText=urllib.quote_plus(keyb.getText())
    if 'TimVideo' in url:  
      url=csn+'search.php?s='+searchText+'&cat=video'      
      Search_Result(url)
    elif 'TimAlbum' in url:  
      url=woim+'search/album/'+searchText.replace('+', '-')+'.html'      
      Search_Result(url)	  
    elif 'TimPhim1' in url:
      url = hdcaphe + 'search-result.html?keywords=' + searchText
      Search_Result(url)
    elif 'TimPhim2' in url:  
      url=megaboxvn + 'search/index?keyword=' + searchText.replace('+', '-')      
      Search_Result(url)
    elif 'TimPhim3' in url:  
      url = pgt+'result.php?type=search&keywords='+searchText      
      Get_Medialist(url,iconimage)	  
  except:
    pass	

def Search_Result(url):
    content = Get_Url(url)
    if 'megabox' in url:
	  try:
		match = re.compile('src="(.+?)">\s*<span class="features">\s*</span>\s*</a>\s*<div class="meta">\s*<h3 class="H3title">\s*<a href="(.+?)">(.+?)</a>').findall(content)
		for thumb, href, title in match:
		  add_Link('[COLOR FF0084EA](Phim Lẻ)[/COLOR] ' +title, href, thumb)
	  except:
		  pass	
	  try:
		match = re.compile('src="(.+?)">\s*<span class=\'esp\'>.+?<span class="features">\s*</span>\s*</a>\s*<div class="meta">\s*<h3 class="H3title">\s*<a href="(.+?)">(.+?)</a>').findall(content)
		for thumb, href, title in match:
		  addDir('[COLOR orange](Phim Bộ)[/COLOR] ' +title, href, 'get_listep', thumb)
	  except:
		  pass
    elif 'hdcaphe' in url:
      match = re.compile("a style=\"position: relative;display: block;\" href=\"(.+?)\">\s*<img class=\"imgborder\" width=\"165\" src=\"(.+?)\"").findall(content)		
      for url,thumbnail in match:
        addDir('[UPPERCASE]' + url.replace('detail/movies/','').replace('-',' ').replace('.html','') + '[/UPPERCASE]',hdcaphe + url.replace('detail','video').replace('.html','/play/clip_1.html'),'episodes',hdcaphe + thumbnail)
    elif 'chiasenhac' in url:	
      match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(content)
      for url,name,thumbnail in match:
        add_Link(name.replace(';',' +'),(csn+url),thumbnail)
      match=re.compile("href=\"(.+?)\" class=\"npage\">(\d+)<").findall(content)
      for url,name in match:
        addDir('[COLOR red]Trang '+name+'[/COLOR]',url.replace('&amp;','&'),'search_result',logos+'NEXT.png')
    elif 'woim' in url:
      match=re.compile('href="(.+?)" title="(.+?)" target="_blank"><img src="(.+?)"').findall(content)
      for url,name,thumb in match:
        addDir(name,url,'get_listep',thumb)	
		
def Get_Medialist(url,iconimage):
  content=Get_Url(url) 
  if 'chiasenhac' in url: 	  		
    match=re.compile("<a href=\"hd(.+?)\" title=\"([^\"]*)\"").findall(content)[1:8]
    for url,name in match:
	  addDir(name.replace('Video','[COLOR ffff0000]Video[/COLOR]'),csn+'hd'+url,'episodes',iconimage)
  elif 'hdcaphe' in url:
    match = re.compile("a style=\"position: relative;display: block;\" href=\"(.+?)\">\s*<img class=\"imgborder\" width=\"165\" src=\"(.+?)\"").findall(content)		
    for url,thumbnail in match:
      addDir('[UPPERCASE]' + url.replace('detail/movies/','').replace('-',' ').replace('.html','') + '[/UPPERCASE]',hdcaphe + url.replace('detail','video').replace('.html','/play/clip_1.html'),'episodes',hdcaphe + thumbnail)
    match = re.compile("<span class=\"next\"><a href=\"(.+?)\" class=\"next\" title=\"(.+?)\">").findall(content)
    for url,name in match:	
      addDir('[COLOR yellow]' + name.replace('Go to page','Trang Tiếp Theo') + '[/COLOR]',hdcaphe + url,'medialist',logos+'NEXT.png')  
  elif 'tvcatchup' in url:
    content = Get_Url(url)
    match = re.compile('href="(\d+)/">(\d+)/<').findall(content)
    for url,name in match:
      addDir(name,tvreplay+url,'episodes',iconimage)
  elif 'woim' in url:
    match=re.compile('href="/the-loai(.+?)">(.+?)<').findall(content)
    for url,name in match:
      addDir(name, '%sthe-loai%s' % (woim,url),'episodes',iconimage)
    match=re.compile('href=".+?/nhac-cu(.+?)">(.+?)<').findall(content)
    for url,name in match:
      addDir(name, '%snhac-cu%s' % (woim,url),'episodes',iconimage)
  elif 'f.vp9.tv' in url:
    content = Get_Url(url)
    match=re.compile('href="(.*?)">(.*?)/<').findall(content)
    for url,name in match:
      name=name.replace('nhac_au_my','Nhạc Âu Mỹ').replace('nhac_han','Nhạc Hàn').replace('nhac_tre','Nhạc Trẻ').replace('nhac_vang','Nhạc Vàng').replace('thieu_nhi','Nhạc Thiếu Nhi').replace('tru_tinh','Nhạc Trữ Tình')
      if 'music_channel' in name:
        pass
      else:			
        addDir(name,vp9+url,'episodes',iconimage)
  elif 'megabox' in url:
	if 'phim-le' in url:	
	  match = re.compile("href='phim-le(.+?)'>(.+?)<").findall(content) 
	  for href, name in match:
	    if 'Phim'in name:
		  pass
	    else:
		  addDir('Phim '+name, url + href, 'episodes', iconimage)		
	elif 'phim-bo' in url:
	  match = re.compile("href='phim-bo(.+?)'>(.+?)<").findall(content) 
	  for href, name in match:
	    if 'Phim'in name:
		  pass
	    else:
		  addDir('Phim '+name, url + href, 'episodes', iconimage)
  elif 'phimgiaitri' in url:
    match = re.compile('<a style=\'text-decoration:none\' href=\'([^\']*).html\'>\s*<img style=.+?src=(.+?) ><table style.+?:0px\'>(.+?)\s*<\/font>').findall(content)
    for url,thumbnail,name in match:
      add_Link(name,pgt+url+'/Tap-1.html',pgt+thumbnail)
    match = re.compile("<a  href='(.+?)'>(\d+)  <\/a>").findall(content) 
    for url,name in match:
      addDir('[COLOR lime]Trang tiếp theo '+name+'[/COLOR]',pgt+url.replace(' ','%20'),'medialist',logos + 'NEXT.png')

  
def Get_Episodes(url):
  content = Get_Url(url)
  if 'youtube' in url:
	add_Link(name, url, thumbnail)
  elif 'chiasenhac' in url:		
    match=re.compile("<a href=\"([^\"]*)\" title=\"(.*?)\"><img src=\"([^\"]+)\"").findall(content)
    for url,name,thumbnail in match:
      add_Link(name,(csn+url),thumbnail)
    match=re.compile("<a href=\"hd\/video\/([a-z]-video\/new[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR lime]Trang Mới Chia Sẻ '+name+'[/COLOR]',csn+'hd/video/'+url+'.html','episodes',logos+'NEXT.png')
    match=re.compile("<a href=\"hd\/video\/([a-z]-video\/down[0-9]+).html\" class=\"npage\">(\d+)<\/a>").findall(content)
    for url,name in match:
      addDir('[COLOR red]Trang Download Mới Nhất '+name+'[/COLOR]',csn+'hd/video/'+url+'.html','episodes',logos+'NEXT.png')
  elif 'ott.thuynga' in url:
	match=re.compile("style=\"background-image: url\('(.+?)'\)\">\s*<span class.+?</span>\s.+\s.+\s.+\s*<a href=\"(.+?)\">(.+?)<").findall(content)
	for thumbnail,url,name in match:
	  add_Link(name,'http://ott.thuynga.com/'+url,thumbnail+'?.jpg')
	match=re.compile('href="http://ott.thuynga.com/([^>]+)">(\d+)<').findall(content)	
	for url,name in match:
	  addDir('[COLOR lime]Trang ' + name + '[/COLOR]','http://ott.thuynga.com/'+url,'episodes',logos+'NEXT.png')
  elif 'hdcaphe' in url:
    add_Link('[UPPERCASE]' +url.replace('http://phim.hdcaphe.com/','').replace('video/movies/','').replace('-',' ').replace('/play/clip_',' - Tập ').replace('.html','')+ '[/UPPERCASE]',url,iconimage)  
    match = re.compile("<a style=\"margin-left:10px\" href=\"(.+?)\"  >(\d+)<\/a>").findall(content)
    for url,title in match:
      #title=title.split('.')[-1]
      add_Link('[UPPERCASE]' +url.replace('video/movies/','').replace('-',' ').replace('/play/clip_',' - Tập ').replace('.html','')+ '[/UPPERCASE]',hdcaphe + url,iconimage)
  elif 'tvcatchup' in url:
    match=re.compile('<a href="(.+?)">(.+?)\.mp4</a>').findall(content)
    for href,name in match:
      name=name.split('_')
      name=name[0]+'_'+name[-1]
      if 'VTV1' in name:
        add_Link(name,url+'/'+href,logos+'VTV1.png')
      elif 'VTV2' in name:
        add_Link(name,url+'/'+href,logos+'VTV2.png')
      elif 'VTV3' in name:
        add_Link(name,url+'/'+href,logos+'VTV3.png')
      elif 'VTV6' in name:
        add_Link(name,url+'/'+href,logos+'VTV6.png')
      elif 'TODAYTV' in name:
        add_Link(name,url+'/'+href,logos+'TODAY-TV.png')		
      elif 'HBO' in name:
        add_Link(name,url+'/'+href,logos+'HBO.png')
      elif 'STARMOVIES' in name:
        add_Link(name,url+'/'+href,logos+'STARMOVIES.png')		
  elif 'woim' in url:
    match=re.compile('<li>\s*<a href="([^"]*)" title="([^"]+)".+?src="(.+?)&w').findall(content)
    for url,name,thumb in match:
      addDir('[COLOR red]Album[/COLOR] : ' + name,url ,'get_listep',thumb)
  elif 'f.vp9.tv' in url:
    match=re.compile('href="(.*?)">(.*?)/<').findall(content)
    for href,name in match:
	  if 'upload' in name: 
	    pass
	  else: 
	    add_Link(name.replace('-',' [COLOR ffff0000]-[/COLOR] ').replace('_',' ').replace('.',' '),url+href,logos+'VMUSIC.png')
  elif 'megabox' in url:
	match = re.compile('src="(.+?)">\s*.*<span class="features">\s*</span>\s*</a>\s*<div class="meta">\s*<h3 class="H3title">\s*<a href="(.+?)">(.+?)</a>').findall(content)
	for thumb, href, title in match:
	  if 'phim-bo' in url:
		addDir(title, href,'get_listep', thumb)
	  else:	
		try:
		  add_Link(title, href, thumb)
		except: 
		  pass		
	try:	
	  match = re.compile('class="next"><a href="(.+?)">').findall(content)
	  addDir('[COLOR red]Trang Tiếp Theo[/COLOR]', megaboxvn + match[0],'episodes', logos + 'NEXT.png')	
	except: 
	  pass
		  
def Get_ListEp(url,name):
  content = Get_Url(url)
  if 'woim' in url:
    thumb=re.compile('img itemprop="image" src="(.+?)&w').findall(content)[0]
    match=re.compile('ascii" value="([^"]*)".+?\s.+\s.+\s.+\s.+\s*\s.+href=".+?download/(.+?).html').findall(content)
    for name,url in match:
      url=urllib2.urlopen(woim+'ma/'+url)
      link=url.geturl()         
      url.close()
      link=urllib.unquote (link)
      link=link[40:len(link)-23]
      content = Get_Url(link)
      match=re.compile('location="(.+?)"').findall(content)[-1]  
      add_Link(name.upper(),match,thumb)
  elif 'megabox' in url:
	match = re.compile("href='(.+?)' >(\d+)<").findall(content)
	for url, title in match:
	  add_Link('Tập ' + title, url, iconimage)

def Get_M3U(url,iconimage):
  m3ucontent = Get_Url(url)
  match = re.compile('#EXTINF:-?\d,(.+?)\n(.+)').findall(m3ucontent)
  for name,url in match:
	  add_Link(name.replace('TVSHOW - ','').replace('MUSIC - ',''),url,iconimage)
	  
def Index(url,iconimage):
    byname = url.split("?n=")[1]
    url = url.split("?")[0]
    xmlcontent = GetUrl(url)
    channels = re.compile('<channel>(.+?)</channel>').findall(xmlcontent)
    for channel in channels:
        if byname in channel:
            items = re.compile('<item>(.+?)</item>').findall(channel)
            for item in items:
                thumb=""
                title=""
                link=""
                if "/title" in item:
                    title = re.compile('<title>(.+?)</title>').findall(item)[0]
                if "/link" in item:
                    link = re.compile('<link>(.+?)</link>').findall(item)[0]
                if "/thumbnail" in item:
                    thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                if "youtube" in link:					
                    addDir(title, link, 'episodes', thumb)
                else:					
                    addLink('' + title + '', link, 'play', thumb)
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(50)')
		
def IndexGroup(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            add_Link(title, link, thumb)
        skin_used = xbmc.getSkinDir()
        if skin_used == 'skin.xeebo':
            xbmc.executebuiltin('Container.SetViewMode(52)')
        else:
            xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)			
    else:
        for name in names:
            addDir('' + name + '', url+"?n="+name, 'index', '')

def Index_Group(url):
	xmlcontent = GetUrl(url)
	names = re.compile('<name>(.+?)</name>\s*<thumbnail>(.+?)</thumbnail>').findall(xmlcontent)
	if len(names) == 1:
		items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
		for item in items:
			thumb=""
			title=""
			link=""
			if "/title" in item:
				title = re.compile('<title>(.+?)</title>').findall(item)[0]
			if "/link" in item:
				link = re.compile('<link>(.+?)</link>').findall(item)[0]
			if "/thumbnail" in item:
				thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
			addLink(title, link, 'play', thumb)
		skin_used = xbmc.getSkinDir()
		if skin_used == 'skin.xeebo':
				xbmc.executebuiltin('Container.SetViewMode(50)')
	else:
		for name,thumb in names:
			addDir(name, url+"?n="+name, 'index', thumb)

def menulist(homepath):
  try:
    mainmenu=open(homepath, 'r')  
    link=mainmenu.read()
    mainmenu.close()
    match=re.compile("<title>([^<]*)<\/title>\s*<link>([^<]+)<\/link>\s*<thumbnail>(.+?)</thumbnail>").findall(link)
    return match
  except:
    pass
	
def resolveUrl(url):
	if 'xemphimso' in url:
		content = Get_Url(url)	
		url = urllib.unquote_plus(re.compile("file=(.+?)&").findall(content)[0])
	elif 'vtvplay' in url:
		content = Get_Url(url)
		url = content.replace("\"", "")
		url = url[:-5]
	elif 'vtvplus' in url:
		content = Get_Url(url)
		url = re.compile('var responseText = "(.+?)";').findall(content)[0]		
	elif 'htvonline' in url:
		content = Get_Url(url)	
		url = re.compile("file: \"([^\"]*)\"").findall(content)[0]
	elif 'hplus' in url:
		content = Get_Url(url)	
		url = re.compile('iosUrl = "(.+?)";').findall(content)[0]
	elif 'megabox' in url:
		content = Get_Url(url)	
		url = re.compile('var iosUrl = "(.+?)"').findall(content)[0]+'|User-Agent=Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0'		
	elif 'chiasenhac' in url:
		content = Get_Url(url)
		try:
		  url = re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(content)[0].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
		except:
		  url = re.compile("\"hd-2\".+?\"([^\"]+)\"").findall(content)[-1].replace('%3A',':').replace('%2F','/').replace('%2520','%20')
	elif 'hdcaphe' in url:
		content = Get_Url(url)	
		url=re.compile('\'http.startparam\':\'start\',\s*file: \'(.+?)\'').findall(content)[0].replace(' ','%20')

	elif 'f.vp9.tv' in url:
		content = Get_Url(url)
		try:
		  try:
		    url = url+re.compile('<a href="(.*?)HV.mp4"').findall(content)[0]+'HV.mp4'
		  except:
		    url = url+re.compile('<a href="(.*?)mvhd.mp4"').findall(content)[0]+'mvhd.mp4'
		except:
		  url = url+re.compile('<a href="(.*?)mv.mp4"').findall(content)[0]+'mv.mp4'
	elif 'ott.thuynga' in url:
		content = Get_Url(url)	
		url=re.compile("var iosUrl = '(.+?)'").findall(content)[0]
	elif 'phimgiaitri' in url:
		#xbmc.log(url)	
		arr = url.split('/')
		print arr
		phimid = arr[len(arr) - 3]
		print phimid
		tap = arr[len(arr) - 1]
		print tap
		tap2 = tap.split('-')
		print tap2		
		tap3 = tap2[1].split('.')
		print tap3		
		tap = tap3[0]
		print tap		
		url2 = 'http://120.72.85.195/phimgiaitri/mobile/service/getep3.php?phimid=' + phimid
		print url2
		content = Get_Url(url2)
		print content
		content = content[3:]
		print content
		infoJson = json.loads(content)
		tapindex = int(tap) -1
		link = infoJson['ep_info'][tapindex]['link']
		link = link.replace('#','*')
		url3 ='http://120.72.85.195/phimgiaitri/mobile/service/getdireclink.php?linkpicasa=' + link
		print url3
		content = Get_Url(url3)
		print content		
		content = content[3:]
		linkJson = json.loads(content)
		url = linkJson['linkpi'][0]['link720'] or linkJson['linkpi'][0]['link360']
	else:
		url = url
	item=xbmcgui.ListItem(path=url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)	  
	return

def PlayVideo(url,title):
    if(url.find("youtube") > 0):
        vidmatch=re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(url)
        vidlink=vidmatch[0][len(vidmatch[0])-1].replace('v/','')
        url = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + vidlink.replace('?','')
        xbmc.executebuiltin("xbmc.PlayMedia("+url+")")	
    else:
        title = urllib.unquote_plus(title)
        playlist = xbmc.PlayList(1)
        playlist.clear()
        listitem = xbmcgui.ListItem(title)
        listitem.setInfo('video', {'Title': title})
        xbmcPlayer = xbmc.Player()
        playlist.add(url, listitem)
        xbmcPlayer.play(playlist)

def Get_Url(url):
    try:
		req=urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
		response=urllib2.urlopen(req)
		link=response.read()
		response.close()  
		return link
    except:
		pass
    
def GetUrl(url):
    link = ""
    if os.path.exists(url)==True:
        link = open(url).read()
    else:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    link = ''.join(link.splitlines()).replace('\'','"')
    link = link.replace('\n','')
    link = link.replace('\t','')
    link = re.sub('  +',' ',link)
    link = link.replace('> <','><')
    return link
	
def add_Link(name,url,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode=stream"+"&iconimage="+urllib.quote_plus(iconimage)
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty('IsPlayable', 'true')  
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)  

def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
    return ok
	
def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    if ('www.youtube.com/user/' in url) or ('www.youtube.com/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok	
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok	
	
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

DecryptData = base64.b64decode	
homeurl = 'aHR0cDovL3hibWMuaXR2cGx1cy5uZXQvTUVOVS9JLU1lbnUueG1s'
params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
name=params.get('name')
iconimage=None

try:
  iconimage=urllib.unquote_plus(params["iconimage"])
except:
  pass

if type(url)==type(str()):
    url=urllib.unquote_plus(url)
sysarg=str(sys.argv[1])

if mode == 'index':Index(url,iconimage)
elif mode == 'indexgroup':IndexGroup(url)	
elif mode == 'index_group':Index_Group(url)	
elif mode == 'menu_group':Menu_Group(url)
elif mode == 'categories':Categories(url)
elif mode == 'medialist':Get_Medialist(url,iconimage)
elif mode == 'episodes':Get_Episodes(url)
elif mode == 'get_listep':Get_ListEp(url,name)	
elif mode == 'get_m3u':Get_M3U(url,iconimage)
elif mode == 'search_result':Search_Result(url)
elif mode == 'search':Search(url)
	
elif mode=='stream' or mode=='play':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('ITV Plus', 'Đang tải. Vui lòng chờ trong giây lát...')
    resolveUrl(url)
    dialogWait.close()
    del dialogWait	

else:Home()
xbmcplugin.endOfDirectory(int(sysarg))