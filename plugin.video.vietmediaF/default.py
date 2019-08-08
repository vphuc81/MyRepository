# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/kodivietnam/

import urllib,urllib2,re
import os
import xbmc,xbmcplugin,xbmcgui,xbmcaddon
import getlink
import urlfetch
import simplejson as json
from config import VIETMEDIA_HOST
from addon import alert, notify, notify1, TextBoxes, ADDON, ADDON_ID, ADDON_PROFILE, LOG, PROFILE
from platform import PLATFORM
from getlink import debug
from getlink import writesub
import uuid
#import SimpleDownloader as downloader
import plugintools as downloader
import remove_accents
import vmfdecode as vmf
import autorun
import datetime as dt, time
import xbmcvfs, shutil, zipfile, requests


#downloader = downloader.SimpleDownloader()

reload(sys);
sys.setdefaultencoding("utf8")

HANDLE = int(sys.argv[1])

CURRENT_PATH = ADDON.getAddonInfo("path")
PROFILE_PATH = xbmc.translatePath(ADDON_PROFILE).decode("utf-8")
VERSION = ADDON.getAddonInfo("version")
USER = ADDON.getSetting('user_id')
ADDON_NAME = ADDON.getAddonInfo("name")
USER_PIN_CODE = ADDON.getSetting('user_pin_code')
USER_VIP_CODE = ADDON.getSetting('user_vip_code')
LOCK_PIN = ADDON.getSetting('lock_pin')
VIEWMODE = ADDON.getSetting('view_mode')
VIEWXXX = ADDON.getSetting('view_xxx')
DOWNLOAD_PATH = ADDON.getSetting("download_path")
DOWNLOAD_SUB = ADDON.getSetting("download_sub")
DIALOG = xbmcgui.Dialog()
vDialog = xbmcgui.DialogProgress()
HOME = xbmc.translatePath('special://home/')
USERDATA = os.path.join(xbmc.translatePath('special://home/'), 'userdata')
ADDONDATA = os.path.join(USERDATA, 'addon_data', ADDON_ID)
CHECK = ADDON.getSetting("check")


#subsence
from CloudflareScraper import get_cookie_string
cookie_value_subsence = ADDON.getSetting(id='subscene_cookie_value')
user_agent = ADDON.getSetting(id='subscene_user_agent')
cookie_time = ADDON.getSetting(id='subscene_user_time')
current_time = int(time.time())

#
pathTOaddon = os.path.join(xbmc.translatePath('special://home/addons'), 'plugin.video.sendtokodi')
if not os.path.exists(pathTOaddon)==True:
	xbmc.executebuiltin('InstallAddon(%s)' % ('plugin.video.sendtokodi'))
	xbmc.executebuiltin('SendClick(11)'), time.sleep(2)
else:
	pass
'''
pathTOaddon = os.path.join(xbmc.translatePath('special://home/addons'), 'plugin.googledrive')
if not os.path.exists(pathTOaddon)==True:
	
	xbmc.executebuiltin('InstallAddon(%s)' % ('plugin.googledrive'))
	xbmc.executebuiltin('SendClick(11)'), time.sleep(2)
	
else:
	pass

'''

def urlencode(url):
	if sys.version_info < (3, 0):
		import urllib
		urllib.quote_plus(url)
	else:
		import urllib.parse
		urllib.parse.quote_plus(url)
	return url
def get_Setting():
	if not os.path.exists(PROFILE_PATH):
		os.makedirs(PROFILE_PATH)
	try:
		if CHECK=="false":
			#notify('Thiết lập Setting cho lần đầu sử dụng')
			choice = DIALOG.yesno("Thông báo trách nhiệm","Sử dụng Addon là bạn hiểu là [COLOR yellow]VietmediaF[/COLOR] chỉ thu thập và tìm kiếm các nguồn dữ liệu từ các website không thuộc sở hữu của [COLOR yellow]VietmediaF[/COLOR]. Vietmediaf cũng không sử hữu bất kì nội dung nào trong addon này.", nolabel='Tôi sẽ thoát ra', yeslabel='Đồng ý và sử dụng')
			if choice:
				addon = xbmcaddon.Addon()
				addon.setSetting(id='check', value="true")
			
				
	except:
		pass		
		
get_Setting()

def get_notif():
	NOTIF = ADDON.getSetting("notif")
	try:
		response = urlfetch.get('http://repo.kodi.vn/Phude/notif.txt')
		check = re.search(r"(\d+)-", response.body).group(1)
		notif1 = re.search(r"-(.+)", response.body).group(1)
		if NOTIF == check:
			#TextBoxes('VietmediaF thông báo', notif1)
			xbmc.log('No notif')	
		else:
			TextBoxes('VietmediaF thông báo', notif1)
			addon = xbmcaddon.Addon()
			addon.setSetting(id='notif', value=check)
			pass		
	except:
		pass


def fetch_data(url, headers=None):
	visitor = get_visitor()
	if headers is None:
		headers = { 
                'User-agent'    : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
                'Referers'      : 'http://www.google.com',
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
	if not os.path.exists(PROFILE_PATH):
		os.makedirs(PROFILE_PATH)
	filename = os.path.join(PROFILE_PATH, 'date.dat' )
	if not os.path.exists(filename):
		with open(filename,"w") as f:
			f.write(date)
	else:	
		with open(filename,"r") as f:
			lines = f.read()
		if date not in lines:
			with open(filename,"w") as f:
				f.write(date)
				get_notif()
			headers = {'X-User-VIP':  USER_VIP_CODE}
			r = fetch_data(VIETMEDIA_HOST+'/?action=CVMF')
			if not r:
				notify('[COLOR yellow]VMF cần donation để duy trì chi phí. Vui lòng ủng hộ[/COLOR]')
				return
			if r.get('error'):
				t = r.get('error')
				if t == 'e':
					notify('[COLOR yellow]VMF cần donation để duy trì chi phí. Vui lòng ủng hộ[/COLOR]')
				elif t == '1':
					notify('[COLOR yellow]VMF sắp hết hạn. Vui lòng ủng hộ[/COLOR]')
				else:
					notify('VMF code: '+r['error']+' ngày hiệu lực')
		return
			

def de(text):
	filename = os.path.join(PROFILE_PATH, 'debug.dat' )
	if not os.path.exists(filename):
		with open(filename,"w+") as f:
			f.write("DEBUG VMF")
	else:
		with open(filename,"r+") as f:
			f.write(text)

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
		
def openURL(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
	
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
def check_fshare():
	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')
	filename = os.path.join(PROFILE_PATH, 'vmfcookie.dat')
	if os.path.exists(filename):
		with open(filename,"r") as f:
			t=f.read()
			cookie,csrf=t.split('|')
			profile_url='https://118.69.164.19/account/profile'
			headers = {
				'Host': 'www.fshare.vn',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Language': 'en-US,en;q=0.5',
				'Referer': 'https://www.fshare.vn/',
				'Cookie': cookie,
				'X-CSRF-Token': csrf,
				'X-Requested-With': 'XMLHttpRequest',
				}
			r=urlfetch.get(profile_url,headers=headers)
			match = re.search(r"<span class=\"bt-vip\">(.+?)<\/span>",r.body)
			acc_type = match.group(1)
			
	#TextBoxes('Trạng thái tài khoản fshare', info)
	
		
def check_lock_tmp(item_path):
	filename = os.path.join(PROFILE_PATH, 'lock_temp.dat' )
	if not os.path.exists(filename):
		return False
	with open(filename,"r") as f:
		lines = f.readlines()
	return (item_path + "\n") in lines
def check_lock(item_path):
	filename = os.path.join(PROFILE_PATH, 'lock_dir.dat' )
	if not os.path.exists(filename):
		return False
	with open(filename,"r") as f:
		lines = f.readlines()
	return (item_path + "\n") in lines
#Thanks to Felv for these codes
def clearCache():
	PROFILEADDONDATA = os.path.join(PROFILE,'addon_data')
	cachelist = [
		(PROFILEADDONDATA),
		(ADDONDATA),
		(os.path.join(HOME,'cache')),
		(os.path.join(HOME,'temp')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')),
		(os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')),
		(os.path.join(ADDONDATA,'script.module.simple.downloader')),
		(os.path.join(PROFILEADDONDATA,'script.module.simple.downloader'))]
		
	delfiles = 0

	for item in cachelist:
		if os.path.exists(item) and not item in [ADDONDATA, PROFILEADDONDATA]:
			for root, dirs, files in os.walk(item):
				file_count = 0
				file_count += len(files)
				if file_count > 0:
					for f in files:
						if not f in ['kodi.log', 'tvmc.log', 'spmc.log', 'xbmc.log']:
							try:
								os.unlink(os.path.join(root, f))
							except:
								pass
						else: xbmc.log('Ignore Log File: %s' % f)
					for d in dirs:
						try:
							shutil.rmtree(os.path.join(root, d))
							delfiles += 1
							
						except:
							xbmc.log("[Failed] to wipe cache in: %s" % os.path.join(item,d))
		else:
			for root, dirs, files in os.walk(item):
				for d in dirs:
					if 'cache' in d.lower():
						try:
							shutil.rmtree(os.path.join(root, d))
							delfiles += 1
							xbmc.log("[Success] wiped %s " % os.path.join(item,d))
						except:
							xbmc.log("[Failed] to wipe cache in: %s" % os.path.join(item,d))

	notify(ADDON_NAME,'Done.')	

def install_repo(url):
	#notify('Chuẩn bị cài đặt repo')
	xbmc_temp = xbmc.translatePath('special://temp')
	addons_folder = xbmc.translatePath('special://home/addons')
	tempdir = os.path.join(xbmc_temp, 'addonVMF')
	vDialog.create('Vietmediaf','Bắt đầu cài đặt xin vui lòng đợi trong giây lát.','Downloading...')
	if not os.path.exists(tempdir):
		try:
			xbmcvfs.mkdirs(tempdir)
			time.sleep(20)
		except:pass
	
	
	useragent = ("User-Agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) "
					   "Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)")
	headers = {'User-Agent': useragent, 'Referer': url}
	local_tmp_file = os.path.join(tempdir, "addon.zip")
	
	try:
		if os.path.exists(local_tmp_file):
			os.remove(local_tmp_file)
		request = urllib2.Request(url, '', headers)
		response = urllib2.urlopen(request)
		local_file_handle = xbmcvfs.File(local_tmp_file, "wb")
		local_file_handle.write(response.read())
		xbmc.sleep(500)
		local_file_handle.close()
	except:
		notify('Không tải được addon')
				
	
	xbmc.executebuiltin('XBMC.Extract("%s","%s")' % (local_tmp_file, addons_folder))
	xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
	xbmc.executebuiltin("XBMC.UpdateAddonRepos()")
	vDialog.close()
	notify('Đã cài xong')
	

def log_check():
	ret = False
	if os.path.exists(os.path.join(LOG,'xbmc.log')):
		ret = os.path.join(LOG,'xbmc.log')
	elif os.path.exists(os.path.join(LOG,'kodi.log')):
		ret = os.path.join(LOG,'kodi.log')
	elif os.path.exists(os.path.join(LOG,'spmc.log')):
		ret = os.path.join(LOG,'spmc.log')
	elif os.path.exists(os.path.join(LOG,'tvmc.log')):
		ret = os.path.join(LOG,'tvmc.log')
	return ret

def viewLogFile():
	log     = log_check()
	logtype = log.replace(LOG,"")
	if os.path.exists(log) or not log == False:
		f = open(log,mode='r'); msg = f.read(); f.close()
		TextBoxes("%s - %s" % (ADDON_NAME, logtype), msg)
	else: 
		notify('Không tìm thấy file log.')

	
def tut1():
	url = 'http://textuploader.com/dd4ds/raw'
	content = openURL(url)
	TextBoxes(ADDON_NAME, content)
def cloudfare(url):
    import cfscrape
    scraper = cfscrape.create_scraper()
    user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
    cookie, user_agent = cfscrape.get_tokens(url,user_agent)
    cookie = json.dumps(cookie)
    jstr = json.loads(cookie)
    jstr['cf_clearance']
    cf_clearance = jstr['cf_clearance']
    __cfduid = jstr['__cfduid']
    cookie = 'cf_clearance='+cf_clearance+'; __cfduid='+__cfduid
    return(cookie)
def curL(url):
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','referer': url,'cookie': cloudfare(url)}
	r = urlfetch.get(url,headers=headers)
	return (r.body)
def DownloadFile(subpath,tempdir):
    tmp_file = os.path.join(tempdir, "phude.zip")
    r = s.get(subpath,headers=headers,verify=False)
    f = open(tmp_file, 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024): 
        if chunk:
            f.write(chunk)
    f.close()
    notify("OK")
    return 

def get_new_cloudflare_token():
    global cookie_value_subsence, user_agent
    cookie_value_subsence, user_agent = get_cookie_string("https://subscene.com")
    ADDON.setSetting(id='subscene_cookie_value', value=cookie_value_subsence)
    ADDON.setSetting(id='subscene_user_agent', value=user_agent)
    ADDON.setSetting(id='subscene_user_time', value=str(current_time))



def download_sub(subtitle,tempdir):
	if 'subscene.com' in subtitle:
		if cookie_value_subsence == "":
			get_new_cloudflare_token()
		headers = {'User-Agent': user_agent, 'Referer': subtitle, 'Cookie': cookie_value_subsence}
		#de(cookie_value_subsence)
		response = requests.get(subtitle, headers=headers,verify=False)
		sub = re.search(r'<a href=\"(/subtitles/vietnamese.*?)\"', response.text)
		sub = sub.group(1)
		subpath = "https://subscene.com" + sub
		
	if 'phudeviet.org' in subtitle:
		f = urlfetch.get(subtitle)
		match = re.search(r"(http://phudeviet.org/download/.+?html)", f.body)
		subpath = match.group(1)
		f = urlfetch.get(subpath)
		subpath = f.getheader('location')
		useragent = ("User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
		headers = {'User-Agent': useragent, 'Referer': subtitle}
		
	if not os.path.exists(tempdir):
		try:
			xbmcvfs.mkdirs(tempdir)
			time.sleep(20)
		except:pass
	else:
		for root, dirs, files in os.walk(tempdir, topdown=False):
			for name in files:
				try:os.remove(os.path.join(root, name))
				except:pass
			for name in dirs:
				try:os.rmdir(os.path.join(root, name))
				except:pass
	
	
	tmp_file = os.path.join(tempdir, "phude.zip")
	
	try:
		if os.path.exists(tmp_file):
			os.remove(tmp_file)
		tmp_file = os.path.join(tempdir, "phude.zip")
		if "subscene" in subpath:
			headers = {'User-Agent': user_agent, 'Referer': subtitle, 'Cookie': cookie_value_subsence}
		r = requests.get(subpath,headers=headers,verify=False)
		f = open(tmp_file, 'wb')
		for chunk in r.iter_content(chunk_size=512 * 1024):
                        if chunk:
                                f.write(chunk)
                f.close()
		import zipfile
		fantasy_zip = zipfile.ZipFile(tmp_file)
		fantasy_zip.extractall(tempdir)
		fantasy_zip.close()
		notify("Đã tải được phụ đề")
		
		
	except:
		notify('Không tải được phụ đề')
		pass
	

def list_item(data):
	
	if data.get("content_type") and len(data["content_type"]) > 0:
					
		xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_UNSORTED)
		xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
		xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_DATE)
		xbmcplugin.addSortMethod(HANDLE, xbmcplugin.SORT_METHOD_GENRE)
		xbmcplugin.setContent(HANDLE, data["content_type"])

	listitems = range(len(data["items"]))
	for i, item in enumerate(data["items"]):
		lock_url = item["path"]
		lock_url = re.sub('\?','/?',lock_url)
		path = item["path"]
		label = item["label"]
		label = label.replace("@","")
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
			#command = 'XBMC.RunPlugin(%s&d=__subtitle__&file_name=%s)' % (item["path"], title)
			#menu_context.append(( 'Tải phụ đề', command, ))
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
		listitems[i] = (path, listItem, not item["is_playable"])

	xbmcplugin.addDirectoryItems(HANDLE, listitems, totalItems=len(listitems))
	xbmcplugin.endOfDirectory(HANDLE, succeeded=True, updateListing=False, cacheToDisc=True)

def play_file():
	keyboardHandle = xbmc.Keyboard('','[COLOR yellow]Nhập link Folder hoặc File Fshare của bạn:[/COLOR] [I]Nhập ID của Fshare[/I]')
	keyboardHandle.doModal()
	if (keyboardHandle.isConfirmed()):
		queryText = keyboardHandle.getText()
		if len(queryText) == 0:
			sys.exit()
		if "fshare.vn" in queryText:
			url_input = queryText.replace("http://","https://")
			if 'token' in url_input:
				match = re.search(r"(\?.+?\d+)",url_input)
				_token = match.group(1)
				url_input = url_input.replace(_token,'')
			if not 'https' in url_input:
				url_input = url_input.replace('http','https')
				fshare_id = re.search(r"file\/(.+)",url_input).group(1)
				url_input = 'https://www.fshare.vn/file/%s' % fshare_id	
				
		else:
			#check if Fshare id
			queryText = queryText.upper()
			url_input = 'https://www.fshare.vn/file/'+queryText
		
		
		#Check status of link
		url_input = url_input.strip()
		if 'fshare' in url_input:
			if 'folder' in url_input:
				regex = r"folder\/(.+)"
			else:
				regex = r"file\/(.+)"
			match = re.search(regex,url_input)
			f_id = match.group(1)
			file_type,name = getlink.check_file_info(url_input)
			#Identify link type
			if file_type == '0':
				file = 'plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/folder/'+f_id
				playable = False
				
			elif file_type == '1':
				file = 'plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/file/'+f_id
				playable = True
				
			elif file_type == '2':
				alert("File bạn nhập không có thực or đã bị xoá")
				return
		else: file = url_input
		#Content to play
		items = []
		item = {}
		item["label"] = '[COLOR yellow]%s[/COLOR]' % name
		item["is_playable"] = playable
		item["path"] = file
		item["thumbnail"] = ''
		item["icon"] = ""
		item["label2"] = ""
		item["info"] = {'plot': ''}
		items = [item]
		data = {"content_type": "episodes","items":""}
		data.update({"items":items})
		return json.dumps(data)
	
def fshare_favourite(url):
	import requests
	try:
		getlink.checkAccFshare()
		token = ADDON.getSetting('tokenfshare')
		session_id = ADDON.getSetting('sessionfshare')
		
	except: 
		token,session_id = getlink.login_f()
		
	header = {'Cookie' : 'session_id=' + session_id}
	
	r = requests.get(url,headers=header,verify=False)
	f_items = json.loads(r.content)
	items = []
	for i in f_items:
		item = {}
        #value[i] = {'info': {'plot': ''}, 'label2': '', 'is_playable': playable, 'label': name, 'path': link, 'thumbnail': '', 'icon': ''}
		name = i["name"]
		linkcode = i["linkcode"]
		type_f = i["type"]
		if type_f == '0':
			link = ('plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/folder/%s' % linkcode)
			playable = False
		else:
			link = ('plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/file/%s' % linkcode)
			playable = True
		item["label"] = name
		item["is_playable"] = playable
		item["path"] = link
		item["thumbnail"] = ''
		item["icon"] = ""
		item["label2"] = ""
		item["info"] = {'plot': ''}
		items += [item]
		
		
	data = {"content_type": "episodes","items":""}
	data.update({"items":items})
	
	return json.dumps(data)
def list_link(url_input):
	import requests
	useragent = ("User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
	headers = {'User-Agent': useragent}
	lines = requests.get(url_input,headers,verify=False)
	lines = lines.content.split('*')
	t = len(lines)
	items = []
	name = ''
	h = ''

	for i in range(1,t): 
		item = {}
		line = (lines[i])
		line = line.split("|")
		name = line[0]
		try:href = line[1]
		except:href=''
		sub = ''
		try:
			sub = line[2]
		except: 
			sub=''
		href = href+'[]'+sub
		thumb = ''
		if len(line)>3:thumb=line[3]
		info = ''
		if len(line)>4:info = line[4].strip()
		
		name = urllib.unquote_plus(name)
		if '@' in name or 'folder' in href: 
			playable = False
			link = 'plugin://plugin.video.vietmediaF?action=play&url=%s' % href
		else:    
			playable = True
			link = 'plugin://plugin.video.vietmediaF?action=play&url=%s' % href

		#Content of file
		item["label"] = name
		item["is_playable"] = playable
		item["path"] = link
		item["thumbnail"] = thumb
		item["icon"] = ""
		item["label2"] = ""
		item["info"] = {'plot': info}
		items += [item]
	data = {"content_type": "episodes","items":""}
	data.update({"items":items})
	return data
def fshare_folder(url):
	url = urllib.unquote_plus(url)
	if 'token' in url:
		match = re.search(r"(\?.+?\d+)",url)
		_token = match.group(1)
		url = url.replace(_token,'')
		
	vDialog.create('VIETMEDIAF','Đang lên danh sách. Vui lòng đợi.')
	if 'fshare.vn/folder' in url:
		match = re.search(r"folder\/(.+)",url)
		folder_id = match.group(1)
		url = 'https://www.fshare.vn/api/v3/files/folder?sort=type,-modified&page=1&per-page=50&linkcode=%s' % folder_id
		url = 'https://murmuring-fortress-18529.herokuapp.com/curl.php?url=%s' % urllib.quote_plus(url)
		
	r = requests.get(url)
	
	f_items = json.loads(r.content)
	f_item = f_items['items']
	items = []
	for i in f_item:
		item = {}
		name = i['name']
		linkcode = i["linkcode"]
		type_f = i["type"]
		if '0' in str(type_f):
			link = ('plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/folder/%s' % linkcode)
			playable = False
		else:
			link = ('plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/file/%s' % linkcode)
			playable = True
		item["label"] = name
		item["is_playable"] = playable
		item["path"] = link
		item["thumbnail"] = 'https://i.imgur.com/8wyaJKv.png'
		item["icon"] = ""
		item["label2"] = ""
		item["info"] = {'plot': ''}
		items += [item]
	#Generate nextpage
	try:
		
		nextpage_url = f_items["_links"]["next"]
		nextpage_url = "https://www.fshare.vn/api"+nextpage_url
		nextpage_url = "plugin://plugin.video.vietmediaF?action=play&url="+urllib.quote_plus(nextpage_url)
		nextpage = {"label":'[COLOR yellow]Next Page[/COLOR]',"is_playable":False,"path":nextpage_url,"thumbnail":'',"icon":"","label2":"","info":{'plot': ''}}
		items.append(nextpage)
	except: items=items
	
	data = {"content_type": "episodes","items":""}
	data.update({"items":items})
	vDialog.close()
	return data
	
def play(data):
	link = data["url"]
	
	if link is None or len(link) == 0:
		notify('Không lấy được link')
		return
	if 'PIC' in link:
		imgSrc = link.replace('PIC','')	
		xbmc.executebuiltin('ShowPicture('+imgSrc+')')
		return
	if 'DONATION' in link:
		r=urlfetch.get('http://repo.kodi.vn/Phude/Donation.txt')
		TextBoxes(ADDON_NAME, r.body)
		return
	if 'textbox' in link or 'Textbox' in link:
		url1 = str(link).replace("textbox", "")
		content = openURL(url1)
		TextBoxes(ADDON_NAME, content)
		return
	if 'text' in link or 'Text' in link:
		content = str(link).replace("text", "")
		TextBoxes(ADDON_NAME, content)
		return
	if 'thongbao' in link:
		if 'thongbao1' in link:
			alert (u'Thông báo của VMF'.encode("utf-8"))
			return
		if 'thongbao2' in link:
			alert (u'Trang nguồn có sự thay đổi. Thông báo cho admin để xử lý.'.encode("utf-8"))
			return
		if 'thongbao3' in link:
			alert (u'Đang xử lý. Xem lại sau.'.encode("utf-8"))
			return
		if 'thongbao4' in link:
			tb = link.replace('thongbao4-', '')
			alert (tb)
			return		
	
	else: 
		link = getlink.get(link)
		
		if not link:
			alert("Không lấy được link. Thử lại sau.")
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
			
			if "phudeviet.org" in subtitle:
				xbmc_temp = xbmc.translatePath('special://temp')
				tempdir = os.path.join(xbmc_temp, 'phudeVMF')
				download_sub(subtitle,tempdir)
				tmp_file = os.path.join(tempdir, "phude.zip")
				xbmc.executebuiltin('XBMC.Extract("%s","%s")' % (tmp_file, tempdir))
				exts = [".srt", ".sub", ".txt", ".smi", ".ssa", ".ass"]
				sub_temp = os.path.join(tempdir, "sub.srt")
				for file in xbmcvfs.listdir(tempdir)[1]:
					if os.path.splitext(file)[1] in exts:
						sub_file = os.path.join(tempdir, file)
						xbmcvfs.rename(sub_file, sub_temp)
				xbmc.Player().setSubtitles(tmp_file)
			elif "subscene.com" in subtitle:
				xbmc_temp = xbmc.translatePath('special://temp')
				tempdir = os.path.join(xbmc_temp, 'phudeVMF')
				download_sub(subtitle,tempdir)
				exts = [".srt", ".sub", ".txt", ".smi", ".ssa", ".ass"]
				sub_temp = os.path.join(tempdir, "sub.srt")
				for file in xbmcvfs.listdir(tempdir)[1]:
					if os.path.splitext(file)[1] in exts:
						sub_file = os.path.join(tempdir, file)
						xbmcvfs.rename(sub_file, sub_temp)
				xbmc.Player().setSubtitles(sub_temp)
			elif "fcine.net" in subtitle:
				
				xbmc_temp = xbmc.translatePath('special://temp')
				tempdir = os.path.join(xbmc_temp, 'phudeVMF')
				if not os.path.exists(tempdir):
					try:
						xbmcvfs.mkdirs(tempdir)
						time.sleep(20)
					except:pass
				else:
					for root, dirs, files in os.walk(tempdir, topdown=False):
						for name in files:
							try:os.remove(os.path.join(root, name))
							except:pass
						for name in dirs:
							try:os.rmdir(os.path.join(root, name))
							except:pass
				
				useragent = ("User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
				headers = {'User-Agent': useragent, 'Referer': 'fcine.net','cookie': getlink.cloudfare(subtitle)}
				tmp_file = os.path.join(tempdir, "phude.srt")
				
				try:
					if os.path.exists(tmp_file):
						os.remove(tmp_file)
					r = requests.get(subtitle,headers,verify=False)
					debug(r.content)
					writesub(r.content)
					xbmc.sleep(500)
					notify("Đã tải được phụ đề.")
				except:
					notify('Không tải được phụ đề')
					return
				filename = os.path.join(PROFILE_PATH, 'phude.srt' )
				xbmc.Player().setSubtitles(filename)
				
			else:
				
				useragent = ("User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0")
				headers = {'User-Agent': useragent}
				xbmc_temp = xbmc.translatePath('special://temp')
				tempdir = os.path.join(xbmc_temp, 'phudeVMF')
				tmp_file = os.path.join(tempdir, "phude.srt")
				try:
					try:
						request = urllib2.Request(subtitle, '', headers)
						r = urllib2.urlopen(request)
						writesub(r.content)
					except:
						r = requests.get(subtitle,headers,verify=False)
						writesub(r.content)
					xbmc.sleep(500)
					notify("Đã tải được phụ đề.")
				except:
					notify('Không tải được phụ đề')
					return
				filename = os.path.join(PROFILE_PATH, 'phude.srt' )
				xbmc.Player().setSubtitles(filename)
				#xbmc.Player().setSubtitles(tmp_file)
				

def go():
  
	url = sys.argv[0].replace("plugin://%s" % ADDON_ID, VIETMEDIA_HOST ) + sys.argv[2]
  
	if url == VIETMEDIA_HOST + '/':
		url += '?action=menu'
	
	#Settings
	if '_debug_' in url:
		xbmc.executebuiltin('RunAddon("script.kodi.loguploader")')
		return
	if '_dellink_' in url:
		filename = os.path.join(PROFILE_PATH, 'yourlink.dat' )
		if not os.path.exists(filename):
			notify('Bạn chưa có link nào được lưu.')
		else:
			with open(filename,"w") as f:
				lines = f.write('')
				notify('Done')
		return
	if '_number_' in url:
		import requests
		keyboardHandle = xbmc.Keyboard('','Nhập ID rút gọn của bạn tại http://gg.gg')
		keyboardHandle.doModal()
		if (keyboardHandle.isConfirmed()):
			queryText = keyboardHandle.getText()
			if len(queryText) == 0:
				sys.exit()
			
			string = queryText.strip()
			string = string.replace('http://gg.gg/','')
			url = 'http://gg.gg/%s' % string
			try:
				r = requests.get(url)
			except:pass
			url_input = r.url
			url_input = url_input.strip()
			url_input = url_input.replace("http://","https://")
			
			#Check embed substitle
			url_input = url_input.replace("-","[]")
			url_input = url_input.replace("&","[]")
			url_input = url_input.replace("+","[]")
			links = url_input.split('[]')
			if len(links) == 2:
				url_input = links[0]
				subs = links[1]
			else: subs = ''			
			if 'fshare.vn' in url_input:file_type,name = getlink.check_file_info(url_input)
			elif 'drive.google.com' in url_input: 
				r = urlfetch.get(url_input)
				name = re.search(r"<meta itemprop=\"name\" content=\"(.+?)\"",r.content).group(1)
			else: name = "List to play"
			#save link to file 
			save_option = ADDON.getSetting('save_file')
			if save_option == "true":
				url = 'Name:'+urllib.quote_plus(name.encode("utf8"))+'Link:'+url_input
				#Generate file
				filename = os.path.join(PROFILE_PATH, 'yourlink.dat' )
				if not os.path.exists(filename):
					with open(filename,"w+") as f:
						f.write(url+'*')
						
				else:
					with open(filename,"r+") as f:
						lines = f.read()
						f.seek(0, 0) 
						f.write(url.rstrip('\r\n') +'*'+ lines)
						
				notify ('Đã lưu link của bạn.')
				
			#--
			if 'fshare' in url_input:
				if 'token' in url_input:
					match = re.search(r"(\?.+?\d+)",url_input)
					_token = match.group(1)
					url_input = url_input.replace(_token,'')
				if 'folder' in url_input:
					regex = r"folder\/(.+)"
				else:
					regex = r"file\/(.+)"
				match = re.search(regex,url_input)
				f_id = match.group(1)
				
				if "folder" in url_input:
					file = 'plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/folder/'+f_id
					playable = False
					if len(name) == 0:
						name = 'Folder to play'
					
				else:
					file = 'plugin://plugin.video.vietmediaF?action=play&url=https://www.fshare.vn/file/'+f_id+'[]'+subs
					playable = True
					if len(name) == 0:
						name = 'File to play'
				
			elif 'drive.google.com' in url_input:
				file = 'plugin://plugin.video.vietmediaF?action=play&url='+url_input
				playable = True
				#name = 'GDrive File to play'
				
			else:
				data = list_link(url_input)
				list_item(data)
				return
			#Content to play
			items = []
			item = {}
			item["label"] = '[COLOR yellow]%s[/COLOR]' % name
			item["is_playable"] = playable
			item["path"] = file
			item["thumbnail"] = ''
			item["icon"] = ""
			item["label2"] = ""
			item["info"] = {'plot': ''}
			items = [item]
			data = {"content_type": "episodes","items":""}
			data.update({"items":items})
			
			list_item(data)
			return
	if 'textbox' in url or 'Textbox' in url:
		url = url.replace(VIETMEDIA_HOST+'/?action=textbox&', '')
		
		url = urllib.unquote_plus(url)
		content = openURL(url)
		TextBoxes(ADDON_NAME, content)
		return
		
	if 'checkupdate' in url:
		notify('Bắt đầu kiểm tra')
		xbmc.executebuiltin('UpdateAddonRepos()')
		xbmc.executebuiltin('UpdateLocalAddons()')
		return
		
	if 'check_fshare' in url:
		#notify('đang check')
		check_fshare()
		return
	if 'addon' in url:
		url = url.replace(VIETMEDIA_HOST+'/?action=addon&', '')
		url=urllib.unquote(url)
		install_repo(url)
		return
		
	if 'clearCache' in url:
		clearCache()
		return
	if 'viewlog' in url:
		viewLogFile()
		return
	if '__settings__' in url:
		ADDON.openSettings()
		return
	if 'addon' in url:
		install_repo(url)
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
		
		match = re.search(r"file_name=(.+)",url)
		if match:
			name = match.group(1)
			
		else:name = "video.mkv"
		if 'fshare.vn' in url:
			match = re.search(r"url=(.+?)&",url)
			if match:
				link = match.group(1)
			
		else:link=url
		download(link,name)
		return
	if '__subtitle__' in url:
		
		match = re.search(r"file_name=(.+)",url)
		
		name = match.group(1)
		name = name.replace('.',' ')
		'''
		match = re.search(r"(.+?)__",url)
		url = match.group(1)
		r = fetch_data(url)
		video_url = r["url"]
		'''
		subtitle_searching(name)
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
	if 'account_fshare' in url:
		import requests
		token,session_id = getlink.login_f()
		header = {'Cookie' : 'session_id=' + session_id}
		r = requests.get('https://118.69.164.19/api/user/get',headers=header,verify=False)
		jstr = json.loads(r.content)
		point = jstr['totalpoints']
		mail = jstr['email']
		acc_type = jstr['account_type']
		webspace = float(jstr['webspace'])/float(1073741824)
		webspace_used = '{0:.2f}'.format(float(jstr['webspace_used'])/float(1073741824))
		line = 'E-mail: [COLOR yellow]%s[/COLOR] - ' % mail
		line += 'Loại tài khoản: [COLOR yellow]%s[/COLOR]\n' % acc_type
		line += 'Point: [COLOR yellow]%s[/COLOR]\n' % point
		line += 'Dung lượng tài khoản: [COLOR yellow]%s Gb[/COLOR] / ' % webspace
		line += 'Đã sử dụng [COLOR yellow]%s Gb[/COLOR]\n' % webspace_used
		alert(line,title='Fshare account')
		return
	elif 'play_file' in url:
		data = play_file()
		data = json.loads(data)
		list_item(data)
			
	elif 'add_file' in url:
		
		#Input link by user
		keyboardHandle = xbmc.Keyboard('','[COLOR yellow]Nhập link Folder hoặc File Fshare của bạn:[/COLOR] [I]Nhập ID của Fshare[/I]')
		keyboardHandle.doModal()
		if (keyboardHandle.isConfirmed()):
			queryText = keyboardHandle.getText()
			if len(queryText) == 0:
				sys.exit()
			if "fshare.vn" in queryText:
				url_input = queryText.replace("http://","https://")
				if 'token' in url_input:
					match = re.search(r"(\?.+?\d+)",url_input)
					_token = match.group(1)
					url_input = url_input.replace(_token,'')
					
			elif len(queryText) == 12 or len(queryText) == 15 :
				
				#check if Fshare id
				queryText = queryText.upper()
				url_input = 'https://www.fshare.vn/file/'+queryText
			else:url_input = queryText
			
			#Check status of link
			url_input = url_input.strip()
			if 'fshare' in url_input:
				if 'folder' in url_input:
					regex = r"folder\/(.+)"
				else:
					regex = r"file\/(.+)"
				match = re.search(regex,url_input)
				f_id = match.group(1)
				file_type, name = getlink.check_file_info(url_input)
				#Identify link type
				if file_type == '0':
					file = 'https://www.fshare.vn/folder/'+f_id
					
				elif file_type == '1':
					file = 'https://www.fshare.vn/file/'+f_id
					
				elif file_type == '2':
					alert("File bạn nhập không có thực")
					return
			else: file = url_input
					
			#file content
			url = 'Name:'+urllib.quote_plus(name.encode("utf8"))+'Link:'+file
			#Generate file
			filename = os.path.join(PROFILE_PATH, 'yourlink.dat' )
			if not os.path.exists(filename):
				with open(filename,"w+") as f:
					f.write(url+'*')
					
			else:
				with open(filename,"r+") as f:
					lines = f.read()
					f.seek(0, 0) 
					f.write(url.rstrip('\r\n') +'*'+ lines)
					
			notify ('Đã lưu link của bạn.')
			return
				
	elif 'load_file' in url:
		#Loading save file
		filename = os.path.join(PROFILE_PATH, 'yourlink.dat' )
		if not os.path.exists(filename):
			alert ('Bạn chưa có link lưu trữ. Xin vui lòng thêm link.')
		else:
			with open(filename,"r") as f:
				lines = f.read()
				lines = lines.rstrip('*')
				if str(len(lines))=='0':
					alert('Bạn chưa có link lưu trữ. Xin vui lòng thêm link.')
					return
				lines = lines.split('*')
				t = len(lines)
				
				items = []
				for i in range(0,t):
					item = {}
					line = (lines[i])
					link = re.search(r"Link:(.+)",line).group(1)
					name = re.search(r"Name:(.+?)Link",line).group(1)
					name = urllib.unquote_plus(name)
					if 'fshare' in link:
						if 'folder' in link: 
							playable = False
							link = 'plugin://plugin.video.vietmediaF?action=play&url=%s' % link
						elif 'file' in link: 
							playable = True
							link = 'plugin://plugin.video.vietmediaF?action=play&url=%s' % link
					else:
						playable = True
						link = link
					#Content of file
					item["label"] = name
					item["is_playable"] = playable
					item["path"] = link
					item["thumbnail"] = ''
					item["icon"] = ""
					item["label2"] = ""
					item["info"] = {'plot': ''}
					items += [item]
				data = {"content_type": "episodes","items":""}
				data.update({"items":items})
				list_item(data)
				
	elif 'home_fshare' in url:
		data = fshare_favourite('https://118.69.164.19/api/fileops/list?pageIndex=0&dirOnly=0&limit=60')
		data = json.loads(data)
		list_item(data)
		
	elif 'follow_fshare' in url:
		data = fshare_favourite('https://118.69.164.19/api/fileops/getListFollow')
		data = json.loads(data)
		list_item(data)
		
	elif 'folderxxx' in url:
		data = fshare_favourite('https://118.69.164.19/api/Fileops/ListFavorite')
		data = json.loads(data)
		list_item(data)
	
	elif 'fshare.vn/file/' in url or 'ok.ru' in url or 'drive.google.com' in url:
		regex = r"url=(.+)"
		match = re.search(regex,url)
		links = match.group(1)
		subtitle = ''
		links = links.split('[]')
		if len(links) == 2:
			subtitle = links[1]
		link = links[0]
		data = {"url":"","subtitle":""}
		data.update({"url":link,"subtitle":subtitle})
		play(data)
		
	elif 'fshare' in url and 'folder' in url:
		url = urllib.unquote_plus(url)
		regex = r"url=(.+)"
		match = re.search(regex,url)
		link = match.group(1)
		data = fshare_folder(link)
		list_item(data)
	elif 'VMF' in url and not 'action=fetch_espisode' in url:
		
		url = urllib.unquote_plus(url)
		url = url.replace('VMF-','')
		regex = r"url=(.+)"
		match = re.search(regex,url)
		links = match.group(1)
		data = list_link(links)
		list_item(data)
	else:
		
		data = fetch_data(url)
		
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
			path = item["path"]
			label = item["label"]
			filterStr = ["xxx","sex","jav","cap 3","18+","20+"]
			
			if check_lock(lock_url):
				label = "*" + label
			else:
				if VIEWXXX == 'false':
					label_ = label.lower()
					if '18+' in label_ or 'xxx' in label_ or 'cấp 3' in label or 'jav' in label_ or '+' in label_ or 'sex' in label_ or 'fuck' in label_:
						listItem = xbmcgui.ListItem(label='[I]Nội dung cần thiết lập để xem[/I]', label2='', iconImage='', thumbnailImage='')
						path = 'plugin://plugin.video.vietmediaF?action=browse&node_id=75'
					else:
						listItem = xbmcgui.ListItem(label=label, label2=item["label2"], iconImage=item["icon"], thumbnailImage=item["thumbnail"])
				if VIEWXXX == 'true':
					listItem = xbmcgui.ListItem(label=label, label2=item["label2"], iconImage=item["icon"], thumbnailImage=item["thumbnail"])
			if item.get("info"):
				listItem.setInfo("video", item["info"])
			if item.get("stream_info"):
				for type_, values in item["stream_info"].items():
					listItem.addStreamInfo(type_, values)
			if item.get("art"):
				listItem.setArt(item["art"])
			#context_menu
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
				command = 'XBMC.RunPlugin(%s&d=__subtitle__&file_name=%s)' % (item["path"], title)
				menu_context.append(( 'Tải phụ đề', command, ))
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
					
			listitems[i] = (path, listItem, not item["is_playable"])
			

		xbmcplugin.addDirectoryItems(HANDLE, listitems, totalItems=len(listitems))
	  
		if VIEWMODE == 'true':
			if '?action=menu' in url or 'node_id=77' in url or 'node_id=86' in url or 'node_id=79' in url or 'thread_id=18666' in url or 'thread_id=15858' in url or 'thread_id=21762' in url or 'thread_id=21802' in url or 'thread_id=15492' in url or 'thread_id=104' in url or 'node_id=13' in url or 'node_id=19' in url:
				xbmc.executebuiltin('Container.SetViewMode(%d)' % 500)
	  
		if 'node_id=75' in url:
			notify('Nội dung do người dùng chia sẻ. VietmediaF không chịu trách nhiệm.')
		
		#hello()
		
		xbmcplugin.endOfDirectory(HANDLE, succeeded=True, updateListing=False, cacheToDisc=True)
	
def subtitle_searching(name,video_url=None):
	if len(DOWNLOAD_SUB) == 0:
		alert("Nhập đường dẫn lưu trữ phụ đề trong mục Addon Setting. [COLOR yellow]Chú ý không chọn thư mục addon hay dữ liệu dễ bị xoá.[/COLOR]")
		xbmcaddon.Addon(id='plugin.video.vietmediaF').openSettings('download_sub')
	if len(DOWNLOAD_SUB) > 0:
		tempdir =DOWNLOAD_SUB
	#Confirm keyword to search
	name = name.replace("mkv",'')
	name = name.replace("mp4",'')
	name = name.replace("avi",'')
	name = name.replace("mov",'')
	name = name.replace("vob",'')
	name = name.replace("wmv",'')
	name = name.replace("-",' ')
	
	keyboardHandle = xbmc.Keyboard(name,'Xem lại keyword tìm kiếm cho phụ đề')
	keyboardHandle.doModal()
	if (keyboardHandle.isConfirmed()):
		name = keyboardHandle.getText()
		if len(name) == 0:
			return
		name = urlencode(name)
	else:
		return
	
	
	title_sub_title = ["[COLOR yellow]Tìm trên subscene[/COLOR]","Tìm trên phudeviet (Đang làm)","Tìm trên Fcine (Đang làm)"]
	title_sub_url = ["subscene.com","phudeviet.org","fcine.net"]
	dialog = xbmcgui.Dialog() 
	ret = dialog.select('Chọn server phụ đề', title_sub_title)
	if ret >=0:
		server_subtitle_url = title_sub_url[ret]
		#alert(server_subtitle_url)
		if "subscene" in server_subtitle_url:
			api_searching_subtile = 'https://subscene.com/subtitles/title?q=%s' % name
			api_searching_subtile = urlencode(api_searching_subtile)
			url = 'http://vietmediaf.net/subscene.php?type=list&url='+api_searching_subtile
			vDialog.create('Vietmediaf','Đang tìm kiếm phụ đề')
			r = urlfetch.get(url)
			jstr = json.loads(r.body)
			vDialog.close()
			t = len(jstr)
			if t > 0:
				sub_title = []
				sub_url = []
				
				for i in range(0,t):
					name_a = jstr[i]["name"]
					sub_title.append(name_a)
					url = jstr[i]["link"]
					sub_url.append(url)
					i = i + 1
					
				dialog = xbmcgui.Dialog() 
				ret_a = dialog.select('Chọn phụ đề cho [COLOR yellow]'+name+'[/COLOR]', sub_title)
				if ret_a >=0:
					phude_url = sub_url[ret_a]
					phude_url = urlencode(phude_url)
					
					phude_url = 'http://vietmediaf.net/subscene.php?type=list&url=%s' % phude_url
					xbmc.log(phude_url)
					vDialog.create('Vietmediaf','Lên danh sách phụ đề')
					r = urlfetch.get(phude_url)
					#Display body
					#TextBoxes("vmf",r.body)
					jstr_a = json.loads(r.body)
					
					vDialog.close()
					x = len(jstr_a)
					if x>0:
						sub_title_a = []
						sub_url_a = []
						for j in range(0,x):
							sub_name = jstr_a[j]["name"]
							sub_title_a.append(sub_name)
							sub_link = jstr_a[j]["link"]
							sub_url_a.append(sub_link)
							j=j+1
						dialog = xbmcgui.Dialog() 
						ret_b = dialog.select('Chọn phụ đề phim [COLOR yellow]'+name+'[/COLOR]', sub_title_a)
						if ret_b >=0:
							sub_link_a = sub_url_a[ret_b]
							download_sub(sub_link_a,tempdir)
							alert("Phụ đề đã được lưu tại [COLOR yellow]"+tempdir+" [/COLOR]. Dùng chức năng Browse subtitle để xem.")
							
					
					
				else: sys.exit()
			else:
				alert("Phụ đề chưa có")
		else:
			alert("Đang làm")
	
def download(url,file_name="video.mkv"):
  
	
	if len(DOWNLOAD_PATH) == 0:
		
		alert('Cài đặt đường dẫn lưu trữ trong mục [COLOR red][B]Cấu hình[/B][/COLOR].')
		xbmcaddon.Addon(id='plugin.video.vietmediaF').openSettings('download_path')
	
	if len(DOWNLOAD_PATH) > 0:
		xbmc.log(url)
		if 'fshare.vn' in url:
			link = getlink.get(url)
			
		else:
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
					notify('Lỗi không lấy được link phim hoặc server không hỗ trợ download.')
					return
				xbmcgui.Dialog().ok('VietmediaF', 'Bạn phải đặt tên files  cần lưu, và extention của file (có thể là "zip, mp4, mkv")', 'Ví dụ: [COLOR blue]video.mkv[/COLOR]')
				
				keyboard2 = xbmc.Keyboard(file_name)
				keyboard2.setHeading('SAVE FILE AS')
				keyboard2.doModal()
				if keyboard2.isConfirmed():
					file_name = keyboard2.getText()
				if len(file_name) == 0:
					sys.exit()
				
		#params = { "url": link, "download_path": DOWNLOAD_PATH }
		downloader.download(link,DOWNLOAD_PATH+file_name)
	
go()

