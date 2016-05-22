# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import urllib,urllib2
import os
import xbmc,xbmcplugin,xbmcgui,xbmcaddon
import getlink
import simplejson as json
from config import VIETMEDIA_HOST
from addon import alert, notify, ADDON, ADDON_ID, ADDON_PROFILE
from platform import PLATFORM
import uuid

reload(sys);
sys.setdefaultencoding("utf8")

HANDLE = int(sys.argv[1])

CURRENT_PATH = ADDON.getAddonInfo("path")
PROFILE_PATH = xbmc.translatePath(ADDON_PROFILE).decode("utf-8")

VERSION = ADDON.getAddonInfo("version")
USER = ADDON.getSetting('user_id')
USER_PIN_CODE = ADDON.getSetting('user_pin_code')

def fetch_data(url, headers=None):
  visitor = get_visitor()
  if headers is None:
    headers = { 
                'User-agent'    : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
                'Referers'      : 'http://www..google.com',
                'X-Visitor'     : visitor,
                'X-Version'     : VERSION,
                'X-User'        : USER,
                'X-User-Pin'    : USER_PIN_CODE,
                'X-Platform'    : PLATFORM,
              }
  try:
    req = urllib2.Request(url,headers=headers)
    f = urllib2.urlopen(req)
    body=f.read()

    return json.loads(body)
  except:
    pass

def get_visitor():
  
  filename = os.path.join(PROFILE_PATH, 'visitor.dat' )
  visitor = ''

  if os.path.exists(filename):
    with open(filename, "r") as f:
      visitor = f.readline()
  else:
    try:
      visitor = str(uuid.uuid1())
    except:
      visitor = str(uuid.uuid4())
    
    if not os.path.exists(PROFILE_PATH):
      os.makedirs(PROFILE_PATH)
    with open(filename, "w") as f:
      f.write(visitor)

  return visitor

def play(data):
  link = data["url"]
  link = getlink.get(link)
  if link is None or len(link) == 0:
    notify('Lỗi không lấy được link phim.')
    return
  subtitle = ''
  links = link.split('[]')
  if len(links) == 2:
    subtitle = links[1]
  elif data.get('subtitle'):
    subtitle = data.get('subtitle')
  link = links[0]

  item = xbmcgui.ListItem(path=link, thumbnailImage=xbmc.getInfoLabel("ListItem.Art(thumb)"))
  xbmcplugin.setResolvedUrl(HANDLE, True, item)
  
  if len(subtitle) > 0:
    subtitlePath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
    subfile = xbmc.translatePath(os.path.join(subtitlePath, "temp.sub"))
    try:
      if os.path.exists(subfile):
        os.remove(subfile)
      f = urllib2.urlopen(subtitle)
      with open(subfile, "wb") as code:
        code.write(f.read())
      xbmc.sleep(3000)
      xbmc.Player().setSubtitles(subfile)
      #notify('Tải phụ đề thành công')
    except:
      notify('Không tải được phụ đề phim.')

def go():
  url = sys.argv[0].replace("plugin://%s" % ADDON_ID, VIETMEDIA_HOST ) + sys.argv[2]
  if url == VIETMEDIA_HOST + '/':
    url += '?action=menu'
  
  #Settings
  if '__settings__' in url:
    ADDON.openSettings()
    return
  #Search
  if '__search__' in url:
    keyboardHandle = xbmc.Keyboard('','VietmediaF')
    keyboardHandle.doModal()
    if (keyboardHandle.isConfirmed()):
      queryText = keyboardHandle.getText()
      if len(queryText) == 0:
        return
      queryText = urllib.quote_plus(queryText)
      url = url.replace('__search__', queryText)
    else:
      return
  data = fetch_data(url)
  if not data:
    return
  if data.get('error'):
    alert(data['error'])
    return
  
  if data.get("url"):
    play(data)
    return

  if data.get("content_type") and len(data["content_type"]) > 0:
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_UNSORTED)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_GENRE)
    xbmcplugin.setContent(HANDLE, data["content_type"])

  listitems = range(len(data["items"]))
  for i, item in enumerate(data["items"]):
      listItem = xbmcgui.ListItem(label=item["label"], label2=item["label2"], iconImage=item["icon"], thumbnailImage=item["thumbnail"])
      if item.get("info"):
          listItem.setInfo("video", item["info"])
      if item.get("stream_info"):
          for type_, values in item["stream_info"].items():
              listItem.addStreamInfo(type_, values)
      if item.get("art"):
          listItem.setArt(item["art"])
      if item.get("context_menu"):
          listItem.addContextMenuItems(item["context_menu"])
      listItem.setProperty("isPlayable", item["is_playable"] and "true" or "false")
      if item.get("properties"):
          for k, v in item["properties"].items():
              listItem.setProperty(k, v)
      listitems[i] = (item["path"], listItem, not item["is_playable"])

  xbmcplugin.addDirectoryItems(HANDLE, listitems, totalItems=len(listitems))
  xbmcplugin.endOfDirectory(HANDLE, succeeded=True, updateListing=False, cacheToDisc=True)

go()

