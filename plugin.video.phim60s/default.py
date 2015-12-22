#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , json , requests
from operator import itemgetter
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.phim60s"
oOOo = 33
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
def IIi1IiiiI1Ii ( s ) :
 s = '' . join ( s . splitlines ( ) ) . replace ( '\'' , '"' )
 s = s . replace ( '\n' , '' )
 s = s . replace ( '\t' , '' )
 s = re . sub ( '  +' , ' ' , s )
 s = s . replace ( '> <' , '><' )
 return s
 if 39 - 39: O0 - ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
@ oo000 . route ( '/' )
def Ii1I ( ) :
 IiiIII111iI ( "None" , "None" )
 IiII = ""
 iI1Ii11111iIi = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  i1i1II = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in i1i1II for b in iI1Ii11111iIi ) : break
 while True :
  O0oo0OO0 = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in O0oo0OO0 for b in iI1Ii11111iIi ) : break
 try :
  IiII = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   IiII = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , IiII . lower ( ) ) : break
 I1i1iiI1 = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( IiII , "11" , i1i1II , O0oo0OO0 ) ) . read ( )
 if "allowed" in I1i1iiI1 :
  iiIIIII1i1iI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( iiIIIII1i1iI , "temp.jpg" ) )
  '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim60s.jpg' , iiIIIII1i1iI )
  o0oO0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , iiIIIII1i1iI )
  oo00 = xbmcgui . WindowDialog ( )
  oo00 . addControl ( o0oO0 )
  oo00 . doModal ( )'''
  if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
  i1I1Iiii1111 = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-chieu-rap/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( i1I1Iiii1111 )
 else :
  iiIIIII1i1iI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  iiIIIII1i1iI = xbmc . translatePath ( os . path . join ( iiIIIII1i1iI , "temp.jpg" ) )
  '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim60s.jpg' , iiIIIII1i1iI )
  o0oO0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , iiIIIII1i1iI )
  oo00 = xbmcgui . WindowDialog ( )
  oo00 . addControl ( o0oO0 )
  oo00 . doModal ( )'''
  if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
  i1I1Iiii1111 = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-chieu-rap/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( i1I1Iiii1111 )
  if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
  if 26 - 26: O00OoOoo00 . iiiI11 / II1iI * iiiiIi11i / Oo0Ooo
@ oo000 . route ( '/latest/<murl>/<page>' )
def iIIIiI11 ( murl , page ) :
 IiiIII111iI ( "Browse" , '/latest/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'latest' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 3 - 3: I1i1i1ii + OO0OO0O0O0
@ oo000 . route ( '/hottest/<murl>/<page>' )
def I1Ii ( murl , page ) :
 IiiIII111iI ( "Browse" , '/hottest/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'hottest' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 66 - 66: oOo0oooo00o
@ oo000 . route ( '/movies/<murl>/<page>' )
def oo0Ooo0 ( murl , page ) :
 IiiIII111iI ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'movies' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 46 - 46: iiiI11 % iiiI11 - II1iI * iiiiIi11i % I1i1i1ii
@ oo000 . route ( '/series/<murl>/<page>' )
def OOooO0OOoo ( murl , page ) :
 IiiIII111iI ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'series' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 29 - 29: iiiiIi11i / iiiIIii1IIi
@ oo000 . route ( '/genres' )
def IiIIIiI1I1 ( ) :
 IiiIII111iI ( "Browse" , '/genres' )
 i1I1Iiii1111 = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-hanh-dong/1/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Giật Gân' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-giat-gan/24/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-vo-thuat/2/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-chien-tranh/3/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-hoat-hinh/5/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Gia Đình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-gia-dinh/15/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị & Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-kinh-di-ma/6/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Bí Ẩn' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-bi-an/23/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-hai-huoc/7/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-phieu-luu/9/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-vien-tuong/8/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-than-thoai/10/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-hinh-su/4/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-tam-ly/16/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-tinh-cam/17/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tài Liệu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-tai-lieu/20/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-lich-su/25/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tiểu Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-tieu-su/29/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tây' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-vien-tay/30/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-am-nhac/19/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-the-thao/18/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-co-trang/12/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Truyền Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/the-loai/phim-truyen-hinh/11/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( i1I1Iiii1111 )
 if 86 - 86: Oo0Ooo + oOo0oooo00o + iiiI11 * O00o0o0000o0o + iiiiIi11i
@ oo000 . route ( '/genres/<murl>/<page>' )
def oOoO ( murl , page = 1 ) :
 IiiIII111iI ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'genres' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 68 - 68: oOoO0oo0OOOo . II1iI . Oo0Ooo
@ oo000 . route ( '/nations' )
def II ( ) :
 IiiIII111iI ( "Browse" , '/nations' )
 i1I1Iiii1111 = [
 { 'label' : 'Phim Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-viet-nam/1/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-trung-quoc/4/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-han-quoc/2/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Hồng Kong' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-hong-kong/6/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-dai-loan/7/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-nhat-ban/3/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-an-do/10/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-thai-lan/11/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-chau-a/8/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/quoc-gia/phim-my-chau-au/5/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( i1I1Iiii1111 )
 if 14 - 14: oOo0O0Ooo . ooOO00oOo / oOo0oooo00o
@ oo000 . route ( '/nations/<murl>/<page>' )
def IiiiI1II1I1 ( murl , page ) :
 IiiIII111iI ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'nations' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 95 - 95: iII111iiiii11 . iiiIIii1IIi
@ oo000 . route ( '/search/' )
def O00o ( ) :
 IiiIII111iI ( "Browse" , '/search' )
 O00 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if O00 :
  i11I1 = "http://phimno1.net/tim-kiem/keyword/page-%s.html" . replace ( "keyword" , O00 . replace ( " " , "+" ) )
  Ii11Ii11I = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( i11I1 ) , 1 )
  oo000 . redirect ( Ii11Ii11I )
  if 43 - 43: ooOO00oOo - I1i1i1ii * iiiIIii1IIi
@ oo000 . route ( '/search/<murl>/<page>' )
def O0O00o0OOO0 ( murl , page ) :
 IiiIII111iI ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 i1I1Iiii1111 = iII111ii ( murl , page , 'search' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1I1Iiii1111 , view_mode = 52 )
  else :
   return oo000 . finish ( i1I1Iiii1111 )
 else :
  return oo000 . finish ( i1I1Iiii1111 )
  if 27 - 27: OO0OO0O0O0 % I1IiiI * II1iI + Oo0Ooo + iII111iiiii11 * I1IiiI
@ oo000 . route ( '/mirrors/<murl>' )
def o0oo0o0O00OO ( murl ) :
 IiiIII111iI ( "Browse" , '/mirrors/%s' % ( murl ) )
 i1I1Iiii1111 = [ ]
 for o0oO in I1i1iii ( murl ) :
  if "Zing" not in o0oO [ "name" ] and "ClipVN" not in o0oO [ "name" ] :
   i1iiI11I = { }
   i1iiI11I [ "label" ] = o0oO [ "name" ] . strip ( )
   iiii = str ( uuid . uuid1 ( ) )
   oO0o0O0OOOoo0 = oo000 . get_storage ( iiii )
   oO0o0O0OOOoo0 [ "list" ] = o0oO [ "eps" ]
   i1iiI11I [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( iiii ) )
   i1I1Iiii1111 . append ( i1iiI11I )
 return oo000 . finish ( i1I1Iiii1111 )
 if 48 - 48: OO0OO0O0O0 + OO0OO0O0O0 - O0Oo0oO0o . iiiI11 / iiiIIii1IIi
@ oo000 . route ( '/eps/<eps_list>' )
def OoOOO00oOO0 ( eps_list ) :
 IiiIII111iI ( "Browse" , '/eps' )
 i1I1Iiii1111 = [ ]
 for oOoo in oo000 . get_storage ( eps_list ) [ "list" ] :
  i1iiI11I = { }
  i1iiI11I [ "label" ] = oOoo [ "name" ] . strip ( )
  i1iiI11I [ "is_playable" ] = True
  i1iiI11I [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( oOoo [ "url" ] ) )
  i1I1Iiii1111 . append ( i1iiI11I )
 return oo000 . finish ( i1I1Iiii1111 )
 if 8 - 8: oOoO0oo0OOOo
@ oo000 . route ( '/play/<url>' )
def o00O ( url ) :
 IiiIII111iI ( "Play" , '/play/%s' % ( url ) )
 OOO0OOO00oo = xbmcgui . DialogProgress ( )
 OOO0OOO00oo . create ( 'phimno1.net' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( Iii111II ( url ) )
 OOO0OOO00oo . close ( )
 del OOO0OOO00oo
 if 9 - 9: Ooo00oOo00o
def Iii111II ( url ) :
 I1i1iiI1 = i11O0oo0OO0oOOOo ( url )
 i1i1i11IIi = ""
 if "youtube" in I1i1iiI1 :
  II1III = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( I1i1iiI1 )
  iI1iI1I1i1I = II1III [ 0 ] [ len ( II1III [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % iI1iI1I1i1I
 if "lh3.googleusercontent.com" in I1i1iiI1 :
  iIi11Ii1 = re . compile ( '"(https://lh3.googleusercontent.com/.+?)"' ) . findall ( I1i1iiI1 )
  i1i1i11IIi = iIi11Ii1 [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( iIi11Ii1 ) > 1 ) : i1i1i11IIi = iIi11Ii1 [ 1 ]
 if '{link:"' in I1i1iiI1 :
  Ii11iII1 = re . compile ( '\{link:"(.+?)"' ) . findall ( I1i1iiI1 ) [ 0 ]
  Oo0O0O0ooO0O = IIIIii ( Ii11iII1 )
  if "list" in Oo0O0O0ooO0O :
   O0o0 = sorted ( Oo0O0O0ooO0O [ "list" ] [ 0 ] [ "link" ] , key = itemgetter ( 'link' ) )
   i1i1i11IIi = O0o0 [ 0 ] [ "link" ]
   if oo000 . get_setting ( 'HQ' , bool ) :
    i1i1i11IIi = O0o0 [ - 1 ] [ "link" ]
  else :
   O0o0 = sorted ( Oo0O0O0ooO0O [ "link" ] , key = itemgetter ( 'link' ) )
   i1i1i11IIi = O0o0 [ 0 ] [ "link" ]
   if oo000 . get_setting ( 'HQ' , bool ) :
    i1i1i11IIi = O0o0 [ - 1 ] [ "link" ]
 return i1i1i11IIi
 if 71 - 71: i1iIii1Ii1II + iiiI11 % Oo0Ooo + O0Oo0oO0o - IIIII
def iII111ii ( url , page , route_name ) :
 oO0OOoO0 = int ( page ) + 1
 I1i1iiI1 = i11O0oo0OO0oOOOo ( url % page )
 II1III = re . compile ( '<li class="movie-item"><a class="block-wrapper" title="(.+?)" href="(.+?)"><div class="movie-thumbnail" style=".*?url=(.+?)\)\; [^>]*>' ) . findall ( I1i1iiI1 )
 i1I1Iiii1111 = [ ]
 for I111Ii111 , Ii11iII1 , i111IiI1I in II1III :
  i1iiI11I = { }
  i1iiI11I [ "label" ] = I111Ii111 . strip ( )
  i1iiI11I [ "thumbnail" ] = i111IiI1I
  i1iiI11I [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://phimno1.net/" + Ii11iII1 ) )
  i1I1Iiii1111 . append ( i1iiI11I )
 if len ( i1I1Iiii1111 ) == oOOo :
  i1I1Iiii1111 . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , oO0OOoO0 ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return i1I1Iiii1111
 if 70 - 70: oOo0oooo00o . oOo0O0Ooo / iiiiIi11i . oOo0oooo00o - OO0OO0O0O0 / IIIII
def I1i1iii ( murl ) :
 I1i1iiI1 = i11O0oo0OO0oOOOo ( murl )
 II1III = re . compile ( 'href="(xem-phim/.+?/\d+.html)">Xem phim</a>' ) . findall ( I1i1iiI1 )
 I1i1iiI1 = i11O0oo0OO0oOOOo ( 'http://phimno1.net/' + II1III [ 0 ] )
 ooOooo000oOO = re . compile ( '(<h3 class="server-name">.+?</div>)' ) . findall ( I1i1iiI1 )
 Oo0oOOo = re . compile ( '\[<a[^>]*title="(.+?)">Xem thêm</a>\]' ) . findall ( I1i1iiI1 ) [ 0 ]
 Oo0OoO00oOO0o = [ ]
 for o0oO in ooOooo000oOO :
  OOO00O = re . compile ( '<h3 class="server-name">(.+?)</h3>' ) . findall ( o0oO ) [ 0 ] . strip ( ) . replace ( ":" , "" )
  OOoOO0oo0ooO = [ ]
  for O0o0O00Oo0o0 , O00O0oOO00O00 in re . compile ( '<li class="episode"><a href="(.+?)"[^>]*>(.+?)</a></li>' ) . findall ( o0oO ) :
   oOoo = { }
   oOoo [ "url" ] = 'http://phimno1.net/' + O0o0O00Oo0o0
   oOoo [ "name" ] = "Part %s - %s" % ( O00O0oOO00O00 , Oo0oOOo )
   OOoOO0oo0ooO . append ( oOoo )
  o0oO = { }
  o0oO [ "name" ] = OOO00O
  o0oO [ "eps" ] = OOoOO0oo0ooO
  Oo0OoO00oOO0o . append ( o0oO )
 return Oo0OoO00oOO0o
 if 11 - 11: IIIII . O0Oo0oO0o
@ oo000 . cached ( TTL = 60 )
def i11O0oo0OO0oOOOo ( url ) :
 o0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36' ,
 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' ,
 'Accept-Encoding' : 'gzip, deflate, sdch'
 }
 oo0oOo = requests . get ( url , headers = o0 )
 oo0oOo . encoding = "utf-8"
 return IIi1IiiiI1Ii ( oo0oOo . text ) . encode ( "utf8" )
 if 89 - 89: oOoO0oo0OOOo
def IIIIii ( url ) :
 OO0oOoOO0oOO0 = requests . get ( 'http://thong.viettv24.com/p' ) . text . strip ( )
 oO0OOoo0OO = { 'link' : url , 'f' : 'true' }
 return requests . post ( OO0oOoOO0oOO0 , data = oO0OOoo0OO ) . json ( )
 if 65 - 65: oOo0oooo00o . iiiIIii1IIi / OO0OO0O0O0 - oOo0oooo00o
iii1i1iiiiIi = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.phim60s' ) . getAddonInfo ( 'profile' ) )
if 2 - 2: ooOO00oOo / OO0OO0O0O0 / iiiiIi11i % oOoO0oo0OOOo % oOo0oooo00o
if os . path . exists ( iii1i1iiiiIi ) == False :
 os . mkdir ( iii1i1iiiiIi )
o0o00OO0 = os . path . join ( iii1i1iiiiIi , 'visitor' )
if 7 - 7: i1iIii1Ii1II + O00OoOoo00 + OO0OO0O0O0
if os . path . exists ( o0o00OO0 ) == False :
 from random import randint
 Ii = open ( o0o00OO0 , "w" )
 Ii . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Ii . close ( )
 if 64 - 64: iiiI11 / oOoO0oo0OOOo - OO0OO0O0O0 - O00o0o0000o0o
def O0oOoOOOoOO ( utm_url ) :
 ii1ii11IIIiiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O00OOOoOoo0O = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : ii1ii11IIIiiI }
 )
  O000OOo00oo = urllib2 . urlopen ( O00OOOoOoo0O ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return O000OOo00oo
 if 71 - 71: Oo0Ooo + IIIII
def IiiIII111iI ( group , name ) :
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
  oOo = "1.0"
  oOO00Oo = open ( o0o00OO0 ) . read ( )
  i1iIIIi1i = "Phim60s"
  iI1iIIiiii = "UA-52209804-2"
  i1 = "www.viettv24.com"
  iI11i1ii11 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   OOooo0O00o = iI11i1ii11 + "?" + "utmwv=" + oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIIIi1i ) + "&utmac=" + iI1iIIiiii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOO00Oo , "1" , "1" , "2" ] )
   if 85 - 85: iiiiIi11i - oOo0O0Ooo
   if 32 - 32: iII111iiiii11 / iiiIIii1IIi - iiiiIi11i
   if 91 - 91: I1i1i1ii % I1IiiI % iiiIIii1IIi
   if 20 - 20: i1iIii1Ii1II % oOo0oooo00o / oOo0oooo00o + oOo0oooo00o
   if 45 - 45: II1iI - IIIII - iII111iiiii11 - Ooo00oOo00o . O0 / OO0OO0O0O0
  else :
   if group == "None" :
    OOooo0O00o = iI11i1ii11 + "?" + "utmwv=" + oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIIIi1i + "/" + name ) + "&utmac=" + iI1iIIiiii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOO00Oo , "1" , "1" , "2" ] )
    if 51 - 51: OO0OO0O0O0 + I1i1i1ii
    if 8 - 8: II1iI * oOoO0oo0OOOo - oOo0oooo00o - Ooo00oOo00o * i1iIii1Ii1II % ooOO00oOo
    if 48 - 48: OO0OO0O0O0
    if 11 - 11: O00o0o0000o0o + iII111iiiii11 - Ooo00oOo00o / iiiiIi11i + oOo0O0Ooo . O0
    if 41 - 41: oOo0oooo00o - OO0OO0O0O0 - OO0OO0O0O0
   else :
    OOooo0O00o = iI11i1ii11 + "?" + "utmwv=" + oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1iIIIi1i + "/" + group + "/" + name ) + "&utmac=" + iI1iIIiiii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOO00Oo , "1" , "1" , "2" ] )
    if 68 - 68: i1iIii1Ii1II % O00OoOoo00
    if 88 - 88: iiiIIii1IIi - iiiI11 + i1iIii1Ii1II
    if 40 - 40: ooOO00oOo * oOo0oooo00o + i1iIii1Ii1II % I1i1i1ii
    if 74 - 74: II1iI - oOo0O0Ooo + iII111iiiii11 + O00OoOoo00 / oOoO0oo0OOOo
    if 23 - 23: OO0OO0O0O0
    if 85 - 85: oOo0oooo00o
  print "============================ POSTING ANALYTICS ============================"
  O0oOoOOOoOO ( OOooo0O00o )
  if 84 - 84: ooOO00oOo . iiiIIii1IIi % iII111iiiii11 + oOo0oooo00o % iII111iiiii11 % Ooo00oOo00o
  if not group == "None" :
   IIi1 = iI11i1ii11 + "?" + "utmwv=" + oOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( i1 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i1iIIIi1i + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i1iIIIi1i ) + "&utmac=" + iI1iIIiiii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , oOO00Oo , "1" , "2" ] )
   if 45 - 45: I1i1i1ii / I1i1i1ii + O00OoOoo00 + iiiI11
   if 47 - 47: iiiiIi11i + iiiI11
   if 82 - 82: O0 . IIIII - iiiIIii1IIi - IIIII * O0
   if 77 - 77: iiiIIii1IIi * Ooo00oOo00o
   if 95 - 95: ooOO00oOo + Oo0Ooo
   if 6 - 6: iiiI11 / Oo0Ooo + I1i1i1ii * II1iI
   if 80 - 80: O0
   if 83 - 83: O00o0o0000o0o . Oo0Ooo + O0 . iiiiIi11i * O00o0o0000o0o
   try :
    print "============================ POSTING TRACK EVENT ============================"
    O0oOoOOOoOO ( IIi1 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 53 - 53: O0
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 31 - 31: Ooo00oOo00o
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
