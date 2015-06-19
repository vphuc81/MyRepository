#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i ( 'Search' , 'http://www.xom50.com/xem/search/%s/1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
 ii11i ( 'Phim Lẻ' , 'http://www.xom50.com/xem/list/phim-dien-anh' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
 ii11i ( 'Phim Bộ' , 'http://www.xom50.com/xem/list/phim-bo' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
 ii11i ( 'Phim Bộ theo Quốc Gia' , 'http://www.xom02.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
 ii11i ( 'Phim Lẻ theo Thể Loại' , 'http://www.xom02.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
 I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: I11i = xbmc . translatePath ( os . path . join ( I11i , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/xomgiaitri.jpg' , I11i )
 if 49 - 49: O0O = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i )
 if 49 - 49: Oo = xbmcgui . WindowDialog ( )
 if 49 - 49: Oo . addControl ( O0O )
 if 49 - 49: Oo . doModal ( )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
def IiII ( ) :
 ii11i ( "Hồng Kong" , "http://www.xom50.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ii11i ( "Hồng Kong (VNLT)" , "http://www.xom50.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ii11i ( "Hàn Quốc" , "http://www.xom50.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ii11i ( "Hàn Quốc (vietsub)" , "http://www.xom50.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ii11i ( "Trung Quốc" , "http://www.xom50.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ii11i ( "Đài Loan" , "http://www.xom50.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xom50.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ii11i ( "Thái Lan" , "http://www.xom50.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xom50.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 ii11i ( "Hành Động" , "http://www.xom50.com/xem/category/8/hanh-dong.html" , "index" , "" )
 ii11i ( "Tình Cảm" , "http://www.xom50.com/xem/category/9/tinh-cam.html" , "index" , "" )
 ii11i ( "Phim Hài" , "http://www.xom50.com/xem/category/10/phim-hai.html" , "index" , "" )
 ii11i ( "Kinh Dị" , "http://www.xom50.com/xem/category/11/kinh-di.html" , "index" , "" )
 ii11i ( "Kiếm Hiệp" , "http://www.xom50.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xom50.com/xem/category/15/viet-nam.html" , "index" , "" )
 ii11i ( "Hài Kịch" , "http://www.xom50.com/xem/category/16/hai-kich.html" , "index" , "" )
 ii11i ( "Ca Nhạc" , "http://www.xom50.com/xem/category/17/ca-nhac.html" , "index" , "" )
 ii11i ( "Cải Lương" , "http://www.xom50.com/xem/category/18/cai-luong.html" , "index" , "" )
 ii11i ( "Phóng Sự" , "http://www.xom50.com/xem/category/19/phong-su.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xom50.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( url ) :
 Oo0oO0oo0oO00 = i111I ( url )
 II1Ii1iI1i = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( Oo0oO0oo0oO00 )
 for iiI1iIiI , OOo , Ii1IIii11 in II1Ii1iI1i :
  ii11i ( "[B]" + OOo + "[/B]" , "http://www.xom02.com/xem" + iiI1iIiI , 'mirrors' , Ii1IIii11 )
 Oooo0000 = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( Oo0oO0oo0oO00 . replace ( "'" , '"' ) )
 for iiI1iIiI , i11 in Oooo0000 :
  ii11i ( i11 , iiI1iIiI . replace ( "./" , "http://www.xom50.com/xem/" ) , 'index' , "" )
  if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
def I1 ( ) :
 try :
  O0OoOoo00o = xbmc . Keyboard ( '' , 'Enter search text' )
  O0OoOoo00o . doModal ( )
  if 31 - 31: i111IiI + o0OoOoOO00 . ii1IiI1i
  if ( O0OoOoo00o . isConfirmed ( ) ) :
   OOoO00o = urllib . quote_plus ( O0OoOoo00o . getText ( ) )
  IIII ( II111iiii % OOoO00o )
 except : pass
 if 48 - 48: ii1IiI1i . iIiI - OOooOOo % iiI1i1 / O00o0o0000o0o . O00o0o0000o0o
def i1Ii ( url ) :
 I111I11 = O0O00Ooo ( url )
 Oo0oO0oo0oO00 = i111I ( I111I11 )
 OOoooooO = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( Oo0oO0oo0oO00 )
 for i1iIIIiI1I in OOoooooO :
  OOoO000O0OO = [ ]
  if not any ( x in i1iIIIiI1I for x in OOoO000O0OO ) :
   ii11i ( i1iIIIiI1I , I111I11 . encode ( "utf-8" ) , 'episodes' , "" )
   if 23 - 23: i11iIiiIii + o0
def oOo ( url , name ) :
 Oo0oO0oo0oO00 = i111I ( url )
 oOoOoO = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % urllib2 . unquote ( name ) ) . findall ( Oo0oO0oo0oO00 )
 ii1IOooO0 = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( oOoOoO [ 0 ] )
 if ( "episode_bg_2" in oOoOoO [ 0 ] ) :
  II11iiii1Ii = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( oOoOoO [ 0 ] )
  OO0oOoo ( "Part - " + II11iiii1Ii [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , url , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 for O0o0Oo , Oo00OOOOO in ii1IOooO0 :
  OO0oOoo ( "Part - " + Oo00OOOOO . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf-8" ) , "http://www.xom02.com/web/" + O0o0Oo , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 85 - 85: i111IiI . oOo0oooo00o - ii1IiI1i % i111IiI % o0OoOoOO00
def O0O00Ooo ( url ) :
 OO0o00o = i111I ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( OO0o00o ) [ 0 ]
 if 89 - 89: Ii11111i + i1
def Ii1I ( url , name ) :
 Oo0oO0oo0oO00 = i111I ( url )
 if ( "proxy.link" in Oo0oO0oo0oO00 ) :
  Oo0o0 = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( Oo0oO0oo0oO00 )
  Oo0oO0oo0oO00 = i111I ( Oo0o0 [ 0 ] )
  if 49 - 49: Ii11111i % O00o0o0000o0o + iIiiiI1IiI1I1 . o0 % IiiIII111iI
 Oo0o0 = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( Oo0oO0oo0oO00 )
 I1i1iii = xbmcgui . ListItem ( name )
 I1i1iii . setProperty ( "IsPlayable" , "true" )
 I1i1iii . setPath ( Oo0o0 [ 0 ] )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1i1iii )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I1i1iii )
 if 20 - 20: I11iIi1I
def i111I ( url ) :
 oO00 = urllib2 . Request ( url )
 oO00 . add_header ( 'Host' , 'phim.xixam.com' )
 oO00 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 oO00 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 ooo = urllib2 . urlopen ( oO00 )
 Oo0oO0oo0oO00 = ooo . read ( )
 ooo . close ( )
 Oo0oO0oo0oO00 = '' . join ( Oo0oO0oo0oO00 . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\n' , '' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\t' , '' )
 Oo0oO0oo0oO00 = re . sub ( '  +' , ' ' , Oo0oO0oo0oO00 )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '> <' , '><' )
 return Oo0oO0oo0oO00
 if 18 - 18: I11iIi1I
def OO0oOoo ( name , url , mode , iconimage , mirrorname ) :
 I1i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 i1IiIiiI = True
 I1I = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 I1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I1I . setProperty ( "IsPlayable" , "true" )
 i1IiIiiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i1I1II , listitem = I1I )
 return i1IiIiiI
 if 80 - 80: OOooOOo - ii1IiI1i
def ii11i ( name , url , mode , iconimage ) :
 I1i1I1II = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1IiIiiI = True
 I1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1IiIiiI = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1i1I1II , listitem = I1I , isFolder = True )
 return i1IiIiiI
 if 87 - 87: Ii11111i / oO0o - iIiiiI1IiI1I1 * iiI1i1 / iIiI . iiI
def iii11I111 ( k , e ) :
 OOOO00ooo0Ooo = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for OOOooOooo00O0 in range ( len ( e ) ) :
  Oo0OO = k [ OOOooOooo00O0 % len ( k ) ]
  oOOoOo00o = chr ( ( 256 + ord ( e [ OOOooOooo00O0 ] ) - ord ( Oo0OO ) ) % 256 )
  OOOO00ooo0Ooo . append ( oOOoOo00o )
 return "" . join ( OOOO00ooo0Ooo )
 if 70 - 70: oOo0oooo00o * IiiIII111iI
def i1II1 ( parameters ) :
 OoO0O0 = { }
 if 21 - 21: ii1IiI1i * ii1I % Ii11111i * iIiiiI1IiI1I1
 if parameters :
  Ii11Ii1I = parameters [ 1 : ] . split ( "&" )
  for O00oO in Ii11Ii1I :
   I11i1I1I = O00oO . split ( '=' )
   if ( len ( I11i1I1I ) ) == 2 :
    OoO0O0 [ I11i1I1I [ 0 ] ] = I11i1I1I [ 1 ]
 return OoO0O0
 if 83 - 83: IiiIII111iI / i111IiI
iIIIIii1 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 58 - 58: i11iIiiIii % oO0o
if os . path . exists ( iIIIIii1 ) == False :
 os . mkdir ( iIIIIii1 )
OO00Oo = os . path . join ( iIIIIii1 , 'visitor' )
if 51 - 51: I1i1i1ii * I11iIi1I + oO0o + ii1IiI1i
if os . path . exists ( OO00Oo ) == False :
 from random import randint
 o0O0O00 = open ( OO00Oo , "w" )
 o0O0O00 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 o0O0O00 . close ( )
 if 86 - 86: oO0o / I1i1i1ii % i11iIiiIii
def I11IiI1I11i1i ( utm_url ) :
 iI1ii1Ii = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  oO00 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : iI1ii1Ii }
 )
  ooo = urllib2 . urlopen ( oO00 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return ooo
 if 92 - 92: OOooOOo
def i1OOO ( group , name ) :
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
  Oo0oOOo = "1.0"
  Oo0OoO00oOO0o = open ( OO00Oo ) . read ( )
  OOO00O = "XomGiaiTri"
  OOoOO0oo0ooO = "UA-52209804-2"
  O0o0O00Oo0o0 = "www.viettv24.com"
  O00O0oOO00O00 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1Oo00 = O00O0oOO00O00 + "?" + "utmwv=" + Oo0oOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOO00O ) + "&utmac=" + OOoOO0oo0ooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0OoO00oOO0o , "1" , "1" , "2" ] )
   if 31 - 31: IIIII . OOooOOo / iiI
   if 89 - 89: OOooOOo
   if 68 - 68: ii1IiI1i * iIiI % iiI + ii1IiI1i + i111IiI
   if 4 - 4: i111IiI + iiI * iiI1i1
   if 55 - 55: i1 + ii1I / OOooOOo * Ii11111i - i11iIiiIii - O00o0o0000o0o
  else :
   if group == "None" :
    i1Oo00 = O00O0oOO00O00 + "?" + "utmwv=" + Oo0oOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOO00O + "/" + name ) + "&utmac=" + OOoOO0oo0ooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0OoO00oOO0o , "1" , "1" , "2" ] )
    if 25 - 25: IiiIII111iI
    if 7 - 7: iIiiiI1IiI1I1 / o0 * IIIII . I1i1i1ii . ii1I
    if 13 - 13: iiI1i1 / i11iIiiIii
    if 2 - 2: o0 / iiI / I11iIi1I % OOooOOo % O00o0o0000o0o
    if 52 - 52: I11iIi1I
   else :
    i1Oo00 = O00O0oOO00O00 + "?" + "utmwv=" + Oo0oOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOO00O + "/" + group + "/" + name ) + "&utmac=" + OOoOO0oo0ooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0OoO00oOO0o , "1" , "1" , "2" ] )
    if 95 - 95: O00o0o0000o0o
    if 87 - 87: i111IiI + OOooOOo . iiI1i1 + OOooOOo
    if 91 - 91: iiI
    if 61 - 61: o0OoOoOO00
    if 64 - 64: i111IiI / OOooOOo - iiI - oO0o
    if 86 - 86: oO0o % OOooOOo / o0 / OOooOOo
  print "============================ POSTING ANALYTICS ============================"
  I11IiI1I11i1i ( i1Oo00 )
  if 42 - 42: ii1IiI1i
  if not group == "None" :
   o0o = O00O0oOO00O00 + "?" + "utmwv=" + Oo0oOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O0o0O00Oo0o0 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + OOO00O + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( OOO00O ) + "&utmac=" + OOoOO0oo0ooO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , Oo0OoO00oOO0o , "1" , "2" ] )
   if 84 - 84: iiI
   if 74 - 74: IiiIII111iI - o0 - i1 . O00o0o0000o0o - I1i1i1ii
   if 73 - 73: i1 - iIiiiI1IiI1I1 - iIiiiI1IiI1I1 - oOo0oooo00o . O00o0o0000o0o + IiiIII111iI
   if 81 - 81: oOo0oooo00o * Ii11111i - IIIII . o0OoOoOO00 % oO0o / o0
   if 34 - 34: I1i1i1ii
   if 57 - 57: Ii11111i . oO0o . iIiiiI1IiI1I1
   if 42 - 42: oO0o + IiiIII111iI % iiI
   if 6 - 6: Ii11111i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    I11IiI1I11i1i ( o0o )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 68 - 68: OOooOOo - ii1IiI1i
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 28 - 28: ii1IiI1i . iiI1i1 / iiI1i1 + i1 . IiiIII111iI
iiii = i1II1 ( sys . argv [ 2 ] )
II1I = iiii . get ( 'mode' )
II111iiii = iiii . get ( 'url' )
O0 = iiii . get ( 'name' )
if type ( II111iiii ) == type ( str ( ) ) :
 II111iiii = urllib . unquote_plus ( II111iiii )
if type ( O0 ) == type ( str ( ) ) :
 O0 = urllib . unquote_plus ( O0 )
 if 5 - 5: IIIII
O0Oooo0O = str ( sys . argv [ 1 ] )
if II1I == 'index' :
 i1OOO ( "Browse" , O0 )
 IIII ( II111iiii )
elif II1I == 'search' :
 i1OOO ( "None" , "Search" )
 I1 ( )
elif II1I == 'videosbyregion' :
 i1OOO ( "Browse" , O0 )
 IiII ( )
elif II1I == 'videosbycategory' :
 i1OOO ( "Browse" , O0 )
 i1I1ii1II1iII ( )
elif II1I == 'mirrors' :
 i1OOO ( "Browse" , O0 )
 i1Ii ( II111iiii )
elif II1I == 'episodes' :
 i1OOO ( "Browse" , O0 )
 oOo ( II111iiii , O0 )
elif II1I == 'loadvideo' :
 i1OOO ( "Play" , O0 + "/" + II111iiii )
 O0o = xbmcgui . DialogProgress ( )
 O0o . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 Ii1I ( II111iiii , O0 )
 O0o . close ( )
 del O0o
else :
 i1OOO ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( O0Oooo0O ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
