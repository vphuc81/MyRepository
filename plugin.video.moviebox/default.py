#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , ast , os , uuid , json
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.moviebox"
oOOo = 32
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: oO00oOo = xbmc . translatePath ( os . path . join ( oO00oOo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/moviebox.jpg' , oO00oOo )
 if 49 - 49: OOOo0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , oO00oOo )
 if 49 - 49: Oooo000o = xbmcgui . WindowDialog ( )
 if 49 - 49: Oooo000o . addControl ( OOOo0 )
 if 49 - 49: Oooo000o . doModal ( )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilm' ) ) } ,
 { 'label' : 'Phóng Sự & Tài Liệu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '33' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/13333734-Phim-Tai-Lieu.jpg' } ,
 { 'label' : 'Ca Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '34' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/99844308-Ca-nhac.jpg' } ,
 { 'label' : 'Hài Kịch' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '35' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/519820-Hai-Kich.jpg' } ,
 { 'label' : 'Phim Lẻ' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '36' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/6855131-MOD.jpg' } ,
 { 'label' : 'Phim Bộ' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '37' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/46252803-Phim-Bo.jpg' } ,
 { 'label' : 'Truyền Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '38' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/14266234-Live-TV.jpg' } ,
 { 'label' : 'Nghe Truyện Đọc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '40' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/3488938-Sach-Noi.jpg' } ,
 { 'label' : 'Dạy Nấu Ăn' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetListFilmByCate' ) , '41' ) , 'thumbnail' : 'http://ictvnow.nl/vod/images/category/14376243-Am-Nhac.jpg' }
 ]
 return oo000 . finish ( IiII )
 if 28 - 28: Ii11111i * iiI1i1
@ oo000 . route ( '/latest/<murl>' )
def i1I1ii1II1iII ( murl ) :
 I11i11Ii ( "Browse" , '/latest/%s' % murl )
 IiII = oooO0oo0oOOOO ( murl , '' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 53 - 53: o0oo0o / Oo + OOo00O0Oo0oO / iIi * ooO00oOoo - O0OOo
@ oo000 . route ( '/genres/<murl>/<mid>' )
def II1Iiii1111i ( murl , mid ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , mid ) )
 IiII = oooO0oo0oOOOO ( murl , mid )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/mirrors/<murl>/<mid>' )
def O0 ( murl , mid ) :
 I11i11Ii ( "Browse" , '/mirrors/%s/%s' % ( murl , mid ) )
 IiII = [ ]
 for I11i1i11i1I in Iiii ( murl , mid ) :
  OOO0O = { }
  OOO0O [ "label" ] = I11i1i11i1I [ "name" ] . strip ( )
  oo0ooO0oOOOOo = str ( uuid . uuid1 ( ) )
  oO000OoOoo00o = oo000 . get_storage ( oo0ooO0oOOOOo )
  oO000OoOoo00o [ "list" ] = I11i1i11i1I [ "eps" ]
  OOO0O [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( oo0ooO0oOOOOo ) )
  IiII . append ( OOO0O )
 return oo000 . finish ( IiII )
 if 31 - 31: i1 + I11i . O0OOo
@ oo000 . route ( '/eps/<eps_list>' )
def OoOooOOOO ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 IiII = [ ]
 for i11iiII in oo000 . get_storage ( eps_list ) [ "list" ] :
  OOO0O = { }
  OOO0O [ "label" ] = i11iiII [ "name" ] . strip ( )
  OOO0O [ "is_playable" ] = True
  OOO0O [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( i11iiII [ "url" ] ) )
  IiII . append ( OOO0O )
 return oo000 . finish ( IiII )
 if 34 - 34: o0oo0o % iII111iiiii11 / I1IiiI . iIi + OO0OO0O0O0
@ oo000 . route ( '/play/<mid>' )
def I1Ii ( mid ) :
 I11i11Ii ( "Play" , '/play/%s' % ( mid ) )
 o0oOo0Ooo0O = xbmcgui . DialogProgress ( )
 o0oOo0Ooo0O . create ( 'MovieBox' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( OO00O0O0O00Oo ( mid ) )
 o0oOo0Ooo0O . close ( )
 del o0oOo0Ooo0O
 if 25 - 25: IiiIII111iI % i1 - i1 . i1
def OO00O0O0O00Oo ( mid ) :
 Ii1 = oOOoO0 ( "http://ictvnow.nl/vod/Api/GetLinkByEpiId" , mid )
 O0OoO000O0OO = json . loads ( Ii1 ) [ "link" ] [ 0 ] [ "url" ]
 iiI1IiI = O0OoO000O0OO
 if "youtube" in O0OoO000O0OO :
  II = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( O0OoO000O0OO )
  ooOoOoo0O = II [ 0 ] [ len ( II [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/play/?video_id=%s' % ooOoOoo0O
 if "picasa" in O0OoO000O0OO :
  OooO0 = re . compile ( 'authkey=(.+?)#' ) . findall ( O0OoO000O0OO )
  II11iiii1Ii = re . compile ( 'https://picasaweb.google.com/(\d+)/' ) . findall ( O0OoO000O0OO )
  OO0o = re . compile ( '#(\d+)' ) . findall ( O0OoO000O0OO )
  Ooo = 480
  if oo000 . get_setting ( 'HQ' , bool ) :
   Ooo = 720
  if ( II11iiii1Ii and OO0o ) :
   O0o0Oo = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?alt=json%s" % ( II11iiii1Ii [ 0 ] , OO0o [ 0 ] , "" if not OooO0 else "&authkey=" + OooO0 [ 0 ] )
   Ii1 = urllib2 . urlopen ( O0o0Oo ) . read ( )
   Oo00OOOOO = json . loads ( Ii1 ) [ "feed" ] [ "media$group" ] [ "media$content" ]
   for O0O in Oo00OOOOO :
    if ( O0O [ "type" ] == "video/mpeg4" ) and ( int ( O0O [ "height" ] ) <= Ooo ) :
     iiI1IiI = O0O [ "url" ]
  else :
   Ii1 = urllib2 . urlopen ( O0OoO000O0OO ) . read ( )
   O0o0Oo = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( Ii1 ) [ 0 ]
   Ii1 = urllib2 . urlopen ( O0o0Oo ) . read ( )
   Oo00OOOOO = json . loads ( Ii1 ) [ "feed" ] [ "media" ] [ "content" ]
   for O0O in Oo00OOOOO :
    if ( O0O [ "type" ] == "video/mpeg4" ) and ( int ( O0O [ "height" ] ) <= Ooo ) :
     iiI1IiI = O0O [ "url" ]
 return iiI1IiI
 if 83 - 83: Oo + i1 * IiiIII111iI % I11i + Oo
def oooO0oo0oOOOO ( url , mid ) :
 Ii1 = oOOoO0 ( url , mid )
 IiII = [ ]
 for Ii1iIIIi1ii in json . loads ( Ii1 ) [ "film" ] :
  OOO0O = { }
  OOO0O [ "label" ] = Ii1iIIIi1ii [ "title_en" ]
  OOO0O [ "thumbnail" ] = Ii1iIIIi1ii [ "cover_image" ] if ( "://" in Ii1iIIIi1ii [ "cover_image" ] ) else "http://ictvnow.nl" + urllib . quote ( Ii1iIIIi1ii [ "cover_image" ] . encode ( "utf8" ) )
  OOO0O [ "path" ] = '%s/%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( 'http://ictvnow.nl/vod/Api/GetEpiByFilmId' ) , Ii1iIIIi1ii [ "ID" ] . strip ( ) )
  IiII . append ( OOO0O )
 return IiII
 if 80 - 80: Oo * Oo0Ooo / O0OOo
def Iiii ( murl , mid ) :
 Ii1 = oOOoO0 ( murl , mid )
 I11II1i = [ ]
 for IIIII in json . loads ( Ii1 ) [ "server" ] :
  ooooooO0oo = [ ]
  for IIiiiiiiIi1I1 in IIIII [ "data" ] :
   i11iiII = { }
   i11iiII [ "url" ] = IIiiiiiiIi1I1 [ "ID" ]
   i11iiII [ "name" ] = IIiiiiiiIi1I1 [ "name" ]
   ooooooO0oo . append ( i11iiII )
  I11i1i11i1I = { }
  I11i1i11i1I [ "name" ] = "%s - %s (%s tập)" % ( IIIII [ "alias" ] . encode ( "utf8" ) , IIIII [ "name" ] . encode ( "utf8" ) , IIIII [ "episode" ] )
  I11i1i11i1I [ "eps" ] = ooooooO0oo
  I11II1i . append ( I11i1i11i1I )
 return I11II1i
 if 13 - 13: ooO00oOoo + o0O - iII111iiiii11 + O0OOo . iIi + I11i
@ oo000 . cached ( TTL = 60 )
def oOOoO0 ( url , mid ) :
 Ii = urllib2 . Request ( url )
 Ii . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 oo0O0oOOO00oO = ""
 if mid != "" :
  if "GetListFilmByCate" in url :
   OooOooooOOoo0 = urllib . urlencode ( { 'cateid' : mid } )
  else :
   OooOooooOOoo0 = urllib . urlencode ( { 'id' : mid } )
  o00OO0OOO0 = urllib2 . urlopen ( Ii , data = OooOooooOOoo0 )
  oo0O0oOOO00oO = o00OO0OOO0 . read ( )
  o00OO0OOO0 . close ( )
  if "gzip" in o00OO0OOO0 . info ( ) . getheader ( 'Content-Encoding' ) :
   oo0O0oOOO00oO = zlib . decompress ( oo0O0oOOO00oO , 16 + zlib . MAX_WBITS )
  return oo0O0oOOO00oO
 else :
  o00OO0OOO0 = urllib2 . urlopen ( Ii )
  oo0O0oOOO00oO = o00OO0OOO0 . read ( )
  o00OO0OOO0 . close ( )
  if "gzip" in o00OO0OOO0 . info ( ) . getheader ( 'Content-Encoding' ) :
   oo0O0oOOO00oO = zlib . decompress ( oo0O0oOOO00oO , 16 + zlib . MAX_WBITS )
  return oo0O0oOOO00oO
  if 83 - 83: iII111iiiii11
Iii111II = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.moviebox' ) . getAddonInfo ( 'profile' ) )
if 9 - 9: I11i
if os . path . exists ( Iii111II ) == False :
 os . mkdir ( Iii111II )
i11 = os . path . join ( Iii111II , 'visitor' )
if 58 - 58: o0oo0o * Oo0Ooo / o0O % O0OOo - Ii11111i / iiI1i1
if os . path . exists ( i11 ) == False :
 from random import randint
 ii11i1 = open ( i11 , "w" )
 ii11i1 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 ii11i1 . close ( )
 if 29 - 29: Ii11111i % ii1IiI1i + OOo000 / IiiIII111iI + o0oo0o * IiiIII111iI
def i1I1iI ( utm_url ) :
 oo0OooOOo0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  Ii = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : oo0OooOOo0 }
 )
  o00OO0OOO0 = urllib2 . urlopen ( Ii ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return o00OO0OOO0
 if 92 - 92: iIi . Oo + IiiIII111iI
def I11i11Ii ( group , name ) :
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
  IiII1I11i1I1I = "1.0"
  oO0Oo = open ( i11 ) . read ( )
  oOOoo0Oo = "MovieBox"
  o00OO00OoO = "UA-52209804-2"
  OOOO0OOoO0O0 = "www.viettv24.com"
  O0Oo000ooO00 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oO0 = O0Oo000ooO00 + "?" + "utmwv=" + IiII1I11i1I1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoo0Oo ) + "&utmac=" + o00OO00OoO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oO0Oo , "1" , "1" , "2" ] )
   if 45 - 45: Oo0Ooo * i1 % iiiIIii1IIi + Ii11111i - OOo00O0Oo0oO
   if 17 - 17: ooO00oOoo
   if 62 - 62: iiiIIii1IIi * o0O
   if 26 - 26: iIi . O0OOo
   if 68 - 68: I11i
  else :
   if group == "None" :
    oO0 = O0Oo000ooO00 + "?" + "utmwv=" + IiII1I11i1I1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoo0Oo + "/" + name ) + "&utmac=" + o00OO00OoO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oO0Oo , "1" , "1" , "2" ] )
    if 35 - 35: I11i - iIi / OOooOOo / o0O
    if 24 - 24: OOo000 - OOo000 / i1 - Ii11111i
    if 69 - 69: iiI1i1 . O0OOo + OOo00O0Oo0oO / OOooOOo - iiI1i1
    if 63 - 63: o0oo0o % iiI1i1 * iiI1i1 * I11i / Ii11111i
    if 74 - 74: i1
   else :
    oO0 = O0Oo000ooO00 + "?" + "utmwv=" + IiII1I11i1I1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoo0Oo + "/" + group + "/" + name ) + "&utmac=" + o00OO00OoO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oO0Oo , "1" , "1" , "2" ] )
    if 75 - 75: IiiIII111iI . OOo000
    if 54 - 54: i1 % o0O % Oo % iiiIIii1IIi + iiiIIii1IIi * OOo000
    if 87 - 87: OOo000 * OOooOOo % Oo0Ooo % o0O - o0oo0o
    if 68 - 68: O0OOo % I1IiiI . ooO00oOoo . Ii11111i
    if 92 - 92: iIi . O0OOo
    if 31 - 31: O0OOo . o0O / OO0OO0O0O0
  print "============================ POSTING ANALYTICS ============================"
  i1I1iI ( oO0 )
  if 89 - 89: o0O
  if not group == "None" :
   OO0oOoOO0oOO0 = O0Oo000ooO00 + "?" + "utmwv=" + IiII1I11i1I1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( OOOO0OOoO0O0 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oOOoo0Oo + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oOOoo0Oo ) + "&utmac=" + o00OO00OoO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , oO0Oo , "1" , "2" ] )
   if 86 - 86: o0oo0o
   if 55 - 55: OOooOOo + iiiIIii1IIi / o0O * iiI1i1 - Oo0Ooo - OOo00O0Oo0oO
   if 25 - 25: Ii11111i
   if 7 - 7: I1IiiI / ii1IiI1i * O0OOo . ooO00oOoo . iiiIIii1IIi
   if 13 - 13: o0oo0o / Oo0Ooo
   if 2 - 2: ii1IiI1i / OO0OO0O0O0 / IiiIII111iI % o0O % OOo00O0Oo0oO
   if 52 - 52: IiiIII111iI
   if 95 - 95: OOo00O0Oo0oO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    i1I1iI ( OO0oOoOO0oOO0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 87 - 87: OOo000 + o0O . o0oo0o + o0O
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 91 - 91: OO0OO0O0O0
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
