#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver
from common import ShowMessage, infoDialog, Paths, write_file

addon_id = 'plugin.video.xomgiaitri'
my_addon = xbmcaddon . Addon ( addon_id )
argvParam = int ( sys . argv [ 1 ] )
# Test log files..
addondir    = xbmc.translatePath( my_addon.getAddonInfo('profile') ) 
rep_matches_file = addondir + "rep_matches_file.txt"
response_file = addondir + "response_file.txt"
video_link_file = addondir + "video_link_file.txt"
server_list_file = addondir + "server_list_file.txt"
mok_req_file = addondir + "mok_req.txt"  
mok_response_file = addondir + "mok_response.txt"

def main_index ( ) :
 addFolder ( 'Search' , 'http://www.xomphimbo.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 addFolder ( 'Phim Lẻ' , 'http://www.xomphimbo.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 addFolder ( 'Phim Bộ' , 'http://www.xomphimbo.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 addFolder ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomphimbo.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 addFolder ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomphimbo.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )

def countries ( ) :
 addFolder ( "Hồng Kong" , "http://www.xomphimbo.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 addFolder ( "Hồng Kong (VNLT)" , "http://www.xomphimbo.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 addFolder ( "Hàn Quốc" , "http://www.xomphimbo.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 addFolder ( "Hàn Quốc (vietsub)" , "http://www.xomphimbo.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 addFolder ( "Trung Quốc" , "http://www.xomphimbo.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 addFolder ( "Đài Loan" , "http://www.xomphimbo.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 addFolder ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 addFolder ( "Thái Lan" , "http://www.xomphimbo.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 addFolder ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/7/cac-loai-khac.html" , "index" , "" )

def categories ( ) :
 addFolder ( "Hành Động" , "http://www.xomphimbo.com/xem/category/8/hanh-dong.html" , "index" , "" )
 addFolder ( "Tình Cảm" , "http://www.xomphimbo.com/xem/category/9/tinh-cam.html" , "index" , "" )
 addFolder ( "Phim Hài" , "http://www.xomphimbo.com/xem/category/10/phim-hai.html" , "index" , "" )
 addFolder ( "Kinh Dị" , "http://www.xomphimbo.com/xem/category/11/kinh-di.html" , "index" , "" )
 addFolder ( "Kiếm Hiệp" , "http://www.xomphimbo.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 addFolder ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/15/viet-nam.html" , "index" , "" )
 addFolder ( "Hài Kịch" , "http://www.xomphimbo.com/xem/category/16/hai-kich.html" , "index" , "" )
 addFolder ( "Ca Nhạc" , "http://www.xomphimbo.com/xem/category/17/ca-nhac.html" , "index" , "" )
 addFolder ( "Cải Lương" , "http://www.xomphimbo.com/xem/category/18/cai-luong.html" , "index" , "" )
 addFolder ( "Phóng Sự" , "http://www.xomphimbo.com/xem/category/19/phong-su.html" , "index" , "" )
 addFolder ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/20/cac-loai-khac.html" , "index" , "" )

def add_mirrors ( url ) :
 response = request_url ( url )
 II1Ii1iI1i = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( response )
 for iiI1iIiI , OOo , Ii1IIii11 in II1Ii1iI1i :
  Ii1IIii11 = Ii1IIii11 . replace ( "xomgiaitri.com" , "mythugian.net" )
  Ii1IIii11 = Ii1IIii11 . replace ( "www." , "" )
  Ii1IIii11 = "/" . join ( Ii1IIii11 . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( Ii1IIii11 . split ( "/" ) [ - 1 ] )
  addFolder ( "[B]" + OOo + "[/B]" , "http://www.xomphimbo.com/xem" + iiI1iIiI , 'mirrors' , Ii1IIii11 )
 Oooo0000 = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( response . replace ( "'" , '"' ) )
 for iiI1iIiI , i11 in Oooo0000 :
  addFolder ( i11 , iiI1iIiI . replace ( "./" , "http://www.xomphimbo.com/xem/" ) , 'index' , "" )

def search ( ) :
 try :
  O0OoOoo00o = xbmc . Keyboard ( '' , 'Enter search text' )
  O0OoOoo00o . doModal ( )
  if ( O0OoOoo00o . isConfirmed ( ) ) :
   OOoO00o = urllib . quote_plus ( O0OoOoo00o . getText ( ) )
  add_mirrors ( url % OOoO00o )
 except : pass
def add_episodes ( url ) :
 I111I11 = xemtructuyen ( url )
 response = request_url ( I111I11 )
 server_list = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( response )
 if "VIP OK : " in server_list :
  server_list . insert ( 0 , server_list . pop ( server_list . index ( "VIP OK : " ) ) )
 if "VIP A : " in server_list :
  server_list . insert ( 0 , server_list . pop ( server_list . index ( "VIP A : " ) ) )
 if "VIP D : " in server_list :
  server_list . insert ( 0 , server_list . pop ( server_list . index ( "VIP D : " ) ) )
 if "VIP B : " in server_list :
  server_list . insert ( 0 , server_list . pop ( server_list . index ( "VIP B : " ) ) )
 for isitem in range ( len ( server_list ) ) :
   addFolder ( "[%d] - %s" % ( isitem + 1 , server_list [ isitem ] ) , I111I11 . encode ( "utf-8" ) , 'episodes' , "" )
def loadvideo ( url , name ) :
 response = request_url ( url )
 name = name . split ( "] - " ) [ 1 ]
 listserver = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % name ) . findall ( response )
 listitems = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( listserver [ 0 ] )
 if ( "episode_bg_2" in listserver [ 0 ] ) :
  ii1 = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( listserver [ 0 ] )
  addLink ( "Part - " + ii1 [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf8" ) , url , 'loadvideo' , '' , name )
 for items , index in listitems :
  addLink ( "Part - " + index . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomphimbo.com/xem/" + items , 'loadvideo' , '' , name )
def xemtructuyen ( url ) :
 response = request_url ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( response ) [ 0 ]

def playStream ( url , name ) :
 req = xbmcgui . ListItem ( name )
 response = request_url ( url )
 if "proxy.link" in response :
  url_link = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( response )
  response = request_url ( url_link [ 0 ] )
 url_link = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( response )
 if ( len ( url_link ) == 0 ) :
  video_link = None
  rep_matches = re . compile ( 'file\: "(.+?)"' ) . findall ( response )
  if 'iframe src="http://play.mythugian.net/' in response :
   url_link = re . compile ( 'iframe src="(http://play.mythugian.net/.+?)"' ) . findall ( response )
   response = request_url ( url_link [ 0 ] )
   url_link = re . compile ( '(\[\{"label".+?\}\])' ) . findall ( response )
   try :
    video_link = json . loads ( url_link [ 0 ] ) [ - 1 ] [ "file" ]
   except :
    video_link = json . loads ( url_link [ 0 ] ) [ - 1 ] [ "src" ]
  elif 'iframe src="http://img.mythugian.net/' in response :
   try :
    url_link = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/.+?)"' , response ) . group ( 1 )
    try :
     video_link = re . search ( 'link=(.+?)$' , url_link ) . group ( 1 ) . decode ( "base64" )
     video_link = get_gdlink ( video_link )
    except :
     response = request_url ( url_link )
     try :
      rep_match = [ ]
      rep_match += [ re . search ( 'start\|primary\|(.+?)\|' . decode ( "base64" ) , response ) . group ( 1 ) ]
      try :
       rep_match += [ re . search ( 'XHxnb29nbGVcfChcdyspXHxjb2xvclx8' . decode ( "base64" ) , response ) . group ( 1 ) ]
      except : pass
      video_link = get_gdlink ( "aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2ZpbGUvZC8lcy92aWV3" . decode ( "base64" ) % ( "-" . join ( rep_match ) ) )
     except :
      try :
       rep_match = [ ]
       rep_match += [ re . search ( 'c3RhcnRcfChcdyspXHxzZXR1cA==' . decode ( "base64" ) , response ) . group ( 1 ) ]
       rep_match += [ re . search ( 'XHxnb29nbGVcfChcdyspXHxjb2xvclx8' . decode ( "base64" ) , response ) . group ( 1 ) ]
       rep_match += [ re . search ( 'cHJpbWFyeVx8KFx3KylcfHN0YXJ0cGFyYW0=' . decode ( "base64" ) , response ) . group ( 1 ) ]
       video_link = get_gdlink ( "aHR0cHM6Ly9kcml2ZS5nb29nbGUuY29tL2ZpbGUvZC8lcy92aWV3" . decode ( "base64" ) % ( "-" . join ( rep_match ) ) )
      except :
       try :
        url_link = re . search ( 'sources = (\[.+?\]);' , response )
        video_link = json . loads ( url_link . group ( 1 ) ) [ - 1 ] [ "file" ]
       except :
        try :
         url_link = re . search ( '"(https://drive.google.com/file/.+?)"' , response ) . group ( 1 )
         video_link = get_gdlink ( url_link . replace ( "preview" , "view" ) )
        except :
         video_link = re . search ( '"(http\://.+?\.mediafire\.com/.+?)"' , response ) . group ( 1 )
   except : pass
  elif rep_matches is not None and not rep_matches == []:
   if "http://" not in rep_matches [ 0 ] :
    rep_matches [ 0 ] = "http://www.xomphimbo.com/xem/" + rep_matches [ 0 ]
   video_link = rep_matches [ 0 ]
  elif "app.box.com" in response :
   OOO00 = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( response ) [ 0 ]
   gRequest = request_url ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % OOO00 )
   O000OO0 = json . loads ( gRequest ) [ "file" ] [ "versionId" ]
   video_link = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( O000OO0 , OOO00 )
  elif "drive.google.com/file" in response :
   url_link = re . search ( '"(https://drive.google.com/file/.+?)"' , response ) . group ( 1 )
   video_link = get_gdlink ( url_link . replace ( "preview" , "view" ) )
   infoDialog(str(video_link), "Get Glink", time=3000)
  elif "ok.ru/videoembed" in response:
   try:
	url_link = re . search ( '"(https://ok.ru/videoembed/.+?)"' , response ) . group ( 1 )
   except:
	url_link = re . search ( '"(https://www.ok.ru/videoembed/.+?)"' , response ) . group ( 1 )
	url_link = url_link.replace("www.", "")
   url_link = url_link.replace("?autoplay=1", "").replace("videoembed", "video")
   video_link = get_mokrulink(url_link.replace("ok.ru", "m.ok.ru"))   
  elif "openload" in response :
   try :
    video_link = re . compile ( '"(https://openload.+?)"' ) . findall ( response ) [ 0 ]
    video_link = urlresolver . resolve ( video_link )
   except :
    pass
  else :
   url_link = re . compile ( "file: '.+?'" ) . findall ( response )
   if "http://" not in url_link [ 0 ] :
    video_link = "http://www.xomphimbo.com/xem/" + url_link [ 0 ]
   else :
    video_link = url_link [ 0 ]
  req . setPath ( video_link )
 else :
  if "http://" not in url_link [ 0 ] :
   url_link [ 0 ] = "http://www.xomphimbo.com/xem/" + url_link [ 0 ]
  req . setPath ( url_link [ 0 ] )
 req . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , req )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , req )

def get_gdlink ( url , hq = True ) :
 urlHeader = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 urlHeaders = {
 'User-Agent' : urlHeader ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 gRequest = requests . get ( url , headers = urlHeaders )
 gdUrl = gRequest . text
 try :
  url_link = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( gdUrl ) [ 0 ]
  gdRes = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : gdRes . reverse ( )
  filterLinks = json . loads ( url_link ) [ 1 ] . split ( "," )
  for items in gdRes :
   for item in filterLinks :
    if item . startswith ( items + "|" ) :
     url = item . split ( "|" ) [ 1 ]
     userAgent = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( urlHeader ) , urllib . quote_plus ( gRequest . headers [ 'set-cookie' ] ) )
     return url + userAgent
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , gdUrl ) . group ( 1 )
  except : pass
 
def get_mokrulink ( url ) :
 response = ""
 video_link = ""
 mok_req = urllib2 . Request ( url )
 mok_req . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 mok_req . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 req_url = urllib2 . urlopen ( mok_req )
 req_url_read = req_url . read ( )
 req_url_read = req_url_read.replace("\u00", "&").replace("amp;", "")
 try :
  response = re . compile ( '"https://m.ok.ru/dk?(.+?)"' ) . findall ( req_url_read )[0]
  video_link = "https://m.ok.ru/dk" + response
  infoDialog(str(video_link), "Gets VIP Ok link", time=6000)
 except :
  pass
 req_url . close ( )
 return video_link

def request_url ( url ) :
 req = urllib2 . Request ( url )
 req . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 req . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 req_url = urllib2 . urlopen ( req )
 response = req_url . read ( )
 req_url . close ( )
 response = '' . join ( response . splitlines ( ) ) . replace ( '\'' , '"' )
 response = response . replace ( '\n' , '' )
 response = response . replace ( '\t' , '' )
 response = re . sub ( '  +' , ' ' , response )
 response = response . replace ( '> <' , '><' )
 return response

def addLink ( name , url , mode , iconimage , mirrorname ) :
 u = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 ok = True
 liz = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 liz . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 liz . setProperty ( "IsPlayable" , "true" )
 ok = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = u , listitem = liz )
 return ok

def addFolder ( name , url , mode , iconimage ) :
 u = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ok = True
 liz = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 liz . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 ok = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = u , listitem = liz , isFolder = True )
 return ok

def get_params ( parameters ) :
 Oo0O00Oo0o0 = { }
 if parameters :
  O0ooo0O0oo0 = parameters [ 1 : ] . split ( "&" )
  for oo0oOo in O0ooo0O0oo0 :
   o000O0o = oo0oOo . split ( '=' )
   if ( len ( o000O0o ) ) == 2 :
    Oo0O00Oo0o0 [ o000O0o [ 0 ] ] = o000O0o [ 1 ]
 return Oo0O00Oo0o0
II = xbmc . translatePath ( my_addon . getAddonInfo ( 'profile' ) )
if os . path . exists ( II ) == False :
 os . mkdir ( II )
Oo0ooOo0o = os . path . join ( II , 'visitor' )
if os . path . exists ( Oo0ooOo0o ) == False :
 from random import randint
 Iiii = open ( Oo0ooOo0o , "w" )
 Iiii . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Iiii . close ( )
params = get_params ( sys . argv [ 2 ] )
mode = params . get ( 'mode' )
url = params . get ( 'url' )
name = params . get ( 'name' )
if type ( url ) == type ( str ( ) ) :
 url = urllib . unquote_plus ( url )
if type ( name ) == type ( str ( ) ) :
 name = urllib . unquote_plus ( name )
I11iiI1i1 = str ( sys . argv [ 1 ] )
if mode == 'index' :
 add_mirrors ( url )
elif mode == 'search' :
 search ( )
elif mode == 'videosbyregion' :
 countries ( )
elif mode == 'videosbycategory' :
 categories ( )
elif mode == 'mirrors' :
 add_episodes ( url )
elif mode == 'episodes' :
 loadvideo ( url , name )
elif mode == 'loadvideo' :
 I1i1Iiiii = xbmcgui . DialogProgress ( )
 I1i1Iiiii . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 playStream ( url , name )
 I1i1Iiiii . close ( )
 del I1i1Iiiii
else :
 main_index ( )
xbmcplugin . endOfDirectory ( int ( I11iiI1i1 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
