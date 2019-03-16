#!/usr/bin/python
#coding=utf-8
import httplib2
import json
import re
import urllib
import os
import uuid
import contextlib
import zipfile
import random
import base64
import time
import thread
import socket
from datetime import datetime
# Tham khảo xbmcswift2 framework cho kodi addon tại
# http://xbmcswift2.readthedocs.io/en/latest/
from kodiswift import Plugin, xbmc, xbmcaddon, xbmcgui, actions
path = xbmc.translatePath(
	xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
cache = xbmc.translatePath(os.path.join(path, ".cache"))
tmp = xbmc.translatePath('special://temp')
addons_folder = xbmc.translatePath('special://home/addons')
image = xbmc.translatePath(os.path.join(path, "icon.png"))

plugin = Plugin()
#addon = xbmcaddon.Addon("plugin.video.vinh.livetv")
#pluginrootpath = "plugin://plugin.video.vinh.livetv"
addon = xbmcaddon.Addon("plugin.video.vinh.giaitritv")
pluginrootpath = "plugin://plugin.video.vinh.giatritv"
http = httplib2.Http(cache, disable_ssl_certificate_validation=True)
query_url = "https://docs.google.com/spreadsheets/d/{sid}/gviz/tq?gid={gid}&headers=1&tq={tq}"
sheet_headers = {
	"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/7.0)",
	"Accept-Encoding": "gzip, deflate, sdch"
}


def GetSheetIDFromSettings():
	#sid = "1zL6Kw4ZGoNcIuW9TAlHWZrNIJbDU5xHTtz-o8vpoJss"
	sid = "18oBXoKaL64nx7tdKe0yqEdnRHabdfZS4iHfRT44Fnwg"
	resp, content = http.request(get_fshare_setting("GSheetURL"), "HEAD")
	try:
		sid = re.compile("/d/(.+?)/").findall(resp["content-location"])[0]
	except:
		pass
	return sid


def M3UToItems(url_path=""):
	'''
	Hàm chuyển đổi m3u playlist sang xbmcswift2 items
	Parameters
	----------
	url_path : string
		link chứa nội dung m3u playlist
	'''
	item_re = '\#EXTINF(.*?,)(.*?)\n(.*?)\n'
	(resp, content) = http.request(
		url_path, "GET",
		headers=sheet_headers
	)
	items = []
	matchs = re.compile(item_re).findall(content)
	for info, label, path in matchs:
		thumb = ""
		label2 = ""
		if "tvg-logo" in info:
			thumb = re.compile('tvg-logo=\"?(.*?)\"?,').findall(info)[0]
		if "group-title" in info:
			label2 = re.compile('group-title="(.*?)"').findall(info)[0]
		if label2 != "":
			label2 = "[%s] " % label2.strip()
		label = "%s%s" % (label2, label.strip())
		item = {
			"label": label,
			"thumbnail": thumb.strip(),
			"path": path.strip(),
		}

		# Nếu là playable link
		if "://" in item["path"]:
			# Kiểu link plugin://
			if item["path"].startswith("plugin://"):
				item["is_playable"] = True
				item["info"] = {"type": "video"}
			# Kiểu link .ts
			elif re.search("\.ts$", item["path"]):
				item["path"] = "plugin://plugin.video.f4mTester/?url=%s&streamtype=TSDOWNLOADER&use_proxy_for_chunks=True&name=%s" % (
					urllib.quote(item["path"]),
					urllib.quote_plus(item["label"])
				)
				item["path"] = pluginrootpath + \
					"/executebuiltin/" + urllib.quote_plus(item["path"])
			# Kiểu direct link
			else:
				if "acestream" in item["path"]:
					item["label"] = "[AceStream] %s" % item["label"]
				item["path"] = pluginrootpath + \
					"/play/%s" % urllib.quote_plus(item["path"])
				item["is_playable"] = True
				item["info"] = {"type": "video"}
		else:
			# Nếu không phải...
			item["is_playable"] = False

		# Hack xbmcswift2 item to set both is_playable and is_folder to False
		# Required for f4mTester
		if "f4mTester" in item["path"]:
			item["is_playable"] = False
		items += [item]
	return items


@plugin.cached(ttl=525600)
def getCachedItems(url_path="0"):
	return AddTracking(getItems(url_path))


def getItems(url_path="0", tq="select A,B,C,D,E"):
	'''
	Tạo items theo chuẩn xbmcswift2 từ Google Spreadsheet
	Parameters
	----------
	url_path : string
		Nếu truyền "gid" của Repositories sheet:
			Cài tự động toàn bộ repo trong Repositories sheet
		Nếu truyền link download zip repo
			Download và cài zip repo đó
	tracking_string : string
		 Tên dễ đọc của view
	'''
	# Default VN Open Playlist Sheet ID

	sheet_id = GetSheetIDFromSettings()
	gid = url_path
	if "@" in url_path:
		path_split = url_path.split("@")
		gid = path_split[0]
		sheet_id = path_split[1]
	history = plugin.get_storage('history')
	if "sources" in history:
		history["sources"] = ["https://docs.google.com/spreadsheets/d/%s/edit#gid=%s" %
                        (sheet_id, gid)] + history["sources"]
		history["sources"] = history["sources"][0:4]
	else:
		history["sources"] = [
			"https://docs.google.com/spreadsheets/d/%s/edit#gid=%s" % (sheet_id, gid)]
	url = query_url.format(
		sid=sheet_id,
		tq=urllib.quote(tq),
		gid=gid
	)
	(resp, content) = http.request(
		url, "GET",
		headers=sheet_headers
	)
	_re = "google.visualization.Query.setResponse\((.+)\);"
	_json = json.loads(re.compile(_re).findall(content)[0])
	items = []
	for row in _json["table"]["rows"]:
		item = {}
		item["label"] = getValue(row["c"][0]).encode("utf-8")
		item["label2"] = getValue(row["c"][4])
		# Nếu phát hiện spreadsheet khác với VNOpenPlaylist
		new_path = getValue(row["c"][1])
		if "@" in url_path and "@" not in new_path and "section/" in new_path:
			gid = re.compile("section/(\d+)").findall(new_path)[0]
			new_path = re.sub(
				'section/\d+',
				'section/%s@%s' % (gid, sheet_id),
				new_path,
				flags=re.IGNORECASE
			)
		item["path"] = new_path

		item["thumbnail"] = getValue(row["c"][2])
		item["info"] = {"plot": getValue(row["c"][3])}
		if "plugin://" in item["path"]:
			if "install-repo" in item["path"]:
				item["is_playable"] = False
			elif re.search("plugin.video.vinh.livetv/(.+?)/.+?\://", item["path"]):
				match = re.search(
					"plugin.video.vinh.livetv(/.+?/).+?\://", item["path"])
				tmp = item["path"].split(match.group(1))
				tmp[-1] = urllib.quote_plus(tmp[-1])
				item["path"] = match.group(1).join(tmp)
				if "/play/" in match.group(1):
					item["is_playable"] = True
					item["info"] = {"type": "video"}
			elif item["path"].startswith("plugin://plugin.video.f4mTester"):
				item["is_playable"] = False
				item["path"] = pluginrootpath + \
					"/executebuiltin/" + urllib.quote_plus(item["path"])
			elif "/play/" in item["path"]:
				item["is_playable"] = True
				item["info"] = {"type": "video"}
		elif item["path"] == "":
			item["label"] = "[I]%s[/I]" % item["label"]
			item["is_playable"] = False
			item["path"] = pluginrootpath + "/executebuiltin/-"
		else:
			if "spreadsheets/d/" in item["path"]:
				# https://docs.google.com/spreadsheets/d/1zL6Kw4ZGoNcIuW9TAlHWZrNIJbDU5xHTtz-o8vpoJss/edit#gid=0
				match_cache = re.search('cache=(.+?)($|&)', item["path"])
				match_passw = re.search('passw=(.+?)($|&)', item["path"])

				sheet_id = re.compile("/d/(.+?)/").findall(item["path"])[0]
				try:
					gid = re.compile("gid=(\d+)").findall(item["path"])[0]
				except:
					gid = "0"
				item["path"] = pluginrootpath + "/section/%s@%s" % (gid, sheet_id)
				if match_cache:
					cache_version = match_cache.group(1)
					item["path"] = pluginrootpath + \
						"/cached-section/%s@%s@%s" % (gid, sheet_id, cache_version)
				elif match_passw:
					item["path"] = pluginrootpath + \
						"/password-section/%s/%s@%s" % (match_passw.group(1), gid, sheet_id)
			elif re.search(r'textuploader', item["path"]):
				item["path"] = pluginrootpath + \
					"/m3u/" + urllib.quote_plus(item["path"])
			elif any(service in item["path"] for service in ["acelisting.in"]):
				item["path"] = pluginrootpath + \
					"/acelist/" + urllib.quote_plus(item["path"])
			elif any(service in item["path"] for service in ["fshare.vn/folder"]):
				item["path"] = pluginrootpath + "/fshare/" + \
					urllib.quote_plus(item["path"].encode("utf8"))
				# item["path"] = "plugin://plugin.video.xshare/?mode=90&page=0&url=" + urllib.quote_plus(item["path"])
			elif any(service in item["path"] for service in ["4share.vn/d/"]):
				item["path"] = "plugin://plugin.video.xshare/?mode=38&page=0&url=" + \
					urllib.quote_plus(item["path"])
			elif any(service in item["path"] for service in ["4share.vn/f/"]):
				# elif any(service in item["path"] for service in ["4share.vn/f/", "fshare.vn/file"]):
				item["path"] = "plugin://plugin.video.xshare/?mode=3&page=0&url=" + \
					urllib.quote_plus(item["path"])
				item["is_playable"] = True
				item["info"] = {"type": "video"}
				item["path"] = pluginrootpath + "/play/" + urllib.quote_plus(item["path"])
			elif "youtube.com/channel" in item["path"]:
				# https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ
				yt_route = "ytcp" if "playlists" in item["path"] else "ytc"
				yt_cid = re.compile("youtube.com/channel/(.+?)$").findall(item["path"])[0]
				item["path"] = "plugin://plugin.video.kodi4vn.launcher/%s/%s/" % (
					yt_route, yt_cid)
				item["path"] = item["path"].replace("/playlists", "")
			elif "youtube.com/playlist" in item["path"]:
				# https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI
				yt_pid = re.compile("list=(.+?)$").findall(item["path"])[0]
				item["path"] = "plugin://plugin.video.kodi4vn.launcher/ytp/%s/" % yt_pid
			elif any(ext in item["path"] for ext in [".png", ".jpg", ".bmp", ".jpeg"]):
				item["path"] = "plugin://plugin.video.kodi4vn.launcher/showimage/%s/" % urllib.quote_plus(
					item["path"])
			elif re.search("\.ts$", item["path"]):
				item["path"] = "plugin://plugin.video.f4mTester/?url=%s&streamtype=TSDOWNLOADER&use_proxy_for_chunks=True&name=%s" % (
					urllib.quote(item["path"]),
					urllib.quote_plus(item["label"])
				)
				item["path"] = pluginrootpath + \
					"/executebuiltin/" + urllib.quote_plus(item["path"])
			else:
				# Nếu là direct link thì route đến hàm play_url
				item["is_playable"] = True
				item["info"] = {"type": "video"}
				item["path"] = pluginrootpath + "/play/" + urllib.quote_plus(item["path"])
		if item["label2"].startswith("http"):
			item["path"] += "?sub=" + urllib.quote_plus(item["label2"].encode("utf8"))
		items += [item]
	if url_path == "0":
		add_playlist_item = {
			"context_menu": [
				ClearPlaylists(""),
			],
			"label": "[COLOR yellow]*** Thêm Playlist ***[/COLOR]",
			"path": "%s/add-playlist" % (pluginrootpath),
			"thumbnail": "http://1.bp.blogspot.com/-gc1x9VtxIg0/VbggLVxszWI/AAAAAAAAANo/Msz5Wu0wN4E/s1600/playlist-advertorial.png",
			"is_playable": True,
			"info": {"type": "video"}

		}
		items += [add_playlist_item]
		playlists = plugin.get_storage('playlists')
		if 'sections' in playlists:
			for section in playlists['sections']:
				item = {
					"context_menu": [
						ClearPlaylists(section),
					]
				}
				if "@@" in section:
					tmp = section.split("@@")
					passw = tmp[-1]
					section = tmp[0]
					item["label"] = section
					item["path"] = "%s/password-section/%s/%s" % (
						pluginrootpath,
						passw,
						section.split("] ")[-1]
					)
				else:
					item["label"] = section
					item["path"] = "%s/section/%s" % (
						pluginrootpath,
						section.split("] ")[-1]
					)
				item["thumbnail"] = "http://1.bp.blogspot.com/-gc1x9VtxIg0/VbggLVxszWI/AAAAAAAAANo/Msz5Wu0wN4E/s1600/playlist-advertorial.png"
				items.append(item)
	return items


@plugin.route('/remove-playlists/', name="remove_all")
@plugin.route('/remove-playlists/<item>')
def RemovePlaylists(item=""):
	item = urllib.unquote_plus(item)
	if item is not "":
		playlists = plugin.get_storage('playlists')
		if 'sections' in playlists:
			new_playlists = []
			for section in playlists["sections"]:
				if section != item:
					new_playlists += [section]
			playlists["sections"] = new_playlists
	else:
		plugin.get_storage('playlists').clear()
	xbmc.executebuiltin('Container.Refresh')


def ClearPlaylists(item=""):
	if item == "":
		label = '[COLOR yellow]Xóa hết Playlists[/COLOR]'
	else:
		label = '[COLOR yellow]Xóa "%s"[/COLOR]' % item

	return (label, actions.background(
		"%s/remove-playlists/%s" % (pluginrootpath, urllib.quote_plus(item))
	))


def getValue(colid):
	'''
	Hàm lấy giá trị theo cột của của mỗi dòng sheet
	Parameters
	----------
	colid : string
		Số thự tự của cột
	'''
	if colid is not None and colid["v"] is not None:
		return colid["v"]
	else:
		return ""


@plugin.route('/')
def Home():
	'''	Main Menu
	'''
	GA()  # tracking
	Section("0")


@plugin.route('/cached-section/<path>/<tracking_string>')
def CachedSection(path="0", tracking_string="Home"):
	GA(  # tracking
		"Section - %s" % tracking_string,
		"/section/%s" % path
	)
	return plugin.finish(getCachedItems(path))


@plugin.route('/password-section/<password>/<path>/<tracking_string>')
def PasswordSection(password="0000", path="0", tracking_string="Home"):
	'''
	Liệt kê danh sách các item của một sheet
	Parameters
	----------
	path : string
		"gid" của sheet
	tracking_string : string
		 Tên dễ đọc của view
	'''
	GA(  # tracking
		"Password Section - %s" % tracking_string,
		"/password-section/%s" % path
	)
	passwords = plugin.get_storage('passwords')
	if password in passwords and (time.time() - passwords[password] < 1800):
		items = AddTracking(getItems(path))
		return plugin.finish(items)
	else:
		passw_string = plugin.keyboard(heading='Nhập password')
		if passw_string == password:
			passwords[password] = time.time()
			items = AddTracking(getItems(path))
			return plugin.finish(items)
		else:
			header = "Sai mật khẩu!!!"
			message = "Mật khẩu không khớp. Không tải được nội dung"
			xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' %
			                    (header, message, 10000, ''))
			return plugin.finish()


@plugin.route('/section/<path>/<tracking_string>')
def Section(path="0", tracking_string="Home"):
	'''
	Liệt kê danh sách các item của một sheet
	Parameters
	----------
	path : string
		"gid" của sheet
	tracking_string : string
		 Tên dễ đọc của view
	'''
	GA(  # tracking
		"Section - %s" % tracking_string,
		"/section/%s" % path
	)
	items = AddTracking(getItems(path))
	return plugin.finish(items)


@plugin.route('/add-playlist/<tracking_string>')
def AddPlaylist(tracking_string="Add Playlist"):
	sheet_url = plugin.keyboard(
		heading='Nhập URL của Google Spreadsheet (có hỗ trợ link rút gọn như bit.ly, goo.gl)')
	if sheet_url:
		if not re.match("^https*://", sheet_url):
			sheet_url = "https://" + sheet_url
		try:
			resp, content = http.request(sheet_url, "HEAD")
			sid, gid = re.compile(
				"/d/(.+?)/.+?gid=(\d+)").findall(resp["content-location"])[0]
			match_passw = re.search('passw=(.+?)($|&)', resp["content-location"])
			playlists = plugin.get_storage('playlists')
			name = plugin.keyboard(heading='Đặt tên cho Playlist')

			item = "[[COLOR yellow]%s[/COLOR]] %s@%s" % (name, gid, sid)
			if match_passw:
				item += "@@" + match_passw.group(1)
			if 'sections' in playlists:
				playlists["sections"] = [item] + playlists["sections"]
			else:
				playlists["sections"] = [item]
			xbmc.executebuiltin('Container.Refresh')
		except:
			line1 = "Vui lòng nhập URL hợp lệ. Ví dụ dạng đầy đủ:"
			line2 = "http://docs.google.com/spreadsheets/d/xxx/edit#gid=###"
			line3 = "Hoặc rút gọn: http://bit.ly/xxxxxx hoặc http://goo.gl/xxxxx"
			dlg = xbmcgui.Dialog()
			dlg.ok("URL không hợp lệ!!!", line1, line2, line3)


@plugin.route('/acelist/<path>/<tracking_string>')
def AceList(path="0", tracking_string="AceList"):
	(resp, content) = http.request(
		path, "GET",
		headers=sheet_headers
	)
	items = []
	match = re.compile('<td class="text-right">(.+?)</td></tr><tr><td class="xsmall text-muted">(.+?)</td></tr></table></td><td>(.+?)</td>.+?href="(acestream.+?)".+?title = "(.+?)"').findall(cleanHTML(content))
	for _time, _date, sport, aceurl, title in match:
		titles = title.strip().split("<br />")
		titles[0] = "[COLOR yellow]%s[/COLOR]" % titles[0]
		title = " - ".join(titles)
		title = "[B][COLOR orange]%s, %s[/COLOR] %s %s[/B]" % (
			_date.strip(), re.sub('<.*?>', '', _time).strip(), sport.strip(), title)
		item = {}
		item["label"] = title
		item["path"] = "%s/play/%s/%s" % (
			pluginrootpath,
			urllib.quote_plus(aceurl),
			urllib.quote_plus("[AceList] %s" % item["label"])
		)
		item["is_playable"] = True
		item["info"] = {"type": "video"}
		items += [item]
	return plugin.finish(items)


@plugin.route('/fshare/<path>/<tracking_string>')
def FShare(path="0", tracking_string="FShare"):
	def toSize(s):
		gb = 2**30
		mb = 2**20
		try:
			s = int(s)
		except:
			s = 0
		if s > gb:
			s = '{:.2f} GB'.format(s/gb)
		elif s > mb:
			s = '{:.0f} MB'.format(s/mb)
		else:
			s = '{:.2f} MB'.format(s/mb)
		return s
	folder_id = re.search('folder/(.+?)(\?|$)', path).group(1)
	page = 1
	try:
		page = int(re.search('page=(\d+)', path).group(1))
	except:
		pass
	fshare_folder_api = "https://www.fshare.vn/api/v3/files/folder?linkcode=%s&sort=type,-modified&page=%s" % (
		folder_id, page)
	(resp, content) = http.request(
		fshare_folder_api, "GET",
		headers={
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36",
			"Accept": "application/json, text/plain, */*",
			"Accept-Encoding": "gzip, deflate, sdch, br"
		}
	)
	items = []
	fshare_items = json.loads(content)["items"]
	for i in fshare_items:
		item = {}
		name = i["name"].encode("utf8")
		size = 0
		try:
			size = toSize(i["size"])
		except:
			pass

		if not i["type"]:  # is folder
			item["path"] = "%s/fshare/%s/%s" % (
				pluginrootpath,
				urllib.quote_plus("https://www.fshare.vn/folder/" + i["linkcode"]),
				urllib.quote_plus("[FShare] %s" % name)
			)
			item["label"] = "[FShare] %s" % name
		else:
			item["path"] = "%s/play/%s/%s" % (
				pluginrootpath,
				urllib.quote_plus("https://www.fshare.vn/file/" + i["linkcode"]),
				urllib.quote_plus("[FShare] %s (%s)" % (name, size))
			)
			item["label"] = "%s (%s)" % (name, size)
			item["is_playable"] = True
			item["info"] = {"type": "video"}
		items += [item]
	if len(fshare_items) >= 20:
		path = "https://www.fshare.vn/folder/%s?page=%s" % (folder_id, page + 1)
		items.append({
			'label': 'Next >>',
			'path': '%s/fshare/%s/%s' % (
				pluginrootpath,
				urllib.quote_plus(path),
				urllib.quote_plus(tracking_string)
			),
			'thumbnail': "https://docs.google.com/drawings/d/12OjbFr3Z5TCi1WREwTWECxNNwx0Kx-FTrCLOigrpqG4/pub?w=256&h=256"
		})
	return plugin.finish(items)


@plugin.route('/m3u-section/<path>/<tracking_string>')
def M3USection(path="0", tracking_string="M3U"):
	'''
	Liệt kê danh sách các item của sheet M3U Playlist
	Parameters
	----------
	path : string
		"gid" của sheet M3U Playlist
	tracking_string : string
		 Tên dễ đọc của view
	'''
	GA(  # tracking
		"M3U Section - %s" % tracking_string,
		"/m3u-section/%s" % path
	)
	items = getItems(path)
	for item in items:
		# Chỉnh lại thành m3u item
		item["path"] = item["path"].replace("/play/", "/m3u/")
		if "is_playable" in item:
			del item["is_playable"]
		if "playable" in item:
			del item["playable"]
	return plugin.finish(AddTracking(items))


@plugin.route('/m3u/<path>', name="m3u_default")
@plugin.route('/m3u/<path>/<tracking_string>')
def M3U(path="0", tracking_string="M3U"):
	'''
	Liệt kê danh sách các item của sheet M3U Playlist
	Parameters
	----------
	path : string
		Link chưa nội dung playlist m3u
	tracking_string : string
		 Tên dễ đọc của view
	'''
	GA(  # tracking
		"M3U - %s" % tracking_string,
		"/m3u/%s" % path
	)

	items = M3UToItems(path)
	return plugin.finish(AddTracking(items))


@plugin.route('/install-repo/<path>/<tracking_string>')
def InstallRepo(path="0", tracking_string=""):
	'''
	Cài đặt repo
	Parameters
	----------
	path : string
		Nếu truyền "gid" của Repositories sheet:
			Cài tự động toàn bộ repo trong Repositories sheet
		Nếu truyền link download zip repo
			Download và cài zip repo đó
	tracking_string : string
		 Tên dễ đọc của view
	'''
	GA(  # tracking
		"Install Repo - %s" % tracking_string,
		"/install-repo/%s" % path
	)
	if path.isdigit():  # xác định GID
		pDialog = xbmcgui.DialogProgress()
		pDialog.create('Vui lòng đợi', 'Bắt đầu cài repo', 'Đang tải...')
		items = getItems(path)
		total = len(items)
		i = 0
		failed = []
		installed = []
		for item in items:
			done = int(100 * i / total)
			pDialog.update(done, 'Đang tải', item["label"] + '...')
			if ":/" not in item["label2"]:
				result = xbmc.executeJSONRPC(
					'{"jsonrpc":"2.0","method":"Addons.GetAddonDetails", "params":{"addonid":"%s", "properties":["version"]}, "id":1}' % item["label"])
				json_result = json.loads(result)
				if "version" in result and version_cmp(json_result["result"]["addon"]["version"], item["label2"]) >= 0:
					pass
				else:
					try:
						item["path"] = "http" + item["path"].split("http")[-1]
						download(urllib.unquote_plus(item["path"]), item["label"])
						installed += [item["label"].encode("utf-8")]
					except:
						failed += [item["label"].encode("utf-8")]
			else:
				if not os.path.exists(xbmc.translatePath(item["label2"])):
					try:
						item["path"] = "http" + item["path"].split("http")[-1]
						download(urllib.unquote_plus(item["path"]), item["label2"])
						installed += [item["label"].encode("utf-8")]
					except:
						failed += [item["label"].encode("utf-8")]

			if pDialog.iscanceled():
				break
			i += 1
		pDialog.close()
		if len(failed) > 0:
			dlg = xbmcgui.Dialog()
			s = "Không thể cài các rep sau:\n[COLOR orange]%s[/COLOR]" % "\n".join(
				failed)
			dlg.ok('Chú ý: Không cài đủ repo!', s)
		else:
			dlg = xbmcgui.Dialog()
			s = "Tất cả repo đã được cài thành công\n%s" % "\n".join(installed)
			dlg.ok('Cài Repo thành công!', s)

	else:  # cài repo riêng lẻ
		try:
			download(path, "")
			dlg = xbmcgui.Dialog()
			s = "Repo %s đã được cài thành công" % tracking_string
			dlg.ok('Cài Repo thành công!', s)
		except:
			dlg = xbmcgui.Dialog()
			s = "Vùi lòng thử cài lại lần sau"
			dlg.ok('Cài repo thất bại!', s)

	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
	xbmc.executebuiltin("XBMC.UpdateAddonRepos()")


@plugin.route('/repo-section/<path>/<tracking_string>')
def RepoSection(path="0", tracking_string=""):
	'''
	Liệt kê các repo
	Parameters
	----------
	path : string
		Link download zip repo.
	tracking_string : string
		Tên dễ đọc của view
	'''
	GA(  # tracking
		"Repo Section - %s" % tracking_string,
		"/repo-section/%s" % path
	)

	items = getItems(path)
	for item in items:
		if "/play/" in item["path"]:
			item["path"] = item["path"].replace("/play/", "/install-repo/")
		# hack xbmcswift2 item to set both is_playable and is_folder to False
		item["is_playable"] = False
	items = AddTracking(items)

	install_all_item = {
		"label": "[COLOR green]Tự động cài tất cả Repo dưới (khuyên dùng)[/COLOR]".decode("utf-8"),
		"path": pluginrootpath + "/install-repo/%s/%s" % (path, urllib.quote_plus("Install all repo")),
		"is_playable": False,
		"info": {"plot": "Bạn nên cài tất cả repo để sử dụng đầy đủ tính năng của [VN Open Playlist]"}
	}
	items = [install_all_item] + items
	return plugin.finish(items)


def download(download_path, repo_id):
	'''
	Parameters
	----------
	path : string
		Link download zip repo.
	repo_id : string
		Tên thư mục của repo để kiểm tra đã cài chưa.
		Mặc định được gán cho item["label2"].
		Truyền "" để bỏ qua Kiểm tra đã cài
	'''
	if repo_id == "":
		repo_id = "temp"
	if ":/" not in repo_id:
		zipfile_path = xbmc.translatePath(os.path.join(tmp, "%s.zip" % repo_id))
		urllib.urlretrieve(download_path, zipfile_path)
		with zipfile.ZipFile(zipfile_path, "r") as z:
			z.extractall(addons_folder)
	else:
		zipfile_path = xbmc.translatePath(
			os.path.join(tmp, "%s.zip" % repo_id.split("/")[-1]))
		urllib.urlretrieve(download_path, zipfile_path)
		with zipfile.ZipFile(zipfile_path, "r") as z:
			z.extractall(xbmc.translatePath("/".join(repo_id.split("/")[:-1])))


def AddTracking(items):
	'''
	Hàm thêm chuỗi tracking cho các item
	Parameters
	----------
	items : list
		Danh sách các item theo chuẩn xbmcswift2.
	'''

	for item in items:
		if "plugin.video.vinh.livetv" in item["path"]:
			tmps = item["path"].split("?")
			if len(tmps) == 1:
				tail = ""
			else:
				tail = tmps[1]
			item["path"] = "%s/%s?%s" % (tmps[0],
			                             urllib.quote_plus(item["label"]), tail)
	return items


@plugin.route('/showimage/<url>/<tracking_string>')
def showimage(url, tracking_string):
	xbmc.executebuiltin("ShowPicture(%s)" % urllib.unquote_plus(url))


@plugin.route('/executebuiltin/<path>/<tracking_string>')
def execbuiltin(path, tracking_string=""):
	GA(  # tracking
		"Execute Builtin - %s" % tracking_string,
		"/repo-execbuiltin/%s" % path
	)
	try:
		xbmc.executebuiltin('XBMC.RunPlugin(%s)' % urllib.unquote_plus(path))
	except:
		pass


@plugin.route('/play/<url>/<title>')
def play_url(url, title=""):
	GA("Play [%s]" % title, "/play/%s/%s" % (title, url))
	url = get_playable_url(url)
	#Hack for some buggy redirect link
	try:
		http = httplib2.Http(disable_ssl_certificate_validation=True)
		http.follow_redirects = True
		(resp, content) = http.request(
			url, "HEAD"
		)
		url = resp['content-location']
	except:
		pass
	if "sub" in plugin.request.args:
		plugin.set_resolved_url(url, subtitles=plugin.request.args["sub"][0])
	else:
		plugin.set_resolved_url(url)


def get_playable_url(url):
	if "youtube" in url:
		match = re.compile(
			'(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)').findall(url)
		yid = match[0][len(match[0])-1].replace('v/', '')
		url = 'plugin://plugin.video.youtube/play/?video_id=%s' % yid
	elif "thvli.vn/backend/cm/detail/" in url:
		get_thvl = "https://docs.google.com/spreadsheets/d/13VzQebjGYac5hxe1I-z1pIvMiNB0gSG7oWJlFHWnqsA/export?format=tsv&gid=1287121588"
		try:
			(resp, content) = http.request(
				get_thvl, "GET"
			)
		except:
			header = "Server quá tải!"
			message = "Xin vui lòng thử lại sau"
			xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' %
			                    (header, message, 10000, ''))
			return ""

		tmps = content.split('\n')
		random.shuffle(tmps)
		for tmp in tmps:
			try:
				thvl_headers = {
					'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/7.0)',
					"Accept-Encoding": "gzip, deflate, br",
					'Accept': 'application/json',
					'Authorization': tmp.decode('base64')
				}

				(resp, content) = http.request(
					url, "GET", headers=thvl_headers
				)
				resp_json = json.loads(content)
				if "link_play" in resp_json:
					return resp_json["link_play"]
			except:
				pass
	elif "sphim.tv" in url:
		http.follow_redirects = False
		get_sphim = "https://docs.google.com/spreadsheets/d/13VzQebjGYac5hxe1I-z1pIvMiNB0gSG7oWJlFHWnqsA/export?format=tsv&gid=1082544232"
		try:
			(resp, content) = http.request(
				get_sphim, "GET"
			)
		except:
			header = "Server quá tải!"
			message = "Xin vui lòng thử lại sau"
			xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' %
			                    (header, message, 10000, ''))
			return ""

		tmps = content.split('\n')
		random.shuffle(tmps)
		for tmp in tmps:
			try:
				sphim_headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
					"Accept-Encoding": "gzip, deflate",
					'Cookie': tmp.decode("base64")
				}

				(resp, content) = http.request(
					url, "GET", headers=sphim_headers
				)
				match = re.search('"(http.+?\.smil/playlist.m3u8.+?)"', content)
				if match:
					return match.group(1)
			except:
				pass
	elif url.startswith("acestream://") or url.endswith(".acelive") or "arenavision.in" in url:
		if "arenavision.in" in url:
			h = {
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
				'Cookie': '__cfduid=d36d59e9714c527d920417ed5bbc9315e1496259947; beget=begetok; ads_smrt_popunder=1%7CSat%2C%2003%20Jun%202017%2018%3A57%3A05%20GMT; 141054_245550_1rhpmin=yes; 141054_245550_1rhpmax=4|Sat%2C%2003%20Jun%202017%2018%3A57%3A14%20GMT; has_js=1; _ga=GA1.2.652127938.1496259947; _gid=GA1.2.653920302.1496429805; _gat=1',
				'Accept-Encoding': 'gzip, deflate'
			}
			(resp, content) = http.request(
				url,
				"GET", headers=h
			)
			url = re.search('(acestream://.+?)"', content).group(1)
		try:
			(resp, content) = http.request(
				"http://localhost:6878/webui/api/service",
				"HEAD"
			)
			url = url.replace(
				"acestream://", "http://localhost:6878/ace/getstream?id=") + "&.mp4"
			if url.endswith(".acelive"):
				url = "http://localhost:6878/ace/getstream?url=" + \
					urllib.quote_plus(url) + "&.mp4"
		except:
			url = 'plugin://program.plexus/?url=%s&mode=1&name=P2PStream&iconimage=' % urllib.quote_plus(
				url)
	elif any(domain in url for domain in ["m.tivi8k.net", "m.xemtvhd.com", "xemtiviso.com"]):
		play_url = ""
		if "xemtiviso.com" not in url:
			for i in range(1, 8):
				try:
					if i > 1:
						range_url = url.replace(".php", "-%s.php" % i)
					h1 = {
						'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
						'Accept-Encoding': 'gzip, deflate',
						'Referer': '%s' % url.replace("/m.", "/www.")
					}
					(resp, content) = http.request(
						range_url,
						"GET", headers=h1,
					)
					content = content.replace("'", '"')

					try:
						play_url = re.search("https*://api.tivi8k.net/.+?'", content).group(1)
						(resp, content) = http.request(
							range_url,
							"GET", headers=h1,
						)
						if "#EXTM3U" in content:
							return play_url
						else:
							return content.strip()
					except:
						pass
					play_url = play_url.replace("q=medium", "q=high")
					if "v4live" in play_url:
						return play_url
				except:
					pass
			try:
				xemtiviso_id = re.search("/(.+?).php", url).group(1).split("-")[0]
				xemtiviso_url = "http://sv2.xemtiviso.com/mimi.php?id=" + xemtiviso_id
				h1 = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': '%s' % xemtiviso_url
				}
				(resp, content) = http.request(
					xemtiviso_url,
					"GET", headers=h1,
				)
				content = content.replace("'", '"')
				play_url = re.search('source\: "(.+?)"', content).group(1)
				play_url = play_url.replace("q=medium", "q=high")
				if "v4live" in play_url:
					return play_url
			except:
				pass
		else:
			try:
				h1 = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
					'Accept-Encoding': 'gzip, deflate',
					'Referer': '%s' % url.replace("/m.", "/www.")
				}
				(resp, content) = http.request(
					url,
					"GET", headers=h1,
				)
				content = content.replace("'", '"')
				play_url = re.search('source\: "(.+?)"', content).group(1)
				play_url = play_url.replace("q=medium", "q=high")
			except:
				pass
		return play_url
	elif "vtc.gov.vn" in url:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
			'Accept-Encoding': 'None'
		}
		(resp, content) = http.request(
			url,
			"GET",
			headers=headers
		)
		match = re.search("src: '(.+?)'", content)
		return match.group(1)
	elif "livestream.com" in url:
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
			'Accept-Encoding': 'gzip, deflate',
		}
		try:
			if "events" not in url:
				(resp, content) = http.request(
					url,
					"GET", headers=headers,
				)
				match = re.search("accounts/\d+/events/\d+", content)
				url = "https://livestream.com/api/%s" % match.group()
			(resp, content) = http.request(
				url,
				"GET", headers=headers,
			)
			j = json.loads(content)
			url = j["stream_info"]["m3u8_url"]
		except:
			pass
	elif "onecloud.media" in url:
		ocid = url.split("/")[-1].strip()
		oc_url = "http://onecloud.media/embed/" + ocid
		h = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
			'Accept-Encoding': 'gzip, deflate, sdch',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
			'X-Requested-With': 'XMLHttpRequest',
			'Cookie': 'TimeOut=999999999'}
		(resp, content) = http.request(
			oc_url,
			"POST", headers=h,
			body=urllib.urlencode({'type': 'directLink', 'ip': ''})
		)

		try:
			url = json.loads(content)["list"][0]["file"]
		except:
			header = "Có lỗi xảy ra!"
			message = "Không lấy được link (link hỏng hoặc bị xóa)"
			xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' % (header, message, 10000, ''))
			return ""
	elif "pscp.tv" in url:
		pscpid = re.search("w/(.+?)($|\?)", url).group(1)
		api_url = "https://proxsee.pscp.tv/api/v2/accessVideoPublic?broadcast_id=%s&replay_redirect=false" % pscpid
		(resp, content) = http.request(
			api_url,
			"GET"
		)
		return json.loads(content)["hls_url"]
	elif "google.com" in url:
		url = getGDriveHighestQuality(url)
	elif re.match("^https*\://www\.fshare\.vn/file", url):
		try:
			cred = GetFShareCred()
			if cred:
				fshare_headers = {
					"Accept-Encoding": "gzip, deflate, br",
					'Cookie': 'session_id=%s' % cred["session_id"]
				}
				data = {
					"url": url,
					"token": cred["token"],
					"password": ""
				}

				(resp, content) = http.request(
					convert_ipv4_url("https://api2.fshare.vn/api/session/download"), "POST",
					body=json.dumps(data),
					headers=fshare_headers
				)
				url = json.loads(content)["location"]
				url = convert_ipv4_url(url)
				if resp.status == 404:
					header = "Không lấy được link FShare VIP!"
					message = "Link không tồn tại hoặc file đã bị xóa"
					xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' % (header, message, 10000, ''))
					return None
				(resp, content) = http.request(
					url, "HEAD"
				)
				if '/ERROR' in resp['content-location']:
					header = "Không lấy được link FShare VIP!"
					message = "Link không tồn tại hoặc file đã bị xóa"
					xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' % (header, message, 10000, ''))
					return None
				return url
			return None
		except:	pass
	elif "tv24.vn" in url:
		cid = re.compile('/(\d+)/').findall(url)[0]
		return "plugin://plugin.video.sctv/play/" + cid
	elif "dailymotion.com" in url:
		did = re.compile("/(\w+)$").findall(url)[0]
		return "plugin://plugin.video.dailymotion_com/?url=%s&mode=playVideo" % did
	else:
		if "://" not in url:
			url = None
	return url

def convert_ipv4_url(url):
	host = re.search('//(.+?)(/|\:)', url).group(1)
	addrs = socket.getaddrinfo(host,443)
	ipv4_addrs = [addr[4][0] for addr in addrs if addr[0] == socket.AF_INET]
	url = url.replace(host, ipv4_addrs[0])
	return url

def LoginFShare(uname,pword):
	login_uri = "https://api2.fshare.vn/api/user/login"
	login_uri = convert_ipv4_url(login_uri)
	fshare_headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
		"Accept-Encoding": "gzip, deflate, sdch"
	}
	data = '{"app_key": "L2S7R6ZMagggC5wWkQhX2+aDi467PPuftWUMRFSn","user_email": "%s","password": "%s"}' % (uname, pword)
	resp, cont = http.request(login_uri, "POST", headers=fshare_headers, body=data)
	if "token" in cont and "session_id" in cont:
		plugin.set_setting("cred",cont)
		plugin.set_setting("hash",uname+pword)
		_json = json.loads(cont)
		return _json
	else: return None

def get_fshare_setting(s):
	try:
		return plugin.get_setting(s)
	except: return ""

def GetFShareCred():
	try:
		_hash = get_fshare_setting("hash")
		uname = get_fshare_setting("usernamefshare")
		pword = get_fshare_setting("passwordfshare")
		if _hash != (uname+pword): 
			plugin.set_setting("cred","")
		cred  = json.loads(get_fshare_setting("cred"))
		user = GetFShareUser(cred)
		LoginOKNoti(user["email"], user["level"])
		return cred
	except:
		try:
			uname = get_fshare_setting("usernamefshare")
			pword = get_fshare_setting("passwordfshare")
			cred = LoginFShare(uname,pword)
			user = GetFShareUser(cred)
			LoginOKNoti(user["email"], user["level"])
			return cred
		except: 
			dialog = xbmcgui.Dialog()
			yes = dialog.yesno(
				'Đăng nhập không thành công!\n',
				'[COLOR yellow]Bạn muốn nhập tài khoản FShare VIP bây giờ không?[/COLOR]',
				yeslabel='OK, nhập ngay',
				nolabel='Bỏ qua'
			)
			if yes:
				plugin.open_settings()
				return GetFShareCred()
			return None


def LoginOKNoti(user="",lvl=""):
	header = "Đăng nhập thành công!"
	message = "Chào user [COLOR orange]{}[/COLOR] (lvl [COLOR yellow]{}[/COLOR])".format(user, lvl)
	xbmc.executebuiltin('Notification("{}", "{}", "{}", "")'.format(header, message, "10000"))


def GetFShareUser(cred):
	user_url = "https://api2.fshare.vn/api/user/get"
	user_url = convert_ipv4_url(user_url)
	headers = {
		"Cookie": "session_id=" + cred["session_id"]
	}
	resp, cont = http.request(user_url, "GET", headers=headers)
	user = json.loads(cont)
	return user


def GetPlayLinkFromDriveID(drive_id):
	play_url = "https://drive.google.com/uc?export=mp4&id=%s" % drive_id
	(resp, content) = http.request(
		play_url, "HEAD",
		headers=sheet_headers
	)
	confirm = ""
	try:
		confirm = re.compile(
			'download_warning_.+?=(.+?);').findall(resp['set-cookie'])[0]
	except:
		return play_url
	tail = "|User-Agent=%s&Cookie=%s" % (urllib.quote(
		sheet_headers["User-Agent"]), urllib.quote(resp['set-cookie']))
	play_url = "%s&confirm=%s" % (play_url, confirm) + tail
	return play_url


def GA(title="Home", page="/"):
	'''
	Hàm thống kê lượt sử dụng bằng Google Analytics (GA)
	Parameters
	----------
	title : string
		Tên dễ đọc của view.
	page : string
		Đường dẫn của view.
	'''
	try:
		ga_url = "http://www.google-analytics.com/collect"
		client_id = open(cid_path).read()
		data = {
			'v': '1',
			'tid': 'UA-52209804-5',  # Thay GA id của bạn ở đây
			'cid': client_id,
			't': 'pageview',
			'dp': "VNPlaylist%s" % page,
			'dt': "[VNPlaylist] - %s" % title
		}
		http.request(
			ga_url, "POST",
			body=urllib.urlencode(data)
		)
	except:
		pass


def getGDriveHighestQuality(url):
	(resp, content) = http.request(
		url, "GET",
		headers=sheet_headers
	)
	match = re.compile('(\["fmt_stream_map".+?\])').findall(content)[0]
	prefer_quality = ["38", "37", "46", "22", "45", "18", "43"]
	stream_map = json.loads(match)[1].split(",")
	for q in prefer_quality:
		for stream in stream_map:
			if stream.startswith(q+"|"):
				url = stream.split("|")[1]
				tail = "|User-Agent=%s&Cookie=%s" % (urllib.quote(
					sheet_headers["User-Agent"]), urllib.quote(resp['set-cookie']))
				return url + tail


def cleanHTML(s):
	s = ''.join(s.splitlines()).replace('\'', '"')
	s = s.replace('\n', '')
	s = s.replace('\t', '')
	s = re.sub('  +', ' ', s)
	s = s.replace('> <', '><')
	return s


def version_cmp(local_version, download_version):
	def normalize(v):
		return [int(x) for x in re.sub(r'(\.0+)*$', '', v).split(".")]
	return cmp(normalize(local_version), normalize(download_version))


# Tạo client id cho GA tracking
# Tham khảo client id tại https://support.google.com/analytics/answer/6205850?hl=vi
device_path = xbmc.translatePath('special://userdata')
if os.path.exists(device_path) == False:
	os.mkdir(device_path)
cid_path = os.path.join(device_path, 'cid')
if os.path.exists(cid_path) == False:
	with open(cid_path, "w") as f:
		f.write(str(uuid.uuid1()))
if __name__ == '__main__':
	plugin.run()
