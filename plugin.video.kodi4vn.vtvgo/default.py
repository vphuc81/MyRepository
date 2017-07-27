#!/usr/bin/python
# coding=utf-8
import urllib , requests , re , json , HTMLParser , os , uuid , datetime , time
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
requests . packages . urllib3 . disable_warnings ( )
oo000 = Plugin ( )
ii = HTMLParser . HTMLParser ( )
oOOo = "plugin://plugin.video.kodi4vn.vtvgo"
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
IIi1IiiiI1Ii = "http://echipstore.com:8000/vntime"
if 39 - 39: O0 - ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
def Ii1I ( s ) :
 s = '' . join ( s . splitlines ( ) ) . replace ( '\'' , '"' )
 s = s . replace ( '\n' , '' )
 s = s . replace ( '\t' , '' )
 s = re . sub ( '  +' , ' ' , s )
 s = s . replace ( '> <' , '><' )
 return ii . unescape ( s )
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
@ oo000 . route ( '/list_date/<args_json>' )
def O0oOO0o0 ( args_json = { } ) :
 i1ii1iIII = [ ]
 Oo0oO0oo0oO00 = json . loads ( args_json )
 i111I = requests . get ( IIi1IiiiI1Ii ) . text
 Oo0oO0oo0oO00 [ "date" ] = i111I [ : 10 ] . replace ( "-" , "" )
 II1Ii1iI1i (
 "[List date] from %s" % (
 Oo0oO0oo0oO00 [ "date" ]
 ) ,
 '/list_date/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 if 12 - 12: o0oOoO00o
 i1 = datetime . datetime ( year = 2016 , month = 1 , day = 1 )
 if 64 - 64: oo % O0Oooo00
 if 87 - 87: i1IIi11111i / ooOO00oOo % o0oOoO00o * o0oOoO00o * o00O0oo / iiiIIii1IIi
 if 88 - 88: o0oOoO00o / ooOO00oOo + I1IiiI % iII111iiiii11 . oo / i1IIi11111i
 try :
  I1I1i1 = datetime . datetime . strptime ( i111I , "%Y-%m-%d %H:%M" )
 except TypeError :
  I1I1i1 = datetime . datetime ( * ( time . strptime ( i111I , "%Y-%m-%d %H:%M" ) [ 0 : 6 ] ) )
  if 18 - 18: iiiIIii1IIi / ooOoO0o + IiII / oOo0O0Ooo - O0 - ooOoO0o
 for I111IiIi in xrange ( 1 , ( I1I1i1 - i1 ) . days ) :
  IiiIIiiI11 = { }
  OOooO = ( I1I1i1 - datetime . timedelta ( days = I111IiIi ) )
  IiiIIiiI11 [ "label" ] = "%s %s" % ( OOooO . strftime ( "%Y-%m-%d" ) , Oo0oO0oo0oO00 [ "title" ] )
  OOoO00o = {
 "title" : Oo0oO0oo0oO00 [ "title" ] ,
 "url" : Oo0oO0oo0oO00 [ "url" ] ,
 "date" : OOooO . strftime ( "%Y-%m-%d" ) ,
 "channel_id" : Oo0oO0oo0oO00 [ "channel_id" ]
 }
  IiiIIiiI11 [ "path" ] = '%s/list_media/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  IiiIIiiI11 [ "thumbnail" ] = "https://docs.google.com/drawings/d/16wuwv1LBUL030G13aypfrRxpQ8rs6b011WnQc_uF0z4/pub?w=256&h=256"
  i1ii1iIII . append ( IiiIIiiI11 )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1ii1iIII , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1ii1iIII , view_mode = 52 )
  else :
   return oo000 . finish ( i1ii1iIII )
 else :
  return oo000 . finish ( i1ii1iIII )
  if 9 - 9: ooOO00oOo - o00O0oo % I1IiiI % iII111iiiii11
  if 3 - 3: o0oOoO00o + OO0OO0O0O0
@ oo000 . route ( '/list_media/<args_json>' )
def I1Ii ( args_json = { } ) :
 i1ii1iIII = [ ]
 Oo0oO0oo0oO00 = json . loads ( args_json )
 o0oOo0Ooo0O = [ ]
 if Oo0oO0oo0oO00 [ "date" ] == "" :
  o0oOo0Ooo0O = requests . get ( IIi1IiiiI1Ii ) . text . split ( " " )
  Oo0oO0oo0oO00 [ "date" ] = o0oOo0Ooo0O [ 0 ]
  if 81 - 81: iII111i * oo * ooOoO0o - o0oOoO00o - iiiiIi11i
 OooO0OO = requests . get ( Oo0oO0oo0oO00 [ "url" ] % ( Oo0oO0oo0oO00 [ "date" ] , Oo0oO0oo0oO00 [ "channel_id" ] ) ) . text
 II1Ii1iI1i (
 "[Browse Media of] %s" % (
 Oo0oO0oo0oO00 [ "title" ] if "title" in Oo0oO0oo0oO00 else "Unknow Title"
 ) ,
 '/list_media/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 if 28 - 28: O0
 iii11iII = re . compile ( '(?s)<li id="(.+?)"[^>]*>.+?(\d\d\:\d\d).+?<h3>(.+?)</h3>.+?<i>(.*?)</i></h4>' ) . findall ( OooO0OO )
 if len ( o0oOo0Ooo0O ) > 0 :
  i1I111I = [ ]
  i11I1IIiiIi = time . strptime ( o0oOo0Ooo0O [ 1 ] , "%H:%M" )
  IiIiIi = II ( i11I1IIiiIi )
  for I111IiIi in iii11iII :
   iI = time . strptime ( I111IiIi [ 1 ] , "%H:%M" )
   if II ( iI ) <= IiIiIi :
    i1I111I += [ I111IiIi ]
   else : break
  iii11iII = i1I111I [ : : - 1 ]
  if 22 - 22: oOo0O0Ooo % o00O0oo
 for ooOO0O00 , iI , ii1 , o0oO0o00oo in iii11iII :
  IiiIIiiI11 = { }
  II1i1Ii11Ii11 = "http://vtvgo.vn/ajax-get-epg-detail?epg_id=" + ooOO0O00 . split ( "_" ) [ - 1 ]
  IiiIIiiI11 [ "label" ] = "[B][%s %s][/B] %s - %s" % ( Oo0oO0oo0oO00 [ "date" ] , iI , ii1 , o0oO0o00oo )
  OOoO00o = {
 "title" : IiiIIiiI11 [ "label" ] ,
 "url" : II1i1Ii11Ii11
 }
  IiiIIiiI11 [ "path" ] = '%s/play/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  IiiIIiiI11 [ "is_playable" ] = True
  i1ii1iIII += [ IiiIIiiI11 ]
  if 35 - 35: iiiiIi11i + o0oOoO00o + o0oOoO00o
 if len ( o0oOo0Ooo0O ) > 0 :
  i1ii1iIII [ 0 ] [ "label" ] = "[B][%s %s Đang chiếu...][/B] %s - %s" % ( Oo0oO0oo0oO00 [ "date" ] . encode ( "utf8" ) , o0oOo0Ooo0O [ 1 ] . encode ( "utf8" ) , iii11iII [ 0 ] [ 2 ] . encode ( "utf8" ) , iii11iII [ 0 ] [ 3 ] . encode ( "utf8" ) )
  OOoO00o = {
 "title" : i1ii1iIII [ 0 ] [ "label" ] ,
 "url" : "http://vtvgo.vn/?xem-truc-tuyen-vtv-%s.html" % Oo0oO0oo0oO00 [ "channel_id" ]
 }
  i1ii1iIII [ 0 ] [ "path" ] = '%s/play/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( OOoO00o ) )
 )
  if 11 - 11: o0oOoO00o - Ooo00oOo00o % i1IIi11111i % o0oOoO00o / oOoO0oo0OOOo - Ooo00oOo00o
 o0o0oOOOo0oo = { }
 o0o0oOOOo0oo [ "label" ] = "Xem thêm..."
 o0o0oOOOo0oo [ "path" ] = '%s/list_date/%s' % (
 oOOo ,
 urllib . quote_plus ( json . dumps ( Oo0oO0oo0oO00 ) )
 )
 o0o0oOOOo0oo [ "thumbnail" ] = "https://docs.google.com/drawings/d/16wuwv1LBUL030G13aypfrRxpQ8rs6b011WnQc_uF0z4/pub?w=256&h=256"
 i1ii1iIII . append ( o0o0oOOOo0oo )
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( i1ii1iIII , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( i1ii1iIII , view_mode = 52 )
  else :
   return oo000 . finish ( i1ii1iIII )
 else :
  return oo000 . finish ( i1ii1iIII )
  if 80 - 80: ooOoO0o * Oo0Ooo / O0Oooo00
@ oo000 . route ( '/play/<args_json>' )
def I11II1i ( args_json = { } ) :
 Oo0oO0oo0oO00 = json . loads ( args_json )
 II1Ii1iI1i (
 "[Play] %s" % (
 Oo0oO0oo0oO00 [ "title" ] . encode ( "utf8" ) if "title" in Oo0oO0oo0oO00 else "Unknow Title"
 ) ,
 '/play/%s/%s' % (
 Oo0oO0oo0oO00 [ "url" ] ,
 json . dumps ( Oo0oO0oo0oO00 [ "payloads" ] ) if "payloads" in Oo0oO0oo0oO00 else "{}"
 )
 )
 IIIII = xbmcgui . DialogProgress ( )
 IIIII . create ( 'VTVGo' , 'Đang tải, Xin quý khách vui lòn đợi trong giây lát...' )
 oo000 . set_resolved_url ( ooooooO0oo ( Oo0oO0oo0oO00 [ "url" ] ) , subtitles = "https://raw.githubusercontent.com/vinhcomp/xml/master/xml/sub1.tsv" )
 IIIII . close ( )
 del IIIII
 if 49 - 49: iiiiIi11i * iiiIIii1IIi / I1IiiI / Oo0Ooo / iiiiIi11i
def ooooooO0oo ( url ) :
 I1i1I1II = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 }
 i1IiIiiI = "|Referer=http%3A%2F%2Fvtvgo.vn%2F"
 try :
  if "ajax-get-epg-detail" in url :
   I1I = requests . get ( url , headers = I1i1I1II )
   return I1I . json ( ) [ "data" ]
  else :
   I1I = requests . get ( url , headers = I1i1I1II )
   return re . search ( "addPlayer\('(.+?.m3u8)" , I1I . text ) . group ( 1 ) + i1IiIiiI
 except :
  return ""
  if 80 - 80: oOoO0oo0OOOo - Ooo00oOo00o
def II ( time_object ) :
 return time_object . tm_hour * 60 + time_object . tm_min
 if 87 - 87: IiII / ooOoO0o - I1IiiI * I1Ii111 / iII111iiiii11 . OO0OO0O0O0
def II1Ii1iI1i ( title = "Home" , page = "/" ) :
 iii11I111 = "http://www.google-analytics.com/collect"
 OOOO00ooo0Ooo = open ( OOOooOooo00O0 ) . read ( )
 Oo0OO = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : OOOO00ooo0Ooo ,
 't' : 'pageview' ,
 'dp' : "VTVGo" + page ,
 'dt' : "[VTVGo] - %s" % title
 }
 requests . post ( iii11I111 , data = urllib . urlencode ( Oo0OO ) )
 if 92 - 92: IiII - oOoO0oo0OOOo
i11i1 = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( i11i1 ) == False :
 os . mkdir ( i11i1 )
OOOooOooo00O0 = os . path . join ( i11i1 , 'cid' )
if 29 - 29: iII111i % ooOO00oOo + i1IIi11111i / iiiiIi11i + I1Ii111 * iiiiIi11i
if os . path . exists ( OOOooOooo00O0 ) == False :
 with open ( OOOooOooo00O0 , "w" ) as i1I1iI :
  i1I1iI . write ( str ( uuid . uuid1 ( ) ) )
  if 93 - 93: iiiIIii1IIi % IiII * I1IiiI
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
