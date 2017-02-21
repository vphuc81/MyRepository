# -*- coding: utf-8 -*-


import xbmc,xbmcaddon,xbmcgui,xbmcplugin
from md_request import open_url
from md_view import setView
from common import Addon
from md_tools import md
import re,sys,urllib


#PubFilm Add-on Created By Mucky Duck (1/2016)


addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon = Addon(addon_id, sys.argv)
addon_name = addon.get_name()
addon_path = addon.get_path()
md = md(addon_id, sys.argv)

metaset = addon.get_setting('enable_meta')
show_tv = addon.get_setting('enable_shows')
show_mov = addon.get_setting('enable_movies')
show_fav = addon.get_setting('enable_favs')
show_add_set = addon.get_setting('add_set')
show_meta_set = addon.get_setting('enable_meta_set')

art = md.get_art()
icon = addon.get_icon()
fanart = addon.get_fanart()


baseurl = addon.get_setting('base_url')
#baseurl = 'http://tv.pubfilmhd.com/'


reload(sys)
sys.setdefaultencoding("utf-8")



def MAIN():

	md.addDir({'mode':'search','name':'[COLOR white][B]SEARCH[/B][/COLOR]', 'url':'url'})
	if show_mov == 'true':
		md.addDir({'mode':'1','name':'[COLOR white][B]MOVIES[/B][/COLOR]', 'url':'%s/tag/movies' %baseurl, 'content':content})
	if show_tv == 'true':
		md.addDir({'mode':'1','name':'[COLOR white][B]SERIES[/B][/COLOR]', 'url':'%s/tag/series' %baseurl, 'content':content})
	md.addDir({'mode':'3','name':'[COLOR white][B]GENRE[/B][/COLOR]', 'url':'GENRE'})
	md.addDir({'mode':'3','name':'[COLOR white][B]YEARS[/B][/COLOR]', 'url':'YEARS'})
	md.addDir({'mode':'1','name':'[COLOR white][B]NEWLY ADDED[/B][/COLOR]', 'url':'%s/tag/new-added' %baseurl})
	md.addDir({'mode':'1','name':'[COLOR white][B]RECOMMENDED[/B][/COLOR]', 'url':'%s/category/recommended' %baseurl, 'content':content})
	md.addDir({'mode':'1','name':'[COLOR white][B]MOST WATCHED[/B][/COLOR]', 'url':'%s/category/most-watched' %baseurl, 'content':content})
	if show_fav == 'true':
		md.addDir({'mode': 'fetch_favs', 'name':'[COLOR white][B]MY FAVOURITES[/B][/COLOR]', 'url':'url'})
	if metaset == 'true':
		if show_meta_set == 'true':
			md.addDir({'mode':'meta_settings', 'name':'[COLOR white][B]META SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False)
	if show_add_set == 'true':
		md.addDir({'mode':'addon_settings', 'name':'[COLOR white][B]ADDON SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False)

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def INDEX(url,content):

	link = open_url(url).content
	all_videos = md.regex_get_all(link, '"recent-item">', '"post-meta">')
	items = len(all_videos)
	for a in all_videos:

		name = md.regex_from_to(a, '<h3 class="post-box-title"><a href=".+?" rel="bookmark">', '</a>').replace(' &#8211; Full (HD)','').replace('Seaosn','Season')
		name = addon.unescape(name)
		qualep = md.regex_from_to(a, '"f_tag">', '<').strip()
		url = md.regex_from_to(a, 'href="', '"')
		thumb = md.regex_from_to(a, 'src="', '"')
		fan_art = {'icon':thumb}

		if '/' in qualep or 'Season ' in name:
			content = 'tvshows'
			qualep = qualep.replace('/',' of ')
				
			season = ''
			try:
				splitName = name.partition(':')
				if len(splitName) > 0:
					name = splitName[0].strip()
					name = name[:-5].strip()
					season = splitName[2]
					
			except:
				pass

			md.addDir({'mode':'2', 'name':'[B][COLOR white]%s[/COLOR] [COLOR red][I](%s Episodes %s)[/I][/COLOR][/B]' %(name,season,qualep), 'url':url,
				   'title':name, 'iconimage':thumb, 'content':'tvshows', 'season':season},
				  {'sorttitle':name, 'season':season}, fan_art, item_count=items)
		else:
			content = 'movies'
			year = name[-4:]
			year = year.replace(' ','')
			name = name[:-4].strip()

			md.addDir({'mode':'4', 'name':'[B][COLOR white]%s[/COLOR] [COLOR red][I](%s-%s)[/I][/COLOR][/B]' %(name,year,qualep), 'url':url, 'iconimage':thumb,
				   'content':'movies'}, {'sorttitle':name, 'year':year}, fan_art, is_folder=False, item_count=items)
	       
	try:
		nextp = re.compile('<a href="(.*?)" >\&raquo;</a>').findall(link)[0] 
		md.addDir({'mode':'1', 'name':'[COLOR red][B][I]>>Next Page>>>[/I][/B][/COLOR]', 'url':nextp})
	except: pass

	if content == 'movies':
		setView(addon_id, 'movies', 'movie-view')
	elif content == 'tvshows':
		setView(addon_id, 'tvshows', 'show-view')

	addon.end_of_directory()




def EPS(title, url, iconimage, content, season):
	link = open_url(url).content
	match = re.compile('<a href="([^"]+)"target="EZWebPlayer" class="abutton orange medium">(.*?)</a>').findall(link) 
	items = len(match)
	fan_art = {'icon':iconimage}
	for url,name in match:
                name = re.sub('\D', '', name)
		md.addDir({'mode':'4', 'name':'[B][COLOR white]Episode [/COLOR][/B][B][COLOR red]%s[/COLOR][/B]' %name,
                           'url':url, 'iconimage':iconimage, 'content':'episodes'},
                          {'sorttitle':title, 'season':season, 'episode':name},
                          fan_art, is_folder=False, item_count=items)

	setView(addon_id,'episodes', 'epi-view')
	addon.end_of_directory()




def GENRE(url):

	link = open_url(baseurl).content
	all_links = md.regex_get_all(link, '>%s<' %url, '</ul>')
	all_videos = md.regex_get_all(str(all_links), '<li', '</li')
	items = len(all_videos)

	for a in all_videos:

		name = md.regex_from_to(a, 'href=.*?>', '<')
		url = md.regex_from_to(a, 'href="', '"')

		if baseurl not in url:
                        url = baseurl + url

		md.addDir({'mode':'1','name':'[COLOR red][B][I]%s[/I][/B][/COLOR]' %name, 'url':url})

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def SEARCH(content, query):
	try:
		if query:
			search = query.replace(' ', '%20')
		else:
			search = md.search('%20')
			if search == '':
				md.notification('[COLOR gold][B]EMPTY QUERY[/B][/COLOR],Aborting search',icon)
				return
			else:
				pass

		url = '%s//search/%s' %(baseurl,search)
		INDEX(url,content)

	except:
		md.notification('[COLOR gold][B]Sorry No Results[/B][/COLOR]',icon)




def RESOLVE(url,name,content,fan_art,infolabels):

	if content == 'movies':
		link = open_url(url).content
		requestURL = re.findall(r'<a href="([^"]+)"target="EZWebPlayer" class="abutton orange medium">SERVER 1</a>', str(link), re.I|re.DOTALL)[0]
	else:
                requestURL = url

        host = baseurl.split('//')[1].split('/')[0] 
	headers = {'Host': 'player.%s' %host, 'Referer': url, 'User-Agent': md.User_Agent()}
	
	link2 = open_url(requestURL, headers=headers).content

	data = re.findall(r'sources:\[(.*?)\]', str(link2), re.I|re.DOTALL)[0].replace(' ','')

	value = []
	max_url = []
	final_url= ''

	match = re.findall(r'file":"(.*?)"', str(data), re.I|re.DOTALL)
	match2 = re.findall(r'label":"(.*?)"', str(data), re.I|re.DOTALL)

	for url in match:
		max_url.append(url)

	for label in match2:
		value.append(int(re.sub('\D', '', label)))

	try:
                final_url =  max_url[md.get_max_value_index(value)[0]]
        except:
                final_url = match[0]

	md.resolved(final_url, name, fan_art, infolabels)
	addon.end_of_directory()




mode = md.args['mode']
url = md.args.get('url', None)
name = md.args.get('name', None)
query = md.args.get('query', None)
title = md.args.get('title', None)
year = md.args.get('year', None)
season = md.args.get('season', None)
episode = md.args.get('episode' ,None)
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
	EPS(title, url,iconimage,content,season)

elif mode == '3':
	GENRE(url)

elif mode == '4':
	RESOLVE(url,name,content,fan_art,infolabels)

elif mode == 'search':
	SEARCH(content, query)

elif mode == 'addon_search':
	md.addon_search(content,query,fan_art,infolabels)

elif mode == 'add_remove_fav':
	md.add_remove_fav(name,url,infolabels,fan_art,
			  content,mode_id,is_folder)
elif mode == 'fetch_favs':
	md.fetch_favs(baseurl)

elif mode == 'addon_settings':
	addon.show_settings()

elif mode == 'meta_settings':
	import metahandler
	metahandler.display_settings()

md.check_source()
addon.end_of_directory()
