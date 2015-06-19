#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , random , base64 , json , time , datetime
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.kodi4vn.megafun'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = oOooOoO0Oo0O ( )
 for iI1 in ii11i [ 'object' ] :
  if ( iI1 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( ) not in [ 'True Sport' , 'QTV1' , 'QTV3' ] ) :
   i1I11i = 'http://c2.cdn.truelife.vn/offica/community/avatar?c=%s&m=1' % iI1 [ 'ownerId' ]
   OoOoOO00 = '[B][COLOR green]%s[/COLOR][/B] - ' % iI1 [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( )
   I11i = ''
   O0O = '[B]Đang chiếu[/B]'
   if iI1 [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I11i = '[B]%s[/B]: ' % iI1 [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if iI1 [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : O0O = '[COLOR yellow]%s[/COLOR]' % iI1 [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   Oo ( OoOoOO00 + I11i + O0O , iI1 [ 'ownerId' ] , i1I11i , 'channelprogram' )
   if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
 IiII = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: IiII = xbmc . translatePath ( os . path . join ( IiII , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/megafun.jpg' , IiII )
 if 49 - 49: iI1Ii11111iIi = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiII )
 if 49 - 49: i1i1II = xbmcgui . WindowDialog ( )
 if 49 - 49: i1i1II . addControl ( iI1Ii11111iIi )
 if 49 - 49: i1i1II . doModal ( )
 if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( channelid ) :
 i1oOOoo00O0O = i1111 ( channelid )
 i11 = I11 ( )
 Oo0o0000o0o0 = datetime . datetime . fromtimestamp ( i11 ) . strftime ( '%Y-%m-%d %H:%M:%S' )
 oOo0oooo00o ( '[B]%s: Đang chiếu...[/B]' % ( Oo0o0000o0o0 ) , channelid , 'playvideo' , '' , '' )
 if 65 - 65: O0o * i1iIIII * I1
 for O0OoOoo00o in reversed ( i1oOOoo00O0O [ 'object' ] ) :
  iiiI11 = O0OoOoo00o [ 'dateTimeBegin' ] . split ( '.' ) [ 0 ]
  OOooO = time . mktime ( time . strptime ( iiiI11 , '%Y-%m-%d %H:%M:%S' ) )
  if OOooO < i11 :
   OOoO00o = '[B]%s[/B]: ' % O0OoOoo00o [ 'dateTimeBegin' ] . encode ( 'utf-8' ) . strip ( ) . split ( '.' ) [ 0 ]
   I11i = ''
   II111iiii = '[B]Đang chiếu[/B]'
   if O0OoOoo00o [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I11i = '[COLOR yellow]%s[/COLOR]: ' % O0OoOoo00o [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if O0OoOoo00o [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : II111iiii = '[B]%s[/B]' % O0OoOoo00o [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   oOo0oooo00o ( OOoO00o + I11i + II111iiii , channelid , 'playvideo' , O0OoOoo00o [ 'dateTimeBegin' ] , str ( O0OoOoo00o [ 'duration' ] ) )
   if 48 - 48: I1Ii . IiIi1Iii1I1 - IiIi1Iii1I1 % IiIi1Iii1I1 - o00ooo0 * Oo0oO0ooo
def O00OooO0 ( channelid , starttime , duration ) :
 Ooooo = o00o ( channelid )
 IiI1I1 = Ooooo [ 'object' ] [ 0 ] [ 'streamingUrl' ] . split ( '&' ) [ 0 ] . replace ( 'c=' , '' )
 IiI1I1 = IiI1I1 . replace ( 'vstv018' , 'vstv093' )
 if starttime != '' or duration != '' :
  OOooO = time . mktime ( time . strptime ( starttime . split ( '.' ) [ 0 ] , '%Y-%m-%d %H:%M:%S' ) )
  if 86 - 86: i11iIiiIii + O0o + IiIi1Iii1I1 * Oo0oO0ooo + Oo0ooO0oo0oO
  OOoO00o = datetime . datetime . fromtimestamp ( OOooO ) . strftime ( '%H%M' )
  oOoO = datetime . datetime . fromtimestamp ( OOooO ) . strftime ( '%y%m%d' )
  oOo = oOoOoO ( IiI1I1 , oOoO , OOoO00o )
 else :
  oOo = ii1IOooO0 ( IiI1I1 )
 II11iiii1Ii = xbmc . Player ( )
 II11iiii1Ii . play ( oOo )
 if 70 - 70: o00ooo0 / ii1I % IiIi1Iii1I1 % i11iIiiIii . OOooOOo
def I11 ( ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/community/action?_f=7&jsoncallback=Ext.data.JsonP.callback2" )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.callback2(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 iIi1ii1I1 = I11i1 [ 'header' ] [ 'sysdate' ] . replace ( ' ICT' , '' ) . encode ( 'utf-8' )
 o0I11II1i = time . mktime ( time . strptime ( iIi1ii1I1 , '%a %b %d %H:%M:%S %Y' ) )
 return o0I11II1i
 if 23 - 23: I1i1iI1i / Oo0ooO0oo0oO + Oo0oO0ooo + Oo0oO0ooo / ii1IiI1i
def o00o ( channelid ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/truelifetv/lib/action?_f=119&tvChannelId=%s&ownerId=1532&jsoncallback=Ext.data.JsonP.tvprofile" % channelid )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJvDE1HIHREnmHbaJbKVVNyAsEMqwvy162y0dPlCA5mNkifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvprofile(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 26 - 26: o0
def i1111 ( channelid ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=14&communityId=%s&jsoncallback=Ext.data.JsonP.tvshow1205151412" % channelid )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJisQ26UQYnnCkwbck2oeVngMSDmkUKxjgYQoWsu|6GGsifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 12 - 12: o0 % o0OO0 / IiIi1Iii1I1 % Oo0ooO0oo0oO
def oOooOoO0Oo0O ( ) :
 O0o0Oo = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=17&ownerId=1532&jsoncallback=Ext.data.JsonP.tvshow1205151412" )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0o0Oo . add_header ( 'DNT' , '1' )
 O0o0Oo . add_header ( 'Connection' , 'keep-alive' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 29 - 29: o0
def iI ( ) :
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( "http://s22.ctl.vsolutions.vn/ctl/tvlive/s/?script&json" ) )
 O0o0Oo . add_header ( 'Host' , 's22.ctl.vsolutions.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 return I11i1
 if 28 - 28: o00 - I1 . I1 + o0OO0 - o0 + iiI
def oOoOoO ( vstv , date , st ) :
 oOoOooOo0o0 = str ( int ( time . time ( ) ) )
 OOOO = base64 . b64encode ( oOoOooOo0o0 )
 OOO00 = ""
 for iiiiiIIii in range ( 1 , 7 ) :
  O000OO0 = random . randrange ( 0 , len ( "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" ) )
  OOO00 = OOO00 + "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" [ O000OO0 : O000OO0 + 1 ]
 I11iii1Ii = "" ;
 for I1IIiiIiii in range ( 0 , len ( OOOO ) ) :
  I11iii1Ii = I11iii1Ii + OOOO [ I1IIiiIiii : I1IIiiIiii + 1 ]
  if ( I1IIiiIiii < len ( OOO00 ) ) :
   I11iii1Ii = I11iii1Ii + OOO00 [ I1IIiiIiii : I1IIiiIiii + 1 ]
 O000oo0O = base64 . b64encode ( I11iii1Ii )
 OOOOi11i1 = ""
 for IIIii1II1II in range ( 0 , len ( O000oo0O ) - 1 ) :
  OOOOi11i1 = OOOOi11i1 + O000oo0O [ IIIii1II1II : IIIii1II1II + 1 ]
  if ( IIIii1II1II < len ( OOO00 ) ) :
   OOOOi11i1 = OOOOi11i1 + OOO00 [ IIIii1II1II : IIIii1II1II + 1 ]
 OOOOi11i1 = OOOOi11i1 . replace ( "=" , "" )
 i1I1iI = { 'location' : '' , 'device_type' : '2' , 'mf_code' : vstv , 'device_id' : '487142' , 'date' : date , 'channel_id' : '1' , 'member_id' : '107805' , 'end_time' : '2359' , 'app_v' : '63' , 'manufacturer_id' : 'E94F6043C85AF86080CA27A439A1D766' , 'start_time' : st , 'tid' : OOOOi11i1 , 'profile' : '2' }
 oo0OooOOo0 = urllib . urlencode ( i1I1iI )
 if 92 - 92: i1iIIII . Oo0oO0ooo + Oo0ooO0oo0oO
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( oOoO ( "u" , "3enp5a-kpOTp6aPi7unr49rpo-vjpOuqpNjd1uPj2uGk4uTX3uHapOnr5Nmi6ufh" ) ) )
 O0o0Oo . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded; charset=utf-8' )
 O0o0Oo . add_header ( 'User-Agent' , 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Nexus 5 Build/KOT49H)' )
 O0o0Oo . add_header ( 'Host' , 'ott.mytvnet.vn' )
 O0o0Oo . add_header ( 'Connection' , 'Keep-Alive' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo , oo0OooOOo0 )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 O0OO00o0OO = re . sub ( "http://.+?/" , "http://m3.mytvnet.vn/" , I11i1 [ 'data' ] [ 'url' ] )
 return O0OO00o0OO
 if 28 - 28: i1 * I11iIi1I - Oo0ooO0oo0oO * I1 * O0o / IiiIII111iI
def ii1IOooO0 ( vstv ) :
 O0o0Oo = urllib2 . Request ( urllib . unquote_plus ( "http://truelife.vn/offica/resourcesubcription/action?_f=6666&c=%s&q=high&type=tv" ) % ( vstv ) )
 O0o0Oo . add_header ( 'Host' , 'truelife.vn' )
 O0o0Oo . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0o0Oo . add_header ( 'Cookie' , 'ojid="dspsns19Lgzd0JHP2kJt|qI9iwnktcCR7lIlfhJM8vYlsqnyhQ7Xlmh2Mfm0jf4cm0ly8DMtoNkb4LIJysPDFP0/cuXcCXjTYxsofpWHjNJFo6hcah5xggY/g4xS7Avl24d4WcPzYgzRd79ETkW2RrzizZBjeNk7hihYpWYbyc/z2Q1jL/Q6kpw0u92OERt0BaxPHC8j|vYqOE2Pnd/h2DdkurOJPoJEi4Ia9KiV3Qs="' )
 O0o0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53' )
 Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
 O0OO00o0OO = Oo00OOOOO . read ( )
 Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) )
 O0OO00o0OO = O0OO00o0OO . replace ( "null(" , "" )
 O0OO00o0OO = O0OO00o0OO . replace ( ")" , "" )
 I11i1 = json . loads ( O0OO00o0OO )
 OooO0OoOOOO = I11i1 [ "object" ] [ 0 ] [ "token" ]
 i1Ii = I11i1 [ "object" ] [ 0 ] [ "time" ]
 if 78 - 78: Oo0oO0ooo
 O0OO00o0OO = 'http://m3.mytvnet.vn/ilive.m3u8?c=' + vstv + '&q=high&token=' + OooO0OoOOOO + '&time=' + i1Ii
 return O0OO00o0OO
 if 71 - 71: o00 + IiIi1Iii1I1 % i11iIiiIii + I1i1iI1i - I1
def oO0OOoO0 ( url ) :
 O0OO00o0OO = ""
 if os . path . exists ( url ) == True :
  O0OO00o0OO = open ( url ) . read ( )
 else :
  O0o0Oo = urllib2 . Request ( url )
  O0o0Oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  Oo00OOOOO = urllib2 . urlopen ( O0o0Oo )
  O0OO00o0OO = Oo00OOOOO . read ( )
  Oo00OOOOO . close ( )
 O0OO00o0OO = '' . join ( O0OO00o0OO . splitlines ( ) ) . replace ( '\'' , '"' )
 O0OO00o0OO = O0OO00o0OO . replace ( '\n' , '' )
 O0OO00o0OO = O0OO00o0OO . replace ( '\t' , '' )
 O0OO00o0OO = re . sub ( '  +' , ' ' , O0OO00o0OO )
 O0OO00o0OO = O0OO00o0OO . replace ( '> <' , '><' )
 return O0OO00o0OO
 if 34 - 34: I1 - I1 * OOooOOo + O0o % I1
def oOoO ( k , e ) :
 i111IiI1I = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O0 in range ( len ( e ) ) :
  iII = k [ O0 % len ( k ) ]
  o0ooOooo000oOO = chr ( ( 256 + ord ( e [ O0 ] ) - ord ( iII ) ) % 256 )
  i111IiI1I . append ( o0ooOooo000oOO )
 return "" . join ( i111IiI1I )
 if 59 - 59: ii1IiI1i + o0 * o0OO0 + i1
def oOo0oooo00o ( name , channelid , mode , starttime , duration ) :
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode ) + "&starttime=" + urllib . quote_plus ( starttime ) + "&duration=" + str ( duration )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = '' )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO )
 return OOO00O
 if 98 - 98: i1iIIII * i1iIIII / i1iIIII + Oo0oO0ooo
def Oo ( name , channelid , channelimg , mode ) :
 Oo0OoO00oOO0o = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode )
 OOO00O = True
 OOoOO0oo0ooO = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = channelimg )
 OOoOO0oo0ooO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO00O = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = Oo0OoO00oOO0o , listitem = OOoOO0oo0ooO , isFolder = True )
 return OOO00O
 if 34 - 34: IiIi1Iii1I1
def I1111I1iII11 ( parameters ) :
 Oooo0O0oo00oO = { }
 if 14 - 14: o0OO0 / I1 . o0OO0 . Oo0oO0ooo % IiiIII111iI * Oo0oO0ooo
 if parameters :
  iIIoO00o0 = parameters [ 1 : ] . split ( "&" )
  for OOoo0O in iIIoO00o0 :
   Oo0ooOo0o = OOoo0O . split ( '=' )
   if ( len ( Oo0ooOo0o ) ) == 2 :
    Oooo0O0oo00oO [ Oo0ooOo0o [ 0 ] ] = Oo0ooOo0o [ 1 ]
 return Oooo0O0oo00oO
 if 22 - 22: ii1I / i11iIiiIii * ii1I * ii1IiI1i . o00 / i11iIiiIii
Iiii = I1111I1iII11 ( sys . argv [ 2 ] )
OO0OoO0o00 = Iiii . get ( 'mode' )
ooOO0O0ooOooO = Iiii . get ( 'channelid' )
oOOOo00O00oOo = Iiii . get ( 'name' )
iiIIIi = Iiii . get ( 'starttime' )
ooo00OOOooO = Iiii . get ( 'duration' )
if 67 - 67: Oo0oO0ooo * o00ooo0 * I1i1iI1i + o00 / i1
if type ( iiIIIi ) == type ( str ( ) ) :
 iiIIIi = urllib . unquote_plus ( iiIIIi )
if type ( ooOO0O0ooOooO ) == type ( str ( ) ) :
 ooOO0O0ooOooO = urllib . unquote_plus ( ooOO0O0ooOooO )
if type ( oOOOo00O00oOo ) == type ( str ( ) ) :
 oOOOo00O00oOo = urllib . unquote_plus ( oOOOo00O00oOo )
 if 11 - 11: O0o + i1iIIII - IiIi1Iii1I1 * o00ooo0 % i11iIiiIii - I1Ii
o0oO = str ( sys . argv [ 1 ] )
if OO0OoO0o00 == 'channelprogram' :
 o0oOoO00o ( ooOO0O0ooOooO )
elif OO0OoO0o00 == 'playvideo' :
 IIiIi1iI = xbmcgui . DialogProgress ( )
 IIiIi1iI . create ( 'megafun.vn' , 'Loading video. Please wait...' )
 O00OooO0 ( ooOO0O0ooOooO , iiIIIi , ooo00OOOooO )
 IIiIi1iI . close ( )
 del IIiIi1iI
else :
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( o0oO ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
