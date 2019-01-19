#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver , HTMLParser , string
oo000 = HTMLParser . HTMLParser ( )
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
oooo = 'plugin.video.xomgiaitri'
iIIii1IIi = xbmcaddon . Addon ( oooo )
o0OO00 = int ( sys . argv [ 1 ] )
global redirect_url
def oo ( source ) :
 source = source . replace ( ' ' , '' )
 if 27 - 27: oO0OooOoO * o0Oo
 if re . search ( 'eval\(function\(p,a,c,k,e,' , source ) : return True
 else : return False
 if 5 - 5: OoO0O00
def IIiIiII11i ( source ) :
 o0oOOo0O0Ooo , I1ii11iIi11i , I1IiI , o0OOO = iIiiiI ( source )
 if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
 if 68 - 68: o00ooo0 / Oo00O0
 if o0OOO != len ( I1ii11iIi11i ) :
  raise ooO0oooOoO0 ( 'Malformed p.a.c.k.e.r. symtab.' )
  if 21 - 21: IiIii1Ii1IIi / O0Oooo00 . oo00 * I11
 try :
  Oo0o0000o0o0 = oOo0oooo00o ( I1IiI )
 except TypeError :
  raise ooO0oooOoO0 ( 'Unknown p.a.c.k.e.r. encoding.' )
  if 65 - 65: O0o * i1iIIII * OoO0O00
 def oO000OoOoo00o ( match ) :
  iiiI11 = match . group ( 0 )
  if 91 - 91: oO0o0ooO0 / OoO0O00 . iiIIIII1i1iI + Oo00O0
  return I1ii11iIi11i [ Oo0o0000o0o0 ( iiiI11 ) ] or iiiI11
  if 47 - 47: ii1II11I1ii1I / O0Oooo00 * oO0OooOoO
 source = re . sub ( r'\b\w+\b' , oO000OoOoo00o , o0oOOo0O0Ooo )
 return II111iiii ( source )
 if 48 - 48: iI1Ii11111iIi . oO0OooOoO - ii1II11I1ii1I % Oo00O0 / O0Oooo00 . O0Oooo00
def iIiiiI ( source ) :
 i1Ii = ( r"}\('(.*)', *(\d+), *(\d+), *'(.*?)'\.split\('\|'\)" )
 if 25 - 25: oo00 + i1iIIII % i1iIIII - o00ooo0 * oO0o0ooO0 % oo00
 OOooO0OOoo = re . search ( i1Ii , source , re . DOTALL ) . groups ( )
 if 29 - 29: oO0o0ooO0 / iI11I1II1I1I
 try :
  return OOooO0OOoo [ 0 ] , OOooO0OOoo [ 3 ] . split ( '|' ) , int ( OOooO0OOoo [ 1 ] ) , int ( OOooO0OOoo [ 2 ] )
 except ValueError :
  raise ooO0oooOoO0 ( 'Corrupted p.a.c.k.e.r. data.' )
  if 24 - 24: o0o00Oo0O % oO0o0ooO0 + o0Oo + O0o + iiIIIII1i1iI
def II111iiii ( source ) :
 OOoO000O0OO = re . search ( r'var *(_\w+)\=\["(.*?)"\];' , source , re . DOTALL )
 if 23 - 23: Ii + iii1II11ii
 if 68 - 68: ii1II11I1ii1I . o00ooo0 . Ii
 if OOoO000O0OO :
  II , iI = OOoO000O0OO . groups ( )
  iI11iiiI1II = len ( OOoO000O0OO . group ( 0 ) )
  oO000OoOoo00o = iI . split ( '","' )
  O0oooo0Oo00 = '%s[%%d]' % II
  for Ii11iii11I , oOo00Oo00O in enumerate ( oO000OoOoo00o ) :
   source = source . replace ( O0oooo0Oo00 % Ii11iii11I , '"%s"' % oOo00Oo00O )
  return source [ iI11iiiI1II : ]
 return source
 if 43 - 43: iii1II11ii - oo00 * iI11I1II1I1I
 if 97 - 97: IiIii1Ii1IIi % IiIii1Ii1IIi + OoO0O00 * oo00
class oOo0oooo00o ( object ) :
 ALPHABET = {
 # iI1Ii11111iIi + OoO0O00 % oo00 * o0o00Oo0O
 # ii1II11I1ii1I / i11iII1iiI - I11 . o0Oo / iii1II11ii % I11
 52 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOP' ,
 54 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR' ,
 62 : '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' ,
 95 : ( ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' )
 }
 if 71 - 71: O0o . o0o00Oo0O
 def __init__ ( self , base ) :
  self . base = base
  if 73 - 73: Oo00O0 % ii1II11I1ii1I - O0Oooo00
  if 10 - 10: iii1II11ii % iiIIIII1i1iI
  if 2 <= base <= 36 :
   self . unbase = lambda I1i1iii : int ( string , base )
  else :
   if 20 - 20: oO0o0ooO0
   try :
    self . dictionary = dict ( ( cipher , index ) for
 index , cipher in enumerate ( self . ALPHABET [ base ] ) )
   except KeyError :
    raise TypeError ( 'Unsupported base encoding.' )
    if 77 - 77: ii1II11I1ii1I / IiIii1Ii1IIi
   self . unbase = self . _dictunbaser
   if 98 - 98: iI11I1II1I1I / o0Oo / Ii / oO0o0ooO0
 def __call__ ( self , string ) :
  return self . unbase ( string )
  if 28 - 28: Oo00O0 - I11 . I11 + ii1II11I1ii1I - oO0OooOoO + o0o00Oo0O
 def _dictunbaser ( self , string ) :
  oOoOooOo0o0 = 0
  if 61 - 61: oO0o0ooO0 / iI1Ii11111iIi + i1iIIII * o00ooo0 / o00ooo0
  for Ii11iii11I , OoOo in enumerate ( string [ : : - 1 ] ) :
   oOoOooOo0o0 += ( self . base ** Ii11iii11I ) * self . dictionary [ OoOo ]
  return oOoOooOo0o0
  if 18 - 18: Ii
class ooO0oooOoO0 ( Exception ) :
 pass
 if 46 - 46: o0Oo / IiIii1Ii1IIi % Oo00O0 + O0o
 if 79 - 79: O0o - oO0o0ooO0 + O0o - oo00
 if 8 - 8: iii1II11ii
def Oo000 ( ) :
 ooii11I ( 'Search' , 'http://www.xomvnonline.com/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 ooii11I ( 'Phim Lẻ' , 'http://www.xomvnonline.com/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 ooii11I ( 'Phim Bộ' , 'http://www.xomvnonline.com/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 ooii11I ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomvnonline.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 ooii11I ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomvnonline.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 if 96 - 96: OoO0O00 % O0Oooo00 . Oo00O0 + oO0OooOoO * o00ooo0 - ii1II11I1ii1I
 if 10 - 10: Oo00O0 / iii1II11ii * Oo00O0
 if 29 - 29: iiIIIII1i1iI % iii1II11ii + i1iIIII / oO0o0ooO0 + Oo00O0 * oO0o0ooO0
 if 42 - 42: O0Oooo00 + o00ooo0
 if 76 - 76: O0o - iI1Ii11111iIi
 if 70 - 70: i1iIIII
 if 61 - 61: iiIIIII1i1iI . iiIIIII1i1iI
 if 10 - 10: ii1II11I1ii1I * oo00 . IiIii1Ii1IIi + OoO0O00 - i1iIIII * o0Oo
 if 56 - 56: oO0o0ooO0 * I11 * OoO0O00
def oO0ooO0OoOOOO ( ) :
 ooii11I ( "Hồng Kong" , "http://www.xomvnonline.com/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ooii11I ( "Hồng Kong (VNLT)" , "http://www.xomvnonline.com/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ooii11I ( "Hàn Quốc" , "http://www.xomvnonline.com/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ooii11I ( "Hàn Quốc (vietsub)" , "http://www.xomvnonline.com/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ooii11I ( "Trung Quốc" , "http://www.xomvnonline.com/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ooii11I ( "Đài Loan" , "http://www.xomvnonline.com/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ooii11I ( "Việt Nam" , "http://www.xomvnonline.com/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ooii11I ( "Thái Lan" , "http://www.xomvnonline.com/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ooii11I ( "Các Loại Khác" , "http://www.xomvnonline.com/category/7/cac-loai-khac.html" , "index" , "" )
 if 46 - 46: Oo00O0 / iiIIIII1i1iI
def I1 ( ) :
 ooii11I ( "Hành Động" , "http://www.xomvnonline.com/category/8/hanh-dong.html" , "index" , "" )
 ooii11I ( "Tình Cảm" , "http://www.xomvnonline.com/category/9/tinh-cam.html" , "index" , "" )
 ooii11I ( "Phim Hài" , "http://www.xomvnonline.com/category/10/phim-hai.html" , "index" , "" )
 ooii11I ( "Kinh Dị" , "http://www.xomvnonline.com/category/11/kinh-di.html" , "index" , "" )
 ooii11I ( "Kiếm Hiệp" , "http://www.xomvnonline.com/category/12/kiem-hiep.html" , "index" , "" )
 ooii11I ( "Việt Nam" , "http://www.xomvnonline.com/category/15/viet-nam.html" , "index" , "" )
 ooii11I ( "Hài Kịch" , "http://www.xomvnonline.com/category/16/hai-kich.html" , "index" , "" )
 ooii11I ( "Ca Nhạc" , "http://www.xomvnonline.com/category/17/ca-nhac.html" , "index" , "" )
 ooii11I ( "Cải Lương" , "http://www.xomvnonline.com/category/18/cai-luong.html" , "index" , "" )
 ooii11I ( "Phóng Sự" , "http://www.xomvnonline.com/category/19/phong-su.html" , "index" , "" )
 ooii11I ( "Các Loại Khác" , "http://www.xomvnonline.com/category/20/cac-loai-khac.html" , "index" , "" )
 if 71 - 71: Oo00O0 + i1iIIII % Ii + iiIIIII1i1iI - I11
def oO0OOoO0 ( url ) :
 I111Ii111 = i111IiI1I ( url )
 O0 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( I111Ii111 )
 for iII , o0 , ooOooo000oOO in O0 :
  ooOooo000oOO = ooOooo000oOO . replace ( "xomgiaitri.com" , "mythugian.net" )
  ooOooo000oOO = ooOooo000oOO . replace ( "www." , "" )
  ooOooo000oOO = "/" . join ( ooOooo000oOO . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( ooOooo000oOO . split ( "/" ) [ - 1 ] )
  ooii11I ( "[B]" + o0 + "[/B]" , "http://www.xomvnonline.com/xem" + iII , 'mirrors' , ooOooo000oOO )
 Oo0oOOo = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( I111Ii111 . replace ( "'" , '"' ) )
 for iII , Oo0OoO00oOO0o in Oo0oOOo :
  ooii11I ( Oo0OoO00oOO0o , iII . replace ( "./" , "http://www.xomvnonline.com/" ) , 'index' , "" )
  if 80 - 80: o00ooo0 + Oo00O0 - Oo00O0 % oo00
def OoOO0oo0o ( ) :
 try :
  II11i1I11Ii1i = xbmc . Keyboard ( '' , 'Enter search text' )
  II11i1I11Ii1i . doModal ( )
  if 97 - 97: i1iIIII % oo00 * O0Oooo00 + oO0o0ooO0 . Oo00O0 + Oo00O0
  if ( II11i1I11Ii1i . isConfirmed ( ) ) :
   Oooo0O0oo00oO = urllib . quote_plus ( II11i1I11Ii1i . getText ( ) )
  oO0OOoO0 ( IIi1i % Oooo0O0oo00oO )
 except : pass
 if 46 - 46: O0o % IiIii1Ii1IIi + iI1Ii11111iIi . ii1II11I1ii1I . iI1Ii11111iIi
def oO00o0 ( url ) :
 OOoo0O = Oo0ooOo0o ( url )
 I111Ii111 = i111IiI1I ( OOoo0O )
 Ii1i1 = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( I111Ii111 )
 if 15 - 15: OoO0O00
 if "VIP Ama : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP Ama : " ) ) )
 if "VIP A : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP A : " ) ) )
 if "VIP D : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP D : " ) ) )
 if "VIP C : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP C : " ) ) )
 if "VIP B : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP B : " ) ) )
 if "VIP M : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP M : " ) ) )
 if "VIP G : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP G : " ) ) )
 if "VIP OK : " in Ii1i1 :
  Ii1i1 . insert ( 0 , Ii1i1 . pop ( Ii1i1 . index ( "VIP OK : " ) ) )
 for Iiooo0O in range ( len ( Ii1i1 ) ) :
  oOoO0o00OO0 = [ "Flv :" ]
  if not any ( x in Ii1i1 [ Iiooo0O ] for x in oOoO0o00OO0 ) :
   ooii11I ( "[%d] - %s" % ( Iiooo0O + 1 , Ii1i1 [ Iiooo0O ] ) , OOoo0O . encode ( "utf-8" ) , 'episodes' , "" )
   if 7 - 7: Oo00O0 + O0o + o0o00Oo0O
def IiO0OOO ( url , name ) :
 I111Ii111 = i111IiI1I ( url )
 if 10 - 10: Oo00O0 * IiIii1Ii1IIi % ii1II11I1ii1I / iii1II11ii / ii1II11I1ii1I
 name = name . split ( "] - " ) [ 1 ]
 iIIi1i1 = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % name ) . findall ( I111Ii111 )
 i1IIIiiII1 = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( iIIi1i1 [ 0 ] )
 if ( "episode_bg_2" in iIIi1i1 [ 0 ] ) :
  OOOOoOoo0O0O0 = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( iIIi1i1 [ 0 ] )
  OOOo00oo0oO ( "Part - " + OOOOoOoo0O0O0 [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf8" ) , url , 'loadvideo' , '' , name )
 for IIiIi1iI , i1IiiiI1iI in i1IIIiiII1 :
  OOOo00oo0oO ( "Part - " + i1IiiiI1iI . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomvnonline.com/" + IIiIi1iI , 'loadvideo' , '' , name )
  if 49 - 49: O0Oooo00 / iI1Ii11111iIi . OoO0O00
def Oo0ooOo0o ( url ) :
 url = url . replace ( "/xem/" , "/" )
 ooOOoooooo = i111IiI1I ( url )
 xbmc . log ( url , 7 )
 xbmc . log ( ooOOoooooo , 7 )
 return re . compile ( '</p><p><a href="(.+?)" title="Xem phim truc tuyen">' ) . findall ( ooOOoooooo ) [ 0 ]
 if 1 - 1: i11iII1iiI / oO0o0ooO0 % oo00 * I11 . Ii
def III1Iiii1I11 ( url ) :
 xbmc . log ( "========= %s =========" % oooo )
 xbmc . log ( "Start resolving url %s" % url )
 if 9 - 9: iiIIIII1i1iI / i11iII1iiI - iii1II11ii / oO0OooOoO / iI11I1II1I1I - oO0o0ooO0
 def o00oooO0Oo ( url ) :
  o0O0OOO0Ooo = re . search ( "ok.ru/videoembed/(\d+)" , url ) . group ( 1 )
  iiIiI = "https://m.ok.ru/video/%s" % o0O0OOO0Ooo
  I111Ii111 = i111IiI1I ( iiIiI )
  return ( oo000 . unescape ( re . search ( "(https://m.ok.ru/dk\?st.+?)\&" , I111Ii111 ) . group ( 1 ) ) ) . decode ( 'unicode_escape' )
  if 6 - 6: I11 . o00ooo0 * ii1II11I1ii1I - O0Oooo00 - I11
 I111Ii111 = i111IiI1I ( url )
 if "proxy.link" in I111Ii111 :
  OOoO000O0OO = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( I111Ii111 )
  xbmc . log ( "Proxy link detected: %s" % OOoO000O0OO [ 0 ] )
  I111Ii111 = i111IiI1I ( OOoO000O0OO [ 0 ] )
 OOoO000O0OO = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( I111Ii111 )
 if 45 - 45: iii1II11ii - oO0OooOoO + iI11I1II1I1I . iii1II11ii * IiIii1Ii1IIi
 if ( len ( OOoO000O0OO ) == 0 ) :
  oOOO = None
  iIII1 = re . compile ( 'file\: "(.+?)"' ) . findall ( I111Ii111 )
  try :
   return o00oooO0Oo ( I111Ii111 )
  except : pass
  if 65 - 65: o0o00Oo0O
  try :
   OOoO000O0OO = re . search ( 'iframe src="(http://play.mythugian.net/.+?)"' , I111Ii111 ) . group ( 1 )
   xbmc . log ( "iframe detected: %s" % OOoO000O0OO [ 0 ] )
   I111Ii111 = i111IiI1I ( OOoO000O0OO [ 0 ] )
   OOoO000O0OO = re . compile ( '(\[\{"label".+?\}\])' ) . findall ( I111Ii111 )
   try :
    return json . loads ( OOoO000O0OO [ 0 ] ) [ - 1 ] [ "file" ]
   except :
    return json . loads ( OOoO000O0OO [ 0 ] ) [ - 1 ] [ "src" ]
  except : pass
  if 68 - 68: Oo00O0 % O0o
  try :
   ooO00OO0 = re . search ( 'iframe[^>]*src="(http://webplay.mythugian.net/.+?)"' , I111Ii111 ) . group ( 1 )
   xbmc . log ( "iframe detected: %s" % ooO00OO0 )
   I111Ii111 = i11111IIIII ( ooO00OO0 )
   try :
    OOoO000O0OO = re . search ( '<script[^>]*>(eval.+?)</script>' , I111Ii111 ) . group ( 1 ) . strip ( )
    if oo ( OOoO000O0OO ) :
     I111Ii111 = IIiIiII11i ( OOoO000O0OO ) . replace ( "\\\\/" , "/" )
     return re . search ( '"*file"*:"(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
   try :
    return re . search ( '"*file"*:"(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://www.xomvnonline.com/play/open.+?)"' , I111Ii111 ) . group ( 1 )
    I111Ii111 = i111IiI1I ( OOoO000O0OO )
    return re . search ( 'data-stream-link="(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
   try :
    iIiii1i111iI1 = requests . head ( ooO00OO0 ) . headers [ 'location' ]
    xbmc . log ( "Stream Dectected: %s" % iIiii1i111iI1 , 7 )
    OOoO000O0OO = re . search ( "http\://(.+?)/.+?id=(.+?)$" , iIiii1i111iI1 )
    return "http://%s/hls/%s/%s.playlist.m3u8" % ( OOoO000O0OO . group ( 1 ) , OOoO000O0OO . group ( 2 ) , OOoO000O0OO . group ( 2 ) )
   except : pass
   try :
    o00oooO0Oo ( I111Ii111 )
   except : pass
  except : pass
  if 14 - 14: oo00 . oo00 % oO0OooOoO
  if False : pass
  elif 'iframe src="http://img.mythugian.net/stream' in I111Ii111 :
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/stream.+?)"' , I111Ii111 ) . group ( 1 )
    I111Ii111 = i111IiI1I ( OOoO000O0OO )
    oOOO = re . search ( '"*file"*:"(.+?)"' , I111Ii111 ) . group ( 1 )
   except :
    try :
     OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/stream.+?)"' , I111Ii111 ) . group ( 1 )
     iIiii1i111iI1 = requests . head ( OOoO000O0OO ) . headers [ 'location' ]
     OOoO000O0OO = re . search ( "http\://(.+?)/.+?id=(.+?)$" , iIiii1i111iI1 )
     oOOO = "http://%s/hls/%s/%s.m3u8" % ( OOoO000O0OO . group ( 1 ) , OOoO000O0OO . group ( 2 ) , OOoO000O0OO . group ( 2 ) )
    except : pass
  elif 'iframe src="http://www.xomvnonline.com/play/mediafire/mediafire.php' in I111Ii111 :
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://www.xomvnonline.com/play/mediafire.+?)"' , I111Ii111 ) . group ( 1 )
    I111Ii111 = i111IiI1I ( OOoO000O0OO )
    oOOO = re . search ( '"*file"*:"(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
  elif 'iframe src="http://www.xomvnonline.com/play/open' in I111Ii111 :
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://www.xomvnonline.com/play/open.+?)"' , I111Ii111 ) . group ( 1 )
    I111Ii111 = i111IiI1I ( OOoO000O0OO )
    oOOO = re . search ( 'data-stream-link="(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
  elif 'iframe src="http://img.mythugian.net/you/api' in I111Ii111 :
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/you/api.+?)"' , I111Ii111 ) . group ( 1 )
    I111Ii111 = i11111IIIII ( OOoO000O0OO )
    OOoO000O0OO = re . search ( '<script[^>]*>(eval.+?)</script>' , I111Ii111 ) . group ( 1 ) . strip ( )
    if oo ( OOoO000O0OO ) :
     I111Ii111 = IIiIiII11i ( OOoO000O0OO ) . replace ( "\\\\/" , "/" )
     oOOO = re . search ( '"*file"*:"(.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
  elif 'iframe src="http://img.mythugian.net/' in I111Ii111 :
   try :
    OOoO000O0OO = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/.+?)"' , I111Ii111 ) . group ( 1 )
    try :
     oOOO = re . search ( 'link=(.+?)$' , OOoO000O0OO ) . group ( 1 ) . decode ( "base64" )
     oOOO = iiIi1IIi1I ( oOOO )
    except :
     I111Ii111 = i111IiI1I ( OOoO000O0OO )
     try :
      def o0OoOO000ooO0 ( url ) :
       o0o0o0oO0oOO = requests . get ( url )
       ii1Ii11I = re . search ( ",'(\|*http.+?)'" , o0o0o0oO0oOO . text ) . group ( 1 ) . split ( "|" )
       o00o0 = re . compile ( '"(0\://.+?)"' ) . findall ( o0o0o0oO0oOO . text )
       return ii1Ii11I , o00o0
       if 45 - 45: o0o00Oo0O
      def I1IiiiiI ( enc_url , words ) :
       o0O = "0123456789abcdefghijklmnopqrstuvwxyz"
       IiII = ""
       for Iiooo0O in range ( 0 , len ( enc_url ) ) :
        if Iiooo0O != 12 and enc_url [ Iiooo0O ] in o0O :
         IiII += words [ o0O . index ( enc_url [ Iiooo0O ] ) ]
        else :
         IiII += enc_url [ Iiooo0O ]
       return IiII
       if 25 - 25: o0o00Oo0O - o0o00Oo0O * oO0o0ooO0
      ii1Ii11I , o00o0 = o0OoOO000ooO0 ( OOoO000O0OO )
      oOOO = I1IiiiiI ( o00o0 [ 0 ] , ii1Ii11I )
      xbmc . log ( oOOO )
     except :
      try :
       OOOO0oo0 = [ ]
       OOOO0oo0 += [ re . search ( 'start\|primary\|(.+?)\|' . decode ( "base64" ) , I111Ii111 ) . group ( 1 ) ]
       try :
        OOOO0oo0 += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , I111Ii111 ) . group ( 1 ) ]
       except : pass
       oOOO = iiIi1IIi1I ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( OOOO0oo0 ) ) )
      except :
       try :
        OOOO0oo0 = [ ]
        OOOO0oo0 += [ re . search ( 'start\|(\w+)\|setup' . decode ( "base64" ) , I111Ii111 ) . group ( 1 ) ]
        OOOO0oo0 += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , I111Ii111 ) . group ( 1 ) ]
        OOOO0oo0 += [ re . search ( 'primary\|(\w+)\|startparam' . decode ( "base64" ) , I111Ii111 ) . group ( 1 ) ]
        oOOO = iiIi1IIi1I ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( OOOO0oo0 ) ) )
       except :
        try :
         OOoO000O0OO = re . search ( 'sources = (\[.+?\]);' , I111Ii111 )
         oOOO = json . loads ( OOoO000O0OO . group ( 1 ) ) [ - 1 ] [ "file" ]
        except :
         try :
          OOoO000O0OO = re . search ( '"(https://drive.google.com/file/.+?)"' , I111Ii111 ) . group ( 1 )
          oOOO = iiIi1IIi1I ( OOoO000O0OO . replace ( "preview" , "view" ) )
         except :
          oOOO = re . search ( '"(http\://.+?\.mediafire\.com/.+?)"' , I111Ii111 ) . group ( 1 )
   except : pass
  elif "drive.google.com/file" in I111Ii111 :
   OOoO000O0OO = re . search ( '"(https://drive.google.com/file.+?)"' , I111Ii111 )
   oOOO = iiIi1IIi1I ( OOoO000O0OO . group ( 1 ) . replace ( "preview" , "view" ) )
  elif len ( iIII1 ) != 0 :
   try :
    if "http://" not in iIII1 [ 0 ] :
     iIII1 [ 0 ] = "http://www.xomvnonline.com/" + iIII1 [ 0 ]
    oOOO = iIII1 [ 0 ]
   except : pass
  elif "app.box.com" in I111Ii111 :
   I11iiI1i1 = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( I111Ii111 ) [ 0 ]
   I1i1Iiiii = i111IiI1I ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % I11iiI1i1 )
   OOo0oO00ooO00 = json . loads ( I1i1Iiiii ) [ "file" ] [ "versionId" ]
   oOOO = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( OOo0oO00ooO00 , I11iiI1i1 )
  elif "openload" in I111Ii111 :
   try :
    oOOO = re . compile ( '"(https://openload.+?)"' ) . findall ( I111Ii111 ) [ 0 ]
    oOOO = urlresolver . resolve ( oOOO )
   except : pass
  else :
   try :
    OOoO000O0OO = re . compile ( "file: '.+?'" ) . findall ( I111Ii111 )
    if "http://" not in OOoO000O0OO [ 0 ] :
     oOOO = "http://www.xomvnonline.com/" + OOoO000O0OO [ 0 ]
    else :
     oOOO = OOoO000O0OO [ 0 ]
   except : pass
  return oOOO
 else :
  if "http://" not in OOoO000O0OO [ 0 ] :
   OOoO000O0OO [ 0 ] = "http://www.xomvnonline.com/" + OOoO000O0OO [ 0 ]
  xbmc . log ( "Embed direct url detected: %s" % OOoO000O0OO [ 0 ] )
  return OOoO000O0OO [ 0 ]
  if 90 - 90: ii1II11I1ii1I * O0o + oO0o0ooO0
def OO ( url , name ) :
 OoOoO = xbmcgui . ListItem ( name )
 OoOoO . setPath ( III1Iiii1I11 ( url ) )
 OoOoO . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoOoO )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , OoOoO )
 if 43 - 43: Ii + i11iII1iiI * OoO0O00 * O0o * o0o00Oo0O
def iiIi1IIi1I ( url , hq = True ) :
 o00oO0oo0OO = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 O0O0OOOOoo = {
 'User-Agent' : o00oO0oo0OO ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 I1i1Iiiii = requests . get ( url , headers = O0O0OOOOoo )
 oOooO0 = I1i1Iiiii . text
 try :
  OOoO000O0OO = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( oOooO0 ) [ 0 ]
  Ii1I1Ii = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : Ii1I1Ii . reverse ( )
  OOoO0 = json . loads ( OOoO000O0OO ) [ 1 ] . split ( "," )
  for OO0Oooo0oOO0O in Ii1I1Ii :
   for o00O0 in OOoO0 :
    if o00O0 . startswith ( OO0Oooo0oOO0O + "|" ) :
     url = o00O0 . split ( "|" ) [ 1 ]
     oOO0O00Oo0O0o = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( o00oO0oo0OO ) , urllib . quote_plus ( I1i1Iiiii . headers [ 'set-cookie' ] ) )
     return url + oOO0O00Oo0O0o
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , oOooO0 ) . group ( 1 )
  except : pass
  if 13 - 13: oO0OooOoO
def I111iI ( url ) :
 oOOo0 = ""
 II1I1iiIII = urllib2 . Request ( url )
 II1I1iiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 II1I1iiIII . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 oOOo0O00o = urllib2 . urlopen ( II1I1iiIII )
 url = oOOo0O00o . geturl ( )
 try :
  oOOo0 = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 oOOo0O00o . close ( )
 return oOOo0
 if 8 - 8: iI1Ii11111iIi
def i111IiI1I ( url ) :
 II1I1iiIII = urllib2 . Request ( url )
 II1I1iiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 II1I1iiIII . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 oOOo0O00o = urllib2 . urlopen ( II1I1iiIII )
 I111Ii111 = oOOo0O00o . read ( )
 oOOo0O00o . close ( )
 I111Ii111 = '' . join ( I111Ii111 . splitlines ( ) ) . replace ( '\'' , '"' )
 I111Ii111 = I111Ii111 . replace ( '\n' , '' )
 I111Ii111 = I111Ii111 . replace ( '\t' , '' )
 I111Ii111 = re . sub ( '  +' , ' ' , I111Ii111 )
 I111Ii111 = I111Ii111 . replace ( '> <' , '><' )
 return I111Ii111
 if 49 - 49: iii1II11ii - IiIii1Ii1IIi
def i11111IIIII ( url ) :
 II1I1iiIII = urllib2 . Request ( url )
 II1I1iiIII . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 II1I1iiIII . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 oOOo0O00o = urllib2 . urlopen ( II1I1iiIII )
 I111Ii111 = oOOo0O00o . read ( )
 oOOo0O00o . close ( )
 if 74 - 74: iI11I1II1I1I * iiIIIII1i1iI + ii1II11I1ii1I / o0Oo / OoO0O00 . i11iII1iiI
 I111Ii111 = I111Ii111 . replace ( '\n' , '' )
 I111Ii111 = I111Ii111 . replace ( '\t' , '' )
 I111Ii111 = re . sub ( '  +' , ' ' , I111Ii111 )
 I111Ii111 = I111Ii111 . replace ( '> <' , '><' )
 return I111Ii111
 if 62 - 62: oO0OooOoO * iii1II11ii
def OOOo00oo0oO ( name , url , mode , iconimage , mirrorname ) :
 oOOOoo0O0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 iIII1I111III = True
 IIo0o0O0O00oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 IIo0o0O0O00oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 IIo0o0O0O00oOOo . setProperty ( "IsPlayable" , "true" )
 iIII1I111III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOOoo0O0oO , listitem = IIo0o0O0O00oOOo )
 return iIII1I111III
 if 14 - 14: ii1II11I1ii1I + o00ooo0
def ooii11I ( name , url , mode , iconimage ) :
 oOOOoo0O0oO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 iIII1I111III = True
 IIo0o0O0O00oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 IIo0o0O0O00oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIII1I111III = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOOOoo0O0oO , listitem = IIo0o0O0O00oOOo , isFolder = True )
 return iIII1I111III
 if 52 - 52: oO0OooOoO - i1iIIII
def o0O0o0 ( k , e ) :
 II111iI111I1I = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for Iiooo0O in range ( len ( e ) ) :
  I1i1i1iii = k [ Iiooo0O % len ( k ) ]
  I1111i = chr ( ( 256 + ord ( e [ Iiooo0O ] ) - ord ( I1i1i1iii ) ) % 256 )
  II111iI111I1I . append ( I1111i )
 return "" . join ( II111iI111I1I )
 if 14 - 14: Oo00O0 / oO0o0ooO0
def iII11I1IiiIi ( parameters ) :
 oo0oO = { }
 if 94 - 94: iI11I1II1I1I / i11iII1iiI % oo00 * oo00 * OoO0O00
 if parameters :
  IIiIiI = parameters [ 1 : ] . split ( "&" )
  for OOO in IIiIiI :
   IIiI1i1i = OOO . split ( '=' )
   if ( len ( IIiI1i1i ) ) == 2 :
    oo0oO [ IIiI1i1i [ 0 ] ] = IIiI1i1i [ 1 ]
 return oo0oO
 if 56 - 56: O0o + ii1II11I1ii1I * i1iIIII / o00ooo0 / o0o00Oo0O * iiIIIII1i1iI
O0o0o00OO0000 = xbmc . translatePath ( iIIii1IIi . getAddonInfo ( 'profile' ) )
if 1 - 1: i1iIIII . i1iIIII / ii1II11I1ii1I - O0o
if os . path . exists ( O0o0o00OO0000 ) == False :
 os . mkdir ( O0o0o00OO0000 )
oooO = os . path . join ( O0o0o00OO0000 , 'visitor' )
if 26 - 26: O0Oooo00 % iiIIIII1i1iI
if os . path . exists ( oooO ) == False :
 from random import randint
 o00Oo0oooooo = open ( oooO , "w" )
 o00Oo0oooooo . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 o00Oo0oooooo . close ( )
 if 76 - 76: IiIii1Ii1IIi / Oo00O0 . o0o00Oo0O % iii1II11ii . oO0o0ooO0 + I11
def o0o ( utm_url ) :
 oo0 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  II1I1iiIII = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : oo0 }
 )
  oOOo0O00o = urllib2 . urlopen ( II1I1iiIII ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return oOOo0O00o
 if 61 - 61: ii1II11I1ii1I - Oo00O0 - o0Oo
def IiI1iIiIIIii ( group , name ) :
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
  oOoO = "1.0"
  oOoO00O0 = open ( oooO ) . read ( )
  OOIi1iI111II1I1 = "XomGiaiTri"
  oOOOOoOO0o = "UA-52209804-2"
  i1II1 = "www.viettv24.com"
  i11i1 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   IiiiiI1i1Iii = i11i1 + "?" + "utmwv=" + oOoO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOIi1iI111II1I1 ) + "&utmac=" + oOOOOoOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOoO00O0 , "1" , "1" , "2" ] )
   if 87 - 87: oO0o0ooO0
   if 29 - 29: iii1II11ii % Oo00O0 - iii1II11ii / Oo00O0 . o0Oo
   if 31 - 31: O0o
   if 88 - 88: iI1Ii11111iIi - i1iIIII + Oo00O0 * iii1II11ii % iI11I1II1I1I + i11iII1iiI
   if 76 - 76: iii1II11ii * oo00 % O0o
  else :
   if group == "None" :
    IiiiiI1i1Iii = i11i1 + "?" + "utmwv=" + oOoO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOIi1iI111II1I1 + "/" + name ) + "&utmac=" + oOOOOoOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOoO00O0 , "1" , "1" , "2" ] )
    if 57 - 57: iI11I1II1I1I - o0Oo / O0o - o0o00Oo0O * oO0OooOoO % OoO0O00
    if 68 - 68: oO0OooOoO * IiIii1Ii1IIi % ii1II11I1ii1I - I11
    if 34 - 34: O0o . iI11I1II1I1I * ii1II11I1ii1I * o00ooo0 / O0o / iiIIIII1i1iI
    if 78 - 78: i11iII1iiI - oO0o0ooO0 / ii1II11I1ii1I
    if 10 - 10: oo00 + i11iII1iiI * iiIIIII1i1iI + iI11I1II1I1I / O0o / iiIIIII1i1iI
   else :
    IiiiiI1i1Iii = i11i1 + "?" + "utmwv=" + oOoO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOIi1iI111II1I1 + "/" + group + "/" + name ) + "&utmac=" + oOOOOoOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , oOoO00O0 , "1" , "1" , "2" ] )
    if 42 - 42: iii1II11ii
    if 38 - 38: Oo00O0 + OoO0O00 % i1iIIII % ii1II11I1ii1I - O0Oooo00 / oO0OooOoO
    if 73 - 73: oO0o0ooO0 * o0o00Oo0O - Ii
    if 85 - 85: O0Oooo00 % oo00 + IiIii1Ii1IIi / oO0o0ooO0 . o00ooo0 + Oo00O0
    if 62 - 62: Ii + Ii - oO0o0ooO0
    if 28 - 28: oo00 . oo00 % iI11I1II1I1I * iI11I1II1I1I . oO0o0ooO0 / oo00
  print "============================ POSTING ANALYTICS ============================"
  o0o ( IiiiiI1i1Iii )
  if 27 - 27: iI1Ii11111iIi + i1iIIII - o0Oo
  if not group == "None" :
   O00oOOooo = i11i1 + "?" + "utmwv=" + oOoO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( i1II1 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + OOIi1iI111II1I1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( OOIi1iI111II1I1 ) + "&utmac=" + oOOOOoOO0o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , oOoO00O0 , "1" , "2" ] )
   if 50 - 50: iiIIIII1i1iI % o0o00Oo0O * oO0o0ooO0
   if 5 - 5: I11 * ii1II11I1ii1I
   if 5 - 5: O0o
   if 90 - 90: O0o . i1iIIII / O0Oooo00 - IiIii1Ii1IIi
   if 40 - 40: oO0OooOoO
   if 25 - 25: I11 + O0Oooo00 / i1iIIII . oO0o0ooO0 % o0o00Oo0O * iI1Ii11111iIi
   if 84 - 84: i1iIIII % O0Oooo00 + Ii
   if 28 - 28: i11iII1iiI + iI1Ii11111iIi * Oo00O0 % o00ooo0 . IiIii1Ii1IIi % o0o00Oo0O
   try :
    print "============================ POSTING TRACK EVENT ============================"
    o0o ( O00oOOooo )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 16 - 16: IiIii1Ii1IIi - iI11I1II1I1I / iii1II11ii . OoO0O00 + iI11I1II1I1I
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 19 - 19: iI1Ii11111iIi - i11iII1iiI . o0o00Oo0O
ooOo00 = iII11I1IiiIi ( sys . argv [ 2 ] )
OOoo = ooOo00 . get ( 'mode' )
IIi1i = ooOo00 . get ( 'url' )
iIIiiiI = ooOo00 . get ( 'name' )
if type ( IIi1i ) == type ( str ( ) ) :
 IIi1i = urllib . unquote_plus ( IIi1i )
if type ( iIIiiiI ) == type ( str ( ) ) :
 iIIiiiI = urllib . unquote_plus ( iIIiiiI )
 if 60 - 60: iii1II11ii . O0o
IiI111ii1ii = str ( sys . argv [ 1 ] )
if OOoo == 'index' :
 IiI1iIiIIIii ( "Browse" , iIIiiiI )
 oO0OOoO0 ( IIi1i )
elif OOoo == 'search' :
 IiI1iIiIIIii ( "None" , "Search" )
 OoOO0oo0o ( )
elif OOoo == 'videosbyregion' :
 IiI1iIiIIIii ( "Browse" , iIIiiiI )
 oO0ooO0OoOOOO ( )
elif OOoo == 'videosbycategory' :
 IiI1iIiIIIii ( "Browse" , iIIiiiI )
 I1 ( )
elif OOoo == 'mirrors' :
 IiI1iIiIIIii ( "Browse" , iIIiiiI )
 oO00o0 ( IIi1i )
elif OOoo == 'episodes' :
 IiI1iIiIIIii ( "Browse" , iIIiiiI )
 IiO0OOO ( IIi1i , iIIiiiI )
elif OOoo == 'loadvideo' :
 IiI1iIiIIIii ( "Play" , iIIiiiI + "/" + IIi1i )
 O0OOo = xbmcgui . DialogProgress ( )
 O0OOo . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 OO ( IIi1i , iIIiiiI )
 O0OOo . close ( )
 del O0OOo
else :
 IiI1iIiIIIii ( "None" , "None" )
 Oo000 ( )
xbmcplugin . endOfDirectory ( int ( IiI111ii1ii ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
