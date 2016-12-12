# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import urllib,urllib2,re
import os
import xbmc,xbmcplugin,xbmcgui,xbmcaddon
import getlink
import simplejson as json
from config import VIETMEDIA_HOST
from addon import alert, notify, ADDON, ADDON_ID, ADDON_PROFILE
from platform import PLATFORM
import uuid
import SimpleDownloader as downloader
import remove_accents
import autorun
import datetime as dt, time

downloader = downloader.SimpleDownloader()

reload(sys);
sys.setdefaultencoding("utf8")

HANDLE = int(sys.argv[1])

CURRENT_PATH = ADDON.getAddonInfo("path")
PROFILE_PATH = xbmc.translatePath(ADDON_PROFILE).decode("utf-8")

VERSION = ADDON.getAddonInfo("version")
USER = ADDON.getSetting('user_id')
USER_PIN_CODE = ADDON.getSetting('user_pin_code')
USER_VIP_CODE = ADDON.getSetting('user_vip_code')
LOCK_PIN = ADDON.getSetting('lock_pin')
VIEWMODE = ADDON.getSetting('view_mode')



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
                'X-User-VIP'    : USER_VIP_CODE,
                'X-Platform'    : PLATFORM,
              }
  try:
    req = urllib2.Request(url,headers=headers)
    f = urllib2.urlopen(req)
    body=f.read()

    return json.loads(body)
  except:
    pass

def hello():
	
	date = dt.date.today().strftime("%d/%m/%Y")
	day = dt.datetime.now().strftime("%A")

	filename = os.path.join(PROFILE_PATH, 'date.dat' )
	if not os.path.exists(filename):
		with open(filename,"w") as f:
			f.write(date)
		if 'Saturday' in day:
				notify('Xin chúc bạn ngày cuối tuần vui vẻ.')
		else:
				notify('Xin chúc bạn có thời gian giải trí vui vẻ.')	
		
	with open(filename,"r") as f:
		lines = f.read()
	if date not in lines:
		if 'Saturday' in day or 'Sunday' in day:
			notify('Xin chúc bạn ngày cuối tuần vui vẻ.')
		else:
			notify('Xin chúc bạn có thời gian giải trí vui vẻ.')	
		with open(filename,"w") as f:
			f.write(date)
 

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

def add_lock_dir(item_path):
  item_path = re.sub('&d=__.*__','',item_path)
  filename = os.path.join(PROFILE_PATH, 'lock_dir.dat' )
  with open(filename,"a+") as f:
    f.write(item_path + "\n")
  notify('Đã khoá thành công')

def remove_lock_dir(item_path):
  filename = os.path.join(PROFILE_PATH, 'lock_dir.dat' )
  if not os.path.exists(filename):
    return
  dialog = xbmcgui.Dialog()
  result = dialog.input('Nhập mã khoá', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
  if len(result) == 0 or result != LOCK_PIN:
    notify('Sai mật mã, vui lòng nhập lại')
    return
  item_path = re.sub('&d=__.*__','',item_path)
  
  with open(filename,"r") as f:
    lines = f.readlines()
  with open(filename,"w") as f:
    for line in lines:
      if line!=item_path + "\n":
        f.write(line)
  notify('Đã mở khoá thành công')

def check_lock(item_path):
  filename = os.path.join(PROFILE_PATH, 'lock_dir.dat' )
  if not os.path.exists(filename):
    return False
  with open(filename,"r") as f:
    lines = f.readlines()
  return (item_path + "\n") in lines

def play(data):
  link = data["url"]
  link = getlink.get(link)
  if link is None or len(link) == 0:
    notify('Lỗi không lấy được link phim. Xin vui lòng thử lại sau.')
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
      xbmc.Player().setSubtitles(subfile.bak)#disable sub
      #notify('Tải phụ đề thành công')
    except:
      notify#('Không tải được phụ đề phim.')

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
  if '__download__' in url:
    download(url)
    return
  if '__lock__' in url:
    add_lock_dir(url)
    return
  if '__unlock__' in url:
    remove_lock_dir(url)
    return
  if check_lock(url):
    dialog = xbmcgui.Dialog()
    result = dialog.input('Nhập mã khoá', type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)
    if len(result) == 0 or result != LOCK_PIN:
      notify('Sai mật mã, vui lòng nhập lại')
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

  if not data.get("items"):
    return
    
  if data.get("content_type") and len(data["content_type"]) > 0:
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_UNSORTED)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_DATE)
    xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_GENRE)
    xbmcplugin.setContent(HANDLE, data["content_type"])

  listitems = range(len(data["items"]))
  for i, item in enumerate(data["items"]):
      lock_url = item["path"].replace("plugin://%s" % ADDON_ID, VIETMEDIA_HOST )
      lock_url = re.sub('\?','/?',lock_url)
      label = item["label"]
      if check_lock(lock_url):
        label = "*" + label
      listItem = xbmcgui.ListItem(label=label, label2=item["label2"], iconImage=item["icon"], thumbnailImage=item["thumbnail"])
      if item.get("info"):
          listItem.setInfo("video", item["info"])
      if item.get("stream_info"):
          for type_, values in item["stream_info"].items():
              listItem.addStreamInfo(type_, values)
      if item.get("art"):
          listItem.setArt(item["art"])
      
      menu_context = []
      if item.get("context_menu"):
          listItem.addContextMenuItems(item["context_menu"])
      elif item["is_playable"] == True:
          
          title = item["label"]
          title = re.sub('\[.*?]','',title)
          title = re.sub('\s','-',title)
          title = re.sub('--','-',title)
          title = re.sub('--','-',title)
          title = re.sub('[\\\\/*?:"<>|#]',"",title)
          title = remove_accents.remove_accents(title)
          command = 'XBMC.RunPlugin(%s&d=__download__&file_name=%s)' % (item["path"], title)
          menu_context.append(( 'Download...', command, ))

      command = 'XBMC.RunPlugin(%s&d=__lock__)' % item["path"]
      menu_context.append(( 'Khoá mục này', command, ))
      command = 'XBMC.RunPlugin(%s&d=__unlock__)' % item["path"]
      menu_context.append(( 'Mở khoá mục này', command, ))
      listItem.addContextMenuItems( menu_context )

      listItem.setProperty("isPlayable", item["is_playable"] and "true" or "false")
      if item.get("properties"):
          for k, v in item["properties"].items():
              listItem.setProperty(k, v)
      listitems[i] = (item["path"], listItem, not item["is_playable"])

  xbmcplugin.addDirectoryItems(HANDLE, listitems, totalItems=len(listitems))
  
  if VIEWMODE == 'true':
	  if '?action=menu' in url or 'node_id=77' in url or 'node_id=86' in url or 'node_id=79' in url or 'thread_id=18666' in url or 'thread_id=15858' in url or 'thread_id=21762' in url or 'thread_id=21802' in url or 'thread_id=15492' in url or 'thread_id=104' in url or 'node_id=13' in url or 'node_id=19' in url:
		xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
  
  
  hello()
  
  xbmcplugin.endOfDirectory(HANDLE, succeeded=True, updateListing=False, cacheToDisc=True)

def download(url):
  dialog = xbmcgui.Dialog()
  download_path = dialog.browse(3, 'XBMC', 'files')
  if len(download_path) > 0:
    xbmc.log(url)
    data = fetch_data(url)
    if not data:
      return
    if data.get('error'):
      alert(data['error'])
      return
    
    if data.get("url"):
      link = data["url"]
      link = getlink.get(link)
      if link is None or len(link) == 0:
        notify('Lỗi không lấy được link phim.')
        return
      match = re.search(r'file_name=(.*?)$', url)
      file_name = match.group(1) + ".mkv"
      params = { "url": link, "download_path": download_path }
      downloader.download(file_name, params)

go()

