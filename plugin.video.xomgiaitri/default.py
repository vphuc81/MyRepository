#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 while True :
  ii11i = xbmc . getInfoLabel ( "Network.MacAddress" )
  if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , ii11i . lower ( ) ) : break
 oOooOoO0Oo0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s" % ( ii11i , "16" ) ) . read ( )
 if "allowed" in oOooOoO0Oo0O :
  iI1 ( 'Search' , 'http://www.xom60.com/xem/search/%s/1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  iI1 ( 'Phim Lẻ' , 'http://www.xom60.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  iI1 ( 'Phim Bộ' , 'http://www.xom60.com/xem/the-loai/phim-bo' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  iI1 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom60.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  iI1 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom60.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 else :
  iI1 ( 'Search' , 'http://www.xom60.com/xem/search/%s/1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  iI1 ( 'Phim Lẻ' , 'http://www.xom60.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  iI1 ( 'Phim Bộ' , 'http://www.xom60.com/xem/the-loai/phim-bo' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  iI1 ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom60.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  iI1 ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom60.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
  if 73 - 73: III - oo00oOOo * Oooo000o % OOo . OOO
 IiI1ii1 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 #IiI1ii1 = xbmc . translatePath ( os . path . join ( IiI1ii1 , "temp.jpg" ) )
 #urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/xomgiaitri.jpg' , IiI1ii1 )
 #oooOOooo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI1ii1 )
 #o0oo0oo0OO00 = xbmcgui . WindowDialog ( )
 #o0oo0oo0OO00 . addControl ( oooOOooo )
 #o0oo0oo0OO00 . doModal ( )
 if 20 - 20: i111iII
def oOOo ( ) :
 iI1 ( "Hồng Kong" , "http://www.xom60.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 iI1 ( "Hồng Kong (VNLT)" , "http://www.xom60.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 iI1 ( "Hàn Quốc" , "http://www.xom60.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 iI1 ( "Hàn Quốc (vietsub)" , "http://www.xom60.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 iI1 ( "Trung Quốc" , "http://www.xom60.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 iI1 ( "Đài Loan" , "http://www.xom60.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 iI1 ( "Việt Nam" , "http://www.xom60.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 iI1 ( "Thái Lan" , "http://www.xom60.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 iI1 ( "Các Loại Khác" , "http://www.xom60.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 25 - 25: O0 + OoOoOoO0o0OO * Ooo0OO0oOO * Ii * o0o - OOO0o0o
def Ii1iI ( ) :
 iI1 ( "Hành Động" , "http://www.xom60.com/xem/category/8/hanh-dong.html" , "index" , "" )
 iI1 ( "Tình Cảm" , "http://www.xom60.com/xem/category/9/tinh-cam.html" , "index" , "" )
 iI1 ( "Phim Hài" , "http://www.xom60.com/xem/category/10/phim-hai.html" , "index" , "" )
 iI1 ( "Kinh Dị" , "http://www.xom60.com/xem/category/11/kinh-di.html" , "index" , "" )
 iI1 ( "Kiếm Hiệp" , "http://www.xom60.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 iI1 ( "Việt Nam" , "http://www.xom60.com/xem/category/15/viet-nam.html" , "index" , "" )
 iI1 ( "Hài Kịch" , "http://www.xom60.com/xem/category/16/hai-kich.html" , "index" , "" )
 iI1 ( "Ca Nhạc" , "http://www.xom60.com/xem/category/17/ca-nhac.html" , "index" , "" )
 iI1 ( "Cải Lương" , "http://www.xom60.com/xem/category/18/cai-luong.html" , "index" , "" )
 iI1 ( "Phóng Sự" , "http://www.xom60.com/xem/category/19/phong-su.html" , "index" , "" )
 iI1 ( "Các Loại Khác" , "http://www.xom60.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 100 - 100: i11Ii11I1Ii1i . ooO - OOoO / ooo0Oo0 * i1 - ooo0Oo0
def Oooo0000 ( url ) :
 i11 = I11 ( url )
 Oo0o0000o0o0 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( i11 )
 for oOo0oooo00o , oO0o0o0ooO0oO , oo0o0O00 in Oo0o0000o0o0 :
  iI1 ( "[B]" + oO0o0o0ooO0oO + "[/B]" , "http://www.xom60.com/xem" + oOo0oooo00o , 'mirrors' , oo0o0O00 )
 oO = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( i11 . replace ( "'" , '"' ) )
 for oOo0oooo00o , i1iiIIiiI111 in oO :
  iI1 ( i1iiIIiiI111 , oOo0oooo00o . replace ( "./" , "http://www.xom60.com/xem/" ) , 'index' , "" )
  if 62 - 62: i11iIiiIii - Oooo000o
def IIIiI11ii ( ) :
 try :
  O000oo = xbmc . Keyboard ( '' , 'Enter search text' )
  O000oo . doModal ( )
  if 3 - 3: ooO + iiI
  if ( O000oo . isConfirmed ( ) ) :
   I1Ii = urllib . quote_plus ( O000oo . getText ( ) )
  Oooo0000 ( o0oOo0Ooo0O % I1Ii )
 except : pass
 if 81 - 81: Ooo0OO0oOO * OOoO * OOO0o0o - ooO - OoOoOoO0o0OO
def OooO0OO ( url ) :
 print url
 iiiIi = IiIIIiI1I1 ( url )
 i11 = I11 ( iiiIi )
 OoO000 = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( i11 )
 for IIiiIiI1 in OoO000 :
  iiIiIIi = [ ]
  if not any ( x in IIiiIiI1 for x in iiIiIIi ) :
   iI1 ( IIiiIiI1 , iiiIi . encode ( "utf-8" ) , 'episodes' , "" )
   if 65 - 65: O0
def ii1IOooO0 ( url , name ) :
 i11 = I11 ( url )
 II11iiii1Ii = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % urllib2 . unquote ( name ) ) . findall ( i11 )
 OO0oOoo = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( II11iiii1Ii [ 0 ] )
 if ( "episode_bg_2" in II11iiii1Ii [ 0 ] ) :
  O0o0Oo = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( II11iiii1Ii [ 0 ] )
  Oo00OOOOO ( "Part - " + O0o0Oo [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , url , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 for O0O , O00o0OO in OO0oOoo :
  Oo00OOOOO ( "Part - " + O00o0OO . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , "http://www.xom60.com/web/" + O0O , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 44 - 44: OOoO / iiI % oo00oOOo * Ii + OOO
def IiIIIiI1I1 ( url ) :
 Ii1I = I11 ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( Ii1I ) [ 0 ]
 if 89 - 89: i11iIiiIii / iiI * O0 % o0o % Ii
def Ii1 ( url , name ) :
 i11 = I11 ( url )
 if ( "proxy.link" in i11 ) :
  III1i1i = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( i11 )
  i11 = I11 ( III1i1i [ 0 ] )
  if 26 - 26: III
 III1i1i = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( i11 )
 IiiI11Iiiii = xbmcgui . ListItem ( name )
 IiiI11Iiiii . setProperty ( "IsPlayable" , "true" )
 IiiI11Iiiii . setPath ( III1i1i [ 0 ] )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiI11Iiiii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiiI11Iiiii )
 if 18 - 18: OoOoOoO0o0OO
def I11 ( url ) :
 I1i1I1II = urllib2 . Request ( url )
 I1i1I1II . add_header ( 'Host' , 'phim.xixam.com' )
 I1i1I1II . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 I1i1I1II . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 i1IiIiiI = urllib2 . urlopen ( I1i1I1II )
 i11 = i1IiIiiI . read ( )
 i1IiIiiI . close ( )
 i11 = '' . join ( i11 . splitlines ( ) ) . replace ( '\'' , '"' )
 i11 = i11 . replace ( '\n' , '' )
 i11 = i11 . replace ( '\t' , '' )
 i11 = re . sub ( '  +' , ' ' , i11 )
 i11 = i11 . replace ( '> <' , '><' )
 return i11
 if 31 - 31: i11Ii11I1Ii1i . i11Ii11I1Ii1i - OoOoOoO0o0OO / i111iII + i1 * OOo
def Oo00OOOOO ( name , url , mode , iconimage , mirrorname ) :
 O0ooOooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO0OOO00oo . setProperty ( "IsPlayable" , "true" )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOooooO , listitem = OOO0OOO00oo )
 return o00O
 if 31 - 31: Oooo000o - o0o . ooo0Oo0 % O0 - iiI
def iI1 ( name , url , mode , iconimage ) :
 O0ooOooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOooooO , listitem = OOO0OOO00oo , isFolder = True )
 return o00O
 if 4 - 4: Oooo000o / i1 . ooO
def O0oo0OO0oOOOo ( k , e ) :
 i1i1i11IIi = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for II1III in range ( len ( e ) ) :
  iI1iI1I1i1I = k [ II1III % len ( k ) ]
  iIi11Ii1 = chr ( ( 256 + ord ( e [ II1III ] ) - ord ( iI1iI1I1i1I ) ) % 256 )
  i1i1i11IIi . append ( iIi11Ii1 )
 return "" . join ( i1i1i11IIi )
 if 50 - 50: Oooo000o - i1 * Ooo0OO0oOO / ooo0Oo0 + OoOoOoO0o0OO
def O0O0O ( parameters ) :
 oO0Oo = { }
 if 54 - 54: OoOoOoO0o0OO - OOo + III
 if parameters :
  O0o0 = parameters [ 1 : ] . split ( "&" )
  for OO00Oo in O0o0 :
   O0OOO0OOoO0O = OO00Oo . split ( '=' )
   if ( len ( O0OOO0OOoO0O ) ) == 2 :
    oO0Oo [ O0OOO0OOoO0O [ 0 ] ] = O0OOO0OOoO0O [ 1 ]
 return oO0Oo
 if 70 - 70: OOoO * OOO * OOO0o0o / i11Ii11I1Ii1i
oOOOoO0O00o0 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 30 - 30: OoOoOoO0o0OO . i11Ii11I1Ii1i - III
if os . path . exists ( oOOOoO0O00o0 ) == False :
 os . mkdir ( oOOOoO0O00o0 )
Ii1iIiii1 = os . path . join ( oOOOoO0O00o0 , 'visitor' )
if 91 - 91: i111iII . Ooo0OO0oOO + i111iII - ooO / III
if os . path . exists ( Ii1iIiii1 ) == False :
 from random import randint
 iII1 = open ( Ii1iIiii1 , "w" )
 iII1 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iII1 . close ( )
 if 30 - 30: Oooo000o - o0o - i11iIiiIii % O0 - Oooo000o * i11Ii11I1Ii1i
def oO00O0O0O ( utm_url ) :
 i1ii1iiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  I1i1I1II = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : i1ii1iiI }
 )
  i1IiIiiI = urllib2 . urlopen ( I1i1I1II ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return i1IiIiiI
 if 98 - 98: ooO * ooO / ooO + OOO0o0o
def ii111111I1iII ( group , name ) :
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
  O00ooo0O0 = "1.0"
  i1iIi1iIi1i = open ( Ii1iIiii1 ) . read ( )
  I1I1iIiII1 = "XomGiaiTri"
  i11i1I1 = "UA-52209804-2"
  ii1IOo0ooOo0o = "www.viettv24.com"
  Ii1i1 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iiIii = Ii1i1 + "?" + "utmwv=" + O00ooo0O0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1iIi1iIi1i , "1" , "1" , "2" ] )
   if 79 - 79: III / iiI
   if 75 - 75: O0 % OoOoOoO0o0OO % OoOoOoO0o0OO . ooo0Oo0
   if 5 - 5: OoOoOoO0o0OO * i1 + O0 . o0o + O0
   if 91 - 91: iiI
   if 61 - 61: Oooo000o
  else :
   if group == "None" :
    iiIii = Ii1i1 + "?" + "utmwv=" + O00ooo0O0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1iIi1iIi1i , "1" , "1" , "2" ] )
    if 64 - 64: i1 / O0 - iiI - OOO0o0o
    if 86 - 86: OOO0o0o % O0 / OOo / O0
    if 42 - 42: i111iII
    if 67 - 67: ooo0Oo0 . ooO . iiI
    if 10 - 10: Ooo0OO0oOO % Ooo0OO0oOO - ii1I / o0o + i11Ii11I1Ii1i
   else :
    iiIii = Ii1i1 + "?" + "utmwv=" + O00ooo0O0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + group + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1iIi1iIi1i , "1" , "1" , "2" ] )
    if 87 - 87: Ii * Ooo0OO0oOO + o0o / ii1I / ooO
    if 37 - 37: ooO - i1 * Ii % i11iIiiIii - ooo0Oo0
    if 83 - 83: OOO0o0o / OOo
    if 34 - 34: OOoO
    if 57 - 57: Ii . OOO0o0o . oo00oOOo
    if 42 - 42: OOO0o0o + Ooo0OO0oOO % iiI
  print "============================ POSTING ANALYTICS ============================"
  oO00O0O0O ( iiIii )
  if 6 - 6: Ii
  if not group == "None" :
   oOOo0oOo0 = Ii1i1 + "?" + "utmwv=" + O00ooo0O0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( ii1IOo0ooOo0o ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + I1I1iIiII1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , i1iIi1iIi1i , "1" , "2" ] )
   if 49 - 49: OOO . i11iIiiIii - oo00oOOo / Oooo000o . OOo
   if 1 - 1: OOO / OoOoOoO0o0OO % ooO * OOoO . i11iIiiIii
   if 2 - 2: Ooo0OO0oOO * OOO0o0o - ii1I + OOo . Ii % ooO
   if 92 - 92: ooO
   if 25 - 25: OOO - OOo / III / OoOoOoO0o0OO
   if 12 - 12: OOo * ooO % oo00oOOo % ii1I
   if 20 - 20: o0o % i11Ii11I1Ii1i / i11Ii11I1Ii1i + i11Ii11I1Ii1i
   if 45 - 45: Ii - OOoO - III - i111iII . Oooo000o / iiI
   try :
    print "============================ POSTING TRACK EVENT ============================"
    oO00O0O0O ( oOOo0oOo0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 51 - 51: iiI + ooO
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 8 - 8: Ii * O0 - i11Ii11I1Ii1i - i111iII * o0o % OOo
ii = O0O0O ( sys . argv [ 2 ] )
oOooOOOoOo = ii . get ( 'mode' )
o0oOo0Ooo0O = ii . get ( 'url' )
i1Iii1i1I = ii . get ( 'name' )
if type ( o0oOo0Ooo0O ) == type ( str ( ) ) :
 o0oOo0Ooo0O = urllib . unquote_plus ( o0oOo0Ooo0O )
if type ( i1Iii1i1I ) == type ( str ( ) ) :
 i1Iii1i1I = urllib . unquote_plus ( i1Iii1i1I )
 if 91 - 91: Ooo0OO0oOO + OOo . o0o * Ooo0OO0oOO + OOo * OOO
O000OOOOOo = str ( sys . argv [ 1 ] )
if oOooOOOoOo == 'index' :
 ii111111I1iII ( "Browse" , i1Iii1i1I )
 Oooo0000 ( o0oOo0Ooo0O )
elif oOooOOOoOo == 'search' :
 ii111111I1iII ( "None" , "Search" )
 IIIiI11ii ( )
elif oOooOOOoOo == 'videosbyregion' :
 ii111111I1iII ( "Browse" , i1Iii1i1I )
 oOOo ( )
elif oOooOOOoOo == 'videosbycategory' :
 ii111111I1iII ( "Browse" , i1Iii1i1I )
 Ii1iI ( )
elif oOooOOOoOo == 'mirrors' :
 ii111111I1iII ( "Browse" , i1Iii1i1I )
 OooO0OO ( o0oOo0Ooo0O )
elif oOooOOOoOo == 'episodes' :
 ii111111I1iII ( "Browse" , i1Iii1i1I )
 ii1IOooO0 ( o0oOo0Ooo0O , i1Iii1i1I )
elif oOooOOOoOo == 'loadvideo' :
 ii111111I1iII ( "Play" , i1Iii1i1I + "/" + o0oOo0Ooo0O )
 Iiii1i1 = xbmcgui . DialogProgress ( )
 Iiii1i1 . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 Ii1 ( o0oOo0Ooo0O , i1Iii1i1I )
 Iiii1i1 . close ( )
 del Iiii1i1
else :
 ii111111I1iII ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( O000OOOOOo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
