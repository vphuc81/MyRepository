#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, xbmcplugin, xbmcgui
import os, re, requests, sys, urllib, urllib2

addonID      = 'plugin.video.v137.phimnhanh'
addon        = xbmcaddon.Addon(addonID)
addondir     = xbmc.translatePath(addon.getAddonInfo('path') ) 
pluginhandle = int(sys.argv[1])
skin_used    = xbmc.getSkinDir()
domain       = 'http://phimnhanh.com'


def Home():
	addDir('Phim mới', 'http://phimnhanh.com/phim-moi', 'index', os.path.join(addondir, 'icons', 'new.png'), '')
	addDir('Phim hot', 'http://phimnhanh.com/phim-hot', 'index', os.path.join(addondir, 'icons', 'hot.png'), '')
	addDir('Phim lẻ', 'http://phimnhanh.com/phim-le', 'index', os.path.join(addondir, 'icons', 'movies.png'), '')
	addDir('Phim bộ', 'http://phimnhanh.com/phim-bo', 'index', os.path.join(addondir, 'icons', 'series.png'), '')
	addDir('Phim chiếu rạp', 'http://phimnhanh.com/phim-chieu-rap', 'index', os.path.join(addondir, 'icons', 'intheatres.png'), '')
	addDir('Phim năm 2016', 'http://phimnhanh.com/nam-san-xuat/2016', 'index', os.path.join(addondir, 'icons', '2016.png'), '')
	addDir('-- Thể loại --', 'http://phimnhanh.com/the-loai/', 'genres', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('-- Quốc gia --', 'http://phimnhanh.com/quoc-gia/', 'countries', os.path.join(addondir, 'icons', 'countries.png'), '')
#	addDir('-- Năm sản xuất --', 'http://phimnhanh.com/nam-san-xuat/', 'years', os.path.join(addondir, 'icons', 'years.png'), '')
	addDir('[ Năm sản xuất ]', 'http://phimnhanh.com/nam-san-xuat/', 'search', os.path.join(addondir, 'icons', 'years.png'), '')
	addDir('-- Chủ đề --', 'http://phimnhanh.com/chu-de/', 'topics', os.path.join(addondir, 'icons', 'topics.png'), '')
	addDir('[ Tìm Kiếm ]', 'http://phimnhanh.com/danh-sach-phim/?s=', 'search', os.path.join(addondir, 'icons', 'search.png'), '')
	if skin_used == 'skin.heidi':
		xbmc.executebuiltin('Container.SetViewMode(53)')

def Genres():
	addDir('Hành động', 'http://phimnhanh.com/the-loai/hanh-dong', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Võ thuật - kiếm hiệp', 'http://phimnhanh.com/the-loai/vo-thuat-kiem-hiep', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Tâm lý - tình cảm', 'http://phimnhanh.com/the-loai/tam-ly-tinh-cam', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Hoạt hình', 'http://phimnhanh.com/the-loai/hoat-hinh', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Kinh dị - ma', 'http://phimnhanh.com/the-loai/kinh-di-ma', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Hài hước', 'http://phimnhanh.com/the-loai/hai-huoc', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Viễn tưởng', 'http://phimnhanh.com/the-loai/vien-tuong', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Phim bộ Hàn Quốc', 'http://phimnhanh.com/the-loai/phim-bo-han-quoc', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Thần thoại', 'http://phimnhanh.com/the-loai/than-thoai', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Chiến tranh', 'http://phimnhanh.com/the-loai/chien-tranh', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Thể thao - âm nhạc', 'http://phimnhanh.com/the-loai/the-thao-am-nhac', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Phiêu lưu', 'http://phimnhanh.com/the-loai/phieu-luu', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Music box', 'http://phimnhanh.com/the-loai/music-box', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')
	addDir('Clip vui', 'http://phimnhanh.com/the-loai/clip-vui', 'index', os.path.join(addondir, 'icons', 'genres.png'), '')

def Countries():
	addDir('Việt Nam', 'http://phimnhanh.com/quoc-gia/viet-nam', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Trung Quốc', 'http://phimnhanh.com/quoc-gia/trung-quoc', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Hàn Quốc', 'http://phimnhanh.com/quoc-gia/han-quoc', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Nhật Bản', 'http://phimnhanh.com/quoc-gia/nhat-ban', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Mỹ - Châu Âu', 'http://phimnhanh.com/quoc-gia/my-chau-au', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Châu Á', 'http://phimnhanh.com/quoc-gia/chau-a', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Thái Lan', 'http://phimnhanh.com/quoc-gia/thai-lan', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Ấn Độ', 'http://phimnhanh.com/quoc-gia/an-do', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Hồng Kông', 'http://phimnhanh.com/quoc-gia/hong-kong', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Đài Loan', 'http://phimnhanh.com/quoc-gia/dai-loan', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')
	addDir('Quốc gia khác', 'http://phimnhanh.com/quoc-gia/quoc-gia-khac', 'index', os.path.join(addondir, 'icons', 'countries.png'), '')

#def Years():
#	addDir('2016', 'http://phimnhanh.com/nam-san-xuat/2016', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2015', 'http://phimnhanh.com/nam-san-xuat/2015', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2014', 'http://phimnhanh.com/nam-san-xuat/2014', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2013', 'http://phimnhanh.com/nam-san-xuat/2013', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2012', 'http://phimnhanh.com/nam-san-xuat/2012', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2011', 'http://phimnhanh.com/nam-san-xuat/2011', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2010', 'http://phimnhanh.com/nam-san-xuat/2010', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2009', 'http://phimnhanh.com/nam-san-xuat/2009', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2008', 'http://phimnhanh.com/nam-san-xuat/2008', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2007', 'http://phimnhanh.com/nam-san-xuat/2007', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2006', 'http://phimnhanh.com/nam-san-xuat/2006', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2005', 'http://phimnhanh.com/nam-san-xuat/2005', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2004', 'http://phimnhanh.com/nam-san-xuat/2004', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2003', 'http://phimnhanh.com/nam-san-xuat/2003', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2002', 'http://phimnhanh.com/nam-san-xuat/2002', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2001', 'http://phimnhanh.com/nam-san-xuat/2001', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('2000', 'http://phimnhanh.com/nam-san-xuat/2000', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('1999', 'http://phimnhanh.com/nam-san-xuat/1999', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('1998', 'http://phimnhanh.com/nam-san-xuat/1998', 'index', os.path.join(addondir, 'icons', 'years.png'), '')
#	addDir('1997', 'http://phimnhanh.com/nam-san-xuat/1997', 'index', os.path.join(addondir, 'icons', 'years.png'), '')

def Topics():
	addDir('Phim HOT Việt Nam', 'http://phimnhanh.com/chu-de/phim-hot-viet-nam', 'index', os.path.join(addondir, 'icons', 'topics.png'), '')
	addDir('Phim HOT nước ngoài', 'http://phimnhanh.com/chu-de/phim-hot-nuoc-ngoai', 'index', os.path.join(addondir, 'icons', 'topics.png'), '')
	addDir('Phim bộ HOT', 'http://phimnhanh.com/chu-de/phim-bo-hot', 'index', os.path.join(addondir, 'icons', 'topics.png'), '')
	addDir('Phim HOT Thập niên 90', 'http://phimnhanh.com/chu-de/phim-hot-thap-nien-90', 'index', os.path.join(addondir, 'icons', 'topics.png'), '')

def Search(url):
	try:
		if '?s=' in url:
			keyb = xbmc.Keyboard('', 'Nhập từ khóa để tìm:')
			keyb.doModal()
			if (keyb.isConfirmed()):
				searchText = urllib.quote_plus(keyb.getText())
		elif '?page=' in url:
			keyb = xbmcgui.Dialog()
			searchText = keyb.input('Nhập số trang:', type=xbmcgui.INPUT_NUMERIC)
		elif 'nam-san-xuat' in url:
			keyb = xbmcgui.Dialog()
			searchText = keyb.input('Nhập năm:', type=xbmcgui.INPUT_NUMERIC)
		url = url + searchText
		Index(url)
	except: pass

def Index(url):
	html = GetUrl(url)
	vidlist = re.compile('<li[^>]*class="serial">.+?<a href="(.+?)".+?>.+?<img .+? data-original="(.+?)" .+?>(.+?)<span class="title display">(.+?)<\/span><span class="title real">(.+?)<\/span>.+?<\/li>').findall(html)
	for vurl, vthumb, vinfo, vname, vname2 in vidlist:
		vqual = ''; vlang = ''; vlen  = ''; vrate = ''
		try: vqual = re.compile('<span class="m-label q">(.+?)</span>').findall(vinfo)[0];
		except: pass
		try: vlang = re.compile('<span class="m-label lang">(.+?)</span>').findall(vinfo)[0]
		except: pass
		try: vlen = re.compile('<span class="m-label ep">(.+?)</span>').findall(vinfo)[0]
		except: pass
		try:
			vrate = re.compile('<span class="rate">(.+?)</span>').findall(vinfo)[0]
			vrate = ' | [COLOR lime]' + vrate + '[/COLOR]'
		except: pass
		if 'class="m-label ep trailer"' in vinfo:
			vurl = vurl + '/trailer'
		addDir('[COLOR white]' + vname.strip().encode('utf-8') + '[/COLOR]' + vrate.encode('utf-8') + ' | [COLOR grey]' + vname2.strip().encode('utf-8') + '[/COLOR]', vurl, 'episodes', vthumb, vname.strip().encode('utf-8'))
	try:
		pagelist = re.compile('<ul class="pagination">(.+?)</ul>').findall(html)[0]
	except:
		pass
	else:
		navmatch = re.compile('<li([^>]*)>(.+?)<\/li>').findall(pagelist)
		for pclass, pblock in navmatch:
			if 'active' in pclass:
				pname = re.compile('<span>(.+?)<\/span>').findall(pblock)[0]
				addDir('[COLOR green]Hiện trên trang: ' + pname.strip().encode("utf-8") + '[/COLOR]', url, 'self', '', '')
			elif pclass == '':
				pblock = re.compile('<a href="(.+?)"[^>]*>(.+?)<\/a>').findall(pblock)
				for plink, pname in pblock:
					if '&raquo;' in pname:
						addDir('[COLOR lime]Trang tiếp theo >>[/COLOR]', plink, 'index', '', '')
#					elif '&laquo;' in pname: # Previous page
#						addDir('<< Trang trước', plink, 'index', '', '')
#					else: # All available pages
#						addDir('Trang ' + pname, plink, 'index', '', '')
#			elif '...' in pblock: # Ellipsis
#				addDir('...', '', 'index', '', '')
		addDir('[COLOR white][ Nhập số trang ][/COLOR]', url + '?page=', 'search', '', '')

def Episodes(url, name, iconimage, vname):
	url = url.replace('/phim/','/xem-phim/')
	html = GetUrl(url)
	match = re.compile('<div id="eps">(.+?)<\/div>').findall(html)[0]
	elist = re.compile('<a.+?href="(.+?)" title="(.+?)">(.+?)<\/a>').findall(match)
	if elist == []:
#		PlayVideo(url, name)
		addLink('Phim hiện không có nguồn', 'http://phimnhanh.com/phim-moi', 'index', '', '')
		addLink('Xin vui lòng thử phim khác', 'http://phimnhanh.com/phim-moi', 'index', '', '')
	else:
		for elink, ename, episode in elist:
			if len(elist) == 1:
				PlayVideo(elink, ename)
			else:
	#			addDir("Tập " + episode.encode('utf-8'), elink, 'mirrors', iconimage, ename.encode('utf-8'))
				addLink("Tập " + episode.encode('utf-8'), elink, 'loadvideo', iconimage, ename.encode('utf-8'))

#def Mirrors(url, name, iconimage, vname):
#	html = GetUrl(url)
#	if "playlist:" in html:
#		link = re.compile('playlist:\s*"(.+?)"').findall(html)[0]
#		src = GetUrl(link)
#		mirrors = re.compile('file="(.+?) label="(.+?)"').findall(src)
#		for mlink, mname in mirrors:
#			addLink("Link: " + mname.encode('utf-8'), mlink, 'loadvideo', iconimage, vname)
#	else:
#		pass

def GetVideo(url):
	html = GetUrl(url)
	if 'youtube.com/watch' in html:
		url = re.compile('\'(.+?youtube.com\/watch.+?)\'').findall(html)[0]
	else:
		link = re.compile('playlist:\s*"(.+?)"').findall(html)[0]
		src = GetUrl(link)
		mirrors = re.compile('file="(.+?)" label="(.+?)" type="video\/mp4"').findall(src)
	#		for mlink, mname in mirrors:
	#			addLink("Link: " + mname.encode('utf-8'), mlink, 'loadvideo', iconimage, vname)
		url = mirrors[-1][0] # Auto play highest res
	return url

def LoadVideo(url, vname):
	url = GetVideo(url)
	video = xbmcgui.ListItem(vname)
	video.setProperty('IsPlayable', 'true')
	video.setPath(str(url))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, video)

def PlayVideo(url, vname):
	dialogWait = xbmcgui.DialogProgress()
	dialogWait.create('Phim Nhanh', 'Đang tải. Xin chờ...')
	try:
		url = GetVideo(url)
		video = xbmcgui.ListItem(vname, path=url)
		xbmc.Player().play(listitem=video)
		p = xbmc.Player().play(url)
	except:
		xbmcgui.Dialog().ok('Xin lỗi', 'Phim hiện không xem được', 'Xin vui lòng thử phim khác')
	dialogWait.close()
	del dialogWait
	xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(str(vname.encode('utf-8')), '', 5000, ''))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), False, '')

def GetUrl(url):
	r = s.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch'})
	response = r.text
	response = ''.join(response.splitlines()).replace('\'', '"')
	response = response.replace('\n', '')
	response = response.replace('\t', '')
	response = re.sub('  +', ' ', response)
	response = response.replace('> <', '><')
	return response

def addLink(name, url, mode, iconimage, vname):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&vname=" + urllib.quote_plus(vname)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={"Title":vname})
	liz.setProperty("IsPlayable", "true")
	ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
	return ok

def addDir(name, url, mode, iconimage, vname):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&vname=" + urllib.quote_plus(vname)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	liz.setInfo(type="Video", infoLabels={"Title":name})
	ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
	return ok

def parameters_string_to_dict(parameters):
	paramDict = {}
	if parameters:
		paramPairs = parameters[1:].split("&")
		for paramsPair in paramPairs:
			paramSplits = paramsPair.split('=')
			if len(paramSplits) == 2:
				paramDict[paramSplits[0]] = paramSplits[1]
	return paramDict

params    = parameters_string_to_dict(sys.argv[2])
url       = params.get('url')
mode      = params.get('mode')
name      = params.get('name')
iconimage = params.get('iconimage')
vname     = params.get('vname')

if type(url) == type(str()):
	url = urllib.unquote_plus(url)
if type(name) == type(str()):
	name = urllib.unquote_plus(name)
if type(iconimage) == type(str()):
	iconimage = urllib.unquote_plus(iconimage)
if type(vname) == type(str()):
	vname = urllib.unquote_plus(vname)

sysarg = str(sys.argv[1])
s = requests.session()

if mode == 'index' or mode == 'self':
	Index(url)
elif mode == 'genres':
	Genres()
elif mode == 'countries':
	Countries()
elif mode == 'years':
	Years()
elif mode == 'topics':
	Topics()
elif mode == 'search':
	Search(url)
elif mode=='episodes':
	Episodes(url, name, iconimage, vname)
#elif mode=='mirrors':
#	Mirrors(url, name, iconimage, vname)
elif mode=='loadvideo':
	dialogWait = xbmcgui.DialogProgress()
	dialogWait.create('PhimNhanh.com', 'Đang tải. Xin chờ...')
	try:
		LoadVideo(url, vname)
	except:
		xbmcgui.Dialog().ok('Xin lỗi', 'Phim hiện không xem được', 'Xin vui lòng thử phim khác')
	dialogWait.close()
	del dialogWait
else:
	Home()

xbmcplugin.endOfDirectory(int(sysarg))