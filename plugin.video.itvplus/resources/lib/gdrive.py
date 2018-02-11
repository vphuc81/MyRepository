import urllib, urllib2

# Class khong cho web chuyen huong 302
class MyHTTPErrorProcessor(urllib2.HTTPErrorProcessor):

    def http_response(self, request, response):
        code, msg, hdrs = response.code, response.msg, response.info()
        if code == 302: return response

        if not (200 <= code < 300):
            response = self.parent.error('http', request, response, code, msg, hdrs)
        return response

    https_response = http_response

def get_curl(url, obj= {}):
    useheader = False
    if "showHeader" in obj:
        useheader = obj['showHeader']

    ucookie = False
    if "cookie" in obj:
        ucookie = obj['cookie']

    sslverify = False
    if "sslverify" in obj:
        sslverify = obj['sslverify']

	usehttpheader = True;

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
        "Keep-Alive" : 115,
        "Connection": "keep-alive",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39"
    }

    if ucookie:
        headers['Cookie'] = ucookie

    try:
        cookieprocessor = urllib2.HTTPCookieProcessor()

        opener = urllib2.build_opener(MyHTTPErrorProcessor, cookieprocessor)
        urllib2.install_opener(opener)

        req = urllib2.Request(url,headers=headers)
    	res = urllib2.urlopen(req)

    	# body = res.read()
        # Lay thong tin trong headers
        info = res.info()
    	res.close()
    	return info
    except(RuntimeError, TypeError, NameError):
        return "fail"

def get_drive_download(id):
    link = "https://docs.google.com/uc?export=download&id=" + id

    url = link + "&confirm=no_antivirus"
    data = get_curl(url=url)

    if "Set-Cookie" in data:
        # Lay thong tin Cookie
        array = data["Set-Cookie"].split(";")

        if len(array) >= 1:
            cookie = array[0]
            confirm = cookie.split("=")
            confirmCode = confirm[1]

            # Lay url cua file tren google drive
            url = link + "&confirm=" + confirmCode
            data = get_curl(url, obj = {'cookie' : cookie})
            if "Location" in data:
                return data["Location"]

    return None


# ID cua file tren google drive
print "Link file for Stream:"
print ""
print get_drive_download(id="1zF4UxTcDghprVh7ObVN1v1FFpb0xVwAI")
print ""
print "------------------"
