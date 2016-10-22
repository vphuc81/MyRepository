import xbmc,xbmcaddon,xbmcgui,xbmcplugin,xbmcvfs
import os,re,requests,shutil,urllib
from addon.common.addon import Addon
from metahandler import metahandlers

#MOVIEPOOL Add-on Created By Mucky Duck (9/2016)

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
addon_id='plugin.video.mdmoviepool'
selfAddon = xbmcaddon.Addon(id=addon_id)
addon_name = selfAddon.getAddonInfo('name')
addon = Addon(addon_id, sys.argv)
art = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/art/'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
auto_play = addon.get_setting('autoplay')
def_quality = addon.get_setting('default_quality')
metaset = selfAddon.getSetting('enable_meta')
metaget = metahandlers.MetaData()
baseurl = 'http://moviepool.net'
s = requests.session()




def CAT():
        addDir('[B][COLOR white]Recommended Movies[/COLOR][/B]',baseurl+'/hd-streaming/category/featured?filtre=date',1,art+'recommended.png',fanart,'')
        addDir('[B][COLOR white]Recently Added[/COLOR][/B]',baseurl+'/?filtre=date&cat=0',1,art+'recent.png',fanart,'')
        addDir('[B][COLOR white]Most Viewed[/COLOR][/B]',baseurl+'/hd-streaming/category/featured?display=tube&filtre=views',1,art+'viewed.png',fanart,'')
        addDir('[B][COLOR white]Categories[/COLOR][/B]',baseurl+'/categories',3,art+'categories.png',fanart,'')
        addDir('[B][COLOR white]Actors[/COLOR][/B]',baseurl+'/tags',5,art+'actors.png',fanart,'')
        addDir('[B][COLOR white]Search[/COLOR][/B]','url',7,art+'search.png',fanart,'')
        setView('files', 'menu-view')




def INDEX(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, 'li class="border', '</li')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, '<span>', '</')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src="', '"')
                if metaset=='true':
                        addDir2('[B][COLOR white]%s[/COLOR][/B]' %name,url,9,thumb,items)
                else:
                        addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,9,thumb,fanart,'')
        try:
                np = re.compile('<li><a href="(.*?)">Next &rsaquo;</a></li>').findall(link)[0]
                np = np.replace('&#038;','&')
                addDir('[I][B][COLOR red]Go To Next Page>>>[/COLOR][/B][/I]',np,1,icon,fanart,'')
        except: pass
        try:
                np = re.compile("<li><a href='(.*?)' class=\"inactive\">(.*?)</a></li>").findall(link)
                for url,pn in np:
                        url = url.replace('&#038;','&')
                        addDir('[I][B][COLOR red]GoTo Page %s[/COLOR][/B][/I]' %pn,url,1,icon,fanart,'')
        except: pass
        setView('movies', 'movie-view')




def GENRE(url):
        link = OPEN_URL(url)
        all_videos = regex_get_all(link, 'li class="border', '</li')
        items = len(all_videos)
        for a in all_videos:
                name = regex_from_to(a, '<span>', '</')
                name = addon.unescape(name)
                name = name.encode('ascii', 'ignore').decode('ascii')
                url = regex_from_to(a, 'href="', '"')
                thumb = regex_from_to(a, 'src="', '"')
                quan = regex_from_to(a, 'radius-5">', '<')
                addDir('[B][COLOR white]%s[/COLOR] [COLOR red]|%s[/COLOR][/B]' %(name,quan),url,1,thumb,fanart,'')
        setView('files', 'menu-view')




def ACTORS(url):
        link = OPEN_URL(url)
        match=re.compile("<li><a href='(.*?)' class='.*?'>(.*?)</a></li>").findall(link)
        for url,name in match:
                addDir('[B][COLOR white]%s[/COLOR][/B]' %name,url,1,art+'actors.png',fanart,'')
        setView('files', 'menu-view')




def SEARCH():
        keyb = xbmc.Keyboard('', addon_name + ' SEARCH')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText().replace(' ','+')
                url = baseurl+'/?s='+search
                INDEX(url)




def RESOLVE(name,url,iconimage):
        link = OPEN_URL(url)
        RequestURL = re.findall(r'<iframe.*?src="(.*?)" .*?>', str(link), re.I|re.DOTALL)[0]
        headers = {}
        headers['User-Agent'] = User_Agent
        link2 = s.get(RequestURL, headers=headers, allow_redirects=False, verify=False).text
        source = re.findall(r'"sources": \[(.*?)\]', str(link2), re.I|re.DOTALL)[0]
        res_quality = []
        stream_url = []
        if auto_play == 'true':
                try:
                        url = re.findall(r'"file":"(.*?)","label":".*?"', str(source), re.I|re.DOTALL)[-1]
                except:
                        url = re.findall(r'"file":"(.*?)","label":".*?"', str(source), re.I|re.DOTALL)[0]
        else:
                match = re.findall(r'"file":"(.*?)","label":"(.*?)"', str(source), re.I|re.DOTALL)
                for url,qual in match:
                        quality = ''
                        if '1080' in qual:
                                quality = '[COLOR blue][B]'+qual+'[/COLOR][/B]'
                        elif '720' in qual:
                                quality = '[COLOR green][B]'+qual+'[/COLOR][/B]'
                        elif '480' in qual:
                                quality = '[COLOR red][B]'+qual+'[/COLOR][/B]'
                        elif '360' in qual:
                                quality = '[COLOR yellow][B]'+qual+'[/COLOR][/B]'
                        res_quality.append(quality)
                        stream_url.append(url)
                if len(match) >1:
                        dialog = xbmcgui.Dialog()
                        ret = dialog.select('Select Stream Quality',res_quality)
                        if ret == -1:
                                return
                        elif ret > -1:
                                url = stream_url[ret]
        url = url.replace('\/','/')
        liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
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
        name = name.replace('()','')
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo(type="Video", infoLabels={"Title":name,"Plot":description})
        liz.setProperty('fanart_image', fanart)
        if mode==9 or mode==10:
            liz.setProperty("IsPlayable","true")
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        else:
            ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok




def PT(url):
        addon.log('Play Trailer %s' % url)
        notification( addon.get_name(), 'fetching trailer', addon.get_icon())
        xbmc.executebuiltin("PlayMedia(%s)"%url)




def notification(title, message, icon):
        addon.show_small_popup( addon.get_name(), message.title(), 5000, icon)
        return




def addDir2(name,url,mode,iconimage,itemcount):#
        title = name
        name = name.replace('[B][COLOR white]','').replace('[/COLOR][/B]','')
        splitName=name.partition('(')
        simplename=""
        simpleyear=""
        if len(splitName)>0:
            simplename=splitName[0]
            simpleyear=splitName[2].partition(')')
        if len(simpleyear)>0:
            simpleyear=simpleyear[0]
        meta = metaget.get_meta('movie',simplename,simpleyear)
        if meta['cover_url']=='':
            try:
                meta['cover_url']=iconimage
            except:
                meta['cover_url']=icon
        meta['title'] = title
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=meta['cover_url'])
        liz.setInfo( type="Video", infoLabels= meta )
        contextMenuItems = []
        contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
        if meta['trailer']:
                contextMenuItems.append(('Play Trailer', 'XBMC.RunPlugin(%s)' % addon.build_plugin_url({'mode': 8, 'url':meta['trailer']})))
        liz.addContextMenuItems(contextMenuItems, replaceItems=False)
        if not meta['backdrop_url'] == '':
                liz.setProperty('fanart_image', meta['backdrop_url'])
        else: liz.setProperty('fanart_image', fanart)
        if mode==9 or mode==10:
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
        link = s.get(url, headers=headers, allow_redirects=False).text
        link = link.encode('utf8')
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
        elif selfAddon.getSetting(viewType) == 'List':
            VT = '50'
        elif selfAddon.getSetting(viewType) == 'Thumbnail':
            VT = '500'
        elif selfAddon.getSetting(viewType) == 'Wide':
            VT = '505'
        elif selfAddon.getSetting(viewType) == 'Default Movie View':
            VT = selfAddon.getSetting('default-view')
        elif selfAddon.getSetting(viewType) == 'Default Menu View':
            VT = selfAddon.getSetting('default-view2')

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




if mode==None or url==None or len(url)<1:
        CAT()

elif mode==1:
        INDEX(url)

elif mode==3:
        GENRE(url)

elif mode==5:
        ACTORS(url)

elif mode==7:
        SEARCH()

elif mode==8:
        PT(url)

elif mode==9:
        RESOLVE(name,url,iconimage)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































'''if xbmcvfs.exists(xbmc.translatePath('special://home/userdata/sources.xml')):
        with open(xbmc.translatePath('special://home/userdata/sources.xml'), 'r+') as f:
                my_file = f.read()
                if re.search(r'http://muckys.mediaportal4kodi.ml', my_file):
                        addon.log('Muckys Source Found in sources.xml, Not Deleting.')
                else:
                        line1 = "you have Installed The MDrepo From An"
                        line2 = "Unofficial Source And Will Now Delete Please"
                        line3 = "Install From [COLOR red]http://muckys.mediaportal4kodi.ml[/COLOR]"
                        line4 = "Removed Repo And Addon"
                        line5 = "successfully"
                        xbmcgui.Dialog().ok(addon_name, line1, line2, line3)
                        delete_addon = xbmc.translatePath('special://home/addons/'+addon_id)
                        delete_repo = xbmc.translatePath('special://home/addons/repository.mdrepo')
                        shutil.rmtree(delete_addon, ignore_errors=True)
                        shutil.rmtree(delete_repo, ignore_errors=True)
                        dialog = xbmcgui.Dialog()
                        addon.log('===DELETING===ADDON+===REPO===')
                        xbmcgui.Dialog().ok(addon_name, line4, line5)'''








































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































