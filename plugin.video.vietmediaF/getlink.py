# -*- coding: utf-8 -*-
#https://www.facebook.com/groups/vietkodi/

import re
import urlfetch
import os
from time import sleep
from addon import notify, alert, ADDON
import simplejson as json
import random
import xbmc
from config import VIETMEDIA_HOST


USER_VIP_CODE = ADDON.getSetting('user_vip_code')

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
	if 'hdsieunhanh.com' in url:
		return get_hdsieunhanh(url)
	if '//vn.tvnet.gov.vn' in url:
		return get_tvnet(url)
	if '//kenh1.mobifone.com.vn' in url:
		return get_mobifone(url)
	if '//thvl.vn' in url:
		return get_thvl(url)
	if 'link.tvmienphi.biz' in url:
		return get_tvmienphi(url)
	if 'serverthunghiem' in url:
		return get_serverthunghiem(url)
	if 'web.tv24.vn' in url:
		return get_servertv24(url)
	else:
		return url


		
def get_fptplay(url):
	headers = { 
				'Referer'			: url,
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
		response = fetch_data('https://fptplay.net/show/getlinklivetv', headers, data)
		if response:
			return json.loads(response.body)['stream']+'|User-Agent=Mozilla'
			
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

	response = fetch_data('https://fptplay.net/show/getlink', headers, data)
	
	if response:
		json_data = json.loads(response.body)
		return json_data['stream']+'|User-Agent=VMF'
		
	pass

def get_vtvgo(url):
	response = urlfetch.get(url)
	cookie=response.cookiestring;
	match = re.search(re.compile(r"(xem-video)"), url)

	if not match:
		
		epgid = re.search(re.compile(ur'vtv\d-(.*?)\.'), url).group(1)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': url, 'X-Requested-With'  : 'XMLHttpRequest'}  
		data = {'epg_id': epgid, 'type':'1'}
		response = urlfetch.get('http://vtvgo.vn//get-program-channel?epg_id=' +epgid +'&type=1', headers=headers, data=data)
		json_data = json.loads(response.body)
		video_url = json_data['data']
		
	else:
		video_url = re.search(re.compile(r"addPlayer\('(.*?)'"), response.body).group(1)
	return video_url

def get_htvonline(url):
	response = fetch_data(url)
	cookie=response.cookiestring;
	if not response:
		return ''
	match = re.search(re.compile(r'data-source=\"(.*?)\"'), response.body)
	if not match:
		return ''
	video_url = match.group(1)
	xbmc.log(video_url)
	return video_url	

def get_servertv24(url):
	response = urlfetch.get('http://web.tv24.vn/')
	cookie=response.cookiestring;
	channelid = re.search(re.compile(r"\/(\d+)\/"), url).group(1)
	headers = {'Host': 'web.tv24.vn', 'Accept-Encoding': 'gzip, deflate, compress, identity, *', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0', 'Cookie': cookie, 'Referer': 'http://web.tv24.vn/dang-nhap'}
	data = {'mobile': '0907280386', 'password': '123456'}
	urlfetch.post('http://web.tv24.vn/client/login/process', headers=headers, data=data)
	data = {'channel_id': channelid}
	response = urlfetch.post('http://web.tv24.vn/client/channel/link', headers=headers, data=data)
	json_data = json.loads(response.body)
	video_url = json_data['data']['PLAY_URL']
	return video_url
	
	
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
	if not response:
		return ''
	match = re.search(re.compile(ur'file:\s"(.*?)"'), response.body)
	if not match:
		return ''
	video_url = match.group(1)
	return video_url	

def get_phim3s(url):
	match = re.search(re.compile(r'\/(xem-phim\/)'), url)
	if match:
		url = url
	else:
		url = url +'xem-phim/'
	response = fetch_data(url)
	if not response:
		return ''
	cookie = response.cookiestring;
	match = re.search(re.compile(ur'data-id="(.*?)"'), response.body)
	espisodeid = match.group(1)
	match = re.search(re.compile(r'data-film-id="(.*?)"'), response.body)
	filmid = match.group(1)
	import time
	ti = (int(time.time()*1000))
	data = {'espisode_id': espisodeid, '_': ti,}
	headers = { 
					'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
					'Cookie'			: response.cookiestring,
					'Referer'			: url,
					'X-Requested-With'	: 'XMLHttpRequest'
								   }
	
	response = fetch_data('http://phim3s.net/ajax/episode/embed/?episode_id=' +espisodeid, data=data, headers=headers)
	json_data = json.loads(response.body)
	google_url = json_data['video_url_hash']
	encode_url = 'http://sub2.phim3s.net/v3/?link=' +google_url+'&json=1&s=44'
	data = {'link': google_url, 'json': '1', 's': '44'}
	headers = { 
				'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
				'Cookie'			: cookie,
				'Referer'			: url,
    			'X-Requested-With'	: 'XMLHttpRequest'
                               }
	response = urlfetch.get(encode_url, data=data, headers=headers)
	match = re.search(re.compile(r'"file_o":"(.*?)"'), response.body)
	video_url = match.group(1)+'.mp4'
	response = urlfetch.get(video_url.replace("\/", "/", 3))
	video_url = response.headers['location']
	return video_url
	
def get_hdsieunhanh(url):
	if 'hdsieunhanh.com.auto' in url:
		response = urlfetch.get('http://www.hdsieunhanh.com/phim-le.html')
		url = re.search(r'<a\sclass=\".*?\"\shref=\"(.*?)\"', response.body).group(1)
	else:
		url = url
		
	match = re.search(re.compile(r'-(\d+.*?)\.html'), url)
	pid = match.group(1)
	response = urlfetch.get(url)
	cookie = response.cookiestring;
	response = urlfetch.get('http://ip.hdsieunhanh.com/')
	match = re.search(re.compile(r"'(.*?)'"), response.body)
	yourip = match.group(1)
	headers = { 
				'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
				'Cookie'			: cookie,
				'Referer'			: url,
    			'X-Requested-With'	: 'XMLHttpRequest'
				}
	data = {'ip': yourip, 'fix': '1'}
	response = urlfetch.get('http://www.hdsieunhanh.com/getsource/' +pid +'?ip=' +yourip +'&fix=1', headers=headers, data=data)
	json_data = json.loads(response.body)
	video_url = json_data[0]['file']
	return video_url

def get_tvnet(url):
	get_url = 'http://118.107.85.21:1337/get-stream.json?p=smil:'+re.search(r'\d\/(.*?)\.htm', url).group(1).lower()+'.smil&t=l'
	response = urlfetch.get(get_url)
	json_data = json.loads(response.body)
	video_url = json_data[0]['url']
	return video_url
	
def get_mobifone(url):
	video_url = re.search(r'file:\s\"(.*?)\"', fetch_data(url).body).group(1)
	return video_url

def get_htvplus(url):
	response = urlfetch.get(url)
	if not response:
		return ''
	match = re.search(re.compile(r'iosUrl\s=\s\"(.*?)\"'), response.body)
	linklive = match.group(1)
	xbmc.log(linklive)
	cookie=response.cookiestring;
	headers = { 
				'User-Agent'		: 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
				'Cookie'			: cookie,
				'Referer'			: url,
    			'X-Requested-With'	: 'XMLHttpRequest'
				
            }
	data={'url':linklive,'type':'1'}
	response = urlfetch.post('http://hplus.com.vn/content/getlinkvideo/',data=data, headers=headers)
	if not response:
		return ''
	video_url = response.content
	xbmc.log(video_url)
	return video_url+'|User-Agent=VMF'	
		
def get_hdonline(url):
	attempt = 1
	MAX_ATTEMPTS = 5
	
	xbmc.log(url)

	while attempt < MAX_ATTEMPTS:
		if attempt > 1: 
			sleep(2)
		url_play = ''
		notify (u'Lấy link lần thứ #%s'.encode("utf-8") % attempt)
		attempt += 1
		response = fetch_data(url)
		if not response:
			return ''

		match = re.search(r'\-(\d+)\.?\d*?\.html$', url)
		if not match:
			return ''
		fid = match.group(1)

		match = re.search(r'\-tap-(\d+)-[\d.]+?\.html$', url)
		if not match:
			ep = 1
		else:
			ep = match.group(1)
		
		match = re.search(r'\|(\w{86}|\w{96})\|', response.body)
		if match:
			token = match.group(1)
			
			match = re.search(r'\|14(\d+)\|', response.body)
			token_key = '14' + match.group(1)
			
			token = token + '-' + token_key

			_x = random.random()
			url_play = ('http://hdonline.vn/frontend/episode/xmlplay?ep=%s&fid=%s&format=json&_x=%s&token=%s' % (ep, fid, _x, token))
			break
		else:
			match = re.search(r'"file":"(.*?)","', response.body)
			if match:
				url_play = 'http://hdonline.vn' + match.group(1).replace('\/','/') + '&format=json'
				url_play = url_play.replace('ep=1','ep=' + str(ep))
				break
	if len(url_play) == 0:
		notify (u'Không lấy được link.')
		return ''

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
				'Referer'		: url,
				'Accept'		: 'application/json, text/javascript, */*; q=0.01',
				'Cookie'		: response.cookiestring
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
	
	xbmc.log(video_url)

	if len(subtitle_url) > 0:		
		subtitle_url = ('http://data.hdonline.vn/api/vsub.php?url=%s' % subtitle_url)
		return video_url + "[]" + subtitle_url
	else:
		return video_url

def get_hash(m):
	md5 = m or 9
	s = ''
	code = 'LinksVIP.Net2014eCrVtByNgMfSvDhFjGiHoJpKlLiEuRyTtYtUbInOj9u4y81r5o26q4a0v'
	for x in range(0, md5):
		s = s + code[random.randint(0,len(code)-1)] 
    
	return s
def get_linkvips(fshare_url,username, password):
	host_url = 'http://linksvip.net'
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

def get_fshare(url):
	login_url = 'https://www.fshare.vn/login'
	logout_url = 'https://www.fshare.vn/logout'
	download_url = 'https://www.fshare.vn/download/get'

	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')

	direct_url = ''
	if len(username) == 0  or len(password) == 0:
		try:
			url_account = VIETMEDIA_HOST + '?action=fshare_account_linkvips'
			response = fetch_data(url_account)
			json_data = json.loads(response.body)
			username = json_data['username']
			password = json_data['password']

			if len(username) > 0  and len(password) > 0:
				direct_url = get_linkvips(url, username,password)
				if len(direct_url) > 0:
					notify(u'Lấy link fshare VIP thành công.'.encode("utf-8"))
					return direct_url
		except:
			pass

	if len(username) == 0  or len(password) == 0:
		alert(u'Bạn chưa nhập tài khoản VIP fshare, hoặc phải có VIP code. Soạn tin: VMF gửi 8698 hoặc Paypal to vietkodi@gmail.com'.encode("utf-8"))
		return

	response = fetch_data(login_url)
	if not response:
		return

	csrf_pattern = '\svalue="(.+?)".*name="fs_csrf"'

	csrf=re.search(csrf_pattern, response.body)
	fs_csrf = csrf.group(1)

	headers = { 
				'User-Agent' 	: 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36 VietMedia/1.0',
				'Cookie'		: response.cookiestring
            }
	
	data = {
			"LoginForm[email]"		: username,
			"LoginForm[password]"	: password,
			"fs_csrf"				: fs_csrf
		}

	response = fetch_data(login_url, headers, data)
	headers['Cookie'] = response.cookiestring
	headers['Referer'] = url
	
	attempt = 1
	MAX_ATTEMPTS = 8
	file_id = os.path.basename(url)
	if response and response.status == 302:
		notify (u'Đăng nhập fshare thành công'.encode("utf-8"))
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
						'DownloadForm[linkcode]'	: file_id
					}
				
				response=fetch_data(download_url, headers, data);
				
				json_data = json.loads(response.body)
				
				if json_data.get('url'):
					direct_url = json_data['url']
					break
				elif json_data.get('msg'):
					notify(json_data['msg'].encode("utf-8"))
			elif response.status == 302:
				direct_url = response.headers['location']
				break
			else:
				notify (u'Lỗi khi lấy link, mã lỗi #%s. Đang thử lại...'.encode("utf-8") % response.status) 

		response = fetch_data(logout_url, headers)
		if response.status == 302:
			notify (u'Đăng xuất fshare thành công'.encode("utf-8"))
	else:
		notify (u'Đăng nhập không thành công, kiểm tra lại tài khoản'.encode("utf-8"))
	if len(direct_url) > 0:
		notify (u'Đã lấy được link'.encode("utf-8"))
	else:
		notify (u'Không được link, bạn vui lòng kiểm tra lại tài khoản'.encode("utf-8"))

	return direct_url
