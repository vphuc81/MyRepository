#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
from operator import itemgetter
oo000 = Plugin ( ) 
ii = "plugin://plugin.video.anhtrang.org"
oOOo = 24
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: oO00oOo = xbmc . translatePath ( os . path . join ( oO00oOo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/anhtrang.jpg' , oO00oOo )
 if 49 - 49: OOOo0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , oO00oOo )
 if 49 - 49: Oooo000o = xbmcgui . WindowDialog ( )
 if 49 - 49: Oooo000o . addControl ( OOOo0 )
 if 49 - 49: Oooo000o . doModal ( )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/danh-sach/new/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim HD' , 'path' : '%s/hd/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/danh-sach/phim-hd/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
 return oo000 . finish ( IiII )
 if 28 - 28: Ii11111i * iiI1i1
@ oo000 . route ( '/latest/<murl>/<page>' )
def i1I1ii1II1iII ( murl , page ) :
 I11i11Ii ( "Browse" , '/latest/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'latest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 53 - 53: o0oo0o / Oo + OOo00O0Oo0oO / iIi * ooO00oOoo - O0OOo
@ oo000 . route ( '/hd/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/hd/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'hd' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/genres' )
def O0 ( ) :
 I11i11Ii ( "Browse" , '/genres/' )
 IiII = [
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hai-huoc-1/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hanh-dong-2/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/vo-thuat-8/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/vien-tuong-3/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý - Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/tam-ly-tinh-cam-4/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/kinh-di-5/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hoat-hinh-6/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/chien-tranh-13/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao - Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/the-thao-am-nhac-12/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hinh-su-15/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/phieu-luu-14/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/co-trang-16/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tư Liệu - Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/tu-lieu-lich-su-11/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài kịch - Clip hài' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/hai-kich-clip-hai-10/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Điển' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/kinh-dien-7/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Sân Khấu - Cải Lương' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/the-loai/san-khau-cai-luong-9/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 34 - 34: ooO00oOoo % i1 % iiiIIii1IIi % ooO00oOoo * iIi / o0O
@ oo000 . route ( '/genres/<murl>/<page>' )
def Iiii ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 87 - 87: iiI1i1 / OOo000 + O0OOo - OOo000 . OOo000 / i1
@ oo000 . route ( '/nations' )
def iiIIIIi1i1 ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 IiII = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/viet-nam-3/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/trung-quoc-4/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/han-quoc-5/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/nhat-ban-6/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/my-chau-au-7/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/chau-a-8/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim.anhtrang.org/quoc-gia/an-do-9/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 54 - 54: o0oo0o % OO0OO0O0O0 + ii1IiI1i - iIi / Oo
@ oo000 . route ( '/nations/<murl>/<page>' )
def iIiiI1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 68 - 68: ii1IiI1i - Oo0Ooo - I11i / o0oo0o - I11i + I1IiiI
@ oo000 . route ( '/search/' )
def IiiIII111ii ( ) :
 I11i11Ii ( "Browse" , '/search/' )
 i1iIIi1 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if i1iIIi1 :
  ii11iIi1I = "http://phim.anhtrang.org/tim-kiem/keyword/1/trang-%s.html" . replace ( "keyword" , i1iIIi1 ) . replace ( " " , "-" )
  iI111I11I1I1 = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( ii11iIi1I ) , 1 )
  oo000 . redirect ( iI111I11I1I1 )
  if 55 - 55: o0O % I1IiiI / OOo00O0Oo0oO - iiI1i1 - OO0OO0O0O0 / i1
@ oo000 . route ( '/search/<murl>/<page>' )
def iii11iII ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 42 - 42: O0OOo + Ii11111i
@ oo000 . route ( '/mirrors/<murl>' )
def OOoO000O0OO ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 IiII = [ ]
 for iiI1IiI in II ( murl ) :
  ooOoOoo0O = { }
  ooOoOoo0O [ "label" ] = iiI1IiI [ "name" ] . strip ( ": " )
  ooOoOoo0O [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( iiI1IiI [ "eps" ] ) )
  IiII . append ( ooOoOoo0O )
 return oo000 . finish ( IiII )
 if 76 - 76: OO0OO0O0O0 / IiiIII111iI . ii1IiI1i * OOo00O0Oo0oO - o0oo0o
@ oo000 . route ( '/eps/<eps_list>' )
def Oooo ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps/' )
 O00o = O00 ( eps_list )
 i11I1 = re . compile ( '&file=/xml.php\?id=(\d+)' ) . findall ( O00o ) [ 0 ]
 O00o = O00 ( "http://phim.anhtrang.org/xml.php?id=%s" % i11I1 )
 Ii11Ii11I = re . compile ( "<item><title>(.+?)</title>" ) . findall ( O00o ) [ 0 ]
 IiII = [ ]
 for iI11i1I1 in re . compile ( '<item>(.+?)</item>' ) . findall ( O00o ) :
  o0o0OOO0o0 = re . compile ( "(\w+)-\w+.html" ) . findall ( iI11i1I1 ) [ 0 ]
  ooOoOoo0O = { }
  if o0o0OOO0o0 . isdigit ( ) :
   ooOoOoo0O [ "label" ] = "Part %03d - %s" % ( int ( o0o0OOO0o0 ) , Ii11Ii11I )
  else :
   ooOOOo0oo0O0 = re . split ( "(\d+)" , o0o0OOO0o0 . strip ( ) )
   if len ( ooOOOo0oo0O0 ) > 1 :
    ooOoOoo0O [ "label" ] = "Part %03d%s - %s" % ( int ( ooOOOo0oo0O0 [ 1 ] ) , ooOOOo0oo0O0 [ 2 ] , Ii11Ii11I )
   else :
    ooOoOoo0O [ "label" ] = "Part %s - %s" % ( ooOOOo0oo0O0 [ 0 ] , Ii11Ii11I )
    if 71 - 71: O0OOo . OO0OO0O0O0
  ooOoOoo0O [ "is_playable" ] = True
  iI111I11I1I1 = re . compile ( "<jwplayer:[h]*[d]*[.]*file\d*>(.+?)</jwplayer:[h]*[d]*[.]*file\d*>" ) . findall ( iI11i1I1 )
  if oo000 . get_setting ( 'HQ' , bool ) :
   ooOoOoo0O [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( iI111I11I1I1 [ - 1 ] ) )
  else :
   ooOoOoo0O [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( iI111I11I1I1 [ 0 ] ) )
  IiII . append ( ooOoOoo0O )
 IiII = sorted ( IiII , key = itemgetter ( 'label' ) )
 return oo000 . finish ( IiII )
 if 73 - 73: o0oo0o % o0O - OOo00O0Oo0oO
@ oo000 . route ( '/play/<url>' )
def iiIIII1i1i ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 iiI1 = xbmcgui . DialogProgress ( )
 iiI1 . create ( 'AnhTrang.org' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( i11Iiii ( url ) )
 iiI1 . close ( )
 del iiI1
 if 23 - 23: IiiIII111iI . i1
def i11Iiii ( url ) :
 if "youtube" in url :
  i11I1 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  Oo0O0OOOoo = i11I1 [ 0 ] [ len ( i11I1 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % Oo0O0OOOoo
 if "picasa" in url :
  return url
  if 95 - 95: I11i % iiI1i1 . OO0OO0O0O0
def oooO0oo0oOOOO ( url , page , route_name ) :
 I1i1I = int ( page ) + 1
 O00o = O00 ( url % page )
 i11I1 = re . compile ( '<div class="poster">(.*?)<a href="(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/>' ) . findall ( O00o )
 IiII = [ ]
 for oOO00oOO , OoOo , Ii11Ii11I , iI in i11I1 :
  ooOoOoo0O = { }
  ooOoOoo0O [ "label" ] = "%s (%s)" % ( Ii11Ii11I , oOO00oOO . replace ( '<span class="process"><span>' , "" ) . replace ( "</span></span>" , "" ) )
  ooOoOoo0O [ "thumbnail" ] = iI . replace ( "http://" , "https://" )
  ooOoOoo0O [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( OoOo ) )
  IiII . append ( ooOoOoo0O )
 if len ( IiII ) == oOOo :
  IiII . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , I1i1I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return IiII
 if 60 - 60: Oo / Oo
def II ( murl ) :
 O00o = O00 ( murl )
 i11I1 = re . compile ( '<p><a href="(.+?)" class="watch_now">XEM PHIM</a>' ) . findall ( O00o )
 O00o = O00 ( i11I1 [ 0 ] )
 i11I1 = re . compile ( '<tr class="listserver"><td valign="top" class="name">(.+?)</td>(.+?)</tr>' ) . findall ( O00o )
 I1II1III11iii = [ ]
 for Oo000 , oo in i11I1 :
  ii11I = re . compile ( '<a href="(.+?)">' ) . findall ( oo ) [ 0 ]
  iiI1IiI = { }
  iiI1IiI [ "name" ] = Oo000
  iiI1IiI [ "eps" ] = ii11I
  I1II1III11iii . append ( iiI1IiI )
 return I1II1III11iii
 if 96 - 96: i1 % OOo00O0Oo0oO . o0oo0o + iII111iiiii11 * iiI1i1 - o0O
@ oo000 . cached ( TTL = 60 )
def O00 ( url ) :
 i11i1 = urllib2 . Request ( url )
 i11i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 i11i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 i11i1 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 IIIii1II1II = urllib2 . urlopen ( i11i1 )
 i1I1iI = IIIii1II1II . read ( )
 IIIii1II1II . close ( )
 if "gzip" in IIIii1II1II . info ( ) . getheader ( 'Content-Encoding' ) :
  i1I1iI = zlib . decompress ( i1I1iI , 16 + zlib . MAX_WBITS )
 i1I1iI = '' . join ( i1I1iI . splitlines ( ) ) . replace ( '\'' , '"' )
 i1I1iI = i1I1iI . replace ( '\n' , '' )
 i1I1iI = i1I1iI . replace ( '\t' , '' )
 i1I1iI = re . sub ( '  +' , ' ' , i1I1iI )
 i1I1iI = i1I1iI . replace ( '> <' , '><' )
 return i1I1iI
 if 93 - 93: iiiIIii1IIi % iiI1i1 * I1IiiI
Ii11Ii1I = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.anhtrang.org' ) . getAddonInfo ( 'profile' ) )
if 72 - 72: iIi / I1IiiI * OOooOOo - O0OOo
if os . path . exists ( Ii11Ii1I ) == False :
 os . mkdir ( Ii11Ii1I )
Oo0O0O0ooO0O = os . path . join ( Ii11Ii1I , 'visitor' )
if 15 - 15: Ii11111i + o0O - iII111iiiii11 / o0oo0o
if os . path . exists ( Oo0O0O0ooO0O ) == False :
 from random import randint
 oo000OO00Oo = open ( Oo0O0O0ooO0O , "w" )
 oo000OO00Oo . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oo000OO00Oo . close ( )
 if 51 - 51: ooO00oOoo * IiiIII111iI + Oo + I11i
def o0O0O00 ( utm_url ) :
 o000o = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i11i1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : o000o }
 )
  IIIii1II1II = urllib2 . urlopen ( i11i1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return IIIii1II1II
 if 7 - 7: OOo000 * I11i % iiI1i1 . ooO00oOoo
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
  Ii1iIiII1ii1 = "1.0"
  ooOooo000oOO = open ( Oo0O0O0ooO0O ) . read ( )
  Oo0oOOo = "AnhTrang.org"
  Oo0OoO00oOO0o = "UA-52209804-2"
  OOO00O = "www.viettv24.com"
  OOoOO0oo0ooO = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   O0o0O00Oo0o0 = OOoOO0oo0ooO + "?" + "utmwv=" + Ii1iIiII1ii1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0oOOo ) + "&utmac=" + Oo0OoO00oOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooOooo000oOO , "1" , "1" , "2" ] )
   if 87 - 87: OOo000 * OOooOOo % Oo0Ooo % o0O - o0oo0o
   if 68 - 68: O0OOo % I1IiiI . ooO00oOoo . Ii11111i
   if 92 - 92: iIi . O0OOo
   if 31 - 31: O0OOo . o0O / OO0OO0O0O0
   if 89 - 89: o0O
  else :
   if group == "None" :
    O0o0O00Oo0o0 = OOoOO0oo0ooO + "?" + "utmwv=" + Ii1iIiII1ii1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0oOOo + "/" + name ) + "&utmac=" + Oo0OoO00oOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooOooo000oOO , "1" , "1" , "2" ] )
    if 68 - 68: I11i * iII111iiiii11 % OO0OO0O0O0 + I11i + OOo000
    if 4 - 4: OOo000 + OO0OO0O0O0 * o0oo0o
    if 55 - 55: OOooOOo + iiiIIii1IIi / o0O * iiI1i1 - Oo0Ooo - OOo00O0Oo0oO
    if 25 - 25: Ii11111i
    if 7 - 7: I1IiiI / ii1IiI1i * O0OOo . ooO00oOoo . iiiIIii1IIi
   else :
    O0o0O00Oo0o0 = OOoOO0oo0ooO + "?" + "utmwv=" + Ii1iIiII1ii1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0oOOo + "/" + group + "/" + name ) + "&utmac=" + Oo0OoO00oOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooOooo000oOO , "1" , "1" , "2" ] )
    if 13 - 13: o0oo0o / Oo0Ooo
    if 2 - 2: ii1IiI1i / OO0OO0O0O0 / IiiIII111iI % o0O % OOo00O0Oo0oO
    if 52 - 52: IiiIII111iI
    if 95 - 95: OOo00O0Oo0oO
    if 87 - 87: OOo000 + o0O . o0oo0o + o0O
    if 91 - 91: OO0OO0O0O0
  print "============================ POSTING ANALYTICS ============================"
  o0O0O00 ( O0o0O00Oo0o0 )
  if 61 - 61: i1
  if not group == "None" :
   O0OOO = OOoOO0oo0ooO + "?" + "utmwv=" + Ii1iIiII1ii1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( OOO00O ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + Oo0oOOo + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( Oo0oOOo ) + "&utmac=" + Oo0OoO00oOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , ooOooo000oOO , "1" , "2" ] )
   if 10 - 10: o0oo0o * Oo % o0O / ii1IiI1i / o0O
   if 42 - 42: I11i
   if 67 - 67: O0OOo . iIi . OO0OO0O0O0
   if 10 - 10: Ii11111i % Ii11111i - iiiIIii1IIi / o0oo0o + OOo00O0Oo0oO
   if 87 - 87: iiI1i1 * Ii11111i + o0oo0o / iiiIIii1IIi / iIi
   if 37 - 37: iIi - OOo000 * iiI1i1 % Oo0Ooo - O0OOo
   if 83 - 83: Oo / ii1IiI1i
   if 34 - 34: ooO00oOoo
   try :
    print "============================ POSTING TRACK EVENT ============================"
    o0O0O00 ( O0OOO )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 57 - 57: iiI1i1 . Oo . I1IiiI
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 42 - 42: Oo + Ii11111i % OO0OO0O0O0
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
