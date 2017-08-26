# -*- coding: utf-8 -*-

"""
    seach.py --- functions dealing with searching bob
    Copyright (C) 2017, Midraal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import requests

import koding
import xbmc
import xbmcaddon
from koding import route
from resources.lib.util.info import get_info
from resources.lib.util.url import get_addon_url, replace_url
from resources.lib.util.xml import BobList, display_list

theme = xbmcaddon.Addon().getSetting('theme')
if theme and theme != 'DEFAULT' and theme != 'none':
    fanart = BobList.set_theme(theme)
else:
    fanart = xbmcaddon.Addon().getAddonInfo('fanart')

icon = xbmcaddon.Addon().getAddonInfo('icon')


@route(mode="Search")
def search():
    """
    Open root search directory
    """
    versionspec = {
        "columns": {
            "version": "TEXT"
        }
    }
    koding.Create_Table("version", versionspec)

    search_spec = {
        "columns": {
            "term": "TEXT"
        }
    }

    koding.Create_Table("search", search_spec)
    terms = koding.Get_All_From_Table("search")
    if terms:
        koding.Add_Dir(name="Clear Search", mode="clear_search", folder=True,
                       icon=icon, fanart=fanart)
    for term in terms:
        label = term["term"]
        context_menu = [
            ("Remove Search",
             "RunPlugin({0})".format(get_addon_url(mode="remove_search",
                                                   url=label)))
        ]
        koding.Add_Dir(name=label, url=label, mode="do_search", folder=True,
                       icon=icon, fanart=fanart, context_items=context_menu)

    koding.Add_Dir(name="Add Search", mode="add_search", folder=True,
                   icon=icon, fanart=fanart)


@route(mode="do_search", args=["url"])
def do_search(term=None):
    import os
    import xbmc
    import xbmcgui
    import time
    import datetime
    import urllib2

    search_term = term.lower()

    boblist = BobList("")
    boblist.list_image = xbmcaddon.Addon().getAddonInfo('icon')
    theme = xbmcaddon.Addon().getSetting('theme')
    if theme and theme != 'DEFAULT' and theme != 'none':
        boblist.list_fanart = boblist.set_theme(theme)
    else:
        boblist.list_fanart = xbmcaddon.Addon().getAddonInfo('fanart')
    result_list = []
    exact_result_list = []
    item_xml_result_list = []
    exact_item_xml_result_list = []
    dest_file = os.path.join(xbmc.translatePath(
        xbmcaddon.Addon().getSetting("cache_folder")), "search.db")

    url = "http://norestrictions.club/norestrictions.club/main/search/search.db"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    try:
        changed = response.headers["Last-Modified"]
        changed_struct = time.strptime(changed, "%a, %d %b %Y %H:%M:%S GMT")
        epoch_changed = int(time.mktime(changed_struct))
        if not os.path.exists(dest_file) or \
           int(os.path.getmtime(dest_file)) < epoch_changed:
            dp = xbmcgui.DialogProgress()
            dp.create('Loading database file', 'Please Wait')
            koding.Download(url, dest_file)
    except:  # server down
        if not os.path.exists(dest_file):
            import xbmcgui
            addon_name = xbmcaddon.Addon().getAddonInfo('name')
            xbmcgui.Dialog().ok(addon_name, "no local file found, and server seems down")
    response.close()
    results = koding.DB_Query(dest_file, 'SELECT * from search where item like "%%%s%%"' % search_term)
    for result in results:
        item = boblist.process_item(result["item"])
        playlister = result["poster"]
        title = item["label"].lower()
        if search_term in title:
            item["info"] = {}
            try:
                item['label'] = '{0} - {1}'.format(playlister,
                                                   item["label"])
            except:
                import xbmc
                xbmc.log("playlister: " + repr(playlister), xbmc.LOGDEBUG)
                xbmc.log("label:" + repr(item["lable"]), xbmc.LOGDEBUG)
                xbmc.log("item: " + repr(item), xbmc.LOGDEBUG)
                raise Exception()
            if title.startswith(search_term + " "):
                exact_result_list.append(item)
                exact_item_xml_result_list.append(result["item"])
                continue
            result_list.append(item)
            item_xml_result_list.append(result["item"])
    meta = xbmcaddon.Addon().getSetting("metadata") == "true"
    if meta:
        # TODO find way to get it all in single cal
        info = get_info(exact_item_xml_result_list)
        if info:
            for index, item in enumerate(exact_result_list):
                item["info"].update(info[index])

        info = get_info(item_xml_result_list)
        if info:
            for index, item in enumerate(result_list):
                item["info"].update(info[index])
    exact_result_list = sorted(exact_result_list,
                               key=lambda item: title)
    exact_result_list.extend(sorted(result_list,
                                    key=lambda item: title))
    display_list(exact_result_list, "videos")


@route(mode="add_search")
def add_search():
    term = str(koding.Keyboard("Enter search term"))
    if not term:
        return
    koding.Add_To_Table("search", {"term": term})
    do_search(term)


@route(mode="remove_search", args=["url"])
def remove_search(term):
    koding.Remove_From_Table("search", {"term": term})
    xbmc.executebuiltin("Container.Refresh")


@route(mode="clear_search")
def clear_search():
    koding.Remove_Table("search")
    xbmc.executebuiltin("Container.update(%s)" % get_addon_url("Search"))


def get_xml(link):
    import time
    xml_cache_spec = {
        "columns":
        {
            "xml": "TEXT",
            "link": "TEXT",
            "created": "TEXT",
            "changed": "TEXT"
        },
        "constraints":
        {
            "unique": "link"
        }
    }
    koding.Create_Table("xml_cache", xml_cache_spec)

    url = replace_url(link)
    req = requests.get(url)
    changed = req.headers["Last-Modified"]
    result = koding.Get_From_Table("xml_cache", {"link": link})
    if result:
        if result[0]["changed"] == changed:
            return result[0]["xml"]
        else:
            koding.Remove_From_Table("xml_cache", {"link": link})
    xml = req.content
    koding.Add_To_Table("xml_cache", {"xml": xml, "link": link,
                                      "created": time.time(),
                                      "changed": changed})
    return xml
