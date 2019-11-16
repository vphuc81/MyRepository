# -*- coding: utf-8 -*-
__author__ = 'thaitni'
import json
from utils import xread, xrw, mess, u2s, fshareKey

class fshare:
	def __init__(self, user, passwd):
		self.key  = fshareKey
		self.user   = user
		self.passwd = passwd
		cookie = xrw('fshare.cookie').split('-')
		
		try:
			self.session_id = cookie[0]
			self.token      = cookie[1]
		except:
			self.session_id = ""
			self.token      = ""
		
		self.hd = {'Cookie' : 'session_id=' + self.session_id}
		self.vip = self.getVIP(self.session_id, True)
	
	
	
		
	def results(self, url, hd = {'User-Agent':'Mozilla/5.0'}, data = None):
		try   :  j = json.loads( xread(url, hd, data) )
		except : j = {}
		return j
	
	
	
	
	def getVIP(self, session_id, refresh=False):
		hd = {'Cookie' : 'session_id=' + session_id}
		userInf = self.results("https://api2.fshare.vn/api/user/get", hd)
		
		if refresh and (not userInf or userInf.get("code", 0) == 201 or not session_id):
			self.login(self.user, self.passwd)
			return self.vip
		
		if userInf.get("account_type", "") == "Bundle":
			vip = 1
		
		elif userInf.get("expire_vip","No") == 'Forever':
			vip = 1
		
		else:
			try:
				vip = int(userInf.get("expire_vip","-1"))
			except:
				vip = -1
			
			if vip > 0: 
				from time import time
				vip = 1 if time() < vip else -1
		
		return  vip >= 0
	
	
	
	
	
	def login(self, user, passwd):
		import requests
		data   = '{"app_key" : "%s", "user_email" : "%s", "password" : "%s"}'
		data   = data % (self.key, user, passwd)
		url = "https://118.69.164.19/api/user/login"
		hd = {"Accept-Encoding": "gzip, deflate, sdch"}
		result = requests.post(url, data, headers=hd, verify=False)
		
		try:
			result = json.loads(result.content)
		except:
			result = {}
		
		
		if result.get("code", 0) == 200:
			self.session_id  = result.get("session_id")
			self.token       = result.get("token")
			self.hd = {'Cookie' : 'session_id=' + self.session_id}
			self.vip = self.getVIP(self.session_id)
			xrw('fshare.cookie', self.session_id + "-" + self.token)
			
			if self.vip:
				mess( "Login thành công", "Fshare.vn")
			else:
				mess( "Acc của bạn hết hạn VIP", "Fshare.vn")
		else:
			mess( "Login không thành công!", "Fshare.vn")
			self.vip = False
		
	
	
	
	
	def getLink(self, url, passwd = ""):
		data   = '{"token" : "%s", "url" : "%s", "password" : "%s"}'
		data   = data % (self.token, url, passwd)
		result = self.results("https://api2.fshare.vn/api/session/download", self.hd, data)
		
		link = ""
		if result.get("location"):
			link = result.get("location")
		
		elif result.get("code", 0) == 123 and not passwd:
			from utils import get_input
			passwd = get_input(u'Hãy nhập: Mật khẩu tập tin')
			if passwd:
				link = self.getLink(url, passwd)
		
		if not link:
			if "không tồn tại" in xread(url):
				mess("Tập tin quý khách yêu cầu không tồn tại")
				link = "Failed"
		
		return link
	
	
	
	
	def getLinkFree(self, url, free="true"):
		from urllib import urlencode
		from utils import addon
		data = urlencode({"url" : url, "token" : addon.getAddonInfo("id")})
		link = xread('http://thai.eu5.org', data=data)

		#if not link:
		#	link = xread('http://ycofo.xyz/newfshare.php', data=data)

		if link and link.endswith("NoVIP"):
			#mess("Bạn nhận được link No VIP")
			link = link.replace("NoVIP", "")
		
		return link





def kphim(b, url, server_id, video_id):
	from utils import xsearch, xget
	hd  = {
		'User-Agent'       : 'Mozilla/5.0',
		'X-Requested-With' : 'XMLHttpRequest',
		'Referer'          : xsearch("_linkHref\W*'(.+?)'",b)
	}
	from hashlib import md5
	ver  = xsearch("ver\W*'(.+?)'",b)
	#http://www.kphim.tv/resources/js/jrating.min.js?ver=1.1 mahoahkphim
	#tk   = "kphi" + video_id + "dcmxemvtv.net"  + ver +  server_id
	tk   = "kphi" + server_id + "dkm_get_cai_diz_con_me_may"  + ver + video_id
	tk   =	md5(tk).hexdigest()[2:]
	href = "http://www.kphim.tv/player/%s/%s/%s" % (server_id + ver, video_id + ver, tk)
	#href = "http://kzone.tv/player/%s/%s/%s" % (server_id + ver, video_id + ver, tk)
	data = 'mid=%s&vid=%s&sid=%s'%(ver, server_id, video_id)
	#import xbmc;xbmc.log("b=xread('%s',%s,'%s')"%(href,str(hd),data), xbmc.LOGNOTICE)
	return xread(href,hd,data)

def kphim1(b, url, server_id, video_id):
	hd  = {
		'User-Agent'       : 'Mozilla/5.0',
		'X-Requested-With' : 'XMLHttpRequest',
		'Referer'          : url
	}
	from hashlib import md5
	from utils import xsearch
	ver  = xsearch("ver\W*'(.+?)'",b)
	tk   = "kphi" + server_id + "dcmxemvtv.net"  + ver + video_id
	tk   =	md5(tk).hexdigest()[2:]
	href = "http://www.kphim.tv/player/%s/%s/%s" % (server_id + ver, video_id + ver, tk)
	data = 'mid=%s&vid=%s&sid=%s'%(ver,server_id,video_id)
	#import xbmc;xbmc.log("b=xread('%s',%s,'%s')"%(href,str(hd),data), xbmc.LOGNOTICE)
	return xread(href,hd,data)

def getToken(server_id, video_id, ver):
	#http://kphim.tv/resources/js/site.js?ver=37 mahoahkphim
	from hashlib import md5
	tk   = "kp" + server_id + "dung_get_em_nua" + video_id  + ver
	tk   =	md5(tk).hexdigest()[1:]
	href = "http://www.kphim.tv/player/%s/%s/%s" % (server_id + ver, video_id + ver, tk)
	return href

def getLinkTVhay(url):
	return ""

def phimnhanh(b):
	href=xsearch('link_url.+?(http.+?)"',b).replace("\\","") + xsearch('"key\W+"(.+?)"',b)
	try    : j = json.loads(xread(href))
	except : j = {}
	return j