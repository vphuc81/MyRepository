#!/usr/bin/python
#coding=utf-8
import xbmc,xbmcaddon,xbmcplugin,xbmcgui,sys,urllib,urllib2,re,os,codecs

addonID = 'plugin.video.accessasiatv'
addon = xbmcaddon.Addon(addonID)
pluginhandle = int(sys.argv[1])

def Home():
    path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path') ).decode("utf-8")
    path = xbmc.translatePath(os.path.join(path,"temp.jpg"))
    #urllib.urlretrieve('http://langsongviet.com/fta4vnForum/upload/images/ads/temp.jpg',path)
    urllib.urlretrieve('https://raw.githubusercontent.com/vinhcomp/xml/master/repository.vinh/tempPat.jpg',path)
    #urllib.urlretrieve("tempPat.jpg",path)
    img = xbmcgui.ControlImage(360,140,540,360, path)
    wdlg = xbmcgui.WindowDialog()
    #wdlg.addControl(img)
    #wdlg.doModal()

    homemenu = GetUrl("https://raw.githubusercontent.com/vinhcomp/xml/master/xml/phimhot")
    #homemenu = codecs.open("local_source_file", encoding='utf-8').read()
    for menutitle,menulink in eval(homemenu):
        addDir(menutitle,menulink,'indexgroup',path.replace("temp.jpg","icon.png"))
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(50)')

def IndexGroup(url):
    xmlcontent = GetUrl(url)
    names = re.compile('<name>(.+?)</name>').findall(xmlcontent)
    if len(names) == 1:
        items = re.compile('<item>(.+?)</item>').findall(xmlcontent)
        for item in items:
            thumb=""
            title=""
            link=""
            if "/title" in item:
                title = re.compile('<title>(.+?)</title>').findall(item)[0]
            if "/link" in item:
                link = re.compile('<link>(.+?)</link>').findall(item)[0]
            if "/thumbnail" in item:
                thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
            addLink(title, link, 'play', thumb)
        skin_used = xbmc.getSkinDir()
        if skin_used == 'skin.xeebo':
            xbmc.executebuiltin('Container.SetViewMode(52)')
    else:
        for name in names:
            addDir(name, url+"?n="+name, 'index', '')

def Index(url):
    byname = url.split("?n=")[1]
    url = url.split("?")[0]
    xmlcontent = GetUrl(url)
    channels = re.compile('<channel>(.+?)</channel>').findall(xmlcontent)
    for channel in channels:
        if byname in channel:
            items = re.compile('<item>(.+?)</item>').findall(channel)
            for item in items:
                thumb=""
                title=""
                link=""
                if "/title" in item:
                    title = re.compile('<title>(.+?)</title>').findall(item)[0]
                if "/link" in item:
                    link = re.compile('<link>(.+?)</link>').findall(item)[0]
                if "/thumbnail" in item:
                    thumb = re.compile('<thumbnail>(.+?)</thumbnail>').findall(item)[0]
                addLink(title, link, 'play', thumb)
    skin_used = xbmc.getSkinDir()
    if skin_used == 'skin.xeebo':
        xbmc.executebuiltin('Container.SetViewMode(52)')

def PlayVideo(url,title):
    title = urllib.unquote_plus(title)
    playlist = xbmc.PlayList(1)
    playlist.clear()
    listitem = xbmcgui.ListItem(title)
    listitem.setInfo('video', {'Title': title})
    xbmcPlayer = xbmc.Player()
    playlist.add(url, listitem)
    xbmcPlayer.play(playlist)

def GetUrl(url):
    link = ""
    if os.path.exists(url)==True:
        link = open(url).read()
    else:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    link = ''.join(link.splitlines()).replace('\'','"')
    link = link.replace('\n','')
    link = link.replace('\t','')
    link = re.sub('  +',' ',link)
    link = link.replace('> <','><')
    return link

def addLink(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
    return ok

def addDir(name,url,mode,iconimage):
    u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
    return ok

def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params=parameters_string_to_dict(sys.argv[2])
mode=params.get('mode')
url=params.get('url')
name=params.get('name')
if type(url)==type(str()):
    url=urllib.unquote_plus(url)

sysarg=str(sys.argv[1])
if mode == 'index':
    Index(url)
elif mode == 'indexgroup':
    IndexGroup(url)
elif mode=='play':
    dialogWait = xbmcgui.DialogProgress()
    dialogWait.create('Brought to you by Danasyentertainment.com', 'Loading video. Please wait...')
    PlayVideo(url,name)
    dialogWait.close()
    del dialogWait
else:
    Home()
xbmcplugin.endOfDirectory(int(sysarg))
