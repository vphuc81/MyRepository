#!/usr/bin/python
#coding=utf-8
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon , actions
import requests , re , urllib , os , zipfile , json , uuid , shutil , pickle , contextlib , base64 , httplib2
oo000 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
ii = xbmc . translatePath ( os . path . join ( oo000 , ".cache" ) )
oOOo = httplib2 . Http ( ii , disable_ssl_certificate_validation = True )
O0 = Plugin ( )
o0O = xbmcaddon . Addon ( "plugin.video.kodi4vn.launcher" )
iI11I1II1I1I = "plugin://plugin.video.kodi4vn.launcher"
oooo = "http://echipstore.com:8000"
if 11 - 11: ii1I - ooO0OO000o
def ii11i ( url ) :
 oOooOoO0Oo0O , iI1 = oOOo . request ( url , "GET" , headers = { 'Cache-Control' : 'public, must-revalidate, max-age=300' } )
 if 43 - 43: I11i11Ii
 oO00oOo = json . loads ( iI1 )
 return oO00oOo
 if 92 - 92: O0O / oo000i1iIi11iIIi1 % Iii1IIIiiI + iI - Oo / o0OIiiIII111iI
def IiII ( url ) :
 oO00oOo = ii11i ( url )
 return oO00oOo
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as oooO0oo0oOOOO :
  for O0oO in oooO0oo0oOOOO . infolist ( ) :
   o0oO0 = O0oO . filename . split ( '/' )
   oo000 = dest_dir
   for oo00 in o0oO0 [ : - 1 ] :
    o00 , oo00 = os . path . splitdrive ( oo00 )
    Oo0oO0ooo , oo00 = os . path . split ( oo00 )
    if oo00 in ( os . curdir , os . pardir , '' ) : continue
    oo000 = os . path . join ( oo000 , oo00 )
   oooO0oo0oOOOO . extract ( O0oO , oo000 )
   if 56 - 56: ooO00oOoo - O0OOo
@ O0 . route ( '/warning/<s>' )
def II1Iiii1111i ( s = "" ) :
 i1IIi11111i ( "Warning" , '/warning/%s' % s )
 o000o0o00o0Oo = xbmcgui . Dialog ( )
 o000o0o00o0Oo . ok ( 'Chú ý: User %s' % O0 . get_setting ( "email" ) , s )
 return O0 . finish ( )
 if 80 - 80: i1iII1I1i1i1 . i1iIIII
@ O0 . route ( '/search/' )
def I1 ( ) :
 i1IIi11111i ( "Browse" , '/search' )
 O0OoOoo00o = O0 . keyboard ( heading = 'Tìm kiếm' )
 if O0OoOoo00o :
  with open ( iiiI11 , "a" ) as OOooO :
   OOooO . write ( O0OoOoo00o + "\n" )
  OOoO00o = '%s/yts/none/video/%s/' % ( iI11I1II1I1I , urllib . quote_plus ( O0OoOoo00o ) )
  II111iiii = O0 . get_storage ( 'search_history' )
  if 'keywords' in II111iiii :
   II111iiii [ "keywords" ] = [ O0OoOoo00o ] + II111iiii [ "keywords" ]
  else :
   II111iiii [ "keywords" ] = [ O0OoOoo00o ]
  O0 . redirect ( OOoO00o )
  if 48 - 48: I1Ii . IiIi1Iii1I1 - O0O0O0O00OooO % Ooooo % i1iIIIiI1I - i1iII1I1i1i1
@ O0 . route ( '/remove-search/' , name = "remove_all" )
@ O0 . route ( '/remove-search/<item>' )
def OoO000 ( item = "" ) :
 if item is not "" :
  II111iiii = ""
  if os . path . exists ( iiiI11 ) :
   with open ( iiiI11 , "r" ) as OOooO :
    II111iiii = OOooO . read ( ) . replace ( item + "\n" , "" )
   with open ( iiiI11 , "w" ) as OOooO :
    OOooO . write ( II111iiii )
 else :
  if os . path . exists ( iiiI11 ) :
   os . remove ( iiiI11 )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 42 - 42: O0OOo - oo000i1iIi11iIIi1 / ii1I + i1iII1I1i1i1 + o0OIiiIII111iI
def iIi ( item = "" ) :
 if item == "" :
  II = '[COLOR yellow]Xóa hết lịch sử tìm kiếm[/COLOR]'
 else :
  II = '[COLOR yellow]Xóa "%s"[/COLOR]' % item
  if 14 - 14: Oo . iI / I1Ii
 return ( II , actions . background (
 "%s/remove-search/%s" % ( iI11I1II1I1I , item )
 ) )
 if 38 - 38: Iii1IIIiiI % ii1I . i1iIIIiI1I - i1iII1I1i1i1 + I1Ii
@ O0 . route ( '/searchlist/' )
def Ooooo0Oo00oO0 ( ) :
 i1IIi11111i ( "Browse" , '/searchlist' )
 oO00oOo = [ ]
 Iiii11I1i1Ii1 = [ {
 "context_menu" : [
 iIi ( "" ) ,
 ] ,
 "label" : "[B]Search[/B]" ,
 "path" : "%s/search" % ( iI11I1II1I1I ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
 II111iiii = [ ]
 if os . path . exists ( iiiI11 ) :
  with open ( iiiI11 , "r" ) as OOooO :
   II111iiii = OOooO . read ( ) . strip ( ) . split ( "\n" )
  for O00 in reversed ( II111iiii ) :
   iII11i = [ {
 "context_menu" : [
 iIi ( O00 ) ,
 ] ,
 "label" : O00 ,
 "path" : '%s/yts/none/video/%s/' % ( iI11I1II1I1I , urllib . quote_plus ( O00 ) ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
   oO00oOo += iII11i
 oO00oOo = Iiii11I1i1Ii1 + oO00oOo
 return O0 . finish ( oO00oOo )
 if 97 - 97: i1iIIII % i1iIIII + Iii1IIIiiI * IiIi1Iii1I1
@ O0 . route ( '/login' )
def o0o00o0 ( ) :
 i1IIi11111i ( "Login" , "/login" )
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  iIi1ii1I1 = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  o0 = iIi1ii1I1 [ "message" ] % iIi1ii1I1 [ "user_code" ] . upper ( )
  I11II1i = xbmcgui . DialogProgress ( )
  I11II1i . create ( 'Login' , o0 )
  if 23 - 23: ooO00oOoo / iiI1i1 + i1iIIII + i1iIIII / Iii1IIIiiI
  iiI1 = 0
  while iiI1 < 60 :
   i11Iiii = int ( ( iiI1 / 60.0 ) * 100 )
   if I11II1i . iscanceled ( ) :
    break
   I11II1i . update ( i11Iiii , "" )
   iiI1 = iiI1 + 1
   xbmc . sleep ( 5000 )
   iII1i1I1II = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( iIi1ii1I1 [ "device_code" ] ) )
   if "token" in iII1i1I1II . text :
    o0O . setSetting ( "token" , iII1i1I1II . json ( ) [ "token" ] )
    o0O . setSetting ( "email" , iII1i1I1II . json ( ) [ "email" ] )
    break
  I11II1i . close ( )
  del I11II1i
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % iI11I1II1I1I )
 except :
  i1 = xbmcgui . Dialog ( )
  i1 . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 48 - 48: ooO0OO000o + ooO0OO000o - ooO00oOoo . i1iIIIiI1I / I11i11Ii
@ O0 . route ( '/' )
def OoOOO00oOO0 ( ) :
 dir ( "0" )
 if 95 - 95: i1iII1I1i1i1 / O0O
@ O0 . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ O0 . route ( '/ytslive/<order>/<page>' )
def iIo00O ( order = "viewcount" , page = "" ) :
 i1IIi11111i ( "Browse YT Live News" , "/ytslive/%s/%s" % ( order , page ) )
 oO00oOo = IiII ( "%s/ytslive/%s/%s" % ( oooo , order , page ) )
 for iII11i in oO00oOo :
  iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 69 - 69: O0OOo % Ooooo - iiI1i1 + Ooooo - ooO0OO000o % O0O
@ O0 . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ O0 . route ( '/yts/<order>/<t>/<q>/<page>' )
def Iii111II ( order , t , q = "" , page = "" ) :
 q = urllib . quote_plus ( q )
 i1IIi11111i ( "Browse YT by topics %s" % q , "/yts/%s/%s/%s/%s" % ( order , t , q , page ) )
 oO00oOo = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 oO00oOo = IiII ( "%s/yts/%s/%s?q=%s&page=%s" % ( oooo , order , t , q , page ) )
 for iII11i in oO00oOo :
  if "plugin://" not in iII11i [ "path" ] :
   iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
 if t == "video" :
  iiii11I = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( iI11I1II1I1I , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  Ooo0OO0oOO = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( iI11I1II1I1I , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  oO00oOo = iiii11I + Ooo0OO0oOO + oO00oOo
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 50 - 50: iI
@ O0 . route ( '/dir/<url>' )
@ O0 . route ( '/dir/<url>/<title>' )
def dir ( url , title = "" ) :
 oO00oOo = [ ]
 i1IIi11111i ( "Browse Menu [%s]" % title , "/dir/%s/%s" % ( title , url ) )
 try :
  if "://" in url :
   pass
  else :
   oO00oOo = IiII ( "%s/dir/%s" % ( oooo , urllib . quote_plus ( url ) ) )
   for iII11i in oO00oOo :
    if "plugin://" not in iII11i [ "path" ] :
     iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
    elif "plugin://plugin.video.f4mTester" in iII11i [ "path" ] :
     iII11i [ "path" ] = iI11I1II1I1I + "/execbuiltin/" + urllib . quote_plus ( iII11i [ "path" ] )
     if 34 - 34: iI * Iii1IIIiiI % IiIi1Iii1I1 * Ii11111i - iI
     if 33 - 33: iiI1i1 + i1iII1I1i1i1 * o0OIiiIII111iI - Oo / O0OOo % I1Ii
     if 21 - 21: o0OIiiIII111iI * I11i11Ii % O0OOo * oo000i1iIi11iIIi1
     if 16 - 16: ooO0OO000o - Ooooo * I11i11Ii + IiIi1Iii1I1
     if 50 - 50: Iii1IIIiiI - i1iIIIiI1I * ooO00oOoo / Ooooo + iiI1i1
     if 88 - 88: I1Ii / Ooooo + IiIi1Iii1I1 - Iii1IIIiiI / i1iIIIiI1I - Ii11111i
     if 15 - 15: ooO00oOoo + Ii11111i - O0O / i1iII1I1i1i1
     if 58 - 58: ii1I % i1iIIII
     if 71 - 71: i1iII1I1i1i1 + i1iIIIiI1I % ii1I + ooO00oOoo - O0O0O0O00OooO
     if 88 - 88: Ii11111i - o0OIiiIII111iI % i1iII1I1i1i1
     if 16 - 16: iI * O0OOo % O0O0O0O00OooO
     if 86 - 86: iI + I1Ii % ii1I * O0OOo . i1iIIIiI1I * i1iIIII
 except :
  oo000 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  i1I11i1iI = xbmc . translatePath ( os . path . join ( oo000 , "error_icon.jpg" ) )
  I1ii1Ii1 = xbmc . translatePath ( os . path . join ( oo000 , "error_bg.jpg" ) )
  iii11 = xbmc . translatePath ( os . path . join ( oo000 , "error_fullscreen.jpg" ) )
  if 68 - 68: o0OIiiIII111iI
  IIi1iIIiI = [ {
 "label" : "Connection Error! OK Here for more details" ,
 "path" : "%s/showimage/%s" % ( iI11I1II1I1I , urllib . quote_plus ( iii11 ) ) ,
 "thumbnail" : i1I11i1iI ,
 "properties" : { 'fanart_image' : I1ii1Ii1 }
 } ]
  oO00oOo += IIi1iIIiI
 return O0 . finish ( oO00oOo )
 if 58 - 58: i1iIIIiI1I / Iii1IIIiiI - i1iII1I1i1i1 - ii1I % Ii11111i - Ooooo
@ O0 . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ O0 . route ( '/ytp/<pid>/<page>' )
def IIII11I1I ( pid , page = "" ) :
 OOO0o = ""
 if " - " in pid :
  IiI1 = pid . split ( " - " )
  OOO0o = " - " . join ( IiI1 [ 1 : ] )
  pid = IiI1 [ 0 ]
  if 54 - 54: Iii1IIIiiI % Ii11111i % i1iIIII % I11i11Ii + I11i11Ii * i1iIIIiI1I
 i1IIi11111i ( "Browse YT Videos by Playlist [%s]" % OOO0o , "/ytp/%s/%s/%s" % ( OOO0o , pid , page ) )
 oO00oOo = IiII ( "%s/ytp/%s/%s" % ( oooo , pid , page ) )
 for iII11i in oO00oOo :
  iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
  O00O0oOO00O00 ( iII11i )
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 11 - 11: O0O0O0O00OooO . ooO00oOoo
@ O0 . route ( '/ytu/<uid>' )
def o0oo0oOo ( uid ) :
 o000O0o = requests . get ( "%s/ytu/%s" % ( oooo , uid ) ) . text
 iI1iII1 ( o000O0o + " - " + uid , "" )
 if 86 - 86: i1iII1I1i1i1
@ O0 . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ O0 . route ( '/ytc/<cid>/<page>' )
def iI1iII1 ( cid , page = "" ) :
 OOO0o = ""
 if " - " in cid :
  OOoo0O = cid . split ( " - " )
  OOO0o = " - " . join ( OOoo0O [ 1 : ] )
  cid = OOoo0O [ 0 ]
  if 67 - 67: ii1I - oo000i1iIi11iIIi1 % ooO00oOoo . ooO0OO000o
 i1IIi11111i ( "Browse YT Videos by Channel [%s]" % OOO0o , "/ytc/%s/%s/%s" % ( OOO0o , cid , page ) )
 oO00oOo = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( iI11I1II1I1I , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( oooo , cid ) ) . text
 if "@" in cid :
  iiii11I = IiII ( "%s/ytp/%s/%s" % ( oooo , cid . split ( "@" ) [ 1 ] , page ) )
  for iII11i in iiii11I :
   iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
   O00O0oOO00O00 ( iII11i )
  oO00oOo += iiii11I
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 77 - 77: O0O0O0O00OooO / iI
@ O0 . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ O0 . route ( '/ytcp/<cid>/<page>' )
def I1iiIii ( cid , page = "" ) :
 OOO0o = ""
 if " - " in cid :
  OOoo0O = cid . split ( " - " )
  OOO0o = " - " . join ( OOoo0O [ 1 : ] )
  cid = OOoo0O [ 0 ]
  if 79 - 79: O0O / ooO0OO000o
 i1IIi11111i ( "Browse YT Playlist by Channel [%s]" % OOO0o , "/ytcp/%s/%s/%s" % ( OOO0o , cid , page ) )
 oO00oOo = IiII ( "%s/ytcp/%s/%s" % ( oooo , cid , page ) )
 for iII11i in oO00oOo :
  iII11i [ "path" ] = iI11I1II1I1I + iII11i [ "path" ]
  O00O0oOO00O00 ( iII11i )
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 75 - 75: Ii11111i % iiI1i1 % iiI1i1 . Ooooo
@ O0 . route ( '/play/<url>' )
@ O0 . route ( '/play/<url>/<title>' )
def III1iII1I1ii ( url , title = "" ) :
 i1IIi11111i ( "Play [%s]" % title , "/play/%s/%s" % ( title , url ) )
 O0 . set_resolved_url ( oOOo0 ( url ) , subtitles = "https://raw.githubusercontent.com/vinhcomp/xml/master/xml/sub1.tsv" )
 if 54 - 54: ooO0OO000o - O0O0O0O00OooO % i1iII1I1i1i1
def oOOo0 ( url ) :
 if "youtube" in url :
  OOoO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  iII = OOoO [ 0 ] [ len ( OOoO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/play/?video_id=%s' % iII
 elif "://" not in url :
  if url . startswith ( "uno-" ) :
   ii1ii11IIIiiI = url . strip ( ) . replace ( "uno-" , "" )
   O00OOOoOoo0O = "NTg4N2RkZmZjMzEyYmYxMDk0ZGU0YmQ1" . decode ( "base64" )
   O000OOo00oo = {
 "Content-Type" : "application/x-www-form-urlencoded" ,
 "User-Agent" : "Dalvik/2.1.0" ,
 "Accept-Encoding" : "gzip"
 }
   oo0OOo = {
 "serial_id" : O00OOOoOoo0O ,
 "query" : ii1ii11IIIiiI
 }
   ooOOO00Ooo = requests . post (
 "http://stbapi.v247tv.com/api/stb_channel2" ,
 headers = O000OOo00oo ,
 data = oo0OOo
 ) . json ( ) [ "data" ]
   oOooOoO0Oo0O = requests . get ( "http://echipstore.com:8000/uno/" + urllib . quote_plus ( ooOOO00Ooo ) )
   IiIIIi1iIi = re . compile ( "(\{.+?\})" ) . findall ( oOooOoO0Oo0O . text . strip ( ) ) [ 0 ]
   return json . loads ( IiIIIi1iIi ) [ "url" ]
  else :
   ooOOoooooo = requests . get ( "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRDaGFubmVsc0FwcEJveC5waHA=" . decode ( "base64" ) ) . json ( )
   for II1I in ooOOoooooo [ "channels" ] :
    if II1I [ "channel_url" ] == url :
     O0i1II1Iiii1I11 = "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRTdHJlYW1pbmdTZXJ2ZXIucGhw" . decode ( "base64" )
     ooOOO00Ooo = { 'strname' : '%s-' % II1I [ "channel_id" ] }
     return requests . post ( O0i1II1Iiii1I11 , data = ooOOO00Ooo ) . text . strip ( )
 else :
  return url
  if 9 - 9: ooO00oOoo / Oo - iI / O0O / I11i11Ii - iiI1i1
@ O0 . route ( '/execbuiltin/<url>' )
def o00oooO0Oo ( url ) :
 xbmc . executebuiltin ( 'XBMC.RunPlugin(%s)' % urllib . unquote_plus ( url ) )
 if 78 - 78: I1Ii % Ooooo + ooO00oOoo
@ O0 . route ( '/showimage/<url>' )
def OOooOoooOoOo ( url ) :
 oo000 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 o0OOOO00O0Oo = xbmc . translatePath ( os . path . join ( oo000 , "tmp" ) )
 if os . path . exists ( o0OOOO00O0Oo ) :
  shutil . rmtree ( o0OOOO00O0Oo )
 os . makedirs ( o0OOOO00O0Oo )
 if ".zip" in url :
  iioOooOOOoOo = xbmc . translatePath ( os . path . join ( o0OOOO00O0Oo , "temp.zip" ) )
  urllib . urlretrieve ( url , iioOooOOOoOo )
  i1I1ii1II1iII ( iioOooOOOoOo , o0OOOO00O0Oo )
  xbmc . executebuiltin ( "SlideShow(%s,recursive)" % o0OOOO00O0Oo )
  if 41 - 41: I1Ii - ooO0OO000o - ooO0OO000o
  if 68 - 68: i1iII1I1i1i1 % Ooooo
 else :
  ooO00OO0 = xbmcgui . WindowDialog ( )
  i11111IIIII = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , url )
  ooO00OO0 . addControl ( i11111IIIII )
  ooO00OO0 . doModal ( )
  if 19 - 19: Ii11111i * oo000i1iIi11iIIi1
def i1IIi11111i ( title = "Home" , page = "/" ) :
 try :
  ii111iI1iIi1 = "http://www.google-analytics.com/collect"
  OOO = open ( oo0OOo0 ) . read ( )
  I11IiI = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : OOO ,
 't' : 'pageview' ,
 'dp' : "Kodi4VNLauncher%s" % page ,
 'dt' : "[Kodi4VNLauncher] - %s" % title
 }
  requests . post ( ii111iI1iIi1 , data = urllib . urlencode ( I11IiI ) )
 except :
  pass
  if 53 - 53: IiIi1Iii1I1 % Iii1IIIiiI . O0O0O0O00OooO - I11i11Ii - O0O0O0O00OooO * Iii1IIIiiI
def O00O0oOO00O00 ( item ) :
 ooO0oOOooOo0 = "/" if item [ "path" ] [ - 1 ] != "/" else ""
 i1I1ii11i1Iii = re . compile ( '/dir/\d+/*$' ) . findall ( item [ "path" ] )
 I1IiiiiI = [ "/ytc/" , "/ytcp/" , "ytp" ]
 if len ( i1I1ii11i1Iii ) > 0 or 'launcher/play/' in item [ "path" ] :
  item [ "path" ] += ooO0oOOooOo0 + urllib . quote_plus ( item [ "label" ] . encode ( "utf8" ) )
 elif any ( word in item [ "path" ] for word in I1IiiiiI ) :
  oo000 = urllib . unquote_plus ( item [ "path" ] )
  if " - " not in oo000 :
   o0OIiII = re . compile ( '/yt[c,p]p?/(.+?)/?$' ) . findall ( oo000 ) [ 0 ] . split ( "/" ) [ 0 ]
   ii1iII1II = "%s - %s" % ( o0OIiII , item [ "label" ] )
   Iii1I1I11iiI1 = urllib . quote_plus ( o0OIiII )
   I1I1i1I = urllib . quote_plus ( ii1iII1II . encode ( "utf8" ) )
   item [ "path" ] = item [ "path" ] . replace ( Iii1I1I11iiI1 , I1I1i1I )
   if 30 - 30: O0O
I1Ii1iI1 = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( I1Ii1iI1 ) == False :
 os . mkdir ( I1Ii1iI1 )
oo0OOo0 = os . path . join ( I1Ii1iI1 , 'cid' )
iiiI11 = os . path . join ( I1Ii1iI1 , 'search.p' )
if 87 - 87: Oo . O0O0O0O00OooO
if os . path . exists ( oo0OOo0 ) == False :
 with open ( oo0OOo0 , "w" ) as OOooO :
  OOooO . write ( str ( uuid . uuid1 ( ) ) )
  if 75 - 75: i1iIIIiI1I + Ii11111i + iiI1i1 * i1iIIII % O0OOo . IiIi1Iii1I1
if __name__ == '__main__' :
 O0 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
