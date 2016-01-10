#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , zlib , os , uuid , requests
from operator import itemgetter
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
# while True :
 # Oooo000o = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  #if not any ( b in Oooo000o for b in OOOo0 ) : break
 #while True :
  #IiIi11iIIi1Ii = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  #if not any ( b in IiIi11iIIi1Ii for b in OOOo0 ) : break
 #try :
  #oO00oOo = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 #except :
  #while True :
  # oO00oOo = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   #if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , oO00oOo . lower ( ) ) : break
 #Oo0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( oO00oOo , "10" , Oooo000o , IiIi11iIIi1Ii ) ) . read ( )
 if True :
  IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  #IiI = xbmc . translatePath ( os . path . join ( IiI , "temp.jpg" ) )
  #urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/phim14.jpg' , IiI )
  #ooOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI )
  #Oo = xbmcgui . WindowDialog ( )
  #Oo . addControl ( ooOo )
  #Oo . doModal ( )
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
  i1i1II = xbmcgui . Dialog ( )
  i1i1II . ok ( "Chú ý" , Oo0O )
  if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
  if 56 - 56: ooO00oOoo - O0OOo
@ oo000 . route ( '/latest/<murl>/<page>' )
def II1Iiii1111i ( murl , page ) :
 I11i11Ii ( "Browse" , '/latest/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'latest' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 74 - 74: Oo0o00o0Oo0 * ii11
@ oo000 . route ( '/movies/<murl>/<page>' )
def I1I1i1 ( murl , page ) :
 I11i11Ii ( "Browse" , '/movies/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'movies' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
 else :
  return oo000 . finish ( iI1Ii11111iIi )
  if 18 - 18: iiIIIIi1i1 / OOoOoo00oo - iI1 + OOoOoo00oo % I1iII1iiII - o00ooo0
@ oo000 . route ( '/series/<murl>/<page>' )
def iIIIIiI ( murl , page ) :
 I11i11Ii ( "Browse" , '/series/%s/%s' % ( murl , page ) )
 iI1Ii11111iIi = i1IIi11111i ( murl , page , 'series' )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
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
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
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
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
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
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return oo000 . finish ( iI1Ii11111iIi )
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
 i11Iiii . create ( 'Phim14' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( iI ( url ) )
 i11Iiii . close ( )
 del i11Iiii
 if 28 - 28: ooO00oOoo - iiIIIIi1i1 . iiIIIIi1i1 + I1i1iI1i - iII111iiiii11 + OO0OO0O0O0
def iI ( url ) :
 Oo0O = oOoOooOo0o0 ( url )
 OOOO = ""
 if "youtube" in Oo0O :
  OOO00 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( Oo0O )
  iiiiiIIii = OOO00 [ 0 ] [ len ( OOO00 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % iiiiiIIii
 if '{link:"' in Oo0O :
  O000OO0 = re . compile ( '<script type="text/javascript" src="(http://player\d+.phim14.net/.+?)"></script>' ) . findall ( Oo0O ) [ 0 ] . replace ( "gkpluginsphp.js" , "gkpluginsphp.php" )
  OOOO = re . compile ( '\{link:"(.+?)"' ) . findall ( Oo0O ) [ 0 ]
  I11iii1Ii = requests . post (
 O000OO0 ,
 data = { 'link' : OOOO , 'f' : 'true' }
 ) . json ( )
  if "list" in I11iii1Ii :
   I11iii1Ii = sorted ( I11iii1Ii [ "list" ] [ 0 ] [ "link" ] , key = itemgetter ( 'link' ) )
   I1IIiiIiii = I11iii1Ii [ 0 ] [ "link" ]
   if oo000 . get_setting ( 'HQ' , bool ) :
    I1IIiiIiii = I11iii1Ii [ - 1 ] [ "link" ]
  else :
   I11iii1Ii = sorted ( I11iii1Ii [ "link" ] , key = itemgetter ( 'link' ) )
   I1IIiiIiii = I11iii1Ii [ 0 ] [ "link" ]
   if oo000 . get_setting ( 'HQ' , bool ) :
    I1IIiiIiii = I11iii1Ii [ - 1 ] [ "link" ]
 else :
  OOOO = re . compile ( '<source src="(.+?)" type="video/mp4"' ) . findall ( Oo0O )
  I1IIiiIiii = OOOO [ 0 ]
  if oo000 . get_setting ( 'HQ' , bool ) :
   I1IIiiIiii = OOOO [ - 1 ]
 return I1IIiiIiii
 if 97 - 97: iI1 - ooO00oOoo * Oo0Ooo / I1i1iI1i % OOoOoo00oo - iII111iiiii11
def i1IIi11111i ( url , page , route_name ) :
 OoOo00o = int ( page ) + 1
 Oo0O = oOoOooOo0o0 ( url % page )
 OOO00 = re . compile ( '<a href="(http://m.phim14.net/phim/.+?)" class="content-items"><img src="(.+?)" alt="(.+?)"[^>]*><h3>.+?</h3><h4>.+?</h4><ul[^>]*><li>Năm phát hành: (.+?)</li><li>Thể loại: .+?</li></ul><p[^>]*>Trạng thái: (.*?)</p></a>' ) . findall ( Oo0O )
 iI1Ii11111iIi = [ ]
 for OOOO , o0OOoo0OO0OOO , iI1iI1I1i1I , iIi11Ii1 , Ii11iII1 in OOO00 :
  O0O = { }
  O0O [ "label" ] = "%s (%s)" % ( iI1iI1I1i1I , Ii11iII1 )
  O0O [ "thumbnail" ] = o0OOoo0OO0OOO
  O0O [ "info" ] = { "year" : iIi11Ii1 }
  O0O [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( OOOO . replace ( "/phim/" , "/xem-phim/" ) ) )
  iI1Ii11111iIi . append ( O0O )
 if len ( iI1Ii11111iIi ) == oOOo :
  iI1Ii11111iIi . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , OoOo00o ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return iI1Ii11111iIi
 if 51 - 51: O00ooOO * Oo0ooO0oo0oO % o00ooo0 * O00ooOO % o00 / iI1
def Oo00OOOOO ( murl ) :
 Oo0O = oOoOooOo0o0 ( murl )
 OOO00 = re . compile ( '<span class="svname">(.+?)</span><span class="svep">(.+?)</span>' ) . findall ( Oo0O )
 iIIIIii1 = re . compile ( '<title>(.+?)</title>' ) . findall ( Oo0O ) [ 0 ]
 oo000OO00Oo = [ ]
 for O0OOO0OOoO0O , O00Oo000ooO0 in OOO00 :
  OoO0O00 = [ ]
  for IIiII , o0 in re . compile ( '<a[^>]*href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( O00Oo000ooO0 ) :
   I11II1i = { }
   I11II1i [ "url" ] = IIiII
   I11II1i [ "name" ] = "Part %s - %s" % ( o0 , iIIIIii1 . split ( " | " ) [ 0 ] )
   OoO0O00 . append ( I11II1i )
  O0o0Oo = { }
  O0o0Oo [ "name" ] = O0OOO0OOoO0O
  O0o0Oo [ "eps" ] = OoO0O00
  oo000OO00Oo . append ( O0o0Oo )
 return oo000OO00Oo
 if 62 - 62: iiiIIii1IIi * I1i1iI1i
 if 26 - 26: ii11 . OOoOoo00oo
def oOoOooOo0o0 ( url ) :
 oOOOOo0 = urllib2 . Request ( url )
 oOOOOo0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 oOOOOo0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 oOOOOo0 . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 oOOOOo0 . add_header ( 'Cookie' , 'location.href=1' )
 iiII1i1 = urllib2 . urlopen ( oOOOOo0 )
 o00oOO0o = iiII1i1 . read ( )
 iiII1i1 . close ( )
 if "gzip" in iiII1i1 . info ( ) . getheader ( 'Content-Encoding' ) :
  o00oOO0o = zlib . decompress ( o00oOO0o , 16 + zlib . MAX_WBITS )
 o00oOO0o = '' . join ( o00oOO0o . splitlines ( ) ) . replace ( '\'' , '"' )
 o00oOO0o = o00oOO0o . replace ( '\n' , '' )
 o00oOO0o = o00oOO0o . replace ( '\t' , '' )
 o00oOO0o = re . sub ( '  +' , ' ' , o00oOO0o )
 o00oOO0o = o00oOO0o . replace ( '> <' , '><' )
 return o00oOO0o
 if 80 - 80: Oo0oO0ooo + ooO00oOoo - ooO00oOoo % ii11
OoOO0oo0o = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.phim14.net' ) . getAddonInfo ( 'profile' ) )
if 14 - 14: o00ooo0 * ii11 * ii11 / I1i1iI1i
if os . path . exists ( OoOO0oo0o ) == False :
 os . mkdir ( OoOO0oo0o )
Oo0o00 = os . path . join ( OoOO0oo0o , 'visitor' )
if 73 - 73: ii11 * Oo0o00o0Oo0 + o00ooo0 . ooO00oOoo + o00 % ii11
if os . path . exists ( Oo0o00 ) == False :
 from random import randint
 oo0O = open ( Oo0o00 , "w" )
 oo0O . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oo0O . close ( )
 if 92 - 92: ii11 . OOoOoo00oo
def i1i ( utm_url ) :
 iiI111I1iIiI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  oOOOOo0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : iiI111I1iIiI }
 )
  iiII1i1 = urllib2 . urlopen ( oOOOOo0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iiII1i1
 if 41 - 41: o0OO0 . iI1 + OO0OO0O0O0 * o00ooo0 % o0OO0 * o0OO0
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
  iIIIIi1iiIi1 = "1.0"
  iii1i1iiiiIi = open ( Oo0o00 ) . read ( )
  Iiii = "Phim14.net"
  OO0OoO0o00 = "UA-52209804-2"
  ooOO0O0ooOooO = "www.HDTVblackbox.com"
  oOOOo00O00oOo = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iiIIIi = oOOOo00O00oOo + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Iiii ) + "&utmac=" + OO0OoO0o00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
   if 93 - 93: ii11
   if 10 - 10: O0OOo
   if 82 - 82: o00 - iiiIIii1IIi / ooO00oOoo + Oo0o00o0Oo0
   if 87 - 87: Oo0oO0ooo * o00 + ooO00oOoo / iiiIIii1IIi / ii11
   if 37 - 37: ii11 - iI1 * Oo0oO0ooo % Oo0Ooo - OOoOoo00oo
  else :
   if group == "None" :
    iiIIIi = oOOOo00O00oOo + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Iiii + "/" + name ) + "&utmac=" + OO0OoO0o00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
    if 83 - 83: O0OOo / I1iII1iiII
    if 34 - 34: iiIIIIi1i1
    if 57 - 57: Oo0oO0ooo . O0OOo . I1IiiI
    if 42 - 42: O0OOo + o00 % OO0OO0O0O0
    if 6 - 6: Oo0oO0ooo
   else :
    iiIIIi = oOOOo00O00oOo + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Iiii + "/" + group + "/" + name ) + "&utmac=" + OO0OoO0o00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iii1i1iiiiIi , "1" , "1" , "2" ] )
    if 68 - 68: I1i1iI1i - Oo0ooO0oo0oO
    if 28 - 28: Oo0ooO0oo0oO . ooO00oOoo / ooO00oOoo + o0OO0 . o00
    if 1 - 1: iiiIIii1IIi / O00ooOO
    if 33 - 33: O0OOo
    if 18 - 18: o00ooo0 % ii11 * OO0OO0O0O0
    if 87 - 87: Oo0Ooo
  print "============================ POSTING ANALYTICS ============================"
  i1i ( iiIIIi )
  if 93 - 93: o00 - Oo0ooO0oo0oO % Oo0Ooo . ii11 / ii11 - OOoOoo00oo
  if not group == "None" :
   IIII = oOOOo00O00oOo + "?" + "utmwv=" + iIIIIi1iiIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( ooOO0O0ooOooO ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + Iiii + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( Iiii ) + "&utmac=" + OO0OoO0o00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , iii1i1iiiiIi , "1" , "2" ] )
   if 32 - 32: iII111iiiii11 / iiiIIii1IIi - o00ooo0
   if 91 - 91: ii11 % I1IiiI % iiiIIii1IIi
   if 20 - 20: ooO00oOoo % Oo0o00o0Oo0 / Oo0o00o0Oo0 + Oo0o00o0Oo0
   if 45 - 45: Oo0oO0ooo - iiIIIIi1i1 - iII111iiiii11 - Oo0ooO0oo0oO . O00ooOO / OO0OO0O0O0
   if 51 - 51: OO0OO0O0O0 + ii11
   if 8 - 8: Oo0oO0ooo * I1i1iI1i - Oo0o00o0Oo0 - Oo0ooO0oo0oO * ooO00oOoo % I1iII1iiII
   if 48 - 48: OO0OO0O0O0
   if 11 - 11: O0OOo + iII111iiiii11 - Oo0ooO0oo0oO / o00ooo0 + o0OO0 . O00ooOO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    i1i ( IIII )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 41 - 41: Oo0o00o0Oo0 - OO0OO0O0O0 - OO0OO0O0O0
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 68 - 68: ooO00oOoo % OOoOoo00oo
if __name__ == '__main__' :
 oo000 . run ( ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
