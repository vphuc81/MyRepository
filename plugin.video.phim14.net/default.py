#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , ast , os , uuid
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.kodi4vn.phim14.net"
oOOo = 32
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: oO00oOo = xbmc . translatePath ( os . path . join ( oO00oOo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim14.jpg' , oO00oOo )
 if 49 - 49: OOOo0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , oO00oOo )
 if 49 - 49: Oooo000o = xbmcgui . WindowDialog ( )
 if 49 - 49: Oooo000o . addControl ( OOOo0 )
 if 49 - 49: Oooo000o . doModal ( )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
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
@ oo000 . route ( '/movies/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/series/<murl>/<page>' )
def O0 ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 34 - 34: ooO00oOoo % i1 % iiiIIii1IIi % ooO00oOoo * iIi / o0O
@ oo000 . route ( '/genres' )
def Iiii ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 IiII = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hanh-dong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-phieu-luu/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-kinh-di/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tinh-cam/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hoat-hinh/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-vo-thuat/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hai-huoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-hinh-su/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tam-ly/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-vien-tuong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-than-thoai/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-co-trang/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-chien-tranh/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-am-nhac/page-%s.html' ) , 1 ) } ,
 { 'label' : 'TV Show' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/the-loai/phim-tv-show/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 87 - 87: iiI1i1 / OOo000 + O0OOo - OOo000 . OOo000 / i1
@ oo000 . route ( '/genres/<murl>/<page>' )
def iiIIIIi1i1 ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 54 - 54: o0oo0o % OO0OO0O0O0 + ii1IiI1i - iIi / Oo
@ oo000 . route ( '/nations' )
def iIiiI1 ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 IiII = [
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-han-quoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-trung-quoc/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-dai-loan/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-viet-nam/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-my/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-nhat-ban/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-thai-lan/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hồng Kông' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-hong-kong/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Philippines' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-philippines/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-chau-au/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Nước Khác' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/quoc-gia/phim-nuoc-khac/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 68 - 68: ii1IiI1i - Oo0Ooo - I11i / o0oo0o - I11i + I1IiiI
@ oo000 . route ( '/nations/<murl>/<page>' )
def IiiIII111ii ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 3 - 3: iIi + OO0OO0O0O0
@ oo000 . route ( '/search/' )
def I1Ii ( ) :
 I11i11Ii ( "Browse" , '/search' )
 o0oOo0Ooo0O = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if o0oOo0Ooo0O :
  OO00O0O0O00Oo = "http://m.phim14.net/search/keyword/page-%s.html" . replace ( "keyword" , o0oOo0Ooo0O ) . replace ( " " , "-" )
  IIIiiiiiIii = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( OO00O0O0O00Oo ) , 1 )
  oo000 . redirect ( IIIiiiiiIii )
  if 70 - 70: I11i . I11i - I11i / Ii11111i * o0oo0o
@ oo000 . route ( '/search/<murl>/<page>' )
def OoO000 ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 42 - 42: iiI1i1 - I1IiiI / Oo0Ooo + o0oo0o + I11i
@ oo000 . route ( '/mirrors/<murl>' )
def iIiII ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 IiII = [ ]
 for iI in iI11iiiI1II ( murl ) :
  O0oooo0Oo00 = { }
  O0oooo0Oo00 [ "label" ] = iI [ "name" ] . strip ( )
  Ii11iii11I = str ( uuid . uuid1 ( ) )
  oOo00Oo00O = oo000 . get_storage ( Ii11iii11I )
  oOo00Oo00O [ "list" ] = iI [ "eps" ]
  O0oooo0Oo00 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( Ii11iii11I ) )
  IiII . append ( O0oooo0Oo00 )
 return oo000 . finish ( IiII )
 if 43 - 43: ii1IiI1i - iIi * iiiIIii1IIi
@ oo000 . route ( '/eps/<eps_list>' )
def O0O00o0OOO0 ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 IiII = [ ]
 for Ii1iIIIi1ii in oo000 . get_storage ( eps_list ) [ "list" ] :
  O0oooo0Oo00 = { }
  O0oooo0Oo00 [ "label" ] = Ii1iIIIi1ii [ "name" ] . strip ( )
  O0oooo0Oo00 [ "is_playable" ] = True
  O0oooo0Oo00 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( Ii1iIIIi1ii [ "url" ] ) )
  IiII . append ( O0oooo0Oo00 )
 return oo000 . finish ( IiII )
 if 80 - 80: Oo * Oo0Ooo / O0OOo
@ oo000 . route ( '/play/<url>' )
def I11II1i ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 IIIII = xbmcgui . DialogProgress ( )
 IIIII . create ( 'phim14.net' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( ooooooO0oo ( url ) )
 IIIII . close ( )
 del IIIII
 if 49 - 49: IiiIII111iI * iiiIIii1IIi / I1IiiI / Oo0Ooo / IiiIII111iI
def ooooooO0oo ( url ) :
 I1i1I1II = i1IiIiiI ( url )
 if "youtube" in I1i1I1II :
  I1I = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( I1i1I1II )
  oOO00oOO = I1I [ 0 ] [ len ( I1I [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % oOO00oOO
 if "http://m.phim14.net/grabvideo/" in I1i1I1II :
  OoOo = re . compile ( '"(http://m.phim14.net/grabvideo/.+?)"' ) . findall ( I1i1I1II ) [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   OoOo = OoOo . replace ( "/grabvideo/" , "/grabvideo720/" )
  return OoOo
  if 18 - 18: Oo0Ooo
def oooO0oo0oOOOO ( url , page , route_name ) :
 Ii11I = int ( page ) + 1
 I1i1I1II = i1IiIiiI ( url % page )
 I1I = re . compile ( '<a href="(http://m.phim14.net/phim/.+?)" class="content-items"><img src="(.+?)" alt="(.+?)"[^>]*><h3>.+?</h3><h4>.+?</h4><ul[^>]*><li>Năm phát hành: (.+?)</li><li>Thể loại: .+?</li></ul><p[^>]*>Trạng thái: (.*?)</p></a>' ) . findall ( I1i1I1II )
 IiII = [ ]
 for OOO0OOO00oo , Iii111II , iiii11I , Ooo0OO0oOO , ii11i1 in I1I :
  O0oooo0Oo00 = { }
  O0oooo0Oo00 [ "label" ] = "%s (%s)" % ( iiii11I , ii11i1 )
  O0oooo0Oo00 [ "thumbnail" ] = Iii111II
  O0oooo0Oo00 [ "info" ] = { "year" : Ooo0OO0oOO }
  O0oooo0Oo00 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( OOO0OOO00oo . replace ( "/phim/" , "/xem-phim/" ) ) )
  IiII . append ( O0oooo0Oo00 )
 if len ( IiII ) == oOOo :
  IiII . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , Ii11I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return IiII
 if 29 - 29: Ii11111i % ii1IiI1i + OOo000 / IiiIII111iI + o0oo0o * IiiIII111iI
def iI11iiiI1II ( murl ) :
 I1i1I1II = i1IiIiiI ( murl )
 I1I = re . compile ( '<span class="svname">(.+?)</span><span class="svep">(.+?)</span>' ) . findall ( I1i1I1II )
 i1I1iI = re . compile ( '<title>(.+?)</title>' ) . findall ( I1i1I1II ) [ 0 ]
 oo0OooOOo0 = [ ]
 for o0OO00oO , I11i1I1I in I1I :
  oO0Oo = [ ]
  for oOOoo0Oo , o00OO00OoO in re . compile ( '<a[^>]*href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( I11i1I1I ) :
   Ii1iIIIi1ii = { }
   Ii1iIIIi1ii [ "url" ] = oOOoo0Oo
   Ii1iIIIi1ii [ "name" ] = "Part %s - %s" % ( o00OO00OoO , i1I1iI . split ( " | " ) [ 0 ] )
   oO0Oo . append ( Ii1iIIIi1ii )
  iI = { }
  iI [ "name" ] = o0OO00oO
  iI [ "eps" ] = oO0Oo
  oo0OooOOo0 . append ( iI )
 return oo0OooOOo0
 if 60 - 60: I11i * o0O - I11i % iII111iiiii11 - OOo000 + ii1IiI1i
@ oo000 . cached ( TTL = 60 )
def i1IiIiiI ( url ) :
 O00Oo000ooO0 = urllib2 . Request ( url )
 O00Oo000ooO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 O00Oo000ooO0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 O00Oo000ooO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 O00Oo000ooO0 . add_header ( 'Cookie' , 'location.href=1' )
 OoO0O00 = urllib2 . urlopen ( O00Oo000ooO0 )
 IIiII = OoO0O00 . read ( )
 OoO0O00 . close ( )
 if "gzip" in OoO0O00 . info ( ) . getheader ( 'Content-Encoding' ) :
  IIiII = zlib . decompress ( IIiII , 16 + zlib . MAX_WBITS )
 IIiII = '' . join ( IIiII . splitlines ( ) ) . replace ( '\'' , '"' )
 IIiII = IIiII . replace ( '\n' , '' )
 IIiII = IIiII . replace ( '\t' , '' )
 IIiII = re . sub ( '  +' , ' ' , IIiII )
 IIiII = IIiII . replace ( '> <' , '><' )
 return IIiII
 if 80 - 80: ooO00oOoo . iiI1i1
IIi = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.phim14.net' ) . getAddonInfo ( 'profile' ) )
if 26 - 26: iIi
if os . path . exists ( IIi ) == False :
 os . mkdir ( IIi )
OOO = os . path . join ( IIi , 'visitor' )
if 59 - 59: i1 + iII111iiiii11 * o0O + I1IiiI
if os . path . exists ( OOO ) == False :
 from random import randint
 Oo0OoO00oOO0o = open ( OOO , "w" )
 Oo0OoO00oOO0o . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Oo0OoO00oOO0o . close ( )
 if 80 - 80: iiI1i1 + o0oo0o - o0oo0o % iIi
def OoOO0oo0o ( utm_url ) :
 II11i1I11Ii1i = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O00Oo000ooO0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : II11i1I11Ii1i }
 )
  OoO0O00 = urllib2 . urlopen ( O00Oo000ooO0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OoO0O00
 if 97 - 97: OOo000 % iIi * OOo00O0Oo0oO + IiiIII111iI . o0oo0o + o0oo0o
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
  Oooo0O0oo00oO = "1.0"
  IIi1i = open ( OOO ) . read ( )
  I1I1iIiII1 = "Phim14.net"
  i11i1I1 = "UA-52209804-2"
  ii1I = "www.viettv24.com"
  Oo0ooOo0o = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   Ii1i1 = Oo0ooOo0o + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
   if 15 - 15: i1
   if 18 - 18: Oo0Ooo . I1IiiI % iII111iiiii11 / OO0OO0O0O0
   if 75 - 75: o0O % IiiIII111iI % IiiIII111iI . O0OOo
   if 5 - 5: IiiIII111iI * OOo000 + o0O . o0oo0o + o0O
   if 91 - 91: OO0OO0O0O0
  else :
   if group == "None" :
    Ii1i1 = Oo0ooOo0o + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
    if 61 - 61: i1
    if 64 - 64: OOo000 / o0O - OO0OO0O0O0 - Oo
    if 86 - 86: Oo % o0O / ii1IiI1i / o0O
    if 42 - 42: I11i
    if 67 - 67: O0OOo . iIi . OO0OO0O0O0
   else :
    Ii1i1 = Oo0ooOo0o + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + group + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
    if 10 - 10: Ii11111i % Ii11111i - iiiIIii1IIi / o0oo0o + OOo00O0Oo0oO
    if 87 - 87: iiI1i1 * Ii11111i + o0oo0o / iiiIIii1IIi / iIi
    if 37 - 37: iIi - OOo000 * iiI1i1 % Oo0Ooo - O0OOo
    if 83 - 83: Oo / ii1IiI1i
    if 34 - 34: ooO00oOoo
    if 57 - 57: iiI1i1 . Oo . I1IiiI
  print "============================ POSTING ANALYTICS ============================"
  OoOO0oo0o ( Ii1i1 )
  if 42 - 42: Oo + Ii11111i % OO0OO0O0O0
  if not group == "None" :
   i1iIIIi1i = Oo0ooOo0o + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( ii1I ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + I1I1iIiII1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , IIi1i , "1" , "2" ] )
   if 43 - 43: o0O % o0oo0o
   if 5 - 5: Oo0Ooo - I1IiiI / iiiIIii1IIi
   if 26 - 26: Oo . iII111iiiii11
   if 39 - 39: iIi - OO0OO0O0O0 % Oo0Ooo * O0OOo . ooO00oOoo
   if 58 - 58: I11i % Oo0Ooo . iIi / iiI1i1
   if 84 - 84: iIi . Ii11111i / OOooOOo - ii1IiI1i / iII111iiiii11 / IiiIII111iI
   if 12 - 12: ii1IiI1i * iIi % I1IiiI % iiiIIii1IIi
   if 20 - 20: o0oo0o % OOo00O0Oo0oO / OOo00O0Oo0oO + OOo00O0Oo0oO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OoOO0oo0o ( i1iIIIi1i )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 45 - 45: iiI1i1 - ooO00oOoo - iII111iiiii11 - I11i . i1 / OO0OO0O0O0
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 51 - 51: OO0OO0O0O0 + iIi
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
