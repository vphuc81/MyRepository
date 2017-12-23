# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import urllib,urllib2,re
import os
import xbmc,xbmcplugin,xbmcgui,xbmcaddon
import getlink
import urlfetch
import simplejson as json
from config import VIETMEDIA_HOST
from addon import alert, notify, notify1, TextBoxes, ADDON, ADDON_ID, ADDON_PROFILE, LOG, PROFILE
from platform import PLATFORM
import uuid
import SimpleDownloader as downloader
import remove_accents
import autorun
import datetime as dt, time
import xbmcvfs, shutil, zipfile


downloader = downloader.SimpleDownloader()

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
DOWNLOAD_PATH = ADDON.getSetting("download_path")
CHECK = ADDON.getSetting("check")
DIALOG = xbmcgui.Dialog()
vDialog = xbmcgui.DialogProgress()
HOME = xbmc.translatePath('special://home/')
USERDATA = os.path.join(xbmc.translatePath('special://home/'), 'userdata')
ADDONDATA = os.path.join(USERDATA, 'addon_data', ADDON_ID)

def get_Setting():
	if not os.path.exists(PROFILE_PATH):
		os.makedirs(PROFILE_PATH)
	try:
		if CHECK=="false":
			#notify('Thiết lập Setting cho lần đầu sử dụng')
			
			yes_pressed=DIALOG.yesno("Thoả thuận sử dụng","1. Bạn hoàn toàn chịu trách nhiệm về nội dung bạn xem trên VietmediaF.", "2. Nội dung do người dùng đóng góp và lấy hoàn toàn trên mạng Internet.", "3. VMF Code là hình thức ủng hộ để duy trì hoạt động VietmediaF, các tính năng đi kèm có thể không hoạt động tùy tình hình thực tế.", "4. Nếu đồng ý sử dụng, hãy nhấn [COLOR yellow][B]Yes[/B][/COLOR] để đi tới cài đặt, nếu không nhấn [COLOR dimgrey][B]No[/B][/COLOR] để thoát.", nolabel='No, Cancel', yeslabel='Yes, Continue')
			if yes_pressed:
				addon = xbmcaddon.Addon()
				addon.setSetting(id='check', value="true")
				xbmcaddon.Addon(id='plugin.video.vietmediaF').openSettings()
			else:
				#notify('Thoát')
				addon = xbmcaddon.Addon()
				addon.setSetting(id='check', value="false")
				xbmc.executebuiltin('ActivateWindow(10000,return)')
				
	except:
		pass		
get_Setting()
	
def get_notif():
	NOTIF = ADDON.getSetting("notif")
	try:
		response = urlfetch.get('http://repo.kodi.vn/Phude/notif.txt')
		matches = re.search(r"(\d+)-", response.body)
		check = matches.group(1)
		matches = re.search(r"-(.+)", response.body)
		notif1 = matches.group(1)
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
		try: 
			fetch_data('https://goo.gl/ESJN7Q')
			
		except:
			pass
		if 'Saturday' in day or 'Sunday' in day:
				notify('Xin chúc bạn ngày cuối tuần vui vẻ.')
		else:
				notify('Chúc bạn vui vẻ.')	
		
	with open(filename,"r") as f:
		lines = f.read()
	if date not in lines:
		try: 
			fetch_data('https://goo.gl/ESJN7Q')
			
		except:
			pass
		if 'Saturday' in day or 'Sunday' in day:
			notify('Xin chúc bạn ngày cuối tuần vui vẻ.')
		else:
			notify('Chúc bạn vui vẻ.')	
		get_notif()
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
	login_url = 'https://www.fshare.vn/login'
	response = urlfetch.fetch(login_url)
	#alert(username)
	#alert(password)
	csrf_pattern = '\svalue="(.+?)".*name="fs_csrf"'
	csrf=re.search(csrf_pattern, response.body)
	fs_csrf = csrf.group(1)
	#alert(fs_csrf)
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring}
	data = {
				"LoginForm[email]"		: username,
				"LoginForm[password]"	: password,
				"fs_csrf"				: fs_csrf
			}
	response = urlfetch.post(login_url, headers=headers, data=data)
	if 'Sai tên đăng nhập hoặc mật khẩu.' in response.body:
		alert('Sai tên đăng nhập hoặc mật khẩu. Xin vui lòng kiểm tra lại user và password', '[COLOR yellow]Fshare thông báo[/COLOR]')
		sys.exit("Error message")
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring}
	check_acc = urlfetch.get('https://www.fshare.vn/account/infoaccount', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring})
	regex = r"data-target=\"#member\">(.+?)</a>"
	ma_tk=re.search(regex, check_acc.body)
	ma_tk=ma_tk.group(1)
	ma_tk='Loại tài khoản: [COLOR red]'+ma_tk+'[/COLOR]'
	date_create=re.search(r"<dt>Ngày tham gia</dt>.*\n.+?<dd>(.+?)</dd>", check_acc.body)
	date_create=date_create.group(1)
	date_create=date_create.rstrip()
	date_create='Ngày tham gia: [COLOR red]'+date_create+'[/COLOR]'
	acc_id=re.search(r"<dt>Mã Tài Khoản</dt>.*\n.+?<dd>(.+?)</dd>",check_acc.body)
	acc_id=acc_id.group(1)
	acc_id='Mã tài khoản: [COLOR red]'+acc_id+'[/COLOR]'
	expire_date=re.search(r"<dt>Hạn dùng</dt>.*\n.+?<dd>(.+?)</dd>",check_acc.body)
	expire_date=expire_date.group(1)
	#expire='Hạn dùng: [COLOR red]'+expire+'[/COLOR]'
	bonus=re.search(r"<dt>Điểm thưởng</dt>.*\n.+?<dd>(.+?)</dd>",check_acc.body)
	bonus=bonus.group(1)
	bonus='Điểm thưởng: [COLOR red]'+bonus+'[/COLOR]'
	check_acc = urlfetch.get('https://www.fshare.vn/account/profile', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring})
	regex = r'Địa chỉ email</label>.+<div class=\"col-sm-8.+text-primary\">(.+?)<\/div>'
	email = re.search(regex, check_acc.body)
	email = email.group(1)
	email = 'Địa chỉ e-mail: [COLOR red]'+email+'[/COLOR]'
	info=acc_id+'\n'+ma_tk+'\n'+date_create+'\n'+'Hạn dùng: [COLOR red]'+expire_date+'[/COLOR]\n'+bonus+'\n'+email
	TextBoxes('Trạng thái tài khoản fshare', info)
	
		
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
def forceUpdate():
	notify('Bắt đầu kiểm tra')
	xbmc.executebuiltin('UpdateAddonRepos()')
	xbmc.executebuiltin('UpdateLocalAddons()')
	notify('Done')
def tut1():
	url = 'http://textuploader.com/dd4ds/raw'
	content = openURL(url)
	TextBoxes(ADDON_NAME, content)

def download_sub(subtitle):
	xbmc_temp = xbmc.translatePath('special://temp')
	tempdir = os.path.join(xbmc_temp, 'phudeVMF')
	if 'subscene.com' in subtitle:
		response = urlfetch.get(subtitle)
		sub = re.search(r'href=\"(/subtitle/download?.*?)\"', response.body)
		sub = sub.group(1)
		subpath = "https://subscene.com" + sub
	if 'phudeviet.org' in subtitle:
		f = urlfetch.get(subtitle)
		match = re.search(r"(http://phudeviet.org/download/.+?html)", f.body)
		subpath = match.group(1)
		f = urlfetch.get(subpath)
		subpath = f.getheader('location')
		
	vDialog.create('Vietmediaf','Bắt đầu tải phụ đề xin vui lòng đợi trong giây lát.','Downloading...')
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
	headers = {'User-Agent': useragent, 'Referer': subtitle}
	tmp_file = os.path.join(tempdir, "phude.zip")
	
	try:
		if os.path.exists(tmp_file):
			os.remove(tmp_file)
		request = urllib2.Request(subpath, '', headers)
		response = urllib2.urlopen(request)
		file_handle = xbmcvfs.File(tmp_file, "wb")
		file_handle.write(response.read())
		xbmc.sleep(500)
		file_handle.close()
		xbmc.executebuiltin('XBMC.Extract("%s","%s")' % (tmp_file, tempdir))
		
	except:
		notify('Không tải được phụ đề')
		pass
	vDialog.close()
	exts = [".srt", ".sub", ".txt", ".smi", ".ssa", ".ass"]
	sub_temp = os.path.join(tempdir, "sub.file")
	for file in xbmcvfs.listdir(tempdir)[1]:
		if os.path.splitext(file)[1] in exts:
			sub_file = os.path.join(tempdir, file)
			xbmcvfs.rename(sub_file, sub_temp)
			return sub_temp
	
def play(data):
	link = data["url"]
	
	if link is None or len(link) == 0:
		notify('Lỗi không lấy được link phim. Xin vui lòng thử lại sau.')
		return
	if 'PIC' in link:
		imgSrc = link.replace('PIC','')	
		xbmc.executebuiltin('ShowPicture('+imgSrc+')')
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
		subtitle = ''
		links = link.split('[]')
		if len(links) == 2:
			subtitle = links[1]
		elif data.get('subtitle'):
			subtitle = data.get('subtitle')
		xbmc.log('subtitle_url')
		xbmc.log(subtitle)
		link = links[0]
		item = xbmcgui.ListItem(path=link, thumbnailImage=xbmc.getInfoLabel("ListItem.Art(thumb)"))
		xbmcplugin.setResolvedUrl(HANDLE, True, item)
		#alert(subtitle)
		
	  	if len(subtitle) > 0:
			if "https://subscene.com/" in subtitle or "phudeviet.org" in subtitle:
				subfile = download_sub(subtitle)
				xbmc.Player().setSubtitles(subfile.bak)#disable sub
			if "fcine.net" in subtitle:
				
				xbmc_temp = xbmc.translatePath('special://temp')
				tempdir = os.path.join(xbmc_temp, 'phudeVMF')
				vDialog.create('Vietmediaf','Bắt đầu tải phụ đề xin vui lòng đợi trong giây lát.','Downloading...')
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
				headers = {'User-Agent': useragent, 'Referer': 'fcine.net'}
				tmp_file = os.path.join(tempdir, "phude.srt")
				
				try:
					if os.path.exists(tmp_file):
						os.remove(tmp_file)
					request = urllib2.Request(subtitle, '', headers)
					response = urllib2.urlopen(request)
					file_handle = xbmcvfs.File(tmp_file, "wb")
					file_handle.write(response.read())
					xbmc.sleep(500)
					file_handle.close()
					
				except:
					notify('Không tải được phụ đề')
					return
				vDialog.close()
				xbmc.Player().setSubtitles(tmp_file.bak)#disable sub
				
			else:
				subtitlePath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
				subfile = xbmc.translatePath(os.path.join(subtitlePath, "temp.sub"))
				try:
					if os.path.exists(subfile):
						os.remove(subfile)
					#f = urllib2.urlopen(subtitle)
					f = urlfetch.get(subtitle)
					with open(subfile, "wb") as code:
						code.write(f.body)
					xbmc.sleep(3000)
					
					xbmc.Player().setSubtitles(subfile.bak)#disable sub
					#notify('Tải phụ đề thành công. Nếu không play được kiểm tra VMF Code.')
				except:
					notify#('Không tải được phụ đề phim.') disable sub

def go():
  
	url = sys.argv[0].replace("plugin://%s" % ADDON_ID, VIETMEDIA_HOST ) + sys.argv[2]
  
	if url == VIETMEDIA_HOST + '/':
		url += '?action=menu'
	
	#Settings
	if 'textbox' in url or 'Textbox' in url:
		url = url.replace(VIETMEDIA_HOST+'/?action=textbox&', '')
		
		url = urllib.unquote_plus(url)
		content = openURL(url)
		TextBoxes(ADDON_NAME, content)
		return
		
	if 'checkupdate' in url:
		forceUpdate()
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
  #dialog = xbmcgui.Dialog()
  #download_path = dialog.browse(3, 'XBMC', 'files')
  
	if len(DOWNLOAD_PATH) == 0:
		
		alert('Cài đặt đường dẫn lưu trữ trong mục [COLOR red][B]Cấu hình[/B][/COLOR].')
		xbmcaddon.Addon(id='plugin.video.vietmediaF').openSettings('download_path')
	
	if len(DOWNLOAD_PATH) > 0:
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
				notify('Lỗi không lấy được link phim hoặc server không hỗ trợ download.')
				return
			xbmcgui.Dialog().ok('VietmediaF', 'Bạn phải đặt tên files  cần lưu, và extention của file (có thể là "zip, mp4, mkv")', 'Ví dụ: [COLOR blue]video.mkv[/COLOR]')
			keyboard2 = xbmc.Keyboard()
			keyboard2.setHeading('SAVE FILE AS')
			keyboard2.doModal()
			if keyboard2.isConfirmed():
				file_name = keyboard2.getText()
			if len(file_name) == 0:
				return
				
			params = { "url": link, "download_path": DOWNLOAD_PATH }
			downloader.download(file_name, params)

go()

