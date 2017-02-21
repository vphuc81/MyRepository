# -*- coding: utf-8 -*-


import xbmc,xbmcaddon,xbmcgui,xbmcplugin
from md_request import open_url
from md_view import setView
from common import Addon
from md_tools import md
import re,sys,urllib


### LUCKY-TV Add-on Created By Mucky Duck (8/2016) ###
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

art = md.get_art()
icon = addon.get_icon()
fanart = addon.get_fanart()

email = addon.get_setting('email')
password = addon.get_setting('pass')
baseurl = addon.get_setting('base_url')

reload(sys)
sys.setdefaultencoding("utf-8")




def CAT():
	
	md.addDir({'mode':'1', 'name':'[B][COLOR white]Latest Updates[/COLOR][/B]', 'url':baseurl+'/Latest-Updates-TV-Series.htm'}, fan_art={'icon':art+'lt1.png'})
	md.addDir({'mode':'search', 'name':'[B][COLOR white]Search Series[/COLOR][/B]', 'url':'url'}, fan_art={'icon':art+'lt2.png'})
	md.addDir({'mode':'5', 'name':'[B][COLOR white]New Series[/COLOR][/B]', 'url':baseurl}, fan_art={'icon':art+'lt3.png'})
	md.addDir({'mode':'1', 'name':'[B][COLOR white]Hot Series[/COLOR][/B]', 'url':baseurl+'/Hot-TV-Series.htm'}, fan_art={'icon':art+'lt4.png'})
	md.addDir({'mode':'6', 'name':'[B][COLOR white]All Series[/COLOR][/B]', 'url':baseurl+'/All-TV-Series.htm'}, fan_art={'icon':art+'lt5.png'})
	md.addDir({'mode':'4', 'name':'[B][COLOR white]Genres[/COLOR][/B]', 'url':baseurl}, fan_art={'icon':art+'lt6.png'})
	if show_fav == 'true':
		md.addDir({'mode': 'fetch_favs', 'name':'[COLOR white][B]MY FAVOURITES[/B][/COLOR]', 'url':'url'})
	if metaset == 'true':
		if show_meta_set == 'true':
			md.addDir({'mode':'meta_settings', 'name':'[COLOR white][B]META SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False, is_playable=False)
	if show_add_set == 'true':
		md.addDir({'mode':'addon_settings', 'name':'[COLOR white][B]ADDON SETTINGS[/B][/COLOR]', 'url':'url'}, is_folder=False, is_playable=False)
	
	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def INDEX(url):

	content = 'tvshows'
	link = open_url(url).content
	match = re.compile('<div><a href="(.*?)"><img src="(.*?)" .*?/></a></div>.*?<br><a title=" Watch (.*?) Free " href=.*?>',re.DOTALL).findall(link)
	items = len(match)

	for url, thumb, name in match:
		thumb = thumb.strip().replace(' ','%20')
		if not baseurl in url:
			url = baseurl + url

		md.addDir({'mode':'2', 'name':'[B][COLOR white]%s[/COLOR][/B]' %name, 'url':url, 'iconimage':thumb,
			   'content':content, 'title':name}, {'sorttitle':name}, fan_art={'icon':thumb}, item_count=items)

	try:
		np = re.compile('<div  class="fy-right"><a href="(.*?)">Next>></a></div></div>').findall(link)[0]
		if not baseurl in np:
			np = baseurl + np
		md.addDir({'mode':'1', 'name':'[I][B][COLOR red]>>Go To Next Page>>>[/COLOR][/B][/I]', 'url':np}, fan_art={'icon':art+'lt7.png'})
	except:pass

	setView(addon_id, 'tvshows', 'show-view')
	addon.end_of_directory()




def SEA(title,url,iconimage,content):

	link = open_url(url).content
	match = re.compile('onclick="selecttab\(\'(.*?)\'\)"').findall(link)
	items = len(match)

	for name in match:
		md.addDir({'mode':'3', 'name':'[B][COLOR red]Season: [/COLOR][COLOR white]%s[/COLOR][/B]' %name, 'url':url,
			   'iconimage':iconimage, 'content':content, 'title':title, 'season':name},
			  {'sorttitle':title}, fan_art={'icon':iconimage}, item_count=items)

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def EP(title,url,iconimage,content,season):

	link = open_url(url).content
	all_links = md.regex_get_all(link, '<ul id="sge%s"' %season, '</ul>')[0]
	match = re.compile('<a href="(.*?)"><img src=".*?" .*?/>&nbsp;(.*?)  (.*?)</a>').findall(str(all_links))
	items = len(match)

	for url, sea_epi, name in match:
		season = re.split(r"x", str(sea_epi), re.I)[0]
		episode = re.split(r"x", str(sea_epi), re.I)[1]
		if not baseurl in url:
			url = baseurl + url

		if addon.get_setting('email') == '':
			login_reg()

		md.addDir({'mode': '7', 'name':'[B][COLOR red]%s[/COLOR] [COLOR white]%s[/COLOR][/B]' %(sea_epi,name),
			   'url':url, 'iconimage':iconimage, 'content':'episodes'},
			  {'sorttitle':title, 'season':season, 'episode':episode},
			  fan_art={'icon':iconimage}, is_folder=False, item_count=items)

	setView(addon_id,'episodes', 'epi-view')
	addon.end_of_directory()




def GENRE(url):

	link = open_url(url).content
	all_links = md.regex_get_all(link, '>TV Genres<', '</ul>')[0]
	match=re.compile('<a href="(.*?)">(.*?)</a>').findall(str(all_links))
	for url, name in match:
		if not baseurl in url:
			url = baseurl + url
		md.addDir({'mode':'1', 'name':'[B][COLOR white]%s[/COLOR][/B]' %name, 'url':url}, fan_art={'icon':art+'lt6.png'})

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def NEW(url):
	link = open_url(url).content
	all_links = md.regex_get_all(link, '>New TV Series<', '</ul>')[0]
	match = re.compile('<a  title="Watch (.*?) Online" href="(.*?)"><img src="(.*?)" .*?/></a>').findall(str(all_links))
	items = len(match)
	for name, url, thumb in match:
		thumb = thumb.strip().replace(' ','%20')
		if not baseurl in url:
			url = baseurl + url
		md.addDir({'mode':'2', 'name':'[B][COLOR white]%s[/COLOR][/B]' %name, 'url':url, 'iconimage':thumb,
			   'content':content, 'title':name}, {'sorttitle':name}, fan_art={'icon':thumb}, item_count=items)

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def ALL(url):
	link = open_url(url).content
	all_links = md.regex_get_all(link, 'right-title">All TV Series<', '</font></div>')[0]
	match = re.compile('<a href="(.*?)">(.*?)</a>').findall(str(all_links))
	for url, name in match:
		name = name.replace('&nbsp;','').replace('#','0/9')
		if not baseurl in url:
			url = baseurl + url
		md.addDir({'mode':'1', 'name':'[B][COLOR white]%s[/COLOR][/B]' %name, 'url':url}, fan_art={'icon':art+'lt5.png'})

	setView(addon_id, 'files', 'menu-view')
	addon.end_of_directory()




def SEARCH(content, query):
        try:
		if query:
			search = query
		else:
			search = md.search(' ')

			if search == '':
				md.notification('[COLOR gold][B]EMPTY QUERY[/B][/COLOR],Aborting search',icon)
				return
			else:
				pass

		request_url = baseurl + '/searchlist.php'
		form_data={'q':search}
		headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			   'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.8',
			   'Cache-Control':'max-age=0', 'Connection':'keep-alive', 'Content-Length':'12',
			   'Content-Type':'application/x-www-form-urlencoded', 'Origin':baseurl,
			   'Referer':baseurl, 'User-Agent':md.User_Agent()}

		link = open_url(request_url, 'post', data=form_data, headers=headers).content
		match = re.compile('<div><a href="(.*?)"><img src="(.*?)" .*?/></a></div>.*?<br><a title=" Watch (.*?) Free " href=.*?>',re.DOTALL).findall(link)
		items = len(match)

		for url, thumb, name in match:
			if not baseurl in url:
				url = baseurl + url

			md.addDir({'mode':'2', 'name':'[B][COLOR white]%s[/COLOR][/B]' %name, 'url':url, 'iconimage':thumb,
                                   'content':content, 'title':name}, {'sorttitle':name}, fan_art={'icon':thumb}, item_count=items)

	except:
		md.notification('[COLOR gold][B]Sorry No Results[/B][/COLOR],Aborting search',icon)

        setView(addon_id, 'tvshows', 'show-view')
	addon.end_of_directory()




def RESOLVE(url,name,content,fan_art,infolabels):
	
	login()
	referer = url
	link = open_url(url).content
	addon.log(link)
	url = re.findall(r'url: "(.*?)"', str(link), re.I|re.DOTALL)[0]
	host =  url.replace('http://','').replace('https://','').partition('/')[0]
	headers = {'Accept':'*/*', 'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'en-US,en;q=0.8',
		   'Connection':'keep-alive', 'Host':host, 'Referer':referer, 'User-Agent': md.User_Agent(),
		   'X-Requested-With':'ShockwaveFlash/22.0.0.209'}
	url = url.replace('|','%7C')
	url = url + '|' + urllib.urlencode(headers)

	md.resolved(url, name, fan_art, infolabels)
	addon.end_of_directory()




def login():

	url = '%s/login.php' %baseurl
	r = open_url(url).content
	form_data = {}

	login_details = re.findall(r'<form class="right-form shadow" data-validate="parsley" id="subscriptionsRegistrationaffForm" method="post" action="(.*?)" .*?><input type="hidden" name="(.*?)" value="(.*?)"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)
	for login_url,  method, method_type, token, token_id in login_details:
	    login_url = baseurl + '/' + login_url
	    form_data.update({method:method_type,token:token_id})

	email_id = re.findall(r'"UserUsername" .*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
	password_id = re.findall(r'"password" .*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
	    

	token_hash = re.findall(r'</tbody></table>.*?<div style="display:none;"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)
	for token_fields, token_fields_id in token_hash:
	    form_data.update({email_id:email,password_id:password,token_fields:token_fields_id})

	login = open_url(login_url,'post',data=form_data)
	



def login_reg():

	line1 = "[B]To stream episodes you need to register for a free account with [COLOR red]http://lucktv.net[/COLOR] You can login or register in the next few simple steps[/B]"
	line2 = "[B]If you already have an account select login below to enter your details otherwise select register to set up a new account[/B]"
	line3 = "[B][/B]"
	line4 = "[B]Please enter a username[/B]"
	line5 = "[B]Please enter your email[/B]"
	line6 = "[B]Please enter a password[/B]"
	line7 = "[B]Please confirm your password[/B]"
	line8 = "You have successfully registered an account with [COLOR red]http://lucktv.net[/COLOR] and are now able to view streams"
	line9 = "Sorry the username you chose is already in use please try again or visit [COLOR red]http://lucktv.net[/COLOR] to register an account then enter your details in settings"
	line10 = "Sorry something went wrong please try again or visit [COLOR red]http://lucktv.net[/COLOR] to register an account then enter your details in settings"

	reg_url = '%s/reg.php' %baseurl
	r = open_url(reg_url).content
	form_data = {}

	login_details = re.findall(r'<form class="right-form shadow" data-validate="parsley" id="subscriptionsRegistrationaffForm" method="post" action="(.*?)" .*?><input type="hidden" name="(.*?)" value="(.*?)"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)
	for login_url,  method, method_type, token, token_id in login_details:
		login_url = baseurl + '/' + login_url
		form_data.update({method:method_type,token:token_id})

	user_id = re.findall(r'<input name="UserUsername".*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
	email_id = re.findall(r'<input name="email".*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
	password_id = re.findall(r'<input type="password".*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
	password2_id = re.findall(r'<input type="password".*?id="(.*?)">', str(r), re.I|re.DOTALL)[1]
	token_hash = re.findall(r'</tbody></table>.*?<div style="display:none;"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)

	for token_fields, token_fields_id in token_hash:
		form_data.update({token_fields:token_fields_id})

	if md.dialog_yesno(line1, 'Proceed', 'Exit'):
		if md.dialog_yesno(line2, 'Register', 'Login'):

			user_input = md.text_return(line4)
			form_data.update({user_id:user_input})
		
			email_input = md.text_return(line5)
			form_data.update({email_id:email_input})

			pwd_input = md.text_return(line6)
			form_data.update({password_id:pwd_input})

			pwd2_input = md.text_return(line7)
			form_data.update({password2_id:pwd2_input})

			headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				   'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.8', 'Cache-Control':'max-age=0',
				   'Connection':'keep-alive', 'Content-Length':'244', 'Content-Type':'application/x-www-form-urlencoded',
				   'Origin':baseurl, 'Referer':reg_url, 'Upgrade-Insecure-Requests':'1', 'User-Agent':md.User_Agent()}

			register = open_url(login_url,'post',data=form_data,headers=headers).content
			try:
				try:
					success = re.findall(r"<a href='msglist.php'>(.*?)</a>", str(register), re.I|re.DOTALL)[0]
					if 'Welcome' in success:
						addon.set_setting('email',user_input)
						addon.set_setting('pass',pwd_input)
						addon.show_ok_dialog([line8])
						
	
				except:
					user_fail = re.findall(r'<script language="javascript">(.*?)</script>', str(register), re.I|re.DOTALL)[0]
					if 'Username is already in use' in user_fail:
						addon.show_ok_dialog([line9])
						md.Exit()
			except:
				addon.show_ok_dialog([line10])
				md.Exit()
		else:
			email_input = md.text_return(line5)
			addon.set_setting('email',email_input)

			pwd_input = md.text_return(line6) 
			addon.set_setting('pass',pwd_input)
	else:
		md.Exit()




mode = md.args['mode']
url = md.args.get('url', None)
name = md.args.get('name', None)
query = md.args.get('query', None)
title = md.args.get('title', None)
season = md.args.get('season', None)
episode = md.args.get('episode' ,None)
infolabels = md.args.get('infolabels', None)
content = md.args.get('content', None)
mode_id = md.args.get('mode_id', None)
iconimage = md.args.get('iconimage', None)
fan_art = md.args.get('fan_art', None)
is_folder = md.args.get('is_folder', True)




if mode is None or url is None or len(url)<1:
	CAT()

elif mode == '1':
	INDEX(url)

elif mode == '2':
	SEA(title, url, iconimage, content)

elif mode == '3':
	EP(title,url,iconimage,content,season)

elif mode == '4':
	GENRE(url)

elif mode == '5':
	NEW(url)

elif mode == '6':
	ALL(url)

elif mode == '7':
	RESOLVE(url,name,content,fan_art,infolabels)

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

