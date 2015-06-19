#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , ast
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.phimvang.org"
oOOo = 48
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii ( "None" , "None" )
 oO00oOo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: oO00oOo = xbmc . translatePath ( os . path . join ( oO00oOo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phimvang.jpg' , oO00oOo )
 if 49 - 49: OOOo0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , oO00oOo )
 if 49 - 49: Oooo000o = xbmcgui . WindowDialog ( )
 if 49 - 49: Oooo000o . addControl ( OOOo0 )
 if 49 - 49: Oooo000o . doModal ( )
 if 6 - 6: i1 * ii1IiI1i % OOooOOo / I11i / o0O / IiiIII111iI
 IiII = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-moi/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim HOT' , 'path' : '%s/hot/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-hot/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim xem nhiều' , 'path' : '%s/most_view/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-xem-nhieu/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim chiếu rạp' , 'path' : '%s/cine/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-chieu-rap/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-bo/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/phim-le/trang-%s.html' ) , 1 ) } ,
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
@ oo000 . route ( '/hot/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/hot/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'hot' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 25 - 25: OOo000
@ oo000 . route ( '/most_view/<murl>/<page>' )
def O0 ( murl , page ) :
 I11i11Ii ( "Browse" , '/most_view/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'most_view' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 34 - 34: ooO00oOoo % i1 % iiiIIii1IIi % ooO00oOoo * iIi / o0O
@ oo000 . route ( '/cine/<murl>/<page>' )
def Iiii ( murl , page ) :
 I11i11Ii ( "Browse" , '/cine/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'cine' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 87 - 87: iiI1i1 / OOo000 + O0OOo - OOo000 . OOo000 / i1
@ oo000 . route ( '/movies/<murl>/<page>' )
def iiIIIIi1i1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 54 - 54: o0oo0o % OO0OO0O0O0 + ii1IiI1i - iIi / Oo
@ oo000 . route ( '/series/<murl>/<page>' )
def iIiiI1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 68 - 68: ii1IiI1i - Oo0Ooo - I11i / o0oo0o - I11i + I1IiiI
@ oo000 . route ( '/genres' )
def IiiIII111ii ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 IiII = [
 { 'label' : 'Clip Vui' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/clip-vui/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hành Động' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/hanh-dong-xa-hoi-den/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Võ Thuật - Kiếm Hiệp' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/vo-thuat-kiem-hiep/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Tâm Lý - Tình Cảm' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/tam-ly-tinh-cam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hài Hước' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/hai-huoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Kinh Dị - Ma' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/kinh-di-ma/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phiêu Lưu' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/phieu-luu/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thần Thoại' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/than-thoai/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Viễn Tưởng' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/vien-tuong/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hoạt Hình' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/hoat-hinh/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Chiến Tranh' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/chien-tranh/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thể Thao - Âm Nhạc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/the-thao-am-nhac/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Việt Nam' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/phim-viet-nam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Trung Quốc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/phim-bo-trung-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Đài Loan' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/phim-bo-dai-loan/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim Bộ Hàn Quốc' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/phim-bo-han-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Music Box' , 'path' : '%s/genres/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/the-loai/music-box/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 3 - 3: iIi + OO0OO0O0O0
@ oo000 . route ( '/genres/<murl>/<page>' )
def I1Ii ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 66 - 66: OOo00O0Oo0oO
@ oo000 . route ( '/nations' )
def oo0Ooo0 ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 IiII = [
 { 'label' : 'Việt Nam' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/viet-nam/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Trung Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/trung-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Hàn Quốc' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/han-quoc/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Nhật Bản' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/nhat-ban/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Mỹ - Châu Âu' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/my-chau-au/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Thái Lan' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/thai-lan/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Châu Á' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/chau-a/trang-%s.html' ) , 1 ) } ,
 { 'label' : 'Ấn Độ' , 'path' : '%s/nations/%s/%s' % ( ii , urllib . quote_plus ( 'http://phim7.com/quoc-gia/an-do/trang-%s.html' ) , 1 ) }
 ]
 return oo000 . finish ( IiII )
 if 46 - 46: OOo000 % OOo000 - iiI1i1 * IiiIII111iI % iIi
@ oo000 . route ( '/nations/<murl>/<page>' )
def OOooO0OOoo ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 29 - 29: IiiIII111iI / iiiIIii1IIi
@ oo000 . route ( '/search/' )
def IiIIIiI1I1 ( ) :
 I11i11Ii ( "Browse" , '/search' )
 OoO000 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if OoO000 :
  IIiiIiI1 = "http://phim7.com/tim-kiem/tat-ca/keyword/trang-%s.html" . replace ( "keyword" , OoO000 ) . replace ( " " , "-" )
  iiIiIIi = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( IIiiIiI1 ) , 1 )
  oo000 . redirect ( iiIiIIi )
  if 65 - 65: o0O
@ oo000 . route ( '/search/<murl>/<page>' )
def ii1I ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 IiII = oooO0oo0oOOOO ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( IiII , view_mode = 52 )
 else :
  return oo000 . finish ( IiII )
  if 76 - 76: OO0OO0O0O0 / IiiIII111iI . ii1IiI1i * OOo00O0Oo0oO - o0oo0o
@ oo000 . route ( '/mirrors/<murl>' )
def Oooo ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 IiII = [ ]
 for O00o in O00 ( murl ) :
  i11I1 = { }
  i11I1 [ "label" ] = O00o [ "name" ] . strip ( )
  Ii11Ii11I = str ( uuid . uuid1 ( ) )
  iI11i1I1 = oo000 . get_storage ( Ii11Ii11I )
  iI11i1I1 [ "list" ] = O00o [ "eps" ]
  i11I1 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( Ii11Ii11I ) )
  IiII . append ( i11I1 )
 return oo000 . finish ( IiII )
 if 71 - 71: OOo000 % iIi / IiiIII111iI
@ oo000 . route ( '/eps/<eps_list>' )
def ii11i1iIII ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 IiII = [ ]
 for Ii1I in oo000 . get_storage ( eps_list ) [ "list" ] :
  i11I1 = { }
  i11I1 [ "label" ] = Ii1I [ "name" ] . strip ( )
  i11I1 [ "is_playable" ] = True
  i11I1 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( Ii1I [ "url" ] ) )
  IiII . append ( i11I1 )
 return oo000 . finish ( IiII )
 if 89 - 89: Oo0Ooo / OO0OO0O0O0 * o0O % o0oo0o % iiI1i1
@ oo000 . route ( '/play/<url>' )
def Ii1 ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 III1i1i = xbmcgui . DialogProgress ( )
 III1i1i . create ( 'phim7.com' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( iiI1 ( url ) )
 III1i1i . close ( )
 del III1i1i
 if 19 - 19: Oo + OOo000
def iiI1 ( url ) :
 ooo = ii1I1i1I ( url )
 OOoo0O0 = ""
 if "youtube" in ooo :
  iiiIi1i1I = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( ooo )
  oOO00oOO = iiiIi1i1I [ 0 ] [ len ( iiiIi1i1I [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % oOO00oOO
 if "lh3.googleusercontent.com" in ooo :
  OoOo = re . compile ( '"(https://lh3.googleusercontent.com/.+?)"' ) . findall ( ooo )
  OOoo0O0 = OoOo [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( OoOo ) > 1 ) :
   OOoo0O0 = OoOo [ 1 ]
  return OOoo0O0
 if "redirector.googlevideo.com/videoplayback" in ooo :
  OoOo = re . compile ( '"(https://redirector.googlevideo.com/.+?)"' ) . findall ( ooo )
  OOoo0O0 = OoOo [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) and ( len ( OoOo ) > 1 ) :
   OOoo0O0 = OoOo [ 1 ]
  return OOoo0O0
  if 18 - 18: Oo0Ooo
def oooO0oo0oOOOO ( url , page , route_name ) :
 Ii11I = int ( page ) + 1
 ooo = ii1I1i1I ( url % page )
 iiiIi1i1I = re . compile ( '<h2><a href="(.+?)" title="(.+?)">.+?<img class="lazy"[^>]*data-original="(.+?)"[^>]*/>' ) . findall ( ooo )
 IiII = [ ]
 for OOO0OOO00oo , Iii111II , iiii11I in iiiIi1i1I :
  i11I1 = { }
  i11I1 [ "label" ] = Iii111II
  i11I1 [ "thumbnail" ] = iiii11I
  i11I1 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://phim7.com" + OOO0OOO00oo . replace ( "/phim/" , "/xem-phim/" ) ) )
  IiII . append ( i11I1 )
 if len ( IiII ) == oOOo :
  IiII . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , Ii11I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return IiII
 if 96 - 96: i1 % OOo00O0Oo0oO . o0oo0o + iII111iiiii11 * iiI1i1 - o0O
def O00 ( murl ) :
 ooo = ii1I1i1I ( murl )
 iiiIi1i1I = re . compile ( '<p class="epi"><b>(.+?)</b>(.+?)</p>' ) . findall ( ooo )
 i11i1 = re . compile ( '<title>(.+?)</title>' ) . findall ( ooo ) [ 0 ]
 IIIii1II1II = [ ]
 for i1I1iI , oo0OooOOo0 in iiiIi1i1I :
  o0OO00oO = [ ]
  for I11i1I1I , oO0Oo in re . compile ( '<a href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( oo0OooOOo0 ) :
   Ii1I = { }
   Ii1I [ "url" ] = "http://phim7.com" + I11i1I1I
   Ii1I [ "name" ] = "Part %s - %s" % ( oO0Oo , i11i1 )
   o0OO00oO . append ( Ii1I )
  if "Xem Full" in o0OO00oO [ 0 ] [ "name" ] : del o0OO00oO [ 0 ]
  O00o = { }
  O00o [ "name" ] = i1I1iI
  O00o [ "eps" ] = o0OO00oO
  IIIii1II1II . append ( O00o )
 return IIIii1II1II
 if 54 - 54: IiiIII111iI - ii1IiI1i + iII111iiiii11
@ oo000 . cached ( TTL = 60 )
def ii1I1i1I ( url ) :
 O0o0 = urllib2 . Request ( url )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
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
oO = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.phimvang.org' ) . getAddonInfo ( 'profile' ) )
if 93 - 93: I11i % iiI1i1 . I11i * O0OOo % OOo00O0Oo0oO . i1
if os . path . exists ( oO ) == False :
 os . mkdir ( oO )
iI1ii1Ii = os . path . join ( oO , 'visitor' )
if 92 - 92: o0O
if os . path . exists ( iI1ii1Ii ) == False :
 from random import randint
 i1OOO = open ( iI1ii1Ii , "w" )
 i1OOO . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 i1OOO . close ( )
 if 59 - 59: i1 + iII111iiiii11 * o0O + I1IiiI
def Oo0OoO00oOO0o ( utm_url ) :
 OOO00O = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O0o0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOO00O }
 )
  OO00Oo = urllib2 . urlopen ( O0o0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OO00Oo
 if 84 - 84: iiI1i1 * I11i / Oo - OO0OO0O0O0
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
  IiI1 = "1.0"
  Oo0O00Oo0o0 = open ( iI1ii1Ii ) . read ( )
  O00O0oOO00O00 = "PhimVang.org"
  i1Oo00 = "UA-52209804-2"
  i1i = "www.viettv24.com"
  iiI111I1iIiI = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   II = iiI111I1iIiI + "?" + "utmwv=" + IiI1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00O0oOO00O00 ) + "&utmac=" + i1Oo00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0O00Oo0o0 , "1" , "1" , "2" ] )
   if 45 - 45: OO0OO0O0O0 * IiiIII111iI % OOooOOo * iII111iiiii11 + iIi . o0O
   if 67 - 67: Oo0Ooo - I1IiiI % Ii11111i . OO0OO0O0O0
   if 77 - 77: ooO00oOoo / ii1IiI1i
   if 15 - 15: ooO00oOoo . iiiIIii1IIi . iII111iiiii11 / Oo0Ooo - OOo00O0Oo0oO . I1IiiI
   if 33 - 33: Oo . IiiIII111iI
  else :
   if group == "None" :
    II = iiI111I1iIiI + "?" + "utmwv=" + IiI1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00O0oOO00O00 + "/" + name ) + "&utmac=" + i1Oo00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0O00Oo0o0 , "1" , "1" , "2" ] )
    if 75 - 75: IiiIII111iI % IiiIII111iI . O0OOo
    if 5 - 5: IiiIII111iI * OOo000 + o0O . o0oo0o + o0O
    if 91 - 91: OO0OO0O0O0
    if 61 - 61: i1
    if 64 - 64: OOo000 / o0O - OO0OO0O0O0 - Oo
   else :
    II = iiI111I1iIiI + "?" + "utmwv=" + IiI1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( O00O0oOO00O00 + "/" + group + "/" + name ) + "&utmac=" + i1Oo00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0O00Oo0o0 , "1" , "1" , "2" ] )
    if 86 - 86: Oo % o0O / ii1IiI1i / o0O
    if 42 - 42: I11i
    if 67 - 67: O0OOo . iIi . OO0OO0O0O0
    if 10 - 10: Ii11111i % Ii11111i - iiiIIii1IIi / o0oo0o + OOo00O0Oo0oO
    if 87 - 87: iiI1i1 * Ii11111i + o0oo0o / iiiIIii1IIi / iIi
    if 37 - 37: iIi - OOo000 * iiI1i1 % Oo0Ooo - O0OOo
  print "============================ POSTING ANALYTICS ============================"
  Oo0OoO00oOO0o ( II )
  if 83 - 83: Oo / ii1IiI1i
  if not group == "None" :
   iIIiIi1iIII1 = iiI111I1iIiI + "?" + "utmwv=" + IiI1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( i1i ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + O00O0oOO00O00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( O00O0oOO00O00 ) + "&utmac=" + i1Oo00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , Oo0O00Oo0o0 , "1" , "2" ] )
   if 78 - 78: OO0OO0O0O0 . iiI1i1 . i1 % o0oo0o
   if 49 - 49: OOo00O0Oo0oO / I11i . i1
   if 68 - 68: Oo0Ooo % Ii11111i + Oo0Ooo
   if 31 - 31: i1 . ii1IiI1i
   if 1 - 1: OOooOOo / IiiIII111iI % iIi * ooO00oOoo . Oo0Ooo
   if 2 - 2: Ii11111i * Oo - iiiIIii1IIi + ii1IiI1i . iiI1i1 % iIi
   if 92 - 92: iIi
   if 25 - 25: OOooOOo - ii1IiI1i / iII111iiiii11 / IiiIII111iI
   try :
    print "============================ POSTING TRACK EVENT ============================"
    Oo0OoO00oOO0o ( iIIiIi1iIII1 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 12 - 12: ii1IiI1i * iIi % I1IiiI % iiiIIii1IIi
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 20 - 20: o0oo0o % OOo00O0Oo0oO / OOo00O0Oo0oO + OOo00O0Oo0oO
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
