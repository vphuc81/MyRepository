# -*- coding: utf-8 -*-

"""
Copyright (C) 2015 PodGod

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
"""

import urllib, urllib2, sys, re, os, unicodedata, cookielib, random, shutil
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, base64
from operator import itemgetter, attrgetter

plugin_handle = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = 'plugin.video.ccloudtv')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
getSetting = xbmcaddon.Addon().getSetting
enable_adult_section = mysettings.getSetting('enable_adult_section')
enable_tvguide = mysettings.getSetting('enable_tvguide')
enable_thongbao = mysettings.getSetting('enable_thongbao')
enable_vietmedia = mysettings.getSetting('enable_vietmedia')
enable_channel_tester = mysettings.getSetting('enable_channel_tester')
enable_local_tester = mysettings.getSetting('enable_local_tester')
enable_public_uploads = mysettings.getSetting('enable_public_uploads')
enable_links_to_tutorials = mysettings.getSetting('enable_links_to_tutorials')
local_path = mysettings.getSetting('local_path')
enable_online_tester = mysettings.getSetting('enable_online_tester')
online_path = mysettings.getSetting('online_path')
viet_mode = mysettings.getSetting('viet_mode')

local_thongbaomoi = xbmc.translatePath(os.path.join(home, 'thongbaomoi.txt'))
local_vietradio = xbmc.translatePath(os.path.join(home, 'vietradio.m3u')) 
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
iconpath = xbmc.translatePath(os.path.join(home, 'resources/icons'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
group_title_regex = 'group-title=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'
adult_regex = '#(.+?)group-title="Adult",(.+)\s*(.+)\s*'
adult_regex2 = '#(.+?)group-title="Public-Adult",(.+)\s*(.+)\s*'
ondemand_regex = '[ON\'](.*?)[\'nd]'
server_regex = '<server>(.+?)</server>'
yt = 'http://www.youtube.com'
text = 'http://pastebin.com/raw.php?i=Zr0Hgrbw'
m3u = 'WVVoU01HTkViM1pNTTBKb1l6TlNiRmx0YkhWTWJVNTJZbE01ZVZsWVkzVmpSMmgzVURKck9WUlViRWxTYXpWNVZGUmpQUT09'.decode('base64')
SRVlist = 'YUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM1pwWlhSalkyeHZkV1IwZGk5eVpYQnZjMmwwYjNKNUxuWnBaWFJqWTJ4dmRXUXZiV0Z6ZEdWeUwwMTVSbTlzWkdWeUwzTmxjblpsY25NdWRIaDA='.decode('base64').decode('base64')
dict = {';':'', '&amp;':'&', '&quot;':'"', '.':' ', '&#39;':'\'', '&#038;':'&', '&#039':'\'', '&#8211;':'-', '&#8220;':'"', '&#8221;':'"', '&#8230':'...'}

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req) 
		link = response.read()
		response.close()  
		return link
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

def select_server():
	try:
		for server in (CCLOUDTV_SRV_URL):
			content = make_request(server)
			if content is None:
				server = CCLOUDTV_SRV_URL[CCLOUDTV_SRV_URL.index(server)+1]
			else:
				return content
	except:
		xbmc.executebuiltin('XBMC.Notification(%s, %s, %s, %s)' % ('[B]cCloudtv[/B]', 'All cCloud TV servers seem to be down. Please try again in a few minutes.', 10000, icon))

def replace_all(text, dict):
	try:
		for a, b in dict.iteritems():
			text = text.replace(a, b)
		return text
	except:
		pass

def platform():
	if xbmc.getCondVisibility('system.platform.android'):
		return 'android'
	elif xbmc.getCondVisibility('system.platform.linux'):
		return 'linux'
	elif xbmc.getCondVisibility('system.platform.windows'):
		return 'windows'
	elif xbmc.getCondVisibility('system.platform.osx'):
		return 'osx'
	elif xbmc.getCondVisibility('system.platform.atv2'):
		return 'atv2'
	elif xbmc.getCondVisibility('system.platform.ios'):
		return 'ios'

def main():
	addDir('[COLOR royalblue][B]***Latest Announcements***[/B][/COLOR]', yt, 3, '%s/announcements.png'% iconpath, fanart)
	if enable_thongbao == 'true':
		addDir('[COLOR royalblue][B]***Thông Báo Mới***[/B][/COLOR]', yt, 4, '%s/thongbaomoi.png'% iconpath, fanart)
	addDir('[COLOR red][B]Search[/B][/COLOR]', 'searchlink', 99, '%s/search.png'% iconpath, fanart)
	if len(CCLOUDTV_SRV_URL) > 0:
		addDir('[COLOR yellow][B]All Channels[/B][/COLOR]', yt, 2, '%s/allchannels.png'% iconpath, fanart)
	if (len(CCLOUDTV_SRV_URL) < 1 ):
		mysettings.openSettings()
		xbmc.executebuiltin("Container.Refresh")
	if enable_tvguide == 'true':        
		addDir('[COLOR yellow][B]TV Guide[/B][/COLOR]', 'guide', 97, '%s/guide.png'% iconpath, fanart)     
	if enable_channel_tester == 'true':   
		addDir('[COLOR lime][B]Channel Tester[/B][/COLOR]', 'channeltester', 40, '%s/channeltester.png'% iconpath, fanart)   
	if enable_local_tester == 'true':     
		addDir('[COLOR lime][B]Local M3U Playlist Tester[/B][/COLOR]', 'localtester', 41, '%s/localtester.png'% iconpath, fanart)
	if enable_online_tester == 'true':     
		addDir('[COLOR lime][B]Online M3U Playlist Tester[/B][/COLOR]', 'onlinetester', 42, '%s/onlinetester.png'% iconpath, fanart)
	if enable_vietmedia == 'true':
		addDir('[COLOR orange][B]VietMedia - YouTube[/B][/COLOR]', 'NoLinkRequired', 20, '%s/vietmedia.png'% iconpath, fanart)
	if platform() == 'windows' or platform() == 'osx':
		if enable_public_uploads == 'true':
			addDir('[COLOR brown][B]Public Uploads[/B][/COLOR]', public_uploads, None, '%s/ChromeLauncher.png'% iconpath, fanart)
		if enable_links_to_tutorials == 'true':
			addDir('[COLOR green][B]Links to Tutorials[/B][/COLOR]', 'TutorialLinks', 27, '%s/tutlinks.png'% iconpath, fanart)
	if viet_mode == 'group':           
		addDir('[COLOR royalblue][B]Vietnam[/B][/COLOR]', 'vietnam_group', 30, '%s/vietnam.png'% iconpath, fanart)
	if viet_mode == 'abc order':           
		addDir('[COLOR royalblue][B]Vietnam[/B][/COLOR]', 'vietnam_abc_order', 48, '%s/vietnam.png'% iconpath, fanart)
	if viet_mode == 'category': 
		addDir('[COLOR royalblue][B]Vietnam[/B][/COLOR]', 'vietnam_category', 70, '%s/vietnam.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]English[/B][/COLOR]', 'english', 62, '%s/english.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Top 10[/B][/COLOR]', 'top10', 51, '%s/top10.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Sports[/B][/COLOR]', 'sports', 52, '%s/sports.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]News[/B][/COLOR]', 'news', 53, '%s/news.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Documentary[/B][/COLOR]', 'documentary', 54, '%s/documentary.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Entertainment[/B][/COLOR]', 'entertainment', 55, '%s/entertainment.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Family[/B][/COLOR]', 'family', 56, '%s/family.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Lifestyle[/B][/COLOR]', 'lifestyle', 63, '%s/lifestyle.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Movies[/B][/COLOR]', 'movie', 57, '%s/movies.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Music[/B][/COLOR]', 'music', 58, '%s/music.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]On Demand Movies[/B][/COLOR]', 'ondemandmovies', 59, '%s/ondemandmovies.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]On Demand Shows[/B][/COLOR]', 'ondemandshows', 65, '%s/ondemandshows.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]24/7 Channels[/B][/COLOR]', '24', 60, '%s/twentyfourseven.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Radio[/B][/COLOR]', 'radio', 61, '%s/radio.png'% iconpath, fanart)
	addDir('[COLOR royalblue][B]Non-English/International (Z-A)[/B][/COLOR]', 'international', 64,'%s/international.png'% iconpath, fanart)
	if getSetting("enable_adult_section") == 'true':
		addDir('[COLOR magenta][B]Adult(18+)[/B][/COLOR]', 'adult', 98, '%s/adult.png'% iconpath, fanart)

def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))

def search(): 
	try:
		keyb = xbmc.Keyboard('', 'Enter Channel Name')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def tutorial_links():
	#content = read_file(os.path.expanduser(m3uFolder + 'tutoriallinks.m3u'))
	content = make_request(tutoriallinks)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'plugin.program.chrome.launcher' in url:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				if thumb.startswith('http'):               
					addDir(name, url, None, thumb, thumb)
				else:
					thumb = '%s/%s' % (iconpath, thumb)
					addDir(name, url, None, thumb, thumb)
			else:      
				addDir(name, url, None, icon, fanart)
		else:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				if thumb.startswith('http'):               
					addLink(name, url, 1, thumb, thumb)
				else:
					thumb = '%s/%s' % (iconpath, thumb)
					addLink(name, url, 1, thumb, thumb)
			else:      
				addLink(name, url, 1, icon, fanart)

def vietmedia_list():       
	addDir('[COLOR magenta][B]Playlists[/B][/COLOR]', (vietmediaurl + '/playlists'), 21, '%s/YTPlaylist.png'% iconpath, fanart)
	link = make_request(vietmediaurl + '/videos')
	link = ''.join(link.splitlines()).replace('\t','')
	match = re.compile('src="//i.ytimg.com/vi/(.+?)".+?aria-label.+?>(.+?)</span>.+?href="/watch\?v=(.+?)">(.+?)</a>').findall(link)
	for thumb, duration, url, name in match:
		name = replace_all(name, dict)
		thumb = 'https://i.ytimg.com/vi/' + thumb
		addLink(name + '[COLOR orange] (' + duration + ')[/COLOR]', 'plugin://plugin.video.youtube/play/?video_id=' + url, 1, thumb, thumb)
	try:
		match = re.compile('data-uix-load-more-href="(.+?)"').findall(link)
		addDir('[COLOR yellow][B]Next page [/B][/COLOR][COLOR lime][B]>>[/B][/COLOR]', 'https://www.youtube.com' + match[0].replace('&amp;','&'), 23, '%s/nextpage.png'% iconpath, fanart)
	except:
		pass

def vietmedia_playlist(url): 
	link = make_request(url)
	link = ''.join(link.splitlines()).replace('\t','')  
	match = re.compile('src="//i.ytimg.com/vi/(.+?)".+?href="/playlist(.+?)">(.+?)<').findall(link)
	for thumb, url, name in match:
		name = replace_all(name, dict)
		thumb = 'https://i.ytimg.com/vi/' + thumb
		addDir(name, url, 22, thumb, thumb)

def vietmedia_playlist_index(url):      
	link = make_request('https://www.youtube.com/playlist' + url)
	link = ''.join(link.splitlines()).replace('\t','')
	newmatch = re.compile('data-title="(.+?)".+?href="\/watch\?v=(.+?)\&amp\;.+?data-thumb="(.+?)".+?aria-label.+?>(.+?)<\/span><\/div>').findall(link)
	for name, url, thumb, duration in newmatch:
		name = replace_all(name, dict)
		thumb = 'https:' + thumb
		if '[Deleted Video]' in name:
			pass
		else:
			addLink(name + '[COLOR orange] (' + duration + ')[/COLOR]', 'plugin://plugin.video.youtube/play/?video_id=' + url, 1, thumb, thumb)
	try:
		match = re.compile('data-uix-load-more-href="(.+?)"').findall(link)
		addDir('[COLOR magenta]Next page >>[/COLOR]', 'https://www.youtube.com' + match[0].replace('&amp;','&'), 23, '%s/nextpage.png'% iconpath, fanart)
	except:
		pass
        
def next_page(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
	response = urllib2.urlopen(req) 
	link = response.read().decode('unicode-escape').encode('utf-8').replace('\\', '')
	response.close()
	newlink = ''.join(link.splitlines()).replace('\t','')
	match = re.compile('src="//i.ytimg.com/vi/(.+?)".+?aria-label.+?>(.+?)</span>.+?href="/watch\?v=(.+?)">(.+?)</a>').findall(newlink)
	for thumb, duration, url, name in match:
		name = replace_all(name, dict)
		thumb = 'https://i.ytimg.com/vi/' + thumb
		addLink(name + '[COLOR orange] (' + duration + ')[/COLOR]', 'plugin://plugin.video.youtube/play/?video_id=' + url, 1, thumb, thumb)
	try:
		match = re.compile('data-uix-load-more-href="(.+?)"').findall(newlink)  
		addDir('[COLOR magenta]Next page >>[/COLOR]', 'https://www.youtube.com' + match[0].replace('&amp;','&'), 23, '%s/nextpage.png'% iconpath, fanart)
	except:
		pass

def vietmedia_tutorials():
	thumb = 'https://yt3.ggpht.com/-Y4hzMs0ItTw/AAAAAAAAAAI/AAAAAAAAAAA/OquSyoI-Y2s/s100-c-k-no/photo.jpg'
	addLink('[COLOR orange][B]VietMedia - YouTube - Hướng Dẫn[/B][/COLOR]', 'NoLinkRequired', 1, thumb, thumb)
	content = make_request(koditutorials)
	newcontent = ''.join(content.splitlines()).replace('\t','')
	newmatch = re.compile('data-title="(.+?)".+?href="\/watch\?v=(.+?)\&amp\;.+?data-thumb="(.+?)".+?aria-label.+?>(.+?)<\/span><\/div>').findall(newcontent)
	for name, url, thumb, duration in newmatch:
		thumb = 'https:' + thumb
		if '[Deleted Video]' in name:
			pass
		else:
			name = replace_all(name, dict)
			addLink(name + '[COLOR orange] (' + duration + ')[/COLOR]', 'plugin://plugin.video.youtube/play/?video_id=' + url, 1, thumb, thumb)
	content = make_request(thuthuatkodi)
	newcontent = ''.join(content.splitlines()).replace('\t','')
	newmatch = re.compile('data-title="(.+?)".+?href="\/watch\?v=(.+?)\&amp\;.+?data-thumb="(.+?)".+?aria-label.+?>(.+?)<\/span><\/div>').findall(newcontent)
	for name, url, thumb, duration in newmatch:
		thumb = 'https:' + thumb
		if '[Deleted Video]' in name:
			pass
		else:
			name = replace_all(name, dict)
			addLink(name + '[COLOR orange] (' + duration + ')[/COLOR]', 'plugin://plugin.video.youtube/play/?video_id=' + url, 1, thumb, thumb)
	thumb1 = '%s/utube.png'% iconpath
	addLink('[COLOR magenta][B]Other Tutorials on YouTube - Những Hướng Dẫn Khác[/B][/COLOR]', 'NoLinkRequired', 1, thumb1, thumb1)
	#content = read_file(os.path.expanduser(m3uFolder + 'tutoriallinks.m3u'))
	content = make_request(tutoriallinks)
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'plugin.video.youtube' in url:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				if thumb.startswith('http'):
					addLink(name, url, 1, thumb, thumb)
				else:
					thumb = '%s/%s' % (iconpath, thumb)
					addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
		else:
			pass

def vietnam_abc_order():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					else:
						m3u_playlist(name, url, thumb)
	except:
		pass
	try:
		content = make_request(haingoaitv)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
		content = make_request(vietradio)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
		vietmedia_tutorials()
	except:
		pass

def vietnam_group():
	addDir('Movies', 'vietnam_group', 77, '%s/group.png'% iconpath, fanart)
	addDir('Music', 'vietnam_group', 75, '%s/group.png'% iconpath, fanart)
	addDir('Radio', 'vietnam_group', 79, '%s/group.png'% iconpath, fanart)
	addDir('Sports', 'vietnam_group', 82, '%s/group.png'% iconpath, fanart)
	addDir('Tutorials', 'vietnam_group', 83, '%s/group.png'% iconpath, fanart)
	addDir('TV', 'vietnam_group', 31, '%s/group.png'% iconpath, fanart)

def viet_tv_group():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)): 
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name) or ('OnDemandMovies' in name) or ('Music' in name) or ('Radio' in name) or ('Sports' in name) or ('Tutorials' in name):
						pass
					else:
						m3u_playlist(name, url, thumb)
	except:
		pass
	try:
		content = make_request(haingoaitv)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
	except:
		pass

def vietnam_category(): 
	addDir('Documentary', 'vietnam_category', 71, '%s/category.png'% iconpath, fanart)
	addDir('Entertainment', 'vietnam_category', 72, '%s/category.png'% iconpath, fanart)
	addDir('Family', 'vietnam_category', 73, '%s/category.png'% iconpath, fanart)
	addDir('Movie Channels', 'vietnam_category', 74, '%s/category.png'% iconpath, fanart)
	addDir('Music', 'vietnam_category', 75, '%s/category.png'% iconpath, fanart)
	addDir('News', 'vietnam_category', 76, '%s/category.png'% iconpath, fanart)
	addDir('On Demand Movies', 'vietnam_category', 77, '%s/category.png'% iconpath, fanart)
	addDir('On Demand Shows', 'vietnam_category', 78, '%s/category.png'% iconpath, fanart)
	addDir('Radio', 'vietnam_category', 79, '%s/category.png'% iconpath, fanart)
	addDir('Random Air Time 24/7', 'vietnam_category', 80, '%s/category.png'% iconpath, fanart)
	addDir('Special Events', 'vietnam_category', 81, '%s/category.png'% iconpath, fanart)
	addDir('Sports', 'vietnam_category', 82, '%s/category.png'% iconpath, fanart)
	addDir('Tutorials', 'vietnam_category', 83, '%s/category.png'% iconpath, fanart)

def viet_Documentary():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Documentary' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Entertainment():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Entertainment' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Family():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Family' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass
	try:
		content = make_request(haingoaitv)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
	except:
		pass

def viet_Movie_Channels():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Movie Channels' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Music():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Music' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_News():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'News' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_OnDemandMovies():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'OnDemandMovies' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_OnDemandShows():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'OnDemandShows' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Radio():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Radio' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass
	try:
		content = make_request(vietradio)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			if 'tvg-logo' in thumb:
				thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
				addLink(name, url, 1, thumb, thumb)
			else:
				addLink(name, url, 1, icon, fanart)
	except:
		pass

def viet_RandomAirTime():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'RandomAirTime 24/7' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Special_Events():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Special Events' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Sports():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Sports' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass

def viet_Tutorials():
	try:
		searchText = '\(VN\)|(Vietnamese)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if (re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					if 'Tutorials' in name:
						m3u_playlist(name, url, thumb)
	except:
		pass
	try:
		vietmedia_tutorials()
	except:
		pass

def top10():
	try:
		searchText = '(Top10)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def sports():
	try:
		searchText = '(Sports)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def news():
	try:
		searchText = '(News)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def documentary():
	try:
		searchText = '(Document)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def entertainment():
	try:
		searchText = '(Entertainment)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def family():
	try:
		searchText = '(Family)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def lifestyle():
	try:
		searchText = '(Lifestyle)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def movie():
	try:
		searchText = '(Movie Channels)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def music():
	try:
		searchText = '(Music)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def ondemandmovies():
	try:
		searchText = '(OnDemandMovies)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def ondemandshows():
	try:
		searchText = '(OnDemandShows)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def twentyfour7():
	try:
		searchText = '(RandomAirTime 24/7)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def radio():
	try:
		searchText = '(Radio)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def adult():
	try:
		searchText = ('(Adult)') or ('(Public-Adult)')
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(adult_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					adult_playlist(name, url, thumb)
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(adult_regex2).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					adult_playlist(name, url, thumb)
	except:
		pass

def english():
	try:
		searchText = '(English)'
		if len(CCLOUDTV_SRV_URL) > 0:
			content = select_server()
			match = re.compile(m3u_regex).findall(content)
			for thumb, name, url in sorted(match, key = itemgetter(1)):
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
	except:
		pass

def international():
	if len(CCLOUDTV_SRV_URL) > 0:
		content = select_server()
		match = sorted(re.compile(m3u_regex).findall(content), key = itemgetter(1))
		try:
			searchVietnamese = '\(VN\)|(Vietnamese)'
			for thumb, name, url in match:
				if (re.search(searchVietnamese, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE)):
					if ('\(Adult\)' in name) or ('\(Public-Adult\)' in name):
						pass
					else:
						m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchUrdu = '(Urdu)'
			for thumb, name, url in match:
				if re.search(searchUrdu, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchUkrainian = '(Ukrainian)'
			for thumb, name, url in match:
				if re.search(searchUkrainian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchTamil = '(Tamil)'
			for thumb, name, url in match:
				if re.search(searchTamil, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchSpanish = '(Spanish)'
			for thumb, name, url in match:
				if re.search(searchSpanish, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchSomali = '(Somali)'
			for thumb, name, url in match:
				if re.search(searchSomali, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchSlovenian = '(Slovenian)'
			for thumb, name, url in match:
				if re.search(searchSlovenian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchRussian = '(Russian)'
			for thumb, name, url in match:
				if re.search(searchRussian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchRomanian = '(Romanian)'
			for thumb, name, url in match:
				if re.search(searchRomanian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchPortuguese = '(Portuguese)'
			for thumb, name, url in match:
				if re.search(searchPortuguese, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchPolish = '(Polish)'
			for thumb, name, url in match:
				if re.search(searchPolish, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchMandarin = '(Mandarin)'
			for thumb, name, url in match:
				if re.search(searchFilipino, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchMaltese = '(Maltese)'
			for thumb, name, url in match:
				if re.search(searchMaltese, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchMacedonian = '(Macedonian)'
			for thumb, name, url in match:
				if re.search(searchMacedonian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchLithuanian = '(Lithuanian)'
			for thumb, name, url in match:
				if re.search(searchLithuanian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchKurdish = '(Kurdish)'
			for thumb, name, url in match:
				if re.search(searchKurdish, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchJamaica = '(Jamaica)'
			for thumb, name, url in match:
				if re.search(searchJamaica, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchItalian = '(Italian)'
			for thumb, name, url in match:
				if re.search(searchItalian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchIsraeli = '(Israeli)'
			for thumb, name, url in match:
				if re.search(searchIsraeli, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchIndian = '(Indian)'
			for thumb, name, url in match:
				if re.search(searchIndian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchhungarian = '(Hungarian)'
			for thumb, name, url in match:
				if re.search(searchHungarian, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchHindi = '(Hindi)'
			for thumb, name, url in match:
				if re.search(searchHindi, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchGreek = '(Greek)'
			for thumb, name, url in match:
				if re.search(searchGreek, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchGerman = '(German)'
			for thumb, name, url in match:
				if re.search(searchGerman, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchFrench = '(French)'
			for thumb, name, url in match:
				if re.search(searchFrench, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchFilipino = '(Filipino)'
			for thumb, name, url in match:
				if re.search(searchFilipino, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchFarsi = '(Farsi)'
			for thumb, name, url in match:
				if re.search(searchFarsi, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchDutch = '(Dutch)'
			for thumb, name, url in match:
				if re.search(searchDutch, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchDeutsch = '(Deutsch)'
			for thumb, name, url in match:
				if re.search(searchDeutsch, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchChinese = '(Chinese)'
			for thumb, name, url in match:
				if re.search(searchChinese, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchCatalan = '(Catalan)'
			for thumb, name, url in match:
				if re.search(searchCatalan, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchArabic = '(Arabic)'
			for thumb, name, url in match:
				if re.search(searchArabic, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass
		try:
			searchAfrikaans = '(Afrikaans)'
			for thumb, name, url in match:
				if re.search(searchAfrikaans, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					m3u_playlist(name, url, thumb)
		except:
			pass

def thongbao():
	try:
		text = '[COLOR royalblue][B]***Thông Báo Mới***[/B][/COLOR]'
		if urllib.urlopen(thongbaomoi).getcode() == 200:
			link = make_request(thongbaomoi)
		else:
			link = read_file(local_thongbaomoi)
		match=re.compile("<START>(.+?)<END>",re.DOTALL).findall(link)
		for status in match:
			try:
					status = status.decode('ascii')
			except:
					status = status.decode('utf-8')
			status = status.replace('&amp;','')
			text = status
		showText('[COLOR royalblue][B]***Thông Báo Mới***[/B][/COLOR]', text)
	except:
		pass

def text_online():
	text = '[COLOR royalblue][B]***Latest Announcements***[/B][/COLOR]'
	newstext = 'http://pastebin.com/raw.php?i=7K3zDiZ2'
	req = urllib2.Request(newstext)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	match=re.compile("<START>(.+?)<END>",re.DOTALL).findall(link)
	for status in match:
		try:
				status = status.decode('ascii', 'ignore')
		except:
				status = status.decode('utf-8','ignore')
		status = status.replace('&amp;','')
		text = status
	showText('[COLOR royalblue][B]***Latest Announcements***[/B][/COLOR]', text)

def showText(heading, text):
	id = 10147
	xbmc.executebuiltin('ActivateWindow(%d)' % id)
	xbmc.sleep(100)
	win = xbmcgui.Window(id)
	retry = 50
	while (retry > 0):
		try:
			xbmc.sleep(10)
			retry -= 1
			win.getControl(1).setLabel(heading)
			win.getControl(5).setText(text)
			return
		except:
			pass

def guide():
	dialog = xbmcgui.Dialog()
	ret = dialog.yesno('cCloud TV Guide', '[COLOR yellow]cCloud TV[/COLOR] is now integrated with your favourite TV Guides.','This is currently in beta and not all channels are supported.','[COLOR yellow]>>>>>>>>>>>>>  Choose Your Guide Below  <<<<<<<<<<<<<[/COLOR]','iVue TV Guide','Renegades TV Guide')
	if ret == 1:
		xbmc.executebuiltin("RunAddon(script.renegadestv)")
		sys.exit()
	if ret == 0:
		xbmc.executebuiltin("RunAddon(script.ivueguide)")
		sys.exit()
	else:
		sys.exit()

def channelTester():
	try:
		keyb = xbmc.Keyboard('', 'Enter Channel Name [COLOR lime]- Tiếng Việt Không Dấu[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			name = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		keyb = xbmc.Keyboard('', 'Enter Channel URL [COLOR lime](m3u8, rtmp, mp4)[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			url = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		keyb = xbmc.Keyboard('', 'Enter Logo URL [COLOR lime]- Không Bắt Buộc[/COLOR]')
		keyb.doModal()
		if (keyb.isConfirmed()):
			thumb = urllib.quote_plus(keyb.getText(), safe="%/:=&?~#+!$,;'@()*[]").replace('+', ' ')
		if len(name) > 0 and len(url) > 0:
			if len(thumb) < 1:
				thumb = icon
			addLink(name, url, 1, thumb, fanart)
	except:
		pass

def localTester():
	if len(local_path) < 1:
		mysettings.openSettings()
		sys.exit()
	else:
		content = read_file(local_path)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			try:
				m3u_playlist(name, url, thumb)
			except:
				pass

def onlineTester():
	if len(online_path) < 1:
		mysettings.openSettings()
		sys.exit()
	else:
		content = make_request(online_path)
		match = re.compile(m3u_regex).findall(content)
		for thumb, name, url in match:
			try:
				m3u_playlist(name, url, thumb)
			except:
				pass

def m3u_online():
	content = select_server() 
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match[0:1]:
		m3u_playlist('[COLOR yellow][B]' + name + '[/B][/COLOR]', url, thumb)
	for thumb, name, url in sorted(match, key = itemgetter(1)):
		try:
			if 'Welcome to cCloudTV' in name:
				pass
			else:
				m3u_playlist(name, url, thumb)
		except:
			pass

def m3u_playlist(name, url, thumb):
	name = re.sub('\s+', ' ', name).strip()
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addDir(name, url, '', thumb, thumb)
		else:
			addDir(name, url, '', icon, fanart)
	else:
		if ('(Adult)' in name) or ('(Public-Adult)' in name):
			name = 'ADULTS ONLY'.url = 'http://ignoreme.com'
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url
		else:
			url = url
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addLink(name, url, 1, thumb, thumb)
		else:
			addLink(name, url, 1, icon, fanart)

def adult_playlist(name, url, thumb):
	name = re.sub('\s+', ' ', name).strip()
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addDir(name, url, '', thumb, thumb)
		else:
			addDir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url
		else:
			url = url
		if 'tvg-logo' in thumb:
			thumb = re.compile(m3u_thumb_regex).findall(str(thumb))[0].replace(' ', '%20')
			addLink(name, url, 1, thumb, thumb)
		else:
			addLink(name, url, 1, icon, fanart)

def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

List1 = 'YUhSMGNEb3ZMMnR2WkdrdVkyTnNaQzVwYnc9PQ=='.decode('base64') .decode('base64')
List2 = 'YUhSMGNEb3ZMM2d1WTI4dlpHSmphREF4'.decode('base64') .decode('base64')
List3 = 'YUhSMGNEb3ZMMkZwYnk1alkyeHZkV1IwZGk1dmNtY3ZhMjlrYVE9PQ=='.decode('base64') .decode('base64')
List4 = 'YUhSMGNEb3ZMMmR2TW13dWFXNXJMMnR2WkdrPQ=='.decode('base64') .decode('base64')
List5 = 'YUhSMGNEb3ZMM051YVhBdWJHa3ZhMjlrYVE9PQ=='.decode('base64') .decode('base64')            
#CCLOUDTV_SRV_URL = [List1, List2, List3, List4, List5]
CCLOUDTV_SRV_URL = re.compile(server_regex).findall(make_request(SRVlist)) 
m3uFolder = 'Zmk5RWIyTjFiV1Z1ZEhNdlIybDBTSFZpTDNKbGNHOXphWFJ2Y25rdWRtbGxkR05qYkc5MVpDOU5lVVp2YkdSbGNpOD0='.decode('base64').decode('base64')
vietmediaurl = 'YUhSMGNITTZMeTkzZDNjdWVXOTFkSFZpWlM1amIyMHZZMmhoYm01bGJDOVZRMk4xYzNwdFEyeHRWVjlxTjNaak9VNWlXVUUyVkhjPQ=='.decode('base64').decode('base64')
koditutorials = 'YUhSMGNITTZMeTkzZDNjdWVXOTFkSFZpWlM1amIyMHZjR3hoZVd4cGMzUS9iR2x6ZEQxUVRFTkdaWGw0WVVSZk4wVXpNRWxpYW1odE9FUTFjVzQzUzFWV1JFVTNiM015'.decode('base64').decode('base64')
thuthuatkodi = 'YUhSMGNITTZMeTkzZDNjdWVXOTFkSFZpWlM1amIyMHZjR3hoZVd4cGMzUS9iR2x6ZEQxUVRFTkdaWGw0WVVSZk4wVXpURXh4YW1oSmQydGliMEZsVUdkRVZDMHRPRmxH'.decode('base64').decode('base64')
tutoriallinks = 'YUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM1pwWlhSalkyeHZkV1IwZGk5eVpYQnZjMmwwYjNKNUxuWnBaWFJqWTJ4dmRXUXZiV0Z6ZEdWeUwwMTVSbTlzWkdWeUwzUjFkRzl5YVdGc2JHbHVhM011YlROMQ=='.decode('base64').decode('base64')
thongbaomoi = 'YUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM1pwWlhSalkyeHZkV1IwZGk5eVpYQnZjMmwwYjNKNUxuWnBaWFJqWTJ4dmRXUXZiV0Z6ZEdWeUwwMTVSbTlzWkdWeUwzUm9iMjVuWW1GdmJXOXBMblI0ZEE9PQ=='.decode('base64').decode('base64')
vietradio = 'YUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM1pwWlhSalkyeHZkV1IwZGk5eVpYQnZjMmwwYjNKNUxuWnBaWFJqWTJ4dmRXUXZiV0Z6ZEdWeUwwMTVSbTlzWkdWeUwzWnBaWFJ5WVdScGJ5NXRNM1U9'.decode('base64').decode('base64')
haingoaitv = 'YUhSMGNITTZMeTl5WVhjdVoybDBhSFZpZFhObGNtTnZiblJsYm5RdVkyOXRMM1pwWlhSalkyeHZkV1IwZGk5eVpYQnZjMmwwYjNKNUxuWnBaWFJqWTJ4dmRXUXZiV0Z6ZEdWeUwwMTVSbTlzWkdWeUwyaGhhVzVuYjJGcGRIWXViVE4x'.decode('base64').decode('base64')
public_uploads = 'plugin://plugin.program.chrome.launcher/?kiosk=no&mode=showSite&stopPlayback=no&url=https%3a%2f%2fscript.google.com%2fmacros%2fs%2fAKfycbxwkVU0o3lckrB5oCQBnQlZ-n8CMx5CZ_ajq6Y3o7YHSTFbcODk%2fexec'
    
def addDir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if 'plugin.program.chrome.launcher' in url:
		u = url
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def addLink(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true')
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)

params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)

elif mode == 2:
	m3u_online()

elif mode == 3:
	text_online()

elif mode == 4:
	thongbao()

elif mode == 20:
	vietmedia_list()

elif mode == 21:
	vietmedia_playlist(url)

elif mode == 22:
	vietmedia_playlist_index(url)

elif mode == 23:
	next_page(url)

elif mode == 27:
	tutorial_links()

elif mode == 30:
	vietnam_group()

elif mode == 31:
	viet_tv_group()

elif mode == 40:
	channelTester()

elif mode == 41:
	localTester()

elif mode == 42:
	onlineTester()

elif mode == 48:
	vietnam_abc_order()

elif mode == 50:
	vietnam(name)

elif mode == 51:
	top10()

elif mode == 52:
	sports()

elif mode == 53:
	news()

elif mode == 54:
	documentary()

elif mode == 55:
	entertainment()

elif mode == 56:
	family()

elif mode == 57:
	movie()

elif mode == 58:
	music()

elif mode == 59:
	ondemandmovies()

elif mode == 65:
	ondemandshows()

elif mode == 60:
	twentyfour7()

elif mode == 61:
	radio()

elif mode == 62:
	english()

elif mode == 63:
	lifestyle()

elif mode == 64:
	international()

elif mode == 70:
	vietnam_category()

elif mode == 71:
	viet_Documentary()

elif mode == 72:
	viet_Entertainment()

elif mode == 73:
	viet_Family()

elif mode == 74:
	viet_Movie_Channels()

elif mode == 75:
	viet_Music()

elif mode == 76:
	viet_News()

elif mode == 77:
	viet_OnDemandMovies()

elif mode == 78:
	viet_OnDemandShows()

elif mode == 79:
	viet_Radio()

elif mode == 80:
	viet_RandomAirTime()

elif mode == 81:
	viet_Special_Events()

elif mode == 82:
	viet_Sports()

elif mode == 83:
	viet_Tutorials()

elif mode == 97:
	guide()

elif mode == 98:
	adult()

elif mode == 99:
	search()

xbmcplugin.endOfDirectory(plugin_handle)