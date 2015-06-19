#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64 , random
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.hayhaytv'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = "http://api.hayhaytv.vn/"
ooo0OO = "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash4/s100x100/293975_126352604193712_667893495_t.jpg"
II1 = "50"
if 64 - 64: Oooo % OOO0O / II1Ii / Ooo
def OoO0O00 ( ) :
 IIiIiII11i ( 'Search' , iiiii + 'search' , 'search' , 'http://static.hayhaytv.vn/layout_m/images/search_bt.png' , '' , '' )
 IIiIiII11i ( 'Phim bộ' , iiiii + 'hot/newest_bundle_movies' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Phim lẻ' , iiiii + 'hot/newest_single_movies' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Phim chiếu rạp' , iiiii + 'hot/cinema_movies' , 'index' , 'http://echipstore.net/addonicons/Cinema.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'TV Show' , iiiii + 'show' , 'index' , 'http://echipstore.net/addonicons/TVShows.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Theo thể loại' , iiiii + 'category' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' , '' , '' )
 IIiIiII11i ( 'Theo quốc gia' , iiiii + 'countries' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' , '' , '' )
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 try :
  I1IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  if 49 - 49: I1IiI = xbmc . translatePath ( os . path . join ( I1IiI , "temp.jpg" ) )
  if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/hayhaytv.jpg' , I1IiI )
  if 49 - 49: o0OOO = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I1IiI )
  if 49 - 49: iIiiiI = xbmcgui . WindowDialog ( )
  if 49 - 49: iIiiiI . addControl ( o0OOO )
  if 49 - 49: iIiiiI . doModal ( )
 finally :
  pass
  if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
def o0oO0 ( ) :
 oo00 = o00 ( Oo0oO0ooo , '' )
 for o0oOoO00o in oo00 [ 'data' ] :
  i1 = '{"type_film":-1,"pageCount":' + II1 + ',"category_id":' + o0oOoO00o [ 'id' ] + ',"startIndex":0,"order_id":"1","country_id":-1}'
  IIiIiII11i ( o0oOoO00o [ 'name' ] . encode ( 'utf-8' ) , iiiii + 'search/filter' , 'index' , 'hayhaytvicon' , '' , i1 )
  if 64 - 64: oo % O0Oooo00
def Ooo0 ( ) :
 oo00 = o00 ( Oo0oO0ooo , '' )
 for oo00000o0 in oo00 [ 'data' ] :
  i1 = '{"type_film":-1,"pageCount":' + II1 + ',"category_id":-1,"startIndex":0,"order_id":"1","country_id":' + oo00000o0 [ 'id' ] + '}'
  IIiIiII11i ( oo00000o0 [ 'name' ] . encode ( 'utf-8' ) , iiiii + 'search/filter' , 'index' , 'hayhaytvicon' , '' , i1 )
  if 34 - 34: O0o00 % o0ooo / OOO0Ooo0ooO0oOOOOo / I111IiIi % OoOOo / OOO0O
def I1IiIiiIII ( url , requestdata ) :
 oo00 = o00 ( url , requestdata )
 for iI11 in oo00 [ 'data' ] :
  iII111ii = ''
  if ( iI11 [ 'extension' ] != '' ) :
   iII111ii = '[COLOR yellow]' + iI11 [ 'extension' ] + '[/COLOR] - '
  iII111ii = iII111ii + '[B]' + iI11 [ 'name' ] + '[/B]'
  try :
   if ( iI11 [ 'last_episode' ] != '' ) :
    iII111ii = iII111ii + ' [COLOR green](' + iI11 [ 'last_episode' ] + ')[/COLOR]'
  except KeyError : pass
  if 'show' in url :
   IIiIiII11i ( iII111ii . encode ( 'utf-8' ) , iiiii + 'show/show_detail' , 'moviedetail' , iI11 [ 'image' ] . encode ( 'utf-8' ) , iI11 [ 'intro_text' ] . encode ( 'utf-8' ) , '{"show_id":"' + iI11 [ 'id' ] + '"}' )
  else :
   IIiIiII11i ( iII111ii . encode ( 'utf-8' ) , iiiii + 'movie/movie_detail' , 'moviedetail' , iI11 [ 'image' ] . encode ( 'utf-8' ) , iI11 [ 'intro_text' ] . encode ( 'utf-8' ) , '{"movie_id":"' + iI11 [ 'id' ] + '"}' )
 i1iIIi1 = json . loads ( requestdata )
 i1iIIi1 [ 'startIndex' ] = int ( i1iIIi1 [ 'startIndex' ] ) + int ( II1 )
 IIiIiII11i ( 'Next 50' , url , 'index' , '' , '' , json . dumps ( i1iIIi1 ) )
 ii11iIi1I = xbmc . getSkinDir ( )
 if ii11iIi1I == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(51)' )
  if 6 - 6: iI1Ii11111iIi * o0ooo
def O00O0O0O0 ( ) :
 try :
  ooO0O = xbmc . Keyboard ( '' , 'Enter search text' )
  ooO0O . doModal ( )
  if ( ooO0O . isConfirmed ( ) ) :
   ooiii11iII = ooO0O . getText ( )
  I1IiIiiIII ( Oo0oO0ooo , '{"pageCount":' + II1 + ',"key":"' + ooiii11iII + '","startIndex":0}' )
 except : pass
 if 42 - 42: I111IiIi + oO0o0ooO0
def OOoO000O0OO ( url , requestdata ) :
 iI11 = o00 ( url , requestdata ) [ 'data' ]
 if ( len ( iI11 [ 'list_episode' ] ) == 0 ) :
  for iiI1IiI in iI11 [ 'link_play' ] :
   II ( iiI1IiI [ 'resolution' ] . strip ( ) , iI11 [ 'id' ] . strip ( ) + iI11 [ 'vn_subtitle' ] . strip ( ) , 'playvideo' , iI11 [ 'image' ] )
   if 57 - 57: iiIIIII1i1iI
   if 14 - 14: iii1II11ii . I1ii11iIi11i / O0o00
 else :
  for IiiiI1II1I1 in iI11 [ 'list_episode' ] :
   for iiI1IiI in IiiiI1II1I1 [ 'link_play' ] :
    II ( '%s - %s' % ( IiiiI1II1I1 [ 'name' ] . encode ( 'utf-8' ) , iiI1IiI [ 'resolution' ] . strip ( ) . encode ( 'utf-8' ) ) , IiiiI1II1I1 [ 'id' ] . strip ( ) + IiiiI1II1I1 [ 'vn_subtitle' ] . strip ( ) , 'playvideo' , iI11 [ 'image' ] )
    if 95 - 95: II1Ii . OOO0O
    if 67 - 67: oo / II1Ii % O0Oooo00 - OOO0O
    if 82 - 82: i11iIiiIii . oo / iii1II11ii * Oooo % iiIIIII1i1iI % OOO0O
    if 78 - 78: OOO0O - O0o00 * i11iII1iiI + ii1II11I1ii1I + o0ooo + o0ooo
def I11I11i1I ( url , sub , title ) :
 ii11i1iIII = Ii1I ( "jlgh" , "nJ2XlpydmJabnZ2Wj98=" ) % random . randint ( 214 , 218 )
 Oo0o0 = xbmcgui . ListItem ( title )
 Oo0o0 . setInfo ( 'video' , { 'Title' : title } )
 if 49 - 49: iiIIIII1i1iI % O0o00 + Ooo . I1ii11iIi11i % oO0o0ooO0
 I1i1iii = Ii1I ( "dfg" , "34jLxdrIhqDC34jb3dbMhqCJysfKycjW09GJkIjM0cfQ0IihhtLMyNvg2M7W0s2ny9PIzdKVx9XUhuPE4Q==" )
 i1iiI11I = Ii1I ( "sda" , "29jV456QosXR3JLJ1N3J1N3V6ZLX4ZPW5snTotfK2tLW48PU4sfK1NDA4cnV6tPT3g==" )
 if 29 - 29: II1Ii
 iI = o00 ( i1iiI11I , I1i1iii )
 I1i1I1II = iI [ Ii1I ( "qw" , "1djl2A==" ) ]
 i1IiIiiI = I1i1I1II [ Ii1I ( "jkl" , "3trXz9nLy9vc" ) ]
 I1I = I1i1I1II [ Ii1I ( "sd" , "6NfY1tLN1w==" ) ]
 if 80 - 80: iI1Ii11111iIi - i11iII1iiI
 if 87 - 87: iiIIIII1i1iI / O0Oooo00 - Ooo * oo / II1Ii . Oooo
 iii11I111 = Ii1I ( "jkl" , "5Y3g2dbR2I2mjJDfjJeO397R3MrVzo2mjJDfjJeO19ri09DL08-OpI2R3Y3p" ) % ( i1IiIiiI , I1I , url )
 OOOO00ooo0Ooo = Ii1I ( "ghkj" , "z9zf2qGXmsvX0ZnSyOHTy-Dc4Zjd1prRzNzX09XTmtfW3tTP" )
 if " - " in urllib . unquote_plus ( OOOooOooo00O0 ) :
  OOOO00ooo0Ooo = OOOO00ooo0Ooo + "_episode"
  if 100 - 100: i11iIiiIii / iI1Ii11111iIi % I111IiIi - oO0o0ooO0 / iiIIIII1i1iI
 url = ""
 if "1080p" in urllib . unquote_plus ( OOOooOooo00O0 ) :
  url = o00 ( OOOO00ooo0Ooo , iii11I111 ) [ "data" ] [ "link_play" ] [ - 1 ] [ "mp3u8_link" ]
 else :
  url = o00 ( OOOO00ooo0Ooo , iii11I111 ) [ "data" ] [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
 url = Ii1I ( "ghkj" , "z9zf2qGXmo_aopyjmp2Q3abd1M6kjd6Q29fWz9WlkN0=" ) % ( ii11i1iIII , url . split ( ":1935" ) [ 1 ] , I1I , i1IiIiiI )
 if 50 - 50: I1ii11iIi11i
 if 34 - 34: I1ii11iIi11i * oOo0O0Ooo % o0ooo * iI1Ii11111iIi - I1ii11iIi11i
 if 33 - 33: ii1II11I1ii1I + oo * i11iII1iiI - iii1II11ii / iiIIIII1i1iI % O0o00
 if 21 - 21: i11iII1iiI * OOO0O % iiIIIII1i1iI * Ooo
 Oo0o0 . setProperty ( "IsPlayable" , "true" )
 Oo0o0 . setPath ( url )
 if 16 - 16: Oooo - I111IiIi * OOO0O + o0ooo
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0o0 )
 Ii11iII1 = xbmc . Player ( )
 if ( sub != '' ) :
  I1IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  I1IiI = xbmc . translatePath ( os . path . join ( I1IiI , "temp.sub" ) )
  urllib . urlretrieve ( sub , I1IiI )
  Ii11iII1 . setSubtitles ( I1IiI )
  if 51 - 51: oOo0O0Ooo * i11iII1iiI % ii1II11I1ii1I * oOo0O0Ooo % oO0o0ooO0 / OoOOo
def o00 ( url , requestdata ) :
 iIIIIii1 = urllib2 . Request ( urllib . unquote_plus ( url ) )
 if "user" not in url :
  oo000OO00Oo = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1X0197S9P7vn7UsUReZUBc8oK6IgjM99FYdX4lcwp68o/export?format=tsv' )
  O0OOO0OOoO0O = oo000OO00Oo . read ( )
  oo000OO00Oo . close ( )
  iIIIIii1 . set_proxy ( O0OOO0OOoO0O . split ( "\n" ) [ 0 ] , "http" )
  if 70 - 70: OOO0Ooo0ooO0oOOOOo * iii1II11ii * O0Oooo00 / O0o00
 iIIIIii1 . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 iIIIIii1 . add_header ( 'Authorization' , 'Basic YXBpaGF5OmFzb2tzYXBySkRMSVVSbzJ1MDF1cndqcQ==' )
 iIIIIii1 . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 oO = urllib . urlencode ( { 'request' : requestdata , 'device' : 'android' , 'secure_token' : '1.0' } )
 iI = urllib2 . urlopen ( iIIIIii1 , oO , 120 )
 OOoO0O00o0 = iI . read ( )
 iI . close ( )
 OOoO0O00o0 = '' . join ( OOoO0O00o0 . splitlines ( ) )
 iII = json . loads ( OOoO0O00o0 )
 return iII
 if 80 - 80: OOO0Ooo0ooO0oOOOOo . iiIIIII1i1iI
def IIi ( url ) :
 OOoO0O00o0 = ""
 if os . path . exists ( url ) == True :
  OOoO0O00o0 = open ( url ) . read ( )
 else :
  iIIIIii1 = urllib2 . Request ( url )
  iIIIIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  iI = urllib2 . urlopen ( iIIIIii1 )
  OOoO0O00o0 = iI . read ( )
  iI . close ( )
 OOoO0O00o0 = '' . join ( OOoO0O00o0 . splitlines ( ) ) . replace ( '\'' , '"' )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '\n' , '' )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '\t' , '' )
 OOoO0O00o0 = re . sub ( '  +' , ' ' , OOoO0O00o0 )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '> <' , '><' )
 return OOoO0O00o0
 if 26 - 26: o0ooo
def II ( name , url , mode , iconimage ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Oo0OoO00oOO0o . setProperty ( "IsPlayable" , "true" )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = Oo0OoO00oOO0o )
 return Oo0oOOo
 if 80 - 80: iiIIIII1i1iI + oo - oo % o0ooo
def IIiIiII11i ( name , url , mode , iconimage , plot , requestdata ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&requestdata=" + urllib . quote_plus ( requestdata )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : plot } )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = Oo0OoO00oOO0o , isFolder = True )
 return Oo0oOOo
 if 63 - 63: I1ii11iIi11i - oO0o0ooO0 + Oooo % O0Oooo00 / OOO0O / ii1II11I1ii1I
def Ii1I ( k , e ) :
 O0o0O00Oo0o0 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O00O0oOO00O00 in range ( len ( e ) ) :
  i1Oo00 = k [ O00O0oOO00O00 % len ( k ) ]
  i1i = chr ( ( 256 + ord ( e [ O00O0oOO00O00 ] ) - ord ( i1Oo00 ) ) % 256 )
  O0o0O00Oo0o0 . append ( i1i )
 return "" . join ( O0o0O00Oo0o0 )
 if 50 - 50: OOO0Ooo0ooO0oOOOOo
def i11I1iIiII ( parameters ) :
 oO00o0 = { }
 if 55 - 55: iii1II11ii + OOO0O / iI1Ii11111iIi * iiIIIII1i1iI - i11iIiiIii - O0o00
 if parameters :
  ii1ii1ii = parameters [ 1 : ] . split ( "&" )
  for oooooOoo0ooo in ii1ii1ii :
   I1I1IiI1 = oooooOoo0ooo . split ( '=' )
   if ( len ( I1I1IiI1 ) ) == 2 :
    oO00o0 [ I1I1IiI1 [ 0 ] ] = I1I1IiI1 [ 1 ]
 return oO00o0
 if 5 - 5: ii1II11I1ii1I * OoOOo + iI1Ii11111iIi . oo + iI1Ii11111iIi
oOiIi1IIIi1 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 86 - 86: O0Oooo00 % iI1Ii11111iIi / I1ii11iIi11i / iI1Ii11111iIi
if os . path . exists ( oOiIi1IIIi1 ) == False :
 os . mkdir ( oOiIi1IIIi1 )
iIIi1i1 = os . path . join ( oOiIi1IIIi1 , 'visitor' )
if 10 - 10: O0Oooo00
if os . path . exists ( iIIi1i1 ) == False :
 from random import randint
 OOooOO000 = open ( iIIi1i1 , "w" )
 OOooOO000 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOooOO000 . close ( )
 if 97 - 97: oO0o0ooO0 + oo / OOO0O / o0ooo
def I1111IIi ( utm_url ) :
 Oo0oO = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iIIIIii1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : Oo0oO }
 )
  iI = urllib2 . urlopen ( iIIIIii1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iI
 if 1 - 1: i11iII1iiI - iiIIIII1i1iI . O0Oooo00 . i11iII1iiI / iii1II11ii + O0Oooo00
def OooOOOOo ( group , name ) :
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
  oo0O0oO = "1.0"
  ooooo = open ( iIIi1i1 ) . read ( )
  II1I = "HayHayTV"
  O0 = "UA-52209804-2"
  i1II1Iiii1I11 = "www.viettv24.com"
  IIII = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iiIiI = IIII + "?" + "utmwv=" + oo0O0oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1I ) + "&utmac=" + O0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooooo , "1" , "1" , "2" ] )
   if 91 - 91: o0ooo % Ooo % OOO0O
   if 20 - 20: oo % O0o00 / O0o00 + O0o00
   if 45 - 45: iiIIIII1i1iI - OOO0Ooo0ooO0oOOOOo - II1Ii - i11iII1iiI . oOo0O0Ooo / Oooo
   if 51 - 51: Oooo + o0ooo
   if 8 - 8: iiIIIII1i1iI * iI1Ii11111iIi - O0o00 - i11iII1iiI * oo % I1ii11iIi11i
  else :
   if group == "None" :
    iiIiI = IIII + "?" + "utmwv=" + oo0O0oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1I + "/" + name ) + "&utmac=" + O0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooooo , "1" , "1" , "2" ] )
    if 48 - 48: Oooo
    if 11 - 11: O0Oooo00 + II1Ii - i11iII1iiI / ii1II11I1ii1I + iii1II11ii . oOo0O0Ooo
    if 41 - 41: O0o00 - Oooo - Oooo
    if 68 - 68: oo % I111IiIi
    if 88 - 88: OOO0O - OoOOo + oo
   else :
    iiIiI = IIII + "?" + "utmwv=" + oo0O0oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( II1I + "/" + group + "/" + name ) + "&utmac=" + O0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , ooooo , "1" , "1" , "2" ] )
    if 40 - 40: I1ii11iIi11i * O0o00 + oo % o0ooo
    if 74 - 74: iiIIIII1i1iI - iii1II11ii + II1Ii + I111IiIi / iI1Ii11111iIi
    if 23 - 23: Oooo
    if 85 - 85: O0o00
    if 84 - 84: I1ii11iIi11i . OOO0O % II1Ii + O0o00 % II1Ii % i11iII1iiI
    if 42 - 42: i11iII1iiI / O0Oooo00 / ii1II11I1ii1I + o0ooo / iI1Ii11111iIi
  print "============================ POSTING ANALYTICS ============================"
  I1111IIi ( iiIiI )
  if 84 - 84: OoOOo * oOo0O0Ooo + iii1II11ii
  if not group == "None" :
   O0ooO0Oo00o = IIII + "?" + "utmwv=" + oo0O0oO + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( i1II1Iiii1I11 ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + II1I + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( II1I ) + "&utmac=" + O0 + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , ooooo , "1" , "2" ] )
   if 77 - 77: OOO0O * i11iII1iiI
   if 95 - 95: I1ii11iIi11i + i11iIiiIii
   if 6 - 6: OoOOo / i11iIiiIii + o0ooo * iiIIIII1i1iI
   if 80 - 80: oOo0O0Ooo
   if 83 - 83: O0Oooo00 . i11iIiiIii + oOo0O0Ooo . ii1II11I1ii1I * O0Oooo00
   if 53 - 53: oOo0O0Ooo
   if 31 - 31: i11iII1iiI
   if 80 - 80: I111IiIi . i11iIiiIii - ii1II11I1ii1I
   try :
    print "============================ POSTING TRACK EVENT ============================"
    I1111IIi ( O0ooO0Oo00o )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 25 - 25: i11iII1iiI
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 62 - 62: oo + Oooo
oO0OOOO0 = i11I1iIiII ( sys . argv [ 2 ] )
iI1I11iiI1i = oO0OOOO0 . get ( 'mode' )
Oo0oO0ooo = oO0OOOO0 . get ( 'url' )
OOOooOooo00O0 = oO0OOOO0 . get ( 'name' )
oO0o0Ooooo = oO0OOOO0 . get ( 'requestdata' )
if type ( Oo0oO0ooo ) == type ( str ( ) ) :
 Oo0oO0ooo = urllib . unquote_plus ( Oo0oO0ooo )
if type ( oO0o0Ooooo ) == type ( str ( ) ) :
 oO0o0Ooooo = urllib . unquote_plus ( oO0o0Ooooo )
 if 94 - 94: ii1II11I1ii1I * O0o00 / iii1II11ii / O0o00
oO0 = str ( sys . argv [ 1 ] )
if iI1I11iiI1i == 'index' :
 OooOOOOo ( "Browse" , OOOooOooo00O0 )
 I1IiIiiIII ( Oo0oO0ooo , oO0o0Ooooo )
elif iI1I11iiI1i == 'search' :
 OooOOOOo ( "None" , "Search" )
 O00O0O0O0 ( )
elif iI1I11iiI1i == 'videosbycategory' :
 OooOOOOo ( "Browse" , OOOooOooo00O0 )
 o0oO0 ( )
elif iI1I11iiI1i == 'videosbyregion' :
 OooOOOOo ( "Browse" , OOOooOooo00O0 )
 Ooo0 ( )
elif iI1I11iiI1i == 'moviedetail' :
 OooOOOOo ( "Browse" , OOOooOooo00O0 )
 OOoO000O0OO ( Oo0oO0ooo , oO0o0Ooooo )
elif iI1I11iiI1i == 'playvideo' :
 OooOOOOo ( "Play" , OOOooOooo00O0 + "/" + Oo0oO0ooo )
 O0OO0O = xbmcgui . DialogProgress ( )
 O0OO0O . create ( 'HayHayTV' , 'Loading video. Please wait...' )
 OO = urllib . unquote_plus ( OOOooOooo00O0 ) . replace ( 'Play [' , '' ) . replace ( ']' , '' )
 if len ( Oo0oO0ooo . split ( 'http' ) ) > 1 :
  I11I11i1I ( Oo0oO0ooo . split ( 'http' ) [ 0 ] , 'http' + Oo0oO0ooo . split ( 'http' ) [ 1 ] , OO )
 else :
  I11I11i1I ( Oo0oO0ooo . split ( 'http' ) [ 0 ] , '' , OO )
 O0OO0O . close ( )
 del O0OO0O
 if 83 - 83: Oooo / I1ii11iIi11i - i11iII1iiI - oo
else :
 OooOOOOo ( "None" , "None" )
 OoO0O00 ( )
xbmcplugin . endOfDirectory ( int ( oO0 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
