#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = ""
 oOooOoO0Oo0O = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  sys = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in sys for b in oOooOoO0Oo0O ) : break
 while True :
  iI1 = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in iI1 for b in oOooOoO0Oo0O ) : break
 try :
  ii11i = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   ii11i = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , ii11i . lower ( ) ) : break
 i1I11i = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( ii11i , "16" , sys , iI1 ) ) . read ( )
 if "allowed" in i1I11i :
  OoOoOO00 ( 'Search' , 'http://www.xom68.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom68.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom68.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom68.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom68.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 else :
  OoOoOO00 ( 'Search' , 'http://www.xom68.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom68.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom68.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom68.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom68.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
  if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
 I11iIi1I = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11iIi1I = xbmc . translatePath ( os . path . join ( I11iIi1I , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/xomgiaitri.jpg' , I11iIi1I )
 IiiIII111iI = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11iIi1I )
 IiII = xbmcgui . WindowDialog ( )
 IiII . addControl ( IiiIII111iI )
 IiII . doModal ( )'''
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 OoOoOO00 ( "Hồng Kong" , "http://www.xom68.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 OoOoOO00 ( "Hồng Kong (VNLT)" , "http://www.xom68.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 OoOoOO00 ( "Hàn Quốc" , "http://www.xom68.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 OoOoOO00 ( "Hàn Quốc (vietsub)" , "http://www.xom68.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 OoOoOO00 ( "Trung Quốc" , "http://www.xom68.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 OoOoOO00 ( "Đài Loan" , "http://www.xom68.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 OoOoOO00 ( "Việt Nam" , "http://www.xom68.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 OoOoOO00 ( "Thái Lan" , "http://www.xom68.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 OoOoOO00 ( "Các Loại Khác" , "http://www.xom68.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( ) :
 OoOoOO00 ( "Hành Động" , "http://www.xom68.com/xem/category/8/hanh-dong.html" , "index" , "" )
 OoOoOO00 ( "Tình Cảm" , "http://www.xom68.com/xem/category/9/tinh-cam.html" , "index" , "" )
 OoOoOO00 ( "Phim Hài" , "http://www.xom68.com/xem/category/10/phim-hai.html" , "index" , "" )
 OoOoOO00 ( "Kinh Dị" , "http://www.xom68.com/xem/category/11/kinh-di.html" , "index" , "" )
 OoOoOO00 ( "Kiếm Hiệp" , "http://www.xom68.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 OoOoOO00 ( "Việt Nam" , "http://www.xom68.com/xem/category/15/viet-nam.html" , "index" , "" )
 OoOoOO00 ( "Hài Kịch" , "http://www.xom68.com/xem/category/16/hai-kich.html" , "index" , "" )
 OoOoOO00 ( "Ca Nhạc" , "http://www.xom68.com/xem/category/17/ca-nhac.html" , "index" , "" )
 OoOoOO00 ( "Cải Lương" , "http://www.xom68.com/xem/category/18/cai-luong.html" , "index" , "" )
 OoOoOO00 ( "Phóng Sự" , "http://www.xom68.com/xem/category/19/phong-su.html" , "index" , "" )
 OoOoOO00 ( "Các Loại Khác" , "http://www.xom68.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( url ) :
 i1oOOoo00O0O = i1111 ( url )
 i11 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( i1oOOoo00O0O )
 for I11 , Oo0o0000o0o0 , oOo0oooo00o in i11 :
  OoOoOO00 ( "[B]" + Oo0o0000o0o0 + "[/B]" , "http://www.xom68.com/xem" + I11 , 'mirrors' , oOo0oooo00o )
 oO0o0o0ooO0oO = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( i1oOOoo00O0O . replace ( "'" , '"' ) )
 for I11 , oo0o0O00 in oO0o0o0ooO0oO :
  OoOoOO00 ( oo0o0O00 , I11 . replace ( "./" , "http://www.xom68.com/xem/" ) , 'index' , "" )
  if 68 - 68: o00oo . iI1OoOooOOOO + i11iiII
def I1iiiiI1iII ( ) :
 try :
  IiIi11i = xbmc . Keyboard ( '' , 'Enter search text' )
  IiIi11i . doModal ( )
  if 43 - 43: o0O0 * O00O0O0O0
  if ( IiIi11i . isConfirmed ( ) ) :
   ooO0O = urllib . quote_plus ( IiIi11i . getText ( ) )
  o0oOoO00o ( oo % ooO0O )
 except : pass
 if 28 - 28: i1iIIIiI1I - Oo0oO0ooo
def OoO000 ( url ) :
 IIiiIiI1 = iiIiIIi ( url )
 i1oOOoo00O0O = i1111 ( IIiiIiI1 )
 ooOoo0O = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( i1oOOoo00O0O )
 for OooO0 in range ( len ( ooOoo0O ) ) :
  II11iiii1Ii = [ ]
  if not any ( x in ooOoo0O [ OooO0 ] for x in II11iiii1Ii ) :
   OoOoOO00 ( "[%d] - %s" % ( OooO0 + 1 , ooOoo0O [ OooO0 ] ) , IIiiIiI1 . encode ( "utf-8" ) , 'episodes' , "" )
   if 70 - 70: o00 / ii1I % i1iIIIiI1I % i11iIiiIii . IIIiiIIii
def O0o0Oo ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 Oo00OOOOO = re . compile ( '\d+' ) . findall ( name . split ( "] - " ) [ 0 ] ) [ 0 ]
 name = name . split ( "] - " ) [ 1 ]
 O0O = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % urllib2 . unquote ( name ) ) . findall ( i1oOOoo00O0O )
 O00o0OO = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( O0O [ int ( Oo00OOOOO ) - 1 ] )
 if ( "episode_bg_2" in O0O [ int ( Oo00OOOOO ) - 1 ] ) :
  I11i1 = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( O0O [ int ( Oo00OOOOO ) - 1 ] )
  iIi1ii1I1 ( "Part - " + I11i1 [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , url , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 for o0 , I11II1i in O00o0OO :
  iIi1ii1I1 ( "Part - " + I11II1i . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , "http://www.xom68.com/xem/" + o0 , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 23 - 23: o00ooo0 / II1i + o00oo + o00oo / ii1IiI1i
def iiIiIIi ( url ) :
 iiI1 = i1111 ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( iiI1 ) [ 0 ]
 if 19 - 19: o00oo + i1iIIIiI1I
def ooo ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 if ( "proxy.link" in i1oOOoo00O0O ) :
  ii1I1i1I = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( i1oOOoo00O0O )
  i1oOOoo00O0O = i1111 ( ii1I1i1I [ 0 ] )
 ii1I1i1I = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( i1oOOoo00O0O )
 OOoo0O0 = xbmcgui . ListItem ( name )
 OOoo0O0 . setProperty ( "IsPlayable" , "true" )
 OOoo0O0 . setPath ( "http://www.xom68.com/xem/" + ii1I1i1I [ 0 ] )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoo0O0 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOoo0O0 )
 if 41 - 41: o00
def i1111 ( url ) :
 ii1i1I1i = urllib2 . Request ( url )
 ii1i1I1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 ii1i1I1i . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 o00oOO0 = urllib2 . urlopen ( ii1i1I1i )
 i1oOOoo00O0O = o00oOO0 . read ( )
 o00oOO0 . close ( )
 i1oOOoo00O0O = '' . join ( i1oOOoo00O0O . splitlines ( ) ) . replace ( '\'' , '"' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\n' , '' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\t' , '' )
 i1oOOoo00O0O = re . sub ( '  +' , ' ' , i1oOOoo00O0O )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '> <' , '><' )
 return i1oOOoo00O0O
 if 95 - 95: Oo0oO0ooo / OOooo000oo0
def iIi1ii1I1 ( name , url , mode , iconimage , mirrorname ) :
 iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO0OOO00oo . setProperty ( "IsPlayable" , "true" )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iI , listitem = OOO0OOO00oo )
 return o00O
 if 31 - 31: ii1IiI1i - Oo0oO0ooo . O00O0O0O0 % oO0o - iiI
def OoOoOO00 ( name , url , mode , iconimage ) :
 iI = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iI , listitem = OOO0OOO00oo , isFolder = True )
 return o00O
 if 4 - 4: ii1IiI1i / i1iIIIiI1I . i11iiII
def O0oo0OO0oOOOo ( k , e ) :
 i1i1i11IIi = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for OooO0 in range ( len ( e ) ) :
  II1III = k [ OooO0 % len ( k ) ]
  iI1iI1I1i1I = chr ( ( 256 + ord ( e [ OooO0 ] ) - ord ( II1III ) ) % 256 )
  i1i1i11IIi . append ( iI1iI1I1i1I )
 return "" . join ( i1i1i11IIi )
 if 24 - 24: o00ooo0
def o0Oo0O0Oo00oO ( parameters ) :
 I11i1I1I = { }
 if 83 - 83: o00ooo0 / i1iIIIiI1I
 if parameters :
  iIIIIii1 = parameters [ 1 : ] . split ( "&" )
  for oo000OO00Oo in iIIIIii1 :
   O0OOO0OOoO0O = oo000OO00Oo . split ( '=' )
   if ( len ( O0OOO0OOoO0O ) ) == 2 :
    I11i1I1I [ O0OOO0OOoO0O [ 0 ] ] = O0OOO0OOoO0O [ 1 ]
 return I11i1I1I
 if 70 - 70: o0O0 * Ii11111i * o00oo / iI1OoOooOOOO
oO = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 93 - 93: iiI1i1 % o00 . iiI1i1 * O00O0O0O0 % iI1OoOooOOOO . ii1IiI1i
if os . path . exists ( oO ) == False :
 os . mkdir ( oO )
iI1ii1Ii = os . path . join ( oO , 'visitor' )
if 92 - 92: oO0o
if os . path . exists ( iI1ii1Ii ) == False :
 from random import randint
 i1OOO = open ( iI1ii1Ii , "w" )
 i1OOO . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 i1OOO . close ( )
 if 59 - 59: ii1IiI1i + OOooo000oo0 * oO0o + i1
def Oo0OoO00oOO0o ( utm_url ) :
 OOO00O = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  ii1i1I1i = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOO00O }
 )
  o00oOO0 = urllib2 . urlopen ( ii1i1I1i ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return o00oOO0
 if 84 - 84: o00 * iiI1i1 / o00oo - iiI
def IiI1 ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  Oo0O00Oo0o0 = "1.0"
  O00O0oOO00O00 = open ( iI1ii1Ii ) . read ( )
  i1Oo00 = "XomGiaiTri"
  i1i = "UA-52209804-2"
  iiI111I1iIiI = "www.viettv24.com"
  II = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
   if 65 - 65: iI1OoOooOOOO . ii1I / iiI - iI1OoOooOOOO
   if 21 - 21: IIIiiIIii * ii1I
   if 91 - 91: o0O0
   if 15 - 15: ii1IiI1i
   if 18 - 18: i11iIiiIii . i1 % OOooo000oo0 / iiI
  else :
   if group == "None" :
    Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 + "/" + name ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
    if 75 - 75: oO0o % II1i % II1i . O00O0O0O0
    if 5 - 5: II1i * i1iIIIiI1I + oO0o . Oo0oO0ooo + oO0o
    if 91 - 91: iiI
    if 61 - 61: ii1IiI1i
    if 64 - 64: i1iIIIiI1I / oO0o - iiI - o00oo
   else :
    Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 + "/" + group + "/" + name ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
    if 86 - 86: o00oo % oO0o / IIIiiIIii / oO0o
    if 42 - 42: iiI1i1
    if 67 - 67: O00O0O0O0 . i11iiII . iiI
    if 10 - 10: o00ooo0 % o00ooo0 - ii1I / Oo0oO0ooo + iI1OoOooOOOO
    if 87 - 87: o00 * o00ooo0 + Oo0oO0ooo / ii1I / i11iiII
    if 37 - 37: i11iiII - i1iIIIiI1I * o00 % i11iIiiIii - O00O0O0O0
  print "============================ POSTING ANALYTICS ============================"
  Oo0OoO00oOO0o ( Ii1I1IIii1II )
  if 83 - 83: o00oo / IIIiiIIii
  if not group == "None" :
   iIIiIi1iIII1 = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iiI111I1iIiI ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i1Oo00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i1Oo00 ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O00O0oOO00O00 , "1" , "2" ] )
   if 78 - 78: iiI . o00 . ii1IiI1i % Oo0oO0ooo
   if 49 - 49: iI1OoOooOOOO / iiI1i1 . ii1IiI1i
   if 68 - 68: i11iIiiIii % o00ooo0 + i11iIiiIii
   if 31 - 31: ii1IiI1i . IIIiiIIii
   if 1 - 1: Ii11111i / II1i % i11iiII * o0O0 . i11iIiiIii
   if 2 - 2: o00ooo0 * o00oo - ii1I + IIIiiIIii . o00 % i11iiII
   if 92 - 92: i11iiII
   if 25 - 25: Ii11111i - IIIiiIIii / OOooo000oo0 / II1i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    Oo0OoO00oOO0o ( iIIiIi1iIII1 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 12 - 12: IIIiiIIii * i11iiII % i1 % ii1I
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 20 - 20: Oo0oO0ooo % iI1OoOooOOOO / iI1OoOooOOOO + iI1OoOooOOOO
III1IiiI = o0Oo0O0Oo00oO ( sys . argv [ 2 ] )
iIi1 = III1IiiI . get ( 'mode' )
oo = III1IiiI . get ( 'url' )
IIIII11I1IiI = III1IiiI . get ( 'name' )
if type ( oo ) == type ( str ( ) ) :
 oo = urllib . unquote_plus ( oo )
if type ( IIIII11I1IiI ) == type ( str ( ) ) :
 IIIII11I1IiI = urllib . unquote_plus ( IIIII11I1IiI )
 if 16 - 16: ii1I
oOooOOOoOo = str ( sys . argv [ 1 ] )
if iIi1 == 'index' :
 IiI1 ( "Browse" , IIIII11I1IiI )
 o0oOoO00o ( oo )
elif iIi1 == 'search' :
 IiI1 ( "None" , "Search" )
 I1iiiiI1iII ( )
elif iIi1 == 'videosbyregion' :
 IiI1 ( "Browse" , IIIII11I1IiI )
 i1I1ii1II1iII ( )
elif iIi1 == 'videosbycategory' :
 IiI1 ( "Browse" , IIIII11I1IiI )
 IIII ( )
elif iIi1 == 'mirrors' :
 IiI1 ( "Browse" , IIIII11I1IiI )
 OoO000 ( oo )
elif iIi1 == 'episodes' :
 IiI1 ( "Browse" , IIIII11I1IiI )
 O0o0Oo ( oo , IIIII11I1IiI )
elif iIi1 == 'loadvideo' :
 IiI1 ( "Play" , IIIII11I1IiI + "/" + oo )
 i1Iii1i1I = xbmcgui . DialogProgress ( )
 i1Iii1i1I . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 ooo ( oo , IIIII11I1IiI )
 i1Iii1i1I . close ( )
 del i1Iii1i1I
else :
 IiI1 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( oOooOOOoOo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
