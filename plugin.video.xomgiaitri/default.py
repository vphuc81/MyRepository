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
 ooii11I ( 'Search' , 'http://www.xomgiaitri.com/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 ooii11I ( 'Phim Lẻ' , 'http://www.xomgiaitri.com/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 ooii11I ( 'Phim Bộ' , 'http://www.xomgiaitri.com/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 ooii11I ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomgiaitri.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 ooii11I ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomgiaitri.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
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
 ooii11I ( "Hồng Kong" , "http://www.xomgiaitri.com/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ooii11I ( "Hồng Kong (VNLT)" , "http://www.xomgiaitri.com/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ooii11I ( "Hàn Quốc" , "http://www.xomgiaitri.com/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ooii11I ( "Hàn Quốc (vietsub)" , "http://www.xomgiaitri.com/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ooii11I ( "Trung Quốc" , "http://www.xomgiaitri.com/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ooii11I ( "Đài Loan" , "http://www.xomgiaitri.com/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ooii11I ( "Việt Nam" , "http://www.xomgiaitri.com/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ooii11I ( "Thái Lan" , "http://www.xomgiaitri.com/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ooii11I ( "Các Loại Khác" , "http://www.xomgiaitri.com/category/7/cac-loai-khac.html" , "index" , "" )
 if 46 - 46: Oo00O0 / iiIIIII1i1iI
def I1 ( ) :
 ooii11I ( "Hành Động" , "http://www.xomgiaitri.com/category/8/hanh-dong.html" , "index" , "" )
 ooii11I ( "Tình Cảm" , "http://www.xomgiaitri.com/category/9/tinh-cam.html" , "index" , "" )
 ooii11I ( "Phim Hài" , "http://www.xomgiaitri.com/category/10/phim-hai.html" , "index" , "" )
 ooii11I ( "Kinh Dị" , "http://www.xomgiaitri.com/category/11/kinh-di.html" , "index" , "" )
 ooii11I ( "Kiếm Hiệp" , "http://www.xomgiaitri.com/category/12/kiem-hiep.html" , "index" , "" )
 ooii11I ( "Việt Nam" , "http://www.xomgiaitri.com/category/15/viet-nam.html" , "index" , "" )
 ooii11I ( "Hài Kịch" , "http://www.xomgiaitri.com/category/16/hai-kich.html" , "index" , "" )
 ooii11I ( "Ca Nhạc" , "http://www.xomgiaitri.com/category/17/ca-nhac.html" , "index" , "" )
 ooii11I ( "Cải Lương" , "http://www.xomgiaitri.com/category/18/cai-luong.html" , "index" , "" )
 ooii11I ( "Phóng Sự" , "http://www.xomgiaitri.com/category/19/phong-su.html" , "index" , "" )
 ooii11I ( "Các Loại Khác" , "http://www.xomgiaitri.com/category/20/cac-loai-khac.html" , "index" , "" )
 if 71 - 71: Oo00O0 + i1iIIII % Ii + iiIIIII1i1iI - I11
def oO0OOoO0 ( url ) :
 I111Ii111 = i111IiI1I ( url )
 O0 = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( I111Ii111 )
 for iII , o0 , ooOooo000oOO in O0 :
  ooOooo000oOO = "http://www.xomgiaitri.com/" + ooOooo000oOO
  ooOooo000oOO = "/" . join ( ooOooo000oOO . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( ooOooo000oOO . split ( "/" ) [ - 1 ] )
  ooii11I ( "[B]" + o0 + "[/B]" , "http://www.xomgiaitri.com/xem" + iII , 'mirrors' , ooOooo000oOO )
 Oo0oOOo = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( I111Ii111 . replace ( "'" , '"' ) )
 for iII , Oo0OoO00oOO0o in Oo0oOOo :
  ooii11I ( Oo0OoO00oOO0o , iII . replace ( "./" , "http://www.xomgiaitri.com/" ) , 'index' , "" )
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
  OOOo00oo0oO ( "Part - " + i1IiiiI1iI . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomgiaitri.com/" + IIiIi1iI , 'loadvideo' , '' , name )
  if 49 - 49: O0Oooo00 / iI1Ii11111iIi . OoO0O00
def Oo0ooOo0o ( url ) :
 url = url . replace ( "/xem/" , "/" )
 ooOOoooooo = i111IiI1I ( url )
 return re . search ( '<a title="Xem Phim Online" href="(.+?)"' , ooOOoooooo ) . group ( 1 )
 if 1 - 1: i11iII1iiI / oO0o0ooO0 % oo00 * I11 . Ii
def III1Iiii1I11 ( url ) :
 if 9 - 9: iiIIIII1i1iI / i11iII1iiI - iii1II11ii / oO0OooOoO / iI11I1II1I1I - oO0o0ooO0
 def o00oooO0Oo ( url ) :
  o0O0OOO0Ooo = re . search ( "ok.ru/video(?:embed)*/(\d+)" , url ) . group ( 1 )
  iiIiI = "https://m.ok.ru/video/%s" % o0O0OOO0Ooo
  I111Ii111 = i111IiI1I ( iiIiI )
  return ( oo000 . unescape ( re . search ( "(https://m.ok.ru/dk\?st.+?)\&" , I111Ii111 ) . group ( 1 ) ) ) . decode ( 'unicode_escape' )
  if 6 - 6: I11 . o00ooo0 * ii1II11I1ii1I - O0Oooo00 - I11
 I111Ii111 = i111IiI1I ( url )
 try :
  OOoO000O0OO = re . search ( 'src=(?:\'|\")(https*\://www[.]dailymotion[.]com/.+?)(?:\'|\")' , I111Ii111 ) . group ( 1 )
  return urlresolver . resolve ( OOoO000O0OO )
 except : pass
 if 45 - 45: iii1II11ii - oO0OooOoO + iI11I1II1I1I . iii1II11ii * IiIii1Ii1IIi
 try :
  try :
   OOoO000O0OO = re . search ( "'proxy.link', '(.+?)'" , I111Ii111 ) . group ( 1 )
  except : pass
  try :
   OOoO000O0OO = re . search ( 'src="(http\://www[.]thvads[.]com/.+?|http\://play[.]xomgiaitri[.]net/.+?)"' , I111Ii111 ) . group ( 1 )
  except : pass
  I111Ii111 = i111IiI1I ( OOoO000O0OO )
 except : pass
 try :
  oOOO = json . loads ( re . search ( 'var sources = (\[.+?\])' , I111Ii111 ) . group ( 1 ) )
  oOOO = sorted ( oOOO , key = lambda iIII1 : int ( re . search ( "\d+" , iIII1 [ "label" ] ) . group ( 0 ) ) )
  return oOOO [ - 1 ] [ "file" ]
 except : pass
 try :
  url = o00oooO0Oo ( I111Ii111 )
  return url
 except : pass
 return None
 if 65 - 65: o0o00Oo0O
def oO00OOoO00 ( url , name ) :
 IiI111111IIII = xbmcgui . ListItem ( name )
 IiI111111IIII . setPath ( III1Iiii1I11 ( url ) )
 IiI111111IIII . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI111111IIII )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , IiI111111IIII )
 if 37 - 37: O0o / ii1II11I1ii1I
def i1 ( url , hq = True ) :
 I1iI1iIi111i = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 iiIi1IIi1I = {
 'User-Agent' : I1iI1iIi111i ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 o0OoOO000ooO0 = requests . get ( url , headers = iiIi1IIi1I )
 o0o0o0oO0oOO = o0OoOO000ooO0 . text
 try :
  OOoO000O0OO = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( o0o0o0oO0oOO ) [ 0 ]
  ii1Ii11I = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : ii1Ii11I . reverse ( )
  o00o0 = json . loads ( OOoO000O0OO ) [ 1 ] . split ( "," )
  for ii in ii1Ii11I :
   for OOooooO0Oo in o00o0 :
    if OOooooO0Oo . startswith ( ii + "|" ) :
     url = OOooooO0Oo . split ( "|" ) [ 1 ]
     OO = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( I1iI1iIi111i ) , urllib . quote_plus ( o0OoOO000ooO0 . headers [ 'set-cookie' ] ) )
     return url + OO
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , o0o0o0oO0oOO ) . group ( 1 )
  except : pass
  if 25 - 25: iI1Ii11111iIi
def oOo0oO ( url ) :
 OOOO0oo0 = ""
 I11iiI1i1 = urllib2 . Request ( url )
 I11iiI1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 I11iiI1i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1i1Iiiii = urllib2 . urlopen ( I11iiI1i1 )
 url = I1i1Iiiii . geturl ( )
 try :
  OOOO0oo0 = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 I1i1Iiiii . close ( )
 return OOOO0oo0
 if 94 - 94: oO0o0ooO0 * O0Oooo00 / i11iII1iiI / O0Oooo00
def i111IiI1I ( url ) :
 I11iiI1i1 = urllib2 . Request ( url )
 I11iiI1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 I11iiI1i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1i1Iiiii = urllib2 . urlopen ( I11iiI1i1 )
 I111Ii111 = I1i1Iiiii . read ( )
 I1i1Iiiii . close ( )
 I111Ii111 = '' . join ( I111Ii111 . splitlines ( ) ) . replace ( '\'' , '"' )
 I111Ii111 = I111Ii111 . replace ( '\n' , '' )
 I111Ii111 = I111Ii111 . replace ( '\t' , '' )
 I111Ii111 = re . sub ( '  +' , ' ' , I111Ii111 )
 I111Ii111 = I111Ii111 . replace ( '> <' , '><' )
 return I111Ii111
 if 87 - 87: i11iII1iiI . I11
def O0OO0O ( url ) :
 I11iiI1i1 = urllib2 . Request ( url )
 I11iiI1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 I11iiI1i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I1i1Iiiii = urllib2 . urlopen ( I11iiI1i1 )
 I111Ii111 = I1i1Iiiii . read ( )
 I1i1Iiiii . close ( )
 if 81 - 81: o00ooo0 . oO0o0ooO0 % o0o00Oo0O / iii1II11ii - o00ooo0
 I111Ii111 = I111Ii111 . replace ( '\n' , '' )
 I111Ii111 = I111Ii111 . replace ( '\t' , '' )
 I111Ii111 = re . sub ( '  +' , ' ' , I111Ii111 )
 I111Ii111 = I111Ii111 . replace ( '> <' , '><' )
 return I111Ii111
 if 43 - 43: Ii + i11iII1iiI * OoO0O00 * O0o * o0o00Oo0O
def OOOo00oo0oO ( name , url , mode , iconimage , mirrorname ) :
 o00oO0oo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 O0O0OOOOoo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oOooO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOooO0 . setProperty ( "IsPlayable" , "true" )
 O0O0OOOOoo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00oO0oo0OO , listitem = oOooO0 )
 return O0O0OOOOoo
 if 29 - 29: iI11I1II1I1I + ii1II11I1ii1I * iI1Ii11111iIi * Oo00O0 . iii1II11ii * iii1II11ii
def ooii11I ( name , url , mode , iconimage ) :
 o00oO0oo0OO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0O0OOOOoo = True
 oOooO0 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oOooO0 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O0O0OOOOoo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o00oO0oo0OO , listitem = oOooO0 , isFolder = True )
 return O0O0OOOOoo
 if 7 - 7: I11 * O0o % O0Oooo00 - oO0o0ooO0
def i1i ( k , e ) :
 oOOoo00O00o = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for Iiooo0O in range ( len ( e ) ) :
  O0O00Oo = k [ Iiooo0O % len ( k ) ]
  oooooo0O000o = chr ( ( 256 + ord ( e [ Iiooo0O ] ) - ord ( O0O00Oo ) ) % 256 )
  oOOoo00O00o . append ( oooooo0O000o )
 return "" . join ( oOOoo00O00o )
 if 64 - 64: iii1II11ii . oO0o0ooO0 - O0o / oO0OooOoO
def O0O0ooOOO ( parameters ) :
 oOOo0O00o = { }
 if 8 - 8: iI1Ii11111iIi
 if parameters :
  ii1111iII = parameters [ 1 : ] . split ( "&" )
  for iiiiI in ii1111iII :
   oooOo0OOOoo0 = iiiiI . split ( '=' )
   if ( len ( oooOo0OOOoo0 ) ) == 2 :
    oOOo0O00o [ oooOo0OOOoo0 [ 0 ] ] = oooOo0OOOoo0 [ 1 ]
 return oOOo0O00o
 if 51 - 51: i11iII1iiI / ii1II11I1ii1I . Oo00O0 * oO0o0ooO0 + iI1Ii11111iIi * I11
OOOoOo = xbmc . translatePath ( iIIii1IIi . getAddonInfo ( 'profile' ) )
if 51 - 51: i1iIIII / iI11I1II1I1I % i11iII1iiI * iii1II11ii % O0o
if os . path . exists ( OOOoOo ) == False :
 os . mkdir ( OOOoOo )
oOoooOOO = os . path . join ( OOOoOo , 'visitor' )
if 52 - 52: oO0OooOoO - i1iIIII
if os . path . exists ( oOoooOOO ) == False :
 from random import randint
 o0O0o0 = open ( oOoooOOO , "w" )
 o0O0o0 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 o0O0o0 . close ( )
 if 37 - 37: iiIIIII1i1iI * IiIii1Ii1IIi % Ii % i1iIIII + O0Oooo00
def OOoOO0o0o0 ( utm_url ) :
 ii1I1 = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  I11iiI1i1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : ii1I1 }
 )
  I1i1Iiiii = urllib2 . urlopen ( I11iiI1i1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return I1i1Iiiii
 if 93 - 93: o0o00Oo0O % o0Oo . Oo00O0 / iii1II11ii - O0o / iii1II11ii
def II1IiiIi1i ( group , name ) :
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
  iiI11ii1I1 = "1.0"
  Ooo0OOoOoO0 = open ( oOoooOOO ) . read ( )
  oOo0OOoO0 = "XomGiaiTri"
  IIo0Oo0oO0oOO00 = "UA-52209804-2"
  oo00OO0000oO = "www.viettv24.com"
  I1II1 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oooO = I1II1 + "?" + "utmwv=" + iiI11ii1I1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOo0OOoO0 ) + "&utmac=" + IIo0Oo0oO0oOO00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Ooo0OOoOoO0 , "1" , "1" , "2" ] )
   if 26 - 26: O0Oooo00 % iiIIIII1i1iI
   if 76 - 76: I11 * oo00
   if 52 - 52: Oo00O0
   if 19 - 19: iii1II11ii
   if 25 - 25: O0Oooo00 / i1iIIII
  else :
   if group == "None" :
    oooO = I1II1 + "?" + "utmwv=" + iiI11ii1I1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOo0OOoO0 + "/" + name ) + "&utmac=" + IIo0Oo0oO0oOO00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Ooo0OOoOoO0 , "1" , "1" , "2" ] )
    if 31 - 31: Oo00O0 . o0o00Oo0O % iii1II11ii . oO0o0ooO0 + I11
    if 71 - 71: O0o . OoO0O00
    if 62 - 62: oO0OooOoO . IiIii1Ii1IIi
    if 61 - 61: ii1II11I1ii1I - Oo00O0 - o0Oo
    if 25 - 25: o0o00Oo0O * IiIii1Ii1IIi + iiIIIII1i1iI . oO0o0ooO0 . oO0o0ooO0
   else :
    oooO = I1II1 + "?" + "utmwv=" + iiI11ii1I1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOo0OOoO0 + "/" + group + "/" + name ) + "&utmac=" + IIo0Oo0oO0oOO00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , Ooo0OOoOoO0 , "1" , "1" , "2" ] )
    if 58 - 58: iii1II11ii
    if 53 - 53: o0Oo
    if 59 - 59: oO0o0ooO0
    if 81 - 81: ii1II11I1ii1I - ii1II11I1ii1I . oo00
    if 73 - 73: IiIii1Ii1IIi % Ii - iii1II11ii
    if 7 - 7: o0o00Oo0O * Ii * O0Oooo00 + i1iIIII % iI1Ii11111iIi - i1iIIII
  print "============================ POSTING ANALYTICS ============================"
  OOoOO0o0o0 ( oooO )
  if 39 - 39: i11iII1iiI * Oo00O0 % Oo00O0 - oO0OooOoO + oO0o0ooO0 - IiIii1Ii1IIi
  if not group == "None" :
   iiO0oOo00o = I1II1 + "?" + "utmwv=" + iiI11ii1I1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( oo00OO0000oO ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oOo0OOoO0 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oOo0OOoO0 ) + "&utmac=" + IIo0Oo0oO0oOO00 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , Ooo0OOoOoO0 , "1" , "2" ] )
   if 81 - 81: I11 % o0Oo . iI11I1II1I1I
   if 4 - 4: Ii % iI1Ii11111iIi % o0Oo / I11
   if 6 - 6: oo00 / iii1II11ii % Oo00O0 - iii1II11ii
   if 31 - 31: Oo00O0
   if 23 - 23: O0o . I11
   if 92 - 92: ii1II11I1ii1I + O0o * O0Oooo00 % iii1II11ii
   if 42 - 42: i11iII1iiI
   if 76 - 76: iii1II11ii * oo00 % O0o
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OOoOO0o0o0 ( iiO0oOo00o )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 57 - 57: iI11I1II1I1I - o0Oo / O0o - o0o00Oo0O * oO0OooOoO % OoO0O00
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 68 - 68: oO0OooOoO * IiIii1Ii1IIi % ii1II11I1ii1I - I11
I1oOoOo0O0OOOoO = O0O0ooOOO ( sys . argv [ 2 ] )
iI11IIIiii1II = I1oOoOo0O0OOOoO . get ( 'mode' )
IIi1i = I1oOoOo0O0OOOoO . get ( 'url' )
i1II1i = I1oOoOo0O0OOOoO . get ( 'name' )
if type ( IIi1i ) == type ( str ( ) ) :
 IIi1i = urllib . unquote_plus ( IIi1i )
if type ( i1II1i ) == type ( str ( ) ) :
 i1II1i = urllib . unquote_plus ( i1II1i )
 if 83 - 83: ii1II11I1ii1I - O0Oooo00 / IiIii1Ii1IIi / O0o + o00ooo0 - o0o00Oo0O
I11I1i1iIII1I = str ( sys . argv [ 1 ] )
if iI11IIIiii1II == 'index' :
 II1IiiIi1i ( "Browse" , i1II1i )
 oO0OOoO0 ( IIi1i )
elif iI11IIIiii1II == 'search' :
 II1IiiIi1i ( "None" , "Search" )
 OoOO0oo0o ( )
elif iI11IIIiii1II == 'videosbyregion' :
 II1IiiIi1i ( "Browse" , i1II1i )
 oO0ooO0OoOOOO ( )
elif iI11IIIiii1II == 'videosbycategory' :
 II1IiiIi1i ( "Browse" , i1II1i )
 I1 ( )
elif iI11IIIiii1II == 'mirrors' :
 II1IiiIi1i ( "Browse" , i1II1i )
 oO00o0 ( IIi1i )
elif iI11IIIiii1II == 'episodes' :
 II1IiiIi1i ( "Browse" , i1II1i )
 IiO0OOO ( IIi1i , i1II1i )
elif iI11IIIiii1II == 'loadvideo' :
 II1IiiIi1i ( "Play" , i1II1i + "/" + IIi1i )
 iII1i11 = xbmcgui . DialogProgress ( )
 iII1i11 . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 oO00OOoO00 ( IIi1i , i1II1i )
 iII1i11 . close ( )
 del iII1i11
else :
 II1IiiIi1i ( "None" , "None" )
 Oo000 ( )
xbmcplugin . endOfDirectory ( int ( I11I1i1iIII1I ) )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
