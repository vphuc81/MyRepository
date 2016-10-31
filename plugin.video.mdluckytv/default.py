import xbmc,xbmcaddon,xbmcgui,xbmcplugin,xbmcvfs
import os,re,requests,shutil,sys,urllib
from addon.common.addon import Addon
from metahandler import metahandlers


#LUCKY-TV Add-on Created By Mucky Duck (8/2016)


User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mdluckytv'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon = Addon(addon_id, sys.argv)
addon_name = selfAddon.getAddonInfo('name')
dialog = xbmcgui.Dialog()
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData()
email = selfAddon.getSetting('email')
password = selfAddon.getSetting('pass')
baseurl = 'http://lucktv.net'




with requests.Session() as s:
        url = baseurl + '/login.php'
        r = requests.get(url).content
        form_data = {}
        login_details = re.findall(r'<form class="right-form shadow" data-validate="parsley" id="subscriptionsRegistrationaffForm" method="post" action="(.*?)" .*?><input type="hidden" name="(.*?)" value="(.*?)"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)
        for login_url,  method, method_type, token, token_id in login_details:
                login_url = baseurl + '/' + login_url
                form_data.update({method:method_type,token:token_id})
        email_id = re.findall(r'<input name="UserUsername".*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
        password_id = re.findall(r'<input type="password".*?id="(.*?)">', str(r), re.I|re.DOTALL)[0]
        token_hash = re.findall(r'</tbody></table>.*?<div style="display:none;"><input type="hidden" name="(.*?)" value="(.*?)" id=".*?">', str(r), re.I|re.DOTALL)
        for token_fields, token_fields_id in token_hash:
                form_data.update({email_id:email,password_id:password,token_fields:token_fields_id})
        login = s.post(login_url,data=form_data)




def CAT():
        addDir('[B][COLOR white]Latest Updates[/COLOR][/B]',baseurl+'/Latest-Updates-TV-Series.htm',1,art+'lt1.png',fanart,'')
        addDir('[B][COLOR white]Search Series[/COLOR][/B]','url',7,art+'lt2.png',fanart,'')
        addDir('[B][COLOR white]New Series[/COLOR][/B]',baseurl,5,art+'lt3.png',fanart,'')
        addDir('[B][COLOR white]Hot Series[/COLOR][/B]',baseurl+'/Hot-TV-Series.htm',1,art+'lt4.png',fanart,'')
        addDir('[B][COLOR white]All Series[/COLOR][/B]',baseurl+'/All-TV-Series.htm',6,art+'lt5.png',fanart,'')
        addDir('[B][COLOR white]Genres[/COLOR][/B]',baseurl,4,art+'lt6.png',fanart,'')
        setView('files', 'menu-view')




def INDEX(url):
        link = OPEN_URL(url)
        match = re.compile('<div><a href="(.*?)"><img src="(.*?)" .*?/></a></div>.*?<br><a title=" Watch (.*?) Free " href=.*?>',re.DOTALL).findall(link)
        items = len(match)
        for url, thumb, name in match:
                thumb = thumb.strip().replace(' ','%20')
                if not baseurl in url:
                        url = baseurl + url
                if metaset=='true':
                        addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,items,'',name)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,fanart,'')
                        
        try:
                np = re.compile('<div  class="fy-right"><a href="(.*?)">Next>></a></div></div>').findall(link)[0]
                if not baseurl in np:
                        np = baseurl + np
                addDir('[I][B][COLOR red]Go To Next Page>>>[/COLOR][/B][/I]',np,1,art+'lt7.png',fanart,'')
        except:pass
        setView('tvshows', 'show-view')




def SEA(url,iconimage,show_title):
        link = OPEN_URL(url)
        match = re.compile('onclick="selecttab\(\'(.*?)\'\)"').findall(link)
        items = len(match)
        for name in match:
                if metaset=='true':
                        addDir2('[B][COLOR red]Season: [/COLOR][COLOR white]%s[/COLOR][/B]' %name,url,3,iconimage,items,'',show_title)
                else:
                        addDir('[B][COLOR red]Season: [/COLOR][COLOR white]%s[/COLOR][/B]' %name,url,3,iconimage,fanart,'')
        setView('files', 'menu-view')




def EP(name,url,iconimage,show_title):
        if selfAddon.getSetting('email') == '':
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
                reg_url = baseurl + '/reg.php'
                r = requests.get(reg_url).content
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
                if dialog.yesno("[B]%s[/B]" %addon_name, line1, yeslabel="Proceed", nolabel="Exit"):
                        if dialog.yesno("[B]%s[/B]" %addon_name, line2, yeslabel="Register", nolabel="Login"):
                                keyboard = xbmc.Keyboard("", line4)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        user_input = keyboard.getText()
                                form_data.update({user_id:user_input})
                        
                                keyboard = xbmc.Keyboard("", line5)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        email_input = keyboard.getText()
                                form_data.update({email_id:email_input})
        
                                keyboard = xbmc.Keyboard("", line6)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        pwd_input = keyboard.getText()
                                form_data.update({password_id:pwd_input})

                                keyboard = xbmc.Keyboard("", line7)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        pwd2_input = keyboard.getText()
                                form_data.update({password2_id:pwd2_input})

                                headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                                           'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.8', 'Cache-Control':'max-age=0',
                                           'Connection':'keep-alive', 'Content-Length':'244', 'Content-Type':'application/x-www-form-urlencoded',
                                           'Origin':baseurl, 'Referer':reg_url, 'Upgrade-Insecure-Requests':'1', 'User-Agent':User_Agent}
                                register = s.post(login_url,data=form_data,headers=headers).content
                                try:
                                        try:
                                                success = re.findall(r"<a href='msglist.php'>(.*?)</a>", str(register), re.I|re.DOTALL)[0]
                                                if 'Welcome' in success:
                                                        selfAddon.setSetting('email',user_input)
                                                        selfAddon.setSetting('pass',pwd_input)
                                                        dialog.ok(addon_name, line8)
                
                                        except:
                                                user_fail = re.findall(r'<script language="javascript">(.*?)</script>', str(register), re.I|re.DOTALL)[0]
                                                if 'Username is already in use' in user_fail:
                                                        dialog.ok(addon_name, line9)
                                                        EP(name,url,iconimage,show_title)
                                except:
                                        dialog.ok(addon_name, line10)
                                        EP(name,url,iconimage,show_title)
                        else:
                                keyboard = xbmc.Keyboard("", line5)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        email_input = keyboard.getText()
                                selfAddon.setSetting('email',email_input)
        
                                keyboard = xbmc.Keyboard("", line6)
                                keyboard.doModal()
                                if keyboard.isConfirmed():
                                        pwd_input = keyboard.getText() 
                                selfAddon.setSetting('pass',pwd_input)
                        
        sn = name.replace('[COLOR white]','').replace('[/COLOR][/B]','').replace('[B][COLOR red]Season: [/COLOR]','')
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '<ul id="sge%s"' % sn, '</ul>')[0]
        match=re.compile('<a href="(.*?)"><img src=".*?" .*?/>&nbsp;(.*?)  (.*?)</a>').findall(str(all_links))
        items = len(match)
        for url, sea_epi, name in match:
                if not baseurl in url:
                        url = baseurl + url
                if metaset=='true':
                        addDir3('[B][COLOR red]%s[/COLOR] [COLOR white]%s[/COLOR][/B]' %(sea_epi,name),url,8,iconimage,items,'',show_title,sea_epi)
                else:
                        addDir('[B][COLOR red]%s[/COLOR] [COLOR white]%s[/COLOR][/B]' %(sea_epi,name),url,8,iconimage,fanart,'')
        setView('episodes', 'epi-view')




def GENRE(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '>TV Genres<', '</ul>')[0]
        match=re.compile('<a href="(.*?)">(.*?)</a>').findall(str(all_links))
        for url, name in match:
                if not baseurl in url:
                        url = baseurl + url
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,1,art+'lt6.png',fanart,'')
        setView('files', 'menu-view')




def NEW(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, '>New TV Series<', '</ul>')[0]
        match = re.compile('<a  title="Watch (.*?) Online" href="(.*?)"><img src="(.*?)" .*?/></a>').findall(str(all_links))
        items = len(match)
        for name, url, thumb in match:
                thumb = thumb.strip().replace(' ','%20')
                if not baseurl in url:
                        url = baseurl + url
                if metaset=='true':
                        addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,items,'',name)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,fanart,'')
        setView('tvshows', 'show-view')




def ALL(url):
        link = OPEN_URL(url)
        all_links = regex_get_all(link, 'right-title">All TV Series<', '</font></div>')[0]
        match = re.compile('<a href="(.*?)">(.*?)</a>').findall(str(all_links))
        for url, name in match:
                name = name.replace('&nbsp;','').replace('#','0/9')
                if not baseurl in url:
                        url = baseurl + url
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,1,art+'lt5.png',fanart,'')
        setView('files', 'menu-view')




def SEARCH():
        keyb = xbmc.Keyboard('', 'SEARCH ' + addon_name)
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                request_url = baseurl + '/searchlist.php'
                form_data={'q':search}
                headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                           'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.8',
                           'Cache-Control':'max-age=0', 'Connection':'keep-alive', 'Content-Length':'12',
                           'Content-Type':'application/x-www-form-urlencoded', 'Origin':baseurl,
                           'Referer':baseurl, 'User-Agent':User_Agent}
                link = requests.post(request_url, data=form_data, headers=headers).text
                match = re.compile('<div><a href="(.*?)"><img src="(.*?)" .*?/></a></div>.*?<br><a title=" Watch (.*?) Free " href=.*?>',re.DOTALL).findall(link)
                items = len(match)
                for url, thumb, name in match:
                        if not baseurl in url:
                                url = baseurl + url
                        if metaset=='true':
                                addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,items,'',name)
                        else:
                                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,2,thumb,fanart,'')
        setView('tvshows', 'show-view')




def RESOLVE(name,url,iconimage):
        referer = url
        headers = {'User-Agent':User_Agent}
        link = OPEN_URL(url)
        addon.log(link)
        url = re.findall(r'url: "(.*?)"', str(link), re.I|re.DOTALL)[0]
        host =  url.replace('http://','').replace('https://','').partition('/')[0]
        headers = {'Accept':'*/*', 'Accept-Encoding':'gzip, deflate, sdch', 'Accept-Language':'en-US,en;q=0.8',
                   'Connection':'keep-alive', 'Host':host, 'Referer':referer, 'User-Agent': User_Agent,
                   'X-Requested-With':'ShockwaveFlash/22.0.0.209'}
        url = url.replace('|','%7C')
        url = url + '|' + urllib.urlencode(headers)
        liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo(type='Video', infoLabels={"Title":name,"Plot":description})
        liz.setProperty("IsPlayable","true")
        liz.setPath(url)
        xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)




def regex_from_to(text, from_string, to_string, excluding=True):
        if excluding:
                try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
                except: r = ''
        else:
                try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
                except: r = ''
        return r




def regex_get_all(text, start_with, end_with):
        r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
        return r




def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addDir(name,url,mode,iconimage,fanart,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title":name,"Plot":description})
        liz.setProperty('fanart_image', fanart)
        if mode==8:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def addDir2(name,url,mode,iconimage,itemcount,description,show_title):
        meta = metaget.get_meta('tvshow',show_title)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        meta['title'] = name
        contextMenuItems = []
        contextMenuItems.append(('TV Show Info', 'XBMC.Action(Info)'))
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&show_title="+urllib.quote_plus(show_title)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '':
                liz.setProperty('fanart_image', meta['backdrop_url'])
        else:
                liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=itemcount)
        return ok




def addDir3(name,url,mode,iconimage,itemcount,description,show_title,sea_epi):
        sea = re.split(r"x", str(sea_epi), re.I)[0]
        epi = re.split(r"x", str(sea_epi), re.I)[1]
        meta = metaget.get_episode_meta(show_title,'',sea,epi)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        meta['title'] = name
        contextMenuItems = []
        contextMenuItems.append(('Episode Info', 'XBMC.Action(Info)'))
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&show_title="+urllib.quote_plus(show_title)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '':
                liz.setProperty('fanart_image', meta['backdrop_url'])
        else:
                liz.setProperty('fanart_image', fanart)
        if mode==8:
                liz.setProperty("IsPlayable","true")
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=itemcount)
        else:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True,totalItems=itemcount)
        return ok
        



def addLink(name,url,mode,iconimage,fanart,description=''):
        #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        #ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok




def OPEN_URL(url):
        headers = {}
        headers['User-Agent'] = User_Agent
        link = s.get(url, headers=headers).text
        link = link.encode('ascii', 'ignore').decode('ascii')
        return link





def setView(content, viewType):
    ''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '504'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '503'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '515'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '508'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '501'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '51'
        elif addon.get_setting(viewType) == 'Low List':
            VT = '724'
        elif addon.get_setting(viewType) == 'List':
            VT = '50'
        elif addon.get_setting(viewType) == 'Thumbnail':
            VT = '500'
        elif addon.get_setting(viewType) == 'Default Menu View':
            VT = addon.get_setting('default-view1')
        elif addon.get_setting(viewType) == 'Default TV Shows View':
            VT = addon.get_setting('default-view2')
        elif addon.get_setting(viewType) == 'Default Episodes View':
            VT = addon.get_setting('default-view3')

        print viewType
        print VT
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )




params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None
show_title=None




try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:
        description=urllib.unquote_plus(params["description"])
except:
        pass

try:
        show_title=urllib.unquote_plus(params["show_title"])
except:
        pass

try:
        show_title=urllib.unquote_plus(params["sea_epi"])
except:
        pass




if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==2:
        SEA(url,iconimage,show_title)

elif mode==3:
        EP(name,url,iconimage,show_title)

elif mode==4:
        GENRE(url)

elif mode==5:
        NEW(url)

elif mode==6:
        ALL(url)

elif mode==7:
        SEARCH()

elif mode==8:
        RESOLVE(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))









































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































'''if xbmcvfs.exists(xbmc.translatePath('special://home/userdata/sources.xml')):
        with open(xbmc.translatePath('special://home/userdata/sources.xml'), 'r+') as f:
                my_file = f.read()
                if re.search(r'http://muckys.mediaportal4kodi.ml', my_file):
                        addon.log('===Muckys===Source===Found===in===sources.xml===Not Deleting.===')
                else:
                        line1 = "you have Installed The MDrepo From An"
                        line2 = "Unofficial Source And Will Now Delete Please"
                        line3 = "Install From [COLOR red]http://muckys.mediaportal4kodi.ml[/COLOR]"
                        line4 = "Removed Repo And Addon"
                        line5 = "successfully"
                        dialog.ok(addon_name, line1, line2, line3)
                        delete_addon = xbmc.translatePath('special://home/addons/'+addon_id)
                        delete_repo = xbmc.translatePath('special://home/addons/repository.mdrepo')
                        shutil.rmtree(delete_addon, ignore_errors=True)
                        shutil.rmtree(delete_repo, ignore_errors=True)
                        addon.log('===DELETING===ADDON===+===REPO===')
                        dialog.ok(addon_name, line4, line5)'''





















































































































































































































































































































































































































































































































































































































































































































































































































































































































































