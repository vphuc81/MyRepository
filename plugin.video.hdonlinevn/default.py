#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , cookielib , xmltodict
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.hdonlinevn'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
iiiii = xbmc . translatePath ( os . path . join ( iiiii , "icon.png" ) )
ooo0OO = cookielib . LWPCookieJar ( )
II1 = urllib2 . build_opener ( urllib2 . HTTPCookieProcessor ( ooo0OO ) )
if 64 - 64: Oooo % OOO0O / II1Ii / Ooo
def OoO0O00 ( ) :
 IIiIiII11i ( '[B]Tìm kiếm[/B]' , 'http://m.hdonline.vn/tim-kiem/keyword/trang-1.html' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' , '' )
 IIiIiII11i ( '[B]Phim Lẻ[/B]' , 'http://m.hdonline.vn/danh-sach/phim-le/trang-1.html' , 'index' , iiiii , '' )
 IIiIiII11i ( '[B]Phim Bộ[/B]' , 'http://m.hdonline.vn/danh-sach/phim-bo/trang-1.html' , 'index' , iiiii , '' )
 IIiIiII11i ( '[B]Phim theo Thể Loại[/B]' , '' , '' , iiiii , '' )
 IIiIiII11i ( '--- Kiếm Hiệp' , 'http://m.hdonline.vn/xem-phim-kiem-hiep/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Hành Động' , 'http://m.hdonline.vn/xem-phim-hanh-dong/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phiêu Lưu' , 'http://m.hdonline.vn/xem-phim-phieu-luu/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Kinh Dị' , 'http://m.hdonline.vn/xem-phim-kinh-di/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Tình Cảm' , 'http://m.hdonline.vn/xem-phim-tinh-cam/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Hoạt Hình' , 'http://m.hdonline.vn/xem-phim-hoat-hinh/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Võ Thuật' , 'http://m.hdonline.vn/xem-phim-vo-thuat/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Hài Hước' , 'http://m.hdonline.vn/xem-phim-hai-huoc/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Tâm Lý' , 'http://m.hdonline.vn/xem-phim-tam-ly/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Viễn Tưởng' , 'http://m.hdonline.vn/xem-phim-vien-tuong/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Thần Thoại' , 'http://m.hdonline.vn/xem-phim-than-thoai/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Chiến Tranh' , 'http://m.hdonline.vn/xem-phim-chien-tranh/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Cổ Trang' , 'http://m.hdonline.vn/xem-phim-da-su-co-trang/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Âm Nhạc' , 'http://m.hdonline.vn/xem-phim-the-thao-am-nhac/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Hình Sự' , 'http://m.hdonline.vn/xem-phim-hinh-su/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- TV Show' , 'http://m.hdonline.vn/xem-phim-tv-show/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Khoa Học' , 'http://m.hdonline.vn/xem-phim-khoa-hoc/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Gia Đình' , 'http://m.hdonline.vn/xem-phim-gia-dinh/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Thể Thao' , 'http://m.hdonline.vn/xem-phim-the-thao/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '[B]Phim Bộ theo Quốc Gia[/B]' , '' , '' , iiiii , '' )
 IIiIiII11i ( '--- Phim Việt Nam' , 'http://m.hdonline.vn/phim-bo-viet-nam_1/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Trung Quốc' , 'http://m.hdonline.vn/phim-bo-trung-quoc_2/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Hàn Quốc' , 'http://m.hdonline.vn/phim-bo-han-quoc_3/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Đài Loan' , 'http://m.hdonline.vn/phim-bo-dai-loan_1/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Mỹ' , 'http://m.hdonline.vn/phim-bo-my_5/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Châu Âu' , 'http://m.hdonline.vn/phim-bo-chau-au_6/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Nhật Bản' , 'http://m.hdonline.vn/phim-bo-nhat-ban_7/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Hồng Kông' , 'http://m.hdonline.vn/phim-bo-hong-kong_8/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Thái Lan' , 'http://m.hdonline.vn/phim-bo-thai-lan_9/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Châu Á' , 'http://m.hdonline.vn/phim-bo-chau-a_10/trang-1.html' , 'index' , '' , '' )
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 IIiIiII11i ( '--- Phim Pháp' , 'http://m.hdonline.vn/phim-bo-phap_12/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Anh' , 'http://m.hdonline.vn/phim-bo-anh_13/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Cananda' , 'http://m.hdonline.vn/phim-bo-canada_14/trang-1.html' , 'index' , '' , '' )
 IIiIiII11i ( '--- Phim Đức' , 'http://m.hdonline.vn/phim-bo-duc_15/trang-1.html' , 'index' , '' , '' )
 if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
 IIiIiII11i ( '--- Phim Nga' , 'http://m.hdonline.vn/phim-bo-nga_17/trang-1.html' , 'index' , '' , '' )
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
 O0oOO0o0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: O0oOO0o0 = xbmc . translatePath ( os . path . join ( O0oOO0o0 , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/hdonline.jpg' , O0oOO0o0 )
 if 49 - 49: i1ii1iIII = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , O0oOO0o0 )
 if 49 - 49: Oo0oO0oo0oO00 = xbmcgui . WindowDialog ( )
 if 49 - 49: Oo0oO0oo0oO00 . addControl ( i1ii1iIII )
 if 49 - 49: Oo0oO0oo0oO00 . doModal ( )
 if 8 - 8: OOo00O0Oo0oO / ooO
 IiIiI11iIi = xbmc . getSkinDir ( )
 if IiIiI11iIi == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 1 - 1: IIii11I1 - i1111 - Ooo / o00O0oo . ooO
def I11 ( url ) :
 Oo0o0000o0o0 = oOo0oooo00o ( url )
 oO0o0o0ooO0oO = re . compile ( '<div class="content-items"><a href="(.+?)"[^>]*><img src="(.+?)"[^>]*><h3>(.+?)</h3>.+?<p>(.+?)</p>' ) . findall ( Oo0o0000o0o0 )
 for oo0o0O00 , oO , i1iiIIiiI111 , oooOOOOO in oO0o0o0ooO0oO :
  IIiIiII11i ( i1iiIIiiI111 , oo0o0O00 , 'episodes' , oO , oooOOOOO )
 if ( len ( oO0o0o0ooO0oO ) == 15 ) :
  i1iiIII111ii = int ( re . compile ( 'trang-(\d+).html' ) . findall ( url ) [ 0 ] )
  url = url . replace ( "trang-" + str ( i1iiIII111ii ) + ".html" , "trang-" + str ( i1iiIII111ii + 1 ) + ".html" )
  IIiIiII11i ( 'Next >>' , url , 'index' , '' , '' )
 IiIiI11iIi = xbmc . getSkinDir ( )
 if IiIiI11iIi == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(51)' )
  if 3 - 3: OOo00O0Oo0oO + Oooo
def I1Ii ( url ) :
 o0oOo0Ooo0O = re . compile ( "-(\d+).html" ) . findall ( url ) [ 0 ]
 url = OO00O0O0O00Oo ( "1" , "maWloWtgYJmVoJ-dmp-WX6efYJahmqSglZZgp6menXCXmp2eblakV5yWqpSglZZul5JkkmNql2aWlJdlaJNkZ2mXk2iXZmmTaWKWZWJjY2Q=" ) % o0oOo0Ooo0O
 Oo0o0000o0o0 = oOo0oooo00o ( url )
 IIIiiiiiIii = re . compile ( OO00O0O0O00Oo ( "2" , "bpuml59wWmBdcVtuYZuml59w" ) ) . findall ( Oo0o0000o0o0 )
 for OO in IIIiiiiiIii :
  OO = OO00O0O0O00Oo ( "3" , "b5ynmKBxWKZvYpynmKBx" ) % OO
  oO0O = xmltodict . parse ( OO ) [ "item" ]
  OOoO000O0OO = ""
  if oO0O [ OO00O0O0O00Oo ( "4" , "nqukoJWtmaZuqqSgqZudomKnqZaanaCZ" ) ] != None :
   OOoO000O0OO = oO0O [ "jwplayer:vplugin.subfile" ] . encode ( "utf8" )
  url = iiI1IiI ( oO0O [ OO00O0O0O00Oo ( "11" , "m6ihnZKqlqNrl5qdlg==" ) ] )
  if "m3u8" in url :
   II ( oO0O [ OO00O0O0O00Oo ( "10" , "pZmlnJY=" ) ] . encode ( "utf8" ) , url + OOoO000O0OO , 'loadvideo' , oO0O [ OO00O0O0O00Oo ( "12" , "m6mhnpKrlqRrqKGeppmaoF-bnpOYlw==" ) ] . encode ( "utf8" ) )
   if 57 - 57: IiII
def iI ( url ) :
 try :
  iI11iiiI1II = xbmc . Keyboard ( '' , 'Enter search text' )
  iI11iiiI1II . doModal ( )
  if ( iI11iiiI1II . isConfirmed ( ) ) :
   O0oooo0Oo00 = urllib . quote_plus ( iI11iiiI1II . getText ( ) . replace ( " " , "-" ) )
  url = url . replace ( "keyword" , O0oooo0Oo00 )
  I11 ( url )
 except : pass
 if 17 - 17: OOO0O % i1111 % i11iIiiIii . I1ii11iIi11i
def O0o0Oo ( url , name ) :
 Oo00OOOOO = url . split ( "m3u8" ) [ 0 ] + "m3u8"
 OOoO000O0OO = url . split ( "m3u8" ) [ 1 ] . split ( "," ) [ - 1 ]
 if OOoO000O0OO != "" :
  OOoO000O0OO = OO00O0O0O00Oo ( "13" , "maelo2tiYKBfm5Win5-aoZZhp6FgmpankKamlV-jmaNwqKOfblik" ) % OOoO000O0OO
 O0O = xbmcgui . ListItem ( name )
 O0O . setProperty ( "IsPlayable" , "true" )
 O0O . setPath ( Oo00OOOOO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O0O )
 O00o0OO = xbmc . Player ( )
 if ( OOoO000O0OO != '' ) :
  O0oOO0o0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  O0oOO0o0 = xbmc . translatePath ( os . path . join ( O0oOO0o0 , "temp.sub" ) )
  I11i1 = urllib2 . Request ( OOoO000O0OO )
  iIi1ii1I1 = urllib2 . urlopen ( I11i1 )
  o0 = iIi1ii1I1 . read ( )
  iIi1ii1I1 . close ( )
  with open ( O0oOO0o0 , "w" ) as I11II1i :
   I11II1i . write ( o0 )
   if 23 - 23: iII111i / Ii1I + ooOoO0o + ooOoO0o / oOo0O0Ooo
  O00o0OO . setSubtitles ( O0oOO0o0 )
  if 26 - 26: II1Ii
def IiiI11Iiiii ( url ) :
 Oo0o0000o0o0 = ""
 if os . path . exists ( url ) == True :
  Oo0o0000o0o0 = open ( url ) . read ( )
 else :
  I11i1 = urllib2 . Request ( url )
  I11i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  ii1I1i1I = urllib2 . urlopen ( I11i1 )
  Oo0o0000o0o0 = ii1I1i1I . read ( )
  ii1I1i1I . close ( )
 Oo0o0000o0o0 = '' . join ( Oo0o0000o0o0 . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\n' , '' )
 Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\t' , '' )
 Oo0o0000o0o0 = re . sub ( '  +' , ' ' , Oo0o0000o0o0 )
 Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '> <' , '><' )
 return Oo0o0000o0o0
 if 88 - 88: OOooOOo + Oooo / I11i * OOo00O0Oo0oO
def oOo0oooo00o ( url ) :
 I11i1 = urllib2 . Request ( url )
 I11i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 try :
  ii1I1i1I = II1 . open ( I11i1 )
  if "app.php" in ii1I1i1I . geturl ( ) :
   ii1I1i1I = II1 . open ( I11i1 )
  Oo0o0000o0o0 = ii1I1i1I . read ( )
  ii1I1i1I . close ( )
  Oo0o0000o0o0 = '' . join ( Oo0o0000o0o0 . splitlines ( ) ) . replace ( '\'' , '"' )
  Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\n' , '' )
  Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\t' , '' )
  Oo0o0000o0o0 = re . sub ( '  +' , ' ' , Oo0o0000o0o0 )
  Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '> <' , '><' )
  return Oo0o0000o0o0
 except urllib2 . HTTPError , iiiIi1i1I :
  if iiiIi1i1I . code in [ 404 ] :
   ii1I1i1I = II1 . open ( I11i1 )
   Oo0o0000o0o0 = ii1I1i1I . read ( )
   ii1I1i1I . close ( )
   Oo0o0000o0o0 = '' . join ( Oo0o0000o0o0 . splitlines ( ) ) . replace ( '\'' , '"' )
   Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\n' , '' )
   Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '\t' , '' )
   Oo0o0000o0o0 = re . sub ( '  +' , ' ' , Oo0o0000o0o0 )
   Oo0o0000o0o0 = Oo0o0000o0o0 . replace ( '> <' , '><' )
   return Oo0o0000o0o0
   if 80 - 80: I11i - OOooOOo
def OO00O0O0O00Oo ( k , e ) :
 OOO00 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for iiiiiIIii in range ( len ( e ) ) :
  O000OO0 = k [ iiiiiIIii % len ( k ) ]
  I11iii1Ii = chr ( ( 256 + ord ( e [ iiiiiIIii ] ) - ord ( O000OO0 ) ) % 256 )
  OOO00 . append ( I11iii1Ii )
 return "" . join ( OOO00 )
 if 13 - 13: IIii11I1 % I11i - i11iIiiIii . I1ii11iIi11i + oOo0O0Ooo
def iiI1IiI ( _arg_1 ) :
 import math
 II111ii1II1i = "" ;
 OoOo00o = list ( "1234567890qwertyuiopasdfghjklzxcvbnm" )
 o0OOoo0OO0OOO = len ( OoOo00o )
 iI1iI1I1i1I = len ( _arg_1 )
 iIi11Ii1 = list ( "f909e34e4b4a76f4a8b1eac696bd63c4" )
 Ii11iII1 = list ( _arg_1 [ ( ( o0OOoo0OO0OOO * 2 ) + 32 ) : iI1iI1I1i1I ] )
 Oo0O0O0ooO0O = list ( _arg_1 [ 0 : ( o0OOoo0OO0OOO * 2 ) ] )
 IIIIii = [ ]
 O0o0 = _arg_1 [ ( ( o0OOoo0OO0OOO * 2 ) + 32 ) : iI1iI1I1i1I ]
 OO00Oo = 0
 while ( OO00Oo < ( o0OOoo0OO0OOO * 2 ) ) :
  O0OOO0OOoO0O = ( OoOo00o . index ( Oo0O0O0ooO0O [ OO00Oo ] ) * o0OOoo0OO0OOO )
  O0OOO0OOoO0O = ( O0OOO0OOoO0O + OoOo00o . index ( Oo0O0O0ooO0O [ ( OO00Oo + 1 ) ] ) )
  O00Oo000ooO0 = int ( math . floor ( ( OO00Oo / 2 ) ) % len ( iIi11Ii1 ) )
  str ( iIi11Ii1 [ O00Oo000ooO0 ] ) [ 0 ]
  O0OOO0OOoO0O = ( O0OOO0OOoO0O - ord ( str ( iIi11Ii1 [ O00Oo000ooO0 ] ) [ 0 ] ) )
  IIIIii . append ( chr ( O0OOO0OOoO0O ) )
  OO00Oo = ( OO00Oo + 2 )
  if 100 - 100: Oooo + ooO - I1Ii111 + i11iIiiIii * o00O0oo
 OO00Oo = 0
 while ( OO00Oo < len ( Ii11iII1 ) ) :
  O0OOO0OOoO0O = ( OoOo00o . index ( Ii11iII1 [ OO00Oo ] ) * o0OOoo0OO0OOO )
  O0OOO0OOoO0O = ( O0OOO0OOoO0O + OoOo00o . index ( Ii11iII1 [ ( OO00Oo + 1 ) ] ) )
  O00Oo000ooO0 = int ( ( math . floor ( ( OO00Oo / 2 ) ) % o0OOoo0OO0OOO ) )
  O0OOO0OOoO0O = ( O0OOO0OOoO0O - ord ( str ( IIIIii [ O00Oo000ooO0 ] ) [ 0 ] ) )
  II111ii1II1i = ( II111ii1II1i + chr ( O0OOO0OOoO0O ) )
  OO00Oo = ( OO00Oo + 2 )
 return II111ii1II1i
 if 30 - 30: Ii1I . o00O0oo - II1Ii
def II ( name , url , mode , iconimage ) :
 Ii1iIiii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOO = True
 Oo0oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 Oo0oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Oo0oOOo . setProperty ( "IsPlayable" , "true" )
 OOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1iIiii1 , listitem = Oo0oOOo )
 return OOO
 if 58 - 58: oOo0O0Ooo * I1Ii111 * iII111i / I1Ii111
def IIiIiII11i ( name , url , mode , iconimage , plot ) :
 Ii1iIiii1 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&plot=" + urllib . quote_plus ( plot )
 OOO = True
 Oo0oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : plot } )
 OOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Ii1iIiii1 , listitem = Oo0oOOo , isFolder = True )
 return OOO
 if 75 - 75: IiII
def I1III ( parameters ) :
 OO0O0OoOO0 = { }
 if 10 - 10: II1Ii % OOO0O
 if parameters :
  O00o0O00 = parameters [ 1 : ] . split ( "&" )
  for ii111111I1iII in O00o0O00 :
   O00ooo0O0 = ii111111I1iII . split ( '=' )
   if ( len ( O00ooo0O0 ) ) == 2 :
    OO0O0OoOO0 [ O00ooo0O0 [ 0 ] ] = O00ooo0O0 [ 1 ]
 return OO0O0OoOO0
 if 23 - 23: OOo00O0Oo0oO
oo0oOo = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 89 - 89: I11i
if os . path . exists ( oo0oOo ) == False :
 os . mkdir ( oo0oOo )
OO0oOoOO0oOO0 = os . path . join ( oo0oOo , 'visitor' )
if 86 - 86: I1Ii111
if os . path . exists ( OO0oOoOO0oOO0 ) == False :
 from random import randint
 OOoo0O = open ( OO0oOoOO0oOO0 , "w" )
 OOoo0O . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOoo0O . close ( )
 if 67 - 67: i11iIiiIii - Ooo % iII111i . Oooo
def o0oo ( utm_url ) :
 oooooOoo0ooo = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  I11i1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : oooooOoo0ooo }
 )
  ii1I1i1I = urllib2 . urlopen ( I11i1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return ii1I1i1I
 if 6 - 6: ooOoO0o - o00O0oo + OOO0O - IIii11I1 - i11iIiiIii
def OO0oOO0O ( group , name ) :
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
  oOiIi1IIIi1 = "1.0"
  O0oOoOOOoOO = open ( OO0oOoOO0oOO0 ) . read ( )
  ii1ii11IIIiiI = "HDOnline"
  O00OOOoOoo0O = "UA-52209804-2"
  O000OOo00oo = "www.viettv24.com"
  oo0OOo = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   ooOOO00Ooo = oo0OOo + "?" + "utmwv=" + oOiIi1IIIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ii1ii11IIIiiI ) + "&utmac=" + O00OOOoOoo0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0oOoOOOoOO , "1" , "1" , "2" ] )
   if 16 - 16: oOo0O0Ooo % I11i - oOo0O0Ooo + o00O0oo
   if 12 - 12: I1Ii111 / I1Ii111 + i11iIiiIii
   if 40 - 40: I1ii11iIi11i . OOO0O / I1ii11iIi11i / i11iIiiIii
   if 75 - 75: ooOoO0o + Ii1I
   if 84 - 84: ooO . i11iIiiIii . ooO * iII111i - ooOoO0o
  else :
   if group == "None" :
    ooOOO00Ooo = oo0OOo + "?" + "utmwv=" + oOiIi1IIIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ii1ii11IIIiiI + "/" + name ) + "&utmac=" + O00OOOoOoo0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0oOoOOOoOO , "1" , "1" , "2" ] )
    if 42 - 42: i11iIiiIii
    if 33 - 33: OOo00O0Oo0oO - Oooo * Ooo * Ii1I - oO0o
    if 32 - 32: II1Ii / OOO0O - Ii1I
    if 91 - 91: OOo00O0Oo0oO % Ooo % OOO0O
    if 20 - 20: I1Ii111 % o00O0oo / o00O0oo + o00O0oo
   else :
    ooOOO00Ooo = oo0OOo + "?" + "utmwv=" + oOiIi1IIIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( ii1ii11IIIiiI + "/" + group + "/" + name ) + "&utmac=" + O00OOOoOoo0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0oOoOOOoOO , "1" , "1" , "2" ] )
    if 45 - 45: IiII - ooO - II1Ii - OOooOOo . oOo0O0Ooo / Oooo
    if 51 - 51: Oooo + OOo00O0Oo0oO
    if 8 - 8: IiII * I11i - o00O0oo - OOooOOo * I1Ii111 % I1ii11iIi11i
    if 48 - 48: Oooo
    if 11 - 11: ooOoO0o + II1Ii - OOooOOo / Ii1I + oO0o . oOo0O0Ooo
    if 41 - 41: o00O0oo - Oooo - Oooo
  print "============================ POSTING ANALYTICS ============================"
  o0oo ( ooOOO00Ooo )
  if 68 - 68: I1Ii111 % IIii11I1
  if not group == "None" :
   ooO00OO0 = oo0OOo + "?" + "utmwv=" + oOiIi1IIIi1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O000OOo00oo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + ii1ii11IIIiiI + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( ii1ii11IIIiiI ) + "&utmac=" + O00OOOoOoo0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O0oOoOOOoOO , "1" , "2" ] )
   if 31 - 31: OOo00O0Oo0oO % OOo00O0Oo0oO % ooOoO0o
   if 69 - 69: OOooOOo - oO0o + Ooo / IIii11I1
   if 49 - 49: Oooo . OOo00O0Oo0oO
   if 11 - 11: ooO * I1ii11iIi11i . OOO0O % II1Ii + OOo00O0Oo0oO
   if 78 - 78: OOooOOo . I1Ii111 + OOooOOo / ooOoO0o / OOooOOo
   if 54 - 54: I11i % OOo00O0Oo0oO
   if 37 - 37: I11i * oO0o / i1111 - OOo00O0Oo0oO % oOo0O0Ooo . IiII
   if 88 - 88: OOo00O0Oo0oO . oOo0O0Ooo * oOo0O0Ooo % IIii11I1
   try :
    print "============================ POSTING TRACK EVENT ============================"
    o0oo ( ooO00OO0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 15 - 15: Ooo * I1ii11iIi11i + i11iIiiIii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 6 - 6: i1111 / i11iIiiIii + OOo00O0Oo0oO * IiII
o00o0 = I1III ( sys . argv [ 2 ] )
ii = o00o0 . get ( 'mode' )
OOooooO0Oo = o00o0 . get ( 'url' )
OOiIiIIi1 = o00o0 . get ( 'name' )
oooOOOOO = o00o0 . get ( 'plot' )
if type ( OOooooO0Oo ) == type ( str ( ) ) :
 OOooooO0Oo = urllib . unquote_plus ( OOooooO0Oo )
if type ( OOiIiIIi1 ) == type ( str ( ) ) :
 OOiIiIIi1 = urllib . unquote_plus ( OOiIiIIi1 )
if type ( oooOOOOO ) == type ( str ( ) ) :
 OOiIiIIi1 = urllib . unquote_plus ( oooOOOOO )
I1IIII1i = str ( sys . argv [ 1 ] )
if ii == 'index' :
 OO0oOO0O ( "Browse" , OOiIiIIi1 )
 I11 ( OOooooO0Oo )
elif ii == 'episodes' :
 OO0oOO0O ( "Browse" , OOiIiIIi1 )
 I1Ii ( OOooooO0Oo )
elif ii == 'search' :
 OO0oOO0O ( "None" , "Search" )
 iI ( OOooooO0Oo )
elif ii == 'loadvideo' :
 OO0oOO0O ( "Play" , OOiIiIIi1 + "/" + OOooooO0Oo )
 I1I11i = xbmcgui . DialogProgress ( )
 I1I11i . create ( 'HDOnline' , 'Loading video. Please wait...' )
 O0o0Oo ( OOooooO0Oo , OOiIiIIi1 )
 I1I11i . close ( )
 del I1I11i
else :
 OO0oOO0O ( "None" , "None" )
 OoO0O00 ( )
xbmcplugin . endOfDirectory ( int ( I1IIII1i ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
