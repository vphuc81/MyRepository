#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, xbmcgui
import os, re, requests, urllib, urllib2, uuid
from xbmcswift2 import Plugin

addonID = "plugin://plugin.video.v.phimlt"
plugin  = Plugin()
listMax = 28

@ plugin.route('/')
def Home() :
	items = [
	{ 'label' : 'Phim mới', 'path' : '%s/latest/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/list/new/p%s'), 1) },
	{ 'label' : 'Phim hot', 'path' : '%s/hot/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/list/top-rate/p%s'), 1) },
	{ 'label' : 'Phim xem nhiều', 'path' : '%s/popular/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/list/phim-xem-nhieu/p%s'), 1) },
	{ 'label' : 'Phim lẻ', 'path' : '%s/movies/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-le/p%s'), 1) },
	{ 'label' : 'Phim bộ', 'path' : '%s/series/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/p%s'), 1) },
	{ 'label' : 'Theo thể loại', 'path' : '%s/genres' % addonID},
	{ 'label' : 'Theo Quốc gia', 'path' : '%s/nations' % addonID},
	{ 'label' : 'Tìm kiếm', 'path' : '%s/search' % addonID}
	]
	return plugin.finish(items)

@ plugin.route('/latest/<murl>/<page>')
def Latest(murl, page):
	items = sortedItems(murl, page, 'latest')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/hot/<murl>/<page>')
def Hot(murl, page):
	items = sortedItems(murl, page, 'hot')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/popular/<murl>/<page>')
def Popular(murl, page):
	items = sortedItems(murl, page, 'popular')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/movies/<murl>/<page>')
def Movies(murl, page):
	items = sortedItems(murl, page, 'movies')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/series/<murl>/<page>')
def Series(murl, page):
	items = sortedItems(murl, page, 'series')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/genres')
def ListGenres() :
	items = [
	{ 'label' : 'Lồng tiếng việt', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/long-tieng-viet/g17/p%s'), 1) },
	{ 'label' : 'Show Truyền Hình', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/tv-shows/g15/p%s'), 1) },
	{ 'label' : 'Cải lương', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/cai-luong/g18/p%s'), 1) },
	{ 'label' : 'Ca nhạc', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/ca-nhac/g13/p%s'), 1) },
	{ 'label' : 'Phóng sự du lịch', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/phong-su/g19/p%s'), 1) },
	{ 'label' : 'Phim Hành động', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/hanh-dong/g1/p%s'), 1) },
	{ 'label' : 'Phim Phiêu Lưu', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/phieu-luu/g2/p%s'), 1) },
	{ 'label' : 'Phim Kinh Dị', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/kinh-di/g3/p%s'), 1) },
	{ 'label' : 'Phim Tình Cảm', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/tinh-cam/g4/p%s'), 1) },
	{ 'label' : 'Phim Hoạt Hình', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/hoat-hinh/g5/p%s'), 1) },
	{ 'label' : 'Phim Võ Thuật', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/vo-thuat/g6/p%s'), 1) },
	{ 'label' : 'Phim Hài Hước', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/hai-huoc/g7/p%s'), 1) },
	{ 'label' : 'Phim Tâm Lý', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/tam-ly/g8/p%s'), 1) },
	{ 'label' : 'Phim Hình Sự', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/hinh-su/g14/p%s'), 1) },
	{ 'label' : 'Phim Viễn Tưởng', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/vien-tuong/g9/p%s'), 1) },
	{ 'label' : 'Phim Thần Thoại', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/than-thoai/g10/p%s'), 1) },
	{ 'label' : 'Phim Chiến Tranh', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/chien-tranh/g11/p%s'), 1) },
	{ 'label' : 'Phim Dã Sữ - Cổ Trang', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/the-loai/da-su-co-trang/g12/p%s'), 1) }
	]
	return plugin.finish(items)

@ plugin.route('/genres/<murl>/<page>')
def Genres(murl, page = 1):
	items = sortedItems(murl, page, 'genres')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/nations')
def ListNations() :
	items = [
	{ 'label' : 'Việt Nam', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/viet-nam/p%s'), 1) },
	{ 'label' : 'Trung Quốc', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/trung-quoc/p%s'), 1) },
	{ 'label' : 'HongKong', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/hong-kong/p%s'), 1) },
	{ 'label' : 'HongKong VNLT', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/hongkong-vnlt/p%s'), 1) },
	{ 'label' : 'Hàn Quốc', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/han-quoc/p%s'), 1) },
	{ 'label' : 'HQ Vietsub', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/han-quoc-vietsub/p%s'), 1) },
	{ 'label' : 'Đài Loan', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/dai-loan/p%s'), 1) },
	{ 'label' : 'Thái Lan', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/thai-lan/p%s'), 1) },
	{ 'label' : 'Nhật Bản', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/nhat-ban/p%s'), 1) },
	{ 'label' : 'Các loại khác', 'path' : '%s/genres/%s/%s' %(addonID, urllib.quote_plus('http://phimlt.com/phim-bo/khac/p%s'), 1) }
	]
	return plugin.finish(items)

@ plugin.route('/nations/<murl>/<page>')
def Nations(murl, page):
	items = sortedItems(murl, page, 'nations')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/search/')
def Search() :
	keyb = plugin.keyboard(heading = 'Tìm kiếm')
	if keyb :
		searchURL = "http://phimlt.com/search/keyword/p%s".replace("keyword", keyb)
		searchRoute = '%s/search/%s/%s' %(addonID, urllib.quote_plus(searchURL), 1)
		plugin.redirect(searchRoute)

@ plugin.route('/search/<murl>/<page>')
def SearchResults(murl, page):
	items = sortedItems(murl, page, 'search')
	if xbmc.getSkinDir() == 'skin.heidi' and plugin.get_setting('thumbview', bool):
		return plugin.finish(items, view_mode = 53)
	else :
		return plugin.finish(items)

@ plugin.route('/mirrors/<murl>')
def Mirrors(murl):
	items = []
	for server in Servers(murl):
		video = {}
		video["label"] = server["name"].strip()
		Ii11iii11I = str(uuid.uuid1())
		oOo00Oo00O = plugin.get_storage(Ii11iii11I)
		oOo00Oo00O["list"] = server["eps"]
		video["path"] = '%s/eps/%s' %(addonID, urllib.quote_plus(Ii11iii11I))
		items.append(video)
	return plugin.finish(items)

@ plugin.route('/eps/<eps_list>')
def Episodes(eps_list):
	items = []
	for episode in plugin.get_storage(eps_list)["list"]:
		video = {}
		video["label"] = episode["name"].strip()
		video["is_playable"] = True
		video["path"] = '%s/play/%s' %(addonID, urllib.quote_plus(episode["url"]))
		items.append(video)
	return plugin.finish(items)

@ plugin.route('/play/<url>')
def Play(url):
	dialogWait = xbmcgui.DialogProgress()
	dialogWait.create('phimlt.com', 'Loading video. Please wait...')
	plugin.set_resolved_url(LoadVideos(url))
	dialogWait.close()
	del dialogWait

def LoadVideos(url):
	vidcontent = GetUrl(url)
	if "youtube" in vidcontent :
		match = re.compile('(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(vidcontent)
		ytlink = match[0][len(match[0])- 1].replace('v/', '')
		return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % ytlink
	if "nonHD=" in vidcontent :
		source = re.compile('nonHD="(.+?)"').findall(vidcontent)[0]
		if plugin.get_setting('HQ', bool) and "&hd=1" in vidcontent :
			source += "&hd=1"
	if '<source src=' in vidcontent:
		source = GetVideo(vidcontent)
	if 'iframe id="iplayer"' in vidcontent :
		links = [url]
		if '<div class="mirrors">' in vidcontent:
			match = re.compile('<div class="mirrors">(.+?)</div>').findall(vidcontent)[0]
			links.extend(re.compile('<a class="button" href="(.+?)"[^>]*>').findall(match))
		for i in range(len(links)):
			if i > 0:
				vidcontent = GetUrl(links[i])
			frame = re.compile('<iframe id="iplayer" class="smallVid" frameborder="0" allowtransparency="true" scrolling="no" allowfullscreen="true" webkitallowfullscreen="true" mozallowfullscreen="true" src="(.+?)">').findall(vidcontent)[0]
			source = GetVideo(GetUrl(frame))
			if source is not '':
				break
	return source

def GetVideo(frame):
	if ('<source src="http://' in frame) or ('<source src="https://' in frame) :
		if '1440p' in frame: #Downgrade from 1440p to 1080p for proper playback in 1K boxes
			vid = re.compile('<source src="(.+?)"[^>]*/>').findall(frame)[1]
		else:
			vid = re.compile('<source src="(.+?)"[^>]*/>').findall(frame)[0]
	elif '<source src="//' in frame :
		vid = 'http:' + re.compile('<source src="(.+?)"[^>]*/>').findall(frame)[0]
	elif '<source src="/' in frame :
		vid = 'http://phimlt.com' + re.compile('<source src="(.+?)"[^>]*/>').findall(frame)[0]
	else:
		vid = ''
	return vid

def sortedItems(url, page, route_name):
	Ii11I = int(page)+ 1
	vidcontent = GetUrl(url % page)
	match = re.compile('<div class="inner"><div class="pic"><a href="(.+?)" title="(.+?)"><img class="thumb" src="(.+?)"[^>]*/>').findall(vidcontent)
	items = []
	for path, label, thumbnail in match :
		video = {}
		video["label"] = "%s" %(label)
		if ('https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=') in thumbnail:
			video["thumbnail"] = urllib.unquote_plus(thumbnail.replace('https://images-blogger-opensocial.googleusercontent.com/gadgets/proxy?url=','').replace('&amp;container=blogger&amp;gadget=a&amp;rewriteMime=image%2F*','').replace('&container=blogger&gadget=a&rewriteMime=image%2F*',''))
		else:
			video["thumbnail"] = 'http://phimlt.com' + thumbnail
		video["path"] = '%s/%s/%s' %(addonID, "mirrors", urllib.quote_plus(path))
		items.append(video)
	if len(items)== listMax :
		items.append({ 'label' : 'Next >>', 'path' : '%s/%s/%s/%s' %(addonID, route_name, urllib.quote_plus(url), Ii11I), 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' })
	return items

def Servers(murl):
	vidcontent = GetUrl(murl)
	match = re.compile('<img src="http://phimlt.com/img/icon_server.png" alt="Icon server phim"[^>]*/>(.+?)\:</span><ul class="episodelist-info-page">(.+?)</ul>').findall(vidcontent)
	i11i1 = re.compile('<title>(.+?)</title>').findall(vidcontent)[0]
	serverList = []
	for serverName, oo0OooOOo0 in match :
		serverEps = []
		for I11i1match, oO0Oo in re.compile('<a[^>]*href="(.+?)"[^>]*>(.+?)</a>').findall(oo0OooOOo0):
			episode = {}
			episode["url"] = I11i1match
			episode["name"] = "Part %s - %s" %(oO0Oo, i11i1.split(" | ")[0])
			serverEps.append(episode)
		server= {}
		server["name"] = serverName
		server["eps"] = serverEps
		serverList.append(server)
	return serverList

def GetUrl(url):
	r = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch'})
	response = r.text
	response = ''.join(response.splitlines()).replace('\'', '"')
	response = response.replace('\n', '')
	response = response.replace('\t', '')
	response = re.sub('  +', ' ', response)
	response = response.replace('> <', '><')
	return response

if __name__ == '__main__' :
	plugin.run()