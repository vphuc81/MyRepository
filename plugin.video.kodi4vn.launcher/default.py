#!/usr/bin/python
#coding=utf-8
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
import requests , re , urllib , os , zipfile , json , uuid , shutil
if 64 - 64: i11iIiiIii
OO0o = Plugin ( )
Oo0Ooo = xbmcaddon . Addon ( "plugin.video.kodi4vn.launcher" )
O0O0OO0O0O0 = "plugin://plugin.video.kodi4vn.launcher"
iiiii = "http://echipstore.com:8000"
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( url ) :
 i1I11i = requests . get ( url + "%st=%s" % ( "&" if "?" in url else "?" , urllib . quote_plus ( OO0o . get_setting ( "token" ) ) ) )
 i1I11i . encoding = "utf-8"
 OoOoOO00 = i1I11i . json ( )
 return OoOoOO00
 if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
def o0OOO ( url ) :
 OoOoOO00 = iI1 ( url )
 return OoOoOO00
 if 13 - 13: ooOo + Ooo0O
def IiiIII111iI ( source , dest_dir ) :
 with zipfile . ZipFile ( source ) as IiII :
  for iI1Ii11111iIi in IiII . infolist ( ) :
   i1i1II = iI1Ii11111iIi . filename . split ( '/' )
   O0oo0OO0 = dest_dir
   for I1i1iiI1 in i1i1II [ : - 1 ] :
    iiIIIII1i1iI , I1i1iiI1 = os . path . splitdrive ( I1i1iiI1 )
    o0oO0 , I1i1iiI1 = os . path . split ( I1i1iiI1 )
    if I1i1iiI1 in ( os . curdir , os . pardir , '' ) : continue
    O0oo0OO0 = os . path . join ( O0oo0OO0 , I1i1iiI1 )
   IiII . extract ( iI1Ii11111iIi , O0oo0OO0 )
   if 100 - 100: i11Ii11I1Ii1i
@ OO0o . route ( '/warning/<s>' )
def Ooo ( s = "" ) :
 o0oOoO00o = xbmcgui . Dialog ( )
 o0oOoO00o . ok ( 'Chú ý: User %s' % OO0o . get_setting ( "email" ) , s )
 return OO0o . finish ( )
 if 43 - 43: O0OOo . II1Iiii1111i
@ OO0o . route ( '/login' )
def i1IIi11111i ( ) :
 o000o0o00o0Oo ( "Login" , "/login" )
 xbmc . executebuiltin ( 'Dialog.Close(busydialog)' )
 try :
  oo = requests . get ( "http://echipstore.com/get-code/?nocache=true" ) . json ( )
  IiII1I1i1i1ii = oo [ "message" ] % oo [ "user_code" ] . upper ( )
  IIIII = xbmcgui . DialogProgress ( )
  IIIII . create ( 'Login' , IiII1I1i1i1ii )
  if 26 - 26: O00OoOoo00 . iiiI11 / oooOOOOO * IiiIII111ii / i1iIIi1
  ii11iIi1I = 0
  while ii11iIi1I < 60 :
   iI111I11I1I1 = int ( ( ii11iIi1I / 60.0 ) * 100 )
   if IIIII . iscanceled ( ) :
    break
   IIIII . update ( iI111I11I1I1 , "" )
   ii11iIi1I = ii11iIi1I + 1
   xbmc . sleep ( 5000 )
   i1I11i = requests . get ( "http://echipstore.com/device?device_code=%s&nocache=true" % urllib . quote_plus ( oo [ "device_code" ] ) )
   if "token" in i1I11i . text :
    Oo0Ooo . setSetting ( "token" , i1I11i . json ( ) [ "token" ] )
    Oo0Ooo . setSetting ( "email" , i1I11i . json ( ) [ "email" ] )
    break
  IIIII . close ( )
  del IIIII
  xbmc . executebuiltin ( 'XBMC.Container.Update(%s)' % O0O0OO0O0O0 )
 except :
  OOooO0OOoo = xbmcgui . Dialog ( )
  OOooO0OOoo . ok ( "Oops!" , "Có lỗi xảy ra. Xin quý vị vui lòng login vào dịp khác" )
  if 29 - 29: o00o / IiI1I1
@ OO0o . route ( '/' )
def OoO000 ( ) :
 o000o0o00o0Oo ( )
 dir ( "0" )
 if 42 - 42: II1Iiii1111i - OOOo0 / i11iIiiIii + O00OoOoo00 + ooOo
@ OO0o . route ( '/ytslive/<order>/' , name = "ytslive_firstpage" )
@ OO0o . route ( '/ytslive/<order>/<page>' )
def iIi ( order = "viewcount" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Live News" , "/ytslive/%s/%s" % ( order , page ) )
 OoOoOO00 = o0OOO ( "%s/ytslive/%s/%s" % ( iiiii , order , page ) )
 for II in OoOoOO00 :
  II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 14 - 14: I1IiI . Ooo00oOo00o / oooOOOOO
@ OO0o . route ( '/yts/<order>/<t>/<q>/' , name = 'yts_firstpage' )
@ OO0o . route ( '/yts/<order>/<t>/<q>/<page>' )
def IiiiI1II1I1 ( order , t , q = "" , page = "" ) :
 o000o0o00o0Oo ( "Browse YT by topics %s" % q , "/yts/%s/%s/%s/%s" % ( order , t , q , page ) )
 OoOoOO00 = [ ]
 if t in [ "channel" , "playlist" ] and order == "date" :
  order = "videocount"
 OoOoOO00 = o0OOO ( "%s/yts/%s/%s?q=%s&page=%s" % ( iiiii , order , t , q , page ) )
 for II in OoOoOO00 :
  if "plugin://" not in II [ "path" ] :
   II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
 if t == "video" :
  ooIi11iI1i = [ {
 "label" : "[B]Channels[/B]" ,
 "path" : "%s/yts/%s/channel/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "http://thong.viettv24.com/kodi4vn/images/yt.png"
 } ]
  OooO0o0Oo = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/yts/%s/playlist/%s" % ( O0O0OO0O0O0 , order , q ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
  OoOoOO00 = ooIi11iI1i + OooO0o0Oo + OoOoOO00
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 78 - 78: ii11i - oooOOOOO * ooOo + i11Ii11I1Ii1i + IiiIII111ii + IiiIII111ii
@ OO0o . route ( '/dir/<url>' )
def dir ( url ) :
 o000o0o00o0Oo ( "Browse Kodi4vn Launcher Menu %s" % url , "/dir/%s" % url )
 OoOoOO00 = [ ]
 if "://" in url :
  pass
 else :
  OoOoOO00 = o0OOO ( "%s/dir/%s" % ( iiiii , urllib . quote_plus ( url ) ) )
  for II in OoOoOO00 :
   if "plugin://" not in II [ "path" ] :
    II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
  I11I11i1I = ( "" if OO0o . get_setting ( "email" ) == "" else ( "Chào %s. " % OO0o . get_setting ( "email" ) ) )
  ii11i1iIII = [ {
 "label" : "[COLOR yellow][B]%sVào đây để Login/Relogin[/B][/COLOR]" % I11I11i1I ,
 "path" : O0O0OO0O0O0 + "/login" ,
 "thumbnail" : "https://cdn3.iconfinder.com/data/icons/gray-toolbar-2/512/login_user_profile_account-512.png"
 } ]
  OoOoOO00 = ii11i1iIII + OoOoOO00
  if 3 - 3: OOOo0 / Ooo00oOo00o % iiiI11 * i11iIiiIii / iIIi1iI1II111 * iiiI11
  if 49 - 49: II1Iiii1111i % oooOOOOO + OOOo0 . Ooo00oOo00o % O0OOo
  if 48 - 48: iiiI11 + iiiI11 / Oo / ii11i
  if 20 - 20: i11Ii11I1Ii1i
  if 77 - 77: Ooo0O / iiiI11
  if 98 - 98: ii11i / OOOo0 / i11iIiiIii / i11Ii11I1Ii1i
  if 28 - 28: O00OoOoo00 - i1iIIi1 . i1iIIi1 + Ooo0O - oOooOoO0Oo0O + iIIi1iI1II111
  if 95 - 95: ooOo % II1Iiii1111i . iIIi1iI1II111
  if 15 - 15: IiI1I1 / oooOOOOO . oooOOOOO - OOOo0
 return OO0o . finish ( OoOoOO00 )
 if 53 - 53: i1iIIi1 + Ooo00oOo00o * II1Iiii1111i
@ OO0o . route ( '/ytp/<pid>' , name = 'ytp_firstpage' )
@ OO0o . route ( '/ytp/<pid>/<page>' )
def OooOooooOOoo0 ( pid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by PlaylistID %s" % pid , "/ytp/%s/%s" % ( pid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , pid , page ) )
 for II in OoOoOO00 :
  II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 71 - 71: o00o % II1Iiii1111i % O00OoOoo00
@ OO0o . route ( '/ytu/<uid>' )
def oO00ooo0 ( uid ) :
 o00 = requests . get ( "%s/ytu/%s" % ( iiiii , uid ) ) . text
 OooOooo ( o00 , "" )
 if 97 - 97: IiI1I1 - O00OoOoo00 * i11iIiiIii / Ooo0O % o00o - oOooOoO0Oo0O
@ OO0o . route ( '/ytc/<cid>' , name = 'ytc_firstpage' )
@ OO0o . route ( '/ytc/<cid>/<page>' )
def OooOooo ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Videos by ChannelID %s" % cid , "/ytc/%s/%s" % ( cid , page ) )
 OoOoOO00 = [ {
 "label" : "[B]Playlist[/B]" ,
 "path" : "%s/ytcp/%s/%s" % ( O0O0OO0O0O0 , cid . split ( "@" ) [ 0 ] , "" ) ,
 "thumbnail" : "https://lh3.googleusercontent.com/184S-U4BBN7f55qcTQFUQSsBjYlJZ246A01J-n_BKa4bwe74nANMPkj58I8DSPzlxYyWocyYYYj89D-1qHXfEkVENdA6O1weJZOVZAMCAIhK8vfZ9bgKpw-eY4pwpaCzfQ0MS4wlwnjZE28jmTZejHIVRflEUcPS-SLJ6xGTAVIHXbIP1uEKugegwL9ULD0vfwD92FWzz9_abZ70VNeBTBRCjE3-gfQ-IKVUmGJlnJeEJcS1fUAo6_qvrBf9NX1n0gLp24lVdTj-ml6VmDtr5bVwQBBes-7zTKthqeLqZoo-Zr0ZDY2hhw871xrXDeUtlwVeK-EnAEgFRAWyRa9HjijEEED81GDYkCc5r0qK3xjqqPvo3aJ-urdVH2TcOkbmTgx2l7jHIMo4WuE9-d8hAMzGXJfLp4NNGty3vYLk-0RG_MjvUp4qeNcmPMHrX8fWih2z-hAXhfvjXZ1SJq_BEnFzSgVCyW44inHkLUallDmcbFyz5EuYgEAVYHMUikabDj2eLrsMbHTM94a_ljcBV9X4jS0Dz5EMjLl5veXQmCA=w175-h107-no"
 } ]
 if "@" not in cid :
  cid = requests . get ( "%s/ytc/%s" % ( iiiii , cid ) ) . text
 if "@" in cid :
  ooIi11iI1i = o0OOO ( "%s/ytp/%s/%s" % ( iiiii , cid . split ( "@" ) [ 1 ] , page ) )
  for II in ooIi11iI1i :
   II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
  OoOoOO00 += ooIi11iI1i
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 59 - 59: iIIi1iI1II111 + Ooo00oOo00o + i1iIIi1 % Ooo00oOo00o
@ OO0o . route ( '/ytcp/<cid>' , name = 'ytcp_firstpage' )
@ OO0o . route ( '/ytcp/<cid>/<page>' )
def o0OOoo0OO0OOO ( cid , page = "" ) :
 o000o0o00o0Oo ( "Browse YT Playlist by ChannelID %s" % cid , "/ytcp/%s/%s" % ( cid , page ) )
 OoOoOO00 = o0OOO ( "%s/ytcp/%s/%s" % ( iiiii , cid , page ) )
 for II in OoOoOO00 :
  II [ "path" ] = O0O0OO0O0O0 + II [ "path" ]
 if OO0o . get_setting ( 'thumbview' , bool ) :
  if xbmc . getSkinDir ( ) in ( 'skin.confluence' , 'skin.eminence' ) :
   return OO0o . finish ( OoOoOO00 , view_mode = 500 )
  elif xbmc . getSkinDir ( ) == 'skin.xeebo' :
   return OO0o . finish ( OoOoOO00 , view_mode = 52 )
  else :
   return OO0o . finish ( OoOoOO00 )
 else :
  return OO0o . finish ( OoOoOO00 )
  if 19 - 19: II1Iiii1111i % OOOo0 % i11Ii11I1Ii1i
@ OO0o . route ( '/play/<url>' )
def oo0OooOOo0 ( url ) :
 o000o0o00o0Oo ( "Play %s" % url , "/play/%s" % url )
 IIIII = xbmcgui . DialogProgress ( )
 IIIII . create ( 'Kodi4VN Launcher' , 'Loading video. Please wait...' )
 OO0o . set_resolved_url ( o0O ( url ) )
 IIIII . close ( )
 del IIIII
 if 72 - 72: IiiIII111ii / OOOo0 * I1IiI - o00o
def o0O ( url ) :
 if "youtube" in url :
  Oo0O0O0ooO0O = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( url )
  IIIIii = Oo0O0O0ooO0O [ 0 ] [ len ( Oo0O0O0ooO0O [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % IIIIii
 elif "://" not in url :
  O0o0 = "http://www.viettv24.com/main/getStreamingServer.php"
  OO00Oo = { 'strname' : '%s-' % url }
  return requests . post ( O0o0 , data = OO00Oo ) . text . strip ( )
 else :
  return url
  if 51 - 51: i1iIIi1 * i11Ii11I1Ii1i + iiiI11 + ooOo
@ OO0o . route ( '/showimage/<url>' )
def o0O0O00 ( url ) :
 O0oo0OO0 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 o000o = xbmc . translatePath ( os . path . join ( O0oo0OO0 , "tmp" ) )
 if os . path . exists ( o000o ) :
  shutil . rmtree ( o000o )
 os . makedirs ( o000o )
 if ".zip" in url :
  I11IiI1I11i1i = xbmc . translatePath ( os . path . join ( o000o , "temp.zip" ) )
  urllib . urlretrieve ( url , I11IiI1I11i1i )
  IiiIII111iI ( I11IiI1I11i1i , o000o )
 else :
  iI1ii1Ii = xbmc . translatePath ( os . path . join ( o000o , "temp.jpg" ) )
  urllib . urlretrieve ( url , iI1ii1Ii )
 xbmc . executebuiltin ( "SlideShow(%s,recursive)" % o000o )
 if 92 - 92: Ooo0O
def o000o0o00o0Oo ( title = "Home" , page = "/" ) :
 i1 = "http://www.google-analytics.com/collect"
 OOO = open ( Oo0oOOo ) . read ( )
 Oo0OoO00oOO0o = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : OOO ,
 't' : 'pageview' ,
 'dp' : page ,
 'dt' : title
 }
 requests . post ( i1 , data = urllib . urlencode ( Oo0OoO00oOO0o ) )
 if 80 - 80: II1Iiii1111i + O00OoOoo00 - O00OoOoo00 % IiiIII111ii
OoOO0oo0o = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( OoOO0oo0o ) == False :
 os . mkdir ( OoOO0oo0o )
Oo0oOOo = os . path . join ( OoOO0oo0o , 'cid' )
if 14 - 14: i11Ii11I1Ii1i * IiiIII111ii * IiiIII111ii / Ooo0O
if os . path . exists ( Oo0oOOo ) == False :
 with open ( Oo0oOOo , "w" ) as Oo0o00 :
  Oo0o00 . write ( str ( uuid . uuid1 ( ) ) )
  if 73 - 73: IiiIII111ii * oooOOOOO + i11Ii11I1Ii1i . O00OoOoo00 + O0OOo % IiiIII111ii
if __name__ == '__main__' :
 OO0o . run ( )
 if 95 - 95: OOOo0
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
