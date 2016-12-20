# -*- coding: utf-8 -*-
import urllib
import urllib2
import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
import xbmc
import re
import json
from resources.lib.common import *

my_addon = xbmcaddon.Addon('plugin.video.Pac-12')
addonPath = my_addon.getAddonInfo('path')
icon = addonPath + '/icon.png'
fanart = addonPath + '/fanart.jpg'
iconbtn = addonPath + '/iconbtn.png'
fanartbtn = addonPath + '/fanartbtn.jpg'
intro = addonPath + '/intro.mp4'
isplayed = xbmc.getInfoLabel("Window(Home).Property(intro.isplayed)").lower() == "true"
site = 'http://xrxs.net/process.php'
site_logo = "http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/"

#More Live Channels..auto updated..
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MTQgPSAiMmY6Ly8zMS4xMi4xZi8yMi8yOC8yOS8iCjEgPSAiMjc6Ly8yMS4xZi9kLzIwLzMzLzIzL2YvMjYvIgo2ID0gMSArICIxOS44IgoyID0gMSArICJlLjgiCjUgPSAxICsgIjEwLjgiCjExICAgPSA3LjQoJzJkJykKMyAgICA9IDJhLjkoIDcuNCgnMWInKSApIAoxNSA9IDMgKyAiMWQuOCIKMTMgPSAzICsgIjFhLjgiCgozMiAwKDE2LCBhPSIiKToKCTFlOgoJCTI0ID0gMWMuMTgoMTYpCgkJYiAyYy4yZSgyNCkKCWM6IGIgYQoKMWU6CgkxNyA9IDAoNikKCTMwID0gMCg1KQoJMjUgPSAwKDIpIApjOgoJMmI=")))(lambda a,b:b[int("0x"+a.group(1),16)],"urlJson_req|onetv_site|onetv_ch_list|addondir|getAddonInfo|onetv_index|onetv_logo|my_addon|txt|translatePath|noData|return|except|LongHongVan|usa_ch_list|iptvsimple2|name_index|addonname|thelogodb|myLogList|LOGO_PATH|myLogData|purl|LOGO_CH|urlopen|logo_ch|LogList|profile|urllib2|LogData|try|com|MyKodi|github|images|master|req|USA_CH|onetv|https|media|logo|xbmc|pass|json|name|load|http|NAME|www|def|raw".split("|")))
 
  
def CATEGORIES():
    xbmc.executebuiltin('Container.SetViewMode(500)')
    if my_addon.getSetting("use_PAC-12_intro") == "true":
        if not isplayed:
            li = xbmcgui.ListItem(label='PAC-12', iconImage=icon, thumbnailImage=icon)
            xbmc.Player().play(intro, li)
            xbmcgui.Window(10000).setProperty("intro.isplayed", "true")
    addDir('Pac National', 'p12netw', 1, icon, fanart, 'Pac-12')
    addDir('Arizona', 'p12ariz', 1, site_logo + 'network-arizona.jpg', fanart, 'Pac-12 Arizona')
    addDir('Bay Area', 'p12baya', 1, site_logo + 'network-bayarea.jpg', fanart, 'Pac-12 Bay Area')
    addDir('Los Angeles', 'p12losa', 1, site_logo + 'network-losangeles.jpg', fanart, 'Pac-12 Los Angeles')
    addDir('Mountain', 'p12moun', 1, site_logo + 'network-mountain.jpg', fanart, 'Pac-12 Mountain')
    addDir('Oregon', 'p12oreg', 1, site_logo + 'network-oregon.jpg', fanart, 'Pac-12 Oregon')
    addDir('Washington', 'p12wash', 1, site_logo + 'network-washington.jpg', fanart, 'Pac-12 Washington')
    if '//' in my_addon.getSetting("BTN"):
        addDir('BTN', my_addon.getSetting("BTN"), 2, iconbtn, fanartbtn, 'Big Ten')
    
    for idx in range(0, len(USA_CH)):
		addDir(NAME[idx], USA_CH[idx], 2, LOGO_CH[idx], fanart, ' HD')


def addDir(name, url, mode, iconimage, fanart, description):
    title = ''
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok = True
    liz = xbmcgui.ListItem(name + '[I]' + title + '[/I]', iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": ''})
    liz.setProperty("Fanart_Image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def Play(url, name, icon):
    if my_addon.getSetting("use_custom_links") == "true":
        lista = [['1080p', '4728.m3u8'], ['720p', '2328.m3u8'], ['SD', '1164.m3u8']]
        lista2 = [['1080p', 'index_4728_av-p.m3u8'], ['720p', 'index_2328_av-b.m3u8'], ['SD', 'index_1164_av-b.m3u8']]
        d = xbmcgui.Dialog()
        item = d.select("Select Quality", getItemTitles(lista))
        if item != -1:
            if 'p12netw' in url:
                url = my_addon.getSetting("National")
            elif 'p12ariz' in url:
                url = my_addon.getSetting("Arizona")
            elif 'p12baya' in url:
                url = my_addon.getSetting("Bay")
            elif 'p12losa' in url:
                url = my_addon.getSetting("Angeles")
            elif 'p12moun' in url:
                url = my_addon.getSetting("Mountain")
            elif 'p12oreg' in url:
                url = my_addon.getSetting("Oregon")
            elif 'p12wash' in url:
                url = my_addon.getSetting("Washington")
            print url
            if 'xrxs' in url:
                url = url + str(lista[item][1])
            else:
                url = url + str(lista2[item][1])
            li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
            xbmc.Player().play(item=url, listitem=li)
        exit()
    else:
        lista = [['1080p', '4728.m3u8'], ['720p', '2328.m3u8'], ['SD', '1164.m3u8']]
        d = xbmcgui.Dialog()
        item = d.select("Select Quality", getItemTitles(lista))
        if item != -1:
            try:
                quality = str(lista[item][1])
                query_args = {'page': 'links', 'network': url, 'bitrate': quality}
                encoded_args = urllib.urlencode(query_args)
                request = urllib2.Request(site)
                request.add_header('User-agent', 'Mozilla/5.0')
                response = urllib2.urlopen(request, encoded_args)
                data = response.read()
                response.close()
                link = re.compile('<input value="(.+?)" class=').findall(data)
                if len(link) > 0:
                    for url in link:
                        url = url.replace('.m3u8.m3u8' , '.m3u8')
                        li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
                        xbmc.Player().play(item=url, listitem=li)
                        exit()
                else:
                    addonname = my_addon.getAddonInfo('name')
                    line1 = "Try custom links"
                    line2 = "Greetings, huball"
                    xbmcgui.Dialog().ok(addonname, line1, line2)
            except: 
                CATEGORIES()


def Playbtn(url, name, icon):
    li = xbmcgui.ListItem(label=name, iconImage=icon, thumbnailImage=icon, path="")
    xbmc.Player().play(item=url, listitem=li)
    exit()


def get_params():
        param = []
        paramstring = sys.argv[2]
        if len(paramstring) >= 2:
                params = sys.argv[2]
                cleanedparams = params.replace('?', '')
                if (params[len(params) - 1] == '/'):
                        params = params[0:len(params) - 2]
                pairsofparams = cleanedparams.split('&')
                param = {}
                for i in range(len(pairsofparams)):
                        splitparams = {}
                        splitparams = pairsofparams[i].split('=')
                        if (len(splitparams)) == 2:
                                param[splitparams[0]] = splitparams[1]
        return param


params = get_params()
url = None
name = None
mode = None

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

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode == None or url == None or len(url) < 1:
        print ""
        CATEGORIES()

elif mode == 1:
        Play(url, name, icon)

elif mode == 2:
        Playbtn(url, name, icon)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
xbmcgui.Window(10000).setProperty("intro.isplayed", "false")

