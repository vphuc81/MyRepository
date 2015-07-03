# -*- coding: utf-8 -*-

"""
Copyright (C) 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""

import urllib, urllib2, sys, re, os
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])
xbmcplugin.setContent(plugin_handle, 'movies')

mysettings = xbmcaddon.Addon(id = 'plugin.video.giaitritv')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

online_m3u = mysettings.getSetting('online_m3u')
local_m3u = mysettings.getSetting('local_m3u')
online_xml = mysettings.getSetting('online_xml')
local_xml = mysettings.getSetting('local_xml')

xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_regex = '#.+,(.+)\n(.+)\n'

u_tube = 'http://www.youtube.com'

def read_file(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
	
def add_m3u_link():
	match = re.compile(m3u_regex).findall(content)
	for name, url in match:
		url = url.replace('"', ' ').replace('&amp;', '&').strip()
		name = re.sub('\s+', ' ', name).replace('"', ' ').strip()			
		add_link(name, url, icon, fanart)
					
def add_xml_link():
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		url = url.replace('"', ' ').replace('&amp;', '&').strip()
		name = re.sub('\s+', ' ', name).replace('"', ' ').strip()				
		if len(thumb) > 0:
			add_link(name, url, thumb, thumb)
		else:
			add_link(name, url, icon, fanart)

def add_link(name, url, img = '', fanart = ''):
    liz = xbmcgui.ListItem(name, iconImage = img, thumbnailImage = img)
    liz.setInfo('video', infoLabels = {'Title': name})
    liz.setProperty('fanart_image', fanart)
    liz.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem = liz)
    return	

if len(online_m3u) > 0:	
	try:
		#add_link('[COLOR yellow][B]*** Online m3u playlist ***[/COLOR][/B]', u_tube, icon, fanart) # label + url checker
		content = make_request(online_m3u)
		add_m3u_link()
	except:
		pass
	
if len(online_xml) > 0:	
	try:
		#add_link('[COLOR red][B]*** Online xml playlist ***[/COLOR][/B]', u_tube, icon, fanart) # label + url checker
		content = make_request(online_xml)
		add_xml_link()
	except:
		pass			

if len(local_m3u) > 0:
	try:
		add_link('[COLOR yellow][B]*** Local m3u playlist ***[/COLOR][/B]', u_tube, icon, fanart)
		content = read_file(local_m3u)
		add_m3u_link()
	except:
		pass
		
if len(local_xml) > 0:
	try:
		add_link('[COLOR red][B]*** Local xml playlist ***[/COLOR][/B]', u_tube, icon, fanart)
		content = read_file(local_xml)
		add_xml_link()	
	except:
		pass
		
if (len(online_m3u) < 1 and len(local_m3u) < 1 and len(online_xml) < 1 and len(local_xml) < 1 ):		
	mysettings.openSettings()
		
xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)