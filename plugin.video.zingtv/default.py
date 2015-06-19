#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.zingtv'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = ""
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( ) :
 i1I11i ( 'Tìm kiếm' , '' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
 i1I11i ( 'Thiếu nhi' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9ZIW8&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'TV Show' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0CE&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Phim Truyền Hình' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DW&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Hài kịch' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0D6&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Âm nhạc' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DC&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Video Games' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9ZIU8&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Hoạt hình' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DO&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Giáo dục' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0D7&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Thể thao' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DI&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Tin tức - Sự kiện' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0CF&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 if 73 - 73: III - oo00oOOo * Oooo000o % OOo . OOO
 IiI1ii1 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: IiI1ii1 = xbmc . translatePath ( os . path . join ( IiI1ii1 , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/zingtv.jpg' , IiI1ii1 )
 if 49 - 49: oooOOooo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI1ii1 )
 if 49 - 49: o0oo0oo0OO00 = xbmcgui . WindowDialog ( )
 if 49 - 49: o0oo0oo0OO00 . addControl ( oooOOooo )
 if 49 - 49: o0oo0oo0OO00 . doModal ( )
 if 20 - 20: i111iII
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 25 - 25: O0 + OoOoOoO0o0OO * Ooo0OO0oOO * Ii * o0o - OOO0o0o
def Ii1iI ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 Ooo = re . compile ( '<a class="content-items" href="(.+?)"><span class="video-img"><img alt="(.+?)" src="(.+?)" [^>]*>(.+?)<h4>(.+?)</h4>' ) . findall ( Oo )
 for o0oOoO00o , i1 , oOOoo00O0O , i1111 , i11 in reversed ( Ooo ) :
  I11 ( "[" + i11 + "] - " + i1 , "http://tv.zing.vn" + o0oOoO00o , 'loadvideo' , oOOoo00O0O )
 if ( len ( Ooo ) == 50 ) :
  Oo0o0000o0o0 = int ( re . compile ( '&page=(.+?)&' ) . findall ( url ) [ 0 ] )
  url = url . replace ( "&page=" + str ( Oo0o0000o0o0 ) , "&page=" + str ( Oo0o0000o0o0 + 1 ) )
  i1I11i ( "Next >>" , url , 'indexvideo' , "" )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 86 - 86: iiiii11iII1 % O0o
def oO0 ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 Ooo = re . compile ( '<a class="content-items" href="(.+?)"><img class="program-img" alt="(.+?)" src="(.+?)" [^>]*>' ) . findall ( Oo )
 for o0oOoO00o , i1 , oOOoo00O0O in Ooo :
  i1I11i ( "[B]" + i1 + "[/B]" , "http://m.tv.zing.vn" + o0oOoO00o , 'indexseries' , oOOoo00O0O )
 if ( len ( Ooo ) == 50 ) :
  Oo0o0000o0o0 = int ( re . compile ( '&page=(.+?)&' ) . findall ( url ) [ 0 ] )
  url = url . replace ( "&page=" + str ( Oo0o0000o0o0 ) , "&page=" + str ( Oo0o0000o0o0 + 1 ) )
  i1I11i ( "Next >>" , url , 'indexprogram' , "" )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 32 - 32: I1i1I - OoOoo0 % Oooo000o % Oooo000o
def iiI11 ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 OOooO = re . compile ( '<h3>(.+?)</h3>' ) . findall ( Oo ) [ 0 ]
 OOoO00o = re . compile ( '<input type="hidden" id="_objectId" objectType="tv_program" value="(.+?)">' ) . findall ( Oo ) [ 0 ]
 II111iiii = "http://m.tv.zing.vn/ajax?f=loadSuggest&type=tv_program&id=&page=1&count=100"
 II = I1Ii11I1Ii1i ( II111iiii . replace ( "id=" , "id=" + OOoO00o ) )
 Ooo = re . compile ( '<a href="(.+?)" [^>]*><img [^>]* src="(.+?)" alt="(.+?)">(.+?)<span>(.+?)</span></a>' ) . findall ( II )
 if 63 - 63: i111iII % III
 for o0oOoO00o , oOOoo00O0O , i1 , o0oOo0Ooo0O , OO00O0O0O00Oo in Ooo :
  OOoO00o = o0oOoO00o . split ( "/" ) [ - 1 ] . split ( "." ) [ 0 ]
  o0oOoO00o = "http://m.tv.zing.vn/ajax?f=loadMediaSeries&id=&page=1&count=50"
  i1I11i ( "[B]" + i1 + "[/B] (" + OO00O0O0O00Oo + ")" , o0oOoO00o . replace ( "id=" , "id=" + OOoO00o ) , 'indexvideo' , oOOoo00O0O )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 25 - 25: O0 % oo00oOOo - oo00oOOo . oo00oOOo
def Ii1 ( ) :
 try :
  oOOoO0 = xbmc . Keyboard ( '' , 'Enter search text' )
  oOOoO0 . doModal ( )
  if ( oOOoO0 . isConfirmed ( ) ) :
   O0OoO000O0OO = urllib . quote_plus ( oOOoO0 . getText ( ) )
  iiI1IiI = 'http://m.tv.zing.vn/ajax?f=searchProgram&s=date&page=1&count=50&q=' + O0OoO000O0OO + '/'
  oO0 ( iiI1IiI )
 except : pass
 if 13 - 13: OOo . i11iIiiIii - ii11i - i111iII
def ii1I ( url , name ) :
 name = urllib . unquote_plus ( name ) . decode ( "utf-8" )
 OooO0 = re . compile ( '/(\w+).html' ) . findall ( url ) [ 0 ]
 OooO0 = OooO0 . replace ( "I" , "1" ) . replace ( "W" , "2" ) . replace ( "O" , "3" ) . replace ( "U" , "4" ) . replace ( "Z" , "5" )
 Oo = I1Ii11I1Ii1i ( "http://api.tv.zing.vn/2.0/media/info?media_id=%s&api_key=9955b1816f11fd848db46c60adcdf866&proxy" % ( int ( OooO0 , 16 ) - 307843200 ) )
 II11iiii1Ii = re . compile ( '"Video720": "(.+?)"' ) . findall ( Oo )
 OO0oOoo = ""
 if len ( II11iiii1Ii ) == 0 :
  II11iiii1Ii = re . compile ( '"Video480": "(.+?)"' ) . findall ( Oo )
  if len ( II11iiii1Ii ) == 0 :
   II11iiii1Ii = re . compile ( '"file_url": "(.+?)"' ) . findall ( Oo )
  OO0oOoo = "http://" + II11iiii1Ii [ 0 ] . split ( "?" ) [ 0 ]
 else :
  OO0oOoo = "http://" + II11iiii1Ii [ 0 ] . split ( "?" ) [ 0 ]
  if 68 - 68: o0o + Ii . ii11i - O0o % ii11i - OoOoo0
 oOOO00o = xbmcgui . ListItem ( name )
 oOOO00o . setInfo ( 'video' , { 'Title' : name } )
 oOOO00o . setProperty ( "IsPlayable" , "true" )
 oOOO00o . setPath ( OO0oOoo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oOOO00o )
 if 97 - 97: o0o % o0o + oo00oOOo * iiiii11iII1
def I1Ii11I1Ii1i ( url ) :
 o0o00o0 = urllib2 . Request ( url . replace ( "&proxy" , "" ) )
 if "&proxy" in url :
  iIi1ii1I1 = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1X0197S9P7vn7UsUReZUBc8oK6IgjM99FYdX4lcwp68o/export?format=tsv' )
  o0 = iIi1ii1I1 . read ( ) . decode ( 'utf-8-sig' )
  iIi1ii1I1 . close ( )
  o0o00o0 . set_proxy ( o0 . split ( "\n" ) [ 0 ] , "http" )
 o0o00o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 o0o00o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 I11II1i = urllib2 . urlopen ( o0o00o0 )
 Oo = I11II1i . read ( )
 I11II1i . close ( )
 Oo = '' . join ( Oo . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo = Oo . replace ( '\n' , '' )
 Oo = Oo . replace ( '\t' , '' )
 Oo = re . sub ( '  +' , ' ' , Oo )
 Oo = Oo . replace ( '> <' , '><' )
 return Oo
 if 23 - 23: OoOoOoO0o0OO / O0 + o0o + o0o / oo00oOOo
def iiI1 ( k , e ) :
 i11Iiii = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for iI in range ( len ( e ) ) :
  I1i1I1II = k [ iI % len ( k ) ]
  i1IiIiiI = chr ( ( 256 + ord ( e [ iI ] ) - ord ( I1i1I1II ) ) % 256 )
  i11Iiii . append ( i1IiIiiI )
 return "" . join ( i11Iiii )
 if 31 - 31: OOO0o0o . OOO0o0o - O0 / OOO + OoOoo0 * Oooo000o
def I11 ( name , url , mode , iconimage ) :
 O0ooOooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO0OOO00oo . setProperty ( "IsPlayable" , "true" )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOooooO , listitem = OOO0OOO00oo )
 return o00O
 if 31 - 31: oo00oOOo - Ii . I1i1I % i111iII - iIIi1iI1II111
def i1I11i ( name , url , mode , iconimage ) :
 O0ooOooooO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o00O = True
 OOO0OOO00oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO0OOO00oo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0ooOooooO , listitem = OOO0OOO00oo , isFolder = True )
 return o00O
 if 4 - 4: oo00oOOo / OoOoo0 . iiiii11iII1
def O0oo0OO0oOOOo ( parameters ) :
 i1i1i11IIi = { }
 if 33 - 33: O0 + Ii * OOO - OOo / Ooo0OO0oOO % OOO0o0o
 if parameters :
  II1i1IiiIIi11 = parameters [ 1 : ] . split ( "&" )
  for iI1Ii11iII1 in II1i1IiiIIi11 :
   Oo0O0O0ooO0O = iI1Ii11iII1 . split ( '=' )
   if ( len ( Oo0O0O0ooO0O ) ) == 2 :
    i1i1i11IIi [ Oo0O0O0ooO0O [ 0 ] ] = Oo0O0O0ooO0O [ 1 ]
 return i1i1i11IIi
 if 15 - 15: OoOoOoO0o0OO + i111iII - oOooOoO0Oo0O / Ii
oo000OO00Oo = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 51 - 51: O0o * O0 + o0o + OOO
if os . path . exists ( oo000OO00Oo ) == False :
 os . mkdir ( oo000OO00Oo )
o0O0O00 = os . path . join ( oo000OO00Oo , 'visitor' )
if 86 - 86: o0o / O0o % i11iIiiIii
if os . path . exists ( o0O0O00 ) == False :
 from random import randint
 I11IiI1I11i1i = open ( o0O0O00 , "w" )
 I11IiI1I11i1i . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 I11IiI1I11i1i . close ( )
 if 38 - 38: O0
def Oo0O ( utm_url ) :
 IIi = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  o0o00o0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : IIi }
 )
  I11II1i = urllib2 . urlopen ( o0o00o0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return I11II1i
 if 26 - 26: iiiii11iII1
def OOOOo0oOOo ( group , name ) :
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
  Oo0OoO00oOO0o = "1.0"
  OOO00O = open ( o0O0O00 ) . read ( )
  OOoOO0oo0ooO = "ZingTV"
  O0o0O00Oo0o0 = "UA-52209804-2"
  O00O0oOO00O00 = "www.viettv24.com"
  i1Oo00 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1i = i1Oo00 + "?" + "utmwv=" + Oo0OoO00oOO0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOoOO0oo0ooO ) + "&utmac=" + O0o0O00Oo0o0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO00O , "1" , "1" , "2" ] )
   if 50 - 50: O0o
   if 14 - 14: o0o % OOO * o0o
   if 16 - 16: i111iII . OoOoo0 + i11iIiiIii
   if 38 - 38: O0o * Ii . O0
   if 98 - 98: oOooOoO0Oo0O + iiiii11iII1 . i111iII
  else :
   if group == "None" :
    i1i = i1Oo00 + "?" + "utmwv=" + Oo0OoO00oOO0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOoOO0oo0ooO + "/" + name ) + "&utmac=" + O0o0O00Oo0o0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO00O , "1" , "1" , "2" ] )
    if 67 - 67: i11iIiiIii - III % OoOoOoO0o0OO . iIIi1iI1II111
    if 77 - 77: O0o / Oooo000o
    if 15 - 15: O0o . ii11i . oOooOoO0Oo0O / i11iIiiIii - OOO0o0o . III
    if 33 - 33: o0o . O0
    if 75 - 75: O0 % O0 . I1i1I
   else :
    i1i = i1Oo00 + "?" + "utmwv=" + Oo0OoO00oOO0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOoOO0oo0ooO + "/" + group + "/" + name ) + "&utmac=" + O0o0O00Oo0o0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOO00O , "1" , "1" , "2" ] )
    if 5 - 5: O0 * OoOoo0 + i111iII . Ii + i111iII
    if 91 - 91: iIIi1iI1II111
    if 61 - 61: oo00oOOo
    if 64 - 64: OoOoo0 / i111iII - iIIi1iI1II111 - o0o
    if 86 - 86: o0o % i111iII / Oooo000o / i111iII
    if 42 - 42: OOO
  print "============================ POSTING ANALYTICS ============================"
  Oo0O ( i1i )
  if 67 - 67: I1i1I . iiiii11iII1 . iIIi1iI1II111
  if not group == "None" :
   IIIIiiII111 = i1Oo00 + "?" + "utmwv=" + Oo0OoO00oOO0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( O00O0oOO00O00 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + OOoOO0oo0ooO + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( OOoOO0oo0ooO ) + "&utmac=" + O0o0O00Oo0o0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , OOO00O , "1" , "2" ] )
   if 97 - 97: OoOoOoO0o0OO + Ii / ii11i / iiiii11iII1
   if 37 - 37: iiiii11iII1 - OoOoo0 * Ooo0OO0oOO % i11iIiiIii - I1i1I
   if 83 - 83: o0o / Oooo000o
   if 34 - 34: O0o
   if 57 - 57: Ooo0OO0oOO . o0o . III
   if 42 - 42: o0o + OoOoOoO0o0OO % iIIi1iI1II111
   if 6 - 6: Ooo0OO0oOO
   if 68 - 68: i111iII - OOO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    Oo0O ( IIIIiiII111 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 28 - 28: OOO . Ii / Ii + OOo . OoOoOoO0o0OO
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 1 - 1: ii11i / oo00oOOo
iiI1I11i1i = O0oo0OO0oOOOo ( sys . argv [ 2 ] )
III1Iiii1I11 = iiI1I11i1i . get ( 'mode' )
iiI1IiI = iiI1I11i1i . get ( 'url' )
IIII = iiI1I11i1i . get ( 'name' )
if type ( iiI1IiI ) == type ( str ( ) ) :
 iiI1IiI = urllib . unquote_plus ( iiI1IiI )
if type ( IIII ) == type ( str ( ) ) :
 IIII = urllib . unquote_plus ( IIII )
 if 32 - 32: oOooOoO0Oo0O / ii11i - O0
o00oooO0Oo = str ( sys . argv [ 1 ] )
if III1Iiii1I11 == 'indexvideo' :
 OOOOo0oOOo ( "Browse" , IIII )
 Ii1iI ( iiI1IiI )
elif III1Iiii1I11 == 'indexprogram' :
 OOOOo0oOOo ( "Browse" , IIII )
 oO0 ( iiI1IiI )
elif III1Iiii1I11 == 'indexseries' :
 OOOOo0oOOo ( "Browse" , IIII )
 iiI11 ( iiI1IiI )
elif III1Iiii1I11 == 'search' :
 OOOOo0oOOo ( "None" , "Search" )
 Ii1 ( )
elif III1Iiii1I11 == 'loadvideo' :
 OOOOo0oOOo ( "Play" , IIII + "/" + iiI1IiI )
 o0O0OOO0Ooo = xbmcgui . DialogProgress ( )
 o0O0OOO0Ooo . create ( 'Zing TV' , 'Loading video. Please wait...' )
 ii1I ( iiI1IiI , IIII )
 o0O0OOO0Ooo . close ( )
 del o0O0OOO0Ooo
else :
 OOOOo0oOOo ( "None" , "None" )
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( o00oooO0Oo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
