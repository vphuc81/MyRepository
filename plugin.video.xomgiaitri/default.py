#!/usr/bin/python
# coding=utf8

import xbmc, xbmcaddon, xbmcplugin, xbmcgui
import os, re, sys, urllib, urllib2

addonID      = 'plugin.video.xomgiaitri'
addon        = xbmcaddon.Addon(addonID)
pluginhandle = int(sys.argv[1])
defaultIcon  = xbmc.translatePath('special://home/addons/'+addonID+'/icon.png')

def Home():
	addDir('Phim Bộ', 'http://www.xom68.com/xem/the-loai/phim-bo', 'index', defaultIcon)
	addDir('Phim Bộ theo Quốc Gia', 'http://www.xom68.com/', 'videosbyregion', defaultIcon)
	addDir('Phim Lẻ', 'http://www.xom68.com/xem/the-loai/phim-dien-anh', 'index', defaultIcon)
	addDir('Phim Lẻ theo Thể Loại', 'http://www.xom68.com/', 'videosbycategory', defaultIcon)
	addDir('[ Tìm Kiếm ]', 'http://www.xom68.com/xem/search/%s/1.html', 'search', defaultIcon)

def SeriesByCountry():
	addDir('Việt Nam', 'http://www.xom68.com/xem/category/5/phim-bo-viet-nam.html', 'index', defaultIcon)
	addDir('Hồng Kong', 'http://www.xom68.com/xem/category/1/phim-bo-hong-kong.html', 'index', defaultIcon)
	addDir('Hồng Kong (VNLT)', 'http://www.xom68.com/xem/category/28/phim-bo-hong-kong-vnlt.html', 'index', defaultIcon)
	addDir('Hàn Quốc', 'http://www.xom68.com/xem/category/4/phim-bo-han-quoc.html', 'index', defaultIcon)
	addDir('Hàn Quốc (vietsub)', 'http://www.xom68.com/xem/category/29/phim-bo-han-quoc-vietsub.html', 'index', defaultIcon)
	addDir('Trung Quốc', 'http://www.xom68.com/xem/category/2/phim-bo-trung-quoc.html', 'index', defaultIcon)
	addDir('Đài Loan', 'http://www.xom68.com/xem/category/3/phim-bo-dai-loan.html', 'index', defaultIcon)
	addDir('Thái Lan', 'http://www.xom68.com/xem/category/22/phim-bo-thai-lan.html', 'index', defaultIcon)
	addDir('Các Loại Khác', 'http://www.xom68.com/xem/category/7/cac-loai-khac.html', 'index', defaultIcon)

def MoviesByCategory():
	addDir('Hành Động', 'http://www.xom68.com/xem/category/8/hanh-dong.html', 'index', defaultIcon)
	addDir('Tình Cảm', 'http://www.xom68.com/xem/category/9/tinh-cam.html', 'index', defaultIcon)
	addDir('Phim Hài', 'http://www.xom68.com/xem/category/10/phim-hai.html', 'index', defaultIcon)
	addDir('Kinh Dị', 'http://www.xom68.com/xem/category/11/kinh-di.html', 'index', defaultIcon)
	addDir('Kiếm Hiệp', 'http://www.xom68.com/xem/category/12/kiem-hiep.html', 'index', defaultIcon)
	addDir('Việt Nam', 'http://www.xom68.com/xem/category/15/viet-nam.html', 'index', defaultIcon)
	addDir('Hài Kịch', 'http://www.xom68.com/xem/category/16/hai-kich.html', 'index', defaultIcon)
	addDir('Ca Nhạc', 'http://www.xom68.com/xem/category/17/ca-nhac.html', 'index', defaultIcon)
	addDir('Cải Lương', 'http://www.xom68.com/xem/category/18/cai-luong.html', 'index', defaultIcon)
	addDir('Phóng Sự', 'http://www.xom68.com/xem/category/19/phong-su.html', 'index', defaultIcon)
	addDir('TV Show', 'http://www.xom68.com/xem/category/32/TV-show.html', 'index', defaultIcon)
	addDir('Các Loại Khác', 'http://www.xom68.com/xem/category/20/cac-loai-khac.html', 'index', defaultIcon)

def Index(url):
	link = GetUrl(url)
	vidlist = re.compile('<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>').findall(link)
	for vurl, vnamefull, vthumb in vidlist:
		addDir("[B]" + vnamefull + "[/B]", "http://www.xom68.com/xem" + vurl, 'mirrors', vthumb)
	navmatch = re.compile('<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>').findall(link.replace("'", '"'))
	for vurl, vname in navmatch:
		addDir(vname, vurl.replace("./", "http://www.xom68.com/xem/"), 'index', "")

def Search():
	try:
		keyb = xbmc.Keyboard('', 'Enter search text')
		keyb.doModal()
		if(keyb.isConfirmed()):
			searchText= urllib.quote_plus(keyb.getText())
		Index(url % searchText)
	except: pass

def Mirrors(url):
	mirrorlink = GetVidPage(url)
	link = GetUrl(mirrorlink)
	serverlist = re.compile('<span class="name"[^>]*>(.+?)</span>').findall(link)
	for i in range(len(serverlist)):
		items = []
		if not any (x in serverlist[i] for x in items):
			addDir("[%d] - %s" %(i + 1, serverlist[i]), mirrorlink.encode("utf-8"), 'episodes', "")

def Episodes(url, name):
	link = GetUrl(url)
	match = re.compile('\d+').findall(name.split("] - ")[0])[0]
	name = name.split("] - ")[1]
	servlist = re.compile('<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % urllib2.unquote(name)).findall(link)[0]
	epilist = re.compile('<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>').findall(servlist)
	if "episode_bg_2" in servlist:
		episode = re.compile('<font class="episode_bg_2">(.+?)</font>').findall(servlist)
		addLink("Part - " + episode[0].replace("&nbsp;", "").strip().encode("utf-8"), url, 'loadvideo', '', name.encode("utf-8"))
	for vlink, vlinkname in epilist:
		addLink("Part - " + vlinkname.replace("&nbsp;", "").strip().encode("utf-8"), "http://www.xom68.com/xem/" + vlink, 'loadvideo', '', name.encode("utf-8"))

def GetVidPage(url):
	url = GetUrl(url)
	return re.compile('<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">').findall(url)[0]

def LoadVideos(url, name):
	link = GetUrl(url)
	if("proxy.link" in link):
		match = re.compile("'proxy.link', '(.+?)'").findall(link)
		link = GetUrl(match[0])
	match = re.compile('<source src="(.+?)" type="video/mp4">').findall(link)
	video = xbmcgui.ListItem(name)
	video.setProperty("IsPlayable", "true")
	video.setPath(match[0])
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, video)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, video)

def GetUrl(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
	req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	response = urllib2.urlopen(req)
	link = response.read()
	response.close()
	link = ''.join(link.splitlines()).replace('\'', '"')
	link = link.replace('\n', '')
	link = link.replace('\t', '')
	link = re.sub('  +', ' ', link)
	link = link.replace('> <', '><')
	return link

def addLink(name, url, mode, iconimage, mirrorname):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&mirrorname=" + urllib.quote_plus(mirrorname)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo(type = "Video", infoLabels = { "Title": name })
	liz.setProperty("IsPlayable", "true")
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
	return ok

def addDir(name, url, mode, iconimage):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo(type = "Video", infoLabels = { "Title": name })
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def parameters_string_to_dict(parameters):
	paramDict = { }
	if parameters:
		paramPairs = parameters[1:].split("&")
		for paramsPair in paramPairs:
			paramSplits = paramsPair.split('=')
			if(len(paramSplits)) == 2:
				paramDict[paramSplits[0]] = paramSplits[1]
	return paramDict

params = parameters_string_to_dict(sys.argv[2])
mode = params.get('mode')
url = params.get('url')
name = params.get('name')

if type(url) == type(str()):
	url = urllib.unquote_plus(url)

if type(name) == type(str()):
	name = urllib.unquote_plus(name)
sysarg = str(sys.argv[1])

if mode == 'index':
	Index(url)
elif mode == 'search':
	Search()
elif mode == 'videosbyregion':
	SeriesByCountry ()
elif mode == 'videosbycategory':
	MoviesByCategory()
elif mode == 'mirrors':
	Mirrors(url)
elif mode == 'episodes':
	Episodes(url, name)
elif mode == 'loadvideo':
	dialogWait = xbmcgui.DialogProgress()
	dialogWait.create('XomGiaiTri.com', 'Loading video. Please wait...')
	LoadVideos(url, name)
	dialogWait.close()
	del dialogWait
else:
	Home()

xbmcplugin.endOfDirectory(int(sysarg))