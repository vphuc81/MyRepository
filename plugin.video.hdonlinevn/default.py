#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.htvonline'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = "http://api.htvonline.com.vn/tv_channels"
 oOooOoO0Oo0O = '{"pageCount":200,"category_id":"-1","startIndex":0}'
 iI1 = i1I11i ( ii11i , oOooOoO0Oo0O )
 for OoOoOO00 in iI1 [ "data" ] :
  I11i = OoOoOO00 [ "link_play" ] [ 0 ] [ "resolution" ]
  O0O = OoOoOO00 [ "image" ]
  Oo = "%s (%s)" % ( OoOoOO00 [ "intro_text" ] , I11i )
  I1ii11iIi11i ( Oo . encode ( "utf8" ) , OoOoOO00 [ "id" ] . encode ( "utf8" ) , "playvideo" , O0O )
  if 48 - 48: oO0o / OOooOOo / I11iIi1I / IiiIII111iI
 try :
  IiII = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  if 49 - 49: IiII = xbmc . translatePath ( os . path . join ( IiII , "temp.jpg" ) )
  if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/htvonline.jpg' , IiII )
  if 49 - 49: iI1Ii11111iIi = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiII )
  if 49 - 49: i1i1II = xbmcgui . WindowDialog ( )
  if 49 - 49: i1i1II . addControl ( iI1Ii11111iIi )
  if 49 - 49: i1i1II . doModal ( )
 finally :
  pass
  if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 o0oOoO00o = xbmc . getSkinDir ( )
 if o0oOoO00o == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 43 - 43: O0OOo . II1Iiii1111i
def i1IIi11111i ( cid , title ) :
 ii11i = "http://api.htvonline.com.vn/tv_channels"
 oOooOoO0Oo0O = '{"pageCount":200,"category_id":"-1","startIndex":0}'
 iI1 = i1I11i ( ii11i , oOooOoO0Oo0O )
 for OoOoOO00 in iI1 [ "data" ] :
  print 'cid = %s - channel["id"] = %s' % ( cid , OoOoOO00 [ "id" ] . encode ( "utf8" ) )
  if OoOoOO00 [ "id" ] . encode ( "utf8" ) == cid :
   o000o0o00o0Oo = OoOoOO00 [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
   print o000o0o00o0Oo
   oo = xbmcgui . ListItem ( title )
   oo . setInfo ( 'video' , { 'Title' : title } )
   oo . setProperty ( "IsPlayable" , "true" )
   oo . setPath ( o000o0o00o0Oo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo )
   if 33 - 33: I1I1i1 * oO0 / OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + Oo0ooO0oo0oO
def i1I11i ( url , requestdata ) :
 i1iiIII111ii = urllib2 . Request ( urllib . unquote_plus ( url ) )
 i1iiIII111ii . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 i1iiIII111ii . add_header ( 'Authorization' , 'Basic YXBpaGF5aGF5dHY6NDUlJDY2N0Bk' )
 i1iiIII111ii . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 i1iIIi1 = urllib . urlencode ( { 'request' : requestdata } )
 ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii , i1iIIi1 , 120 )
 iI111I11I1I1 = ii11iIi1I . read ( )
 ii11iIi1I . close ( )
 iI111I11I1I1 = '' . join ( iI111I11I1I1 . splitlines ( ) )
 OOooO0OOoo = json . loads ( iI111I11I1I1 )
 return OOooO0OOoo
 if 29 - 29: o00ooo0 / ii1I
def IiIIIiI1I1 ( url ) :
 iI111I11I1I1 = ""
 if os . path . exists ( url ) == True :
  iI111I11I1I1 = open ( url ) . read ( )
 else :
  i1iiIII111ii = urllib2 . Request ( url )
  i1iiIII111ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii )
  iI111I11I1I1 = ii11iIi1I . read ( )
  ii11iIi1I . close ( )
 iI111I11I1I1 = '' . join ( iI111I11I1I1 . splitlines ( ) ) . replace ( '\'' , '"' )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '\n' , '' )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '\t' , '' )
 iI111I11I1I1 = re . sub ( '  +' , ' ' , iI111I11I1I1 )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '> <' , '><' )
 return iI111I11I1I1
 if 86 - 86: i11iIiiIii + I1I1i1 + iI1OoOooOOOO * II1Iiii1111i + o00ooo0
def I1ii11iIi11i ( name , cid , mode , iconimage ) :
 oOoO = sys . argv [ 0 ] + "?cid=" + urllib . quote_plus ( cid ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOo = True
 oOoOoO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oOoOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOoOoO . setProperty ( "IsPlayable" , "true" )
 oOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoO , listitem = oOoOoO )
 return oOo
 if 6 - 6: IiiIII111iI / o0OO0 % I1I1i1
def ooOO0O00 ( k , e ) :
 ii1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for o0oO0o00oo in range ( len ( e ) ) :
  II1i1Ii11Ii11 = k [ o0oO0o00oo % len ( k ) ]
  iII11i = chr ( ( 256 + ord ( e [ o0oO0o00oo ] ) - ord ( II1i1Ii11Ii11 ) ) % 256 )
  ii1 . append ( iII11i )
 return "" . join ( ii1 )
 if 97 - 97: II1Iiii1111i % II1Iiii1111i + I11iIi1I * oO0
def o0o00o0 ( parameters ) :
 iIi1ii1I1 = { }
 if 71 - 71: OOoOoo00oo . iiI
 if parameters :
  o0OO0oo0oOO = parameters [ 1 : ] . split ( "&" )
  for oo0oooooO0 in o0OO0oo0oOO :
   i11Iiii = oo0oooooO0 . split ( '=' )
   if ( len ( i11Iiii ) ) == 2 :
    iIi1ii1I1 [ i11Iiii [ 0 ] ] = i11Iiii [ 1 ]
 return iIi1ii1I1
 if 23 - 23: o00ooo0 . I11iIi1I
Oo0O0OOOoo = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 95 - 95: Oo0ooO0oo0oO % Oo0oO0ooo . iiI
if os . path . exists ( Oo0O0OOOoo ) == False :
 os . mkdir ( Oo0O0OOOoo )
I1i1I = os . path . join ( Oo0O0OOOoo , 'visitor' )
if 80 - 80: I1i1iI1i - Oo0ooO0oo0oO
if os . path . exists ( I1i1I ) == False :
 from random import randint
 OOO00 = open ( I1i1I , "w" )
 OOO00 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOO00 . close ( )
 if 21 - 21: oO0o - oO0o
def iIii11I ( utm_url ) :
 OOO0OOO00oo = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i1iiIII111ii = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOO0OOO00oo }
 )
  ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return ii11iIi1I
 if 31 - 31: I11iIi1I - O0OOo . OOoOoo00oo % I1i1iI1i - iiI
def iii11 ( group , name ) :
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
  O0oo0OO0oOOOo = "1.0"
  i1i1i11IIi = open ( I1i1I ) . read ( )
  II1III = "HTVOnline"
  iI1iI1I1i1I = "UA-52209804-2"
  iIi11Ii1 = "www.viettv24.com"
  Ii11iII1 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   Oo0O0O0ooO0O = Ii11iII1 + "?" + "utmwv=" + O0oo0OO0oOOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1III ) + "&utmac=" + iI1iI1I1i1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1i1i11IIi , "1" , "1" , "2" ] )
   if 15 - 15: o00 + I1i1iI1i - oO0o / O0OOo
   if 58 - 58: i11iIiiIii % II1Iiii1111i
   if 71 - 71: O0OOo + iI1OoOooOOOO % i11iIiiIii + o00 - OOo0o0
   if 88 - 88: I1i1iI1i - Oo0ooO0oo0oO % O0OOo
   if 16 - 16: IiiIII111iI * Oo0oO0ooo % OOo0o0
  else :
   if group == "None" :
    Oo0O0O0ooO0O = Ii11iII1 + "?" + "utmwv=" + O0oo0OO0oOOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1III + "/" + name ) + "&utmac=" + iI1iI1I1i1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1i1i11IIi , "1" , "1" , "2" ] )
    if 86 - 86: IiiIII111iI + I1I1i1 % i11iIiiIii * Oo0oO0ooo . iI1OoOooOOOO * II1Iiii1111i
    if 44 - 44: Oo0oO0ooo
    if 88 - 88: OOoOoo00oo % I1I1i1 . I11iIi1I
    if 38 - 38: o00ooo0
    if 57 - 57: iiI / Oo0oO0ooo * OOoOoo00oo / I1i1iI1i . I11iIi1I
   else :
    Oo0O0O0ooO0O = Ii11iII1 + "?" + "utmwv=" + O0oo0OO0oOOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1III + "/" + group + "/" + name ) + "&utmac=" + iI1iI1I1i1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , i1i1i11IIi , "1" , "1" , "2" ] )
    if 26 - 26: oO0
    if 91 - 91: Oo0ooO0oo0oO . o00 + Oo0ooO0oo0oO - oO0 / oO0o
    if 39 - 39: o00 / iI1OoOooOOOO - I11iIi1I
    if 98 - 98: o00 / II1Iiii1111i % Oo0oO0ooo . I1i1iI1i
    if 91 - 91: Oo0oO0ooo % o0OO0
    if 64 - 64: II1Iiii1111i % oO0 - OOoOoo00oo - Oo0oO0ooo
  print "============================ POSTING ANALYTICS ============================"
  iIii11I ( Oo0O0O0ooO0O )
  if 31 - 31: II1Iiii1111i - I11iIi1I . II1Iiii1111i
  if not group == "None" :
   i1I11i1I = Ii11iII1 + "?" + "utmwv=" + O0oo0OO0oOOOo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iIi11Ii1 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + II1III + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( II1III ) + "&utmac=" + iI1iI1I1i1I + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , i1i1i11IIi , "1" , "2" ] )
   if 81 - 81: ii1I + ii1I * OOo0o0 * iI1OoOooOOOO % iI1OoOooOOOO
   if 81 - 81: i11iIiiIii % I1i1iI1i - O0OOo
   if 68 - 68: OOoOoo00oo % OOooOOo . OOo0o0 . o00
   if 92 - 92: oO0 . OOoOoo00oo
   if 31 - 31: OOoOoo00oo . I1i1iI1i / iiI
   if 89 - 89: I1i1iI1i
   if 68 - 68: Oo0ooO0oo0oO * oO0o % iiI + Oo0ooO0oo0oO + iI1OoOooOOOO
   if 4 - 4: iI1OoOooOOOO + iiI * O0OOo
   try :
    print "============================ POSTING TRACK EVENT ============================"
    iIii11I ( i1I11i1I )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 55 - 55: o0OO0 + ii1I / I1i1iI1i * Oo0oO0ooo - i11iIiiIii - I1I1i1
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 25 - 25: o00
Ii1i = o0o00o0 ( sys . argv [ 2 ] )
I1 = Ii1i . get ( 'mode' )
iiIii = Ii1i . get ( 'cid' )
ooo0O = Ii1i . get ( 'name' )
oOooOoO0Oo0O = Ii1i . get ( 'requestdata' )
if type ( iiIii ) == type ( str ( ) ) :
 iiIii = urllib . unquote_plus ( iiIii )
if type ( oOooOoO0Oo0O ) == type ( str ( ) ) :
 oOooOoO0Oo0O = urllib . unquote_plus ( oOooOoO0Oo0O )
 if 75 - 75: o00ooo0 % o00ooo0 . OOoOoo00oo
III1iII1I1ii = str ( sys . argv [ 1 ] )
if I1 == 'playvideo' :
 iii11 ( "Play" , ooo0O + "/" + iiIii )
 oOOo0 = xbmcgui . DialogProgress ( )
 oOOo0 . create ( 'HTV Online' , 'Loading stream. Please wait...' )
 Oo = urllib . unquote_plus ( ooo0O )
 i1IIi11111i ( iiIii , Oo )
 oOOo0 . close ( )
 del oOOo0
else :
 iii11 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( III1iII1I1ii ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
