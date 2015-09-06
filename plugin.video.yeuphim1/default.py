#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.yeuphim1'
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
  OoOoOO00 ( 'Search' , 'http://www.xom60.com/xem/search/%s/1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom60.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom60.com/xem/the-loai/phim-bo' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom60.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom60.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 else :
  OoOoOO00 ( 'Search' , 'http://www.xom60.com/xem/search/%s/1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom60.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom60.com/xem/the-loai/phim-bo' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom60.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom60.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
  if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
 I11iIi1I = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11iIi1I = xbmc . translatePath ( os . path . join ( I11iIi1I , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/yeuphim.jpg' , I11iIi1I )
 IiiIII111iI = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11iIi1I )
 IiII = xbmcgui . WindowDialog ( )
 IiII . addControl ( IiiIII111iI )
 IiII . doModal ( )'''
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 OoOoOO00 ( "Hồng Kong" , "http://www.xom60.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 OoOoOO00 ( "Hồng Kong (VNLT)" , "http://www.xom60.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 OoOoOO00 ( "Hàn Quốc" , "http://www.xom60.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 OoOoOO00 ( "Hàn Quốc (vietsub)" , "http://www.xom60.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 OoOoOO00 ( "Trung Quốc" , "http://www.xom60.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 OoOoOO00 ( "Đài Loan" , "http://www.xom60.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 OoOoOO00 ( "Việt Nam" , "http://www.xom60.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 OoOoOO00 ( "Thái Lan" , "http://www.xom60.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 OoOoOO00 ( "Các Loại Khác" , "http://www.xom60.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( ) :
 OoOoOO00 ( "Hành Động" , "http://www.xom60.com/xem/category/8/hanh-dong.html" , "index" , "" )
 OoOoOO00 ( "Tình Cảm" , "http://www.xom60.com/xem/category/9/tinh-cam.html" , "index" , "" )
 OoOoOO00 ( "Phim Hài" , "http://www.xom60.com/xem/category/10/phim-hai.html" , "index" , "" )
 OoOoOO00 ( "Kinh Dị" , "http://www.xom60.com/xem/category/11/kinh-di.html" , "index" , "" )
 OoOoOO00 ( "Kiếm Hiệp" , "http://www.xom60.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 OoOoOO00 ( "Việt Nam" , "http://www.xom60.com/xem/category/15/viet-nam.html" , "index" , "" )
 OoOoOO00 ( "Hài Kịch" , "http://www.xom60.com/xem/category/16/hai-kich.html" , "index" , "" )
 OoOoOO00 ( "Ca Nhạc" , "http://www.xom60.com/xem/category/17/ca-nhac.html" , "index" , "" )
 OoOoOO00 ( "Cải Lương" , "http://www.xom60.com/xem/category/18/cai-luong.html" , "index" , "" )
 OoOoOO00 ( "Phóng Sự" , "http://www.xom60.com/xem/category/19/phong-su.html" , "index" , "" )
 OoOoOO00 ( "Các Loại Khác" , "http://www.xom60.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( url ) :
 i1oOOoo00O0O = i1111 ( url )
 i11 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( i1oOOoo00O0O )
 for I11 , Oo0o0000o0o0 , oOo0oooo00o in i11 :
  OoOoOO00 ( "[B]" + Oo0o0000o0o0 + "[/B]" , "http://www.xom60.com/xem" + I11 , 'mirrors' , oOo0oooo00o )
 oO0o0o0ooO0oO = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( i1oOOoo00O0O . replace ( "'" , '"' ) )
 for I11 , oo0o0O00 in oO0o0o0ooO0oO :
  OoOoOO00 ( oo0o0O00 , I11 . replace ( "./" , "http://www.xom60.com/xem/" ) , 'index' , "" )
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
 for OooO0 in ooOoo0O :
  II11iiii1Ii = [ ]
  if not any ( x in OooO0 for x in II11iiii1Ii ) :
   OoOoOO00 ( OooO0 , IIiiIiI1 . encode ( "utf-8" ) , 'episodes' , "" )
   if 70 - 70: o00 / ii1I % i1iIIIiI1I % i11iIiiIii . IIIiiIIii
def O0o0Oo ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 Oo00OOOOO = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % urllib2 . unquote ( name ) ) . findall ( i1oOOoo00O0O )
 O0O = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( Oo00OOOOO [ 0 ] )
 if ( "episode_bg_2" in Oo00OOOOO [ 0 ] ) :
  O00o0OO = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( Oo00OOOOO [ 0 ] )
  I11i1 ( "Part - " + O00o0OO [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , url , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 for iIi1ii1I1 , o0 in O0O :
  I11i1 ( "Part - " + o0 . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , "http://www.xom60.com/xem/" + iIi1ii1I1 , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 9 - 9: iI1OoOooOOOO + o00 % iI1OoOooOOOO + i1 . Oo0oO0ooo
def iiIiIIi ( url ) :
 III1i1i = i1111 ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( III1i1i ) [ 0 ]
 if 26 - 26: OOooo000oo0
def IiiI11Iiiii ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 if ( "proxy.link" in i1oOOoo00O0O ) :
  ii1I1i1I = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( i1oOOoo00O0O )
  i1oOOoo00O0O = i1111 ( ii1I1i1I [ 0 ] )
  if 88 - 88: iiI1i1 + iiI / oO0o * i11iiII
 ii1I1i1I = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( i1oOOoo00O0O )
 iiiIi1i1I = xbmcgui . ListItem ( name )
 iiiIi1i1I . setProperty ( "IsPlayable" , "true" )
 iiiIi1i1I . setPath ( ii1I1i1I [ 0 ] )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiIi1i1I )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiIi1i1I )
 if 80 - 80: oO0o - iiI1i1
def i1111 ( url ) :
 OOO00 = urllib2 . Request ( url )
 OOO00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 OOO00 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 iiiiiIIii = urllib2 . urlopen ( OOO00 )
 i1oOOoo00O0O = iiiiiIIii . read ( )
 iiiiiIIii . close ( )
 i1oOOoo00O0O = '' . join ( i1oOOoo00O0O . splitlines ( ) ) . replace ( '\'' , '"' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\n' , '' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\t' , '' )
 i1oOOoo00O0O = re . sub ( '  +' , ' ' , i1oOOoo00O0O )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '> <' , '><' )
 return i1oOOoo00O0O
 if 71 - 71: Oo0oO0ooo + iI1OoOooOOOO * Oo0oO0ooo - iiI1i1 * II1i
def I11i1 ( name , url , mode , iconimage , mirrorname ) :
 Oooo0Ooo000 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 ooii11I = True
 Ooo0OO0oOO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 Ooo0OO0oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Ooo0OO0oOO . setProperty ( "IsPlayable" , "true" )
 ooii11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oooo0Ooo000 , listitem = Ooo0OO0oOO )
 return ooii11I
 if 50 - 50: IIIiiIIii
def OoOoOO00 ( name , url , mode , iconimage ) :
 Oooo0Ooo000 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 ooii11I = True
 Ooo0OO0oOO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Ooo0OO0oOO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 ooii11I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oooo0Ooo000 , listitem = Ooo0OO0oOO , isFolder = True )
 return ooii11I
 if 34 - 34: IIIiiIIii * ii1IiI1i % i11iiII * oO0o - IIIiiIIii
def II1III ( k , e ) :
 iI1iI1I1i1I = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for iIi11Ii1 in range ( len ( e ) ) :
  Ii11iII1 = k [ iIi11Ii1 % len ( k ) ]
  Oo0O0O0ooO0O = chr ( ( 256 + ord ( e [ iIi11Ii1 ] ) - ord ( Ii11iII1 ) ) % 256 )
  iI1iI1I1i1I . append ( Oo0O0O0ooO0O )
 return "" . join ( iI1iI1I1i1I )
 if 15 - 15: o00ooo0 + oO0o - OOooo000oo0 / Oo0oO0ooo
def oo000OO00Oo ( parameters ) :
 O0OOO0OOoO0O = { }
 if 70 - 70: o0O0 * Ii11111i * o00oo / iI1OoOooOOOO
 if parameters :
  oO = parameters [ 1 : ] . split ( "&" )
  for OOoO0O00o0 in oO :
   iII = OOoO0O00o0 . split ( '=' )
   if ( len ( iII ) ) == 2 :
    O0OOO0OOoO0O [ iII [ 0 ] ] = iII [ 1 ]
 return O0OOO0OOoO0O
 if 80 - 80: o0O0 . o00
IIi = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 26 - 26: i11iiII
if os . path . exists ( IIi ) == False :
 os . mkdir ( IIi )
OOO = os . path . join ( IIi , 'visitor' )
if 59 - 59: ii1IiI1i + OOooo000oo0 * oO0o + i1
if os . path . exists ( OOO ) == False :
 from random import randint
 Oo0OoO00oOO0o = open ( OOO , "w" )
 Oo0OoO00oOO0o . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Oo0OoO00oOO0o . close ( )
 if 80 - 80: o00 + Oo0oO0ooo - Oo0oO0ooo % i11iiII
def OoOO0oo0o ( utm_url ) :
 II11i1I11Ii1i = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  OOO00 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : II11i1I11Ii1i }
 )
  iiiiiIIii = urllib2 . urlopen ( OOO00 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iiiiiIIii
 if 97 - 97: i1iIIIiI1I % i11iiII * iI1OoOooOOOO + II1i . Oo0oO0ooo + Oo0oO0ooo
def Oooo0O0oo00oO ( group , name ) :
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
  IIi1i = "1.0"
  I1I1iIiII1 = open ( OOO ) . read ( )
  i11i1I1 = "YeuPhim"
  ii1IOo0ooOo0o = "UA-52209804-2"
  Ii1i1 = "www.viettv24.com"
  iiIii = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   ooo0O = iiIii + "?" + "utmwv=" + IIi1i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11i1I1 ) + "&utmac=" + ii1IOo0ooOo0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1iIiII1 , "1" , "1" , "2" ] )
   if 75 - 75: II1i % II1i . O00O0O0O0
   if 5 - 5: II1i * i1iIIIiI1I + oO0o . Oo0oO0ooo + oO0o
   if 91 - 91: iiI
   if 61 - 61: ii1IiI1i
   if 64 - 64: i1iIIIiI1I / oO0o - iiI - o00oo
  else :
   if group == "None" :
    ooo0O = iiIii + "?" + "utmwv=" + IIi1i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11i1I1 + "/" + name ) + "&utmac=" + ii1IOo0ooOo0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1iIiII1 , "1" , "1" , "2" ] )
    if 86 - 86: o00oo % oO0o / IIIiiIIii / oO0o
    if 42 - 42: iiI1i1
    if 67 - 67: O00O0O0O0 . i11iiII . iiI
    if 10 - 10: o00ooo0 % o00ooo0 - ii1I / Oo0oO0ooo + iI1OoOooOOOO
    if 87 - 87: o00 * o00ooo0 + Oo0oO0ooo / ii1I / i11iiII
   else :
    ooo0O = iiIii + "?" + "utmwv=" + IIi1i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11i1I1 + "/" + group + "/" + name ) + "&utmac=" + ii1IOo0ooOo0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1iIiII1 , "1" , "1" , "2" ] )
    if 37 - 37: i11iiII - i1iIIIiI1I * o00 % i11iIiiIii - O00O0O0O0
    if 83 - 83: o00oo / IIIiiIIii
    if 34 - 34: o0O0
    if 57 - 57: o00 . o00oo . i1
    if 42 - 42: o00oo + o00ooo0 % iiI
    if 6 - 6: o00
  print "============================ POSTING ANALYTICS ============================"
  OoOO0oo0o ( ooo0O )
  if 68 - 68: oO0o - iiI1i1
  if not group == "None" :
   IIiooOOoooooo = iiIii + "?" + "utmwv=" + IIi1i + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( Ii1i1 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i11i1I1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i11i1I1 ) + "&utmac=" + ii1IOo0ooOo0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , I1I1iIiII1 , "1" , "2" ] )
   if 1 - 1: Ii11111i / II1i % i11iiII * o0O0 . i11iIiiIii
   if 2 - 2: o00ooo0 * o00oo - ii1I + IIIiiIIii . o00 % i11iiII
   if 92 - 92: i11iiII
   if 25 - 25: Ii11111i - IIIiiIIii / OOooo000oo0 / II1i
   if 12 - 12: IIIiiIIii * i11iiII % i1 % ii1I
   if 20 - 20: Oo0oO0ooo % iI1OoOooOOOO / iI1OoOooOOOO + iI1OoOooOOOO
   if 45 - 45: o00 - o0O0 - OOooo000oo0 - iiI1i1 . ii1IiI1i / iiI
   if 51 - 51: iiI + i11iiII
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OoOO0oo0o ( IIiooOOoooooo )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 8 - 8: o00 * oO0o - iI1OoOooOOOO - iiI1i1 * Oo0oO0ooo % IIIiiIIii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 48 - 48: iiI
I1IiiI = oo000OO00Oo ( sys . argv [ 2 ] )
IIii1Iii1i1I = I1IiiI . get ( 'mode' )
oo = I1IiiI . get ( 'url' )
OOoO00 = I1IiiI . get ( 'name' )
if type ( oo ) == type ( str ( ) ) :
 oo = urllib . unquote_plus ( oo )
if type ( OOoO00 ) == type ( str ( ) ) :
 OOoO00 = urllib . unquote_plus ( OOoO00 )
 if 40 - 40: IIIiiIIii * iI1OoOooOOOO + Oo0oO0ooo % i11iiII
OOOOOoo0 = str ( sys . argv [ 1 ] )
if IIii1Iii1i1I == 'index' :
 Oooo0O0oo00oO ( "Browse" , OOoO00 )
 o0oOoO00o ( oo )
elif IIii1Iii1i1I == 'search' :
 Oooo0O0oo00oO ( "None" , "Search" )
 I1iiiiI1iII ( )
elif IIii1Iii1i1I == 'videosbyregion' :
 Oooo0O0oo00oO ( "Browse" , OOoO00 )
 i1I1ii1II1iII ( )
elif IIii1Iii1i1I == 'videosbycategory' :
 Oooo0O0oo00oO ( "Browse" , OOoO00 )
 IIII ( )
elif IIii1Iii1i1I == 'mirrors' :
 Oooo0O0oo00oO ( "Browse" , OOoO00 )
 OoO000 ( oo )
elif IIii1Iii1i1I == 'episodes' :
 Oooo0O0oo00oO ( "Browse" , OOoO00 )
 O0o0Oo ( oo , OOoO00 )
elif IIii1Iii1i1I == 'loadvideo' :
 Oooo0O0oo00oO ( "Play" , OOoO00 + "/" + oo )
 ii1 = xbmcgui . DialogProgress ( )
 ii1 . create ( 'yeuphim.com' , 'Loading video. Please wait...' )
 IiiI11Iiiii ( oo , OOoO00 )
 ii1 . close ( )
 del ii1
else :
 Oooo0O0oo00oO ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( OOOOOoo0 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
