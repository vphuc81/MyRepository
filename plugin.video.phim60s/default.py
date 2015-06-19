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
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: oO00oOo = xbmc . translatePath ( os . path . join ( oO00oOo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim60s.jpg' , oO00oOo )
 if 49 - 49: OOOo0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , oO00oOo )
 if 49 - 49: Oooo000o = xbmcgui . WindowDialog ( )
 if 49 - 49: Oooo000o . addControl ( OOOo0 )
 if 49 - 49: Oooo000o . doModal ( )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim hot' , 'path' : '%s/hottest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/danh-sach/phim-chieu-rap/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
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
@ oo000 . route ( '/hottest/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/hottest/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'hottest' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/movies/<murl>/<page>' )
def O0 ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 34 - 34: ooO00oOoo % i1 % iiiIIii1IIi % ooO00oOoo * iIi / o0O
@ oo000 . route ( '/series/<murl>/<page>' )
def Iiii ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 87 - 87: iiI1i1 / OOo000 + O0OOo - OOo000 . OOo000 / i1
@ oo000 . route ( '/genres' )
def iiIIIIi1i1 ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 IiII = [
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-hanh-dong/1/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Giật Gân' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-giat-gan/24/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-vo-thuat/2/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-chien-tranh/3/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-hoat-hinh/5/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Gia Đình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-gia-dinh/15/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị & Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-kinh-di-ma/6/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Bí Ẩn' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-bi-an/23/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-hai-huoc/7/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-phieu-luu/9/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-vien-tuong/8/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-than-thoai/10/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Hình Sự' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-hinh-su/4/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-tam-ly/16/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-tinh-cam/17/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tài Liệu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-tai-lieu/20/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Lịch Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-lich-su/25/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Tiểu Sử' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-tieu-su/29/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tây' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-vien-tay/30/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-am-nhac/19/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-the-thao/18/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Cổ Trang' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-co-trang/12/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Truyền Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/the-loai/phim-truyen-hinh/11/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 54 - 54: o0oo0o % OO0OO0O0O0 + ii1IiI1i - iIi / Oo
@ oo000 . route ( '/genres/<murl>/<page>' )
def iIiiI1 ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 68 - 68: ii1IiI1i - Oo0Ooo - I11i / o0oo0o - I11i + I1IiiI
@ oo000 . route ( '/nations' )
def IiiIII111ii ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 IiII = [
 { 'label' : 'Phim Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-viet-nam/1/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-trung-quoc/4/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-han-quoc/2/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Hồng Kong' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-hong-kong/6/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Đài Loan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-dai-loan/7/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-nhat-ban/3/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-an-do/10/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-thai-lan/11/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-chau-a/8/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim60s.info/quoc-gia/phim-my-chau-au/5/page-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 3 - 3: iIi + OO0OO0O0O0
@ oo000 . route ( '/nations/<murl>/<page>' )
def I1Ii ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 66 - 66: OOo00O0Oo0oO
@ oo000 . route ( '/search/' )
def oo0Ooo0 ( ) :
 I11i11Ii ( "Browse" , '/search' )
 I1I11I1I1I = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if I1I11I1I1I :
  OooO0OO = "http://phim60s.info/tim-kiem/keyword/page-%s.html" . replace ( "keyword" , I1I11I1I1I . replace ( " " , "+" ) )
  iiiIi = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( OooO0OO ) , 1 )
  oo000 . redirect ( iiiIi )
  if 24 - 24: OO0OO0O0O0 % IiiIII111iI + I1IiiI + O0OOo + Ii11111i
@ oo000 . route ( '/search/<murl>/<page>' )
def OOoO000O0OO ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 23 - 23: Oo0Ooo + ii1IiI1i
@ oo000 . route ( '/mirrors/<murl>' )
def oOo ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 IiII = [ ]
 for oOoOoO in ii1I ( murl ) :
  if "Zing" not in oOoOoO [ "name" ] and "ClipVN" not in oOoOoO [ "name" ] :
   OooO0 = { }
   OooO0 [ "label" ] = oOoOoO [ "name" ] . strip ( )
   II11iiii1Ii = str ( uuid . uuid1 ( ) )
   OO0o = oo000 . get_storage ( II11iiii1Ii )
   OO0o [ "list" ] = oOoOoO [ "eps" ]
   OooO0 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( II11iiii1Ii ) )
   IiII . append ( OooO0 )
 return oo000 . finish ( IiII )
 if 82 - 82: Oo0Ooo . o0oo0o / OOooOOo * OO0OO0O0O0 % iiI1i1 % iiiIIii1IIi
@ oo000 . route ( '/eps/<eps_list>' )
def Oo00OOOOO ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 IiII = [ ]
 for O0O in oo000 . get_storage ( eps_list ) [ "list" ] :
  OooO0 = { }
  OooO0 [ "label" ] = O0O [ "name" ] . strip ( )
  OooO0 [ "is_playable" ] = True
  OooO0 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( O0O [ "url" ] ) )
  IiII . append ( OooO0 )
 return oo000 . finish ( IiII )
 if 83 - 83: Oo + i1 * IiiIII111iI % I11i + Oo
@ oo000 . route ( '/play/<url>' )
def Ii1iIIIi1ii ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 o0oo0o0O00OO = xbmcgui . DialogProgress ( )
 o0oo0o0O00OO . create ( 'phim60s.info' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( o0oO ( url ) )
 o0oo0o0O00OO . close ( )
 del o0oo0o0O00OO
 if 48 - 48: Oo + Oo / i1 / iiiIIii1IIi
def o0oO ( url ) :
 i1iiI11I = iiii ( url )
 oO0o0O0OOOoo0 = ""
 if "youtube" in i1iiI11I :
  IiIiiI = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( i1iiI11I )
  I1I = IiIiiI [ 0 ] [ len ( IiIiiI [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % I1I
 if "lh3.googleusercontent.com" in i1iiI11I :
  oOO00oOO = re . compile ( '"(https://lh3.googleusercontent.com/.+?)"' ) . findall ( i1iiI11I )
  oO0o0O0OOOoo0 = oOO00oOO [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( oOO00oOO ) > 1 ) : oO0o0O0OOOoo0 = oOO00oOO [ 1 ]
 if "proxy.link=https://picasaweb.google.com/" in i1iiI11I :
  OoOo = re . compile ( 'proxy.link=(https://picasaweb.google.com/.+?)&amp;' ) . findall ( i1iiI11I ) [ 0 ]
  i1iiI11I = iI ( OoOo )
  oOO00oOO = re . compile ( ',\{"url"\:"(https://.+?)"\,"height"\:\d+\,"width"\:\d+\,"type"\:"video/mpeg4"\}' ) . findall ( i1iiI11I )
  oO0o0O0OOOoo0 = oOO00oOO [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( oOO00oOO ) > 1 ) : oO0o0O0OOOoo0 = oOO00oOO [ 1 ]
 return oO0o0O0OOOoo0
 if 60 - 60: Oo / Oo
def oooO0oo0oOOOO ( url , page , route_name ) :
 I1II1III11iii = int ( page ) + 1
 i1iiI11I = iiii ( url % page )
 IiIiiI = re . compile ( '<img[^>]*src="(.+?)"></a><div class="info"><div class="name"><a title="(.+?)" href="(.+?)">' ) . findall ( i1iiI11I )
 IiII = [ ]
 for Oo000 , oo , ii11I in IiIiiI :
  OooO0 = { }
  OooO0 [ "label" ] = oo . strip ( )
  OooO0 [ "thumbnail" ] = Oo000
  OooO0 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://phim60s.info/" + ii11I ) )
  IiII . append ( OooO0 )
 if len ( IiII ) == oOOo :
  IiII . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , I1II1III11iii ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return IiII
 if 96 - 96: i1 % OOo00O0Oo0oO . o0oo0o + iII111iiiii11 * iiI1i1 - o0O
def ii1I ( murl ) :
 i1iiI11I = iiii ( murl )
 IiIiiI = re . compile ( '(xem-phim/.+?/\d+.html)' ) . findall ( i1iiI11I )
 i1iiI11I = iiii ( 'http://phim60s.info/' + IiIiiI [ 0 ] )
 i11i1 = re . compile ( '<div class="server">.+?</ul></div>' ) . findall ( i1iiI11I )
 IIIii1II1II = re . compile ( '<span itemprop="title" title="(.+?)">' ) . findall ( i1iiI11I ) [ 0 ]
 i1I1iI = [ ]
 for oOoOoO in i11i1 :
  oo0OooOOo0 = re . compile ( '<img[^>]*/>(.+?)</div>' ) . findall ( oOoOoO ) [ 0 ] . strip ( )
  o0OO00oO = [ ]
  for I11i1I1I , oO0Oo in re . compile ( '<a[^>]*href="(xem-phim/.+?/\d+.html)"[^>]*><b>(.+?)</b></a>' ) . findall ( oOoOoO ) :
   O0O = { }
   O0O [ "url" ] = 'http://phim60s.info/' + I11i1I1I
   O0O [ "name" ] = "Part %s - %s" % ( oO0Oo , IIIii1II1II )
   o0OO00oO . append ( O0O )
  oOoOoO = { }
  oOoOoO [ "name" ] = oo0OooOOo0
  oOoOoO [ "eps" ] = o0OO00oO
  i1I1iI . append ( oOoOoO )
 return i1I1iI
 if 54 - 54: IiiIII111iI - ii1IiI1i + iII111iiiii11
@ oo000 . cached ( TTL = 60 )
def iiii ( url ) :
 O0o0 = urllib2 . Request ( url )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36' )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 O0o0 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 OO00Oo = urllib2 . urlopen ( O0o0 )
 O0OOO0OOoO0O = OO00Oo . read ( )
 OO00Oo . close ( )
 if "gzip" in OO00Oo . info ( ) . getheader ( 'Content-Encoding' ) :
  O0OOO0OOoO0O = zlib . decompress ( O0OOO0OOoO0O , 16 + zlib . MAX_WBITS )
 O0OOO0OOoO0O = '' . join ( O0OOO0OOoO0O . splitlines ( ) ) . replace ( '\'' , '"' )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '\n' , '' )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '\t' , '' )
 O0OOO0OOoO0O = re . sub ( '  +' , ' ' , O0OOO0OOoO0O )
 O0OOO0OOoO0O = O0OOO0OOoO0O . replace ( '> <' , '><' )
 return O0OOO0OOoO0O
 if 70 - 70: ooO00oOoo * OOooOOo * Oo / OOo00O0Oo0oO
def iI ( url ) :
 i1iiI11I = urllib2 . urlopen ( 'http://echipstore.net/p' )
 oO = i1iiI11I . read ( )
 i1iiI11I . close ( )
 OOoO0O00o0 = { 'isslverify' : 'true' , 'iagent' : 'User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0' , 'url' : url , 'ihttpheader' : 'true' }
 iII = urllib . urlencode ( OOoO0O00o0 )
 O0o0 = urllib2 . Request ( urllib . unquote_plus ( oO ) , iII )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
 O0o0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0 . add_header ( 'Content-type' , 'application/x-www-form-urlencoded' )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OO00Oo = urllib2 . urlopen ( O0o0 )
 ii11I = OO00Oo . read ( )
 OO00Oo . close ( )
 if "gzip" in OO00Oo . info ( ) . getheader ( 'Content-Encoding' ) :
  ii11I = zlib . decompress ( ii11I , 16 + zlib . MAX_WBITS )
 ii11I = '' . join ( ii11I . splitlines ( ) ) . replace ( '\'' , '"' )
 ii11I = ii11I . replace ( '\n' , '' )
 ii11I = ii11I . replace ( '\t' , '' )
 ii11I = re . sub ( '  +' , ' ' , ii11I )
 ii11I = ii11I . replace ( '> <' , '><' )
 return ii11I
 if 80 - 80: ooO00oOoo . iiI1i1
IIi = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.phim60s' ) . getAddonInfo ( 'profile' ) )
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
  O0o0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : II11i1I11Ii1i }
 )
  OO00Oo = urllib2 . urlopen ( O0o0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OO00Oo
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
  I1I1iIiII1 = "Phim60s"
  i11i1I1 = "UA-52209804-2"
  ii1IOo0ooOo0o = "www.viettv24.com"
  Ii1i1 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iiIii = Ii1i1 + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
   if 79 - 79: iII111iiiii11 / OO0OO0O0O0
   if 75 - 75: o0O % IiiIII111iI % IiiIII111iI . O0OOo
   if 5 - 5: IiiIII111iI * OOo000 + o0O . o0oo0o + o0O
   if 91 - 91: OO0OO0O0O0
   if 61 - 61: i1
  else :
   if group == "None" :
    iiIii = Ii1i1 + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
    if 64 - 64: OOo000 / o0O - OO0OO0O0O0 - Oo
    if 86 - 86: Oo % o0O / ii1IiI1i / o0O
    if 42 - 42: I11i
    if 67 - 67: O0OOo . iIi . OO0OO0O0O0
    if 10 - 10: Ii11111i % Ii11111i - iiiIIii1IIi / o0oo0o + OOo00O0Oo0oO
   else :
    iiIii = Ii1i1 + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1I1iIiII1 + "/" + group + "/" + name ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , IIi1i , "1" , "1" , "2" ] )
    if 87 - 87: iiI1i1 * Ii11111i + o0oo0o / iiiIIii1IIi / iIi
    if 37 - 37: iIi - OOo000 * iiI1i1 % Oo0Ooo - O0OOo
    if 83 - 83: Oo / ii1IiI1i
    if 34 - 34: ooO00oOoo
    if 57 - 57: iiI1i1 . Oo . I1IiiI
    if 42 - 42: Oo + Ii11111i % OO0OO0O0O0
  print "============================ POSTING ANALYTICS ============================"
  OoOO0oo0o ( iiIii )
  if 6 - 6: iiI1i1
  if not group == "None" :
   oOOo0oOo0 = Ii1i1 + "?" + "utmwv=" + Oooo0O0oo00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( ii1IOo0ooOo0o ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + I1I1iIiII1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( I1I1iIiII1 ) + "&utmac=" + i11i1I1 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , IIi1i , "1" , "2" ] )
   if 49 - 49: OOooOOo . Oo0Ooo - I1IiiI / i1 . ii1IiI1i
   if 1 - 1: OOooOOo / IiiIII111iI % iIi * ooO00oOoo . Oo0Ooo
   if 2 - 2: Ii11111i * Oo - iiiIIii1IIi + ii1IiI1i . iiI1i1 % iIi
   if 92 - 92: iIi
   if 25 - 25: OOooOOo - ii1IiI1i / iII111iiiii11 / IiiIII111iI
   if 12 - 12: ii1IiI1i * iIi % I1IiiI % iiiIIii1IIi
   if 20 - 20: o0oo0o % OOo00O0Oo0oO / OOo00O0Oo0oO + OOo00O0Oo0oO
   if 45 - 45: iiI1i1 - ooO00oOoo - iII111iiiii11 - I11i . i1 / OO0OO0O0O0
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OoOO0oo0o ( oOOo0oOo0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 51 - 51: OO0OO0O0O0 + iIi
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 8 - 8: iiI1i1 * o0O - OOo00O0Oo0oO - I11i * o0oo0o % ii1IiI1i
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
