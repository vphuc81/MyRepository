#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , random , base64 , json , time , datetime
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.megafun'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = ""
 oOooOoO0Oo0O = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  sys = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in sys for b in oOooOoO0Oo0O ) : break
 while True :
  iI1 = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in iI1 for b in oOooOoO0Oo0O ) : break
 try :
  ii11i = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   ii11i = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , ii11i . lower ( ) ) : break
 i1I11i = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( ii11i , "11" , sys , iI1 ) ) . read ( )
 if "allowed" in i1I11i :
  OoOoOO00 = I11i ( )
  for O0O in OoOoOO00 [ 'object' ] :
   if ( O0O [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( ) not in [ 'True Sport' , 'QTV1' , 'QTV3' ] ) :
    Oo = 'http://c2.cdn.truelife.vn/offica/community/avatar?c=%s&m=1' % O0O [ 'ownerId' ]
    I1ii11iIi11i = '[B][COLOR green]%s[/COLOR][/B] - ' % O0O [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( )
    I1IiI = ''
    o0OOO = '[B]Đang chiếu[/B]'
    if O0O [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I1IiI = '[B]%s[/B]: ' % O0O [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
    if O0O [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : o0OOO = '[COLOR yellow]%s[/COLOR]' % O0O [ 'title' ] . encode ( 'utf-8' ) . strip ( )
    iIiiiI ( I1ii11iIi11i + I1IiI + o0OOO , O0O [ 'ownerId' ] , Oo , 'channelprogram' )
 else :
  OoOoOO00 = I11i ( )
  for O0O in OoOoOO00 [ 'object' ] :
   if ( O0O [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( ) not in [ 'True Sport' , 'QTV1' , 'QTV3' ] ) :
    Oo = 'http://c2.cdn.truelife.vn/offica/community/avatar?c=%s&m=1' % O0O [ 'ownerId' ]
    I1ii11iIi11i = '[B][COLOR green]%s[/COLOR][/B] - ' % O0O [ 'owner' ] [ 'name' ] . encode ( 'utf-8' ) . strip ( )
    I1IiI = ''
    o0OOO = '[B]Đang chiếu[/B]'
    if O0O [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I1IiI = '[B]%s[/B]: ' % O0O [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
    if O0O [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : o0OOO = '[COLOR yellow]%s[/COLOR]' % O0O [ 'title' ] . encode ( 'utf-8' ) . strip ( )
    iIiiiI ( I1ii11iIi11i + I1IiI + o0OOO , O0O [ 'ownerId' ] , Oo , 'channelprogram' )
  if 10 - 10: I1iII1iiII + I1Ii111 / OOo
 i1i1II = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 i1i1II = xbmc . translatePath ( os . path . join ( i1i1II , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/megafun.jpg' , i1i1II )
 O0oo0OO0 = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , i1i1II )
 I1i1iiI1 = xbmcgui . WindowDialog ( )
 I1i1iiI1 . addControl ( O0oo0OO0 )
 I1i1iiI1 . doModal ( )'''
 if 24 - 24: oOOOO0o0o
def Ii1iI ( channelid ) :
 OoI1Ii11I1Ii1i = Ooo ( channelid )
 o0oOoO00o = i1 ( )
 oOOoo00O0O = datetime . datetime . fromtimestamp ( o0oOoO00o ) . strftime ( '%Y-%m-%d %H:%M:%S' )
 i1111 ( '[B]%s: Đang chiếu...[/B]' % ( oOOoo00O0O ) , channelid , 'playvideo' , '' , '' )
 if 22 - 22: OOo000 . O0
 for I11i1i11i1I in reversed ( OoI1Ii11I1Ii1i [ 'object' ] ) :
  Iiii = I11i1i11i1I [ 'dateTimeBegin' ] . split ( '.' ) [ 0 ]
  OOO0O = time . mktime ( time . strptime ( Iiii , '%Y-%m-%d %H:%M:%S' ) )
  if OOO0O < o0oOoO00o :
   oo0ooO0oOOOOo = '[B]%s[/B]: ' % I11i1i11i1I [ 'dateTimeBegin' ] . encode ( 'utf-8' ) . strip ( ) . split ( '.' ) [ 0 ]
   I1IiI = ''
   oO000OoOoo00o = '[B]Đang chiếu[/B]'
   if I11i1i11i1I [ 'categoryName' ] . encode ( 'utf-8' ) != 'Khác' : I1IiI = '[COLOR yellow]%s[/COLOR]: ' % I11i1i11i1I [ 'categoryName' ] . encode ( 'utf-8' ) . strip ( )
   if I11i1i11i1I [ 'title' ] . encode ( 'utf-8' ) != 'Không rõ' : oO000OoOoo00o = '[B]%s[/B]' % I11i1i11i1I [ 'title' ] . encode ( 'utf-8' ) . strip ( )
   i1111 ( oo0ooO0oOOOOo + I1IiI + oO000OoOoo00o , channelid , 'playvideo' , I11i1i11i1I [ 'dateTimeBegin' ] , str ( I11i1i11i1I [ 'duration' ] ) )
   if 31 - 31: i111IiI + iIIIiI11 . iII111ii
def i1iIIi1 ( channelid , starttime , duration ) :
 ii11iIi1I = iI111I11I1I1 ( channelid )
 OOooO0OOoo = ii11iIi1I [ 'object' ] [ 0 ] [ 'streamingUrl' ] . split ( '&' ) [ 0 ] . replace ( 'c=' , '' )
 OOooO0OOoo = OOooO0OOoo . replace ( 'vstv018' , 'vstv093' )
 if starttime != '' or duration != '' :
  OOO0O = time . mktime ( time . strptime ( starttime . split ( '.' ) [ 0 ] , '%Y-%m-%d %H:%M:%S' ) )
  if 29 - 29: o00o / IiI1I1
  oo0ooO0oOOOOo = datetime . datetime . fromtimestamp ( OOO0O ) . strftime ( '%H%M' )
  OoO000 = datetime . datetime . fromtimestamp ( OOO0O ) . strftime ( '%y%m%d' )
  IIiiIiI1 = iiIiIIi ( OOooO0OOoo , OoO000 , oo0ooO0oOOOOo )
 else :
  IIiiIiI1 = ooOoo0O ( OOooO0OOoo )
 OooO0 = xbmc . Player ( )
 OooO0 . play ( IIiiIiI1 )
 if 35 - 35: Ooooo0Oo00oO0 % OooO0o0Oo . O00 % iII11i
def i1 ( ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/community/action?_f=7&jsoncallback=Ext.data.JsonP.callback2" )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.callback2(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 I1i1iii = o0oO [ 'header' ] [ 'sysdate' ] . replace ( ' ICT' , '' ) . encode ( 'utf-8' )
 i1iiI11I = time . mktime ( time . strptime ( I1i1iii , '%a %b %d %H:%M:%S %Y' ) )
 return i1iiI11I
 if 29 - 29: iiIi
def iI111I11I1I1 ( channelid ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/truelifetv/lib/action?_f=119&tvChannelId=%s&ownerId=1532&jsoncallback=Ext.data.JsonP.tvprofile" % channelid )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJvDE1HIHREnmHbaJbKVVNyAsEMqwvy162y0dPlCA5mNkifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvprofile(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 98 - 98: I1IIIii % i111IiI * O0 % iiI
def Ooo ( channelid ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=14&communityId=%s&jsoncallback=Ext.data.JsonP.tvshow1205151412" % channelid )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="UryGHmUCni0KfiuwTUS2zetq|QZcIptDEA4Rd4pyY3GUauEPigwgClr3zopggcFFuzcqH90Y3MdEz9BOdNMAeYFL3kHVnrovgSQcEM7wp05s6Ovedh74CQjH6krC9J4Yqiq|DuqGSPeU2gaX9VKCJisQ26UQYnnCkwbck2oeVngMSDmkUKxjgYQoWsu|6GGsifc6O4j0GJgCCLiKGAzj69vma5O2h7XkqLpvQI2vNeA="' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 63 - 63: ii1I
def I11i ( ) :
 O0O00o0OOO0 = urllib2 . Request ( "http://truelife.vn/offica/tvchannel/tvshow/action?_f=17&ownerId=1532&jsoncallback=Ext.data.JsonP.tvshow1205151412" )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Referer' , 'http://megafun.vn/tv/' )
 O0O00o0OOO0 . add_header ( 'DNT' , '1' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'keep-alive' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "Ext.data.JsonP.tvshow1205151412(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 57 - 57: ii1I * OooO0o0Oo
def OOOO ( ) :
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( "http://s22.ctl.vsolutions.vn/ctl/tvlive/s/?script&json" ) )
 O0O00o0OOO0 . add_header ( 'Host' , 's22.ctl.vsolutions.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 return o0oO
 if 87 - 87: o00o / Ooooo0Oo00oO0 - I1Ii111 * IiI1I1 / I1iII1iiII . iiI
def iiIiIIi ( vstv , date , st ) :
 iii11I111 = str ( int ( time . time ( ) ) )
 OOOO00ooo0Ooo = base64 . b64encode ( iii11I111 )
 OOOooOooo00O0 = ""
 for Oo0OO in range ( 1 , 7 ) :
  oOOoOo00o = random . randrange ( 0 , len ( "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" ) )
  OOOooOooo00O0 = OOOooOooo00O0 + "ABCDEFGHIJKLMNOPQRSTUVXYZ1234567890" [ oOOoOo00o : oOOoOo00o + 1 ]
 o0OOoo0OO0OOO = "" ;
 for iI1iI1I1i1I in range ( 0 , len ( OOOO00ooo0Ooo ) ) :
  o0OOoo0OO0OOO = o0OOoo0OO0OOO + OOOO00ooo0Ooo [ iI1iI1I1i1I : iI1iI1I1i1I + 1 ]
  if ( iI1iI1I1i1I < len ( OOOooOooo00O0 ) ) :
   o0OOoo0OO0OOO = o0OOoo0OO0OOO + OOOooOooo00O0 [ iI1iI1I1i1I : iI1iI1I1i1I + 1 ]
 iIi11Ii1 = base64 . b64encode ( o0OOoo0OO0OOO )
 Ii11iII1 = ""
 for Oo0O0O0ooO0O in range ( 0 , len ( iIi11Ii1 ) - 1 ) :
  Ii11iII1 = Ii11iII1 + iIi11Ii1 [ Oo0O0O0ooO0O : Oo0O0O0ooO0O + 1 ]
  if ( Oo0O0O0ooO0O < len ( OOOooOooo00O0 ) ) :
   Ii11iII1 = Ii11iII1 + OOOooOooo00O0 [ Oo0O0O0ooO0O : Oo0O0O0ooO0O + 1 ]
 Ii11iII1 = Ii11iII1 . replace ( "=" , "" )
 IIIIii = { 'location' : '' , 'device_type' : '2' , 'mf_code' : vstv , 'device_id' : '487142' , 'date' : date , 'channel_id' : '1' , 'member_id' : '107805' , 'end_time' : '2359' , 'app_v' : '63' , 'manufacturer_id' : 'E94F6043C85AF86080CA27A439A1D766' , 'start_time' : st , 'tid' : Ii11iII1 , 'profile' : '2' }
 O0o0 = urllib . urlencode ( IIIIii )
 if 71 - 71: IiI1I1 + I1IIIii % i11iIiiIii + iII111ii - iII11i
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( OoO000 ( "u" , "3enp5a-kpOTp6aPi7unr49rpo-vjpOuqpNjd1uPj2uGk4uTX3uHapOnr5Nmi6ufh" ) ) )
 O0O00o0OOO0 . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded; charset=utf-8' )
 O0O00o0OOO0 . add_header ( 'User-Agent' , 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; Nexus 5 Build/KOT49H)' )
 O0O00o0OOO0 . add_header ( 'Host' , 'ott.mytvnet.vn' )
 O0O00o0OOO0 . add_header ( 'Connection' , 'Keep-Alive' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 , O0o0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 if 88 - 88: i111IiI - O0 % IiI1I1
 o0oo0o0O00OO = o0oO [ 'data' ] [ 'url' ]
 return o0oo0o0O00OO
 if 16 - 16: oOOOO0o0o * o00o % iII11i
def ooOoo0O ( vstv ) :
 O0O00o0OOO0 = urllib2 . Request ( urllib . unquote_plus ( "http://truelife.vn/offica/resourcesubcription/action?_f=6666&c=%s&q=high&type=tv" ) % ( vstv ) )
 O0O00o0OOO0 . add_header ( 'Host' , 'truelife.vn' )
 O0O00o0OOO0 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 O0O00o0OOO0 . add_header ( 'Cookie' , 'ojid="dspsns19Lgzd0JHP2kJt|qI9iwnktcCR7lIlfhJM8vYlsqnyhQ7Xlmh2Mfm0jf4cm0ly8DMtoNkb4LIJysPDFP0/cuXcCXjTYxsofpWHjNJFo6hcah5xggY/g4xS7Avl24d4WcPzYgzRd79ETkW2RrzizZBjeNk7hihYpWYbyc/z2Q1jL/Q6kpw0u92OERt0BaxPHC8j|vYqOE2Pnd/h2DdkurOJPoJEi4Ia9KiV3Qs="' )
 O0O00o0OOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPad; CPU OS 7_0_4 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B554a Safari/9537.53' )
 Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
 o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
 Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( "null(" , "" )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( ")" , "" )
 o0oO = json . loads ( o0oo0o0O00OO )
 Oo000o = o0oO [ "object" ] [ 0 ] [ "token" ]
 I11IiI1I11i1i = o0oO [ "object" ] [ 0 ] [ "time" ]
 if 38 - 38: iIIIiI11
 o0oo0o0O00OO = 'http://123.29.68.44/live.m3u8?c=' + vstv + '&q=high&token=' + Oo000o + '&time=' + I11IiI1I11i1i
 return o0oo0o0O00OO
 if 57 - 57: iiI / o00o * iiIi / i111IiI . OOo
def i11iIIIIIi1 ( url ) :
 o0oo0o0O00OO = ""
 if os . path . exists ( url ) == True :
  o0oo0o0O00OO = open ( url ) . read ( )
 else :
  O0O00o0OOO0 = urllib2 . Request ( url )
  O0O00o0OOO0 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  Ii1iIIIi1ii = urllib2 . urlopen ( O0O00o0OOO0 )
  o0oo0o0O00OO = Ii1iIIIi1ii . read ( )
  Ii1iIIIi1ii . close ( )
 o0oo0o0O00OO = '' . join ( o0oo0o0O00OO . splitlines ( ) ) . replace ( '\'' , '"' )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '\n' , '' )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '\t' , '' )
 o0oo0o0O00OO = re . sub ( '  +' , ' ' , o0oo0o0O00OO )
 o0oo0o0O00OO = o0oo0o0O00OO . replace ( '> <' , '><' )
 return o0oo0o0O00OO
 if 20 - 20: I1Ii111 + iII111ii - I1IIIii
def OoO000 ( k , e ) :
 IiI11iII1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for IIII11I1I in range ( len ( e ) ) :
  OOO0o = k [ IIII11I1I % len ( k ) ]
  IiI1 = chr ( ( 256 + ord ( e [ IIII11I1I ] ) - ord ( OOO0o ) ) % 256 )
  IiI11iII1 . append ( IiI1 )
 return "" . join ( IiI11iII1 )
 if 54 - 54: OOo % i111IiI % Ooooo0Oo00oO0 % ii1I + ii1I * I1IIIii
def i1111 ( name , channelid , mode , starttime , duration ) :
 O00O0oOO00O00 = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode ) + "&starttime=" + urllib . quote_plus ( starttime ) + "&duration=" + str ( duration )
 i1Oo00 = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = '' )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1Oo00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00O0oOO00O00 , listitem = i1i )
 return i1Oo00
 if 50 - 50: iII11i
def iIiiiI ( name , channelid , channelimg , mode ) :
 O00O0oOO00O00 = sys . argv [ 0 ] + "?name=" + urllib . quote_plus ( name ) + "&channelid=" + urllib . quote_plus ( str ( channelid ) ) + "&mode=" + str ( mode )
 i1Oo00 = True
 i1i = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = channelimg )
 i1i . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1Oo00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O00O0oOO00O00 , listitem = i1i , isFolder = True )
 return i1Oo00
 if 14 - 14: Ooooo0Oo00oO0 % O0 * Ooooo0Oo00oO0
def iII ( parameters ) :
 oO00o0 = { }
 if 55 - 55: OOo000 + ii1I / i111IiI * o00o - i11iIiiIii - OooO0o0Oo
 if parameters :
  ii1ii1ii = parameters [ 1 : ] . split ( "&" )
  for oooooOoo0ooo in ii1ii1ii :
   I1I1IiI1 = oooooOoo0ooo . split ( '=' )
   if ( len ( I1I1IiI1 ) ) == 2 :
    oO00o0 [ I1I1IiI1 [ 0 ] ] = I1I1IiI1 [ 1 ]
 return oO00o0
 if 5 - 5: iIIIiI11 * I1IIIii + i111IiI . IiI1I1 + i111IiI
oO = iII ( sys . argv [ 2 ] )
iIi1IIIi1 = oO . get ( 'mode' )
O0oOoOOOoOO = oO . get ( 'channelid' )
ii1ii11IIIiiI = oO . get ( 'name' )
O00OOOoOoo0O = oO . get ( 'starttime' )
O000OOo00oo = oO . get ( 'duration' )
if 71 - 71: i11iIiiIii + iII11i
if type ( O00OOOoOoo0O ) == type ( str ( ) ) :
 O00OOOoOoo0O = urllib . unquote_plus ( O00OOOoOoo0O )
if type ( O0oOoOOOoOO ) == type ( str ( ) ) :
 O0oOoOOOoOO = urllib . unquote_plus ( O0oOoOOOoOO )
if type ( ii1ii11IIIiiI ) == type ( str ( ) ) :
 ii1ii11IIIiiI = urllib . unquote_plus ( ii1ii11IIIiiI )
 if 57 - 57: o00o . Ooooo0Oo00oO0 . I1Ii111
i11Iii = str ( sys . argv [ 1 ] )
if iIi1IIIi1 == 'channelprogram' :
 Ii1iI ( O0oOoOOOoOO )
elif iIi1IIIi1 == 'playvideo' :
 IiIIIi1iIi = xbmcgui . DialogProgress ( )
 IiIIIi1iIi . create ( 'megafun.vn' , 'Loading video. Please wait...' )
 i1iIIi1 ( O0oOoOOOoOO , O00OOOoOoo0O , O000OOo00oo )
 IiIIIi1iIi . close ( )
 del IiIIIi1iIi
else :
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( i11Iii ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
