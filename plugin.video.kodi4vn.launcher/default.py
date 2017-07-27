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
  iiiI11 = '%s/yts/none/video/%s/' % ( iI11I1II1I1I , urllib . quote_plus ( O0OoOoo00o ) )
  OOooO = O0 . get_storage ( 'search_history' )
  if 'keywords' in OOooO :
   OOooO [ "keywords" ] = [ O0OoOoo00o ] + OOooO [ "keywords" ]
  else :
   OOooO [ "keywords" ] = [ O0OoOoo00o ]
  O0 . redirect ( iiiI11 )
  if 58 - 58: i11iiII + OooooO0oOO + oOo0 / oo0Ooo0
@ O0 . route ( '/remove-search/' , name = "remove_all" )
@ O0 . route ( '/remove-search/<item>' )
def I1I11I1I1I ( item = "" ) :
 if item is not "" :
  OOooO = O0 . get_storage ( 'search_history' )
  if 'keywords' in OOooO :
   OooO0OO = [ ]
   for iiiIi in OOooO [ "keywords" ] :
    if iiiIi != item :
     OooO0OO += [ iiiIi ]
   OOooO [ "keywords" ] = OooO0OO
 else :
  O0 . get_storage ( 'search_history' ) . clear ( )
 xbmc . executebuiltin ( 'Container.Refresh' )
 if 24 - 24: iIiI1I11 % Oo % Oo . oOo0 % iIiI1I11
def IIiiIiI1 ( item = "" ) :
 if item == "" :
  iiIiIIi = '[COLOR yellow]Xóa hết lịch sử tìm kiếm[/COLOR]'
 else :
  iiIiIIi = '[COLOR yellow]Xóa "%s"[/COLOR]' % item
  if 65 - 65: Ii11111i
 return ( iiIiIIi , actions . background (
 "%s/remove-search/%s" % ( iI11I1II1I1I , item )
 ) )
 if 6 - 6: iI / Oo % i11iiII
@ O0 . route ( '/searchlist/' )
def oo ( ) :
 i1IIi11111i ( "Browse" , '/searchlist' )
 oO00oOo = [ ]
 OO0O00 = [ {
 "context_menu" : [
 IIiiIiI1 ( "" ) ,
 ] ,
 "label" : "[B]Search[/B]" ,
 "path" : "%s/search" % ( iI11I1II1I1I ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
 OOooO = O0 . get_storage ( 'search_history' )
 if 'keywords' in OOooO :
  for iiiIi in OOooO [ 'keywords' ] :
   ii1 = [ {
 "context_menu" : [
 IIiiIiI1 ( iiiIi ) ,
 ] ,
 "label" : iiiIi ,
 "path" : '%s/yts/none/video/%s/' % ( iI11I1II1I1I , urllib . quote_plus ( iiiIi ) ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/jH1IxHp7MbOx62G1aboX2kj1vgtt3kercFVPYTxh7Yr0kMoVZARVNZIYjFZQOY1FzK7DisXyfHo=s256-no"
 } ]
   oO00oOo += ii1
 oO00oOo = OO0O00 + oO00oOo
 return O0 . finish ( oO00oOo )
 if 57 - 57: i11iiII % O0O
@ O0 . route ( '/login' )
def O00 ( ) :
 i1IIi11111i ( "Login" , "/login" )
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  i11I1 = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  Ii11Ii11I = i11I1 [ "message" ] % i11I1 [ "user_code" ] . upper ( )
  iI11i1I1 = xbmcgui . DialogProgress ( )
  iI11i1I1 . create ( 'Login' , Ii11Ii11I )
  if 71 - 71: iIiI1I11 % OooooO0oOO / iiI1i1
  ii11i1iIII = 0
  while ii11i1iIII < 60 :
   Ii1I = int ( ( ii11i1iIII / 60.0 ) * 100 )
   if iI11i1I1 . iscanceled ( ) :
    break
   iI11i1I1 . update ( Ii1I , "" )
   ii11i1iIII = ii11i1iIII + 1
   xbmc . sleep ( 5000 )
   Oo0o0 = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( i11I1 [ "device_code" ] ) )
   if "token" in Oo0o0 . text :
    o0O . setSetting ( "token" , Oo0o0 . json ( ) [ "token" ] )
    o0O . setSetting ( "email" , Oo0o0 . json ( ) [ "email" ] )
    break
  iI11i1I1 . close ( )
  del iI11i1I1
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % iI11I1II1I1I )
 except :
  III1ii1iII = xbmcgui . Dialog ( )
  III1ii1iII . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 54 - 54: iI % Iii1IIIiiI % Iii1IIIiiI
@ O0 . route ( '/' )
def iI1i11Iiii ( ) :
 dir ( "0" )
 if 23 - 23: iiI1i1 . Iii1IIIiiI
@ O0 . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ O0 . route ( '/ytslive/<order>/<page>' )
def Oo0O0OOOoo ( order = "viewcount" , page = "" ) :
 i1IIi11111i ( "Browse YT Live News" , "/ytslive/%s/%s" % ( order , page ) )
 oO00oOo = IiII ( "%s/ytslive/%s/%s" % ( oooo , order , page ) )
 for ii1 in oO00oOo :
  ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 95 - 95: o0OIiiIII111iI % O0OOo . ooO0OO000o
@ O0 . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ O0 . route ( '/yts/<order>/<t>/<q>/<page>' )
def I1i1I ( order , t , q = "" , page = "" ) :
 q = urllib . quote_plus ( q )
 i1IIi11111i ( "Browse YT by topics %s" % q , "/yts/%s/%s/%s/%s" % ( order , t , q , page ) )
 oO00oOo = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 oO00oOo = IiII ( "%s/yts/%s/%s?q=%s&page=%s" % ( oooo , order , t , q , page ) )
 for ii1 in oO00oOo :
  if "plugin://" not in ii1 [ "path" ] :
   ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
 if t == "video" :
  oOO00oOO = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( iI11I1II1I1I , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  OoOo = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( iI11I1II1I1I , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  oO00oOo = oOO00oOO + OoOo + oO00oOo
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 18 - 18: ii1I
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
   for ii1 in oO00oOo :
    if "plugin://" not in ii1 [ "path" ] :
     ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
    elif "plugin://plugin.video.f4mTester" in ii1 [ "path" ] :
     ii1 [ "path" ] = iI11I1II1I1I + "/execbuiltin/" + urllib . quote_plus ( ii1 [ "path" ] )
     if 46 - 46: oo000i1iIi11iIIi1 / i1iIIII % i1iII1I1i1i1 + oo0Ooo0
     if 79 - 79: oo0Ooo0 - iiI1i1 + oo0Ooo0 - OooooO0oOO
     if 8 - 8: iI
     if 75 - 75: I11i11Ii / i1iII1I1i1i1 % iiI1i1 * Ii11111i
     if 9 - 9: o0OIiiIII111iI
   i11 = ( "" if O0 . get_setting ( "email" ) == "" else ( "Chào %s. " % O0 . get_setting ( "email" ) ) )
   O0oo0OO0oOOOo = [ {
 "label" : "[COLOR yellow][B]%sVào đây để Login/Relogin[/B][/COLOR]" % i11 ,
 "path" : iI11I1II1I1I + "/login" ,
 "thumbnail" : "https://cdn3.iconfinder.com/data/icons/gray-toolbar-2/512/login_user_profile_account-512.png"
 } ]
   oO00oOo = oO00oOo + O0oo0OO0oOOOo
 except :
  oo000 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  i1i1i11IIi = xbmc . translatePath ( os . path . join ( oo000 , "error_icon.jpg" ) )
  II1III = xbmc . translatePath ( os . path . join ( oo000 , "error_bg.jpg" ) )
  iI1iI1I1i1I = xbmc . translatePath ( os . path . join ( oo000 , "error_fullscreen.jpg" ) )
  if 24 - 24: ooO00oOoo
  o0Oo0O0Oo00oO = [ {
 "label" : "Connection Error! OK Here for more details" ,
 "path" : "%s/showimage/%s" % ( iI11I1II1I1I , urllib . quote_plus ( iI1iI1I1i1I ) ) ,
 "thumbnail" : i1i1i11IIi ,
 "properties" : { 'fanart_image' : II1III }
 } ]
  oO00oOo += o0Oo0O0Oo00oO
 return O0 . finish ( oO00oOo )
 if 39 - 39: oOo0 - Iii1IIIiiI * o0OIiiIII111iI % iiI1i1 * Iii1IIIiiI % Iii1IIIiiI
@ O0 . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ O0 . route ( '/ytp/<pid>/<page>' )
def OoOOOOO ( pid , page = "" ) :
 iIi1i111II = ""
 if " - " in pid :
  OoOO00O = pid . split ( " - " )
  iIi1i111II = " - " . join ( OoOO00O [ 1 : ] )
  pid = OoOO00O [ 0 ]
  if 53 - 53: o0OIiiIII111iI % O0O - Ii11111i
 i1IIi11111i ( "Browse YT Videos by Playlist [%s]" % iIi1i111II , "/ytp/%s/%s/%s" % ( iIi1i111II , pid , page ) )
 oO00oOo = IiII ( "%s/ytp/%s/%s" % ( oooo , pid , page ) )
 for ii1 in oO00oOo :
  ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
  oO000Oo000 ( ii1 )
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 4 - 4: O0OOo
@ O0 . route ( '/ytu/<uid>' )
def OOoO0O00o0 ( uid ) :
 iII = requests . get ( "%s/ytu/%s" % ( oooo , uid ) ) . text
 o0 ( iII + " - " + uid , "" )
 if 62 - 62: I11i11Ii * Ii11111i
@ O0 . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ O0 . route ( '/ytc/<cid>/<page>' )
def o0 ( cid , page = "" ) :
 iIi1i111II = ""
 if " - " in cid :
  i1 = cid . split ( " - " )
  iIi1i111II = " - " . join ( i1 [ 1 : ] )
  cid = i1 [ 0 ]
  if 91 - 91: o0OIiiIII111iI . ooO00oOoo + o0OIiiIII111iI - OooooO0oOO / O0O
 i1IIi11111i ( "Browse YT Videos by Channel [%s]" % iIi1i111II , "/ytc/%s/%s/%s" % ( iIi1i111II , cid , page ) )
 oO00oOo = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( iI11I1II1I1I , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( oooo , cid ) ) . text
 if "@" in cid :
  oOO00oOO = IiII ( "%s/ytp/%s/%s" % ( oooo , cid . split ( "@" ) [ 1 ] , page ) )
  for ii1 in oOO00oOO :
   ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
   oO000Oo000 ( ii1 )
  oO00oOo += oOO00oOO
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 39 - 39: ooO00oOoo / iIiI1I11 - Iii1IIIiiI
@ O0 . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ O0 . route ( '/ytcp/<cid>/<page>' )
def OO00o ( cid , page = "" ) :
 iIi1i111II = ""
 if " - " in cid :
  i1 = cid . split ( " - " )
  iIi1i111II = " - " . join ( i1 [ 1 : ] )
  cid = i1 [ 0 ]
  if 61 - 61: Iii1IIIiiI * O0OOo % Oo
 i1IIi11111i ( "Browse YT Playlist by Channel [%s]" % iIi1i111II , "/ytcp/%s/%s/%s" % ( iIi1i111II , cid , page ) )
 oO00oOo = IiII ( "%s/ytcp/%s/%s" % ( oooo , cid , page ) )
 for ii1 in oO00oOo :
  ii1 [ "path" ] = iI11I1II1I1I + ii1 [ "path" ]
  oO000Oo000 ( ii1 )
 if O0 . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return O0 . finish ( oO00oOo , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return O0 . finish ( oO00oOo , view_mode = 52 )
  else :
   return O0 . finish ( oO00oOo )
 else :
  return O0 . finish ( oO00oOo )
  if 64 - 64: i1iIIII % OooooO0oOO - oo0Ooo0 - O0OOo
@ O0 . route ( '/play/<url>' )
@ O0 . route ( '/play/<url>/<title>' )
def i1ii1iiI ( url , title = "" ) :
 i1IIi11111i ( "Play [%s]" % title , "/play/%s/%s" % ( title , url ) )
 O0 . set_resolved_url ( O0o0O00Oo0o0 ( url ) , subtitles = "https://raw.githubusercontent.com/vinhcomp/xml/master/xml/sub1.tsv" )
 if 87 - 87: iIiI1I11 * Oo % ii1I % Ii11111i - i1iII1I1i1i1
def O0o0O00Oo0o0 ( url ) :
 if "youtube" in url :
  O0ooo0O0oo0 = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  oo0oOo = O0ooo0O0oo0 [ 0 ] [ len ( O0ooo0O0oo0 [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/play/?video_id=%s' % oo0oOo
 elif "://" not in url :
  if url . startswith ( "uno-" ) :
   o000O0o = url . strip ( ) . replace ( "uno-" , "" )
   iI1iII1 = "NTg4N2RkZmZjMzEyYmYxMDk0ZGU0YmQ1" . decode ( "base64" )
   oO0OOoo0OO = {
 "Content-Type" : "application/x-www-form-urlencoded" ,
 "User-Agent" : "Dalvik/2.1.0" ,
 "Accept-Encoding" : "gzip"
 }
   O0ii1ii1ii = {
 "serial_id" : iI1iII1 ,
 "query" : o000O0o
 }
   oooooOoo0ooo = requests . post (
 "http://stbapi.v247tv.com/api/stb_channel2" ,
 headers = oO0OOoo0OO ,
 data = O0ii1ii1ii
 ) . json ( ) [ "data" ]
   oOooOoO0Oo0O = requests . get ( "http://echipstore.com:8000/uno/" + urllib . quote_plus ( oooooOoo0ooo ) )
   I1I1IiI1 = re . compile ( "(\{.+?\})" ) . findall ( oOooOoO0Oo0O . text . strip ( ) ) [ 0 ]
   return json . loads ( I1I1IiI1 ) [ "url" ]
  else :
   III1iII1I1ii = requests . get ( "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRDaGFubmVsc0FwcEJveC5waHA=" . decode ( "base64" ) ) . json ( )
   for oOOo0 in III1iII1I1ii [ "channels" ] :
    if oOOo0 [ "channel_url" ] == url :
     oo00O00oO = "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRTdHJlYW1pbmdTZXJ2ZXIucGhw" . decode ( "base64" )
     oooooOoo0ooo = { 'strname' : '%s-' % oOOo0 [ "channel_id" ] }
     return requests . post ( oo00O00oO , data = oooooOoo0ooo ) . text . strip ( )
 else :
  return url
  if 23 - 23: o0OIiiIII111iI + o0OIiiIII111iI . i1iII1I1i1i1
@ O0 . route ( '/execbuiltin/<url>' )
def ii1ii11IIIiiI ( url ) :
 xbmc . executebuiltin ( 'XBMC.RunPlugin(%s)' % urllib . unquote_plus ( url ) )
 if 67 - 67: i1iIIII * O0OOo * ooO00oOoo + i1iII1I1i1i1 / oo000i1iIi11iIIi1
@ O0 . route ( '/showimage/<url>' )
def I1I111 ( url ) :
 oo000 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 Oo00oo0oO = xbmc . translatePath ( os . path . join ( oo000 , "tmp" ) )
 if os . path . exists ( Oo00oo0oO ) :
  shutil . rmtree ( Oo00oo0oO )
 os . makedirs ( Oo00oo0oO )
 if ".zip" in url :
  IIiIi1iI = xbmc . translatePath ( os . path . join ( Oo00oo0oO , "temp.zip" ) )
  urllib . urlretrieve ( url , IIiIi1iI )
  i1I1ii1II1iII ( IIiIi1iI , Oo00oo0oO )
  xbmc . executebuiltin ( "SlideShow(%s,recursive)" % Oo00oo0oO )
  if 35 - 35: i11iiII % ooO0OO000o - ooO0OO000o
  if 16 - 16: Iii1IIIiiI % Ii11111i - Iii1IIIiiI + i11iiII
 else :
  i1I1i = xbmcgui . WindowDialog ( )
  Ii = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , url )
  i1I1i . addControl ( Ii )
  i1I1i . doModal ( )
  if 22 - 22: Iii1IIIiiI
def i1IIi11111i ( title = "Home" , page = "/" ) :
 try :
  iiI1I11i1i = "http://www.google-analytics.com/collect"
  III1Iiii1I11 = open ( IIII ) . read ( )
  iiIiI = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : III1Iiii1I11 ,
 't' : 'pageview' ,
 'dp' : "Kodi4VNLauncher%s" % page ,
 'dt' : "[Kodi4VNLauncher] - %s" % title
 }
  requests . post ( iiI1I11i1i , data = urllib . urlencode ( iiIiI ) )
 except :
  pass
  if 91 - 91: OooooO0oOO % oo000i1iIi11iIIi1 % I11i11Ii
def oO000Oo000 ( item ) :
 IIi1I11I1II = "/" if item [ "path" ] [ - 1 ] != "/" else ""
 OooOoooOo = re . compile ( '/dir/\d+/*$' ) . findall ( item [ "path" ] )
 ii11IIII11I = [ "/ytc/" , "/ytcp/" , "ytp" ]
 if len ( OooOoooOo ) > 0 or 'launcher/play/' in item [ "path" ] :
  item [ "path" ] += IIi1I11I1II + urllib . quote_plus ( item [ "label" ] . encode ( "utf8" ) )
 elif any ( word in item [ "path" ] for word in ii11IIII11I ) :
  oo000 = urllib . unquote_plus ( item [ "path" ] )
  if " - " not in oo000 :
   OOooo = re . compile ( '/yt[c,p]p?/(.+?)/?$' ) . findall ( oo000 ) [ 0 ] . split ( "/" ) [ 0 ]
   oOooOOOoOo = "%s - %s" % ( OOooo , item [ "label" ] )
   i1Iii1i1I = urllib . quote_plus ( OOooo )
   OOoO00 = urllib . quote_plus ( oOooOOOoOo . encode ( "utf8" ) )
   item [ "path" ] = item [ "path" ] . replace ( i1Iii1i1I , OOoO00 )
   if 40 - 40: iI * i11iiII + i1iII1I1i1i1 % OooooO0oOO
OOOOOoo0 = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( OOOOOoo0 ) == False :
 os . mkdir ( OOOOOoo0 )
IIII = os . path . join ( OOOOOoo0 , 'cid' )
ii1I1iI1iIi111i = os . path . join ( OOOOOoo0 , 'search.p' )
if 44 - 44: oo000i1iIi11iIIi1 % Iii1IIIiiI + i1iIIII
if os . path . exists ( IIII ) == False :
 with open ( IIII , "w" ) as I1I1I :
  I1I1I . write ( str ( uuid . uuid1 ( ) ) )
  if 95 - 95: Iii1IIIiiI + iiI1i1 + OooooO0oOO * I11i11Ii % O0OOo / oOo0
if __name__ == '__main__' :
 O0 . run ( )
 if 56 - 56: OooooO0oOO
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
