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
site_logo = "http://x.pac-12.com/profiles/pac12/themes/pac12_foundation/images/pac12/networks/"

#More Live Channels..auto updated..
exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MTQgPSAiMmY6Ly8zMS4xMi4xZi8yMi8yOC8yOS8iCjEgPSAiMjc6Ly8yMS4xZi9kLzIwLzMzLzIzL2YvMjYvIgo2ID0gMSArICIxOS44IgoyID0gMSArICJlLjgiCjUgPSAxICsgIjEwLjgiCjExICAgPSA3LjQoJzJkJykKMyAgICA9IDJhLjkoIDcuNCgnMWInKSApIAoxNSA9IDMgKyAiMWQuOCIKMTMgPSAzICsgIjFhLjgiCgozMiAwKDE2LCBhPSIiKToKCTFlOgoJCTI0ID0gMWMuMTgoMTYpCgkJYiAyYy4yZSgyNCkKCWM6IGIgYQoKMWU6CgkxNyA9IDAoNikKCTMwID0gMCg1KQoJMjUgPSAwKDIpIApjOgoJMmI=")))(lambda a,b:b[int("0x"+a.group(1),16)],"urlJson_req|onetv_site|onetv_ch_list|addondir|getAddonInfo|onetv_index|onetv_logo|my_addon|txt|translatePath|noData|return|except|LongHongVan|usa_ch_list|iptvsimple2|name_index|addonname|thelogodb|myLogList|LOGO_PATH|myLogData|purl|LOGO_CH|urlopen|logo_ch|LogList|profile|urllib2|LogData|try|com|MyKodi|github|images|master|req|USA_CH|onetv|https|media|logo|xbmc|pass|json|name|load|http|NAME|www|def|raw".split("|")))
  
usa_icon = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHEbCdJb52qz-bAt0SqML7OnwfNU0z6tiB7kC4UVXVdYyMujFc"
uk_icon = "https://i.ytimg.com/vi/KjvUtf78YhQ/hqdefault.jpg"
canada_icon = "https://i.ytimg.com/vi/-ID-ZadxCJ0/hqdefault.jpg"
all_icon = "https://i0.wp.com/iptv-shop.net/wp-content/uploads/2017/06/Download-Free-IPTV-m3u-World-Channels-list-Vlc-Kodi-15-06-17.jpg?fit=1200%2C675&resize=350%2C200"
adult_icon = "http://allaboutwindowsphone.com/images/appicons/80096.png"
vn_icon = "http://www.hoavouu.com/images/file/DoVbzmQx0QgBAM8X/vntv-logo.jpg"
world_icon = "https://i.ytimg.com/vi/F6sf_Pd4l8M/maxresdefault.jpg"
music_icon = "http://1.bp.blogspot.com/_sYig04Fo8IY/Sw6UKV-323I/AAAAAAAAVhI/fzVH5bIUhfM/s1600/MTV.jpg"
news_icon = "http://occupyilluminati.com/wp-content/plugins/rss-poster/cache/ae9bf_us-news-channels-logo.jpg"
sport_icom = "https://i.ytimg.com/vi/JyiDYj1t2UE/maxresdefault.jpg"
movie_icon ="http://img.youtube.com/vi/PR6PJQdc1Ss/0.jpg"
kid_icon = "http://static.appstore.vn/a/uploads/thumbnails/122014/tomokids-tv_icon.png"
entertainmet_icon = "http://pimg.p30download.com/APK_IMG/e/usa.entertainment.television/icon/icon_3_small.png"
ppv_icon = "http://animalrightscoalition.com/wp-content/uploads/2012/05/PPV-Logo-Final.png"

FILTER1_VI = "VTV|HTV|VTC|SCTV|Hanoi|Thuần Việt|StarWorld|PHIM|Thuần Việt HD|THẾ GIỚI|SBTN|VSTAR|VIET|VBS|SAIGON|US BONUS|BONUS|VN "
FILTER2_CA = "GLOBAL|CTV|Astro|Sportsnet|NETV|TSN|HGTV|CA |Sports net|Sportnet|Sport net|TSN"

FILTER3_UK = "UK |UK: TS|UK: BT SPORT|UK: EUR|UK: National|UK: Nat |UK: ANI|UK: Sky Sport|SKY SPORTS|SKY MOVIE|National|Comedy|Sony|\
BABY|BBC WORLD|BBC AMERICA|BBC NEWS|ITV|SKY SPORT|BT SPORT|MUTV|Nick|Disney|VH|Box|RTE|Lifetime|NAT|Cartoon Network|SYFY|E!|GOL TV|EURO|COOKING|TRAVEL|FIGHT|5 USA|Premier Sport|Racing|PPV|Star |BEIN \
Willow Cricket|UTV|True|Super|WARNER|Slice|TMN|World|paramount|FOOTB|Antena|Boomerang" # removed FILM due to FILM Adult contents - SPORT, MBC, Premium

FILTER4_US = "US |USA|US:|FOX HD|FOX SPORT|FOX NEWS|FOX EAST|FOX WEST|FOX SOCCER|ESPN|NFL|NBC|CBS|ABC|NBA|TNT|BRAVO|History|SPIKE|HBO|SHOWTIME|DISCOVER|MTV |TENIS|OUTDOOR|FOOD|COOK|HGTV|\
AMC|THE CW|US|PBS|my9|SYFY|FX|FXX|DIY|Animal|Hallmark|Travel|Cartoon Network|PPV|tbs|USA-Astro|BET\
Bein Sport|Starz|MSNBC|E!|A & E|A&E|CNN|NBCSN|AXN|NEWS|TENNIS|A&E|The CW|FXx|MY9|ION|COOKING|MLB NETWORK|NHL|AMERICAN|LIFE|FREEFORM|H2|HUNTING|\
FISHING|OUTDOOR|SHOPPING|UNIVERSAL|ACTION|CINEMAX|CNBC|DESINATION|ENCORE|LIFETIME|NICK|TV Land|C-SPAN|FIGHT|MOREMAX|Big Ten|BTN|We TV|TPK |A and E|BOXING"
FILTER5_ADULT = "XXX|Play|Adult|FILM Adult|Video Adult|Video XXX|Girl|First Girl"# PAC (Removed Pac 12 | ENL)

# Indian: LN, Turkish: TR, French: FR, EX-YU: AL, GERCEE: GR, Swedish: SE, Netherland: NE, German: DE, Portugal: PT, Spanish-Latino: ES, Cyfrowy Polsat: PL, Adulti: IT, AFFRICA: AF, ARIBIC BiwnSport-OSN: AR, Russian: RU, IRAN: IR, Romani: RO, 
FILTER6_WORLD = "LN |TR |FR |AL |GR |SE |NE |DE |PT |ES |PL |IT |AF |AR |RU |IR |RO "
FILTER7_MTV = "MTV |MUSIC|VH|TPK |UK MTV|US MTV"

FILTER8_US_NEWS = "ABC|US ABC|USA ABC|CBS HD EAST|US CBS HD EAST|USA CBS HD EAST|CBS HD WEST|US CBS HD WEST|USA CBS HD WEST|NBC HD WEST|US NBC HD WEST|USA NBC HD WEST|NBC HD EAST|US NBC HD EAST|USA NBC HD EAST|CNN|US CNN|USA CNN|FOX NEWS|US FOX NEWS}USA FOX NEWS|BBC NEWS|UK BBC NEWS|MSNBC|US MSNBC|CNBC|US CNBC"
FILTER_SPORTS = "ESPN|US ESPN|USA ESPN|FOX SPORTS|US FOX SPORTS|USA FOX SPORTS|BT SPORT|UK BT SPORT|SKY SPORT|UK SKY SPORT|TSN}CA TSN|US SPORTNET|CA SPORTNET|EUROSPORT|UK EURO SPORT|TENNIS|US TENNIS|UK TENNIS|SPORT|US SPORT|UK SPORT|NBCSN|US NBCSN|USA NBCSN|NBC SPORT|US NBC SPORT|USA NBC SPORT|BT SPORT|CBS SPORTV|Bein Sport|FIGHT|FISHING|OUTDOOR|MLB NETWORK|US MLB NETWORK|NFL NETWORK|US MLB NETWORK|USA MLB NETWORK|FOX SOCCER{US FOX SOCCER|BTN|US BTN|PAC-12|US PAC-12|USA PAC-12|GOL TV}US GOL TV|UK GOL TV|NBA|US NBA|TSN|US TSN|CA TSN|EURO SPORT|UK EURO SPORT|BEIN|US BEIN|NHL NETWORK|OS NHL NETWORK|WWE|US WWE|BOXING|Boxnation|UFC|US UFC|BOXING|PPV"

FILTER_MOVIES = "SKY MOVIE|UK SKY MOVIE|HBO|US HBO|USA HBO|SHOWTIME|US SHOWTIME|USA SHOWTIME|CINEMAX|US CINEMAX|USA CINEMAX|STARZ|US STARZ|USA STARZ|MOVIE CHANNEL}ACTION}US ACTION|paramount|AMC|US AMC|MOREMAX|US MOREMAX"

FILTER_KIDS = "Nick|US Nick|Disney|UK Disney|US Disney|Cartoon Network|US Cartoon Network|UK Cartoon Network|BABY|US BABY"

FILTER_ENT = "BRAVO|US BRAVO|HGTV|US BRAVO|CA BRAVO|A and E|US A and E|USA NETWORK|US USA NETWORK|History| US History|Travel|US Travel|SPIKE|US SPIKE|DISCOVER|US DISCOVER|SYFY|US SYFY|UK SYFY|FOOD|US FOOD|COOK|US COOK|UK COOK|AMC|US AMC|THE CW|US THE CW|CW|US THE CW|PBS|US PBS|FX|US FX|FXX| US FXX|E!|US E!|AXN|US AXN|Animal|US Animal}UK Animal|LIFE|US LIFE|UK LIFE|my9|US my9|ENCORE|US ENCORE|DIY|US DIY|DESINATION|US DESINATION|NAT|US NAT|UK NAT"

try:  
	usa_ch_list = ReadList(addondir + "usa_ch_list.txt")
	name_index = ReadList(addondir + "name_index.txt")
	logo_ch = ReadList(addondir + "logo_ch.txt")
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

def filter_cat_url(FILTER="", iSMovies=False):
	if not iSMovies:
		for idx in range(0, len(USA_CH)):
			if re.match(FILTER, str(NAME[idx]), re.IGNORECASE):
				addDir(NAME[idx], USA_CH[idx], 2, LOGO_CH[idx], fanart, 'HD')
	else:
		MOVIE_NAME = NAME
		MOVIE_CH = USA_CH
		MOVIE_LOGO_CH = LOGO_CH
		for idx in range(0, len(MOVIE_CH)):
			if re.search(FILTER, str(MOVIE_NAME[idx]), re.IGNORECASE):
				addDir(MOVIE_NAME[idx], MOVIE_CH[idx], 2, MOVIE_LOGO_CH[idx], fanart, ' HD')

def CATEGORIES(REMOTE_URL=True):
	#xbmc.executebuiltin('Container.SetViewMode(500)')

	addDir("[COLOR aqua]PAC12[/COLOR]", "url", 1, icon, fanart, ' HD', isFolder=True)
	if not REMOTE_URL:
		addDir("USA CHANNELS", FILTER4_US, 4, usa_icon, fanart, ' HD', isFolder=True)
		addDir("CANADA CHANNELS", FILTER2_CA, 4, canada_icon, fanart, ' HD', isFolder=True)
		addDir("UK CHANNELS", FILTER3_UK, 4, uk_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR orange]ALL[/COLOR]", FILTER4_US + "|" + FILTER3_UK  + "|" + FILTER2_CA, 4, all_icon, fanart, ' HD', isFolder=True)
	else:
		addDir("[COLOR red]USA[/COLOR]", FILTER4_US, 5, usa_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR lime]CANADA[/COLOR]", FILTER2_CA, 5, canada_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR yellow]UK[/COLOR]", FILTER3_UK, 5, uk_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR aqua]ADULT[/COLOR]", FILTER5_ADULT, 5, adult_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]VIETNAM[/COLOR]", FILTER1_VI, 5, vn_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]MUSIC[/COLOR]", FILTER7_MTV, 5, music_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR lime]PPV CHANNELS[/COLOR]", "PPV |FIGHT NETWORK", 5, ppv_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]WORLD[/COLOR]", FILTER6_WORLD, 5, world_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]US NEWS[/COLOR]", FILTER8_US_NEWS, 5, news_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR lime]SPORT PPV CHANNELS[/COLOR]", FILTER_SPORTS, 5, sport_icom, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]MOVIE CHANNELS[/COLOR]", FILTER_MOVIES, 5, movie_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]KIDS CHANNELS[/COLOR]", FILTER_KIDS, 5, kid_icon, fanart, ' HD', isFolder=True)
		addDir("[COLOR blue]ENTERTAINMENT TV[/COLOR]", FILTER_ENT, 5, entertainmet_icon, fanart, ' HD', isFolder=True)
		#addDir("[COLOR orange]ALL LIVE CHANNELS[/COLOR]", FILTER4_US + "|" + FILTER3_UK  + "|" + FILTER2_CA, 5, all_icon, fanart, ' HD', isFolder=True)


def addDir(name, url, mode, iconimage, fanart, description, isFolder=False):
    title = ''
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)
    ok = True
    liz = xbmcgui.ListItem(name + '[I]' + title + '[/I]', iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Plot": ''})
    liz.setProperty("Fanart_Image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
    return ok

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

