#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , ast , os , uuid
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.phim14.net"
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
 Oo0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( oO00oOo , "10" , Oooo000o , IiIi11iIIi1Ii ) ) . read ( )
 if "allowed" in Oo0O :
  IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  IiI = xbmc . translatePath ( os . path . join ( IiI , "temp.jpg" ) )
  '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim14.jpg' , IiI )
  ooOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI )
  Oo = xbmcgui . WindowDialog ( )
  Oo . addControl ( ooOo )
  Oo . doModal ( )'''
  if 67 - 67: O00ooOO . I1iII1iiII
  iI1Ii11111iIi = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Theo thể loại' , 'path' : '%s/genres' % ii } ,
 { 'label' : 'Theo Quốc gia' , 'path' : '%s/nations' % ii } ,
 { 'label' : 'Tìm kiếm' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( iI1Ii11111iIi )
 else :
  iI1Ii11111iIi = [
 { 'label' : 'Phim mới' , 'path' : '%s/latest/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-moi/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim lẻ' , 'path' : '%s/movies/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-le/page-%s.html' ) , 1 ) } ,
 { 'label' : 'Phim bộ' , 'path' : '%s/series/%s/%s' % ( ii , urllib . quote_plus ( 'http://m.phim14.net/danh-sach/phim-bo/page-%s.html' ) , 1 ) } ,
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
@ oo000 . route ( '/movies/<murl>/<page>' )
def I1I1i1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'movies' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 18 - 18: iiIIIIi1i1 / OOoOoo00oo - iI1 + OOoOoo00oo % I1iII1iiII - o00ooo0
@ oo000 . route ( '/series/<murl>/<page>' )
def iIIIIiI ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'series' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 91 - 91: OO0OO0O0O0 / Oo0oO0ooo - ii11 + ooO00oOoo % I1IiiI
@ oo000 . route ( '/genres' )
def iI1i ( ) :
 I11i11Ii ( "Browse" , '/genres' )
 iI1Ii11111iIi = [
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
 return oo000 . finish ( iI1Ii11111iIi )
 if 42 - 42: ooO00oOoo / I1IiiI + Oo0Ooo - Oo0o00o0Oo0
@ oo000 . route ( '/genres/<murl>/<page>' )
def oo0Ooo0 ( murl , page = 1 ) :
 I11i11Ii ( "Browse" , '/genres/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'genres' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 46 - 46: iI1 % iI1 - Oo0oO0ooo * o00ooo0 % ii11
@ oo000 . route ( '/nations' )
def OOooO0OOoo ( ) :
 I11i11Ii ( "Browse" , '/nations' )
 iI1Ii11111iIi = [
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
 return oo000 . finish ( iI1Ii11111iIi )
 if 29 - 29: o00ooo0 / iiiIIii1IIi
@ oo000 . route ( '/nations/<murl>/<page>' )
def IiIIIiI1I1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/nations/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'nations' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 86 - 86: Oo0Ooo + Oo0o00o0Oo0 + iI1 * O0OOo + o00ooo0
@ oo000 . route ( '/search/' )
def oOoO ( ) :
 I11i11Ii ( "Browse" , '/search' )
 oOo = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if oOo :
  oOoOoO = "http://m.phim14.net/search/keyword/page-%s.html" . replace ( "keyword" , oOo ) . replace ( " " , "-" )
  ii1I = '%s/search/%s/%s' % ( ii , urllib . quote_plus ( oOoOoO ) , 1 )
  oo000 . redirect ( ii1I )
  if 76 - 76: OO0OO0O0O0 / o00ooo0 . I1iII1iiII * Oo0o00o0Oo0 - ooO00oOoo
@ oo000 . route ( '/search/<murl>/<page>' )
def Oooo ( murl , page ) :
 I11i11Ii ( "Browse" , '/search/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 67 - 67: ooO00oOoo / iII111iiiii11 % O0OOo - iiiIIii1IIi
@ oo000 . route ( '/mirrors/<murl>' )
def Ooo ( murl ) :
 I11i11Ii ( "Browse" , '/mirrors/%s' % ( murl ) )
 iI1Ii11111iIi = [ ]
 for O0o0Oo in Oo00OOOOO ( murl ) :
  O0O = { }
  O0O [ "label" ] = O0o0Oo [ "name" ] . strip ( )
  O00o0OO = str ( uuid . uuid1 ( ) )
  I11i1 = oo000 . get_storage ( O00o0OO )
  I11i1 [ "list" ] = O0o0Oo [ "eps" ]
  O0O [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( O00o0OO ) )
  iI1Ii11111iIi . append ( O0O )
 return oo000 . finish ( iI1Ii11111iIi )
 if 25 - 25: o0OO0 - iiIIIIi1i1 . iII111iiiii11
@ oo000 . route ( '/eps/<eps_list>' )
def I11ii1 ( eps_list ) :
 I11i11Ii ( "Browse" , '/eps' )
 iI1Ii11111iIi = [ ]
 for I11II1i in oo000 . get_storage ( eps_list ) [ "list" ] :
  O0O = { }
  O0O [ "label" ] = I11II1i [ "name" ] . strip ( )
  O0O [ "is_playable" ] = True
  O0O [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( I11II1i [ "url" ] ) )
  iI1Ii11111iIi . append ( O0O )
 return oo000 . finish ( iI1Ii11111iIi )
 if 23 - 23: o00 / o00ooo0 + O0OOo + O0OOo / O00ooOO
@ oo000 . route ( '/play/<url>' )
def iiI1 ( url ) :
 I11i11Ii ( "Play" , '/play/%s' % ( url ) )
 i11Iiii = xbmcgui . DialogProgress ( )
 i11Iiii . create ( 'phim14.net' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( iI ( url ) )
 i11Iiii . close ( )
 del i11Iiii
 if 28 - 28: ooO00oOoo - iiIIIIi1i1 . iiIIIIi1i1 + I1i1iI1i - iII111iiiii11 + OO0OO0O0O0
def iI ( url ) :
 Oo0O = oOoOooOo0o0 ( url )
 print Oo0O
 if "youtube" in Oo0O :
  OOOO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( Oo0O )
  OOO00 = OOOO [ 0 ] [ len ( OOOO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % OOO00
 if ".php?url=" in Oo0O :
  iiiiiIIii = re . compile ( '<source src="(http://.+?.mp4)"' ) . findall ( Oo0O )
  O000OO0 = iiiiiIIii [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   O000OO0 = iiiiiIIii [ 1 ]
  return O000OO0
  if 43 - 43: OOoOoo00oo - OO0OO0O0O0 % I1iII1iiII . O0OOo
def i1IIi11111i ( url , page , route_name ) :
 o00OooOooo = int ( page ) + 1
 Oo0O = oOoOooOo0o0 ( url % page )
 OOOO = re . compile ( '<a href="(http://m.phim14.net/phim/.+?)" class="content-items"><img src="(.+?)" alt="(.+?)"[^>]*><h3>.+?</h3><h4>.+?</h4><ul[^>]*><li>Năm phát hành: (.+?)</li><li>Thể loại: .+?</li></ul><p[^>]*>Trạng thái: (.*?)</p></a>' ) . findall ( Oo0O )
 iI1Ii11111iIi = [ ]
 for O000oo0O , OOOOi11i1 , IIIii1II1II , i1I1iI , oo0OooOOo0 in OOOO :
  O0O = { }
  O0O [ "label" ] = "%s (%s)" % ( IIIii1II1II , oo0OooOOo0 )
  O0O [ "thumbnail" ] = OOOOi11i1
  O0O [ "info" ] = { "year" : i1I1iI }
  O0O [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( O000oo0O . replace ( "/phim/" , "/xem-phim/" ) ) )
  iI1Ii11111iIi . append ( O0O )
 if len ( iI1Ii11111iIi ) == oOOo :
  iI1Ii11111iIi . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , o00OooOooo ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return iI1Ii11111iIi
 if 92 - 92: ii11 . O0OOo + o00ooo0
def Oo00OOOOO ( murl ) :
 Oo0O = oOoOooOo0o0 ( murl )
 OOOO = re . compile ( '<span class="svname">(.+?)</span><span class="svep">(.+?)</span>' ) . findall ( Oo0O )
 IiII1I11i1I1I = re . compile ( '<title>(.+?)</title>' ) . findall ( Oo0O ) [ 0 ]
 oO0Oo = [ ]
 for oOOoo0Oo , o00OO00OoO in OOOO :
  OOOO0OOoO0O0 = [ ]
  for O0Oo000ooO00 , oO0 in re . compile ( '<a[^>]*href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( o00OO00OoO ) :
   I11II1i = { }
   I11II1i [ "url" ] = O0Oo000ooO00
   I11II1i [ "name" ] = "Part %s - %s" % ( oO0 , IiII1I11i1I1I . split ( " | " ) [ 0 ] )
   OOOO0OOoO0O0 . append ( I11II1i )
  O0o0Oo = { }
  O0o0Oo [ "name" ] = oOOoo0Oo
  O0o0Oo [ "eps" ] = OOOO0OOoO0O0
  oO0Oo . append ( O0o0Oo )
 return oO0Oo
 if 45 - 45: Oo0Ooo * O00ooOO % iiiIIii1IIi + o00 - Oo0o00o0Oo0
@ oo000 . cached ( TTL = 60 )
def oOoOooOo0o0 ( url ) :
 iIi1iIiii111 = urllib2 . Request ( url )
 iIi1iIiii111 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 iIi1iIiii111 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 iIi1iIiii111 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 iIi1iIiii111 . add_header ( 'Cookie' , 'location.href=1' )
 iIIIi1 = urllib2 . urlopen ( iIi1iIiii111 )
 iiII1i1 = iIIIi1 . read ( )
 iIIIi1 . close ( )
 if "gzip" in iIIIi1 . info ( ) . getheader ( 'Content-Encoding' ) :
  iiII1i1 = zlib . decompress ( iiII1i1 , 16 + zlib . MAX_WBITS )
 iiII1i1 = '' . join ( iiII1i1 . splitlines ( ) ) . replace ( '\'' , '"' )
 iiII1i1 = iiII1i1 . replace ( '\n' , '' )
 iiII1i1 = iiII1i1 . replace ( '\t' , '' )
 iiII1i1 = re . sub ( '  +' , ' ' , iiII1i1 )
 iiII1i1 = iiII1i1 . replace ( '> <' , '><' )
 return iiII1i1
 if 66 - 66: ooO00oOoo - O0OOo
I1i1III = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.kodi4vn.phim14.net' ) . getAddonInfo ( 'profile' ) )
if 63 - 63: ooO00oOoo % Oo0oO0ooo * Oo0oO0ooo * Oo0ooO0oo0oO / o00
if os . path . exists ( I1i1III ) == False :
 os . mkdir ( I1i1III )
o0ooO = os . path . join ( I1i1III , 'visitor' )
if 98 - 98: ii11 * ii11 / ii11 + O0OOo
if os . path . exists ( o0ooO ) == False :
 from random import randint
 ii111111I1iII = open ( o0ooO , "w" )
 ii111111I1iII . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 ii111111I1iII . close ( )
 if 68 - 68: ii11 - iiiIIii1IIi * Oo0Ooo / o00 * OOoOoo00oo
def i1iIi1iIi1i ( utm_url ) :
 I1I1iIiII1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iIi1iIiii111 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : I1I1iIiII1 }
 )
  iIIIi1 = urllib2 . urlopen ( iIi1iIiii111 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iIIIi1
 if 4 - 4: iI1 + OO0OO0O0O0 * ooO00oOoo
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
  OOoo0O = "1.0"
  Oo0ooOo0o = open ( o0ooO ) . read ( )
  Ii1i1 = "Phim14.net"
  iiIii = "UA-52209804-2"
  ooo0O = "www.viettv24.com"
  oOoO0o00OO0 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1I1ii = oOoO0o00OO0 + "?" + "utmwv=" + OOoo0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Ii1i1 ) + "&utmac=" + iiIii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0ooOo0o , "1" , "1" , "2" ] )
   if 61 - 61: O00ooOO
   if 64 - 64: iI1 / I1i1iI1i - OO0OO0O0O0 - O0OOo
   if 86 - 86: O0OOo % I1i1iI1i / I1iII1iiII / I1i1iI1i
   if 42 - 42: Oo0ooO0oo0oO
   if 67 - 67: OOoOoo00oo . ii11 . OO0OO0O0O0
  else :
   if group == "None" :
    i1I1ii = oOoO0o00OO0 + "?" + "utmwv=" + OOoo0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Ii1i1 + "/" + name ) + "&utmac=" + iiIii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0ooOo0o , "1" , "1" , "2" ] )
    if 10 - 10: o00 % o00 - iiiIIii1IIi / ooO00oOoo + Oo0o00o0Oo0
    if 87 - 87: Oo0oO0ooo * o00 + ooO00oOoo / iiiIIii1IIi / ii11
    if 37 - 37: ii11 - iI1 * Oo0oO0ooo % Oo0Ooo - OOoOoo00oo
    if 83 - 83: O0OOo / I1iII1iiII
    if 34 - 34: iiIIIIi1i1
   else :
    i1I1ii = oOoO0o00OO0 + "?" + "utmwv=" + OOoo0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Ii1i1 + "/" + group + "/" + name ) + "&utmac=" + iiIii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Oo0ooOo0o , "1" , "1" , "2" ] )
    if 57 - 57: Oo0oO0ooo . O0OOo . I1IiiI
    if 42 - 42: O0OOo + o00 % OO0OO0O0O0
    if 6 - 6: Oo0oO0ooo
    if 68 - 68: I1i1iI1i - Oo0ooO0oo0oO
    if 28 - 28: Oo0ooO0oo0oO . ooO00oOoo / ooO00oOoo + o0OO0 . o00
    if 1 - 1: iiiIIii1IIi / O00ooOO
  print "============================ POSTING ANALYTICS ============================"
  i1iIi1iIi1i ( i1I1ii )
  if 33 - 33: O0OOo
  if not group == "None" :
   iI11i1ii11 = oOoO0o00OO0 + "?" + "utmwv=" + OOoo0O + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( ooo0O ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + Ii1i1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( Ii1i1 ) + "&utmac=" + iiIii + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , Oo0ooOo0o , "1" , "2" ] )
   if 58 - 58: Oo0ooO0oo0oO % Oo0Ooo . ii11 / Oo0oO0ooo
   if 84 - 84: ii11 . o00 / o0OO0 - I1iII1iiII / iII111iiiii11 / o00ooo0
   if 12 - 12: I1iII1iiII * ii11 % I1IiiI % iiiIIii1IIi
   if 20 - 20: ooO00oOoo % Oo0o00o0Oo0 / Oo0o00o0Oo0 + Oo0o00o0Oo0
   if 45 - 45: Oo0oO0ooo - iiIIIIi1i1 - iII111iiiii11 - Oo0ooO0oo0oO . O00ooOO / OO0OO0O0O0
   if 51 - 51: OO0OO0O0O0 + ii11
   if 8 - 8: Oo0oO0ooo * I1i1iI1i - Oo0o00o0Oo0 - Oo0ooO0oo0oO * ooO00oOoo % I1iII1iiII
   if 48 - 48: OO0OO0O0O0
   try :
    print "============================ POSTING TRACK EVENT ============================"
    i1iIi1iIi1i ( iI11i1ii11 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 11 - 11: O0OOo + iII111iiiii11 - Oo0ooO0oo0oO / o00ooo0 + o0OO0 . O00ooOO
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 41 - 41: Oo0o00o0Oo0 - OO0OO0O0O0 - OO0OO0O0O0
if __name__ == '__main__' :
 oo000 . run ( ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
