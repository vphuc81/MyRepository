#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , json
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.phim60s"
oOOo = 32
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = ""
 OOOo0 = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  Oooo000o = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in Oooo000o for b in OOOo0 ) : break
 while True :
  IiIi11iIIi1Ii = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in IiIi11iIIi1Ii for b in OOOo0 ) : break
 try :
  oO00oOo = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   oO00oOo = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , oO00oOo . lower ( ) ) : break
 Oo0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( oO00oOo , "11" , Oooo000o , IiIi11iIIi1Ii ) ) . read ( )
 if "allowed" in Oo0O :
  IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  IiI = xbmc . translatePath ( os . path . join ( IiI , "temp.jpg" ) )
  '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim60s.jpg' , IiI )
  ooOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI )
  Oo = xbmcgui . WindowDialog ( )
  Oo . addControl ( ooOo )
  Oo . doModal ( )'''
  if 67 - 67: O00ooOO . I1iII1iiII
  iI1Ii11111iIi = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-chieu-rap/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( iI1Ii11111iIi )
 else :
  iI1Ii11111iIi = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-chieu-rap/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phimno1.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( iI1Ii11111iIi )
  if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
  if 56 - 56: ooO00oOoo - O0OOo
@ oo000 . route ( '/latest/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/latest/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'latest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 74 - 74: Oo0o00o0Oo0 * ii11
@ oo000 . route ( '/hottest/<murl>/<page>' )
def I1I1i1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/hottest/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'hottest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 18 - 18: iiIIIIi1i1 / OOoOoo00oo - iI1 + OOoOoo00oo % I1iII1iiII - o00ooo0
@ oo000 . route ( '/movies/<murl>/<page>' )
def iIIIIiI ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 91 - 91: OO0OO0O0O0 / Oo0oO0ooo - ii11 + ooO00oOoo % I1IiiI
@ oo000 . route ( '/series/<murl>/<page>' )
def iI1i ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 42 - 42: ooO00oOoo / I1IiiI + Oo0Ooo - Oo0o00o0Oo0
@ oo000 . route ( '/genres' )
def oo0Ooo0 ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 iI1Ii11111iIi = [
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
 return oo000 . finish ( iI1Ii11111iIi )
 if 46 - 46: iI1 % iI1 - Oo0oO0ooo * o00ooo0 % ii11
@ oo000 . route ( '/genres/<murl>/<page>' )
def OOooO0OOoo ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 29 - 29: o00ooo0 / iiiIIii1IIi
@ oo000 . route ( '/nations' )
def IiIIIiI1I1 ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 iI1Ii11111iIi = [
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
 return oo000 . finish ( iI1Ii11111iIi )
 if 86 - 86: Oo0Ooo + Oo0o00o0Oo0 + iI1 * O0OOo + o00ooo0
@ oo000 . route ( '/nations/<murl>/<page>' )
def oOoO ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 68 - 68: I1i1iI1i . Oo0oO0ooo . Oo0Ooo
@ oo000 . route ( '/search/' )
def II ( ) :
 I11i11Ii ( "Browse" , '/search' )
 iI = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if iI :
  iI11iiiI1II = "http://phimno1.net/tim-kiem/keyword/page-%s.html" . replace ( "keyword" , iI . replace ( " " , "+" ) )
  O0oooo0Oo00 = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( iI11iiiI1II ) , 1 )
  oo000 . redirect ( O0oooo0Oo00 )
  if 17 - 17: iiiIIii1IIi % iI1 % Oo0Ooo . I1iII1iiII
@ oo000 . route ( '/search/<murl>/<page>' )
def O0o0Oo ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 78 - 78: iiiIIii1IIi - Oo0o00o0Oo0 * Oo0ooO0oo0oO + o00ooo0 + ii11 + ii11
@ oo000 . route ( '/mirrors/<murl>' )
def I11I11i1I ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 iI1Ii11111iIi = [ ]
 for ii11i1iIII in Ii1I ( murl ) :
  if "Zing" not in ii11i1iIII [ "name" ] and "ClipVN" not in ii11i1iIII [ "name" ] :
   Oo0o0 = { }
   Oo0o0 [ "label" ] = ii11i1iIII [ "name" ] . strip ( )
   III1ii1iII = str ( uuid . uuid1 ( ) )
   oo0oooooO0 = oo000 . get_storage ( III1ii1iII )
   oo0oooooO0 [ "list" ] = ii11i1iIII [ "eps" ]
   Oo0o0 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( III1ii1iII ) )
   iI1Ii11111iIi . append ( Oo0o0 )
 return oo000 . finish ( iI1Ii11111iIi )
 if 19 - 19: O0OOo + iI1
@ oo000 . route ( '/eps/<eps_list>' )
def ooo ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 iI1Ii11111iIi = [ ]
 for ii1I1i1I in oo000 . get_storage ( eps_list ) [ "list" ] :
  Oo0o0 = { }
  Oo0o0 [ "label" ] = ii1I1i1I [ "name" ] . strip ( )
  Oo0o0 [ "is_playable" ] = True
  Oo0o0 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( ii1I1i1I [ "url" ] ) )
  iI1Ii11111iIi . append ( Oo0o0 )
 return oo000 . finish ( iI1Ii11111iIi )
 if 88 - 88: Oo0ooO0oo0oO + OO0OO0O0O0 / I1i1iI1i * ii11
@ oo000 . route ( '/play/<url>' )
def iiiIi1i1I ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 oOO00oOO = xbmcgui . DialogProgress ( )
 oOO00oOO . create ( 'phimno1.net' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( OoOo ( url ) )
 oOO00oOO . close ( )
 del oOO00oOO
 if 18 - 18: Oo0Ooo
def OoOo ( url ) :
 Oo0O = Ii11I ( url )
 OOO0OOO00oo = ""
 if "youtube" in Oo0O :
  Iii111II = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( Oo0O )
  iiii11I = Iii111II [ 0 ] [ len ( Iii111II [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % iiii11I
 if "lh3.googleusercontent.com" in Oo0O :
  Ooo0OO0oOO = re . compile ( '"(https://lh3.googleusercontent.com/.+?)"' ) . findall ( Oo0O )
  OOO0OOO00oo = Ooo0OO0oOO [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( Ooo0OO0oOO ) > 1 ) : OOO0OOO00oo = Ooo0OO0oOO [ 1 ]
 if 'proxy.link' in Oo0O :
  ii11i1 = re . compile ( 'proxy.link=(.+?)&amp;' ) . findall ( Oo0O ) [ 0 ]
  IIIii1II1II = re . compile ( '"url"\:"(.+?)"' ) . findall ( i1I1iI ( ii11i1 ) )
  OOO0OOO00oo = IIIii1II1II [ 1 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( IIIii1II1II ) > 3 ) : OOO0OOO00oo = IIIii1II1II [ 2 ]
 return OOO0OOO00oo
 if 93 - 93: iiiIIii1IIi % Oo0oO0ooo * I1IiiI
def i1IIi11111i ( url , page , route_name ) :
 Ii11Ii1I = int ( page ) + 1
 Oo0O = Ii11I ( url % page )
 Iii111II = re . compile ( '<li class="movie-item"><a class="block-wrapper" title="(.+?)" href="(.+?)"><div class="movie-thumbnail" style=".*?url=(.+?)\)\; [^>]*>' ) . findall ( Oo0O )
 iI1Ii11111iIi = [ ]
 for O00oO , I11i1I1I , oO0Oo in Iii111II :
  Oo0o0 = { }
  Oo0o0 [ "label" ] = O00oO . strip ( )
  Oo0o0 [ "thumbnail" ] = oO0Oo
  Oo0o0 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://phimno1.net/" + I11i1I1I ) )
  iI1Ii11111iIi . append ( Oo0o0 )
 if len ( iI1Ii11111iIi ) == oOOo :
  iI1Ii11111iIi . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , Ii11Ii1I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return iI1Ii11111iIi
 if 54 - 54: o00ooo0 - I1iII1iiII + iII111iiiii11
def Ii1I ( murl ) :
 Oo0O = Ii11I ( murl )
 Iii111II = re . compile ( 'href="(xem-phim/.+?/\d+.html)">Xem phim</a>' ) . findall ( Oo0O )
 Oo0O = Ii11I ( 'http://phimno1.net/' + Iii111II [ 0 ] )
 O0o0 = re . compile ( '(<h3 class="server-name">.+?</div>)' ) . findall ( Oo0O )
 OO00Oo = re . compile ( '\[<a[^>]*title="(.+?)">Xem thêm</a>\]' ) . findall ( Oo0O ) [ 0 ]
 O0OOO0OOoO0O = [ ]
 for ii11i1iIII in O0o0 :
  O00Oo000ooO0 = re . compile ( '<h3 class="server-name">(.+?)</h3>' ) . findall ( ii11i1iIII ) [ 0 ] . strip ( ) . replace ( ":" , "" )
  OoO0O00 = [ ]
  for IIiII , o0 in re . compile ( '<li class="episode"><a href="(.+?)"[^>]*>(.+?)</a></li>' ) . findall ( ii11i1iIII ) :
   ii1I1i1I = { }
   ii1I1i1I [ "url" ] = 'http://phimno1.net/' + IIiII
   ii1I1i1I [ "name" ] = "Part %s - %s" % ( o0 , OO00Oo )
   OoO0O00 . append ( ii1I1i1I )
  ii11i1iIII = { }
  ii11i1iIII [ "name" ] = O00Oo000ooO0
  ii11i1iIII [ "eps" ] = OoO0O00
  O0OOO0OOoO0O . append ( ii11i1iIII )
 return O0OOO0OOoO0O
 if 62 - 62: iiiIIii1IIi * I1i1iI1i
@ oo000 . cached ( TTL = 60 )
def Ii11I ( url ) :
 i1 = urllib2 . Request ( url )
 i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36' )
 i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 i1 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 OOO = urllib2 . urlopen ( i1 )
 Oo0oOOo = OOO . read ( )
 OOO . close ( )
 if "gzip" in OOO . info ( ) . getheader ( 'Content-Encoding' ) :
  Oo0oOOo = zlib . decompress ( Oo0oOOo , 16 + zlib . MAX_WBITS )
 Oo0oOOo = '' . join ( Oo0oOOo . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0oOOo = Oo0oOOo . replace ( '\n' , '' )
 Oo0oOOo = Oo0oOOo . replace ( '\t' , '' )
 Oo0oOOo = re . sub ( '  +' , ' ' , Oo0oOOo )
 Oo0oOOo = Oo0oOOo . replace ( '> <' , '><' )
 return Oo0oOOo
 if 58 - 58: O00ooOO * ooO00oOoo * o00 / ooO00oOoo
def i1I1iI ( url ) :
 Oo0O = urllib2 . urlopen ( 'http://thong.viettv24.com/p' )
 oO0o0OOOO = Oo0O . read ( )
 Oo0O . close ( )
 O0O0OoOO0 = {
 'iheader' : 'true' ,
 'isslverify' : 'true' ,
 'ihttpheader' : 'true' ,
 'iagent' : 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0' ,
 'url' : url
 }
 iiiI1I11i1 = urllib . urlencode ( O0O0OoOO0 )
 i1 = urllib2 . Request ( urllib . unquote_plus ( oO0o0OOOO ) , iiiI1I11i1 )
 i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
 i1 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 i1 . add_header ( 'Content-type' , 'application/x-www-form-urlencoded' )
 i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OOO = urllib2 . urlopen ( i1 )
 I11i1I1I = OOO . read ( )
 OOO . close ( )
 if "gzip" in OOO . info ( ) . getheader ( 'Content-Encoding' ) :
  I11i1I1I = zlib . decompress ( I11i1I1I , 16 + zlib . MAX_WBITS )
 I11i1I1I = '' . join ( I11i1I1I . splitlines ( ) ) . replace ( '\'' , '"' )
 I11i1I1I = I11i1I1I . replace ( '\n' , '' )
 I11i1I1I = I11i1I1I . replace ( '\t' , '' )
 I11i1I1I = re . sub ( '  +' , ' ' , I11i1I1I )
 I11i1I1I = I11i1I1I . replace ( '> <' , '><' )
 return I11i1I1I
 if 49 - 49: I1iII1iiII % iI1 . iI1 . O0OOo * iI1
O0oOO0 = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.phim60s' ) . getAddonInfo ( 'profile' ) )
if 68 - 68: OOoOoo00oo % I1IiiI . iiIIIIi1i1 . o00
if os . path . exists ( O0oOO0 ) == False :
 os . mkdir ( O0oOO0 )
o0oo0oOo = os . path . join ( O0oOO0 , 'visitor' )
if 89 - 89: I1i1iI1i
if os . path . exists ( o0oo0oOo ) == False :
 from random import randint
 OO0oOoOO0oOO0 = open ( o0oo0oOo , "w" )
 OO0oOoOO0oOO0 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OO0oOoOO0oOO0 . close ( )
 if 86 - 86: ooO00oOoo
def OOoo0O ( utm_url ) :
 Oo0ooOo0o = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : Oo0ooOo0o }
 )
  OOO = urllib2 . urlopen ( i1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OOO
 if 22 - 22: iiiIIii1IIi / Oo0Ooo * iiiIIii1IIi * O00ooOO . ooO00oOoo / Oo0Ooo
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
  Iiii = "1.0"
  OO0OoO0o00 = open ( o0oo0oOo ) . read ( )
  ooOO0O0ooOooO = "Phim60s"
  oOOOo00O00oOo = "UA-52209804-2"
  iiIIIi = "www.viettv24.com"
  ooo00OOOooO = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   O00OOOoOoo0O = ooo00OOOooO + "?" + "utmwv=" + Iiii + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ooOO0O0ooOooO ) + "&utmac=" + oOOOo00O00oOo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OO0OoO0o00 , "1" , "1" , "2" ] )
   if 77 - 77: ii11 % ii11 * Oo0oO0ooo - Oo0Ooo
   if 93 - 93: iII111iiiii11 / I1iII1iiII % Oo0Ooo + o00 * Oo0ooO0oo0oO
   if 15 - 15: O0OOo . Oo0ooO0oo0oO / o0OO0 + O0OOo
   if 78 - 78: OO0OO0O0O0 . Oo0oO0ooo . O00ooOO % ooO00oOoo
   if 49 - 49: Oo0o00o0Oo0 / Oo0ooO0oo0oO . O00ooOO
  else :
   if group == "None" :
    O00OOOoOoo0O = ooo00OOOooO + "?" + "utmwv=" + Iiii + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ooOO0O0ooOooO + "/" + name ) + "&utmac=" + oOOOo00O00oOo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OO0OoO0o00 , "1" , "1" , "2" ] )
    if 68 - 68: Oo0Ooo % o00 + Oo0Ooo
    if 31 - 31: O00ooOO . I1iII1iiII
    if 1 - 1: o0OO0 / o00ooo0 % ii11 * iiIIIIi1i1 . Oo0Ooo
    if 2 - 2: o00 * O0OOo - iiiIIii1IIi + I1iII1iiII . Oo0oO0ooo % ii11
    if 92 - 92: ii11
   else :
    O00OOOoOoo0O = ooo00OOOooO + "?" + "utmwv=" + Iiii + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ooOO0O0ooOooO + "/" + group + "/" + name ) + "&utmac=" + oOOOo00O00oOo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OO0OoO0o00 , "1" , "1" , "2" ] )
    if 25 - 25: o0OO0 - I1iII1iiII / iII111iiiii11 / o00ooo0
    if 12 - 12: I1iII1iiII * ii11 % I1IiiI % iiiIIii1IIi
    if 20 - 20: ooO00oOoo % Oo0o00o0Oo0 / Oo0o00o0Oo0 + Oo0o00o0Oo0
    if 45 - 45: Oo0oO0ooo - iiIIIIi1i1 - iII111iiiii11 - Oo0ooO0oo0oO . O00ooOO / OO0OO0O0O0
    if 51 - 51: OO0OO0O0O0 + ii11
    if 8 - 8: Oo0oO0ooo * I1i1iI1i - Oo0o00o0Oo0 - Oo0ooO0oo0oO * ooO00oOoo % I1iII1iiII
  print "============================ POSTING ANALYTICS ============================"
  OOoo0O ( O00OOOoOoo0O )
  if 48 - 48: OO0OO0O0O0
  if not group == "None" :
   I1IiiIIIi = ooo00OOOooO + "?" + "utmwv=" + Iiii + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iiIIIi ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + ooOO0O0ooOooO + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( ooOO0O0ooOooO ) + "&utmac=" + oOOOo00O00oOo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , OO0OoO0o00 , "1" , "2" ] )
   if 41 - 41: Oo0o00o0Oo0 - OO0OO0O0O0 - OO0OO0O0O0
   if 68 - 68: ooO00oOoo % OOoOoo00oo
   if 88 - 88: iiiIIii1IIi - iI1 + ooO00oOoo
   if 40 - 40: I1iII1iiII * Oo0o00o0Oo0 + ooO00oOoo % ii11
   if 74 - 74: Oo0oO0ooo - o0OO0 + iII111iiiii11 + OOoOoo00oo / I1i1iI1i
   if 23 - 23: OO0OO0O0O0
   if 85 - 85: Oo0o00o0Oo0
   if 84 - 84: I1iII1iiII . iiiIIii1IIi % iII111iiiii11 + Oo0o00o0Oo0 % iII111iiiii11 % Oo0ooO0oo0oO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OOoo0O ( I1IiiIIIi )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 42 - 42: Oo0ooO0oo0oO / O0OOo / o00ooo0 + ii11 / I1i1iI1i
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 84 - 84: iI1 * O00ooOO + o0OO0
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
