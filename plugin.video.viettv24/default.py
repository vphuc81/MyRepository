#!/usr/bin/python
#coding=utf-8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , base64 , json , shutil , zipfile
from math import radians , sqrt , sin , cos , atan2
from operator import itemgetter
import xmltodict
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.viettv24'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
iiiii = int ( sys . argv [ 1 ] )
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( ) :
 i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: i1I11i = xbmc . translatePath ( os . path . join ( i1I11i , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/viettv24.jpg' , i1I11i )
 if 49 - 49: OoOoOO00 = xbmcgui . WindowDialog ( )
 if 49 - 49: I11i = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , i1I11i )
 if 49 - 49: OoOoOO00 . addControl ( I11i )
 if 49 - 49: OoOoOO00 . doModal ( )
 if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
 I11iIi1I = IiiIII111iI ( IiII ( "ghjl" , "z9ze3KGXmeDP19jTld7T0dvc4J6bls3b1Jfd29zazdHGztPYzA==" ) )
 if 28 - 28: Ii11111i * iiI1i1
 for i1I1ii1II1iII , oooO0oo0oOOOO in eval ( I11iIi1I ) :
  O0oO ( i1I1ii1II1iII , oooO0oo0oOOOO , 'indexgroup' , i1I11i . replace ( "temp.jpg" , "icon.png" ) )
 o0oO0 = xbmc . getSkinDir ( )
 if o0oO0 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 100 - 100: i11Ii11I1Ii1i
def Ooo ( url ) :
 o0oOoO00o = IiiIII111iI ( url )
 i1oOOoo00O0O = re . compile ( '<name>(.+?)</name>' ) . findall ( o0oOoO00o )
 if len ( i1oOOoo00O0O ) == 1 :
  i1111 = re . compile ( '<item>(.+?)</item>' ) . findall ( o0oOoO00o )
  for i11 in i1111 :
   I11 = ""
   Oo0o0000o0o0 = ""
   oOo0oooo00o = ""
   if "/title" in i11 :
    Oo0o0000o0o0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i11 ) [ 0 ]
   if "/link" in i11 :
    oOo0oooo00o = re . compile ( '<link>(.+?)</link>' ) . findall ( i11 ) [ 0 ]
   if "/thumbnail" in i11 :
    I11 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11 ) [ 0 ]
   oO0o0o0ooO0oO ( i1oOOoo00O0O [ 0 ] + "/" + Oo0o0000o0o0 , oOo0oooo00o , 'play' , I11 )
  o0oO0 = xbmc . getSkinDir ( )
  if o0oO0 == 'skin.xeebo' :
   xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 else :
  for oo0o0O00 in i1oOOoo00O0O :
   O0oO ( oo0o0O00 , url + "&n=" + oo0o0O00 , 'index' , '' )
   if 68 - 68: o00oo . iI1OoOooOOOO + i11iiII
def I1iiiiI1iII ( url ) :
 IiIi11i = url . split ( "&n=" ) [ 1 ]
 o0oOoO00o = IiiIII111iI ( url )
 iIii1I111I11I = re . compile ( '<channel>(.+?)</channel>' ) . findall ( o0oOoO00o )
 for OO00OooO0OO in iIii1I111I11I :
  if IiIi11i in OO00OooO0OO :
   i1111 = re . compile ( '<item>(.+?)</item>' ) . findall ( OO00OooO0OO )
   for i11 in i1111 :
    I11 = ""
    Oo0o0000o0o0 = ""
    oOo0oooo00o = ""
    if "/title" in i11 :
     Oo0o0000o0o0 = re . compile ( '<title>(.+?)</title>' ) . findall ( i11 ) [ 0 ]
    if "/link" in i11 :
     oOo0oooo00o = re . compile ( '<link>(.+?)</link>' ) . findall ( i11 ) [ 0 ]
    if "/thumbnail" in i11 :
     I11 = re . compile ( '<thumbnail>(.+?)</thumbnail>' ) . findall ( i11 ) [ 0 ]
    oO0o0o0ooO0oO ( IiIi11i + "/" + Oo0o0000o0o0 , oOo0oooo00o , 'play' , I11 )
 o0oO0 = xbmc . getSkinDir ( )
 if o0oO0 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 28 - 28: iIii1
def IiII ( k , e ) :
 oOOoO0 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O0OoO000O0OO in range ( len ( e ) ) :
  iiI1IiI = k [ O0OoO000O0OO % len ( k ) ]
  II = chr ( ( 256 + ord ( e [ O0OoO000O0OO ] ) - ord ( iiI1IiI ) ) % 256 )
  oOOoO0 . append ( II )
 return "" . join ( oOOoO0 )
 if 57 - 57: ooOoo0O
def OooO0 ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as II11iiii1Ii :
  for OO0oOoo in II11iiii1Ii . infolist ( ) :
   O0o0Oo = OO0oOoo . filename . split ( '/' )
   i1I11i = dest_dir
   for Oo00OOOOO in O0o0Oo [ : - 1 ] :
    O0O , Oo00OOOOO = os . path . splitdrive ( Oo00OOOOO )
    O00o0OO , Oo00OOOOO = os . path . split ( Oo00OOOOO )
    if Oo00OOOOO in ( os . curdir , os . pardir , '' ) : continue
    i1I11i = os . path . join ( i1I11i , Oo00OOOOO )
   II11iiii1Ii . extract ( OO0oOoo , i1I11i )
   if 44 - 44: O0o / o0 + I11ii1 / o0OO0oo0oOO . i11Ii11I1Ii1i
def I1iii ( url ) :
 i1I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 i1iiI11I = xbmc . translatePath ( os . path . join ( i1I11i , "tmp" ) )
 if os . path . exists ( i1iiI11I ) :
  shutil . rmtree ( i1iiI11I )
 os . makedirs ( i1iiI11I )
 if ".zip" in url :
  iiii = xbmc . translatePath ( os . path . join ( i1iiI11I , "temp.zip" ) )
  urllib . urlretrieve ( url , iiii )
  OooO0 ( iiii , i1iiI11I )
 else :
  oO0o0O0OOOoo0 = xbmc . translatePath ( os . path . join ( i1iiI11I , "temp.jpg" ) )
  urllib . urlretrieve ( url , oO0o0O0OOOoo0 )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % i1iiI11I )
 if 48 - 48: iIIi1iI1II111 + iIIi1iI1II111 - o00oo . o0OO0oo0oOO / ii11i
def OoOOO00oOO0 ( url , title ) :
 if ( "youtube" in url ) :
  oOoo = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  iIii11I = oOoo [ 0 ] [ len ( oOoo [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  url = "plugin://plugin.video.youtube/play/?video_id=%s" % iIii11I
  xbmc . executebuiltin ( "xbmc.PlayMedia(" + url + ")" )
 else :
  if url . isdigit ( ) :
   OOO0OOO00oo = "http://www.viettv24.com/main/getStreamingServer.php"
   IiII = urllib . urlencode ( { 'strname' : '%s-' % url } )
   url = urllib2 . urlopen ( OOO0OOO00oo , data = IiII ) . read ( )
   print url
  title = urllib . unquote_plus ( title )
  Iii111II = xbmc . PlayList ( 1 )
  Iii111II . clear ( )
  iiii11I = xbmcgui . ListItem ( title )
  iiii11I . setInfo ( 'video' , { 'Title' : title } )
  Ooo0OO0oOO = xbmc . Player ( )
  Iii111II . add ( url , iiii11I )
  Ooo0OO0oOO . play ( Iii111II )
  if 50 - 50: ii1IiI1i
def Ii1i11IIii1I ( lat1 , lon1 , lat2 , lon2 ) :
 lat1 = radians ( lat1 )
 lon1 = radians ( lon1 )
 lat2 = radians ( lat2 )
 lon2 = radians ( lon2 )
 if 52 - 52: i11Ii11I1Ii1i - oOooOoO0Oo0O + ooOoo0O + ooOoo0O - i11Ii11I1Ii1i / I11ii1
 I1I = lon1 - lon2
 if 24 - 24: o00oo
 o0Oo0O0Oo00oO = 6372.8
 if 39 - 39: o0 - i1 * Ii11111i % i11Ii11I1Ii1i * i1 % i1
 OoOOOOO = sqrt (
 ( cos ( lat2 ) * sin ( I1I ) ) ** 2
 + ( cos ( lat1 ) * sin ( lat2 ) - sin ( lat1 ) * cos ( lat2 ) * cos ( I1I ) ) ** 2
 )
 iIi1i111II = sin ( lat1 ) * sin ( lat2 ) + cos ( lat1 ) * cos ( lat2 ) * cos ( I1I )
 OoOO00O = atan2 ( OoOOOOO , iIi1i111II )
 return o0Oo0O0Oo00oO * OoOO00O
 if 53 - 53: Ii11111i % oOooOoO0Oo0O - iiI1i1
def IiiIII111iI ( url ) :
 oOo0oooo00o = ""
 if os . path . exists ( url ) == True :
  oOo0oooo00o = open ( url ) . read ( )
 else :
  oO000Oo000 = urllib2 . Request ( url )
  oO000Oo000 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  i111IiI1I = urllib2 . urlopen ( oO000Oo000 )
  oOo0oooo00o = i111IiI1I . read ( )
  i111IiI1I . close ( )
  if 70 - 70: ooOoo0O . IIIiiIIii / i11Ii11I1Ii1i . ooOoo0O - iIIi1iI1II111 / o0
 if ( "xml" in url ) :
  oOo0oooo00o = IiII ( "umbala" , oOo0oooo00o )
 oOo0oooo00o = '' . join ( oOo0oooo00o . splitlines ( ) ) . replace ( '\'' , '"' )
 oOo0oooo00o = oOo0oooo00o . replace ( '\n' , '' )
 oOo0oooo00o = oOo0oooo00o . replace ( '\t' , '' )
 oOo0oooo00o = re . sub ( '  +' , ' ' , oOo0oooo00o )
 oOo0oooo00o = oOo0oooo00o . replace ( '> <' , '><' )
 return oOo0oooo00o
 if 62 - 62: ii11i * iiI1i1
def oO0o0o0ooO0oO ( name , url , mode , iconimage ) :
 i1OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo0oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 Oo0oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 if ( "youtube.com/user/" in url ) or ( "youtube.com/channel/" in url ) :
  i1OOO = "plugin://plugin.video.youtube/%s/%s/" % ( url . split ( "/" ) [ - 2 ] , url . split ( "/" ) [ - 1 ] )
  return xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1OOO , listitem = Oo0oOOo , isFolder = True )
 return xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1OOO , listitem = Oo0oOOo )
 if 58 - 58: i1 * i11iiII * o00oo / i11iiII
def O0oO ( name , url , mode , iconimage ) :
 i1OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oO0o0OOOO = True
 Oo0oOOo = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0oOOo . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oO0o0OOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i1OOO , listitem = Oo0oOOo , isFolder = True )
 return oO0o0OOOO
 if 68 - 68: O0o - I11ii1 - ii1IiI1i - o00oo + iIii1
def iiiI1I11i1 ( parameters ) :
 IIi1i11111 = { }
 if 81 - 81: i11iIiiIii % iiI1i1 - i11iiII
 if parameters :
  O0ooo0O0oo0 = parameters [ 1 : ] . split ( "&" )
  for oo0oOo in O0ooo0O0oo0 :
   o000O0o = oo0oOo . split ( '=' )
   if ( len ( o000O0o ) ) == 2 :
    IIi1i11111 [ o000O0o [ 0 ] ] = o000O0o [ 1 ]
 return IIi1i11111
 if 42 - 42: iiI1i1
if os . path . exists ( O0O0OO0O0O0 ) == False :
 os . mkdir ( O0O0OO0O0O0 )
IIIi1I1IIii1II = os . path . join ( O0O0OO0O0O0 , 'visitor' )
if 65 - 65: ooOoo0O . ii11i / iIIi1iI1II111 - ooOoo0O
if os . path . exists ( IIIi1I1IIii1II ) == False :
 from random import randint
 iii1i1iiiiIi = open ( IIIi1I1IIii1II , "w" )
 iii1i1iiiiIi . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 iii1i1iiiiIi . close ( )
 if 2 - 2: ii1IiI1i / iIIi1iI1II111 / i11Ii11I1Ii1i % iiI1i1 % ooOoo0O
def o0o00OO0 ( utm_url ) :
 i1I1ii = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  oO000Oo000 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : i1I1ii }
 )
  i111IiI1I = urllib2 . urlopen ( oO000Oo000 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return i111IiI1I
 if 61 - 61: i1
def O0OOO ( group , name ) :
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
  II11iIiIIIiI = "4.2.8"
  o0o = open ( IIIi1I1IIii1II ) . read ( )
  o00 = "VietTV24"
  OooOO000 = "UA-52209804-2"
  OOoOoo = "www.viettv24.com"
  oO0000OOo00 = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iiIi1IIiIi = oO0000OOo00 + "?" + "utmwv=" + II11iIiIIIiI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 ) + "&utmac=" + OooOO000 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o0o , "1" , "1" , "2" ] )
   if 75 - 75: ii1IiI1i + IIIiiIIii
   if 73 - 73: iIIi1iI1II111 - oOooOoO0Oo0O . i11iiII - i11iiII / iiI1i1
   if 45 - 45: ii11i % Ii11111i
   if 29 - 29: i11iiII + IIIiiIIii . i11iIiiIii - OOooo000oo0 / ii11i
   if 26 - 26: iIii1 . oOooOoO0Oo0O
  else :
   if group == "None" :
    iiIi1IIiIi = oO0000OOo00 + "?" + "utmwv=" + II11iIiIIIiI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 + "/" + name ) + "&utmac=" + OooOO000 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o0o , "1" , "1" , "2" ] )
    if 39 - 39: O0o - iIIi1iI1II111 % i11iIiiIii * I11ii1 . o0
    if 58 - 58: Ii11111i % i11iIiiIii . O0o / iI1OoOooOOOO
    if 84 - 84: O0o . o00oo / IIIiiIIii - ii1IiI1i / oOooOoO0Oo0O / i11Ii11I1Ii1i
    if 12 - 12: ii1IiI1i * O0o % OOooo000oo0 % ii11i
    if 20 - 20: i11iiII % ooOoo0O / ooOoo0O + ooOoo0O
   else :
    iiIi1IIiIi = oO0000OOo00 + "?" + "utmwv=" + II11iIiIIIiI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( o00 + "/" + group + "/" + name ) + "&utmac=" + OooOO000 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , o0o , "1" , "1" , "2" ] )
    if 45 - 45: iI1OoOooOOOO - o0 - oOooOoO0Oo0O - Ii11111i . i1 / iIIi1iI1II111
    if 51 - 51: iIIi1iI1II111 + O0o
    if 8 - 8: iI1OoOooOOOO * iiI1i1 - ooOoo0O - Ii11111i * i11iiII % ii1IiI1i
    if 48 - 48: iIIi1iI1II111
    if 11 - 11: iIii1 + oOooOoO0Oo0O - Ii11111i / i11Ii11I1Ii1i + IIIiiIIii . i1
    if 41 - 41: ooOoo0O - iIIi1iI1II111 - iIIi1iI1II111
  print "============================ POSTING ANALYTICS ============================"
  o0o00OO0 ( iiIi1IIiIi )
  if 68 - 68: i11iiII % I11ii1
  if not group == "None" :
   ooO00OO0 = oO0000OOo00 + "?" + "utmwv=" + II11iIiIIIiI + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( OOoOoo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + o00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( o00 ) + "&utmac=" + OooOO000 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , o0o , "1" , "2" ] )
   if 31 - 31: O0o % O0o % iIii1
   if 69 - 69: Ii11111i - IIIiiIIii + OOooo000oo0 / I11ii1
   if 49 - 49: iIIi1iI1II111 . O0o
   if 11 - 11: o0 * ii1IiI1i . ii11i % oOooOoO0Oo0O + O0o
   if 78 - 78: Ii11111i . i11iiII + Ii11111i / iIii1 / Ii11111i
   if 54 - 54: iiI1i1 % O0o
   if 37 - 37: iiI1i1 * IIIiiIIii / o0OO0oo0oOO - O0o % i1 . iI1OoOooOOOO
   if 88 - 88: O0o . i1 * i1 % I11ii1
   try :
    print "============================ POSTING TRACK EVENT ============================"
    o0o00OO0 ( ooO00OO0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 15 - 15: OOooo000oo0 * ii1IiI1i + i11iIiiIii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 6 - 6: o0OO0oo0oOO / i11iIiiIii + O0o * iI1OoOooOOOO
o00o0 = iiiI1I11i1 ( sys . argv [ 2 ] )
ii = o00o0 . get ( 'mode' )
OOooooO0Oo = o00o0 . get ( 'url' )
oo0o0O00 = o00o0 . get ( 'name' )
if type ( OOooooO0Oo ) == type ( str ( ) ) :
 OOooooO0Oo = urllib . unquote_plus ( OOooooO0Oo )
if type ( oo0o0O00 ) == type ( str ( ) ) :
 oo0o0O00 = urllib . unquote_plus ( oo0o0O00 )
 if 91 - 91: i11Ii11I1Ii1i . ii11i / iI1OoOooOOOO + OOooo000oo0
I1i = str ( sys . argv [ 1 ] )
if ii == 'index' :
 O0OOO ( "Browse" , oo0o0O00 )
 I1iiiiI1iII ( OOooooO0Oo )
elif ii == 'indexgroup' :
 O0OOO ( "Browse" , oo0o0O00 )
 Ooo ( OOooooO0Oo )
elif ii == 'play' :
 O0OOO ( "Play" , oo0o0O00 + "/" + OOooooO0Oo )
 if any ( x in OOooooO0Oo for x in [ ".jpg" , ".zip" ] ) :
  I1iii ( OOooooO0Oo )
 else :
  OOOOO0oo0O0O0 = xbmcgui . DialogProgress ( )
  OOOOO0oo0O0O0 . create ( 'Brought to you by VietTV24.com' , 'Loading video. Please wait...' )
  OoOOO00oOO0 ( OOooooO0Oo , oo0o0O00 )
  OOOOO0oo0O0O0 . close ( )
  del OOOOO0oo0O0O0
else :
 O0OOO ( "None" , "None" )
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( I1i ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
