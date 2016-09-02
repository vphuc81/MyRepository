__author__ = 'Dknight'
import urllib,urllib2,re
import StringIO,gzip

def make_Request(url, headers=None):
    if headers is None:
        headers = {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                 'Referer' : 'http://www.google.com'}
    try:
        req = urllib2.Request(url,headers=headers)
        f = urllib2.urlopen(req)
        body=f.read()
        return body
    except:
        pass 

def GetContent(url, useProxy=False):
    strresult=""
    #if useProxy==True:
        #url = "http://webcache.googleusercontent.com/search?q=cache:*url*".replace("*url*",urllib.quote_plus(url))
    try:
		opener = urllib2.build_opener()
		opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
							 ('Accept-Encoding','gzip, deflate'),
							 ('Referer', "http://hdonline.vn/player/vplayer.swf"),
							 ('Content-Type', 'application/x-www-form-urlencoded'),
							 ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0'),
							 ('Connection','keep-alive'),
							 ('Accept-Language','en-us,en;q=0.5'),
							 ('Pragma','no-cache'),
							 ('Host','hdonline.vn')]
		usock=opener.open(url)
		if usock.info().get('Content-Encoding') == 'gzip':
			buf = StringIO.StringIO(usock.read())
			f = gzip.GzipFile(fileobj=buf)
			strresult = f.read()
		else:
			strresult = usock.read()
		usock.close()
    except Exception, e:
       print str(e)+" |" + url
    return strresult

def decodevplug(_arg_1):
            import math
            _local_2 = "";
            _local_3 = list("1234567890qwertyuiopasdfghjklzxcvbnm")
            _local_4= len(_local_3)
            strlen=len(_arg_1)
            _local_5= list("f909e34e4b4a76f4a8b1eac696bd63c4")
            _local_6 = list(_arg_1[((_local_4 * 2) + 32):strlen])
            _local_7= list(_arg_1[0:(_local_4 * 2)])
            _local_8= []
            _local_9= _arg_1[((_local_4 * 2) + 32):strlen]
            _local_10 = 0
            while (_local_10 < (_local_4 * 2)):
                _local_11 = (_local_3.index(_local_7[_local_10]) * _local_4)
                _local_11 = (_local_11 + _local_3.index(_local_7[(_local_10 + 1)]))
                idx= int(math.floor((_local_10 / 2)) % len(_local_5))
                str(_local_5[idx])[0]
                _local_11 = (_local_11 - ord(str(_local_5[idx])[0]))
                _local_8.append(chr(_local_11))
                _local_10 = (_local_10 + 2)
				
            _local_10 = 0
            while (_local_10 < len(_local_6)):
                _local_11 = (_local_3.index(_local_6[_local_10]) * _local_4)
                _local_11 = (_local_11 + _local_3.index(_local_6[(_local_10 + 1)]))
                idx= int((math.floor((_local_10 / 2)) % _local_4))
                _local_11 = (_local_11 - ord(str(_local_8[idx])[0]))
                _local_2 = (_local_2 + chr(_local_11))
                _local_10 = (_local_10 + 2)

            return _local_2
	
def client_id_1():
	
	try:
		content = GetContent('http://hdonline.vn/phim-quy-ba-diep-vien-8170.html')
		
		vxml=re.compile(',"file":"(.+?)","').findall(content)[0]
		vxml = 'http://hdonline.vn' + vxml.replace('\/','/')

		content = GetContent(vxml)
		
		url_encoded = re.compile('<jwplayer:file>(.*?)</jwplayer:file>').findall(content)[0]
		url_decoded = decodevplug(url_encoded)
		
		content = GetContent(url_decoded)

		url_encoded = re.compile('<jwplayer:file>(.*?)</jwplayer:file>').findall(content)[0]
		
		url_decoded = decodevplug(url_encoded)
		
		#client_id = re.compile('phimhd3s.com/.*?/?(................................)/').findall(url_decoded)
		client_id = re.compile('/?(................................)/').findall(url_decoded)
		
		if len(client_id) > 0:
			return client_id[0]

		return None
	except:
		pass

def client_id_2():
	
	try:
		content = GetContent('http://hdonline.vn/frontend/episode/loadxmlconfigorder?ep=1&fid=7876')

		url_decoded = re.compile('<jwplayer:file>(.*?)</jwplayer:file>').findall(content)[0]
		
		#client_id = re.compile('phimhd3s.com/.*?/?(................................)/').findall(url_decoded)
		client_id = re.compile('/?(................................)/').findall(url_decoded)
		
		if len(client_id) > 0:
			return client_id[0]

		return None
	except:
		pass
