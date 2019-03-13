# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
import requests.utils
import urllib, os, re, json, uuid
import urlresolver
import HTMLParser
from cookielib import LWPCookieJar
from kodi_six import xbmc
from urlresolver.plugins.lib import unwise
from urlresolver.plugins.lib import jsunpack
from operator import itemgetter
from cachecontrol import CacheControl

ADDON_FOLDER = xbmc.translatePath('special://home/addons')
TMP_FOLDER = xbmc.translatePath('special://temp')
WEB_CACHE = xbmc.translatePath(os.path.join(TMP_FOLDER, ".web_cache"))
DEVICE_PATH = xbmc.translatePath('special://userdata')
SEARCH_HISTORY_PATH = os.path.join(DEVICE_PATH, 'search.p')
CID_PATH = os.path.join(DEVICE_PATH, 'cid')

CHROME_DESKTOP_AGENTS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
MOBILE_IOS_AGENTS = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4"
DEFAULT_HEADERS = {
	"User-Agent": CHROME_DESKTOP_AGENTS,
	"Accept-Encoding": "gzip, deflate, sdch"
}
GA_MEDIA_TITLE_TEMPLATE = "[Browse MEDIA of] {title} ({quality}) [{mirror}] - Page {page}"
GA_MIRROR_TITLE_TEMPLATE = "[Browse MIRROR of] {title} ({quality}) [{mirror}]"
GA_EPS_TITLE_TEMPLATE = "[Browse EPS of] {title} ({quality}) [{mirror}]"
GA_PLAY_TITLE_TEMPLATE = "[Play] {title} ({quality}) - Part {eps} [{mirror}]"

GA_MEDIA_PATH_TEMPLATE = '/list_media/{url}/{payloads}'
GA_MIRROR_PATH_TEMPLATE = '/list_eps/{url}/{payloads}'
GA_EPS_PATH_TEMPLATE = '/list_mirrors/{url}/{payloads}'
GA_PLAY_PATH_TEMPLATE = '/play/{url}/{payloads}'

GA_MEDIA = [GA_MEDIA_TITLE_TEMPLATE, GA_MEDIA_PATH_TEMPLATE]
GA_MIRROR = [GA_MIRROR_TITLE_TEMPLATE, GA_MIRROR_PATH_TEMPLATE]
GA_EPS = [GA_EPS_TITLE_TEMPLATE, GA_EPS_PATH_TEMPLATE]
GA_PLAY = [GA_PLAY_TITLE_TEMPLATE, GA_PLAY_PATH_TEMPLATE]


def Request(
	url,
	method="GET",
	headers=DEFAULT_HEADERS,
	additional_headers=None,
	data=None,
	session=None,
	allow_redirects=True,
	timeout=10,
	load_cookies=True,
	mobile=False
):
	if additional_headers:
		headers.update(additional_headers)
	try:
		session = CacheControl(session)
	except Exception as e:
		pass
		# Error("Init web cache failed!!!", e)
	if mobile:
		headers["User-Agents"] = MOBILE_IOS_AGENTS
	xbmc.log("Requests headers: {0}".format(json.dumps(headers)), 1)
	if session:
		session.headers.update(headers)
		domain = re.search("https*\://(.+?)($|/)", url).group(1)
		if load_cookies:
			LoadCookies(session, cookies_name=domain)
		if data:
			response = session.post(url, data=data, allow_redirects=allow_redirects, timeout=timeout, verify=False)
		else:
			if method == "HEAD":
				response = session.head(url, allow_redirects=allow_redirects, timeout=timeout, verify=False)
			else:
				response = session.get(url, allow_redirects=allow_redirects, timeout=timeout, verify=False)
		response.encoding = "utf8"
		SaveCookies(session, cookies_name=domain)
		return response
	else:
		if method == "HEAD":
			return requests.head(url, headers=headers, allow_redirects=allow_redirects, timeout=timeout, verify=False)
		else:
			return requests.get(url, headers=headers, allow_redirects=allow_redirects, timeout=timeout, verify=False)


def RetryBlogspot(url):
	for i in range(30):
		res = Request(url, method="HEAD")
		if res.status_code < 300:
			xbmc.log("blogspot link retry successfully!", 1)
			return res.url
	raise Exception('RetryBlogspot Failed!!!')


def SaveCookies(session, cookies_name="tmp_cookies"):
	try:
		path = xbmc.translatePath(os.path.join(TMP_FOLDER, cookies_name))
		session.cookies.save(filename=path, ignore_discard=True, ignore_expires=True)
		xbmc.log("Cookies saved!",1)
	except Exception as e:
		pass
		# Error("Saving cookies failed!!!", e)


def LoadCookies(session, cookies_name="tmp_cookies"):
	try:
		path = xbmc.translatePath(os.path.join(TMP_FOLDER, cookies_name))
		session.cookies.load(filename=path, ignore_discard=True, ignore_expires=True)
	except Exception as e: pass
		# Error("Loading cookies failed!!!", e)


def Noti(header="",message="",t=10000):
	xbmc.executebuiltin(u'Notification("{0}", "{1}", "{2}", "{3}")'.format(header, message, t, ''))


def Error(message="", title="Error occurred!!!", e="", t=10000):
	Log(message)
	Log(e)
	Noti(title, message, t)


def Log(message,log_level=xbmc.LOGDEBUG):
	xbmc.log(u"[Kodi4VN] {0}".format(message), log_level)
	try:
		pass
	except Exception as e:
		xbmc.log(u"Logging Failed: {0}".format(e))
		Noti("Logging Failed!!!", e)

def GSheet2KSwift(url_path="0", sheet_id="", tq="select *"):
	query_url = "https://docs.google.com/spreadsheets/d/{sid}/gviz/tq?gid={gid}&headers=1&tq={tq}"
	if "@" in url_path:
		xbmc.log("Found gid@sid path", 1)
		url_path, sheet_id = url_path.split("@")
	url = query_url.format(
		sid = sheet_id,
		tq  = urllib.quote(tq),
		gid = url_path
	)

	res = Request(url)
	_re = "google.visualization.Query.setResponse\((.+?)\);"
	_json = json.loads(re.search(_re, res.encode("utf8")).group(1))
	


def GSRow2KSRow(gs_row):
	
	item = {}
	item["label"] = getValue(row["c"][0]).encode("utf-8")
	item["label2"] = getValue(row["c"][4])
	# Nếu phát hiện spreadsheet khác với VNOpenPlaylist
	new_path = getValue(row["c"][1])
	if "@" in url_path and "@" not in new_path and "section/" in new_path:
		gid = re.compile("section/(\d+)").findall(new_path)[0]
		new_path = re.sub(
			'section/\d+',
			'section/%s@%s' % (gid, sheet_id),
			new_path,
			flags=re.IGNORECASE
		)
	item["path"] = new_path

	item["thumbnail"] = getValue(row["c"][2])
	item["info"] = {"plot": getValue(row["c"][3])}
	if "plugin://" in item["path"]:
		if "install-repo" in item["path"]:
			item["is_playable"] = False
		elif re.search("plugin.video.thongld.vnplaylist/(.+?)/.+?\://", item["path"]):
			match = re.search(
				"plugin.video.thongld.vnplaylist(/.+?/).+?\://", item["path"])
			tmp = item["path"].split(match.group(1))
			tmp[-1] = urllib.quote_plus(tmp[-1])
			item["path"] = match.group(1).join(tmp)
			if "/play/" in match.group(1):
				item["is_playable"] = True
		elif item["path"].startswith("plugin://plugin.video.f4mTester"):
			item["is_playable"] = False
			item["path"] = pluginrootpath + \
				"/executebuiltin/" + urllib.quote_plus(item["path"])
		elif "/play/" in item["path"]:
			item["is_playable"] = True
	elif item["path"] == "":
		item["label"] = "[I]%s[/I]" % item["label"]
		item["is_playable"] = False
		item["path"] = pluginrootpath + "/executebuiltin/-"
	else:
		if "spreadsheets/d/" in item["path"]:
			# https://docs.google.com/spreadsheets/d/1zL6Kw4ZGoNcIuW9TAlHWZrNIJbDU5xHTtz-o8vpoJss/edit#gid=0
			match_cache = re.search('cache=(.+?)($|&)', item["path"])
			match_passw = re.search('passw=(.+?)($|&)', item["path"])

			sheet_id = re.compile("/d/(.+?)/").findall(item["path"])[0]
			try:
				gid = re.compile("gid=(\d+)").findall(item["path"])[0]
			except:
				gid = "0"
			item["path"] = pluginrootpath + "/section/%s@%s" % (gid, sheet_id)
			if match_cache:
				cache_version = match_cache.group(1)
				item["path"] = pluginrootpath + \
					"/cached-section/%s@%s@%s" % (gid, sheet_id, cache_version)
			elif match_passw:
				item["path"] = pluginrootpath + \
					"/password-section/%s/%s@%s" % (match_passw.group(1), gid, sheet_id)
		elif any(service in item["path"] for service in ["acelisting.in"]):
			item["path"] = pluginrootpath + \
				"/acelist/" + urllib.quote_plus(item["path"])
		elif any(service in item["path"] for service in ["fshare.vn/folder"]):
			item["path"] = pluginrootpath + "/fshare/" + \
				urllib.quote_plus(item["path"].encode("utf8"))
			# item["path"] = "plugin://plugin.video.xshare/?mode=90&page=0&url=" + urllib.quote_plus(item["path"])
		elif any(service in item["path"] for service in ["4share.vn/d/"]):
			item["path"] = "plugin://plugin.video.xshare/?mode=38&page=0&url=" + \
				urllib.quote_plus(item["path"])
		elif any(service in item["path"] for service in ["4share.vn/f/"]):
			# elif any(service in item["path"] for service in ["4share.vn/f/", "fshare.vn/file"]):
			item["path"] = "plugin://plugin.video.xshare/?mode=3&page=0&url=" + \
				urllib.quote_plus(item["path"])
			item["is_playable"] = True
			item["path"] = pluginrootpath + "/play/" + urllib.quote_plus(item["path"])
		elif "youtube.com/channel" in item["path"]:
			# https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ
			yt_route = "ytcp" if "playlists" in item["path"] else "ytc"
			yt_cid = re.compile("youtube.com/channel/(.+?)$").findall(item["path"])[0]
			item["path"] = "plugin://plugin.video.kodi4vn.launcher/%s/%s/" % (
				yt_route, yt_cid)
			item["path"] = item["path"].replace("/playlists", "")
		elif "youtube.com/playlist" in item["path"]:
			# https://www.youtube.com/playlist?list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI
			yt_pid = re.compile("list=(.+?)$").findall(item["path"])[0]
			item["path"] = "plugin://plugin.video.kodi4vn.launcher/ytp/%s/" % yt_pid
		elif any(ext in item["path"] for ext in [".png", ".jpg", ".bmp", ".jpeg"]):
			item["path"] = "plugin://plugin.video.kodi4vn.launcher/showimage/%s/" % urllib.quote_plus(
				item["path"])
		elif re.search("\.ts$", item["path"]):
			item["path"] = "plugin://plugin.video.f4mTester/?url=%s&streamtype=TSDOWNLOADER&use_proxy_for_chunks=True&name=%s" % (
				urllib.quote(item["path"]),
				urllib.quote_plus(item["label"])
			)
			item["path"] = pluginrootpath + \
				"/executebuiltin/" + urllib.quote_plus(item["path"])
		else:
			# Nếu là direct link thì route đến hàm play_url
			item["is_playable"] = True
			item["path"] = pluginrootpath + "/play/" + urllib.quote_plus(item["path"])
	if item["label2"].startswith("http"):
		item["path"] += "?sub=" + urllib.quote_plus(item["label2"].encode("utf8"))
	return item


def Create_cid():
	if not os.path.exists(DEVICE_PATH):
		os.mkdir(DEVICE_PATH)
	if not os.path.exists(CID_PATH):
		with open(CID_PATH, "w") as f:
			f.write(str(uuid.uuid1()))


def Dict2String(template, args_json):
	from collections import defaultdict
	import string
	s = string.Formatter().vformat(template, (), defaultdict(str, args_json))
	return s


def GA(plugin_name, ga_template, args_json):
	try:
		title = Dict2String(ga_template[0], args_json)
		page = Dict2String(ga_template[1], args_json)
		plugin_name = plugin_name
		ga_url = "http://www.google-analytics.com/collect"
		client_id = ""
		if not os.path.exists(CID_PATH):
			Create_cid()
		with open(CID_PATH, "r") as f:
			client_id = f.read()
		data = {
			'v': '1',
			'tid': 'UA-52209804-5',
			'cid': client_id,
			't': 'pageview',
			'dp': "{0}{1}".format(plugin_name, page).encode("utf8","ignore"),
			'dt': "[{0}] - {1}".format(plugin_name, title).encode("utf8","ignore")
		}
		requests.post(ga_url, data=urllib.urlencode(data))
		Log("GA dp: {0}".format(data["dp"].decode("utf8","ignore")), 1)
		Log("GA dt: {0}".format(data["dt"].decode("utf8","ignore")), 1)
	except Exception as e: Error("GA Failed!!!", e)


def removeDup(items):
	seen = set()
	new_items = []
	for d in items:
		t = tuple(d.items())
		if t not in seen:
			seen.add(t)
			new_items.append(d)
	return new_items


def sort_gk_links(links):
	return sorted(links, key=itemgetter('label'), reverse=True)


def resolve(url):
	return urlresolver.resolve(url)


def getGDriveQuality(url, userAgent, hq):
	headers = {
		'User-Agent': userAgent,
		'Accept-Encoding': 'gzip, deflate, sdch',
	}
	res = requests.get(url, headers=headers)
	match = re.compile('(\["fmt_stream_map".+?\])').findall(res.text)[0]
	prefer_quality = ["38", "37", "46", "22", "45", "18", "43"]
	if not hq:
		reversed(prefer_quality)
	stream_map = json.loads(match)[1].split(",")
	for q in prefer_quality:
		for stream in stream_map:
			if stream.startswith(q+"|"):
				url = stream.split("|")[1]
				tail = "|User-Agent=%s&Cookie=%s" % (urllib.quote(
					chrome_user_agent), urllib.quote(res.headers['set-cookie']))
				return url + tail
	raise ValueError('NaN')


def join_items(items):
	d = {}
	for v,k in items:
		d.setdefault(k, [k]).append(v)
	return map(tuple, d.values())


def quality_convert(item, default=99999):
	try:
		if "label" in item:
			return int(re.search(r'\d+', item["label"]).group(0))
		else:
			return int(re.search(r'\d+', item).group(0))
	except:
		return default


def cleanHTML(s):
	s = ''.join(s.splitlines()).replace('\'', '"')
	s = s.replace('\n', '')
	s = s.replace('\t', '')
	s = re.sub('  +', ' ', s)
	s = s.replace('> <', '><')
	return HTMLParser.HTMLParser().unescape(s)


def stripHTML(s):
	q = re.compile(r'<.*?>', re.IGNORECASE)
	s = re.sub(q, '', s)
	return s.strip()


def String(s):
	try:
		return str(s)
	except:
		try:
			return str(s.encode('utf-8','ignore'))
		except:
			try:
				return str(s.decode('utf-8','ignore').encode('utf-8','ignore'))
			except:
				xbmc.log("Convert to string failed!!!", 1)
				return s


def UnWise(src):
	return unwise.unwise_process(src)


def JSunpack(src):
	#	import resolveurl
	#	from resolveurl.plugins.lib import jsunpack
	return jsunpack.unpack(src)


def xsearch(pattern, string, group=1, flags=0, result=''):
	try:
		s = re.search(pattern, string, flags).group(group)
	except:
		s = result
	return s


def gibberishAES(string, key=''):
	import ctypes

	def aa(l, s=4):
		a = []
		for i in range(0, len(l), s):
			a.append((l[i:i+s]))
		return a

	def j2p(v): return ctypes.c_int(v).value

	def rshift(val, n): return (val % 0x100000000) >> n

	e = 14
	r = 8
	n = False

	def f(e):
		# try:result=urllib.quote(e)
		# except:result=str(e)
		return str(e)

	def c(e):
		# try:result=urllib.quote(e, safe='~()*!.\'')
		# except:result=str(e)
		return str(e)

	def t(e):
		f = [0]*len(e)
		if 16 > len(e):
			r = 16 - len(e)
			f = [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r]
		for n in range(len(e)):
			f[n] = e[n]
		return f

	def o(e):
		n = ""
		for r in len(e):
			n += ("0" if 16 > e[r] else "") + format(e[r], 'x')
		return n

	def u(e, r):
		c = []
		if not r:
			e = f(e)
		for n in range(len(e)):
			c.append(ord(e[n]))
		return c

	def i(n):
		if n == 128:
			e = 10
			r = 4
		elif n == 192:
			e = 12
			r = 6
		elif n == 256:
			e = 14
			r = 8

	def b(e):
		n = []
		for r in range(e):
			n.append(256)
		return n

	def h(n, f):
		d = []
		t = 3 if e >= 12 else 2
		i = n + f
		d.append(L(i))
		u = [c for c in d[0]]
		for c in range(1, t):
			d.append(L(d[c - 1] + i))
			u += d[c]
		return {'key': u[0: 4 * r], 'iv': u[4 * r: 4 * r + 16]}

	def a1(e, r=False):
		c = ""
		if (r):
			n = e[15]
			# if n > 16:print "Decryption error: Maybe bad key"
			if 16 != n:
				for f in range(16 - n):
					c += chr(e[f])
		else:
			for f in range(16):
				c += chr(e[f])
		return c

	def a(e, r=False):
		if not r:
			c = ''.join(chr(e[f])for f in range(16))
		elif 16 != e[15]:
			c = ''.join(chr(e[f]) for f in range(16-e[15]))
		else:
			c = ''
		return c

	def v(e, r, n, f=''):
		r = S(r)
		o = len(e) / 16
		u = [0]*o
		d = [e[16 * t: 16 * (t + 1)] for t in range(o)]
		for t in range(len(d) - 1, -1, -1):
			u[t] = p(d[t], r)
			u[t] = x(u[t], n) if 0 == t else x(u[t], d[t - 1])

		i = ''.join(a(u[t]) for t in range(o-1))
		i += a(u[o-1], True)
		return i if f else c(i)

	def s(r, f):
		n = False
		t = M(r, f, 0)
		for c in (1, e + 1, 1):
			t = g(t)
			t = y(t)
			if e > c:
				t = k(t)
			t = M(t, f, c)
		return t

	def p(r, f):
		n = True
		t = M(r, f, e)
		for c in range(e - 1, -1, -1):
			t = y(t, n)
			t = g(t, n)
			t = M(t, f, c)
			if c > 0:
				t = k(t, n)
		return t

	def g(e, n=True):  # OK
		f = D if n else B
		c = [0]*16
		for r in range(16):
			c[r] = f[e[r]]
		return c

	def y(e, n=True):
		f = []
		if n:
			c = [0, 13, 10, 7, 4, 1, 14, 11, 8, 5, 2, 15, 12, 9, 6, 3]
		else:
			c = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]
		for r in range(16):
			f.append(e[c[r]])
		return f

	def k(e, n=True):
		f = [0]*16
		if (n):
			for r in range(4):
				f[4 * r] = F[e[4 * r]] ^ R[e[1 + 4 * r]
										   ] ^ j[e[2 + 4 * r]] ^ z[e[3 + 4 * r]]
				f[1 + 4 * r] = z[e[4 * r]] ^ F[e[1 + 4 * r]
											   ] ^ R[e[2 + 4 * r]] ^ j[e[3 + 4 * r]]
				f[2 + 4 * r] = j[e[4 * r]] ^ z[e[1 + 4 * r]
											   ] ^ F[e[2 + 4 * r]] ^ R[e[3 + 4 * r]]
				f[3 + 4 * r] = R[e[4 * r]] ^ j[e[1 + 4 * r]
											   ] ^ z[e[2 + 4 * r]] ^ F[e[3 + 4 * r]]
		else:
			for r in range(4):
				f[4 * r] = E[e[4 * r]] ^ U[e[1 + 4 * r]
										   ] ^ e[2 + 4 * r] ^ e[3 + 4 * r]
				f[1 + 4 * r] = e[4 * r] ^ E[e[1 + 4 * r]
											] ^ U[e[2 + 4 * r]] ^ e[3 + 4 * r]
				f[2 + 4 * r] = e[4 * r] ^ e[1 + 4 *
											r] ^ E[e[2 + 4 * r]] ^ U[e[3 + 4 * r]]
				f[3 + 4 * r] = U[e[4 * r]] ^ e[1 + 4 *
											   r] ^ e[2 + 4 * r] ^ E[e[3 + 4 * r]]
		return f

	def M(e, r, n):  # OK
		c = [0]*16
		for f in range(16):
			c[f] = e[f] ^ r[n][f]
		return c

	def x(e, r):
		f = [0]*16
		for n in range(16):
			f[n] = e[n] ^ r[n]
		return f

	def S(n):  # r=8;e=14
		o = [[n[4 * f + i] for i in range(4)] for f in range(r)]

		for f in range(r, 4 * (e + 1)):
			d = [t for t in o[f-1]]
			if 0 == f % r:
				d = m(w(d))
				d[0] ^= K[f / r - 1]
			elif r > 6 and 4 == f % r:
				d = m(d)
			o.append([o[f - r][t] ^ d[t] for t in range(4)])

		u = []
		for f in range(e + 1):
			u.append([])
			for a in range(4):
				u[f] += o[4 * f + a]
		return u

	def m(e):
		return [B[e[r]] for r in range(4)]

	def w(e):
		e.insert(4, e[0])
		e.remove(e[4])
		return e

	def A(e, r): return [int(e[n:n+r], 16) for n in range(0, len(e), r)]

	def C(e):
		n = [0]*len(e)
		for r in range(len(e)):
			n[e[r]] = r
		return n

	def I(e, r):
		f = 0
		for n in range(8):
			f = f ^ e if 1 == (1 & r) else f
			e = j2p(283 ^ e << 1) if e > 127 else j2p(e << 1)
			r >>= 1
		return f

	def O(e):
		n = [0]*256
		for r in range(256):
			n[r] = I(e, r)
		return n

	B = A("637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b27509832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cfd0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdbe0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9ee1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16", 2)
	D = C(B)
	K = A("01020408102040801b366cd8ab4d9a2f5ebc63c697356ad4b37dfaefc591", 2)
	E = O(2)
	U = O(3)
	z = O(9)
	R = O(11)
	j = O(13)
	F = O(14)

	def H(e, r, n=''):
		f = decode(e)
		c = f[8: 16]
		t = h(u(r, n), c)
		a = t['key']
		o = t['iv']
		f = f[16: len(f)]
		return v(f, a, o, n)

	def decode(r):  # OK
		def indexOfchar(n):
			try:
				a = e.index(r[n])
			except:
				a = -1
			return a

		e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
		r = r.replace('\n', '')
		f = []
		c = [0]*4
		for n in range(0, len(r), 4):
			for i in range(len(c)):
				c[i] = indexOfchar(n+i)
			f.append(j2p(c[0] << 2 | c[1] >> 4))
			f.append(j2p((15 & c[1]) << 4 | c[2] >> 2))
			f.append(j2p((3 & c[2]) << 6 | c[3]))
		return f[0:len(f)-len(f) % 16]

	def L(e):
		def r(e, r): return j2p(e << r) | j2p(rshift(e, 32-r))

		def n(e, r):
			c = 2147483648 & e
			t = 2147483648 & r
			n = 1073741824 & e
			f = 1073741824 & r
			a = (1073741823 & e) + (1073741823 & r)
			i = 2147483648 ^ a ^ c ^ t
			j = 3221225472 ^ a ^ c ^ t
			k = 1073741824 ^ a ^ c ^ t
			return j2p(i if n & f else ((j if 1073741824 & a else k) if n | f else a ^ c ^ t))

		def f(e, r, n): return j2p(e & r) | j2p(~e & n)

		def c(e, r, n): return j2p(e & n) | j2p(r & ~n)

		def t(e, r, n): return e ^ r ^ n

		def a(e, r, n): return r ^ (e | ~n)

		def o(e, c, t, a, o, d, u):
			e = n(e, n(n(f(c, t, a), o), u))
			return n(r(e, d), c)

		def d(e, f, t, a, o, d, u):
			e = n(e, n(n(c(f, t, a), o), u))
			return n(r(e, d), f)

		def u(e, f, c, a, o, d, u):
			e = n(e, n(n(t(f, c, a), o), u))
			return n(r(e, d), f)

		def i(e, f, c, t, o, d, u):
			e = n(e, n(n(a(f, c, t), o), u))
			return n(r(e, d), f)

		def b(e):
			n = len(e)
			f = n + 8
			c = (f - f % 64) / 64
			t = 16 * (c + 1)
			a = [0]*t
			o = 0
			for d in range(n):
				r = (d - d % 4) / 4
				o = 8 * (d % 4)
				a[r] = a[r] | j2p(e[d] << o)
			d += 1
			r = (d - d % 4) / 4
			o = 8 * (d % 4)
			a[r] = a[r] | j2p(128 << o)
			a[t - 2] = j2p(n << 3)
			a[t - 1] = j2p(rshift(n, 29))
			return a

		def h(e):
			f = []
			for n in range(4):
				r = j2p(255 & rshift(e, 8 * n))
				f.append(r)
			return f

		m = A("67452301efcdab8998badcfe10325476d76aa478e8c7b756242070dbc1bdceeef57c0faf4787c62aa8304613fd469501698098d88b44f7afffff5bb1895cd7be6b901122fd987193a679438e49b40821f61e2562c040b340265e5a51e9b6c7aad62f105d02441453d8a1e681e7d3fbc821e1cde6c33707d6f4d50d87455a14eda9e3e905fcefa3f8676f02d98d2a4c8afffa39428771f6816d9d6122fde5380ca4beea444bdecfa9f6bb4b60bebfbc70289b7ec6eaa127fad4ef308504881d05d9d4d039e6db99e51fa27cf8c4ac5665f4292244432aff97ab9423a7fc93a039655b59c38f0ccc92ffeff47d85845dd16fa87e4ffe2ce6e0a30143144e0811a1f7537e82bd3af2352ad7d2bbeb86d391", 8)
		S = []
		S = b(e)
		y = m[0]
		k = m[1]
		M = m[2]
		x = m[3]
		l = 0
		for l in range(0, len(S), 16):
			v = y
			s = k
			p = M
			g = x
			y = o(y, k, M, x, S[l + 0], 7, m[4])
			x = o(x, y, k, M, S[l + 1], 12, m[5])
			M = o(M, x, y, k, S[l + 2], 17, m[6])
			k = o(k, M, x, y, S[l + 3], 22, m[7])
			y = o(y, k, M, x, S[l + 4], 7, m[8])
			x = o(x, y, k, M, S[l + 5], 12, m[9])
			M = o(M, x, y, k, S[l + 6], 17, m[10])
			k = o(k, M, x, y, S[l + 7], 22, m[11])
			y = o(y, k, M, x, S[l + 8], 7, m[12])
			x = o(x, y, k, M, S[l + 9], 12, m[13])
			M = o(M, x, y, k, S[l + 10], 17, m[14])
			k = o(k, M, x, y, S[l + 11], 22, m[15])
			y = o(y, k, M, x, S[l + 12], 7, m[16])
			x = o(x, y, k, M, S[l + 13], 12, m[17])
			M = o(M, x, y, k, S[l + 14], 17, m[18])
			k = o(k, M, x, y, S[l + 15], 22, m[19])
			y = d(y, k, M, x, S[l + 1], 5, m[20])
			x = d(x, y, k, M, S[l + 6], 9, m[21])
			M = d(M, x, y, k, S[l + 11], 14, m[22])
			k = d(k, M, x, y, S[l + 0], 20, m[23])
			y = d(y, k, M, x, S[l + 5], 5, m[24])
			x = d(x, y, k, M, S[l + 10], 9, m[25])
			M = d(M, x, y, k, S[l + 15], 14, m[26])
			k = d(k, M, x, y, S[l + 4], 20, m[27])
			y = d(y, k, M, x, S[l + 9], 5, m[28])
			x = d(x, y, k, M, S[l + 14], 9, m[29])
			M = d(M, x, y, k, S[l + 3], 14, m[30])
			k = d(k, M, x, y, S[l + 8], 20, m[31])
			y = d(y, k, M, x, S[l + 13], 5, m[32])
			x = d(x, y, k, M, S[l + 2], 9, m[33])
			M = d(M, x, y, k, S[l + 7], 14, m[34])
			k = d(k, M, x, y, S[l + 12], 20, m[35])
			y = u(y, k, M, x, S[l + 5], 4, m[36])
			x = u(x, y, k, M, S[l + 8], 11, m[37])
			M = u(M, x, y, k, S[l + 11], 16, m[38])
			k = u(k, M, x, y, S[l + 14], 23, m[39])
			y = u(y, k, M, x, S[l + 1], 4, m[40])
			x = u(x, y, k, M, S[l + 4], 11, m[41])
			M = u(M, x, y, k, S[l + 7], 16, m[42])
			k = u(k, M, x, y, S[l + 10], 23, m[43])
			y = u(y, k, M, x, S[l + 13], 4, m[44])
			x = u(x, y, k, M, S[l + 0], 11, m[45])
			M = u(M, x, y, k, S[l + 3], 16, m[46])
			k = u(k, M, x, y, S[l + 6], 23, m[47])
			y = u(y, k, M, x, S[l + 9], 4, m[48])
			x = u(x, y, k, M, S[l + 12], 11, m[49])
			M = u(M, x, y, k, S[l + 15], 16, m[50])
			k = u(k, M, x, y, S[l + 2], 23, m[51])
			y = i(y, k, M, x, S[l + 0], 6, m[52])
			x = i(x, y, k, M, S[l + 7], 10, m[53])
			M = i(M, x, y, k, S[l + 14], 15, m[54])
			k = i(k, M, x, y, S[l + 5], 21, m[55])
			y = i(y, k, M, x, S[l + 12], 6, m[56])
			x = i(x, y, k, M, S[l + 3], 10, m[57])
			M = i(M, x, y, k, S[l + 10], 15, m[58])
			k = i(k, M, x, y, S[l + 1], 21, m[59])
			y = i(y, k, M, x, S[l + 8], 6, m[60])
			x = i(x, y, k, M, S[l + 15], 10, m[61])
			M = i(M, x, y, k, S[l + 6], 15, m[62])
			k = i(k, M, x, y, S[l + 13], 21, m[63])
			y = i(y, k, M, x, S[l + 4], 6, m[64])
			x = i(x, y, k, M, S[l + 11], 10, m[65])
			M = i(M, x, y, k, S[l + 2], 15, m[66])
			k = i(k, M, x, y, S[l + 9], 21, m[67])
			y = n(y, v)
			k = n(k, s)
			M = n(M, p)
			x = n(x, g)
		return h(y)+h(k)+h(M)+h(x)

	def recode(b):
		def getcode(s):
			w, i, s, e = s.split(',')
			a = b = c = 0
			d = []
			f = []
			while True:
				if a < 5:
					f.append(w[a])
				elif a < len(w):
					d.append(w[a])
				a += 1

				if b < 5:
					f.append(i[b])
				elif b < len(i):
					d.append(i[b])
				b += 1

				if c < 5:
					f.append(s[c])
				elif c < len(s):
					d.append(s[c])
				c += 1

				if len(w) + len(i) + len(s) + len(e) == len(d) + len(f) + len(e):
					break

			k = ''.join(s for s in d)
			m = ''.join(s for s in f)
			b = 0
			o = []
			for a in range(0, len(d), 2):
				n = -1
				if ord(m[b]) % 2:
					n = 1
				o.append(chr(int(k[a:a+2], 36) - n))
				b += 1
				if b >= len(f):
					b = 0
			return ''.join(s for s in o)
		l = 0
		while l < 5 or 'decodeLink' not in b:
			try:
				b = getcode(
					xsearch("(\w{100,},\w+,\w+,\w+)", b.replace("'", '')))
				l += 1
			except:
				break
		return b

	return H(string, key) if key else recode(string)
