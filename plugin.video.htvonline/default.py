#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.htvonline"
if 51 - 51: IiI1i11I
@ oo000 . route ( '/' )
def Iii1I1 ( ) :
 OOO0O0O0ooooo ( "None" , "None" )
 try :
  iIIii1IIi = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  iIIii1IIi = xbmc . translatePath ( os . path . join ( iIIii1IIi , "temp.jpg" ) )
  '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/htvonline.jpg' , iIIii1IIi )
  o0OO00 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , iIIii1IIi )
  oo = xbmcgui . WindowDialog ( )
  oo . addControl ( o0OO00 )
  oo . doModal ( )'''
 finally :
  pass
 i1iII1IiiIiI1 = ""
 iIiiiI1IiI1I1 = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  sys = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in sys for b in iIiiiI1IiI1I1 ) : break
 while True :
  o0OoOoOO00 = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in o0OoOoOO00 for b in iIiiiI1IiI1I1 ) : break
 try :
  i1iII1IiiIiI1 = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   i1iII1IiiIiI1 = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , i1iII1IiiIiI1 . lower ( ) ) : break
 I11i = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( i1iII1IiiIiI1 , "5" , sys , o0OoOoOO00 ) ) . read ( )
 if "allowed" in I11i :
  O0O = "http://api.htvonline.com.vn/tv_channels"
  Oo = '{"pageCount":200,"category_id":"-1","startIndex":0}'
  I1ii11iIi11i = I1IiI ( O0O , Oo )
  o0OOO = [ ]
  for iIiiiI in I1ii11iIi11i [ "data" ] :
   I11i = iIiiiI [ "link_play" ] [ 0 ] [ "resolution" ]
   Iii1ii1II11i = iIiiiI [ "image" ]
   iI111iI = "%s (%s)" % ( iIiiiI [ "intro_text" ] . strip ( ) , I11i . strip ( ) )
   IiII = { }
   IiII [ "label" ] = iI111iI . encode ( "utf8" )
   IiII [ "is_playable" ] = True
   IiII [ "thumbnail" ] = Iii1ii1II11i
   IiII [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( iIiiiI [ "id" ] . encode ( "utf8" ) ) )
   o0OOO . append ( IiII )
 else :
  O0O = "http://api.htvonline.com.vn/tv_channels"
  Oo = '{"pageCount":200,"category_id":"-1","startIndex":0}'
  I1ii11iIi11i = I1IiI ( O0O , Oo )
  o0OOO = [ ]
  for iIiiiI in I1ii11iIi11i [ "data" ] :
   I11i = iIiiiI [ "link_play" ] [ 0 ] [ "resolution" ]
   Iii1ii1II11i = iIiiiI [ "image" ]
   iI111iI = "%s (%s)" % ( iIiiiI [ "intro_text" ] . strip ( ) , I11i . strip ( ) )
   IiII = { }
   IiII [ "label" ] = iI111iI . encode ( "utf8" )
   IiII [ "is_playable" ] = True
   IiII [ "thumbnail" ] = Iii1ii1II11i
   IiII [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( iIiiiI [ "id" ] . encode ( "utf8" ) ) )
   o0OOO . append ( IiII )
  if 41 - 41: I1II1
 if oo000 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return oo000 . finish ( o0OOO , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return oo000 . finish ( o0OOO , view_mode = 52 )
  else :
   return oo000 . finish ( o0OOO )
 else :
  return oo000 . finish ( o0OOO )
  if 100 - 100: iII1iII1i1iiI % iiIIIII1i1iI % iiI11iii111 % i1I1Ii1iI1ii
  if 11 - 11: OOoO / ooo0Oo0 * i1 - OOooo0000ooo
@ oo000 . route ( '/play/<url>' )
def OOo000 ( url ) :
 OOO0O0O0ooooo ( "Play" , '/play/%s' % ( url ) )
 O0 = xbmcgui . DialogProgress ( )
 O0 . create ( 'HTVOnline' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( I11i1i11i1I ( url ) )
 O0 . close ( )
 del O0
 if 31 - 31: i11iI / Oo0o0ooO0oOOO + I1 - OOoOoo00oo - iiI11
def I11i1i11i1I ( cid ) :
 if "http" not in cid :
  O0O = "http://api.htvonline.com.vn/tv_channels"
  Oo = '{"pageCount":200,"category_id":"-1","startIndex":0}'
  I1ii11iIi11i = I1IiI ( O0O , Oo )
  OOooO = ""
  for iIiiiI in I1ii11iIi11i [ "data" ] :
   if iIiiiI [ "id" ] . encode ( "utf8" ) == cid :
    OOooO = iIiiiI [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
  return OOooO
 else :
  try :
   OOoO00o = II111iiii ( cid )
   return re . compile ( 'data-source="(http://.+?m3u8.+?)"' ) . findall ( OOoO00o ) [ 0 ]
  except :
   return None
   if 48 - 48: I1Ii . IiIi1Iii1I1 - O0O0O0O00OooO % Ooooo % i1iIIIiI1I - OOoOoo00oo
def I1IiI ( url , requestdata ) :
 OoO000 = urllib2 . Request ( urllib . unquote_plus ( url ) )
 OoO000 . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 OoO000 . add_header ( 'Authorization' , 'Basic YXBpaGF5aGF5dHY6NDUlJDY2N0Bk' )
 OoO000 . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 IIiiIiI1 = urllib . urlencode ( { 'request' : requestdata } )
 iiIiIIi = urllib2 . urlopen ( OoO000 , IIiiIiI1 , 120 )
 OOoO00o = iiIiIIi . read ( )
 iiIiIIi . close ( )
 OOoO00o = '' . join ( OOoO00o . splitlines ( ) )
 ooOoo0O = json . loads ( OOoO00o )
 return ooOoo0O
 if 76 - 76: I1II1 / i11iI . OOoO * I1Ii - OOoOoo00oo
def II111iiii ( url ) :
 OOoO00o = ""
 if os . path . exists ( url ) == True :
  OOoO00o = open ( url ) . read ( )
 else :
  OoO000 = urllib2 . Request ( url )
  OoO000 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  iiIiIIi = urllib2 . urlopen ( OoO000 )
  OOoO00o = iiIiIIi . read ( )
  iiIiIIi . close ( )
 OOoO00o = '' . join ( OOoO00o . splitlines ( ) ) . replace ( '\'' , '"' )
 OOoO00o = OOoO00o . replace ( '\n' , '' )
 OOoO00o = OOoO00o . replace ( '\t' , '' )
 OOoO00o = re . sub ( '  +' , ' ' , OOoO00o )
 OOoO00o = OOoO00o . replace ( '> <' , '><' )
 return OOoO00o
 if 76 - 76: IiI1i11I / iII1iII1i1iiI . Oo0o0ooO0oOOO % OOoOoo00oo / iiIIIII1i1iI % I1
o0ooo00O0o0 = xbmc . translatePath ( xbmcaddon . Addon ( 'plugin.video.htvonline' ) . getAddonInfo ( 'profile' ) )
if 63 - 63: I1Ii
if os . path . exists ( o0ooo00O0o0 ) == False :
 os . mkdir ( o0ooo00O0o0 )
O00 = os . path . join ( o0ooo00O0o0 , 'visitor' )
if 35 - 35: i11iI + IiIi1Iii1I1 + IiIi1Iii1I1
if os . path . exists ( O00 ) == False :
 from random import randint
 I11I11i1I = open ( O00 , "w" )
 I11I11i1I . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 I11I11i1I . close ( )
 if 49 - 49: i1I1Ii1iI1ii % IiIi1Iii1I1 * I1II1
def oOOo0oo ( utm_url ) :
 o0oo0o0O00OO = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  OoO000 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : o0oo0o0O00OO }
 )
  iiIiIIi = urllib2 . urlopen ( OoO000 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iiIiIIi
 if 80 - 80: iiI11iii111
def OOO0O0O0ooooo ( group , name ) :
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
  oOOO0o0o = "1.0"
  iiI1 = open ( O00 ) . read ( )
  i11Iiii = "HTVOnline"
  iI = "UA-52209804-2"
  I1i1I1II = "www.viettv24.com"
  i1IiIiiI = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   I1I = i1IiIiiI + "?" + "utmwv=" + oOOO0o0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11Iiii ) + "&utmac=" + iI + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiI1 , "1" , "1" , "2" ] )
   if 80 - 80: OOooo0000ooo - i1
   if 87 - 87: I1 / iiI11 - iiI11iii111 * OOoOoo00oo / iiIIIII1i1iI . I1II1
   if 1 - 1: i1I1Ii1iI1ii - iiI11 / iiI11
   if 46 - 46: I1Ii * OOoOoo00oo - i1 * I1 - Ooooo
   if 83 - 83: iiIIIII1i1iI
  else :
   if group == "None" :
    I1I = i1IiIiiI + "?" + "utmwv=" + oOOO0o0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11Iiii + "/" + name ) + "&utmac=" + iI + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiI1 , "1" , "1" , "2" ] )
    if 31 - 31: i1I1Ii1iI1ii - OOoOoo00oo . Ooooo % OOooo0000ooo - I1II1
    if 4 - 4: i1I1Ii1iI1ii / i1iIIIiI1I . IiIi1Iii1I1
    if 58 - 58: OOoOoo00oo * IiI1i11I / OOooo0000ooo % Ooooo - Oo0o0ooO0oOOO / I1
    if 50 - 50: OOoO
    if 34 - 34: OOoO * i1I1Ii1iI1ii % IiIi1Iii1I1 * OOooo0000ooo - OOoO
   else :
    I1I = i1IiIiiI + "?" + "utmwv=" + oOOO0o0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i11Iiii + "/" + group + "/" + name ) + "&utmac=" + iI + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiI1 , "1" , "1" , "2" ] )
    if 33 - 33: i11iI + OOoOoo00oo * i1 - ooo0Oo0 / I1 % I1Ii
    if 21 - 21: i1 * iII1iII1i1iiI % I1 * iiI11iii111
    if 16 - 16: I1II1 - Ooooo * iII1iII1i1iiI + IiIi1Iii1I1
    if 50 - 50: i1I1Ii1iI1ii - i1iIIIiI1I * Oo0o0ooO0oOOO / Ooooo + i11iI
    if 88 - 88: I1Ii / Ooooo + IiIi1Iii1I1 - i1I1Ii1iI1ii / i1iIIIiI1I - OOooo0000ooo
    if 15 - 15: Oo0o0ooO0oOOO + OOooo0000ooo - iiIIIII1i1iI / OOoOoo00oo
  print "============================ POSTING ANALYTICS ============================"
  oOOo0oo ( I1I )
  if 58 - 58: IiI1i11I % iiI11
  if not group == "None" :
   OO00Oo = i1IiIiiI + "?" + "utmwv=" + oOOO0o0o + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( I1i1I1II ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i11Iiii + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i11Iiii ) + "&utmac=" + iI + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , iiI1 , "1" , "2" ] )
   if 51 - 51: O0O0O0O00OooO * i11iI + iiI11 + i1
   if 66 - 66: OOooo0000ooo
   if 97 - 97: I1 % O0O0O0O00OooO * O0O0O0O00OooO
   if 39 - 39: I1Ii % O0O0O0O00OooO
   if 4 - 4: I1
   if 93 - 93: i1 % I1 . i1 * Ooooo % I1Ii . i1I1Ii1iI1ii
   if 38 - 38: i11iI
   if 57 - 57: I1II1 / I1 * Ooooo / OOooo0000ooo . i1I1Ii1iI1ii
   try :
    print "============================ POSTING TRACK EVENT ============================"
    oOOo0oo ( OO00Oo )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 26 - 26: IiIi1Iii1I1
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 91 - 91: i1 . Oo0o0ooO0oOOO + i1 - IiIi1Iii1I1 / iiIIIII1i1iI
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
