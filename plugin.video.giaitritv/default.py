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

import xbmc, xbmcgui, xbmcplugin, sys, re

plugin_handle = int(sys.argv[1])
xbmcplugin.setContent(plugin_handle, "video")
icon = xbmc.translatePath("special://home/addons/plugin.video.giaitritv/icon.png")
fanart = xbmc.translatePath("special://home/addons/plugin.video.giaitritv/fanart.jpg")
xml_playlist = xbmc.translatePath("special://home/addons/plugin.video.giaitritv/playlist.xml")
xml_regex = "<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>"
m3u_playlist = xbmc.translatePath("special://home/addons/plugin.video.giaitritv/playlist.m3u")
m3u_regex = "#.+,(.+?)\n(.+?)\n"

def open_file(file):
    try:
        f = open(file, "r")
        content = f.read()
        f.close()
        return content
    except:
        pass

def add_item(url, infolabels, img = "", fanart = ""):
    listitem = xbmcgui.ListItem(infolabels["title"], iconImage = img, thumbnailImage = img)
    listitem.setInfo("video", infolabels)
    listitem.setProperty("fanart_image", fanart)
    listitem.setProperty("IsPlayable", "false")
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return

try:
    link = open_file(m3u_playlist)
    match = re.compile(m3u_regex).findall(link)
    for title, url in match:
        try:
            url = url.replace('"', ' ').replace('&amp;', '&').strip()
            title = re.sub('\s+', ' ', title).replace('"', ' ').strip()
            add_item(url, {"title": title}, icon, fanart)
        except:
            pass
except:
    pass

try:
    link = open_file(xml_playlist)
    match = re.compile(xml_regex).findall(link)
    for title, url, thumb in match:
        try:
            url = url.replace('"', ' ').replace('&amp;', '&').strip()
            title = re.sub('\s+', ' ', title).replace('"', ' ').strip()
            if (len(thumb) > 0):
                add_item(url, {"title": title}, thumb, thumb)
            else:
                add_item(url, {"title": title}, icon, fanart)
        except:
            pass
except:
    pass

xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)