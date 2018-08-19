#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver , HTMLParser , string
oo000 = HTMLParser . HTMLParser ( )
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
oooo = 'plugin.video.xomgiaitri'
iIIii1IIi = xbmcaddon . Addon ( oooo )
o0OO00 = int ( sys . argv [ 1 ] )
if 78 - 78: i11i . oOooOoO0Oo0O
def iI1 ( source ) :
 source = source . replace ( ' ' , '' )
 if 43 - 43: I11i11Ii
 if re . search ( 'eval\(function\(p,a,c,k,e,' , source ) : return True
 else : return False
 if 65 - 65: i1iIi11iIIi1I
def Oo ( source ) :
 I1ii11iIi11i , I1IiI , o0OOO , iIiiiI = Iii1ii1II11i ( source )
 if 10 - 10: I1iII1iiII + I1Ii111 / OOo
 if 41 - 41: I1II1
 if iIiiiI != len ( I1IiI ) :
  raise Ooo0OO0oOO ( 'Malformed p.a.c.k.e.r. symtab.' )
  if 86 - 86: oO0o
 try :
  IIII = Oo0oO0oo0oO00 ( o0OOO )
 except TypeError :
  raise Ooo0OO0oOO ( 'Unknown p.a.c.k.e.r. encoding.' )
  if 8 - 8: OOo00O0Oo0oO / ooO
 def IiIiI11iIi ( match ) :
  Ii1IIii11 = match . group ( 0 )
  if 55 - 55: i1111 - i1IIi11111i / I11i1i11i1I % oo / OOO0O / oo0ooO0oOOOOo
  return I1IiI [ IIII ( Ii1IIii11 ) ] or Ii1IIii11
  if 71 - 71: OOO0O
 source = re . sub ( r'\b\w+\b' , IiIiI11iIi , I1ii11iIi11i )
 return O0OoOoo00o ( source )
 if 31 - 31: I11i11Ii + I1Ii111 . OOO0O
def Iii1ii1II11i ( source ) :
 OoOooOOOO = ( r"}\('(.*)', *(\d+), *(\d+), *'(.*?)'\.split\('\|'\)" )
 if 45 - 45: OOO0O + i1IIi11111i
 iII111ii = re . search ( OoOooOOOO , source , re . DOTALL ) . groups ( )
 if 3 - 3: I11i1i11i1I + o0o00Oo0O
 try :
  return iII111ii [ 0 ] , iII111ii [ 3 ] . split ( '|' ) , int ( iII111ii [ 1 ] ) , int ( iII111ii [ 2 ] )
 except ValueError :
  raise Ooo0OO0oOO ( 'Corrupted p.a.c.k.e.r. data.' )
  if 42 - 42: ooO / oOooOoO0Oo0O + Ii - i1IIi11111i
def O0OoOoo00o ( source ) :
 oo0Ooo0 = re . search ( r'var *(_\w+)\=\["(.*?)"\];' , source , re . DOTALL )
 if 46 - 46: oo0ooO0oOOOOo % oo0ooO0oOOOOo - OOo00O0Oo0oO * I1II1 % I11i1i11i1I
 if 55 - 55: OOo % oOooOoO0Oo0O / i1IIi11111i - OOo00O0Oo0oO - o0o00Oo0O / I11i11Ii
 if oo0Ooo0 :
  iii11iII , i1I111I = oo0Ooo0 . groups ( )
  i11I1IIiiIi = len ( oo0Ooo0 . group ( 0 ) )
  IiIiI11iIi = i1I111I . split ( '","' )
  IiIiIi = '%s[%%d]' % iii11iII
  for II , iI in enumerate ( IiIiI11iIi ) :
   source = source . replace ( IiIiIi % II , '"%s"' % iI )
  return source [ i11I1IIiiIi : ]
 return source
 if 22 - 22: I1iII1iiII % i1IIi11111i
 if 84 - 84: Ii . I1II1
class Oo0oO0oo0oO00 ( object ) :
 ALPHABET = {
 # ooO + ooO % OOO0O % Ii / iI11I1II1I1I . ooO
 # ooO / i11i % i1111 - iI11I1II1I1I
 52 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP' ,
 54 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR' ,
 62 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' ,
 95 : ( ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' )
 }
 if 82 - 82: Ii . ooO / I1iII1iiII * o0o00Oo0O % OOo00O0Oo0oO % iI11I1II1I1I
 def __init__ ( self , base ) :
  self . base = base
  if 78 - 78: iI11I1II1I1I - i1IIi11111i * I1Ii111 + I1II1 + I11i1i11i1I + I11i1i11i1I
  if 11 - 11: I11i1i11i1I - I1Ii111 % oo0ooO0oOOOOo % I11i1i11i1I / OOo - I1Ii111
  if 2 <= base <= 36 :
   self . unbase = lambda o0o0oOOOo0oo : int ( string , base )
  else :
   if 80 - 80: i1111 * Ii / OOO0O
   try :
    self . dictionary = dict ( ( cipher , index ) for
 index , cipher in enumerate ( self . ALPHABET [ base ] ) )
   except KeyError :
    raise TypeError ( 'Unsupported base encoding.' )
    if 9 - 9: i1IIi11111i + OOo00O0Oo0oO % i1IIi11111i + oOooOoO0Oo0O . ooO
   self . unbase = self . _dictunbaser
   if 31 - 31: I1II1 + i1111 + i1111 / I11i11Ii
 def __call__ ( self , string ) :
  return self . unbase ( string )
  if 26 - 26: i11i
 def _dictunbaser ( self , string ) :
  IiiI11Iiiii = 0
  if 18 - 18: I1II1
  for II , I1i1I1II in enumerate ( string [ : : - 1 ] ) :
   IiiI11Iiiii += ( self . base ** II ) * self . dictionary [ I1i1I1II ]
  return IiiI11Iiiii
  if 45 - 45: OOO0O . OOo
class Ooo0OO0oOO ( Exception ) :
 pass
 if 83 - 83: OOo00O0Oo0oO . iI11I1II1I1I . oO0o
 if 31 - 31: i1IIi11111i . i1IIi11111i - I1II1 / I1Ii111 + oo0ooO0oOOOOo * i1iIi11iIIi1I
 if 63 - 63: OOO0O % oOooOoO0Oo0O / i11i - i11i
def iIii11I ( ) :
 OOO0OOO00oo ( 'Search' , 'http://www.xomphimbo.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 OOO0OOO00oo ( 'Phim Lẻ' , 'http://www.xomphimbo.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 OOO0OOO00oo ( 'Phim Bộ' , 'http://www.xomphimbo.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 OOO0OOO00oo ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomphimbo.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 OOO0OOO00oo ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomphimbo.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 if 31 - 31: I11i11Ii - ooO . OOO0O % OOo - o0o00Oo0O
 iii11 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 iii11 = xbmc . translatePath ( os . path . join ( iii11 , "temp.jpg.bak" ) )
 urllib . urlretrieve ( 'http://drive.google.com/uc?export=jpg&id=0B-ygKtjD8Sc-OUxwbVR5ZzZsbFJFT3A5aS04YlJkdDJtQ3BF.bak' , iii11 )
 O0oo0OO0oOOOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , iii11 )
 i1i1i11IIi = xbmcgui . WindowDialog ( )
 i1i1i11IIi . addControl ( O0oo0OO0oOOOo )
 #i1i1i11IIi . doModal ( )
 if 33 - 33: I1II1 + ooO * I1Ii111 - I1iII1iiII / OOo00O0Oo0oO % i1IIi11111i
def II1i1IiiIIi11 ( ) :
 OOO0OOO00oo ( "Hồng Kong" , "http://www.xomphimbo.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 OOO0OOO00oo ( "Hồng Kong (VNLT)" , "http://www.xomphimbo.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 OOO0OOO00oo ( "Hàn Quốc" , "http://www.xomphimbo.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 OOO0OOO00oo ( "Hàn Quốc (vietsub)" , "http://www.xomphimbo.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 OOO0OOO00oo ( "Trung Quốc" , "http://www.xomphimbo.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 OOO0OOO00oo ( "Đài Loan" , "http://www.xomphimbo.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 OOO0OOO00oo ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 OOO0OOO00oo ( "Thái Lan" , "http://www.xomphimbo.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 OOO0OOO00oo ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 47 - 47: I11i1i11i1I
def Ii11iII1 ( ) :
 OOO0OOO00oo ( "Hành Động" , "http://www.xomphimbo.com/xem/category/8/hanh-dong.html" , "index" , "" )
 OOO0OOO00oo ( "Tình Cảm" , "http://www.xomphimbo.com/xem/category/9/tinh-cam.html" , "index" , "" )
 OOO0OOO00oo ( "Phim Hài" , "http://www.xomphimbo.com/xem/category/10/phim-hai.html" , "index" , "" )
 OOO0OOO00oo ( "Kinh Dị" , "http://www.xomphimbo.com/xem/category/11/kinh-di.html" , "index" , "" )
 OOO0OOO00oo ( "Kiếm Hiệp" , "http://www.xomphimbo.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 OOO0OOO00oo ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/15/viet-nam.html" , "index" , "" )
 OOO0OOO00oo ( "Hài Kịch" , "http://www.xomphimbo.com/xem/category/16/hai-kich.html" , "index" , "" )
 OOO0OOO00oo ( "Ca Nhạc" , "http://www.xomphimbo.com/xem/category/17/ca-nhac.html" , "index" , "" )
 OOO0OOO00oo ( "Cải Lương" , "http://www.xomphimbo.com/xem/category/18/cai-luong.html" , "index" , "" )
 OOO0OOO00oo ( "Phóng Sự" , "http://www.xomphimbo.com/xem/category/19/phong-su.html" , "index" , "" )
 OOO0OOO00oo ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 51 - 51: I11i11Ii * I1Ii111 % I1II1 * I11i11Ii % oO0o / oo0ooO0oOOOOo
def iIIIIii1 ( url ) :
 oo000OO00Oo = O0OOO0OOoO0O ( url )
 O00Oo000ooO0 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( oo000OO00Oo )
 for OoO0O00 , IIiII , o0 in O00Oo000ooO0 :
  o0 = o0 . replace ( "xomgiaitri.com" , "mythugian.net" )
  o0 = o0 . replace ( "www." , "" )
  o0 = "/" . join ( o0 . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( o0 . split ( "/" ) [ - 1 ] )
  OOO0OOO00oo ( "[B]" + IIiII + "[/B]" , "http://www.xomphimbo.com/xem" + OoO0O00 , 'mirrors' , o0 )
 ooOooo000oOO = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( oo000OO00Oo . replace ( "'" , '"' ) )
 for OoO0O00 , Oo0oOOo in ooOooo000oOO :
  OOO0OOO00oo ( Oo0oOOo , OoO0O00 . replace ( "./" , "http://www.xomphimbo.com/xem/" ) , 'index' , "" )
  if 58 - 58: I11i11Ii * ooO * oO0o / ooO
def oO0o0OOOO ( ) :
 try :
  O0O0OoOO0 = xbmc . Keyboard ( '' , 'Enter search text' )
  O0O0OoOO0 . doModal ( )
  if 10 - 10: i11i % iI11I1II1I1I
  if ( O0O0OoOO0 . isConfirmed ( ) ) :
   O00o0O00 = urllib . quote_plus ( O0O0OoOO0 . getText ( ) )
  iIIIIii1 ( ii111111I1iII % O00o0O00 )
 except : pass
 if 68 - 68: I11i1i11i1I - iI11I1II1I1I * Ii / oO0o * OOO0O
def i1iIi1iIi1i ( url ) :
 I1I1iIiII1 = i11i1I1 ( url )
 oo000OO00Oo = O0OOO0OOoO0O ( I1I1iIiII1 )
 ii1I = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( oo000OO00Oo )
 if 67 - 67: Ii - oOooOoO0Oo0O % oO0o . o0o00Oo0O
 if "VIP A : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP A : " ) ) )
 if "VIP D : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP D : " ) ) )
 if "VIP B : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP B : " ) ) )
 if "VIP M : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP M : " ) ) )
 if "VIP G : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP G : " ) ) )
 if "VIP Ama : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP Ama : " ) ) )
 if "VIP OK : " in ii1I :
  ii1I . insert ( 0 , ii1I . pop ( ii1I . index ( "VIP OK : " ) ) )
 for o0oo in range ( len ( ii1I ) ) :
  oooooOoo0ooo = [ "Flv :" ]
  if not any ( x in ii1I [ o0oo ] for x in oooooOoo0ooo ) :
   OOO0OOO00oo ( "[%d] - %s" % ( o0oo + 1 , ii1I [ o0oo ] ) , I1I1iIiII1 . encode ( "utf-8" ) , 'episodes' , "" )
   if 6 - 6: i1111 - i1IIi11111i + iI11I1II1I1I - OOO0O - Ii
def OO0oOO0O ( url , name ) :
 oo000OO00Oo = O0OOO0OOoO0O ( url )
 if 91 - 91: o0o00Oo0O
 name = name . split ( "] - " ) [ 1 ]
 oOOo0 = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % name ) . findall ( oo000OO00Oo )
 oo00O00oO = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( oOOo0 [ 0 ] )
 if ( "episode_bg_2" in oOOo0 [ 0 ] ) :
  iIiIIIi = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( oOOo0 [ 0 ] )
  ooo00OOOooO ( "Part - " + iIiIIIi [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf8" ) , url , 'loadvideo' , '' , name )
 for O00OOOoOoo0O , O000OOo00oo in oo00O00oO :
  ooo00OOOooO ( "Part - " + O000OOo00oo . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomphimbo.com/xem/" + O00OOOoOoo0O , 'loadvideo' , '' , name )
  if 71 - 71: Ii + oo
def i11i1I1 ( url ) :
 oOo = O0OOO0OOoO0O ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( oOo ) [ 0 ]
 if 75 - 75: i1iIi11iIIi1I + I1iII1iiII
def OoooO0oO ( url , name ) :
 i1iIi = xbmcgui . ListItem ( name )
 oo000OO00Oo = O0OOO0OOoO0O ( url )
 if "proxy.link" in oo000OO00Oo :
  oo0Ooo0 = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( oo000OO00Oo )
  oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 [ 0 ] )
 oo0Ooo0 = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( oo000OO00Oo )
 if ( len ( oo0Ooo0 ) == 0 ) :
  ooOOoooooo = None
  II1I = re . compile ( 'file\: "(.+?)"' ) . findall ( oo000OO00Oo )
  if 'iframe src="http://play.mythugian.net/' in oo000OO00Oo :
   oo0Ooo0 = re . compile ( 'iframe src="(http://play.mythugian.net/.+?)"' ) . findall ( oo000OO00Oo )
   oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 [ 0 ] )
   oo0Ooo0 = re . compile ( '(\[\{"label".+?\}\])' ) . findall ( oo000OO00Oo )
   try :
    ooOOoooooo = json . loads ( oo0Ooo0 [ 0 ] ) [ - 1 ] [ "file" ]
   except :
    ooOOoooooo = json . loads ( oo0Ooo0 [ 0 ] ) [ - 1 ] [ "src" ]
  elif 'ok.ru/videoembed/' in oo000OO00Oo :
   O0 = re . search ( "ok.ru/videoembed/(\d+)" , oo000OO00Oo ) . group ( 1 )
   i1II1Iiii1I11 = "https://m.ok.ru/video/%s" % O0
   oo000OO00Oo = O0OOO0OOoO0O ( i1II1Iiii1I11 )
   ooOOoooooo = ( oo000 . unescape ( re . search ( "(https://m.ok.ru/dk\?st.+?)\&" , oo000OO00Oo ) . group ( 1 ) ) ) . decode ( 'unicode_escape' )
  elif 'iframe src="http://img.mythugian.net/stream' in oo000OO00Oo :
   try :
    oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/stream.+?)"' , oo000OO00Oo ) . group ( 1 )
    oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 )
    ooOOoooooo = re . search ( '"*file"*:"(.+?)"' , oo000OO00Oo ) . group ( 1 )
   except :
    try :
     oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/stream.+?)"' , oo000OO00Oo ) . group ( 1 )
     IIIIiiIiI = requests . head ( oo0Ooo0 ) . headers [ 'location' ]
     oo0Ooo0 = re . search ( "http\://(.+?)/.+?id=(.+?)$" , IIIIiiIiI )
     ooOOoooooo = "http://%s/hls/%s/%s.m3u8" % ( oo0Ooo0 . group ( 1 ) , oo0Ooo0 . group ( 2 ) , oo0Ooo0 . group ( 2 ) )
    except : pass
  elif 'iframe src="http://www.xomvnonline.com/play/mediafire/mediafire.php' in oo000OO00Oo :
   try :
    oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://www.xomvnonline.com/play/mediafire.+?)"' , oo000OO00Oo ) . group ( 1 )
    oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 )
    ooOOoooooo = re . search ( '"*file"*:"(.+?)"' , oo000OO00Oo ) . group ( 1 )
   except : pass
  elif 'iframe src="http://www.xomvnonline.com/play/open' in oo000OO00Oo :
   try :
    oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://www.xomvnonline.com/play/open.+?)"' , oo000OO00Oo ) . group ( 1 )
    oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 )
    ooOOoooooo = re . search ( 'data-stream-link="(.+?)"' , oo000OO00Oo ) . group ( 1 )
   except : pass
  elif 'iframe src="http://img.mythugian.net/you/api' in oo000OO00Oo :
   try :
    oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/you/api.+?)"' , oo000OO00Oo ) . group ( 1 )
    oo000OO00Oo = o00oooO0Oo ( oo0Ooo0 )
    oo0Ooo0 = re . search ( '<script[^>]*>(eval.+?)</script>' , oo000OO00Oo ) . group ( 1 ) . strip ( )
    if iI1 ( oo0Ooo0 ) :
     oo000OO00Oo = Oo ( oo0Ooo0 ) . replace ( "\\\\/" , "/" )
     ooOOoooooo = re . search ( '"*file"*:"(.+?)"' , oo000OO00Oo ) . group ( 1 )
   except : pass
  elif 'iframe src="http://img.mythugian.net/' in oo000OO00Oo :
   try :
    oo0Ooo0 = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/.+?)"' , oo000OO00Oo ) . group ( 1 )
    try :
     ooOOoooooo = re . search ( 'link=(.+?)$' , oo0Ooo0 ) . group ( 1 ) . decode ( "base64" )
     ooOOoooooo = o0O0OOO0Ooo ( ooOOoooooo )
    except :
     oo000OO00Oo = O0OOO0OOoO0O ( oo0Ooo0 )
     try :
      def iiIiI ( url ) :
       I1 = requests . get ( url )
       OOO00O0O = re . search ( ",'(\|*http.+?)'" , I1 . text ) . group ( 1 ) . split ( "|" )
       iii = re . compile ( '"(0\://.+?)"' ) . findall ( I1 . text )
       return OOO00O0O , iii
       if 90 - 90: I1II1 % oOooOoO0Oo0O / I1Ii111
      def IIi ( enc_url , words ) :
       i1Iii1i1I = "0123456789abcdefghijklmnopqrstuvwxyz"
       OOoO00 = ""
       for o0oo in range ( 0 , len ( enc_url ) ) :
        if o0oo != 12 and enc_url [ o0oo ] in i1Iii1i1I :
         OOoO00 += words [ i1Iii1i1I . index ( enc_url [ o0oo ] ) ]
        else :
         OOoO00 += enc_url [ o0oo ]
       return OOoO00
       if 40 - 40: i1iIi11iIIi1I * i1IIi11111i + ooO % I11i1i11i1I
      OOO00O0O , iii = iiIiI ( oo0Ooo0 )
      ooOOoooooo = IIi ( iii [ 0 ] , OOO00O0O )
      xbmc . log ( ooOOoooooo )
     except :
      try :
       OOOOOoo0 = [ ]
       OOOOOoo0 += [ re . search ( 'start\|primary\|(.+?)\|' . decode ( "base64" ) , oo000OO00Oo ) . group ( 1 ) ]
       try :
        OOOOOoo0 += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , oo000OO00Oo ) . group ( 1 ) ]
       except : pass
       ooOOoooooo = o0O0OOO0Ooo ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( OOOOOoo0 ) ) )
      except :
       try :
        OOOOOoo0 = [ ]
        OOOOOoo0 += [ re . search ( 'start\|(\w+)\|setup' . decode ( "base64" ) , oo000OO00Oo ) . group ( 1 ) ]
        OOOOOoo0 += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , oo000OO00Oo ) . group ( 1 ) ]
        OOOOOoo0 += [ re . search ( 'primary\|(\w+)\|startparam' . decode ( "base64" ) , oo000OO00Oo ) . group ( 1 ) ]
        ooOOoooooo = o0O0OOO0Ooo ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( OOOOOoo0 ) ) )
       except :
        try :
         oo0Ooo0 = re . search ( 'sources = (\[.+?\]);' , oo000OO00Oo )
         ooOOoooooo = json . loads ( oo0Ooo0 . group ( 1 ) ) [ - 1 ] [ "file" ]
        except :
         try :
          oo0Ooo0 = re . search ( '"(https://drive.google.com/file/.+?)"' , oo000OO00Oo ) . group ( 1 )
          ooOOoooooo = o0O0OOO0Ooo ( oo0Ooo0 . replace ( "preview" , "view" ) )
         except :
          ooOOoooooo = re . search ( '"(http\://.+?\.mediafire\.com/.+?)"' , oo000OO00Oo ) . group ( 1 )
   except : pass
  elif "drive.google.com/file" in oo000OO00Oo :
   oo0Ooo0 = re . search ( '"(https://drive.google.com/file.+?)"' , oo000OO00Oo )
   ooOOoooooo = o0O0OOO0Ooo ( oo0Ooo0 . group ( 1 ) . replace ( "preview" , "view" ) )
  elif II1I is not None :
   if "http://" not in II1I [ 0 ] :
    II1I [ 0 ] = "http://www.xomphimbo.com/xem/" + II1I [ 0 ]
   ooOOoooooo = II1I [ 0 ]
  elif "app.box.com" in oo000OO00Oo :
   ii1 = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( oo000OO00Oo ) [ 0 ]
   I1iI1iIi111i = O0OOO0OOoO0O ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % ii1 )
   iiIi1IIi1I = json . loads ( I1iI1iIi111i ) [ "file" ] [ "versionId" ]
   ooOOoooooo = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( iiIi1IIi1I , ii1 )
  elif "openload" in oo000OO00Oo :
   try :
    ooOOoooooo = re . compile ( '"(https://openload.+?)"' ) . findall ( oo000OO00Oo ) [ 0 ]
    ooOOoooooo = urlresolver . resolve ( ooOOoooooo )
   except :
    pass
  else :
   oo0Ooo0 = re . compile ( "file: '.+?'" ) . findall ( oo000OO00Oo )
   if "http://" not in oo0Ooo0 [ 0 ] :
    ooOOoooooo = "http://www.xomphimbo.com/xem/" + oo0Ooo0 [ 0 ]
   else :
    ooOOoooooo = oo0Ooo0 [ 0 ]
  i1iIi . setPath ( ooOOoooooo )
 else :
  if "http://" not in oo0Ooo0 [ 0 ] :
   oo0Ooo0 [ 0 ] = "http://www.xomphimbo.com/xem/" + oo0Ooo0 [ 0 ]
  i1iIi . setPath ( oo0Ooo0 [ 0 ] )
 i1iIi . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iIi )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , i1iIi )
 if 84 - 84: oo0ooO0oOOOOo * I11i11Ii + I1iII1iiII
def o0O0OOO0Ooo ( url , hq = True ) :
 O0ooO0Oo00o = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 ooO0oOOooOo0 = {
 'User-Agent' : O0ooO0Oo00o ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 I1iI1iIi111i = requests . get ( url , headers = ooO0oOOooOo0 )
 i1I1ii11i1Iii = I1iI1iIi111i . text
 try :
  oo0Ooo0 = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( i1I1ii11i1Iii ) [ 0 ]
  I1IiiiiI = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : I1IiiiiI . reverse ( )
  o0O = json . loads ( oo0Ooo0 ) [ 1 ] . split ( "," )
  for IiII in I1IiiiiI :
   for ii1iII1II in o0O :
    if ii1iII1II . startswith ( IiII + "|" ) :
     url = ii1iII1II . split ( "|" ) [ 1 ]
     Iii1I1I11iiI1 = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( O0ooO0Oo00o ) , urllib . quote_plus ( I1iI1iIi111i . headers [ 'set-cookie' ] ) )
     return url + Iii1I1I11iiI1
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , i1I1ii11i1Iii ) . group ( 1 )
  except : pass
  if 18 - 18: ooO + I11i1i11i1I - i1IIi11111i . I11i11Ii + Ii
def iI1Ii1iI11iiI ( url ) :
 OO0OO0O00oO0 = ""
 oO = urllib2 . Request ( url )
 oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 oO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1Ii1I1 = urllib2 . urlopen ( oO )
 url = I1Ii1I1 . geturl ( )
 try :
  OO0OO0O00oO0 = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 I1Ii1I1 . close ( )
 return OO0OO0O00oO0
 if 28 - 28: o0o00Oo0O * I1iII1iiII - ooO % iI11I1II1I1I * i1IIi11111i - Ii
def O0OOO0OOoO0O ( url ) :
 oO = urllib2 . Request ( url )
 oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 oO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1Ii1I1 = urllib2 . urlopen ( oO )
 oo000OO00Oo = I1Ii1I1 . read ( )
 I1Ii1I1 . close ( )
 oo000OO00Oo = '' . join ( oo000OO00Oo . splitlines ( ) ) . replace ( '\'' , '"' )
 oo000OO00Oo = oo000OO00Oo . replace ( '\n' , '' )
 oo000OO00Oo = oo000OO00Oo . replace ( '\t' , '' )
 oo000OO00Oo = re . sub ( '  +' , ' ' , oo000OO00Oo )
 oo000OO00Oo = oo000OO00Oo . replace ( '> <' , '><' )
 return oo000OO00Oo
 if 7 - 7: I1iII1iiII + OOo00O0Oo0oO - OOO0O % i1IIi11111i + oO0o
def o00oooO0Oo ( url ) :
 oO = urllib2 . Request ( url )
 oO . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 oO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1Ii1I1 = urllib2 . urlopen ( oO )
 oo000OO00Oo = I1Ii1I1 . read ( )
 I1Ii1I1 . close ( )
 if 53 - 53: oOooOoO0Oo0O - i1111 . OOo
 oo000OO00Oo = oo000OO00Oo . replace ( '\n' , '' )
 oo000OO00Oo = oo000OO00Oo . replace ( '\t' , '' )
 oo000OO00Oo = re . sub ( '  +' , ' ' , oo000OO00Oo )
 oo000OO00Oo = oo000OO00Oo . replace ( '> <' , '><' )
 return oo000OO00Oo
 if 39 - 39: I11i11Ii / oo0ooO0oOOOOo + OOO0O / OOo
def ooo00OOOooO ( name , url , mode , iconimage , mirrorname ) :
 I1Ii11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 i1111I1I = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1i . setProperty ( "IsPlayable" , "true" )
 i1111I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Ii11i , listitem = i1i )
 return i1111I1I
 if 56 - 56: oO0o % o0o00Oo0O - i1iIi11iIIi1I
def OOO0OOO00oo ( name , url , mode , iconimage ) :
 I1Ii11i = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 i1111I1I = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1111I1I = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = I1Ii11i , listitem = i1i , isFolder = True )
 return i1111I1I
 if 100 - 100: i1IIi11111i - o0o00Oo0O % OOo00O0Oo0oO * ooO + i1iIi11iIIi1I
def Oo0O0oooo ( k , e ) :
 I111iI = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for o0oo in range ( len ( e ) ) :
  oOOo0II1I1iiIII = k [ o0oo % len ( k ) ]
  oOOo0O00o = chr ( ( 256 + ord ( e [ o0oo ] ) - ord ( oOOo0II1I1iiIII ) ) % 256 )
  I111iI . append ( oOOo0O00o )
 return "" . join ( I111iI )
 if 8 - 8: I1Ii111
def ii1111iII ( parameters ) :
 iiiiI = { }
 if 62 - 62: i11i * i1iIi11iIIi1I
 if parameters :
  oOOOoo0O0oO = parameters [ 1 : ] . split ( "&" )
  for iIII1I111III in oOOOoo0O0oO :
   IIo0o0O0O00oOOo = iIII1I111III . split ( '=' )
   if ( len ( IIo0o0O0O00oOOo ) ) == 2 :
    iiiiI [ IIo0o0O0O00oOOo [ 0 ] ] = IIo0o0O0O00oOOo [ 1 ]
 return iiiiI
 if 14 - 14: OOo + OOo00O0Oo0oO
oo00oO0O0 = xbmc . translatePath ( iIIii1IIi . getAddonInfo ( 'profile' ) )
if 30 - 30: ooO + oO0o * i1111 % Ii % OOo
if os . path . exists ( oo00oO0O0 ) == False :
 os . mkdir ( oo00oO0O0 )
OO0OoOO0o0o = os . path . join ( oo00oO0O0 , 'visitor' )
if 95 - 95: Ii
if os . path . exists ( OO0OoOO0o0o ) == False :
 from random import randint
 iI1111iiii = open ( OO0OoOO0o0o , "w" )
 iI1111iiii . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iI1111iiii . close ( )
 if 67 - 67: i11i / i1iIi11iIIi1I * i1IIi11111i + i1111
def OooOo0ooo ( utm_url ) :
 o00oo0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  oO = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : o00oo0 }
 )
  I1Ii1I1 = urllib2 . urlopen ( oO ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return I1Ii1I1
 if 38 - 38: oo0ooO0oOOOOo % I11i11Ii % i1111 / I1Ii111 + OOo / oOooOoO0Oo0O
def OoOOo0OOoO ( group , name ) :
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
  ooO0O00Oo0o = "1.0"
  OOO = open ( OO0OoOO0o0o ) . read ( )
  Oo0o00OO0000 = "XomGiaiTri"
  I1i = "UA-52209804-2"
  O00Oooo = "www.viettv24.com"
  i11I = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   o00Oo0oooooo = i11I + "?" + "utmwv=" + ooO0O00Oo0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0o00OO0000 ) + "&utmac=" + I1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO , "1" , "1" , "2" ] )
   if 76 - 76: i1111 / ooO . o0o00Oo0O % i1iIi11iIIi1I . I1II1 + oo
   if 71 - 71: OOO0O . I11i11Ii
   if 62 - 62: i11i . i1111
   if 61 - 61: OOo - ooO - oOooOoO0Oo0O
   if 25 - 25: o0o00Oo0O * i1111 + oO0o . I1II1 . I1II1
  else :
   if group == "None" :
    o00Oo0oooooo = i11I + "?" + "utmwv=" + ooO0O00Oo0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0o00OO0000 + "/" + name ) + "&utmac=" + I1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO , "1" , "1" , "2" ] )
    if 58 - 58: i1iIi11iIIi1I
    if 53 - 53: oOooOoO0Oo0O
    if 59 - 59: I1II1
    if 81 - 81: OOo - OOo . I11i1i11i1I
    if 73 - 73: i1111 % Ii - i1iIi11iIIi1I
   else :
    o00Oo0oooooo = i11I + "?" + "utmwv=" + ooO0O00Oo0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( Oo0o00OO0000 + "/" + group + "/" + name ) + "&utmac=" + I1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO , "1" , "1" , "2" ] )
    if 7 - 7: o0o00Oo0O * Ii * i1IIi11111i + oo0ooO0oOOOOo % I1Ii111 - oo0ooO0oOOOOo
    if 39 - 39: I1iII1iiII * ooO % ooO - i11i + I1II1 - i1111
    if 23 - 23: Ii
    if 30 - 30: I1II1 - oOooOoO0Oo0O % I11i11Ii + i1111 * iI11I1II1I1I
    if 81 - 81: oo % oOooOoO0Oo0O . iI11I1II1I1I
    if 4 - 4: Ii % I1Ii111 % oOooOoO0Oo0O / oo
  print "============================ POSTING ANALYTICS ============================"
  OooOo0ooo ( o00Oo0oooooo )
  if 6 - 6: I11i1i11i1I / i1iIi11iIIi1I % ooO - i1iIi11iIIi1I
  if not group == "None" :
   iiii111II = i11I + "?" + "utmwv=" + ooO0O00Oo0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O00Oooo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + Oo0o00OO0000 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( Oo0o00OO0000 ) + "&utmac=" + I1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , OOO , "1" , "2" ] )
   if 50 - 50: ooO * i1iIi11iIIi1I % iI11I1II1I1I + i1IIi11111i + I11i1i11i1I + i1iIi11iIIi1I
   if 71 - 71: oO0o * oO0o * oOooOoO0Oo0O . OOo00O0Oo0oO / OOO0O
   if 85 - 85: i1111
   if 20 - 20: OOo00O0Oo0oO % oo
   if 19 - 19: oO0o % oo + oo0ooO0oOOOOo / OOO0O . oo0ooO0oOOOOo
   if 12 - 12: oOooOoO0Oo0O + oOooOoO0Oo0O - oO0o * I1iII1iiII % I1iII1iiII - I11i11Ii
   if 52 - 52: oo0ooO0oOOOOo . I11i1i11i1I + OOO0O
   if 38 - 38: oOooOoO0Oo0O - I11i11Ii . OOO0O
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OooOo0ooo ( iiii111II )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 58 - 58: i1iIi11iIIi1I . I11i1i11i1I + OOo
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 66 - 66: I11i1i11i1I / OOo00O0Oo0oO * i11i + i11i % i1111
IIii1111 = ii1111iII ( sys . argv [ 2 ] )
I1iI = IIii1111 . get ( 'mode' )
ii111111I1iII = IIii1111 . get ( 'url' )
IIIIiIiIi1 = IIii1111 . get ( 'name' )
if type ( ii111111I1iII ) == type ( str ( ) ) :
 ii111111I1iII = urllib . unquote_plus ( ii111111I1iII )
if type ( IIIIiIiIi1 ) == type ( str ( ) ) :
 IIIIiIiIi1 = urllib . unquote_plus ( IIIIiIiIi1 )
 if 2 - 2: I11i1i11i1I % iI11I1II1I1I * iI11I1II1I1I . I1II1 / I11i1i11i1I
iII1i1 = str ( sys . argv [ 1 ] )
if I1iI == 'index' :
 OoOOo0OOoO ( "Browse" , IIIIiIiIi1 )
 iIIIIii1 ( ii111111I1iII )
elif I1iI == 'search' :
 OoOOo0OOoO ( "None" , "Search" )
 oO0o0OOOO ( )
elif I1iI == 'videosbyregion' :
 OoOOo0OOoO ( "Browse" , IIIIiIiIi1 )
 II1i1IiiIIi11 ( )
elif I1iI == 'videosbycategory' :
 OoOOo0OOoO ( "Browse" , IIIIiIiIi1 )
 Ii11iII1 ( )
elif I1iI == 'mirrors' :
 OoOOo0OOoO ( "Browse" , IIIIiIiIi1 )
 i1iIi1iIi1i ( ii111111I1iII )
elif I1iI == 'episodes' :
 OoOOo0OOoO ( "Browse" , IIIIiIiIi1 )
 OO0oOO0O ( ii111111I1iII , IIIIiIiIi1 )
elif I1iI == 'loadvideo' :
 OoOOo0OOoO ( "Play" , IIIIiIiIi1 + "/" + ii111111I1iII )
 O0oOOoooOO0O = xbmcgui . DialogProgress ( )
 O0oOOoooOO0O . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 OoooO0oO ( ii111111I1iII , IIIIiIiIi1 )
 O0oOOoooOO0O . close ( )
 del O0oOOoooOO0O
else :
 OoOOo0OOoO ( "None" , "None" )
 iIii11I ( )
xbmcplugin . endOfDirectory ( int ( iII1i1 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
