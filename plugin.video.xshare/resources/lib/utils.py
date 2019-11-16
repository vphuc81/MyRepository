# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, xbmcgui, urllib2, json
re=urllib2.re
os=urllib2.os
addon= xbmcaddon.Addon()
profile=xbmc.translatePath(addon.getAddonInfo('profile'))
iconpath=os.path.join(profile,'icon')
datapath=os.path.join(profile,'data')
tempfolder=xbmc.translatePath('special://temp')
xsharefolder=os.path.join(profile,'xshare')
icon=os.path.join(profile,'icon','icon.png')
fshareKey = "z9M2xoA93ZUSA7CX5x4h0IjQLDFVvRG7JYXbWmgB"
media_ext=['aif','iff','m3u','m3u8','m4a','mid','mp3','mpa','ra','wav','wma','3g2','3gp','asf','asx','avi','flv','mov','mp4','mpg','mkv','m4v','rm','swf','vob','wmv','bin','cue','dmg','iso','mdf','toast','vcd','ts','flac','m2ts','dtshd','nrg']
color={'fshare':'[COLOR gold]','vaphim':'[COLOR gold]','phimfshare':'[COLOR khaki]','4share':'[COLOR blue]','tenlua':'[COLOR fuchsia]','fptplay':'[COLOR orange]','trangtiep':'[COLOR lime]','search':'[COLOR lime]','ifile':'[COLOR blue]','hdvietnam':'[COLOR red]','hdviet':'[COLOR darkorange]','xshare':'[COLOR blue]','subscene':'[COLOR green]','chiasenhac':'[COLOR orange]','phimmoi':'[COLOR ghostwhite]','megabox':'[COLOR orangered]','dangcaphd':'[COLOR yellow]','hayhaytv':'[COLOR tomato]','kenh88':'[COLOR cyan]','phimdata':'[COLOR FFDB4BDA]','phim47':'[COLOR springgreen]','phimsot':'[COLOR orangered]','hdonline':'[COLOR turquoise]','phim3s':'[COLOR lightgray]','kphim':'[COLOR lightgreen]','phimnhanh':'[COLOR chartreuse]','bilutv':'[COLOR hotpink]','pubvn':'[COLOR deepskyblue]','anime47':'[COLOR deepskyblue]','phim14':'[COLOR chartreuse]','taifile':'[COLOR cyan]','phim':'[COLOR orange]','tvhay':'[COLOR gold]','nhacdj':'[COLOR fuchsia]','phimbathu':'[COLOR lightgray]','taiphimhd':'[COLOR blue]','hdsieunhanh':'[COLOR orangered]','vuahd':'[COLOR tomato]','nhaccuatui':'[COLOR turquoise]','imovies':'[COLOR orange]','vietsubhd':'[COLOR cyan]','imax':'[COLOR chartreuse]','mphim':'[COLOR deepskyblue]','vtvgo':'[COLOR green]','youtube':'[COLOR red]','fcine':'[COLOR gold]','taiphimhdnet':'[COLOR teal]','vungtv':'[COLOR FF228B22]','biphim':'[COLOR FFBA55D3]','banhtv':'[COLOR FFF08080]','fsharefilm':'[COLOR FFF08080]','kenhphimbo':'[COLOR yellow]','anivn':'[COLOR FF8FAE22]','animetvn':'[COLOR FFD0C101]','htvonline':'[COLOR FF59B951]','gdrive':'[COLOR FF18AB67]'}

#b.getcode();b.headers.get('Set-Cookie');b.geturl();res.info().dict
#json.loads(urllib.urlopen("http://ip.jsontest.com/").read())

def log(s):
	if isinstance(s, basestring) : s = u2s(s)
	else                         : s = str(s)
	xbmc.log(s, xbmc.LOGNOTICE)

class myaddon:
    def __init__(self):
		self.addon			= xbmcaddon.Addon()
		self.info			= self.addon.getAddonInfo
		self.name			= self.info('name')
		self.version		= self.info('version')
		self.get_setting	= self.addon.getSetting
		self.set_setting	= self.addon.setSetting

		self.src_path		= xbmc.translatePath(self.info('path'))
		self.data_path		= xbmc.translatePath(self.info('profile'))
		self.temp_path		= xbmc.translatePath('special://temp')

		self.data_folder	= os.path.join(self.data_path,'data')
		self.icon_folder	= os.path.join(self.data_path,'icon')
		self.icon			= os.path.join(self.icon_folder,'icon.png')

def libsChecker(fn,url):#replace('\r\n', '\n')
	filename=os.path.join(profile,'xsharelib',fn)
	if filetime('myinfo.json') < 1 and os.path.isfile(filename):return
	sHost=getXshareData(True)
	sLocal=xrw('myinfo.json')
	try:old=json.loads(sLocal).get('versions',{}).get(fn,'')
	except:old=''
	try:new=json.loads(sHost).get('versions',{}).get(fn,'')
	except:new=''
	if new > old or not os.path.isfile(os.path.join(profile,'xsharelib',fn)):
		b=xread(url)
		if b:
			xrw(filename,b)
			xrw('myinfo.json',sHost)
			mess('New vesion of %s Updated'%fn)
	else:xrw('myinfo.json',sLocal)
	
def filetime(fn):#return hour
	if len(fn) < 20:fn=os.path.join(xsharefolder,fn)
	t=os.path.getmtime(fn) if os.path.isfile(fn) else 0
	return int((urllib2.time.time()-t)/3600)

def siteName(url):
	url=url.split('?')[0]
	return url.rsplit('/',1)[1] if url.rsplit('/',1)[1] else url.rsplit('/',1)[0].rsplit('/',1)[1]

def get_setting(name):return addon.getSetting(name)
def set_setting(name,value):addon.setSetting(name,value)
def getXshareData(lib=False):
	b = getTextFile('http://pastebin.com/raw/QincDEYZ', 'http://textuploader.com/dtgak/raw')
	if lib:
		return b
	
	try    : j = json.loads(b)
	except : j = {}
	
	return j

def namecolor(name,c=''):
	return '[COLOR %s]%s[/COLOR]'%(c,name) if c else re.sub('\[[^\[]+?\]','',name)

def getTextFile(pastebin, textuploader = ""):
	if pastebin.startswith('http'):
		b = xread(pastebin)
	else:
		b = xread("https://pastebin.com/raw/" + pastebin)
	
	if not b and textuploader:
		if textuploader.startswith('http'):
			b = xread(textuploader)
		else:
			b = xread("http://textuploader.com/%s/raw" % textuploader)
	return b.replace('\r\n', '\n')

def s2u(s):return s.decode('utf-8') if isinstance(s,str) else s
def u2s(s):return s.encode('utf-8') if isinstance(s,unicode) else s
def unescape(string):
	return ' '.join(re.sub('&.+;',xsearch('&(\w).+;',s,1),s) for s in string.split())

def xhref(s,p=''):return xsearch('href="(.+?)"',s,result=xsearch(p,s))
def xtitle(s,p=''):return ' '.join(xsearch('title="(.+?)"',s,result=xsearch(p,s)).split())
def ximg(s,p=''):return xsearch('src="(.+?)"',s,result=xsearch(p,s))
def refa(p,s,f=0):return re.findall(p,s,f)
def refas(p,s):return re.findall(p,s,re.S)
def mess(message='',title='',timeShown=5000):
	if message:
		title   = ': [COLOR blue]%s[/COLOR]'%title if title else ''
		s0      = '[COLOR green][B]Xshare[/B][/COLOR]'+title
		message = s2u(message)
		s1      = u'[COLOR %s]%s[/COLOR]'%('red' if '!' in message else 'gold', message)
		message = u'XBMC.Notification(%s,%s,%s,%s)'%(s0,s1,timeShown,icon)
		xbmc.executebuiltin(message.encode("utf-8"))
	else:
		xbmc.executebuiltin("Dialog.Close(all, true)")

def xselect(label,choices):
	dialog = xbmcgui.Dialog()
	return dialog.select(label, choices)

def googleItems(j,link='link',label='label'):
	try:l=[(i.get(link),rsl(i.get(label,0))) for i in j]
	except:
		try:l=[(i.get(link),rsl(i.get('type'))) for i in j]
		except:
			try:l=[(i.get('file'),rsl(i.get('type'))) for i in j]
			except:l=j
	#elif isinstance(j,list):l=j
	link=''#;xbmc.log('111 '+str(l))
	try:
		l=ls(l)
		for href,label in l:
			href=href.replace('\\','').strip()
			resp=xget(href)#;xbmc.log(href)
			if resp:link=href;break
		if not link:link=l[0][0]
	except:pass
	return link

def googlevideo(s,label='label',src='file'):
	link=''
	items=re.findall('%s\W*(\w+?)\W.+?%s\W+(.+?)["|\| ]'%(label,src),s)
	for href,label in ls([(i[1].replace('\\/','/'),rsl(i[0])) for i in items]):
		resp=xget(href)#;xbmc.log(href)
		if resp:link=resp.geturl();break
	if not link:
		try:link=l[0][0]
		except:pass
	return link
	
def rsl(s):
	s=str(s).replace('HDG','').replace('HD','1080').replace('SD','640').replace('large','640').replace('medium','480').replace('mobile','240').replace('lowest','240').replace('low','480').replace('hd','720').replace('fullhd','1080').replace('Auto','640').replace('AUTO','640')
	result=xsearch('(\d+)',s)
	return result if result else '240'

def ls(l):
	reverse = True if get_setting('resolut')=='Max' else False
	
	try:
		L = sorted(l, key=lambda k: int(k[1]),reverse=reverse)
	except:
		L = l
	
	return L

def googleLinks(s, file="file", type='label'):
	def rsl(s):
		arr = [
			('HDG',''),
			('HD','1080'),
			('SD','640'),
			('LARGE','640'),
			('MEDIUM','480'),
			('AUTO','640'),
			('org','240')
		]
		
		s = str(s).upper()
		e = re.sub('\D','',s)
		s = ''.join(re.sub(i[0],i[1],s) for i in arr if i[0] in s)
		if not s and not e:
			s = '0'
		return e+re.sub('\D','',s)
	
	
	if isinstance(s,basestring):
		items = []
		if 'file' in s and 'label' in s:
			items = re.findall('file\W+(\w.+?)["|\'| ].+?label\W+(\w.+?)["|\'| ]',s)#;xbmc.log(s)
		
		if (not items or "googlevideo.com" not in str(items)) and 'link' in s and 'label' in s:
			items = re.findall('link\W+(\w.+?)["|\'| ].+?label\W+(\w.+?)["|\'| ]',s)
		
		if (not items or "googlevideo.com" not in str(items)) and 'label' in s and 'src' in s:
			items = re.findall('label\W+(\w.+?)["|\'| ].+?src\W+(\w.+?)["|\'| ]',s)
			items = [(i[1],i[0]) for i in items]
		
		if (not items or "googlevideo.com" not in str(items)) and 'file' in s:
			items = re.findall('file\W+(\w.+?)["|\'| ]',s)
			if items and "googlevideo.com" in str(items):
				items = [(i,'1') for i in items]
	
	elif isinstance(s,dict):
		try    : items = [(i.get(file),i.get(type)) for i in s]
		except :
			try    : items=[(i.get("file"),i.get("label")) for i in s]
			except :
				try     : items=[(i.get("file"),i.get("type")) for i in s]
				except  : items = []
		
	elif isinstance(s,list):
		items = s
	
	else:
		items = []
	
	items   = [(i[0].replace('\\/','/'),rsl(i[1])) for i in items]
	reverse = True if get_setting('resolut') == 'Max' else False
	items   = sorted(items, key=lambda k: int(k[1]),reverse=reverse)
	
	
	#for i in items:xbmc.log('1111 '+str(i))
	
	link=''
	for href,label in items:
		try:
			link = xget(href).geturl();xbmc.log('qqqqq '+href)
			if link:
				break
		except:
			pass
	
	return link
#url='https://www.googleapis.com/customsearch/v1element?key=AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY&rsz=filtered_cse&num=20&hl=vi&prettyPrint=false&source=gcsc&gss=.com&cx=009789051051551375973:rw4tz3oypqq&googlehost=www.google.com&callback=google.search.Search.apiary19044&q=Sword'
def googleDrive(url, pageToken=""):
	def spreadsheets(url, id=""):
		if url.startswith('http:') or url.startswith('https:'):
			id  = xsearch('([\w|-]{28,})',url)
			gid = xsearch('gid=(\d+)',url)
			if gid:
				b      = ""
				sheets = [gid]
				label  = "|Google Spreadsheets"
				
			else:
				b = xread('https://docs.google.com/spreadsheets/d/'+id)
				label  = xsearch('<title>(.+?)</title>',b)+"|Google Spreadsheets"
				sheets = list(set(re.findall('"(\d+)"',xsearch('(\{structure.+?\}\});',b))))

		else:
			b      = url
			label  = xsearch('<title>(.+?)</title>',b)+"|Google Spreadsheets"
			sheets = list(set(re.findall('"(\d+)"',xsearch('(\{structure.+?\}\});',b))))
		
		#xbmc.log(str(sheets))
		if not sheets:
			label = ""
			j     = []
		elif len(sheets) > 1:
			sheetsName = re.findall('sheet-tab-caption">([^<]+?)</div>',b)
			try:
				j = {"ids":[(sheets[i],u2s(sheetsName[i])) for i in range(len(sheets))]}
			except:
				j = {"ids":[(sheets[i],sheets[i]) for i in range(len(sheets))]}
		else:
			url = "https://docs.google.com/spreadsheets/d/%s/gviz/tq?gid=%s&headers=1&tq=%s"
			url = url % (id, sheets[0], "select%20A%2CB%2CC")
			b   = xread(url)
			try:
				rows = json.loads(xsearch('\((\{.+?\})\);',b)).get("table",{}).get("rows",[])
			except:
				rows = []
			
			j = []
			for row in rows:
				detail = row.get("c",[])
				try:
					title = detail[0].get("v","")
					link  = detail[1].get("v","")
					img   = detail[2].get("v","")
					if title and link:
						j.append((title, link, img))
				except : pass

		return label, j
	
	if "goo.gl" in url or len(url) < 10:
		s = xget('http://goo.gl/' + xsearch('(\w{6,10})',url))
		if s:
			url = s.geturl()
		
	id     = xsearch('([\w|-]{28,})',url)
	cookie = ""
	if not url.startswith('http:') and not url.startswith('https:') or "spreadsheets" not in url:
		href = 'https://drive.google.com/'
		res  = xget('%suc?id=%s'%(href,id), data = 'X-Json-Requested=true')
		
		if res:
			cookie=res.headers.get('Set-Cookie')
			label = "Label In dict"
			try:
				j = json.loads(xsearch('(\{.+?\})',res.read()))
			except:
				j = {}
		
		elif not res:
			b     = xread('%sopen?id=%s'%(href,id))
			label = xsearch('<title>(.+?)</title>',b)
			href  = "https://www.googleapis.com/drive/v2/files?maxResults=30&orderBy=title&"
			href += "q='%s'+in+parents&key=AIzaSyCoi-DctzJWnIcydk89UETNQaf4W7QTUi8&pageToken=%s"
			href  = href % (id, pageToken)
			
			def abc(i):
				return i.get("id"),i.get("title"),i.get("mimeType"),i.get("fileSize")
			
			try:
				j = json.loads(xread(href))
				nextPageToken = j.get("nextPageToken")
				if nextPageToken:
					j = {"nextPageToken":nextPageToken,"items":[abc(i) for i in j['items']]}
				else:
					j = [abc(i) for i in j['items']]
				
				label += "|Google Drive"
			except:
				j = []
			
		else:#xem lai bo nhanh nay
			b     = xread('%sopen?id=%s'%(href,id))
			label = xsearch('<title>(.+?)</title>',b)
			try:
				s = json.loads(xsearch("'(\[\[\[.+?)'",b).decode('string_escape'))[0]
				j = [(i[0],i[2],i[3],i[13]) for i in s]
				label += "|Google Drive"
			except:
				j = []
		
		if not j and "drive." not in url:
			label, j = spreadsheets(b, id)
	
	else:#"spreadsheets/" in url
		label, j = spreadsheets(url)
	
	return label, j, cookie

def googleDriveLink(id):
	link   = 'https://docs.google.com/get_video_info?docid='+id
	b      = xget(link)#;xbmc.log(link+' '+b.cookiestring)
	res={'36': 240, '38': 3072, '17': 144, '22': 720, '46': 1080, '18': 360, '44': 480, '45': 720, '37': 1080, '43': 360, '35': 480, '34': 360, '5': 240, '6': 270}
	try:
		cookie = b.headers.get('Set-Cookie')
		s       = dict(urllib2.urlparse.parse_qsl(b.read())).get('fmt_stream_map')
		items   = [(i.split('|')[1],i.split('|')[0]) for i in s.split(',')]
		items   = [(i[0],res.get(i[1],0)) for i in items]
		reverse = True if get_setting('resolut')=='Max' else False
		items   = sorted(items, key=lambda k: int(k[1]) if k[1] else 0,reverse=reverse)
	except:
		items   = []
	
	link = ""
	if items:
		hd_={'User-Agent':'Mozilla/5.0','Cookie':cookie}
		for href,label in items:
			resp = xget(href,hd_)#;xbmc.log(str(label)+' '+href)
			if resp:
				link = resp.geturl()
				break
		if link:
			import urllib
			link += '|User-Agent=Mozilla/5.0&Cookie='+urllib.quote(cookie)
	return link

def packer(code):
	def encode_base_n(num, n, table=None):
		FULL_TABLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
		if not table:
			table = FULL_TABLE[:n]

		if n > len(table):
			raise ValueError('base %d exceeds table length %d' % (n, len(table)))

		if num == 0:
			return table[0]

		ret = ''
		while num:
			ret = table[num % n] + ret
			num = num // n
		return ret

	PACKED_CODES_RE = r"}\('(.+)',(\d+),(\d+),'([^']+)'\.split\('\|'\)"
	mobj = re.search(PACKED_CODES_RE, code)
	obfucasted_code, base, count, symbols = mobj.groups()
	base = int(base)
	count = int(count)
	symbols = symbols.split('|')
	symbol_table = {}

	while count:
		count -= 1
		base_n_count = encode_base_n(count, base)
		symbol_table[base_n_count] = symbols[count] or base_n_count

	return re.sub(r'\b(\w+)\b', lambda mobj: symbol_table[mobj.group(0)], obfucasted_code)
	
def xrw(fn,s='',a='w'):
	if ":" not in fn:
		fn = os.path.join(xsharefolder,fn)
	
	try:
		if s and a=='w':
			s = s.replace('\r\n','\n')
			f = open(fn, a)
			f.write(s)
		elif s:
			f = open(fn,a)
			f.write(s)
		else:
			f = open(fn)
			s = f.read().replace('\r\n','\n')
		f.close()
	
	except:
		s = ''
	return s

def xcookie(cookie=None):
	if cookie:ck=';'.join('%s=%s'%(i.name,i.value) for i in cookie.cookiejar)
	else:ck=urllib2.HTTPCookieProcessor();urllib2.install_opener(urllib2.build_opener(ck))
	return ck
	
def xread(url,headers={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	req=urllib2.Request(url,data,headers)
	try:
		res=urllib2.urlopen(req, timeout=timeout)
		hd=dict(res.headers.items())
		cookie=hd.get('set-cookie','')
		encoding=hd.get('content-encoding','')
		if encoding=='gzip':
			import StringIO,gzip
			buf=StringIO.StringIO(res.read())
			f=gzip.GzipFile(fileobj=buf)
			b=f.read()
		else:b=res.read()
		res.close()
	except:b=''
	return b

def xreadc(url,hd={'User_Agent':'Mozilla/5.0'}, data=None, c='', timeout=30):
	cookie=urllib2.HTTPCookieProcessor()
	opener=urllib2.build_opener(cookie)
	urllib2.install_opener(opener)
	opener.addheaders=hd.items()
	if c:opener.addheaders=[('Cookie',c)]
	try:
		o=opener.open(url,data,timeout=10);b=o.read();o.close()
		b+='xshare%s'%';'.join('%s=%s'%(i.name,i.value) for i in cookie.cookiejar)
	except:b=''
	return b

def xget(url,hd={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	try:res=urllib2.urlopen(urllib2.Request(url,data,hd),timeout=timeout)
	except:res=None
	return res#res.info().get('content-length')

def xcheck(item,hd={'User-Agent':'Mozilla/5.0'},data=None,timeout=30):
	def check(url):
		req = urllib2.Request(url,data,hd)
		try:
			b = urllib2.urlopen(req,timeout=timeout)
			link = b.geturl()
			b.close()
		except:
			link = ''
		return link
	
	link = ''
	if type(item) in (str,unicode):
		link = check(item)
	
	elif type(item)==list:
		try:
			for href,title in item:
				link = check(href)
				if link:
					break
		except:
			mess('Link checked fail !','xshare')
	return link

def get_input(title=u"", default=u""):
	result = ''
	keyboard = xbmc.Keyboard(default, title)
	keyboard.doModal()
	if keyboard.isConfirmed():
		result = keyboard.getText()
	return result.strip()

def xsearch(pattern,string,group=1,flags=0,result=''):
	try:s=re.search(pattern,string,flags).group(group)
	except:s=result
	return s

def xsearchs(pattern,string):
	try:s=re.search(pattern,string,re.S).group(1)
	except:s=result
	return s

def fmn(n):
	try:s=format(int(n), "8,d").replace(',','.').strip()
	except:s=str(n)
	return s

def fixTitleEPS(i):
	p=[xsearch('(Tập.?\d+)|(tập.?\d+)|(TẬP.?\d+)',i),xsearch('(\WE.?\d+)',i)]
	if p[0]:i=re.sub(p[0],'Tập '+format(int(xsearch('(\d+)',p[0])),'02d'),i)
	elif p[1]:i=re.sub(p[1],'.E'+format(int(xsearch('(\d+)',p[1])),'02d'),i)
	return i

def vnu(s):
	dic={'&Aacute;':'Á','&aacute;':'á','&Agrave;':'À','&agrave;':'à','&acirc;':'â','&atilde;':'ã','&Egrave;':'È','&egrave;':'è','&Eacute;':'É','&eacute;':'é','&ecirc;':'ê','&Ograve;':'Ò','&ograve;':'ò','&Oacute;':'Ó','&oacute;':'ó','&Ocirc;':'Ô','&ocirc;':'ô','&otilde;':'õ','&Uacute;':'Ú','&uacute;':'ú','&Ugrave;':'Ù','&ugrave;':'ù','&Igrave;':'Ì','&igrave;':'ì','&Iacute;':'Í','&iacute;':'í','&Yacute;':'Ý','&yacute;':'ý','&bull;':'*','&#039;':'\''}
	for i in dic:s=s.replace(i,dic.get(i))
	return ' '.join(re.sub('&.+;',xsearch('&(\w).+;',i),i) for i in s.split())

def s2c(s):
	def sc(s):
		i = xsearch('&a?m?p?;?#(\d+);',s);
		return re.sub('&a?m?p?;?#\d+;',d.get(i,''),s) if i else s
	
	d={'192':'À','193':'Á','194':'Â','195':'Ă','202':'Ê','204':'Ì','205':'Í','211':'Ó','212':'Ô','217':'Ù','218':'Ú','224':'à','225':'á','226':'â','227':'ă','232':'è','233':'é','234':'ê','235':'ẽ','236':'ì','237':'í','242':'ò','243':'ó','244':'ô','245':'ỏ','249':'ù','250':'ú','253':'ý','039':"'",'8211':'-'}
	return ' '.join(sc(i) for i in s.split()).replace('&amp;','&').replace('&quot;','"').replace('&#39',"'")

def s2c1(s):
	return ' '.join(
					re.sub(
						'&#\d+;', unichr(int(xsearch('&#(\d+);',i))), i
						) if xsearch('&#(\d+);',i) else i for i in s.split()
					)

def s2c2(s):
	for i in re.findall('(&#\d+;)', s):
		try:
			s = s.replace(i, u2s(unichr(int(i[2:-1]))))
		except:
			continue
	return s.replace('&quot;', '"').replace('&amp;', '&')

def unescape(text):
	import htmlentitydefs
	def fixup(m):
		text = m.group(0)
		if text[:2] == "&#":
			try:
				if text[:3] == "&#x":
					return unichr(int(text[3:-1], 16))
				else:
					return unichr(int(text[2:-1]))
			except:
				pass
		else:
			try:
				text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
			except:
				pass
		return text
	return re.sub("&#?\w+;", fixup, text)

def ok_ru(url):
	b = xread(url)
	s = xsearch('data-options="(.+?)"', b)
	try:
		s = json.loads(unescape(s).decode('utf-8'))
		s = json.loads(s['flashvars']['metadata'])
		items = [(i['url'], rsl(i['name'])) for i in s['videos']]
		reverse = True if get_setting('resolut')=='Max' else False
		items = sorted(items, key=lambda k: int(k[1]) if k[1] else 0,reverse=reverse)
	except:
		items = []
	
	link = ""
	#log(items)
	if items:
		for href,label in items:
			#log([href, label])
			resp = xget(href)
			if resp:
				link = resp.geturl()
				break
		if link:
			link += '|User-Agent=Mozilla/5.0' + '&Referer=' + url + '&Origin=http://ok.ru'
	return link

def getOpenloadLink(id):
	try:
		j = json.loads(xread('https://api.openload.co/1/streaming/get?file=' + id))
	except:
		j = {}
	
	link = ""
	if j.get("status",0) == 200:
		link = j.get('result',{}).get('url','')
	
	elif j.get("status",0) == 403:
		link = ""
		mess('Hãy pair ip tại https://olpair.com để play được link trên openload')
	
	return link

def getGDLink(href):
	link = ""
	
	id = xsearch('([\w|-]{28,})', href)
	href = 'https://drive.google.com/file/d/%s/view' % id
	
	b = xreadc(href)
	fmt_stream_map = re.findall('(\["fmt_stream_map".+?\])', b)
	
	if fmt_stream_map:
		if 'xshare' in b:
			cookie = b.split('xshare')[1]
			import urllib
			hd = "|User-Agent=Mozilla/5.0&Cookie=" + urllib.quote(cookie)
			b = b.split('xshare')[0]
		else:
			hd = '|User-Agent=Mozilla/5.0'
		
		fmt_stream_map = fmt_stream_map[0]
		stream_map = json.loads(fmt_stream_map)[1].split(",")
		
		qualitys = ['38', '46', '37', '45', '22', '35', '44', '18', '43', '34', '6', '36', '17']
		if get_setting('resolut')=='Max':
			qualitys.reverse()
		
		for quality in qualitys:
			for stream in stream_map:
				#log(stream)
				if stream.startswith(quality + "|"):
					link = stream.split("|")[1] + hd
					break
	
	else:
		href = 'https://drive.google.com/uc?id=' + id
		
		b = xread(href, data = 'X-Json-Requested=true')
		try:
			j = json.loads(xsearch('(\{.+\})',b))
		except:
			j = {}
		
		link = j.get("downloadUrl","")
	
	return link

def leechInfo(link):
	href='http://vnz-leech.com/checker/check.php?links=%s'
	headers={'Referer':'http://vnz-leech.com/checker/','User-Agent':'Mozilla/5.0'}
	b=xread(href%''.join(link.split()),headers)
	try:j=json.loads(b.replace('(','').replace(')',''))
	except:j={}
	def geti(j,i):return j.get(i,'').encode('utf-8')
	result='',''
	if j.get('status','')=='good_link':
		title='%s (%s)'%(geti(j,'filename'),geti(j,'filesize'))
		href=geti(j,'link')
		if title and href:result=title,href
	return result

def siteInfo(url):
	if '4share.vn/f/' in url.lower():
		url='http://4share.vn/f/%s/'%xsearch('/f/(\w+)',url)
		title,url=leechInfo(url)
	elif '4share.vn/d/' in url.lower():
		url='http://4share.vn/d/%s/'%xsearch('/d/(\w+)',url)
		b=xread(url)
		if '[Empty Folder]' in b:title=''
		else:title=xsearch("<title>(.+?)</title>",b).replace('4Share.vn - ','')
	elif 'fshare.vn' in url.lower():
		id=siteName(url).upper();link='https://www.fshare.vn/%s/'+id
		url=link%('file' if '/file/' in url.lower() else 'folder')
		b=xread(url)#,{'User-Agent':'Mozilla/5.0','x-requested-with':'XMLHttpRequest'})
		if b and '/file/' in url:
			s=xsearch('(<div class="file-info".+?data-owner)',b,1,re.S)
			m=xsearch('(<i class="fa fa-file.+?/div>)',s,1,re.S)
			title=' '.join(re.sub('<[^>]+?>','',m).split())
			if title:
				size=xsearch('(<i class="fa fa-hdd.+?/div>)',s,1,re.S)
				title=title+' '+re.sub('<[^>]+?>| ','',size)
			elif not xsearch('(<title>Lỗi 404</title>)',b):title,url=leechInfo(url)
		elif b:
			p='(<span class="glyphicon glyphicon-info.+?/div>)'
			size=re.sub('<[^>]+?>|Số lượng|:','',xsearch(p,b,1,re.S)).strip()
			if size and size>'0':
				title=xsearch('(<title>.+?</title>)',b)
				title='%s %s file(s)'%(' '.join(re.sub('<[^>]+?>|Fshare|-','',title).split()),size)
			else:title=''
		else:title,url=leechInfo(url)
	if not title:url=''
	return title,url

def toBase36(value):
	if not isinstance(value, int):return " "
	elif value==0:return "0"
	elif value<0:sign="-";value=-value
	else:sign=""

	result = []
	while value:
		value,mod=divmod(value, 36)
		result.append("0123456789abcdefghijklmnopqrstuvwxyz"[mod])
	return sign+"".join(reversed(result))

def cliptv_cookie():
	path = xbmc.translatePath(addon.getAddonInfo('path'))
	return xrw(os.path.join(path,'resources','lib','cliptv.cookie'))

class NoRedirection(urllib2.HTTPErrorProcessor):
	def http_response(self, request, response):
		return response
	https_response = http_response

def xread0(url, hd = {'User-Agent':'Mozilla/5.0'}):
	opener = urllib2.build_opener(NoRedirection)
	urllib2.install_opener(opener)
	opener.addheaders = hd.items()
	try:
		o = opener.open(url)
	except:
		o = ""
	
	return o

