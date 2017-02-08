# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import xbmcplugin
import xbmcgui
import xbmcaddon
import sys
import xbmc
import re
import json
# vtvgolive code ++++++++++++++++
from resources.lib.common import *
from resources.lib.vtvgovn import vtvgovn
addon_id = 'plugin.video.vtvgolive'
my_addon = xbmcaddon.Addon(addon_id)
download_path = str(my_addon.getSetting(id='download_path'))

addonPath = my_addon.getAddonInfo('path')
version = my_addon.getAddonInfo('version')
icon = os.path.join(addonPath,'icon.png')
m3u = os.path.join(addonPath,'m3u.png')
reload = os.path.join(addonPath,'reload.jpg')
fanart = os.path.join(addonPath,'fanart.jpg')
iconbtn = os.path.join(addonPath,'iconbtn.png')
fanartbtn = os.path.join(addonPath,'fanartbtn.jpg')
setting_logo = os.path.join(addonPath,'setting.jpg')
logo_dir = os.path.join(Paths.resDir,'logos')

vnLogoHost = "http://www.tv-logo.com/pt-data/uploads/images/logo/"

m3u_file = "vtvlist_all.m3u"
addondir    = xbmc.translatePath( my_addon.getAddonInfo('profile') ) 
vtvgovnlivelist = addondir + "vtvgovnlivelist.txt"
vtvnetvnlivelist = addondir + "vtvnetvnlivelist.txt"

vtc_chid = ["vtv1","vtv2","vtv3","vtv4","ttxvn","htv9","vtc1","vtc10","vtc16","hn1"]
logo_id = ["vtv1_vn", "vtv2_vn","vtv3_vn","vtv4_vn", "ttx_vn", "htv_9", "vtc_1", "vtc_10", "vtc_16_vn", "hanoi_tv1"]	
url_vtvgovn = base64.b64decode("aHR0cDovLzEyNy4wLjAuMToxOTA5Ni92dHZnb3ZuUHJveHkv")
vntvnet_pxy = base64.b64decode("aHR0cDovLzEyNy4wLjAuMToxOTA5Ni92bnR2bmV0cHJveHkv")
m3uHdr = '#EXTINF:-1 group-title="Top 10 USA Channels",  tvg-id="" tvg-name="" tvg-logo='
m3uHdr_vtvgo = '#EXTINF:-1 group-title="VTVGoVN Live",  tvg-id="" tvg-name="" tvg-logo='	
m3uHdr_tvnet = '#EXTINF:-1 group-title="Top VTV VTC Live",  tvg-id="" tvg-name="" tvg-logo='
ProxyMode = str(my_addon.getSetting(id='isProxyMode'))

try: # intial/refresh
	global vtvm3u_all
	import uuid
	macAdr = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
	lanIpAdr = str(xbmc.getIPAddress())
	ProxyMode = str(my_addon.getSetting(id='isProxyMode'))
	if download_path == "":
		vtvm3u_all = os.path.join(addondir,m3u_file)
	else:
		vtvm3u_all = os.path.join(download_path, m3u_file)
	mydebug = str(my_addon.getSetting(id='debug_message'))
except: pass

#check Version
try:
	import platform
	osType = platform.system()
	osVer = platform.release()
	KodiVer = xbmc.getInfoLabel( "System.BuildVersion" )[:2]
	infoDialog("OS: " + str(osType) + " " + str(osVer) + "\nKodi " + str(KodiVer), "Check Version")	
	
except: pass

def vtvnet_livelist(m3uList=False,chid=vtc_chid):
	global vntvnet_pxy, ProxyMode 
	ProxyMode = str(my_addon.getSetting(id='isProxyMode'))
	if ProxyMode == "false": vntvnet_pxy = ""
	else: vntvnet_pxy = base64.b64decode("aHR0cDovLzEyNy4wLjAuMToxOTA5Ni92bnR2bmV0cHJveHkv")
	if not m3uList:
		for idx in range(0, len(chid)):
			name = chid[idx]
			image = logo_id[idx]
			thumb = vnLogoHost + image + ".jpg"
			addLink(name.upper() + " HD", vntvnet_pxy + name, 2, thumb, fanart, ' HD')
			writeappend_file(vtvnetvnlivelist, m3uHdr_tvnet +'"'+ thumb +'",' + name)
			writeappend_file(vtvnetvnlivelist, vntvnet_pxy + chid[idx])
	else:# create m3u
		deleteContent(vtvnetvnlivelist)
		for idx in range(0, len(chid)):
			infoDialog("process index: " + str(idx), "vtvnet m3uList. Please wait..")
			name = chid[idx]
			image = logo_id[idx]
			thumb = vnLogoHost + image + ".jpg"
			writeappend_file(vtvnetvnlivelist, m3uHdr_tvnet +'"'+ thumb +'",' + name)
			writeappend_file(vtvnetvnlivelist, vntvnet_pxy + chid[idx])
			
def vtvgo_livelist(m3uList=False):
	global url_vtvgovn, ProxyMode
	myvtvgo=vtvgovn() 
	index = 0
	ProxyMode = str(my_addon.getSetting(id='isProxyMode'))
	if ProxyMode == "false": url_vtvgovn = ""
	else: url_vtvgovn = base64.b64decode("aHR0cDovLzEyNy4wLjAuMToxOTA5Ni92dHZnb3ZuUHJveHkv")
	if m3uList:
		deleteContent(vtvgovnlivelist)
		for name, url, thumb in myvtvgo.liveList():
		    index += 1
		    infoDialog("process index: " + str(index), "vtvgo m3uList. Please wait..")
		    writeappend_file(vtvgovnlivelist, m3uHdr_vtvgo +'"'+ thumb +'",' + name.replace(",", " -"))
		    writeappend_file(vtvgovnlivelist, url_vtvgovn + url + "\n")# url link
	else:
		deleteContent(vtvgovnlivelist)
		for name, url, thumb in myvtvgo.liveList():
			addLink(name, url_vtvgovn + url, 2, thumb, fanart, ' HD')
			writeappend_file(vtvgovnlivelist, m3uHdr_vtvgo +'"'+ thumb +'",' + name.replace(",", " -"))
			writeappend_file(vtvgovnlivelist, url_vtvgovn + url + "\n")# url link
		
def vtvm3uList_all(list=vtvm3u_all, chid=vtc_chid):
	global vtvm3u_all
	import time
	myvtvgo=vtvgovn()
	index = 0
	deleteContent(list)
	writeappend_file(list, "#EXTM3U \n")
	for name, url, thumb in myvtvgo.liveList():
		index += 1
		#xbmc.sleep(350)
		infoDialog("process index " + "vtvgo: " + str(index), "vtvgo m3uList. Please wait..")
		#xbmc.sleep(350)
		writeappend_file(list, m3uHdr_vtvgo +'"'+ thumb +'",' + name.replace(",", " -"))
		writeappend_file(list, url_vtvgovn + url + "\n")# url link
		#xbmc.sleep(350)
	for idx in range(0, len(chid)):
		infoDialog("process index "  + "vtvnet: " + str(idx), "vtvnet m3uList. Please wait..")
		#xbmc.sleep(350)
		name = chid[idx]			
		image = logo_id[idx]
		thumb = vnLogoHost + image + ".jpg"
		writeappend_file(list, m3uHdr_vtvgo +'"'+ thumb +'",' + name.upper() + " HD")
		writeappend_file(list, vntvnet_pxy + chid[idx])	
		#xbmc.sleep(350)
	infoDialog("Done m3u list for IPTV Simple Client", "vtvm3uList_all")
	time.sleep(3)
	ShowMessage("M3U list for PVR IPTV Simple Client", "Creating M3U file in: \n" + str(list))
	
def get_vtvgo_chid(pattern,string,group=1,flags=0,result=''):
	try:s=re.search(pattern,string,flags).group(group)
	except:s=result
	return s	

def Categories():	
    xbmc.executebuiltin('Container.SetViewMode(500)')
    addLink("[COLOR teal]Settings[/COLOR]", "url", 1, setting_logo, fanart, " HD")
    addLink("[COLOR teal]Export M3U file[/COLOR]", "url", 3, m3u, fanart, " HD")	
    vtvgo_livelist(False)	
    vtvnet_livelist(False,vtc_chid)	
	
def addLink(name, url, mode, iconimage, fanart, description, isFolder=False):
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

try: url = urllib.unquote_plus(params["url"])
except: pass
try: name = urllib.unquote_plus(params["name"])
except: pass
try: mode = int(params["mode"])
except: pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode == None or url == None or len(url) < 1:
        print ""
        Categories()

elif mode==1:
	showAddonSettings()
	Categories()
		
elif mode == 2:
	global ProxyMode
	ProxyMode = str(my_addon.getSetting(id='isProxyMode'))
	if ProxyMode == "false" and "vtvgo.vn" in url:
		try:
			url_stream = vtvgovn().getStream(url)
			playStream(url_stream, name, icon)
		except: pass
	elif ProxyMode == "false" and url in vtc_chid:
		try:
			url_stream = vtvgovn().getStreamTvnet(url)
			playStream(url_stream, name, icon)
		except: pass
	else:
		playStream(url, name, icon)
	infoDialog('Status: Start/Stop', '[COLOR yellow]Media Player[/COLOR]', time=5000)
	
elif mode == 3:
	infoDialog('Process channel list', '[COLOR yellow]vtvm3uList_all M3U Creator[/COLOR]')
	vtvm3uList_all()
	xbmc.sleep(5)
	infoDialog('Done channel list', '[COLOR yellow]vtvm3uList_all M3U Creator[/COLOR]')
	exit()	

elif mode == 4:
        Categories()

xbmcplugin.endOfDirectory(int(sys.argv[1]))
