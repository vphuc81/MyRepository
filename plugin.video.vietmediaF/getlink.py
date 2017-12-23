# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import re
import urlfetch
import os
from time import sleep
from addon import alert, notify,notify1, TextBoxes, ADDON, ADDON_ID, ADDON_PROFILE, LOG, PROFILE
import json
import random
import xbmc,xbmcgui
import pyxbmct
from config import VIETMEDIA_HOST
import urllib
import os, sys
#import requests
import time
import vmfdecode as vmf
#import urlresolver


USER_VIP_CODE = ADDON.getSetting('user_vip_code')
ADDON_NAME = ADDON.getAddonInfo("name")
PROFILE_PATH = xbmc.translatePath(ADDON_PROFILE).decode("utf-8")
T='aHR0cDovL3BsYXllci50cnVuZ3VpdC5uZXQvZ2V0P3VybD0='
F1 = 'U2FsdGVkX18tMUoo3k2cYautKONoQ5xHCpLDHBz/RNhTLRbBvHKgrtMKiRks5tw4'
HOME = xbmc.translatePath('special://home/')
USERDATA = os.path.join(xbmc.translatePath('special://home/'), 'userdata')
ADDONDATA = os.path.join(USERDATA, 'addon_data', ADDON_ID)
DIALOG = xbmcgui.Dialog()
vDialog = xbmcgui.DialogProgress()

def fetch_data(url, headers=None, data=None):
  	if headers is None:

  		headers = { 
    				'User-agent'	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
                	'Referer'		: 'http://www.google.com',
                	'X-User-VIP'    :  USER_VIP_CODE
            }
  	try:

  		if data:
  			response = urlfetch.post(url, headers=headers, data=data)
  		else:
			response = urlfetch.get(url, headers=headers)
           	return response

	except Exception as e:
  		print e
  		pass


def get(url):
	if '//fptplay.net' in url:
		return get_fptplay(url)
	if 'www.fshare.vn' in url:
		return get_fshare(url)
	if '//4share.vn' in url:
		return get_4share(url)
	if len(url)==16:
		return get_4share(url)
	if 'hdonline.vn' in url:
		return get_hdonline(url)
	if '//vtvgo.vn' in url:
		return get_vtvgo(url)
	if '//htvonline.com.vn' in url:
		return get_htvonline(url)
	if '//hplus.com.vn' in url:
		return get_htvplus(url)
	if '//xuongphim.tv' in url:
		return get_xuongphim(url)
	if '//phim3s.net' in url:
		return get_phim3s(url)
	if 'tvnet.gov.vn' in url:
		return getTvnet(url)
	if '//kenh1.mobifone.com.vn' in url:
		return get_mobifone(url)
	if '//thvl.vn' in url:
		return get_thvl(url)
	if 'link.tvmienphi.biz' in url:
		return get_tvmienphi(url)
	if 'serverthunghiem' in url:
		return get_serverthunghiem(url)
	if 'tv24.vn' in url:
		return get_servertv24(url)
	if 'acestream' in url:
		return getAcestream(url)
	if 'sop:' in url:
		return getSopcast(url)
	if 'vtv.vn' in url:
		return getVtv(url)	
	if 'dzone.vn' in url:
		return getDzone(url)
	if 'clip.vn' in url:
		return getClipvn(url)
	if 'haivn.com' in url:
		return getHaivn(url)
	if 'checkupdate' in url:
		return forceUpdate()
	if 'xemphimbox.com' in url:
		return getxemphimbox(url)
	if 'hayhaytv.vn' in url:
		return getHayhayTV(url)
	if 'kphim.tv' in url:
		return getKphim(url)
	if 'truongquocvi.com' in url:
		return getTQV(url)
	if 'anime47.com' in url:
		return getAnime47(url)
	if 'mp3.zing.vn' in url:
		return getMp3Zing(url)
	if 'hdsieunhanh.com' in url:
		return getHdsieunhanh(url)
	if 'aphim.co' in url:
		return getAphim(url)
	if 'phimmoi.net' in url:
		return getPhimMoi(url)
	if 'TEST' in url:
		return getTEST(url)
	if 'xemphimso.com' in url:
		return xemphimso(url)
	if 'openload' in url:
		return getOpenload(url)
	if 'drive.google.com' in url:
		return getDriveG(url)
	if 'vtvgo' in url:
		return getvtvgo(url)
	else:
		return url


		
def getTEST(url):
	video_url = ''
	return video_url
def getDriveG(url):
	
	media_url = urlresolver.resolve(url)
	return media_url	
	
def getvtvgo(url):
	url = url.lower()
	vtv = {'vtv1':1, 'vtv2': 2, 'vtv3': 3, 'vtv4': 4, 'vtv5': 5, 'vtv6': 6, 'vtv7': 27, 'vtv8':36, 'vtv9':39, 'vtv5nambo': 7}
	match = re.search(r"\/(.+)", url)
	channel = match.group(1)
	contentid = str(vtv[channel])
	f = 'U2FsdGVkX187QjjKy+qMwPB6Z8YoN5Yz2C8miPmAsL+2OuqTXwZzOxcsDnaxbh/N'
	if len(USER_VIP_CODE) > 0:
		try:
			response = fetch_data(VIETMEDIA_HOST + vmf.gibberishAES(f, 'vmf'))
			json_data = json.loads(response.body)
			t =json_data['username'].decode('base64')
			matches = re.search(r"grab=\"(.+?)\"&app_id=\"(.+?)\"&device_type=\"(.+?)\"&vtv_id=\"(.+?)\"&acc_id=\"(.+?)\"&sign=\"(.+?)\"", t)
			#TextBoxes('VMF', t)
			grab = matches.group(1)
			app_id = matches.group(2)
			device_type = matches.group(3)
			vtv_id = matches.group(4)
			acc_id = matches.group(5)
			sign = matches.group(6)
			payload = '{"app_id":"'+app_id+'","device_type":"'+device_type+'","vtv_id":"'+vtv_id+'","acc_id":"'+acc_id+'","sign":"'+sign+'","contenttype":"1","contentid":"'+contentid+'"}'
			headers = {'cache-control': "no-cache"}
			response = urlfetch.post(grab.decode("base64"), data=payload, headers=headers)
			jsonStr = json.loads(response.body)
			video_url = jsonStr['result']['stream_url'][0]
			return(video_url)
		except Exception as e:
			notify('Khong lay duoc link')
			pass
	
def getPhimMoi(url):
	headers = { 'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
				'Host'				: 'www.phimmoi.net',
				'Referer'			: url
				}
	T2="U2FsdGVkX1+J5yRXU1goqexulsqcAaICSdXjSrml+FFQiYusRAwciVrwAIW86pvrU2RGQmSb9YL/8xMaOnWGbA"		
	response = urlfetch.get(url, headers=headers)
	regex = r"(;eval.+)<\/script>"
	matches = re.search(regex, response.body)
	payload = matches.group(1)
	payload = urllib.quote(payload)
	payload = "data="+payload
	headers = {
		'content-type': "application/x-www-form-urlencoded",
		'cache-control': "no-cache"
		}
	response = urlfetch.post(vmf.gibberishAES(T2, 'vmf'), data=payload, headers=headers)
	response = urlfetch.get(response.body)
	regex = r"var _responseJson='(.+)';"
	matches = re.search(regex, response.body)
	json_data = matches.group(1)
	json_data = json.loads(json_data)
	backup_order = json_data['backupOrder']
	t = len(json_data['medias'])
	video_url = json_data['medias'][(t-1)]['url']
	return video_url
	'''
	response = urlfetch.get(video_url)
	if response.status == 302:
		t = response.getheader('set-cookie')
		t = urllib.quote(t)
		link = response.getheader('location')
		video_url = link+'|'+'Cookie='+t
		
	else:
		t = len(json_data['mediasBk'])
		video_url = json_data['mediasBk'][(t-1)]['url']
		response = urlfetch.get(video_url)
		if response.status == 302:
			t = response.getheader('set-cookie')
			link = response.getheader('location')
			video_url = link+'|'+'Cookie='+t
		else:
			t = len(json_data['mediasBk1'])
			if not 'googleusercontent' in video_url:
				video_url = json_data['mediasBk1'][0]['url']
	return video_url
	'''
def getAphim(url):
	if 'get_file' in url:
		import urllib
		url = urllib.unquote_plus(url)
		matches = re.search(r"movie_id=(.+?)&episode_id=(.+?)&", url)
		movie_id = matches.group(1)
		episodes_id = matches.group(2)
		matches = re.search(r"slug=(.+)", url)
		slug = matches.group(1)
		url1 = 'https://aphim.co/phim/'+slug
		
		headers = { 'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Host'				: 'aphim.co',
			'X-Requested-With'	:  'XMLHttpRequest',
			'Referer'			: url1
			}
		
		response = urlfetch.get(url, headers=headers)
		jsonStr = json.loads(response.body)
		video_url = jsonStr['file']
		
		
	else:
		headers = { 'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
				'Host'				: 'aphim.co',
				'X-Requested-With'	:  'XMLHttpRequest',
				'Referer'			: url
				}
				
		response = urlfetch.get(url, headers=headers)
		regex = r"phim\/(.+)"
		matches = re.search(regex, url)
		slug = matches.group(1)
		getid_url = 'https://aphim.co/api/movie/'+slug
		response = urlfetch.get(getid_url, headers=headers)
		jsonStr = json.loads(response.body)
		movie_id = jsonStr['id']
		episodes_id = jsonStr['episodes'][0]['contents'][0]['id']
		get_url = 'https://aphim.co/player/get_file?type=watch&movie_id='+movie_id+'&episode_id='+episodes_id+'&server=&_x=0.36660287152800464'
		response = urlfetch.get(get_url, headers=headers)
		jsonStr = json.loads(response.body)
		video_url = jsonStr['file']
	
	return video_url
def GoogleDrive(url):
	response = urlfetch.get(url)
	if response.status == 302:
		t = response.getheader('set-cookie')
		link = response.getheader('location')
		video_url = link+'|'+'Cookie='+t
	else:
		video_url = 'thongbao4-Video het luot xem. Xin vui long quay lai sau.'
	return video_url

def getOpenload(url):
	alert('Đang xử lý. Vui lòng quay lại sau.')
	#media_url = urlresolver.resolve(url)
	return 	
	
def getHdsieunhanh(url):
	
	if 'Tap' in url:
		match = re.search(re.compile(r"Tap-(\d+)"), url)
		tapid = match.group(1)
	else:
		tapid = ''
	if '/show-' in url:
			show = 'show'
	else:
			show = ''
	match = re.search(re.compile(r"-(\d+)\.html"), url)
	pid = match.group(1)
	#print (pid)
	response = urlfetch.get(url)
	cookie = response.cookiestring;

	response = urlfetch.get('http://ip.hdsieunhanh.com/')
	match = re.search(re.compile(r"'(.*?)'"), response.body)
	yourip = match.group(1)
	print (yourip)
	headers = {'Host': 'www.hdsieunhanh.com', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': url, 'X-Requested-With'	: 'XMLHttpRequest'}
	data = {'ip': yourip}

	attempt = 1
	MAX_ATTEMPTS = 3

	try:
		response = urlfetch.get('http://www.hdsieunhanh.com/getsource'+show+'/' +pid +'_'+tapid +'?ip=' +yourip, headers=headers, data=data)

		print (response.body)
		json_data = json.loads(response.body)
		video_url = json_data['sources'][0]['file']
		#Phu de
		phude = json_data['tracks'][2]['file']
		return (video_url+'[]'+phude)
	except Exception as e:
			print e
			pass
			

def getMp3Zing(url):
	headers = { 'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Host'				: 'mp3.zing.vn',
			'Referer'			: url,
			'X-Requested-With'	: 'XMLHttpRequest'
			}
					
	s = requests.Session()
	r = s.get(url, headers=headers)
	matches = re.search(r"data-xml=\"(.+?)\"", r.content)
	url_get = matches.group(1)
	url_get = 'http://mp3.zing.vn'+url_get
	r = s.get(url_get, headers=headers)
	json_data = json.loads(r.content)
	mp3link = json_data["data"][0]["source_list"][0]		
	return mp3link
	
def getAnime47(url):
	headers = {
			'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Referer': 'http://anime47.com',
			'Cookie'			: 'location.href=1; path=/'}
	url_data = urlfetch.get(url, headers=headers)
	matches = re.search(r"var _\w+\W+(\[.+?\])", url_data.body)
	keys = matches.group(1)
	keys = keys.decode('string_escape')
	keys = json.loads(keys)[5].encode('utf-8')
	matches = re.search(r'link:\s\"(.*?)\"', url_data.body)
	google_link = matches.group(1)
	player_url = 'http://anime47.com/player/player.php'
	data = {'link': google_link}
	response = urlfetch.post(player_url, headers=headers, data=data)
	j = response.body.decode('base64')
	jsonStr = json.loads(j)
	s = jsonStr['s']
	salt  = s.decode("hex")
	ct = jsonStr['ct']
	l = vmf.decode(ct, keys, salt)
	links = json.loads(l)
	matches = re.search(r"\"file\":\"(.*?)\"", links)
	if matches:
		links = matches.group(1)
	else:
		return 'thongbao2'
	return (links)
		

	
def getTQV(url):
	if 'get' in url:
		r = requests.get(url)
		url = r.url
		
	else:	
		matches = re.search(r"channel=(.+)", url)
		channel = matches.group(1)
		response = urlfetch.get(url)
		matches = re.search(r"source src=\"(.+?)\"", response.body)
		url = matches.group(1)
	return url
def getKphim(url):
	matches = re.search(r"\?vid=(\d+)\?sid=(\d+)", url)
	vid = matches.group(1)
	sid = matches.group(2)
	token=urllib2.hashlib.md5(vid+'func'+sid).hexdigest()[1:]
	getlink = 'http://kphim.tv/embed/'+vid+'/'+sid+'/'+token
	response = urlfetch.get(getlink)
	matches = re.search(r"file:\s'(.+?)'", response.body)
	video_url = matches.group(1)
	response = urlfetch.get(video_url)
	rh = response.getheaders()
	video_url = rh[5][1]
	return video_url

def getmp3zing(url):	
	response = urlfetch.get(url)
	matches = re.search(r"data-xml=\"(.+?)\"", response.body)
	url_get= matches.group(1)
	if 'http' not in url_get:
		url_get = 'http://mp3.zing.vn'+url_get
	#lấy link nhạc
	response = urlfetch.get(url_get)
	json_data = json.loads(response.body)
	data = json_data["data"][0]["source_list"][1]
	if len(data) == 0:
		data = json_data["data"][0]["source_list"][0]
	return data
	
def getHayhayTV(url):
	response = urlfetch.get('http://ip.hayhaytv.vn/')
	cookie = response.cookiestring;
	matches = re.search(r"userip = '(.+?)'", response.body)
	yourip = matches.group(1)
	response = urlfetch.get(url)
	matches = re.search(r"FILM_KEY = '(.+?)'", response.body)
	id_url = matches.group(1)
	get_url = 'http://www.hayhaytv.vn/getsource/'+id_url+'__?ip='+yourip
	headers = {
			'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Referer': url,
			'Host'	: 'www.hayhaytv.vn',
			'Cookie'			: cookie}
	if "show" in url:
		get_url = get_url.replace("getsource", "getsourceshow")
	
	attempt = 1
	MAX_ATTEMPTS = 3
	
	while attempt < MAX_ATTEMPTS:
		if attempt > 1: 
			sleep(2)
		notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
		response = urlfetch.get(get_url, headers=headers)
		if not response:
			return 'thongbao2'
					
		matches = re.search(r"(\{\"sources.+)", response.body)
		if matches:
			break
	t = matches.group(1)
	json_data = json.loads(t)
	video_url = json_data["sources"][1]["file"]
	if 'youtube.com' in video_url:
		matches = re.search(r"v=(.+)", video_url)
		id_youtube = matches.group(1)
		video_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + id_youtube 
	phude = json_data["tracks"][0]["file"]
	if len(phude) > 0:
		return video_url+"[]"+phude
	else:
		return video_url

def xemphimso(url):
	response = urlfetch.get(url)
	match = re.search(r"<script type=\"text\/javascript\" src=\"(https://grab.+?)\"", response.body)
	grablink = match.group(1)
	attempt = 1
	MAX_ATTEMPTS = 2
	while attempt < MAX_ATTEMPTS:
		if attempt > 1: 
			print('p')
		notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
		attempt += 1
		grablink = grablink+'&reload=%s' % attempt
		response = urlfetch.get(grablink)
		match = re.search(r"jwConfigPlayer.playlist\[0]\.sources =(.+?);", response.body)
		if match:
			video_url = match.group(1)
			jStr = json.loads(video_url)
			video_url = jStr[0]['file']
		
	return video_url
	

def getxemphimbox(url):
	matches = re.search(r"-(\d+)", url)
	idfilm = matches.group(1)
	response = urlfetch.get(url)
	cookie = response.cookiestring;
	matches = re.search(r"filmInfo\.episodeID = parseInt\('(\d+)'\);", response.body)
	idEP = matches.group(1)
	host = 'xemphimbox.com'
	headers = {
			'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Referer': url,
			'Host'	: host,
			'X-Requested-With'	: 'XMLHttpRequest',
			'Cookie'			: cookie}
	data = {
			'NextEpisode':  1,
			'EpisodeID'	: idEP,
			'filmID'	: idfilm,
			'playTech'	: 'auto'}

	response = urlfetch.post('http://xemphimbox.com/ajax', headers=headers, data=data)
	matches = re.search(r"src=\"(.+?)\"", response.body)
	getlink = matches.group(1)
	millis = int(round(time.time() * 1000))
	getlink += '&_=' + str(millis)
	host = 'grab.xemphimbox.com'
	headers = {
			'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Referer': url,
			'Host'	: host,
			'X-Requested-With'	: 'XMLHttpRequest',
			'Cookie'			: cookie}
	response = urlfetch.get(getlink, headers=headers)
	matches = re.search(r"jwConfigPlayer.playlist\[0\].sources =(.*?);", response.body)
	jsonStr = json.loads(matches.group(1))
	video_url = jsonStr[len(jsonStr)-1]['file']	
	return video_url
	
		

def getHaivn(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Referer'  : url
		}
	response = urlfetch.get(url, headers=headers)
	if not response:
		notify(u'Trang nguồn có lỗi. Thông báo cho dev.'.encode("utf-8"))

	if 'youtube-player' in response.body:
		
		matches = re.search(r"iframe allowfullscreen=\"true\" src=\"(.+?)\?", response.body)
		
		video_url = matches.group(1)
		matches = re.search(r"embed\/(.+)", video_url)
		youtube_id = matches.group(1)
		video_url = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + youtube_id
		
	else:
		regex = r'script type=\"text\/javascript\" src=\"(.+?mecloud-player)\"'
		matches = re.search(regex, response.body)
		if not matches:
			return ''
		url_player = matches.group(1)
		
		response = urlfetch.get(url_player, headers=headers)
		regex = r"\"video\":(\[.+?\])"
		matches = re.search(regex, response.body)
		video_url = matches.group(1)
		t = video_url.count('url')
		data = json.loads(video_url)
		video_url = data[t-1]['url']
		video_url = 'http:'+video_url
	
	return video_url
	xbmc.log(video_url)
		
def get_hdonline(url):
	attempt = 1
	MAX_ATTEMPTS = 5
	
	while attempt < MAX_ATTEMPTS:
		if attempt > 1: 
			sleep(2)
		url_play = ''
		notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
		attempt += 1
		headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
				'Referer'		: 'http://hdonline.vn'
			}
		response = fetch_data(url, headers)
		if not response:
			return ''

		cookie = response.cookiestring

		match = re.search(r'eval\(function\((.*?)split\(\'\|\'\),0,\{\}\)\)', response.body)
		if match:
			eval_js = 'eval(function(' + match.group(1) + 'split(\'|\'),0,{}))'
			
			response = fetch_data('http://vietmediaf.net:4000/api/v1/decode/hdo', None, {'data': eval_js})

			json_data = json.loads(response.body)
			_x = random.random()
			url_play = ('http://hdonline.vn%s&format=json&_x=%s' % (json_data['playlist'][0]['file'], _x))
			
			#tim ep
			
			match = re.search(r'\-tap-(\d+)-[\d.]+?\.html$', url)
			if match:
				ep = match.group(1)
				url_play = url_play.replace('ep=1','ep='+ep)
			
			break
		else:
			match = re.search(r'\-tap-(\d+)-[\d.]+?\.html$', url)
			if not match:
				ep = 1
			else:
				ep = match.group(1)
			match = re.search(r'"file":"(.*?)","', response.body)
			if match:
				url_play = 'http://hdonline.vn' + match.group(1).replace('\/','/') + '&format=json&reloadbk=1'
				url_play = url_play.replace('ep=1','ep=' + str(ep))
				break
	if len(url_play) == 0:
		notify (u'Không lấy được link.')
		return ''

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
				'Referer'		: 'http://hdonline.vn',
				'Accept'		: 'json',
				'Cookie'		: cookie
			}
	
	
	response = fetch_data(url_play, headers)

	json_data = json.loads(response.body)
	video_url = json_data['file']
	if json_data.get('level') and len(json_data['level']) > 0:
		video_url = json_data['level'][len(json_data['level']) - 1]['file']

	subtitle_url = ''
	if json_data.get('subtitle') and len(json_data['subtitle']) > 0:
		for subtitle in json_data['subtitle']:
			subtitle_url = subtitle['file']
			if subtitle['code'] == 'vi':
				subtitle_url = subtitle['file']
				break
	if len(subtitle_url) > 0:		
		#subtitle_url = ('http://data.hdonline.vn/api/vsub.php?url=%s' % subtitle_url)
		subtitle_url = subtitle_url.replace('http://data.hdonline.vn//', 'http://data.hdonline.vn/')
		xbmc.log('HDONLINE')
		xbmc.log(subtitle_url)
		return video_url + "[]" + subtitle_url
	else:
		return video_url
def getVtv(url)	:
	response = urlfetch.get(url)
	matches = re.search(r"src=\"(.+play.+?)\"", response.body)
	play_url = matches.group(1)
	headers = {'Host': 'play.sohatv.vn', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Referer': url}
	response = urlfetch.get(play_url, headers=headers)
	matches = re.search(r"status-code=200 src=\"(.+?)\"", response.body)
	url_play = matches.group(1)
	matches = re.search(r"live=(.+?m3u8)", url_play)
	m3u8 = matches.group(1)
	m3u8 = 'http:'+urllib.unquote_plus(m3u8)
	split_list = m3u8.split('/', 9)
	remove = split_list[8]
	vtvvn_option = 'true'
	if 'vtv5-tay-nam-bo' not in url:
		matches = re.search(r"==(.+?)\.", remove)
		remove = matches.group(1)
		if vtvvn_option == 'false':
			m3u8 = m3u8.replace(remove, '_m')
		if vtvvn_option == 'true':
			m3u8 = m3u8.replace(remove, '')
	else:
		print('Kenh vtv5 nam bo')
		if vtvvn_option == 'false':
			m3u8 = m3u8.replace(remove, 'dnR2NWtt_m.m3u8')
		if vtvvn_option == 'true':
			m3u8 = m3u8.replace(remove, 'dnR2NWtt.m3u8')
	return m3u8

	
def getTvnet(url):
	headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Origin': 'http://vn.tvnet.gov.vn', 'Referer': url}
	matches = re.search(r"/\d+\/(.+)", url)
	channel = matches.group(1)
	r = urlfetch.get(url, headers=headers)
	matches = re.search(r"data-file=\"(.+?)\"", r.body)
	url_get = matches.group(1)
	url_get = url_get.replace('amp;', '')
	r = urlfetch.get(url_get, headers=headers)
	json_data = json.loads(r.body)
	video_url = json_data[0]["url"]
	return video_url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=http://vn.tvnet.gov.vn'

		
def getAcestream(url):
	if 'plugin:' in url:
		ace_link = url
	else:
		ace_option = ADDON.getSetting('ace')
		if ace_option == 'true':
			ace_link = 'plugin://program.plexus/?mode=1&url='+url+'&name=Video'
		else:
			response = fetch_data('http://127.0.0.1:6878/webui/api/service?method=get_version&format=jsonp&callback=mycallback')
			if not response:
				alert('Vui lòng khởi động ứng dụng Acestream. Cài đặt tại [COLOR yellow]acestream.org[/COLOR]')
				return
			else:
				ace_link = url.replace("acestream://", "http://localhost:6878/ace/getstream?id=")
				
	return ace_link		

def getSopcast(url):
	if 'plugin:' in url:
		sopcast_link = url
	else:
		sopcast_link = 'plugin://program.plexus/?mode=2&url='+url+'&name=Video'
	return sopcast_link
		
def get_fptplay(url):
	fptplay_option = ADDON.getSetting('fptplay_option')
	
	#Xem tv có thể không cần account hoặc có account hoặc có code VMF
	
	if 'livetv' in url:
		if fptplay_option == 'true':
			
			user = ADDON.getSetting('fptplay_user')
			password = ADDON.getSetting('fptplay_pass')
			country_code = ADDON.getSetting('country_code')
			matches = re.search(r"(.+)\s", country_code)
			country_code = matches.group(1)
			params = {'country_code': country_code, 'phone': user, 'password': password, 'submit': ''}
			headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Referer':'https://fptplay.net/'}
			url_login = 'https://fptplay.net/user/login'
			url_logout = 'https://fptplay.net/user/logout'
			if len(user) == 0  or len(password) == 0:
				sleep(2)
				notify(u'Bạn nên nhập user và pasword của FPTplay.net. Đăng ký trên trang web http://fptplay.net'.encode("utf-8"))
				#ADDON.openSettings()
			
			s = requests.Session()
			r = s.get('https://fptplay.net')
			r = s.post(url_login, headers=headers, data=params)
			headers = { 
						'Referer'			: url,
						'X-KEY'				: '123456',
						'X-Requested-With'	: 'XMLHttpRequest'
					}
			
			#Kiểm tra live tivi 
			match = re.search(r'\/livetv\/(.*)$', url)
			if match:
				channel_id = match.group(1)
				data = {
					'id' 	   : channel_id,
					'type'     : 'newchannel',
					'quality'  : 3,
					'mobile'   : 'web'
				}
				r = s.post('https://fptplay.net/show/getlinklivetv', headers=headers, data=data)
				
				response = fetch_data(url_logout, headers)
				if response.status == 302:
					notify (u'Done'.encode("utf-8"))
				video_url=json.loads(r.content)['stream']+'User-Agent=Mozilla/5.0 (compatible; MSIE 10.0; Trident/6.0; IEMobile/10.0; ARM; Touch; WINDOWS;MSI;MSI MSI-MS-7996;)'
				
				return video_url

				
			#match = re.search(r'\-([\w]+)\.html', url)
			#if not match:
			#	return

		if fptplay_option == 'false':
			if len(USER_VIP_CODE) == 0:
				alert(u'Bạn chưa nhập [COLOR red]VMF[/COLOR] code hoặc tài khoản cá nhân FPTPLAY'.encode("utf-8"), 'Soạn tin: [COLOR red]VMF[/COLOR] gửi [COLOR red]8798[/COLOR] để lấy VMF Code')
				return
			if len(USER_VIP_CODE) > 0:
				try:
					url_account = VIETMEDIA_HOST + '?action=fptplay_account'
					response = fetch_data(url_account)
					json_data = json.loads(response.body)
					user = json_data['username']
					xbmc.log(user)
					password = json_data['password']
					xbmc.log(password)
					country_code = 'VN'
					#Code getlink
					params = {'country_code': country_code, 'phone': user, 'password': password, 'submit': ''}
					headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Referer':'https://fptplay.net/'}
					url_login = 'https://fptplay.net/user/login'
					url_logout = 'https://fptplay.net/user/logout'
					s = requests.Session()
					r = s.get('https://fptplay.net')
					r = s.post(url_login, headers=headers, data=params)
					headers = { 
								'Referer'			: url,
								'X-KEY'				: '123456',
								'X-Requested-With'	: 'XMLHttpRequest'
							}
					
					#Kiểm tra live tivi 
					match = re.search(r'\/livetv\/(.*)$', url)
					if match:
						channel_id = match.group(1)
						data = {
							'id' 	   : channel_id,
							'type'     : 'newchannel',
							'quality'  : 3,
							'mobile'   : 'web'
						}
						r = s.post('https://fptplay.net/show/getlinklivetv', headers=headers, data=data)
						
						video_url=json.loads(r.content)['stream']+'User-Agent=Mozilla/5.0 (compatible; MSIE 10.0; Trident/6.0; IEMobile/10.0; ARM; Touch; WINDOWS;MSI;MSI MSI-MS-7996;)'
						
						return video_url
						
				except Exception as e:
					pass
				
	#Xem phim k cần account vip
	else:
		user = ADDON.getSetting('fptplay_user')
		password = ADDON.getSetting('fptplay_pass')
		country_code = ADDON.getSetting('country_code')
		matches = re.search(r"(.+)\s", country_code)
		country_code = matches.group(1)
		url_login = 'https://fptplay.net/user/login'
		params = {'country_code': country_code, 'phone': user, 'password': password, 'submit': ''}
		headers = {'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0','Referer':'https://fptplay.net/'}
		s = requests.Session()
		r = s.get('https://fptplay.net')
		r = s.post(url_login, headers=headers, data=params)
		headers = { 
					'Referer'			: 'https://fptplay.net',
					'X-Requested-With'	: 'XMLHttpRequest'
				}
		
		match = re.search(r'\-([\w]+)\.html', url)
		if not match:
			return
		movie_id = match.group(1)
		match = re.search(r'#tap-([\d]+)$', url)
		
		if match:
			episode_id = match.group(1)
		else:
			episode_id = 1

		data = {
			'id' 	   : movie_id,
			'type'     : 'newchannel',
			'quality'  : 3,
			'episode'  : episode_id,
			'mobile'   : 'web',
		}
		r = s.post('https://fptplay.net/show/getlink', headers=headers, data=data)
		json_data = json.loads(r.content)
		video_url=json.loads(r.content)['stream']+'User-Agent=Mozilla/5.0 (compatible; MSIE 10.0; Trident/6.0; IEMobile/10.0; ARM; Touch; WINDOWS;MSI;MSI MSI-MS-7996;)'
		return video_url

def get_vtvgo(url):
	response = urlfetch.get(url)
	matches = re.search(r"addPlayer\('(.+?)'", response.body)
	if not matches:
		return 'thongbao2'
	else:	
		video_url = matches.group(1)
		return(video_url+'|Referer=http%3a%2f%2fvtvgo.vn&User-Agent=Mozilla%2f5.0+(Windows+NT+10.0%3b+WOW64%3b+rv%3a48.0)+Gecko%2f20100101+Firefox%2f48.0')

def get_htvonline(url):
	response = fetch_data(url)
	cookie=response.cookiestring;
	if not response:
		return ''
	match = re.search(re.compile(r'data-source=\"(.*?)\"'), response.body)
	if not match:
		return 'thongbao2'
	video_url = match.group(1)
	video_url = video_url.replace('playlist', 'chunklist')
	return(video_url+'|Referer=http%3A%2F%2Fhplus.com.vn&User-Agent=Mozilla%2f5.0+(Windows+NT+10.0%3b+WOW64%3b+rv%3a48.0)+Gecko%2f20100101+Firefox%2f48.0')

def get_servertv24(url):
	user = ADDON.getSetting('sctv_user')
	password = ADDON.getSetting('sctv_pass')
	channelid = re.search(re.compile(r"\/(\d+)\/"), url).group(1)
	response = urlfetch.get(url)
	if not response:
		notify('Kiểm tra nguồn phát tại [COLOR red]tv24h.vn[/COLOR] và báo cho người phát triển.')
		return
	cookie=response.cookiestring;
	matches = re.search(r'\"channel_token\" value=\"(.+?)\"', response.body)
	channeltoken = matches.group(1)
	signin_url = 'http://tv24.vn/client/login/process'
	headers = {'Host': 'tv24.vn', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://web.tv24.vn/dang-nhap'}
	data = {'mobile': user, 'password': password}
	urlfetch.post(signin_url, headers=headers, data=data)
	data = {'channel_id': channelid, 'channel_token': channeltoken}
	response = urlfetch.post('http://tv24.vn/client/channel/link', headers=headers, data=data)
	if 'null' in response.body:
		if len(user) == 0  or len(password) == 0:
			sleep(1)
			alert(u'Bạn hãy đăng ký tài khoản trên web [COLOR red]http://tv24.vn[/COLOR] và nhập trong Setting của Addon VMF'.encode("utf-8"))
		else:
			notify('Link bị lỗi')
	else:
		json_data = json.loads(response.body)
		video_url = json_data['data']['PLAY_URL']
		notify("Đang getlink")
		video_url = vmf.sctv(channeltoken, video_url)
		sleep(5)
		if len(video_url) == 0:
			alert(u'Lỗi không lấy được link. Xin vui lòng thử lại.'.encode("utf-8"))
		return (video_url)
	
	
def get_thvl(url):
	cookie = urlfetch.get('http://thvl.vn/').cookiestring;
	headers = {'Host': 'thvl.vn', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://thvl.vn/jwplayer/?l=rtmp&i=http://thvl.vn/wp-content/uploads/2014/12/THVL1Online.jpg&w=640&h=360&a=0', 'X-Requested-With'	: 'XMLHttpRequest'}
	data = {'l': 'rtmp', 'i': 'http://thvl.vn/wp-content/uploads/2014/12/THVL1Online.jpg', 'w': '640', 'h': '360', 'a': '1'}
	response = urlfetch.get(url, data=data, headers=headers)
	return re.search(r'file:\s"(.*?)"', response.body).group(1)

def get_tvmienphi(url):
	cookie = urlfetch.get('http://www.tvmienphi.biz').cookiestring;
	headers = {'Host': 'link.tvmienphi.biz', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://mi.tvmienphi.biz/'}
	return re.search(r'channel_stream\s=\s\"(.*?)\"', urlfetch.get(url, headers=headers).body).group(1)

def get_serverthunghiem(url):
	return re.search(r'data-file="(.*?)"', urlfetch.get(re.search(r'=(.*)', url).group(1)).body).group(1)
	
def get_xuongphim(url):
	response = urlfetch.get(url)
	#cookie=response.cookiestring;
	match = re.search(re.compile(ur'file:\s"(.*?)"'), response.body)
	video_url = match.group(1)
	match = re.search(re.compile(r'file:\s\"(\/sub.*?)\"'), response.body)
	if match:
		phude = '|http://xuongphim.tv/'+match.group(1)
	else:
		phude = ''
	return video_url+phude	

def get_htvplus(url):
	if len(USER_VIP_CODE) > 0:
		try:
			f='U2FsdGVkX1+RQXkDAFegicGii3RLBVGrsbMVRV+kHpUpTExURcDQLDLLDkxsGOTf'
			notify(u'VMF Getlink system'.encode("utf-8"))
			response = fetch_data(VIETMEDIA_HOST + vmf.gibberishAES(f, 'vmf'))
			json_data = json.loads(response.body)
			t =json_data['username'].decode("base64")
			headers = { 
					'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
					'Referer'			: url,
					'Cookie'		: t
					}
			response = urlfetch.get(url, headers=headers)
			
			regex = r"iosUrl = \"(.+?)\""	
			matches = re.search(regex, response.body)
			video_url = matches.group(1)
			get_url = 'http://hplus.com.vn/content/getlinkvideo/'
			headers = { 
					'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
					'Referer'			: url,
					'Cookie'		: t			
					}
			data = {'url': video_url, 'type': '1', 'is_mobile': '0'}
			response = urlfetch.post(get_url, headers=headers, data=data)
			video_url = response.body.encode("utf-8")
			refer = "|User-Agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F58.0.3029.110%20Safari%2F537.36&Referer=http%3A%2F%2Fhplus.com.vn%2F"
			return (video_url + refer)
		except Exception as e:
			notify('Khong lay duoc link')
			pass
	else:
		headers = { 
					'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
					'Referer'			: url,
					'Cookie'		: t
					}
		response = urlfetch.get(url, headers=headers)
		t = response.cookiestring;
		regex = r"iosUrl = \"(.+?)\""	
		matches = re.search(regex, response.body)
		video_url = matches.group(1)
		get_url = 'http://hplus.com.vn/content/getlinkvideo/'
		headers = { 
				'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
				'Referer'			: url,
				'Cookie'		: t			
				}
		data = {'url': video_url, 'type': '1', 'is_mobile': '0'}
		response = urlfetch.post(get_url, headers=headers, data=data)
		video_url = response.body.encode("utf-8")
		refer = "|User-Agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F58.0.3029.110%20Safari%2F537.36&Referer=http%3A%2F%2Fhplus.com.vn%2F"
		return (video_url + refer)
		
def get_hash(m):
	md5 = m or 9
	s = ''
	code = 'LinksVIP.Net2014eCrVtByNgMfSvDhFjGiHoJpKlLiEuRyTtYtUbInOj9u4y81r5o26q4a0v'
	for x in range(0, md5):
		s = s + code[random.randint(0,len(code)-1)] 
    
	return s
def get_linkvips(fshare_url,username, password):
	
	host_url = 'http://linksvip.net/?ref=9669'
	login_url = 'http://linksvip.net/login/'
	logout_url = 'http://linksvip.net/login/logout.php'
	getlink_url = 'http://linksvip.net/GetLinkFs'
	
	response = fetch_data(host_url)
	if not response:
		return
	
	cookie = response.cookiestring

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
				'Cookie'		: cookie,
				'Referer'		: host_url,
				'Content-Type'	: 'application/x-www-form-urlencoded; charset=UTF-8',
				'Accept'		: 'application/json, text/javascript, */*; q=0.01',
				'X-Requested-With'	: 'XMLHttpRequest'
            }
	
	data = {
			"u"				: username,
			"p"				: password,
			"auto_login"	: 'checked'
		}

	response = fetch_data(login_url, headers, data)

	video_url = ''
	if response.status == 200:
		json_data = json.loads(response.body)
		if int(json_data['status']) == 1:
			cookie = cookie + ';' + response.cookiestring
			headers['Cookie'] = cookie
			data = {
				"link"			: fshare_url,
				"pass"			: 'undefined',
				"hash"			: get_hash(32),
				"captcha"		: ''

			}
			headers['Accept-Encoding'] = 'gzip, deflate'
			headers['Accept-Language'] = 'en-US,en;q=0.8,vi;q=0.6'
			
			response = fetch_data(getlink_url, headers, data)

			json_data = json.loads(response.body)

			link_vip = json_data['linkvip']
			
			response = fetch_data(link_vip, headers)

			match = re.search(r'id="linkvip"\stype="text"\svalue="(.*?)"', response.body)
			if not match:
				return ''
			video_url = match.group(1)
			video_url = video_url.replace("[LinksVIP.Net]", "")
			xbmc.log(video_url)
			#logout
			response = fetch_data(logout_url, headers)
			
	return video_url

def get_4share(url):
	cookie = 'SHARINGSESSID4S=hpd9hdj8j1hnaseba6uicc6ss5'
	headers = {
			'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
			'Referer': 'http://4share.vn/',
			'Host'	: '4share.vn',
			'Cookie': cookie
			}
	response = urlfetch.get(url, headers=headers)
	matches = re.search(r"text-decoration:none' href='(.+?)'", response.body)
	direct_url = matches.group(1)
	
	refer = "|User-Agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F58.0.3029.110%20Safari%2F537.36"
	return direct_url+refer
		
	
def get_fshare(url):
	response = urlfetch.get(url)
	if 'Tập tin quý khách yêu cầu không tồn tại' in response.body:
		notify('Tập tin quý khách yêu cầu không tồn tại')
		sys.exit("Error message")
	def checkpass(url):
		response = urlfetch.get(url)
		if 'Tập tin có mật khẩu bảo vệ' in response.body:
			keyboardHandle = xbmc.Keyboard('','Nhập mật khẩu bảo vệ của tập tin')
			keyboardHandle.doModal()
			if (keyboardHandle.isConfirmed()):
				queryText = keyboardHandle.getText()
				if len(queryText) == 0:
					return
				queryText = urllib.quote_plus(queryText)
				password1 = queryText
				return password1
			else:
				return
	
	url = url.replace('http://', 'https://')
	if '-' in url:
		matches = re.search(r"(http.*)-(.*)", url)
		password1 = matches.group(2)
		url = matches.group(1)
		
	else:
		password1 = checkpass(url)
		#notify(password1)

	match = re.search(r"(https://)", url)
	if not match:
		url = 'https://'+url
	else:
		url = url
		
	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')
	fshare_option = ADDON.getSetting('fshare_option')
	F = 'U2FsdGVkX1+oRjEcO06h18WuKSLFnniVhsVxR1l2aUWLmQAC3v4KfeXi5Xx5I11I'
	def check_user(session_id):
		f = 'U2FsdGVkX1+fntz3Jv92YvlUvQk6pEhgPiGKJcEBVtVH9lpd8YS6idK8G9Lr7etACq/sLnO12tI2klwOz9QQWQ'
		headers = {'cookie': "session_id="+session_id}
		response = urlfetch.get(vmf.gibberishAES(f, 'Faidemteiv'), headers=headers)
		jStr = json.loads(response.body)
		c = jStr['account_type']
		return(c)
	
	def fshare_download(url, username, password):
		payload = '{"app_key":"L2S7R6ZMagggC5wWkQhX2+aDi467PPuftWUMRFSn","user_email":"'+username+'","password":"'+password+'"}'
		headers = {'cache-control': "no-cache"}
		f = 'U2FsdGVkX1+DNcAz9bYFd5cYzmMSxkO6cjEESsnvnFDRwI/cJ7q9e3PMqRvzhaQG/3AKt6uXJwS1dzBpPGlotw'
		response = urlfetch.post(vmf.gibberishAES(f, 'Faidemteiv'), data=payload, headers=headers)
		
		if '405' in response.body:
			alert('Không đăng nhập được. Kiểm tra lại username và mật khẩu.\nUser: [COLOR yellow]' + username+'[/COLOR]\nPassword: [COLOR yellow]'+password+'[/COLOR]','Fshare thông báo')
			sys.exit	
		
		jStr = json.loads(response.body)
		code = jStr['code']
		msg = jStr['msg']
		token = jStr['token']
		session_id = jStr['session_id']
		t = check_user(session_id)
		t = str(t)
		
		if code == 200:
			notify ('Đăng nhập thành công')
			notify ('Tài khoản là: [COLOR red]'+t+'[/COLOR]')
			f = 'U2FsdGVkX1/vJ77W7WEfjOu+hZeMdqup95C+GE85n+a+y7jPpVuWQ/84LkPrQvpvA0xuchHX/FwK++XMK+EnVg'
			data   = '{"token" : "%s", "url" : "%s", "password" : "%s"}'
			header = {'Cookie' : 'session_id=' + session_id}
			data   = data % (token, url, password1)
			t = urlfetch.post(vmf.gibberishAES(f, 'Faidemteiv'), headers=header, data=data)
			jStr = json.loads(t.body)
			video_url = jStr['location']
			if not video_url:
				notify('Link hỏng')
		return video_url	
		
	def getlink(url, username, password):
		login_url = 'https://www.fshare.vn/login'
		logout_url = 'https://www.fshare.vn/logout'
		download_url = 'https://www.fshare.vn/download/get'
		notify (u'VMF Getlink system'.encode("utf-8"))
		response = fetch_data(login_url)
		if not response:
			return

		csrf_pattern = '\svalue="(.+?)".*name="fs_csrf"'

		csrf=re.search(csrf_pattern, response.body)
		fs_csrf = csrf.group(1)

		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring}
		
		data = {
				"LoginForm[email]"		: username,
				"LoginForm[password]"	: password,
				"fs_csrf"				: fs_csrf
			}

		response = fetch_data(login_url, headers, data)
		if 'Sai tên đăng nhập hoặc mật khẩu.' in response.body:
			alert('Sai tên đăng nhập hoặc mật khẩu. Xin vui lòng kiểm tra lại user và password', '[COLOR yellow]Fshare thông báo[/COLOR]')
			sys.exit
		check_acc = fetch_data('https://www.fshare.vn/account/infoaccount', headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0', 'Cookie': response.cookiestring})
		regex = r"data-target=\"#member\">(.+?)</a>"
		ma_tk=re.search(regex, check_acc.body)
		ma_tk=ma_tk.group(1)
		notify1('Tài khoản Fshare của bạn là: [COLOR red]'+ma_tk+'[/COLOR]')
		headers['Cookie'] = response.cookiestring
		headers['Referer'] = url
		direct_url = ''
		attempt = 1
		MAX_ATTEMPTS = 3
		file_id = os.path.basename(url)
		if response and response.status == 302:
			notify (u'Đang xử lý lấy link'.encode("utf-8"))
			while attempt < MAX_ATTEMPTS:
				if attempt > 1: sleep(2)
				notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
				attempt += 1

				response = fetch_data(url, headers, data)

				if response.status == 200:
					csrf=re.search(csrf_pattern, response.body)
					fs_csrf = csrf.group(1)
					data = {
							'fs_csrf'					: fs_csrf,
							'ajax'						: 'download-form',
							'DownloadForm[pwd]'			: password1,
							'DownloadForm[linkcode]'	: file_id
						}

					response=fetch_data(download_url, headers, data);

					json_data = json.loads(response.body)

					if json_data.get('url'):
						direct_url = json_data['url']
						
					elif json_data.get('msg'):
						notify(json_data['msg'].encode("utf-8"))
					else:
						notify('Kiểm tra lại user, mật khẩu, mã password')
				elif response.status == 302:
					direct_url = response.headers['location']
					
				else:
					notify (u'Lỗi khi lấy link, mã lỗi #%s. Đang thử lại...'.encode("utf-8") % response.status)

			response = fetch_data(logout_url, headers)
			if response.status == 302:
				notify (u'Done'.encode("utf-8"))
		else:
			notify (u'Lấy link không thành công.'.encode("utf-8"))
		if len(direct_url) > 0:
			notify (u'Đã lấy được link'.encode("utf-8"))
		else:
			notify (u'Có sự cố khi lấy link. Xin vui lòng thử lại'.encode("utf-8"))

		return direct_url
	#+++++++++++++++++	
	if fshare_option == "true":
		if len(username) == 0  or len(password) == 0:
			alert(u'Bạn chưa nhập [COLOR red]VMF[/COLOR] code hoặc tài khoản cá nhân Fshare'.encode("utf-8"), 'Soạn tin: [COLOR red]VMF[/COLOR] gửi [COLOR red]8798[/COLOR] để lấy VMF Code')
			return
		else:
			try:
				notify('Đang lấy link')
				#return fshare_download(url, username, password)
				return getlink(url, username, password)
			except:
				notify('Không đăng nhập được tài khoản')
				
			
	
	if fshare_option == "false":	
		if len(USER_VIP_CODE) == 0:
			alert(u'Bạn chưa có tài khoản cá nhân Fshare'.encode("utf-8"))
			return
		if len(USER_VIP_CODE) > 0:
			download_url = 'https://www.fshare.vn/download/get'
			
			try:
				response = fetch_data(VIETMEDIA_HOST + vmf.gibberishAES(F1, 'idok'))
				json_data = json.loads(response.body)
				a =json_data['ttt']
				c = a.split('|')
				for x in c:
					
					file_id = re.search(r"file\/(.+)", url).group(1)
					headers = { 
								'User-Agent' 	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
								'Cookie':'session_id='+x
							}
					response = urlfetch.get(url, headers=headers)
					if 'Tài khoản VIP là tài khoản trả tiền của Fshare' in response.body or 'Tài khoản BUNDLE là tài khoản KM theo gói Internet FPT' in response.body and 'getlink' not in response.body:
						fs_csrf = re.search(r"fs_csrf:'(.+?)'", response.body).group(1)
						headers = { 
									'User-Agent' 	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
									'Cookie':'session_id='+x
								}
						
						data = {
									'fs_csrf'					: fs_csrf,
									'ajax'						: 'download-form',
									'DownloadForm[pwd]'			: '',
									'DownloadForm[linkcode]'	: file_id,
									'underfined'				: 'underfined'
								}
						response=urlfetch.post(download_url, headers=headers, data=data);
						json_data = json.loads(response.body)
						if json_data.get('url'):
							if len(json_data['url']) > 0:
								video_url =	json_data['url']
								return (video_url)
						break			
			except Exception as e:
				alert('Sử dụng tài khoản Fshare VIP cá nhân để play. Liên hệ [COLOR yellow]vietkodi@gmail.com[/COLOR] để mua Fshare VIP', 'VMF code lỗi')
				pass									
						
			
		
def forceUpdate():
	xbmc.executebuiltin('UpdateAddonRepos()')
	xbmc.executebuiltin('UpdateLocalAddons()')
	DIALOG = xbmcgui.Dialog()
	notify('Kiểm tra cập nhật.')
	if DIALOG.yesno(ADDON_NAME, "Đi đến mục kiểm tra update hay không?", yeslabel="Go to Page", nolabel="No Thanks"):
		xbmc.executebuiltin('ActivateWindow(10040,"addons://outdated/",return)')
	return 'checkupdate'

