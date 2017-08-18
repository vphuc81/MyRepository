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
  
usa_icon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEbCdJb52qz-bAt0SqML7OnwfNU0z6tiB7kC4UVXVdYyMujFc"
uk_icon = "https://albaniaiptv.com/wp-content/uploads/2016/12/uk-british-flag-waving-animated-gif-9-300x160.gif"
canana_icon = "https://i.ytimg.com/vi/-ID-ZadxCJ0/hqdefault.jpg"
all_icon = "https://i0.wp.com/iptv-shop.net/wp-content/uploads/2017/06/Download-Free-IPTV-m3u-World-Channels-list-Vlc-Kodi-15-06-17.jpg?fit=1200%2C675&resize=350%2C200"

FILTER1_VI = "VTV|HTV|VTC|SCTV|Hanoi|Thuần Việt|Star|PHIM|MTV |Music|VH|Thuần Việt HD|National|Concerts|JPOP|TOM|THẾ GIỚI|SBTN|VSTAR|VIET|VBS"
FILTER2_CA = "GLOBAL|CTV|Astro|Sportsnet|NETV|TSN|HGTV|CA |Sports net|Sportnet|Sport net"

FILTER3_UK = "UK |UK: TS|UK: BT SPORT|UK: EUR|UK: National|UK: Nat |UK: ANI|UK: Sky Sport|SKY SPORTS|SKY MOVIE|National|Comedy|Sony|\
BABY|BBC WORLD|BBC AMERICA|BBC NEWS|ITV|SKY SPORT|BT SPORT|MUTV|Nick|Disney|VH|Box|RTE|Lifetime|NAT|Cartoon Network|SYFY|E!|GOL TV|EURO|COOKING|TRAVEL|FIGHT|5 USA|Premier Sport|Racing|PPV|Star |\
Willow Cricket|UTV|True|Super|WARNER|Slice|TMN|World|paramount|FOOTB|Antena|Boomerang" # removed FILM due to FILM Adult contents - SPORT, MBC, Premium

FILTER4_US = "US |USA|US:|FOX HD|FOX SPORT|FOX NEWS|FOX EAST|FOX WEST|FOX SOCCER|ESPN|NFL|NBC|CBS|ABC|NBA|TNT|BRAVO|History|SPIKE|HBO|SHOWTIME|DISCOVER|MTV |TENIS|OUTDOOR|FOOD|COOK|HGTV|\
AMC|THE CW|US|PBS|my9|SYFY|FX|FXX|DIY|Animal|Hallmark|Travel|Cartoon Network|PPV|tbs|USA-Astro|BET\
Bein Sport|Starz|MSNBC|E!|A & E|A&E|CNN|NBCSN|AXN|NEWS|TENNIS|A&E|The CW|FXx|MY9|ION|COOKING|MLB NETWORK|NHL|AMERICAN|LIFE|FREEFORM|H2|HUNTING|\
FISHING|OUTDOOR|SHOPPING|UNIVERSAL|ACTION|CINEMAX|CNBC|DESINATION|ENCORE|LIFETIME|NICK|TV Land|C-SPAN|FIGHT|MOREMAX|Big Ten|BTN|We TV|TPK "
FILTER5_ADULT = "XXX|Play|Adult|FILM Adult|Video Adult|Video XXX|Girl|First Girl"# PAC (Removed Pac 12 | ENL)

try:  
	usa_ch_list = ReadList(addondir + "\usa_ch_list.txt")
	name_index = ReadList(addondir + "name_index.txt")
	logo_ch = ReadList(addondir + "\logo_ch.txt")
except: pass

def pac12():
    addDir('National FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEybmV0dy00NzI4Lm0zdTg=', 2, icon, fanart, 'Pac-12')
    addDir('Arizona FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEyYXJpei00NzI4Lm0zdTg=', 2, site_logo + 'network-arizona.jpg', fanart, 'Pac-12 Arizona')
    addDir('Bay Area FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEybG9zYS00NzI4Lm0zdTg=', 2, site_logo + 'network-bayarea.jpg', fanart, 'Pac-12 Bay Area')
    addDir('Los Angeles FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEybW91bi00NzI4Lm0zdTg=', 2, site_logo + 'network-losangeles.jpg', fanart, 'Pac-12 Los Angeles')
    addDir('Mountain FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEyb3JlZy00NzI4Lm0zdTg=', 2, site_logo + 'network-mountain.jpg', fanart, 'Pac-12 Mountain')
    addDir('Oregon FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEyd2FzaC00NzI4Lm0zdTg=', 2, site_logo + 'network-oregon.jpg', fanart, 'Pac-12 Oregon')
    addDir('Washington FHD', 'http://127.0.0.1:19098/livestreamer/aGxzOi8vaHR0cDovL3hyeHMubmV0L3ZpZGVvL2xpdmUtcDEyYmF5YS00NzI4Lm0zdTg=', 2, site_logo + 'network-washington.jpg', fanart, 'Pac-12 Washington')

def filter_cat(FILTER=""):
	for idx in range(0, len(usa_ch_list)):
		if re.match(FILTER, str(name_index[idx]), re.IGNORECASE):
			addDir(name_index[idx], usa_ch_list[idx], 2, logo_ch[idx], fanart, ' HD')

def filter_cat_url(FILTER=""):
	for idx in range(0, len(USA_CH)):
		if re.match(FILTER, str(NAME[idx]), re.IGNORECASE):
			addDir(NAME[idx], USA_CH[idx], 2, LOGO_CH[idx], fanart, ' HD')

def CATEGORIES(REMOTE_URL=True):
	#xbmc.executebuiltin('Container.SetViewMode(500)')
	addDir("[COLOR aqua]PAC12[/COLOR]", "url", 1, icon, fanart, ' HD', isFolder=True)
	if not REMOTE_URL:
		addDir("USA CHANNELS", FILTER4_US, 4, usa_icon, fanart, ' HD', isFolder=True)
		addDir("CANADA CHANNELS", FILTER2_CA, 4, canana_icon, fanart, ' HD', isFolder=True)
		addDir("UK CHANNELS", FILTER3_UK, 4, uk_icon, fanart, ' HD', isFolder=True)
	else:
		addDir("[COLOR red]USA[/COLOR]", FILTER4_US, 5, usa_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR lime]CANADA[/COLOR]", FILTER2_CA, 5, canana_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR yellow]UK[/COLOR]", FILTER3_UK, 5, uk_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR orange]ALL[/COLOR]", FILTER4_US + "|" + FILTER3_UK  + "|" + FILTER2_CA, 5, all_icon, fanart, ' HD', isFolder=True)


def addDir(name, url, mode, iconimage, fanart, description, isFolder=False):
    title = ''
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok = True
    liz = xbmcgui.ListItem(name + '[I]' + title + '[/I]', iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": ''})
    liz.setProperty("Fanart_Image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
    return ok


def getItemTitles(table):
    out = []
    for i in range(len(table)):
        value = table[i]
        out.append(value[0])
    return out


def playStream(url, name, icon):
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
        pac12()

elif mode == 2:
        playStream(url, name, icon)
		
elif mode == 4:
		filter_cat(url)

elif mode == 5:
		filter_cat_url(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
xbmcgui.Window(10000).setProperty("intro.isplayed", "false")

