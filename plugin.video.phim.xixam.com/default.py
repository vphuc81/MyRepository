#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , urlresolver , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.phim.xixam.com'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = "http://phim.xixam.com"
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( ) :
 i1I11i ( 'Search' , 'http://phim.xixam.com/tim-kiem/?tk=' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
 i1I11i ( 'Movies' , 'http://phim.xixam.com/phim-le/' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
 i1I11i ( 'Series' , 'http://phim.xixam.com/phim-bo/' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
 i1I11i ( 'By Region' , 'http://phim.xixam.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
 i1I11i ( 'Movies By Category ' , 'http://phim.xixam.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 i1I11i ( 'Others ' , 'http://phim.xixam.com/phim-khac/' , 'index' , 'http://echipstore.net/addonicons/Categories.jpg' )
 if 73 - 73: III - oo00oOOo * Oooo000o % OOo . OOO
 IiI1ii1 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: IiI1ii1 = xbmc . translatePath ( os . path . join ( IiI1ii1 , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/xixam.jpg' , IiI1ii1 )
 if 49 - 49: oooOOooo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI1ii1 )
 if 49 - 49: o0oo0oo0OO00 = xbmcgui . WindowDialog ( )
 if 49 - 49: o0oo0oo0OO00 . addControl ( oooOOooo )
 if 49 - 49: o0oo0oo0OO00 . doModal ( )
 if 20 - 20: i111iII
def oOOo ( ) :
 i1I11i ( 'Vietnam' , 'http://phim.xixam.com/country/vietnam-9/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Korea' , 'http://phim.xixam.com/country/korea-1/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'China' , 'http://phim.xixam.com/country/china-5/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Hong Kong' , 'http://phim.xixam.com/country/hong-kong-18/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Japan' , 'http://phim.xixam.com/country/japan-11/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Taiwan' , 'http://phim.xixam.com/country/taiwan-2/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Singapore' , 'http://phim.xixam.com/country/singapore-17/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Philippines' , 'http://phim.xixam.com/country/philippines-4/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Thailand' , 'http://phim.xixam.com/country/thailand-3/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'UK' , 'http://phim.xixam.com/country/united-kingdom-52/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'US' , 'http://phim.xixam.com/country/united-states-10/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 if 25 - 25: O0 + OoOoOoO0o0OO * Ooo0OO0oOO * Ii * o0o - OOO0o0o
def Ii1iI ( ) :
 i1I11i ( 'Action' , 'http://phim.xixam.com/phim-hanh-dong/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Martial Arts' , 'http://phim.xixam.com/phim-kiem-hiep/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Comedy' , 'http://phim.xixam.com/phim-hai/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Adventure' , 'http://phim.xixam.com/phim-phieu-luu/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Horror' , 'http://phim.xixam.com/phim-kinh-di/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Romance' , 'http://phim.xixam.com/phim-tinh-cam/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Animation' , 'http://phim.xixam.com/phim-hoat-hinh/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Fiction' , 'http://phim.xixam.com/phim-vien-tuong/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Psychological' , 'http://phim.xixam.com/phim-tam-ly/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Comedy (Vietnamesse only)' , 'http://phim.xixam.com/hai-kich/11/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'War/Combat' , 'http://phim.xixam.com/phim-chien-tranh/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Sports' , 'http://phim.xixam.com/the-thao/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'TV Shows' , 'http://phim.xixam.com/talkshow-tivi-show/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 i1I11i ( 'Adult Only (18+)' , 'http://phim.xixam.com/phim-18/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 if 100 - 100: i11Ii11I1Ii1i . ooO - OOoO / ooo0Oo0 * OOO - i11iIiiIii
def II1Iiii1111i ( url ) :
 i1IIi11111i = o000o0o00o0Oo ( url )
 oo = re . compile ( '<div class="rowProduct">(.+?)<div class="fr_page_links">' ) . findall ( i1IIi11111i )
 IiII1I1i1i1ii = re . compile ( '<a href="(.+?)" class="img" title="(.+?)"><img src="(.+?)" [^>]*/>(.+?)<span class="tap">(.*?)</span>' ) . findall ( oo [ 0 ] )
 for IIIII , I1 , O0OoOoo00o , iiiI11 , OOooO in IiII1I1i1i1ii :
  if ( O0OoOoo00o . find ( "http://" ) == - 1 ) :
   O0OoOoo00o = iiiii + O0OoOoo00o . replace ( "/ " , "/" )
  if ( OOooO . find ( "HD" ) != - 1 ) :
   OOooO = "[B][COLOR yellow]" + OOooO + "[/COLOR][/B]"
  i1I11i ( "[B]" + I1 + "[/B] (" + OOooO + ")" , IIIII , 'mirrors' , O0OoOoo00o )
 OOoO00o = re . compile ( '<div class="fr_page_links">(.+?)</div>' ) . findall ( i1IIi11111i )
 II111iiii = re . compile ( '<a href="(.+?)" [^>]*>(.+?)</a>' ) . findall ( OOoO00o [ 0 ] )
 for IIIII , II in II111iiii :
  i1I11i ( II , iiiii + IIIII , 'index' , "" )
 oOoOo00oOo = xbmc . getSkinDir ( )
 if oOoOo00oOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 96 - 96: III . i111iII * Ii % ooo0Oo0
def OO0O0O00OooO ( ) :
 try :
  OoooooOoo = xbmc . Keyboard ( '' , 'Enter search text' )
  OoooooOoo . doModal ( )
  if 70 - 70: OOO . OOO - OOO / OoOoOoO0o0OO * Ii
  if ( OoooooOoo . isConfirmed ( ) ) :
   OoO000 = urllib . quote_plus ( OoooooOoo . getText ( ) )
  IIiiIiI1 = 'http://phim.xixam.com/tim-kiem/?tk=' + OoO000
  II1Iiii1111i ( IIiiIiI1 )
 except : pass
 if 41 - 41: i111iII
def IIooOoOoo0O ( url ) :
 OooO0 = II11iiii1Ii ( url )
 if OooO0 . find ( "html" ) != - 1 :
  i1IIi11111i = o000o0o00o0Oo ( OooO0 )
  OO0oOoo = re . compile ( '<div class="serverlist"><span>(.+?)</span>' ) . findall ( i1IIi11111i )
  for O0o0Oo in OO0oOoo :
   Oo00OOOOO = [ 'Zing' , 'Download' ]
   if not any ( x in O0o0Oo for x in Oo00OOOOO ) :
    i1I11i ( O0o0Oo , OooO0 . encode ( "utf-8" ) , 'episodes' , "" )
    if 85 - 85: ooo0Oo0 . i11Ii11I1Ii1i - OOO % ooo0Oo0 % oo00oOOo
def OO0o00o ( url , name ) :
 i1IIi11111i = o000o0o00o0Oo ( url )
 oOOo0oo = re . compile ( '<div class="serverlist"><span>' + urllib2 . unquote ( name ) + '</span>(.*?)</div>' ) . findall ( i1IIi11111i )
 o0oo0o0O00OO = re . compile ( '<a [^>]*href="(.+?)">(.+?)</a>' ) . findall ( oOOo0oo [ 0 ] )
 for o0oO , I1i1iii in o0oo0o0O00OO :
  i1iiI11I ( "Part - " + I1i1iii . strip ( ) . encode ( "utf-8" ) , iiiii + "/m/" + o0oO , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 29 - 29: oOooOoO0Oo0O
def II11iiii1Ii ( url ) :
 url = url . split ( "/" ) [ 2 ] . replace ( ".html" , "-1-1.html" )
 return iiiii + "/m/xem-online/" + url
 if 23 - 23: O0 . oo00oOOo
def Oo0O0OOOoo ( url , name ) :
 i1IIi11111i = o000o0o00o0Oo ( url )
 oOoOooOo0o0 = re . compile ( '<figure class="videoWrapper">(.+?)</figure>' ) . findall ( i1IIi11111i ) [ 0 ]
 if ( "youtube" in oOoOooOo0o0 ) :
  OOOO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( oOoOooOo0o0 )
  OOO00 = OOOO [ 0 ] [ len ( OOOO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  url = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + OOO00 . replace ( '?' , '' )
  iiiiiIIii = xbmcgui . ListItem ( name )
  iiiiiIIii . setProperty ( "IsPlayable" , "true" )
  iiiiiIIii . setPath ( url )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiiiIIii )
 else :
  oo = re . compile ( '<source src="(.+?)" [^>]*/>' ) . findall ( oOoOooOo0o0 )
  O000OO0 = oo [ 0 ]
  I11iii1Ii = O000OO0 . split ( "=m" ) [ 0 ] + "=m22"
  if Oo0Ooo . getSetting ( 'HQ' ) == "true" :
   try :
    I1IIiiIiii = urllib2 . urlopen ( oo [ 0 ] ) . getcode ( )
    O000OO0 = I11iii1Ii
   except :
    pass
  iiiiiIIii = xbmcgui . ListItem ( name )
  iiiiiIIii . setProperty ( "IsPlayable" , "true" )
  iiiiiIIii . setPath ( O000OO0 )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , iiiiiIIii )
  if 97 - 97: ooo0Oo0 - Ii * i11iIiiIii / i111iII % OOoO - oOooOoO0Oo0O
def o000o0o00o0Oo ( url ) :
 OoOo00o = urllib2 . Request ( url )
 OoOo00o . add_header ( 'Host' , 'phim.xixam.com' )
 OoOo00o . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 OoOo00o . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 o0OOoo0OO0OOO = urllib2 . urlopen ( OoOo00o )
 i1IIi11111i = o0OOoo0OO0OOO . read ( )
 o0OOoo0OO0OOO . close ( )
 i1IIi11111i = '' . join ( i1IIi11111i . splitlines ( ) ) . replace ( '\'' , '"' )
 i1IIi11111i = i1IIi11111i . replace ( '\n' , '' )
 i1IIi11111i = i1IIi11111i . replace ( '\t' , '' )
 i1IIi11111i = re . sub ( '  +' , ' ' , i1IIi11111i )
 i1IIi11111i = i1IIi11111i . replace ( '> <' , '><' )
 return i1IIi11111i
 if 19 - 19: Ooo0OO0oOO % III % O0
def i1iiI11I ( name , url , mode , iconimage , mirrorname ) :
 oo0OooOOo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 o0O = True
 O00oO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 O00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O00oO . setProperty ( "IsPlayable" , "true" )
 o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0OooOOo0 , listitem = O00oO )
 return o0O
 if 39 - 39: ooO - oo00oOOo * OOO % O0 * oo00oOOo % oo00oOOo
def i1I11i ( name , url , mode , iconimage ) :
 oo0OooOOo0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o0O = True
 O00oO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 O00oO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o0O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oo0OooOOo0 , listitem = O00oO , isFolder = True )
 return o0O
 if 59 - 59: ii11i + Oooo000o - O0 - Oooo000o + Ii / OoOoOoO0o0OO
def I1OO00Oo ( k , e ) :
 O0OOO0OOoO0O = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O00Oo000ooO0 in range ( len ( e ) ) :
  OoO0O00 = k [ O00Oo000ooO0 % len ( k ) ]
  IIiII = chr ( ( 256 + ord ( e [ O00Oo000ooO0 ] ) - ord ( OoO0O00 ) ) % 256 )
  O0OOO0OOoO0O . append ( IIiII )
 return "" . join ( O0OOO0OOoO0O )
 if 80 - 80: ooO . Ooo0OO0oOO
def IIi ( parameters ) :
 i11iIIIIIi1 = { }
 if 20 - 20: III + OoOoOoO0o0OO - ooo0Oo0
 if parameters :
  IiI11iII1 = parameters [ 1 : ] . split ( "&" )
  for IIII11I1I in IiI11iII1 :
   OOO0o = IIII11I1I . split ( '=' )
   if ( len ( OOO0o ) ) == 2 :
    i11iIIIIIi1 [ OOO0o [ 0 ] ] = OOO0o [ 1 ]
 return i11iIIIIIi1
 if 30 - 30: ii11i / ooo0Oo0 - OOoO - oo00oOOo % i11Ii11I1Ii1i
IIi1i11111 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 81 - 81: i11iIiiIii % i111iII - Ii
if os . path . exists ( IIi1i11111 ) == False :
 os . mkdir ( IIi1i11111 )
O0ooo0O0oo0 = os . path . join ( IIi1i11111 , 'visitor' )
if 91 - 91: ii11i + OOoO
if os . path . exists ( O0ooo0O0oo0 ) == False :
 from random import randint
 i1i = open ( O0ooo0O0oo0 , "w" )
 i1i . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 i1i . close ( )
 if 46 - 46: OOoO % o0o + OOO . i111iII . OOO
def oO00o0 ( utm_url ) :
 OOoo0O = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  OoOo00o = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOoo0O }
 )
  o0OOoo0OO0OOO = urllib2 . urlopen ( OoOo00o ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return o0OOoo0OO0OOO
 if 67 - 67: i11iIiiIii - III % OoOoOoO0o0OO . iIIi1iI1II111
def o0oo ( group , name ) :
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
  oooooOoo0ooo = "1.0"
  I1I1IiI1 = open ( O0ooo0O0oo0 ) . read ( )
  III1iII1I1ii = "XiXam"
  oOOo0 = "UA-52209804-2"
  oo00O00oO = "www.viettv24.com"
  iIiIIIi = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   ooo00OOOooO = iIiIIIi + "?" + "utmwv=" + oooooOoo0ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( III1iII1I1ii ) + "&utmac=" + oOOo0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1IiI1 , "1" , "1" , "2" ] )
   if 67 - 67: o0o * Ooo0OO0oOO * OoOoOoO0o0OO + Ii / III
   if 11 - 11: OOO0o0o + i11Ii11I1Ii1i - ooo0Oo0 * Ooo0OO0oOO % i11iIiiIii - OOoO
   if 83 - 83: o0o / Oooo000o
   if 34 - 34: ooO
   if 57 - 57: Ooo0OO0oOO . o0o . III
  else :
   if group == "None" :
    ooo00OOOooO = iIiIIIi + "?" + "utmwv=" + oooooOoo0ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( III1iII1I1ii + "/" + name ) + "&utmac=" + oOOo0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1IiI1 , "1" , "1" , "2" ] )
    if 42 - 42: o0o + OoOoOoO0o0OO % iIIi1iI1II111
    if 6 - 6: Ooo0OO0oOO
    if 68 - 68: i111iII - OOO
    if 28 - 28: OOO . Ii / Ii + OOo . OoOoOoO0o0OO
    if 1 - 1: ii11i / oo00oOOo
   else :
    ooo00OOOooO = iIiIIIi + "?" + "utmwv=" + oooooOoo0ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( III1iII1I1ii + "/" + group + "/" + name ) + "&utmac=" + oOOo0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I1I1IiI1 , "1" , "1" , "2" ] )
    if 33 - 33: o0o
    if 18 - 18: O0 % i11Ii11I1Ii1i * iIIi1iI1II111
    if 87 - 87: i11iIiiIii
    if 93 - 93: OoOoOoO0o0OO - OOO % i11iIiiIii . i11Ii11I1Ii1i / i11Ii11I1Ii1i - OOoO
    if 9 - 9: OoOoOoO0o0OO / OOo - Oooo000o / oOooOoO0Oo0O / ii11i - O0
    if 91 - 91: i11Ii11I1Ii1i % III % ii11i
  print "============================ POSTING ANALYTICS ============================"
  oO00o0 ( ooo00OOOooO )
  if 20 - 20: Ii % OOO0o0o / OOO0o0o + OOO0o0o
  if not group == "None" :
   III1IiiI = iIiIIIi + "?" + "utmwv=" + oooooOoo0ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( oo00O00oO ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + III1iII1I1ii + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( III1iII1I1ii ) + "&utmac=" + oOOo0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , I1I1IiI1 , "1" , "2" ] )
   if 31 - 31: O0 . Oooo000o
   if 46 - 46: i11Ii11I1Ii1i
   if 8 - 8: Ooo0OO0oOO * i111iII - OOO0o0o - OOO * Ii % Oooo000o
   if 48 - 48: iIIi1iI1II111
   if 11 - 11: o0o + oOooOoO0Oo0O - OOO / O0 + OOo . oo00oOOo
   if 41 - 41: OOO0o0o - iIIi1iI1II111 - iIIi1iI1II111
   if 68 - 68: Ii % OOoO
   if 88 - 88: ii11i - ooo0Oo0 + Ii
   try :
    print "============================ POSTING TRACK EVENT ============================"
    oO00o0 ( III1IiiI )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 40 - 40: Oooo000o * OOO0o0o + Ii % i11Ii11I1Ii1i
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 74 - 74: Ooo0OO0oOO - OOo + oOooOoO0Oo0O + OOoO / i111iII
i1 = IIi ( sys . argv [ 2 ] )
I1iI1iIi111i = i1 . get ( 'mode' )
IIiiIiI1 = i1 . get ( 'url' )
iiIi1IIi1I = i1 . get ( 'name' )
if type ( IIiiIiI1 ) == type ( str ( ) ) :
 IIiiIiI1 = urllib . unquote_plus ( IIiiIiI1 )
if type ( iiIi1IIi1I ) == type ( str ( ) ) :
 iiIi1IIi1I = urllib . unquote_plus ( iiIi1IIi1I )
 if 84 - 84: ooo0Oo0 * oo00oOOo + OOo
O0ooO0Oo00o = str ( sys . argv [ 1 ] )
if I1iI1iIi111i == 'index' :
 o0oo ( "Browse" , iiIi1IIi1I )
 II1Iiii1111i ( IIiiIiI1 )
elif I1iI1iIi111i == 'search' :
 o0oo ( "None" , "Search" )
 OO0O0O00OooO ( )
elif I1iI1iIi111i == 'videosbyregion' :
 o0oo ( "Browse" , iiIi1IIi1I )
 oOOo ( )
elif I1iI1iIi111i == 'videosbycategory' :
 o0oo ( "Browse" , iiIi1IIi1I )
 Ii1iI ( )
elif I1iI1iIi111i == 'mirrors' :
 o0oo ( "Browse" , iiIi1IIi1I )
 IIooOoOoo0O ( IIiiIiI1 )
elif I1iI1iIi111i == 'episodes' :
 o0oo ( "Browse" , iiIi1IIi1I )
 OO0o00o ( IIiiIiI1 , iiIi1IIi1I )
elif I1iI1iIi111i == 'loadvideo' :
 o0oo ( "Play" , iiIi1IIi1I + "/" + IIiiIiI1 )
 ooO0oOOooOo0 = xbmcgui . DialogProgress ( )
 ooO0oOOooOo0 . create ( 'phim.xixam.com' , 'Loading video. Please wait...' )
 Oo0O0OOOoo ( IIiiIiI1 , iiIi1IIi1I )
 ooO0oOOooOo0 . close ( )
 del ooO0oOOooOo0
else :
 o0oo ( "None" , "None" )
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( O0ooO0Oo00o ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
