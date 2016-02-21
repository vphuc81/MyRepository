#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, xbmcgui
import os, re, requests, urllib, urllib2, uuid
from xbmcswift2 import Plugin
import urlresolver

addonID = "plugin://plugin.video.v137.xemphim73"
plugin  = Plugin()
listMax = 24

@ plugin.route('/')
def Home():
	items = [
	{'label': '[COLOR white]Phim lẻ mới cập nhật[/COLOR]', 'path': '%s/movies/new/%s' % (addonID, urllib.quote_plus('http://xemphim73.com'))},
	{'label': '[COLOR white]Phim bộ mới cập nhật[/COLOR]', 'path': '%s/series/new/%s' % (addonID, urllib.quote_plus('http://xemphim73.com'))},
	{'label': '[COLOR aqua]Theo thể loại[/COLOR]', 'path': '%s/genres' % addonID},
	{'label': '[COLOR aqua]Theo quốc gia[/COLOR]', 'path': '%s/nations' % addonID},
	{'label': '[COLOR blue]Phim lẻ[/COLOR]', 'path': '%s/movies/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/type/le/%s'), 1)},
	{'label': '[COLOR blue]Phim bộ[/COLOR]', 'path': '%s/series/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/type/bo/%s'), 1)},
	{'label': '[COLOR white]Phim xem nhiều[/COLOR]', 'path': '%s/hot/%s' % (addonID, urllib.quote_plus('http://xemphim73.com'))},
#	{'label': 'Phim Full - [COLOR aqua]Phim lẻ[/COLOR]', 'path': '%s/movies/%s/%s' % (addonID, urllib.quote_plus('http://xemphimfull.net/type/le/%s'), 1)},
#	{'label': 'Phim TV - [COLOR blue]Phim lẻ[/COLOR]', 'path': '%s/movies/%s/%s' % (addonID, urllib.quote_plus('http://xemphimtv.com/type/le/%s'), 1)},
	{'label': '[ Tìm kiếm ]', 'path': '%s/search' % addonID}
	]
	return plugin.finish(items)

@ plugin.route('/series/new/<url>')
def NewSeries(url):
	pageContent = getUrl(url)
	sectionContent = re.compile('<div class="box-drama">.+?<h[0-9]>.+?PHIM BỘ MỚI CẬP NHẬT.+?<\/h[0-9]>(.+?)<div class="box-drama">'.decode('utf-8')).findall(pageContent)[0]
	items = sortedItems(sectionContent, 0, 'newseries')
	if xbmc.getSkinDir() == 'skin.heidi': return plugin.finish(items, view_mode = 54)
	else: return plugin.finish(items)


@ plugin.route('/movies/new/<url>')
def NewMovies(url):
	pageContent = getUrl(url)
	sectionContent = re.compile('<div class="box-drama">.+?<h[0-9]>.+?PHIM LẺ MỚI CẬP NHẬT.+?<\/h[0-9]>(.+?)<div class="colright">'.decode('utf-8')).findall(pageContent)[0]
	items = sortedItems(sectionContent, 0, 'newmovies')
	if xbmc.getSkinDir() == 'skin.heidi': return plugin.finish(items, view_mode = 54)
	else: return plugin.finish(items)


@ plugin.route('/hot/<url>')
def Hot(url):
	pageContent = getUrl(url)
	match = re.compile('%s<\/strong><ul class="group">(.+?)<\/ul>' % 'Phim Xem Nhiều'.decode('utf-8')).findall(pageContent)[0]
	match = re.compile('<a href="(.+?)" .+?>(.+?)<\/a>').findall(match)
	items = []
	for path, label in match:
		video = {}
		video["label"] = "[COLOR white]%s[/COLOR]" % (label.strip())
		video["path"] = '%s/%s/%s' % (addonID, "mirrors", urllib.quote_plus(path))
		items.append(video)
	return plugin.finish(items)

@ plugin.route('/movies/<url>/<page>')
def Movies(url, page):
	items = sortedItems(url, page, 'movies')
	if xbmc.getSkinDir() == 'skin.heidi':
		return plugin.finish(items, view_mode = 52)
	else:
		return plugin.finish(items)

@ plugin.route('/series/<url>/<page>')
def Series(url, page):
	items = sortedItems(url, page, 'series')
	if plugin.get_setting('thumbview', bool):
		if xbmc.getSkinDir() in ('skin.confluence'):
			return plugin.finish(items, view_mode = 500)
		elif xbmc.getSkinDir() == 'skin.heidi':
			return plugin.finish(items, view_mode = 52)
		else:
			return plugin.finish(items)
	else:
		return plugin.finish(items)

@ plugin.route('/genres')
def ListGenres():
	items = [
	{'label': '[COLOR white]Tâm Lý[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-tam-ly/%s'), 1)},
	{'label': '[COLOR white]Cổ Trang[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-co-trang/%s'), 1)},
	{'label': '[COLOR white]Hành Động[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-hanh-dong/%s'), 1)},
	{'label': '[COLOR white]Viễn Tưởng[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-vien-tuong/%s'), 1)},
	{'label': '[COLOR white]Hoạt Hình[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-hoat-hinh/%s'), 1)},
	{'label': '[COLOR white]Hài Hước[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-hai-huoc/%s'), 1)},
	{'label': '[COLOR white]Võ Thuật[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-vo-thuat/%s'), 1)},
	{'label': '[COLOR white]Kinh Dị[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-kinh-di/%s'), 1)},
	{'label': '[COLOR white]TV Show[/COLOR]', 'path': '%s/genres/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/category/phim-tv-show/%s'), 1)}
]
	return plugin.finish(items)

@ plugin.route('/genres/<url>/<page>')
def Genres(url, page = 1):
	items = sortedItems(url, page, 'genres')
	if plugin.get_setting('thumbview', bool):
		if xbmc.getSkinDir() in ('skin.confluence'):
			return plugin.finish(items, view_mode = 500)
		elif xbmc.getSkinDir() == 'skin.heidi':
			return plugin.finish(items, view_mode = 52)
		else:
			return plugin.finish(items)
	else:
		return plugin.finish(items)

@ plugin.route('/nations')
def ListNations():
	items = [
	{'label': '[COLOR white]Việt Nam[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/viet-nam/%s'), 1)},
	{'label': '[COLOR white]Ấn Độ[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/an-do/%s'), 1)},
	{'label': '[COLOR white]Châu Á[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/chau-a/%s'), 1)},
	{'label': '[COLOR white]Hàn Quốc[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/han-quoc/%s'), 1)},
	{'label': '[COLOR white]Hồng Kông[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/hong-kong/%s'), 1)},
	{'label': '[COLOR white]Mỹ - Châu Âu[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/my-chau-au/%s'), 1)},
	{'label': '[COLOR white]Nhật Bản[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/nhat-ban/%s'), 1)},
	{'label': '[COLOR white]Philippines[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/philippines/%s'), 1)},
	{'label': '[COLOR white]Thái Lan[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/thai-lan/%s'), 1)},
	{'label': '[COLOR white]Trung Quốc[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/trung-quoc/%s'), 1)},
	{'label': '[COLOR white]Đài Loan[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/dai-loan/%s'), 1)},
	{'label': '[COLOR white]Nước Khác[/COLOR]', 'path': '%s/nations/%s/%s' % (addonID, urllib.quote_plus('http://xemphim73.com/quoc-gia/khac/%s'), 1)}
]
	return plugin.finish(items)

@ plugin.route('/nations/<url>/<page>')
def Nations(url, page):
	items = sortedItems(url, page, 'nations')
	if plugin.get_setting('thumbview', bool):
		if xbmc.getSkinDir() in ('skin.confluence'):
			return plugin.finish(items, view_mode = 500)
		elif xbmc.getSkinDir() == 'skin.heidi':
			return plugin.finish(items, view_mode = 52)
		else:
			return plugin.finish(items)
	else:
		return plugin.finish(items)

@ plugin.route('/search/')
def Search():
	keyb = plugin.keyboard(heading = 'Tìm kiếm')
	if keyb:
		searchUrl = "http://xemphim73.com/phim/keyword/%s".replace("keyword", keyb).replace(" ", "+")
		searchRoute = '%s/search/%s/%s' % (addonID, urllib.quote_plus(searchUrl), 1)
		plugin.redirect(searchRoute)

@ plugin.route('/search/<url>/<page>')
def SearchResults(url, page):
	items = sortedItems(url, page, 'search')
	if plugin.get_setting('thumbview', bool):
		if xbmc.getSkinDir() in ('skin.confluence'):
			return plugin.finish(items, view_mode = 500)
		elif xbmc.getSkinDir() == 'skin.heidi':
			return plugin.finish(items, view_mode = 52)
		else:
			return plugin.finish(items)
	else:
		return plugin.finish(items)

@ plugin.route('/mirrors/<url>')
def Mirrors(url):
	items = []
	for server in servers(url):
		video = {}
		video["label"] = ('%s: [COLOR white]' + server["name"].strip() + '[/COLOR]') % 'Nguồn'.decode('utf-8')
		guid = str(uuid.uuid1())
		eps = plugin.get_storage(guid)
		eps["list"] = server["eps"]
		video["path"] = '%s/eps/%s' % (addonID, urllib.quote_plus(guid))
		items.append(video)
	return plugin.finish(items)

@ plugin.route('/eps/<eps_list>')
def Episodes(eps_list):
	items = []
	for episode in plugin.get_storage(eps_list)["list"]:
		video = {}
		video["label"] = episode["name"].strip()
		video["is_playable"] = True
		video["path"] = '%s/play/%s' % (addonID, urllib.quote_plus(episode["url"]))
		items.append(video)
	return plugin.finish(items)

@ plugin.route('/play/<url>')
def Play(url):
	dialogWait = xbmcgui.DialogProgress()
	dialogWait.create('Xem Phim 73', 'Đang tải. Xin chờ...')
	try:
#		li = ListItem(label=None, label2=None, icon=None, thumbnail=plugin.get_storage('vid')["thumbnail"], path=LoadVideos(url))
		plugin.set_resolved_url(LoadVideos(url))
	except:
		xbmcgui.Dialog().ok('Xin lỗi','Nguồn phim hiện không xem được','Xin vui lòng thử nguồn khác')
	dialogWait.close()
	del dialogWait

def LoadVideos(url):
	pageContent = getUrl(url.decode('utf-8'))
	if 'mediaplayer' in pageContent:
		match = re.compile('id="mediaplayer" .+? src="(.+?)"').findall(pageContent)[0]
		frameContent = getUrl(match)
		if 'file: ' in frameContent:
			if 'decodeLink' in frameContent:
				pass # resolve b64.js links ##############################################################
			else:
				source = re.compile('file: "(.+?)"').findall(frameContent)[0]
				if 'youtube' in source:
					youtubeID = re.compile('watch\?v=(.*)').findall(source)[0]
					source = 'plugin://plugin.video.youtube/play/?video_id=%s' % youtubeID
			return source
		elif 'showa' in frameContent: # resolve ok.ru links ##############################################
			js_list = re.compile('var showa = \[(.+?)\]').findall(frameContent)[0] + (',')
			js_list = re.compile('(.+?),').findall(js_list)
			js_num = re.compile('fromCharCode\(.+?[-|\+|\*|\/](.+?)\)').findall(frameContent)[0]
			js_code = ''
			for js_oper in js_list:
				js_code = js_code + unichr(eval(js_oper) - int(js_num))
			link = re.compile('src="(.+?)"').findall(js_code.decode('utf-8'))[0]
			source = urlresolver.resolve(link)
			return source

def sortedItems(url, page, route_name):
	if page > 0:
		pageNumber = int(page)+1
		pageContent = getUrl(url % page)
	else:
		pageContent = url
	if 'xemphim73' in url:
		match = re.compile('<div class="item-inner"><div><a href="(.+?)"><img[^>]*src="(.+?)"[^>]*\/><p class="group"><strong>(.+?)<\/strong><span>(.+?)<\/span><\/p><\/a><\/div><h3><a href=".+?"[^>]*>(.+?)<\/a>').findall(pageContent)
	elif 'xemphimfull' in url:
		match = re.compile('<div class="item-inner"><div><a href="(.+?)"><img[^>]*src="(.+?)"[^>]*\/><p class="group"><strong>(.+?)<\/strong><span>(.+?)<\/span><\/p><\/a><\/div><h3><a href=".+?"[^>]*>(.+?)<\/a>').findall(pageContent)
	else:
		pass
	items = []
	for path, thumbnail, label2, year, label in match:
		video = {}
		video["label"] = "[COLOR white]%s[/COLOR] - [COLOR aqua]%s[/COLOR] [COLOR blue]%s[/COLOR]" % (label.strip(), year, label2)
		video["thumbnail"] = thumbnail
		vid = plugin.get_storage('vid')
		vid["thumbnail"] = thumbnail
		video["info"] = {"year": year}
		video["path"] = '%s/%s/%s' % (addonID, "mirrors", urllib.quote_plus(path.encode('utf-8')))
		items.append(video)
	if len(items) == listMax:
		items.append({'label': 'Next >>', 'path': '%s/%s/%s/%s' % (addonID, route_name, urllib.quote_plus(url), pageNumber), 'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Go-next-grey.svg/360px-Go-next-grey.svg.png'})
	return items

def servers(url):
	if 'xemphim73' in url:
		url = url.replace('/info/', '/play/')
	elif 'xemphimfull' in url:
		url = url.replace('/phim/', '/play/')
	else:
		pass
	pageContent = getUrl(url)
	match = re.compile('<div class="listserver">(.+?)<\/div><ul class="listep">(.+?)<\/ul>').findall(pageContent)
	name = re.compile('<title>(.+?)</title>').findall(pageContent)[0].replace('Xem phim','')
	serverList = []
	for serverName, episodeList in match:
		serverEps = []
		for url, part in re.compile('<a[^>]*href="(.+?)"[^>]*>(.+?)<\/a>').findall(episodeList):
			episode = {}
			episode["url"] = url.encode('utf-8')
			episode["name"] = "%s %s - [COLOR white]%s[/COLOR]" % ('Phần'.decode('utf-8'), part, name)
			serverEps.append(episode)
		server = {}
		server["name"] = serverName
		server["eps"] = serverEps
		serverList.append(server)
	return serverList

def metaInfo(url):
	pass

def getUrl(url):
	r = requests.get(url=url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate, sdch'})
	response = r.text
	response = ''.join(response.splitlines()).replace('\'', '"')
	response = response.replace('\n', '')
	response = response.replace('\t', '')
	response = re.sub('  +', ' ', response)
	response = response.replace('> <', '><')
	return response

if __name__ == '__main__':
	plugin.run()