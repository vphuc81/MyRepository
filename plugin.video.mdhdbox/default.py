# -*- coding: utf-8 -*-


import xbmc,xbmcaddon,xbmcgui,xbmcplugin
from md_request import open_url
from md_view import setView
from common import Addon
from md_tools import md
import re,sys,urllib


### HD Box Add-on Created By Mucky Duck (3/2016) ###
# I spend a lot of time working on my addons
# it is NOT ok to clone my work and pass it
# off as your own to make yourself look good
# if this continues i will stop pushing updates


addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon = Addon(addon_id, sys.argv)
addon_name = addon.get_name()
addon_path = addon.get_path()
md = md(addon_id, sys.argv)

metaset = addon.get_setting('enable_meta')
show_fav = addon.get_setting('enable_favs')
show_add_set = addon.get_setting('add_set')
show_meta_set = addon.get_setting('enable_meta_set')
auto_play = addon.get_setting('autoplay')

art = md.get_art()
icon = addon.get_icon()
fanart = addon.get_fanart()


baseurl = addon.get_setting('base_url')


reload(sys)
sys.setdefaultencoding("utf-8")




def MAIN():
	md.addDir({'mode':'2', 'name':'[B][COLOR ivory]Year[/COLOR][/B]', 'url':'years'})
	md.addDir({'mode':'2', 'name':'[B][COLOR ivory]Genre[/COLOR][/B]', 'url':'Genres'})
	md.addDir({'mode':'search', 'name':'[B][COLOR ivory]Search[/COLOR][/B]', 'url':'url'})
	md.addDir({'mode':'1', 'name':'[B][COLOR ivory]Most Viewed[/COLOR][/B]', 'url':'%s/most_watched_movies' %baseurl})
	md.addDir({'mode':'1', 'name':'[B][COLOR ivory]Recent Movies[/COLOR][/B]', 'url':'%s/latest_movies' %baseurl})
	md.addDir({'mode':'1', 'name':'[B][COLOR ivory]Popular Movies[/COLOR][/B]', 'url':'%s/popular_movies' %baseurl})
	if show_fav == 'true':
		md.addDir({'mode': 'fetch_favs', 'name':'[COLOR white][B]MY FAVOURITES[/B][/COLOR]', 'url':'url'})
	if metaset == 'true':
		if show_meta_set == 'true':
			md.addDir({'mode':'meta_settings', 'name':'[COLOR white][B]META SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False, is_playable=False)
	if show_add_set == 'true':
		md.addDir({'mode':'addon_settings', 'name':'[COLOR white][B]ADDON SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False, is_playable=False)

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def INDEX(url, content):

	headers = {'User-Agent':md.User_Agent()}
	link = open_url(url, headers=headers, redirects=False)

	cookie = link.cookies.get_dict()
	headers['Cookie'] = 'ci_session=%s' %cookie['ci_session']
	link = open_url(url, headers=headers, redirects=False).content
	
	content = 'movies'
	all_videos = md.regex_get_all(link.replace('\n',''), 'cell_container', '</div></div>')
	items = len(all_videos)

	for a in all_videos:

		name = md.regex_from_to(a, 'a title="', '\(')
		name = addon.unescape(name)
		url = md.regex_from_to(a, 'href="', '"').replace("&amp;","&")
		year = md.regex_from_to(a, 'Year</b>:', '<').strip()
		qual = md.regex_from_to(a, 'Quality</b>:', '<')
		if baseurl not in url:
			url = baseurl + url
		thumb = md.regex_from_to(a, 'src="', '"')
		if not 'http://' in thumb:
			thumb = 'http://%s' %thumb
		fan_art = {'icon':thumb}

		md.addDir({'mode':'3', 'name':'[B][COLOR ivory]%s[/COLOR][COLOR red][I](%s%s)[/I][/COLOR][/B]' %(name,year,qual), 'url':url, 'iconimage':thumb, 'content':content},
			  {'sorttitle':name}, fan_art, is_folder=False, item_count=items)
	try:
		match = re.compile('<a href="(.*?)\?page\=(.*?)">').findall(link)
		for url, pn in match:
			url = baseurl+url+'?page='+pn
			md.addDir({'mode':'1', 'name':'[I][B][COLOR red]Page %s >>>[/COLOR][/B][/I]' %pn, 'url':url, 'content':content})
	except: pass

	setView(addon_id, 'movies', 'movie-view')
	addon.end_of_directory()




def GENRE(url):

	link = open_url(baseurl, redirects=False).content
	all_links = md.regex_get_all(link, '%s<' %url, '</ul>')
	all_videos = md.regex_get_all(str(all_links), '<li>', '</li>')

	for a in all_videos:
		name = md.regex_from_to(a, '<a href=.*?>', '</')

		url = md.regex_from_to(a, 'href="', '"')
		if not baseurl in url:
			url = baseurl + url

		md.addDir({'mode':'1', 'name':'[COLOR red][B][I]%s[/I][/B][/COLOR]' %name, 'url':url})

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def SEARCH(content, query):
	try:
		if query:
			search = query.replace(' ','+')
		else:
			search = md.search()
			if search == '':
				md.notification('[COLOR gold][B]EMPTY QUERY[/B][/COLOR],Aborting search',icon)
				return
			else:
				pass

		url = '%s/results?q=%s' %(baseurl,search)
		INDEX(url,content)

	except:
		md.notification('[COLOR gold][B]Sorry No Results[/B][/COLOR]',icon)




def RESOLVE(url,iconimage,content,infolabels):

	url = re.split(r'#', url, re.I)[0]
	request_url = '%s/video_info/iframe' %baseurl

	headers = {'User-Agent':md.User_Agent()}
	link = open_url(url, headers=headers, redirects=False)

	cookie = link.cookies.get_dict()
	
	form_data={'v': re.search(r'v\=(.*?)$',url,re.I).group(1)}
	headers = {'origin':baseurl, 'referer': url,
		   'user-agent':md.User_Agent(),'x-requested-with':'XMLHttpRequest'}
	headers['Cookie'] = 'ci_session=%s' %cookie['ci_session']

	final = open_url(request_url, 'post', data=form_data, headers=headers, redirects=False).json()
	

	res_quality = []
	stream_url = []
	quality = ''

	if auto_play == 'true':
		key = max(final.keys(), key=int)
		url = final[str(key)].split('=')[1]
		
	else:
		match = final

		for a, b in match.iteritems():

			quality = '[B][I][COLOR red]%s[/COLOR][/I][/B]' %a
			res_quality.append(quality)
			stream_url.append(b.split('=')[1])

		if len(match) >1:

			ret = md.dialog_select('Select Stream Quality',res_quality)
			if ret == -1:
				return
			elif ret > -1:
				url = stream_url[ret]
		else:
			key = max(final.keys(), key=int)
			url = final[str(key)].split('=')[1]

	url = urllib.unquote(url)
	md.resolved(url, name, iconimage, infolabels)
	addon.end_of_directory()




mode = md.args['mode']
url = md.args.get('url', None)
name = md.args.get('name', None)
query = md.args.get('query', None)
infolabels = md.args.get('infolabel', None)
content = md.args.get('content', None)
mode_id = md.args.get('mode_id', None)
iconimage = md.args.get('iconimage', None)
fan_art = md.args.get('fan_art', None)
is_folder = md.args.get('is_folder', True)




if mode is None or url is None or len(url)<1:
	MAIN()

elif mode == '1':
	INDEX(url,content)

elif mode == '2':
	GENRE(url)

elif mode == '3':
	RESOLVE(url,iconimage,content,infolabels)

elif mode == 'search':
	SEARCH(content,query)

elif mode == 'addon_search':
	md.addon_search(content,query,fan_art,infolabels)

elif mode == 'add_remove_fav':
	md.add_remove_fav(name, url, infolabels, fan_art,
			  content, mode_id, is_folder)
elif mode == 'fetch_favs':
	md.fetch_favs(baseurl)

elif mode == 'addon_settings':
	addon.show_settings()

elif mode == 'meta_settings':
	import metahandler
	metahandler.display_settings()

md.check_source()
addon.end_of_directory()
