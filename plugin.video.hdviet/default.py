#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib, urllib2, json, re, urlparse, sys, time, os, hashlib
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
from BeautifulSoup import BeautifulSoup

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

my_addon = xbmcaddon.Addon()
subtitle_lang = my_addon.getSetting('subtitle')
npp = str(my_addon.getSetting('npp'))
video_quality = my_addon.getSetting('video_quality')
use_api = my_addon.getSetting('info_method') == 'API'
tm_notice = my_addon.getSetting('tm_notice') == 'true'
use_dolby_audio = my_addon.getSetting('sound') == '5.1'
try_fullhd = my_addon.getSetting('tryfullhd') == 'true'
fullhd_free = my_addon.getSetting('fullhdfree') == 'true'
apitoken = my_addon.getSetting('token')
if apitoken == 'none': apitoken = '22bb07a59d184383a3c0cd5e3db671fc'
reload(sys);

fixed_quality = (video_quality != 'Chọn khi xem')

min_width = {'SD' : 0, 'HD' : 1024, 'Full HD' : 1366}
max_width = {'SD' : 1024, 'HD' : 1366, 'Full HD' : 10000}

header_web = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1'}
header_api = {'User-Agent' : 'Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; AndyWin Build/JDQ39E) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30',
			'Access-Token' : apitoken}
header_app = {'User-agent' : 'com.hdviet.app.ios.HDViet/2.0.1 (unknown, iPhone OS 8.2, iPad, Scale/2.000000)'}

def make_request(url, params=None, headers=None):
	if headers is None:
		headers = header_web
	try:
		if params is not None:
			params = urllib.urlencode(params)
			req = urllib2.Request(url,params,headers)
		else:req = urllib2.Request(url,headers=headers)
		f = urllib2.urlopen(req)
		body=f.read()
		f.close()
		return body
	except:
		return False
def login():
	username = my_addon.getSetting('userhdviet')
	password = my_addon.getSetting('passhdviet')
	if len(username) < 5 or len(password) < 1:
		my_addon.setSetting("token", "none")
		xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR red]Chưa nhập user/password HDViet[/COLOR]',3000)).encode("utf-8"))
		return "fail"
	h = hashlib.md5()
	h.update(password)
	passwordhash = h.hexdigest()
	result = make_request('https://api-v2.hdviet.com/user/login?email=%s&password=%s' % (username,passwordhash), None, header_app)
	if "AccessTokenKey" in result:
		res = json.loads(result)["r"]
		try:
			if int(res['Vip']) == 1:
				my_addon.setSetting("vip", 'true')
		except:my_addon.setSetting("vip", 'false')
		my_addon.setSetting("token", res["AccessTokenKey"])
		xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR green]Logged in ![/COLOR]',2000)).encode("utf-8"))
		return res["AccessTokenKey"];
	else:
		#xbmcgui.Dialog().ok("HDViet", passwordhash)
		my_addon.setSetting("token", "none")
		my_addon.setSetting("vip", 'false')
		xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR red]Log in Failed ![/COLOR]',2000)).encode("utf-8"))
		return "fail"
def logout():
	my_addon.setSetting("token", "none")
	my_addon.setSetting("vip", 'false')
	xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR red]Logged out ![/COLOR]',2000)).encode("utf-8"))
def convert_vi_to_en(str):
	try:
		if str == '': return
		if type(str).__name__ == 'unicode': str = str.encode('utf-8')
		list_pat = ["á|à|ả|ạ|ã|â|ấ|ầ|ẩ|ậ|ẫ|ă|ắ|ằ|ẳ|ặ|ẵ", "Á|À|Ả|Ạ|Ã|Â|Ấ|Ầ|Ẩ|Ậ|Ẫ|Ă|Ắ|Ằ|Ẳ|Ặ|Ẵ",
					"đ", "Đ", "í|ì|ỉ|ị|ĩ", "Í|Ì|Ỉ|Ị|Ĩ", "é|è|ẻ|ẹ|ẽ|ê|ế|ề|ể|ệ|ễ", "É|È|Ẻ|Ẹ|Ẽ|Ê|Ế|Ề|Ể|Ệ|Ễ",
					"ó|ò|ỏ|ọ|õ|ô|ố|ồ|ổ|ộ|ỗ|ơ|ớ|ờ|ở|ợ|ỡ", "Ó|Ò|Ỏ|Ọ|Õ|Ô|Ố|Ồ|Ổ|Ộ|Ỗ|Ơ|Ớ|Ờ|Ở|Ợ|Ỡ",
					"ú|ù|ủ|ụ|ũ|ư|ứ|ừ|ử|ự|ữ", "Ú|Ù|Ủ|Ụ|Ũ|Ư|Ứ|Ừ|Ử|Ự|Ữ", "ý|ỳ|ỷ|ỵ|ỹ", "Ý|Ỳ|Ỷ|Ỵ|Ỹ"]
		list_re = ['a', 'A', 'd', 'D', 'i', 'I', 'e', 'E', 'o', 'O', 'u', 'U', 'y', 'Y']
		for i in range(len(list_pat)):
			str = re.sub(list_pat[i], list_re[i], str)
		return str.replace(' ', '-')
	except:
		traceback.print_exc()


def get_movies_from_html(html):
	soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)

	number_of_pages = 1

	# number of pages
	pages = soup.find('ul', 'paginglist')
	if (pages):
		pages = pages.findAll('a')
		number_of_pages = int(pages[len(pages) - 1].string)

	# movies
	movies = []
	items = soup.find(attrs = 'box-movie-list')
	items = items.findAll('li', 'mov-item')

	for item in items:
		movie = {}
		movie['id'] = item.find('div', 'tooltipthumb2').get('href').replace('#tooltip', '')
		movie['title'] = item.find('a', 'mv-namevn').get('title')
		movie['thumbnail'] = item.img.get('src').replace('124x184', 'origins')
		movie['plot'] = item.find('span', 'cot1').string
		
		eps = item.find('span', 'labelchap2')
		
		if (eps):
			movie['eps'] = int(eps.string)
		else:
			movie['eps'] = 0

		if movie['title'].startswith('Phim '):
			movie['title'] = movie['title'].replace('Phim ', '')

		movies.append(movie)

	return movies, number_of_pages

def main_menu():
	addDir('Tìm Kiếm', {'mode':'search'}, '', '')
	addDir('Phim hot trong tháng', {'mode':'movies_from_url', 'url':'http://movies.hdviet.com/phim-hot-trong-thang/trang-1.html', 'page':'1'}, '', '')
	addDir('Phim Lẻ', {'mode':'sub_menu', 'type': '0'}, '', '')
	addDir('Phim Bộ', {'mode':'sub_menu', 'type': '1'}, '', '')
	addDir('Đăng xuất tài khoản', {'mode':'logout'}, '', '')
def main_menu_api():
	addDir('Tìm Kiếm', {'mode':'search'}, '', '')
	addDir('Phim hot trong tháng', {'mode':'movies_from_api', 'cat':'hot-trong-thang', 'genre':'0','page':'1'}, '', '')
	addDir('Phim Lẻ', {'mode':'sub_menu_api', 'type': '1'}, '', '')
	addDir('Phim Bộ', {'mode':'sub_menu_api', 'type': '2'}, '', '')
	addDir('Đăng xuất tài khoản', {'mode':'logout'}, '', '')

def sub_menu(movie_type):
	soup = BeautifulSoup(make_request('http://movies.hdviet.com/'))
	
	menus = []
	
	if movie_type == '0':
		menus = soup.find(id = 'menu-phimle')
	else:
		menus = soup.find(id = 'menu-phimbo')
	
	menus = menus.findAll('a')
	first_item = True
	parrent_group = '';
	for item in menus:
		if first_item == True:
			addDir(u'Tất cả', {'mode':'movies_from_url', 'url':item.get('href').replace('.html', '/trang-1.html'), 'page':'1'}, '', '')
			first_item = False
		else:
			group_name = item.string.strip()
			if item.parent.get('class') == 'childcols2':
				addDir('%s - %s' % (parrent_group, group_name), {'mode':'movies_from_url', 'url':item.get('href').replace('.html', '/trang-1.html'), 'page':'1'}, '', '')
			else:
				addDir(group_name, {'mode':'movies_from_url', 'url':item.get('href').replace('.html', '/trang-1.html'), 'page':'1'}, '', '')
				parrent_group = group_name
def sub_menu_api(movie_type):
	cats = json.loads(make_request('http://pastebin.com/raw.php?i=idQ4kMFt', None, header_web))
	for cat in cats[movie_type]:
		addDir(cat['name'], {'mode':'movies_from_api', 'cat': cat['slug'], 'genre': movie_type,'page':'1'}, '', '')
def search():
	global use_api
	query = ''
	try:
		keyboard = xbmc.Keyboard('', '')
		keyboard.doModal()
		if (keyboard.isConfirmed()):
			query = keyboard.getText()
	except:
		pass
	
	if query != '':
		if use_api:
			if not is_ascii(query):query = convert_vi_to_en(query)
			query = urllib.quote(query)
			movies_from_search_api(query, '1')
		else:movies_from_url('http://movies.hdviet.com/tim-kiem.html?keyword=%s&page=1' % urllib.quote(query, ''), '1')
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
def get_movie_info(movie_id):
	result = json.loads(make_request('https://api-v2.hdviet.com/movie?ep=1&movieid=%s&sign=sign&sequence=0' % movie_id, None, header_app))
	return result['r']

def movies_from_url(url, page):
	page = int(page)
	
	url = re.sub(r'trang-\d+\.html', 'trang-%d.html' % page, url)
	url = re.sub(r'page=\d+', 'page=%d' % page, url)
	
	html = make_request(url)

	movies, number_of_pages = get_movies_from_html(html)
	items = []
	if (page > 1):
		addDir('Trang Trước', {'mode':'movies_from_url', 'url':url, 'page':page - 1}, '', '')

	for movie in movies:
		if (movie['eps'] == 0):
			if fixed_quality:
				addMovie(movie['title'], {'mode':'play', 'movie_id' : movie['id'], 'ep' : '0'}, movie['thumbnail'], movie['plot'])
			else:
				addDir(movie['title'], {'mode':'play', 'movie_id' : movie['id'], 'ep' : '0'}, movie['thumbnail'], movie['plot'])
		else:
			addDir(movie['title'], {'mode':'movie_detail', 'movie_id' : movie['id']}, movie['thumbnail'], movie['plot'])

	if page < number_of_pages:
		addDir('Trang Sau', {'mode':'movies_from_url', 'url':url, 'page':page + 1}, '', '')

def movies_from_api(mcat,mgenre,mpage):
	result = make_request('http://rest.hdviet.com/api/v3/movie/filter?genre=%s&tag=%s&page=%s&limit=%s' % (mgenre, mcat, mpage, npp), None, header_api)
	if not result:
		newtoken = login()
		header_api['Access-Token'] = newtoken
		result = make_request('http://rest.hdviet.com/api/v3/movie/filter?genre=%s&tag=%s&page=%s&limit=%s' % (mgenre, mcat, mpage, npp), None, header_api)
	res = json.loads(result)['data']
	movies = res['lists']
	for movie in movies:
		fanart = 'http://t.hdviet.com/backdrops/origins/' + movie['Backdrop']
		thumbnail = 'http://t.hdviet.com/thumbs/origins/' + movie['NewPoster']
		#name = movie['MovieName'] + ' - ' + movie['KnownAs']
		name = movie['MovieName']
		if movie['KnownAs'] and len(movie['KnownAs'])>0: name += ' - %s' %movie['KnownAs']
		rdate = str(movie['ReleaseDate']) 
		if len(rdate) > 3:year = rdate[:4]
		cast = []
		casts = movie['Cast'].split('/')
		for c in casts:cast.append(c.strip())
		extinfo = {"year" : year, "rating" : movie['ImdbRating'], "cast" : cast, "director" : movie['Director']}
		if (movie['Sequence'] == 0 and movie['Episode'] == 0):
			if fixed_quality:
				addMovie(name, {'mode':'play', 'movie_id' : movie['MovieID'], 'ep' : '0'}, thumbnail, movie['PlotVI'], fanart, extinfo)
			else:
				addDir(name, {'mode':'play', 'movie_id' : movie['MovieID'], 'ep' : '0'}, thumbnail, movie['PlotVI'], fanart, extinfo)
		else:
			addDir(name, {'mode':'movie_detail', 'movie_id' : movie['MovieID']}, thumbnail, movie['PlotVI'], fanart, extinfo)
	page = int(mpage)
	recordcount = page*int(npp)
	totalrecord = int(res['metadata']['totalRecord'])
	if recordcount < totalrecord:addDir('Trang Sau', {'mode':'movies_from_api', 'cat': mcat, 'genre': mgenre,'page': page+1}, '', '')
def movies_from_search_api(mkw,mpage):
	result = make_request('http://rest.hdviet.com/api/v3/search?keyword=%s&page=%s&limit=%s' % (mkw, mpage, npp), None, header_api)
	if not result:
		newtoken = login()
		header_api['Access-Token'] = newtoken
		result = make_request('http://rest.hdviet.com/api/v3/search?keyword=%s&page=%s&limit=%s' % (mkw, mpage, npp), None, header_api)
	#xbmcgui.Dialog().ok("hdviet", result)
	res = json.loads(result)['data']['response']
	movies = res['docs']
	for movie in movies:
		fanart = 'http://t.hdviet.com/backdrops/origins/' + movie['mo_backdrop']
		thumbnail = 'http://t.hdviet.com/thumbs/origins/' + movie['mo_new_poster']
		#name = movie['mo_name'] + ' - ' + movie['mo_known_as']
		name = movie['mo_name']
		if movie['mo_known_as'] and len(movie['mo_known_as'])>0: name += ' - %s' %movie['mo_known_as']
		rdate = str(movie['mo_release_date'])
		if len(rdate) > 3:year = rdate[:4]
		cast = []
		casts = movie['mo_cast'].split('/')
		for c in casts:cast.append(c.strip())
		extinfo = {"year" : year, "rating" : movie['mo_imdb_rating'], "cast" : cast, "director" : movie['mo_director'], "genre" :movie['category']}
		if (str(movie['mo_sequence']) == '0'):
			if fixed_quality:
				addMovie(name, {'mode':'play', 'movie_id' : movie['id'], 'ep' : '0'}, thumbnail, movie['mo_plot_vi'], fanart, extinfo)
			else:
				addDir(name, {'mode':'play', 'movie_id' : movie['id'], 'ep' : '0'}, thumbnail, movie['mo_plot_vi'], fanart, extinfo)
		else:
			addDir(name, {'mode':'movie_detail', 'movie_id' : movie['id']}, thumbnail, movie['mo_plot_vi'], fanart, extinfo)
	page = int(mpage)
	recordcount = page*int(npp)
	totalrecord = int(res['numFound'])
	if recordcount < totalrecord:addDir('Trang Sau', {'mode':'movies_from_search_api', 'keyword': mkw, 'page': page+1}, '', '')
def movie_detail(movie_id):
	movie_info = get_movie_info(movie_id)
	name = movie_info['MovieName']
	if movie_info['KnownAs'] and len(movie_info['KnownAs'])>0: name += ' - %s' %movie_info['KnownAs']
	if movie_info['Episode'] == '0':
		# single ep
		if fixed_quality:
			addMovie(name, {'mode':'play', 'movie_id' : movie_id, 'ep' : '1'}, movie_info['Poster'], movie_info['PlotVI'])
		else:
			addDir(name, {'mode':'play', 'movie_id' : movie_id, 'ep' : '1'}, movie_info['Poster'], movie_info['PlotVI'])
	else:
		for  i in range (1, int(movie_info['Sequence']) + 1):
			if fixed_quality:
				addMovie(u'[COLOR green][B]%d.[/B][/COLOR] %s' % (i, name), {'mode':'play', 'movie_id' : movie_id, 'ep' : i}, movie_info['Poster'], movie_info['PlotVI'])
			else:
				addDir(u'[COLOR green][B]%d.[/B][/COLOR] %s' % (i, name), {'mode':'play', 'movie_id' : movie_id, 'ep' : i}, movie_info['Poster'], movie_info['PlotVI'])
	


def play(movie_id, ep = 0):
	global header_api
	token = my_addon.getSetting('token')
	# get link to play and subtitle
	if token == 'none':
		token = login()
		header_api['Access-Token'] = token
	if token == 'fail': return
	url = 'http://rest.hdviet.com/api/v3/playlist/%s?w=1920&platform=AndroidBox&sequence=%s'
	urlx = 'https://api-v2.hdviet.com/movie/play?movieid=%s&accesstokenkey=%s&ep=%s'
	res = make_request(urlx % (movie_id, token, ep), None, header_app)
	if "0000000000" in res:
		token = login()
		header_api['Access-Token'] = token
		if token != 'fail':
			res = make_request(urlx % (movie_id, token, ep), None, header_app)
		else: return
	resj = json.loads(res)
	movie = resj["r"]
	vip = my_addon.getSetting('vip') == 'true'
	resvip = False
	if vip or resj['e'] == 1:
		resvip = make_request(url %(movie_id,ep), None, header_api)
		lp = json.loads(resvip)["data"]["playList"]
	else:lp = movie['LinkPlay']
	if lp and movie:
		subtitle_url = ''
		if subtitle_lang != 'Tắt':
			try:
				if resj['e'] == 1 and resvip:
					for sub in json.loads(resvip)['data']['subtitle']:
						if sub['sub'] == subtitle_lang:subtitle_url = sub['source']
				else:
					subtitle_url = movie['Subtitle'][subtitle_lang]['Source']
					if subtitle_url == '':
						subtitle_url = movie['SubtitleExt'][subtitle_lang]['Source']
					if subtitle_url == '':
						subtitle_url = movie['SubtitleExtSe'][subtitle_lang]['Source']
			except:
				pass

		# audioindex
		audio_index = 0
		use_vi_audio = False
		if resj['e'] != 1:
			if tm_notice and movie['Audio'] > 0:
				use_vi_audio = xbmcgui.Dialog().yesno('HDViet', '[COLOR green][B]%s[/B][/COLOR]' %movie['MovieName'],'Phim này có thuyết minh tiếng việt','Bạn có muốn sử dụng audio thuyết minh ?',nolabel='Không',yeslabel='Có',autoclose=10000)
			if use_vi_audio and movie['Audio'] > 0:audio_index = 1
			elif use_dolby_audio:
				if movie['Audio'] > 0:audio_index = 2
				else:audio_index = 1
		
		# get link and resolution
		got = False
		if try_fullhd and not vip:
			link_to_play = re.sub(r'_\d+_\d+_', '_320_4096_', lp)
			result = make_request(link_to_play, None, header_app)
			if 'RESOLUTION=' in result: got = True
		if fullhd_free and not vip and not got:
			rs = make_request(lp, None, header_app)
			ln = rs.splitlines()
			i = 0
			while (i < len(ln)):
				if 'RESOLUTION=' in ln[i]:
					i += 1
					break
				i += 1
			rs = make_request('%s?audioindex=%d' %(ln[i],audio_index), None, header_app)
			ln = rs.splitlines()
			i = 0
			while (i < len(ln)):
				if '.ts' in ln[i] and '/' in ln[i]:
					break
				i += 1
			arlk = ln[i].split('/')
			rx = ln[i].replace(arlk[len(arlk)-1],'')
			rq = rx + 'playlist.m3u8'
			try:
				rs = make_request(rq, None, header_app)
				if 'chunklist' in rs:
					result= rs.replace('chunklist','%schunklist'%rx)
					got = True
			except:pass
		if not got:
			link_to_play = lp
			result = make_request(link_to_play, None, header_app)
		
		
		playable_items = []
		lines = result.splitlines()

		i = 0
		# find the first meaning line
		while (i < len(lines)):
			if 'RESOLUTION=' in lines[i]:
				break
			i += 1
		while (i < len(lines)):
			playable_item = {}
			playable_item['res'] = lines[i][lines[i].index('RESOLUTION=') + 11:]

			if lines[i + 1].startswith('http'):
				playable_item['url'] = lines[i + 1]
			else:
				playable_item['url'] = lp.replace('playlist.m3u8', lines[i + 1])

			playable_items.append(playable_item)
			i += 2
		
		if not fixed_quality:
			for item in playable_items:
				addMovie(item['res'], {'mode':'play_url', 'stream_url' : '%s?audioindex=%d' % (item['url'], audio_index), 'subtitle_url' : subtitle_url}, '', '')
		else:
			i = len(playable_items) - 1
			while (i >= 0):
				current_width = int(playable_items[i]['res'].split('x')[0])
				if (min_width[video_quality] <= current_width and max_width[video_quality] > current_width) or current_width < min_width[video_quality]:
					break
				i -= 1

			if i >= 0:
				set_resolved_url('%s?audioindex=%d' % (playable_items[i]['url'], audio_index), subtitle_url)

	
def set_resolved_url(stream_url, subtitle_url):
	h1 = '|User-Agent=' + urllib.quote_plus('HDViet/2.0.1 CFNetwork/711.2.23 Darwin/14.0.0')
	h2 = '&Accept=' + urllib.quote_plus('*/*')
	xbmcplugin.setResolvedUrl(addon_handle, succeeded=True, listitem=xbmcgui.ListItem(label = '', path = stream_url))
	
	datapath=xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
	subtitlePath = os.path.join(datapath,'subs')
	try:
		if subtitle_url != '':
			sublink = subtitle_url.split('/')
			subfile = os.path.join(subtitlePath, sublink[len(sublink)-1])
			if not os.path.exists(subtitlePath):os.mkdir(subtitlePath)
			for file in os.listdir(subtitlePath):
				if os.path.isfile(os.path.join(subtitlePath,file)):
					try:os.remove(os.path.join(subtitlePath,file))
					except:pass
			f = urllib2.urlopen(subtitle_url)
			with open(subfile, "wb") as code:
				code.write(f.read())
			xbmc.sleep(1000)
			timeout = 0
			while not xbmc.Player().isPlaying() and timeout < 60:
				xbmc.sleep(500)
				timeout += 1
			if timeout < 60:
				xbmc.Player().setSubtitles(subfile)
				xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR green]Subtitle Loaded ![/COLOR]',2000)).encode("utf-8"))
			else:xbmc.executebuiltin((u'XBMC.Notification(%s,%s,%s)'%('HDViet','[COLOR red]Connection timed out ![/COLOR]',2000)).encode("utf-8"))
	except:
		pass

def build_url(query):
	return base_url + '?' + urllib.urlencode(query)


def addDir(name,query,iconimage, plot, fanart = False, extendinfo = False):
	addItem(name, query, iconimage, plot, True, fanart, extendinfo)
	
def addMovie(name,query,iconimage, plot, fanart = False, extendinfo = False):
	addItem(name, query, iconimage, plot, False, fanart, extendinfo)
	
def addItem(name,query,iconimage, plot, isFolder, fanart = False, extendinfo = False):
	u=build_url(query)
	ok=True
	liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
	if fanart:liz.setProperty('Fanart_Image',fanart)
	mediainfo = {"Title": name, "Plot" : plot}
	if extendinfo:mediainfo.update(extendinfo)
	liz.setInfo( type="Video", infoLabels=mediainfo)
	if not isFolder:
		liz.setProperty('IsPlayable', 'true')
	ok=xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=liz,isFolder=isFolder)
	return ok

mode = args.get('mode', None)

if mode is None:
	if use_api:main_menu_api()
	else:main_menu()
elif mode[0] == 'sub_menu':
	type = args.get('type', None)
	sub_menu(type[0])
elif mode[0] == 'sub_menu_api':
	type = args.get('type', None)
	sub_menu_api(type[0])
elif mode[0] == 'movies_from_url':
	url = args.get('url', None)
	page = args.get('page', None)
	movies_from_url(url[0], page[0])
elif mode[0] == 'movies_from_api':
	cat = args.get('cat', None)
	page = args.get('page', None)
	genre = args.get('genre', None)
	movies_from_api(cat[0], genre[0],page[0])
elif mode[0] == 'movies_from_search_api':
	keyword = args.get('keyword', None)
	page = args.get('page', None)
	movies_from_search_api(keyword[0], page[0])
elif mode[0] == 'movie_detail':
	movie_detail(args.get('movie_id', None)[0])
elif mode[0] == 'play':
	play(args.get('movie_id', None)[0], args.get('ep', None)[0])
elif mode[0] == 'play_url':
	set_resolved_url(args.get('stream_url', None)[0], args.get('subtitle_url', None)[0])
elif mode[0] == 'search':
	search()
elif mode[0] == 'logout':
	logout()
	
xbmcplugin.endOfDirectory(int(sys.argv[1]))