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
 i1I11i = ""
 OoOoOO00 = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  sys = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in sys for b in OoOoOO00 ) : break
 while True :
  I11i = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in I11i for b in OoOoOO00 ) : break
 try :
  i1I11i = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   i1I11i = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , i1I11i . lower ( ) ) : break
 O0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( i1I11i , "9" , sys , I11i ) ) . read ( )
 if "allowed" in O0O :
  Oo ( 'Search' , 'http://phim.xixam.com/tim-kiem/?tk=' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  Oo ( 'Movies' , 'http://phim.xixam.com/phim-le/' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  Oo ( 'Series' , 'http://phim.xixam.com/phim-bo/' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  Oo ( 'By Region' , 'http://phim.xixam.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  Oo ( 'Movies By Category ' , 'http://phim.xixam.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
  Oo ( 'Others ' , 'http://phim.xixam.com/phim-khac/' , 'index' , 'http://echipstore.net/addonicons/Categories.jpg' )
 else :
  Oo ( 'Search' , 'http://phim.xixam.com/tim-kiem/?tk=' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
  Oo ( 'Movies' , 'http://phim.xixam.com/phim-le/' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' )
  Oo ( 'Series' , 'http://phim.xixam.com/phim-bo/' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' )
  Oo ( 'By Region' , 'http://phim.xixam.com/' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
  Oo ( 'Movies By Category ' , 'http://phim.xixam.com/' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
  Oo ( 'Others ' , 'http://phim.xixam.com/phim-khac/' , 'index' , 'http://echipstore.net/addonicons/Categories.jpg' )
  if 48 - 48: oO0o / OOooOOo / I11iIi1I / IiiIII111iI
  if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
 OoI1Ii11I1Ii1i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 OoI1Ii11I1Ii1i = xbmc . translatePath ( os . path . join ( OoI1Ii11I1Ii1i , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/xixam.jpg' , OoI1Ii11I1Ii1i )
 Ooo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , OoI1Ii11I1Ii1i )
 o0oOoO00o = xbmcgui . WindowDialog ( )
 o0oOoO00o . addControl ( Ooo )
 o0oOoO00o . doModal ( )'''
 if 43 - 43: O0OOo . II1Iiii1111i
def i1IIi11111i ( ) :
 Oo ( 'Vietnam' , 'http://phim.xixam.com/country/vietnam-9/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Korea' , 'http://phim.xixam.com/country/korea-1/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'China' , 'http://phim.xixam.com/country/china-5/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Hong Kong' , 'http://phim.xixam.com/country/hong-kong-18/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Japan' , 'http://phim.xixam.com/country/japan-11/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Taiwan' , 'http://phim.xixam.com/country/taiwan-2/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Singapore' , 'http://phim.xixam.com/country/singapore-17/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Philippines' , 'http://phim.xixam.com/country/philippines-4/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Thailand' , 'http://phim.xixam.com/country/thailand-3/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'UK' , 'http://phim.xixam.com/country/united-kingdom-52/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'US' , 'http://phim.xixam.com/country/united-states-10/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 if 74 - 74: Oo0o00o0Oo0 * ii11
def I1I1i1 ( ) :
 Oo ( 'Action' , 'http://phim.xixam.com/phim-hanh-dong/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Martial Arts' , 'http://phim.xixam.com/phim-kiem-hiep/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Comedy' , 'http://phim.xixam.com/phim-hai/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Adventure' , 'http://phim.xixam.com/phim-phieu-luu/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Horror' , 'http://phim.xixam.com/phim-kinh-di/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Romance' , 'http://phim.xixam.com/phim-tinh-cam/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Animation' , 'http://phim.xixam.com/phim-hoat-hinh/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Fiction' , 'http://phim.xixam.com/phim-vien-tuong/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Psychological' , 'http://phim.xixam.com/phim-tam-ly/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Comedy (Vietnamesse only)' , 'http://phim.xixam.com/hai-kich/11/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'War/Combat' , 'http://phim.xixam.com/phim-chien-tranh/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Sports' , 'http://phim.xixam.com/the-thao/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'TV Shows' , 'http://phim.xixam.com/talkshow-tivi-show/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 Oo ( 'Adult Only (18+)' , 'http://phim.xixam.com/phim-18/' , 'index' , 'http://phim.xixam.com/images/logo.png' )
 if 18 - 18: iiIIIIi1i1 / OOoOoo00oo - iii1I1I + ii11i / iiIIIIi1i1 + II
def OOooO ( url ) :
 OOoO00o = II111iiii ( url )
 IIoOoOo00oOo = re . compile ( '<div class="rowProduct">(.+?)<div class="fr_page_links">' ) . findall ( OOoO00o )
 Ooo00O00O0O0O = re . compile ( '<a href="(.+?)" class="img" title="(.+?)"><img src="(.+?)" [^>]*/>(.+?)<span class="tap">(.*?)</span>' ) . findall ( IIoOoOo00oOo [ 0 ] )
 for OooO0OO , iiiIi , IiIIIiI1I1 , OoO000 , IIiiIiI1 in Ooo00O00O0O0O :
  if ( IiIIIiI1I1 . find ( "http://" ) == - 1 ) :
   IiIIIiI1I1 = iiiii + IiIIIiI1I1 . replace ( "/ " , "/" )
  if ( IIiiIiI1 . find ( "HD" ) != - 1 ) :
   IIiiIiI1 = "[B][COLOR yellow]" + IIiiIiI1 + "[/COLOR][/B]"
  Oo ( "[B]" + iiiIi + "[/B] (" + IIiiIiI1 + ")" , OooO0OO , 'mirrors' , IiIIIiI1I1 )
 iiIiIIi = re . compile ( '<div class="fr_page_links">(.+?)</div>' ) . findall ( OOoO00o )
 ooOoo0O = re . compile ( '<a href="(.+?)" [^>]*>(.+?)</a>' ) . findall ( iiIiIIi [ 0 ] )
 for OooO0OO , OooO0 in ooOoo0O :
  Oo ( OooO0 , iiiii + OooO0OO , 'index' , "" )
 II11iiii1Ii = xbmc . getSkinDir ( )
 if II11iiii1Ii == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 70 - 70: I1i1iI1i / ii11i % OOoOoo00oo % i11iIiiIii . I11iIi1I
def O0o0Oo ( ) :
 try :
  Oo00OOOOO = xbmc . Keyboard ( '' , 'Enter search text' )
  Oo00OOOOO . doModal ( )
  if 85 - 85: OOoOoo00oo . Oo0o00o0Oo0 - iii1I1I % OOoOoo00oo % OOooOOo
  if ( Oo00OOOOO . isConfirmed ( ) ) :
   OO0o00o = urllib . quote_plus ( Oo00OOOOO . getText ( ) )
  oOOo0oo = 'http://phim.xixam.com/tim-kiem/?tk=' + OO0o00o
  OOooO ( oOOo0oo )
 except : pass
 if 80 - 80: O0OOo * i11iIiiIii / iiIIIIi1i1
def I11II1i ( url ) :
 IIIII = ooooooO0oo ( url )
 if IIIII . find ( "html" ) != - 1 :
  OOoO00o = II111iiii ( IIIII )
  IIiiiiiiIi1I1 = re . compile ( '<div class="serverlist"><span>(.+?)</span>' ) . findall ( OOoO00o )
  for I1IIIii in IIiiiiiiIi1I1 :
   oOoOooOo0o0 = [ 'Zing' , 'Download' ]
   if not any ( x in I1IIIii for x in oOoOooOo0o0 ) :
    Oo ( I1IIIii , IIIII . encode ( "utf-8" ) , 'episodes' , "" )
    if 61 - 61: O0oo0OO0 / iii1I1I + OOoOoo00oo * I1i1iI1i / I1i1iI1i
def OoOo ( url , name ) :
 OOoO00o = II111iiii ( url )
 iI = re . compile ( '<div class="serverlist"><span>' + urllib2 . unquote ( name ) + '</span>(.*?)</div>' ) . findall ( OOoO00o )
 o00O = re . compile ( '<a [^>]*href="(.+?)">(.+?)</a>' ) . findall ( iI [ 0 ] )
 for OOO0OOO00oo , Iii111II in o00O :
  iiii11I ( "Part - " + Iii111II . strip ( ) . encode ( "utf-8" ) , iiiii + "/m/" + OOO0OOO00oo , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 96 - 96: OOooOOo % II1Iiii1111i . II + oOooOoO0Oo0O * I1i1iI1i - O00oOoOoO0o0O
def ooooooO0oo ( url ) :
 url = url . split ( "/" ) [ 2 ] . replace ( ".html" , "-1-1.html" )
 return iiiii + "/m/xem-online/" + url
 if 10 - 10: II / I11iIi1I * II
def IIIii1II1II ( url , name ) :
 OOoO00o = II111iiii ( url )
 i1I1iI = re . compile ( '<figure class="videoWrapper">(.+?)</figure>' ) . findall ( OOoO00o ) [ 0 ]
 if ( "youtube" in i1I1iI ) :
  oo0OooOOo0 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( i1I1iI )
  o0O = oo0OooOOo0 [ 0 ] [ len ( oo0OooOOo0 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  url = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + o0O . replace ( '?' , '' )
  O00oO = xbmcgui . ListItem ( name )
  O00oO . setProperty ( "IsPlayable" , "true" )
  O00oO . setPath ( url )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00oO )
 else :
  IIoOoOo00oOo = re . compile ( '<source src="(.+?)" [^>]*/>' ) . findall ( i1I1iI )
  I11i1I1I = IIoOoOo00oOo [ 0 ]
  print i1I1iI
  print I11i1I1I
  if ( Oo0Ooo . getSetting ( 'HQ' ) == "true" ) and ( "redirector.googlevideo.com" not in I11i1I1I ) :
   try :
    oO0Oo = urllib2 . urlopen ( IIoOoOo00oOo [ 0 ] ) . getcode ( )
    I11i1I1I = I11i1I1I . split ( "=m" ) [ 0 ] + "=m22"
   except :
    pass
  O00oO = xbmcgui . ListItem ( name )
  O00oO . setProperty ( "IsPlayable" , "true" )
  O00oO . setPath ( I11i1I1I )
  xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , O00oO )
  if 54 - 54: O0oo0OO0 - I11iIi1I + oOooOoO0Oo0O
def II111iiii ( url ) :
 O0o0 = urllib2 . Request ( url )
 O0o0 . add_header ( 'Host' , 'phim.xixam.com' )
 O0o0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 O0o0 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OO00Oo = urllib2 . urlopen ( O0o0 )
 OOoO00o = OO00Oo . read ( )
 OO00Oo . close ( )
 OOoO00o = '' . join ( OOoO00o . splitlines ( ) ) . replace ( '\'' , '"' )
 OOoO00o = OOoO00o . replace ( '\n' , '' )
 OOoO00o = OOoO00o . replace ( '\t' , '' )
 OOoO00o = re . sub ( '  +' , ' ' , OOoO00o )
 OOoO00o = OOoO00o . replace ( '> <' , '><' )
 return OOoO00o
 if 51 - 51: ii11 * O0oo0OO0 + O0OOo + iii1I1I
def iiii11I ( name , url , mode , iconimage , mirrorname ) :
 o0O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 o000o = True
 I11IiI1I11i1i = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 I11IiI1I11i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 I11IiI1I11i1i . setProperty ( "IsPlayable" , "true" )
 o000o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0O0O00 , listitem = I11IiI1I11i1i )
 return o000o
 if 38 - 38: O0oo0OO0
def Oo ( name , url , mode , iconimage ) :
 o0O0O00 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 o000o = True
 I11IiI1I11i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 I11IiI1I11i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 o000o = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = o0O0O00 , listitem = I11IiI1I11i1i , isFolder = True )
 return o000o
 if 57 - 57: iIIi1iI1II111 / I1i1iI1i * iiIIIIi1i1 / O00oOoOoO0o0O . OOooOOo
def i11iIIIIIi1 ( k , e ) :
 iiII1i1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for o00oOO0o in range ( len ( e ) ) :
  OOO00O = k [ o00oOO0o % len ( k ) ]
  OOoOO0oo0ooO = chr ( ( 256 + ord ( e [ o00oOO0o ] ) - ord ( OOO00O ) ) % 256 )
  iiII1i1 . append ( OOoOO0oo0ooO )
 return "" . join ( iiII1i1 )
 if 98 - 98: Oo0o00o0Oo0 * Oo0o00o0Oo0 / Oo0o00o0Oo0 + O0OOo
def ii111111I1iII ( parameters ) :
 O00ooo0O0 = { }
 if 23 - 23: Oo0o00o0Oo0
 if parameters :
  oo0oOo = parameters [ 1 : ] . split ( "&" )
  for o000O0o in oo0oOo :
   iI1iII1 = o000O0o . split ( '=' )
   if ( len ( iI1iII1 ) ) == 2 :
    O00ooo0O0 [ iI1iII1 [ 0 ] ] = iI1iII1 [ 1 ]
 return O00ooo0O0
 if 86 - 86: II
OOoo0O = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 67 - 67: i11iIiiIii - oO0o % Oo0ooO0oo0oO . iIIi1iI1II111
if os . path . exists ( OOoo0O ) == False :
 os . mkdir ( OOoo0O )
o0oo = os . path . join ( OOoo0O , 'visitor' )
if 91 - 91: ii11
if os . path . exists ( o0oo ) == False :
 from random import randint
 iiIii = open ( o0oo , "w" )
 iiIii . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iiIii . close ( )
 if 79 - 79: oOooOoO0Oo0O / iIIi1iI1II111
def OO0OoO0o00 ( utm_url ) :
 ooOO0O0ooOooO = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O0o0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : ooOO0O0ooOooO }
 )
  OO00Oo = urllib2 . urlopen ( O0o0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OO00Oo
 if 55 - 55: O0oo0OO0 * O00oOoOoO0o0O
def o0O00oOoOO ( group , name ) :
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
  iIIi1i1 = "1.0"
  i1IIIiiII1 = open ( o0oo ) . read ( )
  OOOOoOoo0O0O0 = "XiXam"
  OOOo00oo0oO = "UA-52209804-2"
  IIiIi1iI = "www.viettv24.com"
  i1IiiiI1iI = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1iIi = i1IiiiI1iI + "?" + "utmwv=" + iIIi1i1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOOOoOoo0O0O0 ) + "&utmac=" + OOOo00oo0oO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IIIiiII1 , "1" , "1" , "2" ] )
   if 68 - 68: i11iIiiIii % Oo0ooO0oo0oO + i11iIiiIii
   if 31 - 31: OOooOOo . I11iIi1I
   if 1 - 1: IiiIII111iI / O0oo0OO0 % Oo0o00o0Oo0 * ii11 . i11iIiiIii
   if 2 - 2: Oo0ooO0oo0oO * O0OOo - ii11i + I11iIi1I . I1i1iI1i % Oo0o00o0Oo0
   if 92 - 92: Oo0o00o0Oo0
  else :
   if group == "None" :
    i1iIi = i1IiiiI1iI + "?" + "utmwv=" + iIIi1i1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOOOoOoo0O0O0 + "/" + name ) + "&utmac=" + OOOo00oo0oO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IIIiiII1 , "1" , "1" , "2" ] )
    if 25 - 25: IiiIII111iI - I11iIi1I / oOooOoO0Oo0O / O0oo0OO0
    if 12 - 12: I11iIi1I * Oo0o00o0Oo0 % oO0o % ii11i
    if 20 - 20: II % II1Iiii1111i / II1Iiii1111i + II1Iiii1111i
    if 45 - 45: I1i1iI1i - ii11 - oOooOoO0Oo0O - iii1I1I . OOooOOo / iIIi1iI1II111
    if 51 - 51: iIIi1iI1II111 + Oo0o00o0Oo0
   else :
    i1iIi = i1IiiiI1iI + "?" + "utmwv=" + iIIi1i1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( OOOOoOoo0O0O0 + "/" + group + "/" + name ) + "&utmac=" + OOOo00oo0oO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1IIIiiII1 , "1" , "1" , "2" ] )
    if 8 - 8: I1i1iI1i * O00oOoOoO0o0O - II1Iiii1111i - iii1I1I * II % I11iIi1I
    if 48 - 48: iIIi1iI1II111
    if 11 - 11: O0OOo + oOooOoO0Oo0O - iii1I1I / O0oo0OO0 + IiiIII111iI . OOooOOo
    if 41 - 41: II1Iiii1111i - iIIi1iI1II111 - iIIi1iI1II111
    if 68 - 68: II % iiIIIIi1i1
    if 88 - 88: ii11i - OOoOoo00oo + II
  print "============================ POSTING ANALYTICS ============================"
  OO0OoO0o00 ( i1iIi )
  if 40 - 40: I11iIi1I * II1Iiii1111i + II % Oo0o00o0Oo0
  if not group == "None" :
   OOOOOoo0 = i1IiiiI1iI + "?" + "utmwv=" + iIIi1i1 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( IIiIi1iI ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + OOOOoOoo0O0O0 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( OOOOoOoo0O0O0 ) + "&utmac=" + OOOo00oo0oO + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , i1IIIiiII1 , "1" , "2" ] )
   if 49 - 49: iIIi1iI1II111 . Oo0o00o0Oo0
   if 11 - 11: ii11 * I11iIi1I . ii11i % oOooOoO0Oo0O + Oo0o00o0Oo0
   if 78 - 78: iii1I1I . II + iii1I1I / O0OOo / iii1I1I
   if 54 - 54: O00oOoOoO0o0O % Oo0o00o0Oo0
   if 37 - 37: O00oOoOoO0o0O * IiiIII111iI / OOoOoo00oo - Oo0o00o0Oo0 % OOooOOo . I1i1iI1i
   if 88 - 88: Oo0o00o0Oo0 . OOooOOo * OOooOOo % iiIIIIi1i1
   if 15 - 15: oO0o * I11iIi1I + i11iIiiIii
   if 6 - 6: OOoOoo00oo / i11iIiiIii + Oo0o00o0Oo0 * I1i1iI1i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OO0OoO0o00 ( OOOOOoo0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 80 - 80: OOooOOo
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 83 - 83: O0OOo . i11iIiiIii + OOooOOo . O0oo0OO0 * O0OOo
oooO0 = ii111111I1iII ( sys . argv [ 2 ] )
iIiIiiIIiIIi = oooO0 . get ( 'mode' )
oOOo0oo = oooO0 . get ( 'url' )
oO0OOOO0 = oooO0 . get ( 'name' )
if type ( oOOo0oo ) == type ( str ( ) ) :
 oOOo0oo = urllib . unquote_plus ( oOOo0oo )
if type ( oO0OOOO0 ) == type ( str ( ) ) :
 oO0OOOO0 = urllib . unquote_plus ( oO0OOOO0 )
 if 26 - 26: II1Iiii1111i
I11iiI1i1 = str ( sys . argv [ 1 ] )
if iIiIiiIIiIIi == 'index' :
 o0O00oOoOO ( "Browse" , oO0OOOO0 )
 OOooO ( oOOo0oo )
elif iIiIiiIIiIIi == 'search' :
 o0O00oOoOO ( "None" , "Search" )
 O0o0Oo ( )
elif iIiIiiIIiIIi == 'videosbyregion' :
 o0O00oOoOO ( "Browse" , oO0OOOO0 )
 i1IIi11111i ( )
elif iIiIiiIIiIIi == 'videosbycategory' :
 o0O00oOoOO ( "Browse" , oO0OOOO0 )
 I1I1i1 ( )
elif iIiIiiIIiIIi == 'mirrors' :
 o0O00oOoOO ( "Browse" , oO0OOOO0 )
 I11II1i ( oOOo0oo )
elif iIiIiiIIiIIi == 'episodes' :
 o0O00oOoOO ( "Browse" , oO0OOOO0 )
 OoOo ( oOOo0oo , oO0OOOO0 )
elif iIiIiiIIiIIi == 'loadvideo' :
 o0O00oOoOO ( "Play" , oO0OOOO0 + "/" + oOOo0oo )
 I1i1Iiiii = xbmcgui . DialogProgress ( )
 I1i1Iiiii . create ( 'phim.xixam.com' , 'Loading video. Please wait...' )
 IIIii1II1II ( oOOo0oo , oO0OOOO0 )
 I1i1Iiiii . close ( )
 del I1i1Iiiii
else :
 o0O00oOoOO ( "None" , "None" )
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( I11iiI1i1 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
