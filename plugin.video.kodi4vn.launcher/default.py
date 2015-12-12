#!/usr/bin/python
#coding=utf-8
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
import requests , re , urllib , shutil , os , zipfile , json
if 64 - 64: i11iIiiIii
OO0o = Plugin ( )
Oo0Ooo = xbmcaddon . Addon ( "plugin.video.kodi4vn.launcher" )
O0O0OO0O0O0 = "plugin://plugin.video.kodi4vn.launcher"
iiiii = "http://echipstore.com:8000"
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( url ) :
 if "youtube" in url :
  i1I11i = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  OoOoOO00 = i1I11i [ 0 ] [ len ( i1I11i [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % OoOoOO00
 elif "://" not in url :
  I11i = "http://www.viettv24.com/main/getStreamingServer.php"
  O0O = { 'strname' : '%s-' % url }
  return requests . post ( I11i , data = O0O ) . text . strip ( )
 else :
  return url
  if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
def iI111iI ( url ) :
 IiII = requests . get ( url + "%st=%s" % ( "&" if "?" in url else "?" , urllib . quote_plus ( OO0o . get_setting ( "token" ) ) ) )
 IiII . encoding = "utf-8"
 iI1Ii11111iIi = IiII . json ( )
 return iI1Ii11111iIi
 if 41 - 41: I1II1
def Ooo0OO0oOO ( url ) :
 iI1Ii11111iIi = iI111iI ( url )
 return iI1Ii11111iIi
 if 86 - 86: oO0o
def IIII ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as Oo0oO0oo0oO00 :
  for i111I in Oo0oO0oo0oO00 . infolist ( ) :
   II1Ii1iI1i = i111I . filename . split ( '/' )
   iiI1iIiI = dest_dir
   for OOo in II1Ii1iI1i [ : - 1 ] :
    Ii1IIii11 , OOo = os . path . splitdrive ( OOo )
    Oooo0000 , OOo = os . path . split ( OOo )
    if OOo in ( os . curdir , os . pardir , '' ) : continue
    iiI1iIiI = os . path . join ( iiI1iIiI , OOo )
   Oo0oO0oo0oO00 . extract ( i111I , iiI1iIiI )
   if 22 - 22: OOo000 . O0
@ OO0o . route ( '/warning/<s>' )
def I11i1i11i1I ( s = "" ) :
 Iiii = xbmcgui . Dialog ( )
 Iiii . ok ( 'Chú ý: User %s' % OO0o . get_setting ( "email" ) , s )
 return OO0o . finish ( )
 if 87 - 87: oO0o0o0ooO0oO / I1i1I - OoOoo0 % iIiiI1 % OOooO % OOoO00o
@ OO0o . route ( '/login' )
def II111iiii ( ) :
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  II = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  oOoOo00oOo = II [ "message" ] % II [ "user_code" ] . upper ( )
  Oo = xbmcgui . DialogProgress ( )
  Oo . create ( 'Login' , oOoOo00oOo )
  if 85 - 85: O00O0O0O0 % iI1I % oO0o0o0ooO0oO
  iiiIi = 0
  while iiiIi < 60 :
   IiIIIiI1I1 = int ( ( iiiIi / 60.0 ) * 100 )
   if Oo . iscanceled ( ) :
    break
   Oo . update ( IiIIIiI1I1 , "" )
   iiiIi = iiiIi + 1
   xbmc . sleep ( 5000 )
   IiII = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( II [ "device_code" ] ) )
   if "token" in IiII . text :
    Oo0Ooo . setSetting ( "token" , IiII . json ( ) [ "token" ] )
    Oo0Ooo . setSetting ( "email" , IiII . json ( ) [ "email" ] )
    break
  Oo . close ( )
  del Oo
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % O0O0OO0O0O0 )
 except :
  OoO000 = xbmcgui . Dialog ( )
  OoO000 . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 42 - 42: oO0o0o0ooO0oO - i11ii11iIi11i / i11iIiiIii + I1i1I + I1II1
@ OO0o . route ( '/' )
def iIi ( ) :
 dir ( "0" )
 if 40 - 40: oO0o0o0ooO0oO . oO0o . Iii1ii1II11i . i11ii11iIi11i
@ OO0o . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ OO0o . route ( '/ytslive/<order>/<page>' )
def I11iii ( order = "viewcount" , page = "" ) :
 iI1Ii11111iIi = Ooo0OO0oOO ( "%s/ytslive/%s/%s" % ( iiiii , order , page ) )
 for OO0O00 in iI1Ii11111iIi :
  OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return OO0o . finish ( iI1Ii11111iIi )
 else :
  return OO0o . finish ( iI1Ii11111iIi )
  if 20 - 20: oOooOoO0Oo0O
@ OO0o . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ OO0o . route ( '/yts/<order>/<t>/<q>/<page>' )
def Ii11iI1i ( order , t , q = "" , page = "" ) :
 iI1Ii11111iIi = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 iI1Ii11111iIi = Ooo0OO0oOO ( "%s/yts/%s/%s?q=%s&page=%s" % ( iiiii , order , t , q , page ) )
 for OO0O00 in iI1Ii11111iIi :
  if "plugin://" not in OO0O00 [ "path" ] :
   OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
 if t == "video" :
  Ooo = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  O0o0Oo = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  iI1Ii11111iIi = Ooo + O0o0Oo + iI1Ii11111iIi
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return OO0o . finish ( iI1Ii11111iIi )
 else :
  return OO0o . finish ( iI1Ii11111iIi )
  if 78 - 78: ii11i - iIiiI1 * I1II1 + OOo000 + OOooO + OOooO
@ OO0o . route ( '/dir/<url>' )
def dir ( url ) :
 iI1Ii11111iIi = [ ]
 if "://" in url :
  pass
 else :
  iI1Ii11111iIi = Ooo0OO0oOO ( "%s/dir/%s" % ( iiiii , urllib . quote_plus ( url ) ) )
  for OO0O00 in iI1Ii11111iIi :
   if "plugin://" not in OO0O00 [ "path" ] :
    OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
  I11I11i1I = ( "" if OO0o . get_setting ( "email" ) == "" else ( "Chào %s. " % OO0o . get_setting ( "email" ) ) )
  ii11i1iIII = [ {
 "label" : "[COLOR yellow][B]%sVào đây để Login/Relogin[/B][/COLOR]" % I11I11i1I ,
 "path" : O0O0OO0O0O0 + "/login" ,
 "thumbnail" : "https://cdn3.iconfinder.com/data/icons/gray-toolbar-2/512/login_user_profile_account-512.png"
 } ]
  iI1Ii11111iIi = ii11i1iIII + iI1Ii11111iIi
  if 3 - 3: i11ii11iIi11i / IiiI % OoOoo0 * i11iIiiIii / iIIi1iI1II111 * OoOoo0
  if 49 - 49: oO0o0o0ooO0oO % iIiiI1 + i11ii11iIi11i . IiiI % O0
  if 48 - 48: OoOoo0 + OoOoo0 / oOoO0oo0OOOo / ii11i
  if 20 - 20: OOo000
  if 77 - 77: oO0o / OoOoo0
  if 98 - 98: ii11i / i11ii11iIi11i / i11iIiiIii / OOo000
  if 28 - 28: I1i1I - OOoO00o . OOoO00o + oO0o - oOooOoO0Oo0O + iIIi1iI1II111
  if 95 - 95: I1II1 % oO0o0o0ooO0oO . iIIi1iI1II111
  if 15 - 15: iI1I / iIiiI1 . iIiiI1 - i11ii11iIi11i
 return OO0o . finish ( iI1Ii11111iIi )
 if 53 - 53: OOoO00o + IiiI * oO0o0o0ooO0oO
@ OO0o . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ OO0o . route ( '/ytp/<pid>/<page>' )
def OooOooooOOoo0 ( pid , page = "" ) :
 iI1Ii11111iIi = Ooo0OO0oOO ( "%s/ytp/%s/%s" % ( iiiii , pid , page ) )
 for OO0O00 in iI1Ii11111iIi :
  OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return OO0o . finish ( iI1Ii11111iIi )
 else :
  return OO0o . finish ( iI1Ii11111iIi )
  if 71 - 71: O00O0O0O0 % oO0o0o0ooO0oO % I1i1I
@ OO0o . route ( '/ytu/<uid>' )
def oO00ooo0 ( uid ) :
 o00 = requests . get ( "%s/ytu/%s" % ( iiiii , uid ) ) . text
 OooOooo ( o00 , "" )
 if 97 - 97: iI1I - I1i1I * i11iIiiIii / oO0o % O00O0O0O0 - oOooOoO0Oo0O
@ OO0o . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ OO0o . route ( '/ytc/<cid>/<page>' )
def OooOooo ( cid , page = "" ) :
 iI1Ii11111iIi = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( O0O0OO0O0O0 , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( iiiii , cid ) ) . text
 if "@" in cid :
  Ooo = Ooo0OO0oOO ( "%s/ytp/%s/%s" % ( iiiii , cid . split ( "@" ) [ 1 ] , page ) )
  for OO0O00 in Ooo :
   OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
  iI1Ii11111iIi += Ooo
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return OO0o . finish ( iI1Ii11111iIi )
 else :
  return OO0o . finish ( iI1Ii11111iIi )
  if 59 - 59: iIIi1iI1II111 + IiiI + OOoO00o % IiiI
@ OO0o . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ OO0o . route ( '/ytcp/<cid>/<page>' )
def o0OOoo0OO0OOO ( cid , page = "" ) :
 iI1Ii11111iIi = Ooo0OO0oOO ( "%s/ytcp/%s/%s" % ( iiiii , cid , page ) )
 for OO0O00 in iI1Ii11111iIi :
  OO0O00 [ "path" ] = O0O0OO0O0O0 + OO0O00 [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( iI1Ii11111iIi , view_mode = 52 )
  else :
   return OO0o . finish ( iI1Ii11111iIi )
 else :
  return OO0o . finish ( iI1Ii11111iIi )
  if 19 - 19: oO0o0o0ooO0oO % i11ii11iIi11i % OOo000
@ OO0o . route ( '/play/<url>' )
def oo0OooOOo0 ( url ) :
 Oo = xbmcgui . DialogProgress ( )
 Oo . create ( 'Kodi4VN Launcher' , 'Loading video. Please wait...' )
 OO0o . set_resolved_url ( iI1 ( url ) )
 Oo . close ( )
 del Oo
 if 92 - 92: OOooO . OoOoo0 + OOo000
@ OO0o . route ( '/showimage/<url>' )
def IiII1I11i1I1I ( url ) :
 iiI1iIiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 oO0Oo = xbmc . translatePath ( os . path . join ( iiI1iIiI , "tmp" ) )
 if os . path . exists ( oO0Oo ) :
  shutil . rmtree ( oO0Oo )
 os . makedirs ( oO0Oo )
 if ".zip" in url :
  oOOoo0Oo = xbmc . translatePath ( os . path . join ( oO0Oo , "temp.zip" ) )
  urllib . urlretrieve ( url , oOOoo0Oo )
  IIII ( oOOoo0Oo , oO0Oo )
 else :
  o00OO00OoO = xbmc . translatePath ( os . path . join ( oO0Oo , "temp.jpg" ) )
  urllib . urlretrieve ( url , o00OO00OoO )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % oO0Oo )
 if 60 - 60: I1II1 * oO0o - I1II1 % oOooOoO0Oo0O - iI1I + IiiI
if __name__ == '__main__' :
 OO0o . run ( )
 if 70 - 70: OOoO00o * Iii1ii1II11i * OoOoo0 / iIiiI1
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
