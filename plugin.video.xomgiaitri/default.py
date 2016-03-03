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
  OoOoOO00 ( 'Search' , 'http://www.xom68.com/xem/search/%s/1.html' , 'search' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom68.com/xem/the-loai/phim-dien-anh' , 'index' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom68.com/xem/the-loai/phim-bo' , 'index' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom68.com/' , 'videosbyregion' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom68.com/' , 'videosbycategory' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
 else :
  OoOoOO00 ( 'Search' , 'http://www.xom68.com/xem/search/%s/1.html' , 'search' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Lẻ' , 'http://www.xom68.com/xem/the-loai/phim-dien-anh' , 'index' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Bộ' , 'http://www.xom68.com/xem/the-loai/phim-bo' , 'index' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom68.com/' , 'videosbyregion' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  OoOoOO00 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom68.com/' , 'videosbycategory' , 'https://googledrive.com/host/0B7zkkQwo5pr5fjVUZG5MRkhFalRKTHF0T0poZnd6aTZUbmx1ZDZWMkwtR3FHZFhtdTB4TTQ/xomgiaitri.png' )
  if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
 I11iIi1I = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11iIi1I = xbmc . translatePath ( os . path . join ( I11iIi1I , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'http://drive.google.com/uc?export=jpg&id=0B-ygKtjD8Sc-OUxwbVR5ZzZsbFJFT3A5aS04YlJkdDJtQ3BF' , I11iIi1I )
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
 if 85 - 85: i1iIIIiI1I . i11iiII - iiI1i1 % i1iIIIiI1I % ii1IiI1i
 OO0o00o = re . compile ( '<div class="listserver"><span class="name"[^>]*>.+?</span>(.+?)</div>' ) . findall ( i1oOOoo00O0O )
 oOOo0oo = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( OO0o00o [ int ( Oo00OOOOO ) - 1 ] )
 if ( "episode_bg_2" in OO0o00o [ int ( Oo00OOOOO ) - 1 ] ) :
  o0oo0o0O00OO = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( OO0o00o [ int ( Oo00OOOOO ) - 1 ] )
  o0oO ( "Part - " + o0oo0o0O00OO [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , url , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 for I1i1iii , i1iiI11I in oOOo0oo :
  o0oO ( "Part - " + i1iiI11I . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , "http://www.xom68.com/xem/" + I1i1iii , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 29 - 29: OOooo000oo0
def iiIiIIi ( url ) :
 iI = i1111 ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( iI ) [ 0 ]
 if 28 - 28: Oo0oO0ooo - o0O0 . o0O0 + oO0o - OOooo000oo0 + iiI
def oOoOooOo0o0 ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 if ( "proxy.link" in i1oOOoo00O0O ) :
  OOOO = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( i1oOOoo00O0O )
  i1oOOoo00O0O = i1111 ( OOOO [ 0 ] )
 OOOO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( i1oOOoo00O0O )
 OOO00 = xbmcgui . ListItem ( name )
 OOO00 . setProperty ( "IsPlayable" , "true" )
 if "://" not in OOOO [ 0 ] :
  OOO00 . setPath ( "http://www.xom68.com/xem/" + OOOO [ 0 ] )
 else :
  OOO00 . setPath ( OOOO [ 0 ] )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOO00 )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OOO00 )
 if 21 - 21: OOooo000oo0 - OOooo000oo0
def i1111 ( url ) :
 iIii11I = urllib2 . Request ( url )
 iIii11I . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 iIii11I . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OOO0OOO00oo = urllib2 . urlopen ( iIii11I )
 i1oOOoo00O0O = OOO0OOO00oo . read ( )
 OOO0OOO00oo . close ( )
 i1oOOoo00O0O = '' . join ( i1oOOoo00O0O . splitlines ( ) ) . replace ( '\'' , '"' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\n' , '' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\t' , '' )
 i1oOOoo00O0O = re . sub ( '  +' , ' ' , i1oOOoo00O0O )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '> <' , '><' )
 return i1oOOoo00O0O
 if 31 - 31: ii1IiI1i - Oo0oO0ooo . O00O0O0O0 % oO0o - iiI
def o0oO ( name , url , mode , iconimage , mirrorname ) :
 iii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 O0oo0OO0oOOOo = True
 i1i1i11IIi = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 i1i1i11IIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1i1i11IIi . setProperty ( "IsPlayable" , "true" )
 O0oo0OO0oOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii11 , listitem = i1i1i11IIi )
 return O0oo0OO0oOOOo
 if 33 - 33: II1i + Oo0oO0ooo * iiI1i1 - Ii11111i / o00 % iI1OoOooOOOO
def OoOoOO00 ( name , url , mode , iconimage ) :
 iii11 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0oo0OO0oOOOo = True
 i1i1i11IIi = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i1i11IIi . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O0oo0OO0oOOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = iii11 , listitem = i1i1i11IIi , isFolder = True )
 return O0oo0OO0oOOOo
 if 21 - 21: iiI1i1 * ii1I % o00 * i1
def Ii11Ii1I ( k , e ) :
 O00oO = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for OooO0 in range ( len ( e ) ) :
  I11i1I1I = k [ OooO0 % len ( k ) ]
  oO0Oo = chr ( ( 256 + ord ( e [ OooO0 ] ) - ord ( I11i1I1I ) ) % 256 )
  O00oO . append ( oO0Oo )
 return "" . join ( O00oO )
 if 54 - 54: II1i - IIIiiIIii + OOooo000oo0
def O0o0 ( parameters ) :
 OO00Oo = { }
 if 51 - 51: o0O0 * II1i + o00oo + iiI1i1
 if parameters :
  o0O0O00 = parameters [ 1 : ] . split ( "&" )
  for o000o in o0O0O00 :
   I11IiI1I11i1i = o000o . split ( '=' )
   if ( len ( I11IiI1I11i1i ) ) == 2 :
    OO00Oo [ I11IiI1I11i1i [ 0 ] ] = I11IiI1I11i1i [ 1 ]
 return OO00Oo
 if 38 - 38: II1i
Oo0O = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 25 - 25: oO0o . ii1IiI1i / i11iiII . Oo0oO0ooo * iiI1i1 . IIIiiIIii
if os . path . exists ( Oo0O ) == False :
 os . mkdir ( Oo0O )
Oo0oOOo = os . path . join ( Oo0O , 'visitor' )
if 58 - 58: ii1IiI1i * Oo0oO0ooo * o00ooo0 / Oo0oO0ooo
if os . path . exists ( Oo0oOOo ) == False :
 from random import randint
 oO0o0OOOO = open ( Oo0oOOo , "w" )
 oO0o0OOOO . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oO0o0OOOO . close ( )
 if 68 - 68: i11iiII - O00O0O0O0 - IIIiiIIii - o00ooo0 + o00oo
def iiiI1I11i1 ( utm_url ) :
 IIi1i11111 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iIii11I = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : IIi1i11111 }
 )
  OOO0OOO00oo = urllib2 . urlopen ( iIii11I ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OOO0OOO00oo
 if 81 - 81: i11iIiiIii % oO0o - Oo0oO0ooo
def O0ooo0O0oo0 ( group , name ) :
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
  oo0oOo = "1.0"
  o000O0o = open ( Oo0oOOo ) . read ( )
  iI1iII1 = "XomGiaiTri"
  oO0OOoo0OO = "UA-52209804-2"
  O0 = "www.viettv24.com"
  ii1ii1ii = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oooooOoo0ooo = ii1ii1ii + "?" + "utmwv=" + oo0oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( iI1iII1 ) + "&utmac=" + oO0OOoo0OO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o000O0o , "1" , "1" , "2" ] )
   if 6 - 6: o00oo - iI1OoOooOOOO + ii1I - O00O0O0O0 - i11iIiiIii
   if 79 - 79: oO0o - iiI * iiI1i1 + oO0o % iiI * iiI
   if 61 - 61: ii1IiI1i
   if 64 - 64: i1iIIIiI1I / oO0o - iiI - o00oo
   if 86 - 86: o00oo % oO0o / IIIiiIIii / oO0o
  else :
   if group == "None" :
    oooooOoo0ooo = ii1ii1ii + "?" + "utmwv=" + oo0oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( iI1iII1 + "/" + name ) + "&utmac=" + oO0OOoo0OO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o000O0o , "1" , "1" , "2" ] )
    if 42 - 42: iiI1i1
    if 67 - 67: O00O0O0O0 . i11iiII . iiI
    if 10 - 10: o00ooo0 % o00ooo0 - ii1I / Oo0oO0ooo + iI1OoOooOOOO
    if 87 - 87: o00 * o00ooo0 + Oo0oO0ooo / ii1I / i11iiII
    if 37 - 37: i11iiII - i1iIIIiI1I * o00 % i11iIiiIii - O00O0O0O0
   else :
    oooooOoo0ooo = ii1ii1ii + "?" + "utmwv=" + oo0oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( iI1iII1 + "/" + group + "/" + name ) + "&utmac=" + oO0OOoo0OO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o000O0o , "1" , "1" , "2" ] )
    if 83 - 83: o00oo / IIIiiIIii
    if 34 - 34: o0O0
    if 57 - 57: o00 . o00oo . i1
    if 42 - 42: o00oo + o00ooo0 % iiI
    if 6 - 6: o00
    if 68 - 68: oO0o - iiI1i1
  print "============================ POSTING ANALYTICS ============================"
  iiiI1I11i1 ( oooooOoo0ooo )
  if 28 - 28: iiI1i1 . Oo0oO0ooo / Oo0oO0ooo + Ii11111i . o00ooo0
  if not group == "None" :
   iiii = ii1ii1ii + "?" + "utmwv=" + oo0oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O0 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + iI1iII1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( iI1iII1 ) + "&utmac=" + oO0OOoo0OO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , o000O0o , "1" , "2" ] )
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
    iiiI1I11i1 ( iiii )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 8 - 8: o00 * oO0o - iI1OoOooOOOO - iiI1i1 * Oo0oO0ooo % IIIiiIIii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 48 - 48: iiI
I1IiiI = O0o0 ( sys . argv [ 2 ] )
IIi = I1IiiI . get ( 'mode' )
oo = I1IiiI . get ( 'url' )
i1Iii1i1I = I1IiiI . get ( 'name' )
if type ( oo ) == type ( str ( ) ) :
 oo = urllib . unquote_plus ( oo )
if type ( i1Iii1i1I ) == type ( str ( ) ) :
 i1Iii1i1I = urllib . unquote_plus ( i1Iii1i1I )
 if 91 - 91: o00ooo0 + IIIiiIIii . Oo0oO0ooo * o00ooo0 + IIIiiIIii * Ii11111i
O000OOOOOo = str ( sys . argv [ 1 ] )
if IIi == 'index' :
 O0ooo0O0oo0 ( "Browse" , i1Iii1i1I )
 o0oOoO00o ( oo )
elif IIi == 'search' :
 O0ooo0O0oo0 ( "None" , "Search" )
 I1iiiiI1iII ( )
elif IIi == 'videosbyregion' :
 O0ooo0O0oo0 ( "Browse" , i1Iii1i1I )
 i1I1ii1II1iII ( )
elif IIi == 'videosbycategory' :
 O0ooo0O0oo0 ( "Browse" , i1Iii1i1I )
 IIII ( )
elif IIi == 'mirrors' :
 O0ooo0O0oo0 ( "Browse" , i1Iii1i1I )
 OoO000 ( oo )
elif IIi == 'episodes' :
 O0ooo0O0oo0 ( "Browse" , i1Iii1i1I )
 O0o0Oo ( oo , i1Iii1i1I )
elif IIi == 'loadvideo' :
 O0ooo0O0oo0 ( "Play" , i1Iii1i1I + "/" + oo )
 Iiii1i1 = xbmcgui . DialogProgress ( )
 Iiii1i1 . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 oOoOooOo0o0 ( oo , i1Iii1i1I )
 Iiii1i1 . close ( )
 del Iiii1i1
else :
 O0ooo0O0oo0 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( O000OOOOOo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
