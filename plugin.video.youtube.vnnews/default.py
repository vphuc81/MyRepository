#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.youtube.vnnews'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 while True :
  ii11i = xbmc . getInfoLabel ( "Network.MacAddress" )
  if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , ii11i . lower ( ) ) : break
 oOooOoO0Oo0O = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s" % ( ii11i , "19" ) ) . read ( )
 if "allowed" in oOooOoO0Oo0O :
  oOooOoO0Oo0O = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw/export?format=tsv&id=1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw&gid=0' )
  iI1 = oOooOoO0Oo0O . read ( ) . decode ( 'utf-8-sig' ) . encode ( 'utf8' )
  oOooOoO0Oo0O . close ( )
  for i1I11i in iI1 . split ( "\n" ) :
   OoOoOO00 = i1I11i . split ( "\t" )
   I11i ( OoOoOO00 [ 0 ] , OoOoOO00 [ 1 ] , 'index' , '' )
 else :
  oOooOoO0Oo0O = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw/export?format=tsv&id=1P1ViMaKLDRZzUbHZ5aE192R-juxmMycs2R8RrludeVw&gid=0' )
  iI1 = oOooOoO0Oo0O . read ( ) . decode ( 'utf-8-sig' ) . encode ( 'utf8' )
  oOooOoO0Oo0O . close ( )
  for i1I11i in iI1 . split ( "\n" ) :
   OoOoOO00 = i1I11i . split ( "\t" )
   I11i ( OoOoOO00 [ 0 ] , OoOoOO00 [ 1 ] , 'index' , '' )
 Oo = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: Oo = xbmc . translatePath ( os . path . join ( Oo , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/vnnews.jpg' , Oo )
 if 49 - 49: I1ii11iIi11i = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , Oo )
 if 49 - 49: I1IiI = xbmcgui . WindowDialog ( )
 if 49 - 49: I1IiI . addControl ( I1ii11iIi11i )
 if 49 - 49: I1IiI . doModal ( )
 if 73 - 73: OOooOOo / ii11ii1ii
def O00ooOO ( url ) :
 I1iII1iiII = iI1Ii11111iIi ( url )
 i1i1II = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( I1iII1iiII )
 O0oo0OO0 = int ( i1i1II [ 0 ] [ 0 ] )
 I1i1iiI1 = int ( i1i1II [ 0 ] [ 1 ] )
 iiIIIII1i1iI = I1iII1iiII . split ( '<entry' )
 if I1i1iiI1 < 50 :
  o0oO0 = re . compile ( "users/(.+?)/" , re . DOTALL ) . findall ( url ) [ 0 ]
  I11i ( "[COLOR orange][B]Hot News[/B][/COLOR]" , "https://gdata.youtube.com/feeds/api/users/%s/uploads?v=2&max-results=50" % o0oO0 , 'showItems' , '' )
 for oo00 in range ( 1 , len ( iiIIIII1i1iI ) , 1 ) :
  o00 = iiIIIII1i1iI [ oo00 ]
  i1i1II = re . compile ( "src='(.+?)'" , re . DOTALL ) . findall ( o00 )
  Oo0oO0ooo = i1i1II [ 0 ]
  i1i1II = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( o00 )
  o0oOoO00o = i1i1II [ 0 ]
  if len ( i1i1II ) > 0 :
   o0oOoO00o = i1i1II [ 0 ]
   o0oOoO00o = i1 ( o0oOoO00o )
  i1i1II = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120' yt:name='default'/>" , re . DOTALL ) . findall ( o00 )
  oOOoo00O0O = ""
  if ( len ( i1i1II ) > 0 ) :
   oOOoo00O0O = i1i1II [ 0 ]
  I11i ( "[B]" + o0oOoO00o + "[/B]" , Oo0oO0ooo , 'showItems' , oOOoo00O0O )
 if I1i1iiI1 + 50 <= O0oo0OO0 :
  I11i ( "[Next >]" , url + "&start-index=" + str ( int ( I1i1iiI1 ) + 50 ) , "showNextPlaylists" , "" )
  if 15 - 15: I11iii11IIi
def I11i ( name , url , mode , iconimage ) :
 O00o0o0000o0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0Oo = True
 if iconimage == "" : iconimage = "DefaultFolder.png"
 oo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 if ( "youtube.com/user/" in url ) or ( "youtube.com/channel/" in url ) :
  O00o0o0000o0o = "plugin://plugin.video.youtube/%s/%s/" % ( url . split ( "/" ) [ - 2 ] , url . split ( "/" ) [ - 1 ] )
  return xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00o0o0000o0o , listitem = oo , isFolder = True )
 O0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00o0o0000o0o , listitem = oo , isFolder = True )
 return O0Oo
 if 33 - 33: I1I1i1 * oO0 / OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + i11iiII
def I1iiiiI1iII ( name , url , mode , iconimage ) :
 O00o0o0000o0o = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O0Oo = True
 oo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oo . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : "" } )
 oo . setProperty ( 'IsPlayable' , 'true' )
 O0Oo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00o0o0000o0o , listitem = oo )
 return O0Oo
 if 20 - 20: I1 + i1Ii % o00O00O0O0O / ooO0O * ooiii11iII
def i1I111I ( youtubeID ) :
 i11I1IIiiIi = IiIiIi ( youtubeID )
 II = xbmcgui . ListItem ( path = i11I1IIiiIi )
 II . setProperty ( "IsPlayable" , "true" )
 return xbmcplugin . setResolvedUrl ( O0O0OO0O0O0 , True , II )
 if 14 - 14: i1I11 . i1II1I11 / ii1
def IiIiIi ( youtubeID ) :
 i11I1IIiiIi = "plugin://plugin.video.youtube/?path=/root/video&action=play_video&videoid=" + youtubeID
 return i11I1IIiiIi
 if 57 - 57: ooO0O % OOooOOo
def O00 ( ) :
 I1iII1iiII = iI1Ii11111iIi ( i11I1IIiiIi + "&max-results=50" )
 i1i1II = re . compile ( "<openSearch:totalResults>(.+?)</openSearch:totalResults><openSearch:startIndex>(.+?)</openSearch:startIndex>" , re . DOTALL ) . findall ( I1iII1iiII )
 O0oo0OO0 = int ( i1i1II [ 0 ] [ 0 ] )
 I1i1iiI1 = int ( i1i1II [ 0 ] [ 1 ] )
 iiIIIII1i1iI = I1iII1iiII . split ( '<entry' )
 for oo00 in range ( 1 , len ( iiIIIII1i1iI ) , 1 ) :
  o00 = iiIIIII1i1iI [ oo00 ]
  i1i1II = re . compile ( "<yt:videoid>(.+?)</yt:videoid>" , re . DOTALL ) . findall ( o00 )
  i11I1 = i1i1II [ 0 ]
  i1i1II = re . compile ( "<title>(.+?)</title>" , re . DOTALL ) . findall ( o00 )
  o0oOoO00o = i1i1II [ 0 ]
  if len ( i1i1II ) > 0 :
   o0oOoO00o = i1i1II [ 0 ]
   o0oOoO00o = i1 ( o0oOoO00o )
  i1i1II = re . compile ( "<media:thumbnail url='(.+?)' height='90' width='120'" , re . DOTALL ) . findall ( o00 )
  oOOoo00O0O = ""
  if len ( i1i1II ) > 0 :
   oOOoo00O0O = i1i1II [ 0 ]
  I1iiiiI1iII ( "[B]" + o0oOoO00o + "[/B]" , i11I1 , 'playVideo' , oOOoo00O0O )
 if I1i1iiI1 + 50 <= O0oo0OO0 :
  I11i ( "[Next >]" , i11I1IIiiIi + "&start-index=" + str ( int ( I1i1iiI1 ) + 50 ) + "&max-results=50" , 'showItems' , oOOoo00O0O )
  if 8 - 8: ii1I - i1I11 % ii1I - ooO0O * I1I1i1
def i1 ( title ) :
 title = title . replace ( "&lt;" , "<" ) . replace ( "&gt;" , ">" ) . replace ( "&amp;" , "&" ) . replace ( "&#039;" , "\\" ) . replace ( "&quot;" , "\"" ) . replace ( "&szlig;" , "ß" ) . replace ( "&ndash;" , "-" )
 title = title . replace ( "&#038;" , "&" ) . replace ( "&#8230;" , "..." ) . replace ( "&#8211;" , "-" ) . replace ( "&#8220;" , "-" ) . replace ( "&#8221;" , "-" ) . replace ( "&#8217;" , "'" )
 title = title . replace ( "&Auml;" , "Ä" ) . replace ( "&Uuml;" , "Ü" ) . replace ( "&Ouml;" , "Ö" ) . replace ( "&auml;" , "ä" ) . replace ( "&uuml;" , "ü" ) . replace ( "&ouml;" , "ö" )
 title = title . strip ( )
 return title
 if 43 - 43: I1I1i1 - ooiii11iII * ii1I
def iI1Ii11111iIi ( url ) :
 O0O00o0OOO0 = urllib2 . Request ( url )
 O0O00o0OOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 return o0oo0o0O00OO
 if 80 - 80: ii11ii1ii
def oOOO0o0o ( parameters ) :
 iiI1 = { }
 if 19 - 19: o00O00O0O0O + ii1
 if parameters :
  ooo = parameters [ 1 : ] . split ( "&" )
  for ii1I1i1I in ooo :
   OOoo0O0 = ii1I1i1I . split ( '=' )
   if ( len ( OOoo0O0 ) ) == 2 :
    iiI1 [ OOoo0O0 [ 0 ] ] = OOoo0O0 [ 1 ]
 return iiI1
 if 41 - 41: I1
ii1i1I1i = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 53 - 53: i1I11 + I1I1i1 * I1
if os . path . exists ( ii1i1I1i ) == False :
 os . mkdir ( ii1i1I1i )
OooOooooOOoo0 = os . path . join ( ii1i1I1i , 'visitor' )
if 71 - 71: i1II1I11 % I1 % i1Ii
if os . path . exists ( OooOooooOOoo0 ) == False :
 from random import randint
 oO00ooo0 = open ( OooOooooOOoo0 , "w" )
 oO00ooo0 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oO00ooo0 . close ( )
 if 57 - 57: i1Ii . i1Ii
def OoOoOO00 ( k , e ) :
 OooOooo = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for oo00 in range ( len ( e ) ) :
  O000oo0O = k [ oo00 % len ( k ) ]
  OOOO = chr ( ( 256 + ord ( e [ oo00 ] ) - ord ( O000oo0O ) ) % 256 )
  OooOooo . append ( OOOO )
 return "" . join ( OooOooo )
 if 10 - 10: i1Ii / I1I1i1 * i1Ii
def IIIii1II1II ( utm_url ) :
 i1I1iI = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  O0O00o0OOO0 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : i1I1iI }
 )
  Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return Ii1iIIIi1ii
 if 93 - 93: ii1I % I1 * ii11ii1ii
def Ii11Ii1I ( group , name ) :
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
  O00oO = "1.0"
  I11i1I1I = open ( OooOooooOOoo0 ) . read ( )
  oO0Oo = "VNNews"
  oOOoo0Oo = "UA-52209804-2"
  o00OO00OoO = "www.viettv24.com"
  OOOO0OOoO0O0 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   O0Oo000ooO00 = OOOO0OOoO0O0 + "?" + "utmwv=" + O00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0Oo ) + "&utmac=" + oOOoo0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I11i1I1I , "1" , "1" , "2" ] )
   if 75 - 75: I1 . OOo0o0 * i1Ii
   if 91 - 91: ooO0O
   if 30 - 30: iI1OoOooOOOO . ooO0O - OOooOOo
   if 8 - 8: ii11ii1ii - ii1I * I11iii11IIi + i11iIiiIii / i1II1I11 % i1Ii
   if 16 - 16: i11iiII + OOo0o0 - I11iii11IIi
  else :
   if group == "None" :
    O0Oo000ooO00 = OOOO0OOoO0O0 + "?" + "utmwv=" + O00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0Oo + "/" + name ) + "&utmac=" + oOOoo0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I11i1I1I , "1" , "1" , "2" ] )
    if 85 - 85: OOoOoo00oo + ii11ii1ii
    if 58 - 58: I11iii11IIi * i1Ii * i11iiII / i1Ii
    if 75 - 75: I1
    if 50 - 50: ooO0O / oO0 - I1 - o00O00O0O0O % ooiii11iII - I1
    if 91 - 91: OOo0o0 / o00O00O0O0O - I11iii11IIi . o00O00O0O0O
   else :
    O0Oo000ooO00 = OOOO0OOoO0O0 + "?" + "utmwv=" + O00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0Oo + "/" + group + "/" + name ) + "&utmac=" + oOOoo0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , I11i1I1I , "1" , "1" , "2" ] )
    if 18 - 18: iI1OoOooOOOO
    if 98 - 98: ooiii11iII * ooiii11iII / ooiii11iII + o00O00O0O0O
    if 34 - 34: ii1
    if 15 - 15: o00O00O0O0O * ii1 * oO0 % i11iIiiIii % OOoOoo00oo - i1Ii
    if 68 - 68: i1II1I11 % ii11ii1ii . i1I11 . i11iiII
    if 92 - 92: ooiii11iII . i1II1I11
  print "============================ POSTING ANALYTICS ============================"
  IIIii1II1II ( O0Oo000ooO00 )
  if 31 - 31: i1II1I11 . OOoOoo00oo / iiI
  if not group == "None" :
   o000O0o = OOOO0OOoO0O0 + "?" + "utmwv=" + O00oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( o00OO00OoO ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oO0Oo + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oO0Oo ) + "&utmac=" + oOOoo0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , I11i1I1I , "1" , "2" ] )
   if 42 - 42: OOoOoo00oo
   if 41 - 41: oO0 . ii1 + iiI * iI1OoOooOOOO % oO0 * oO0
   if 19 - 19: ooiii11iII
   if 46 - 46: i11iiII - ooO0O . ii1I / i11iiII
   if 7 - 7: ii11ii1ii / I1I1i1 * i1II1I11 . i1I11 . ii1I
   if 13 - 13: i1Ii / i11iIiiIii
   if 2 - 2: I1I1i1 / iiI / iI1OoOooOOOO % OOoOoo00oo % ooO0O
   if 52 - 52: iI1OoOooOOOO
   try :
    print "============================ POSTING TRACK EVENT ============================"
    IIIii1II1II ( o000O0o )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 95 - 95: ooO0O
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 87 - 87: ii1 + OOoOoo00oo . i1Ii + OOoOoo00oo
oO = oOOO0o0o ( sys . argv [ 2 ] )
iIi1IIIi1 = oO . get ( 'mode' )
i11I1IIiiIi = oO . get ( 'url' )
O0oOoOOOoOO = oO . get ( 'name' )
if type ( i11I1IIiiIi ) == type ( str ( ) ) :
 i11I1IIiiIi = urllib . unquote_plus ( i11I1IIiiIi )
if type ( O0oOoOOOoOO ) == type ( str ( ) ) :
 O0oOoOOOoOO = urllib . unquote_plus ( O0oOoOOOoOO )
if iIi1IIIi1 == 'index' :
 Ii11Ii1I ( "Browse" , O0oOoOOOoOO )
 O00ooOO ( i11I1IIiiIi )
elif iIi1IIIi1 == 'showItems' :
 Ii11Ii1I ( "Browse" , O0oOoOOOoOO )
 O00 ( )
elif iIi1IIIi1 == 'showNextPlaylists' :
 Ii11Ii1I ( "Browse" , O0oOoOOOoOO )
 O00ooOO ( i11I1IIiiIi )
elif iIi1IIIi1 == 'playVideo' :
 Ii11Ii1I ( "Play" , O0oOoOOOoOO + "/" + i11I1IIiiIi )
 ii1ii11IIIiiI = xbmcgui . DialogProgress ( )
 ii1ii11IIIiiI . create ( 'SBTNOfficial Playlist' , 'Loading video. Please wait...' )
 i1I111I ( i11I1IIiiIi )
 ii1ii11IIIiiI . close ( )
 del ii1ii11IIIiiI
else :
 Ii11Ii1I ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( O0O0OO0O0O0 )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
