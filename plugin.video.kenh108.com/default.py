#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib , urllib2 , re , os , uuid , json , htmlentitydefs
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
oo000 = Plugin ( )
ii = "plugin://plugin.video.kenh108.com"
oOOo = 40
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
@ oo000 . route ( '/' )
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 '''urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/kenh108.jpg' , I11i11Ii )
 oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 OOOo0 = xbmcgui . WindowDialog ( )
 OOOo0 . addControl ( oO00oOo )
 OOOo0 . doModal ( )'''
 Oooo000o = ""
 IiIi11iIIi1Ii = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 while True :
  Oo0O = urllib . quote ( xbmc . getInfoLabel ( "System.KernelVersion" ) . strip ( ) )
  if not any ( b in Oo0O for b in IiIi11iIIi1Ii ) : break
 while True :
  IiI = urllib . quote ( xbmc . getInfoLabel ( "System.FriendlyName" ) . strip ( ) )
  if not any ( b in IiI for b in IiIi11iIIi1Ii ) : break
 try :
  Oooo000o = open ( '/sys/class/net/eth0/address' ) . read ( ) . strip ( )
 except :
  while True :
   Oooo000o = xbmc . getInfoLabel ( "Network.MacAddress" ) . strip ( )
   if re . match ( "[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$" , Oooo000o . lower ( ) ) : break
 ooOo = urllib2 . urlopen ( "http://www.viettv24.com/main/checkActivation.php?MacID=%s&app_id=%s&sys=%s&dev=%s" % ( Oooo000o , "6" , Oo0O , IiI ) ) . read ( )
 if "allowed" in ooOo :
  Oo = [
 { 'label' : 'Recently Updated Videos' , 'path' : '%s/updated/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=recently_updated&page=%s' ) , 1 ) } ,
 { 'label' : 'Recently Added Videos' , 'path' : '%s/added/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=more&page=%s' ) , 1 ) } ,
 { 'label' : 'Search' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( Oo )
 else :
  Oo = [
 { 'label' : 'Recently Updated Videos' , 'path' : '%s/updated/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=recently_updated&page=%s' ) , 1 ) } ,
 { 'label' : 'Recently Added Videos' , 'path' : '%s/added/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=more&page=%s' ) , 1 ) } ,
 { 'label' : 'Search' , 'path' : '%s/search' % ii }
 ]
  return oo000 . finish ( Oo )
  if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
  if 97 - 97: oO0o0ooO0 - IIII / O0oO - o0oO0
@ oo000 . route ( '/updated/<murl>/<page>' )
def oo00 ( murl , page ) :
 Oo = o00 ( murl , page , 'updated' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( Oo )
 if 62 - 62: II1ii - o0oOoO00o . iIi1IIii11I + oo0 * Ooo0 % oo00000o0
@ oo000 . route ( '/added/<murl>/<page>' )
def I11i1i11i1I ( murl , page ) :
 Oo = o00 ( murl , page , 'added' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( Oo )
 if 31 - 31: Oo0Ooo / IiII / oo00000o0 * O0oO / I1Ii111
@ oo000 . route ( '/search/' )
def Oo0o0ooO0oOOO ( ) :
 oo0O000OoO = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if oo0O000OoO :
  i1iiIIiiI111 = '%s/search/%s' % ( ii , urllib . quote_plus ( oo0O000OoO ) )
  oo000 . redirect ( i1iiIIiiI111 )
  if 62 - 62: Oo0Ooo - iII111i
@ oo000 . route ( '/search/<search_string>' )
def IIIiI11ii ( search_string ) :
 Oo = O000oo ( search_string , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( Oo )
 if 3 - 3: iIi1IIii11I + OO0OO0O0O0
@ oo000 . route ( '/mirrors/<murl>' )
def I1Ii ( murl ) :
 Oo = [ ]
 for o0oOo0Ooo0O in OO00O0O0O00Oo ( murl ) :
  IIIiiiiiIii = { }
  IIIiiiiiIii [ "label" ] = o0oOo0Ooo0O [ "name" ] . strip ( )
  OO = str ( uuid . uuid1 ( ) )
  oO0O = oo000 . get_storage ( OO )
  oO0O [ "list" ] = o0oOo0Ooo0O [ "eps" ]
  IIIiiiiiIii [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( OO ) )
  Oo . append ( IIIiiiiiIii )
 return oo000 . finish ( Oo )
 if 70 - 70: I1Ii111 % I1Ii111 . oo0 % ooOoO0o * oO0o0ooO0 % O0oO
@ oo000 . route ( '/eps/<eps_list>' )
def iiI1IiI ( eps_list ) :
 Oo = [ ]
 for II in oo000 . get_storage ( eps_list ) [ "list" ] :
  IIIiiiiiIii = { }
  IIIiiiiiIii [ "label" ] = II [ "name" ] . strip ( )
  IIIiiiiiIii [ "is_playable" ] = True
  IIIiiiiiIii [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( II [ "url" ] ) )
  Oo . append ( IIIiiiiiIii )
 return oo000 . finish ( Oo )
 if 57 - 57: O0oO
@ oo000 . route ( '/play/<url>' )
def iI ( url ) :
 iI11iiiI1II = xbmcgui . DialogProgress ( )
 iI11iiiI1II . create ( 'kenh108.com' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( O0oooo0Oo00 ( url ) )
 iI11iiiI1II . close ( )
 del iI11iiiI1II
 if 17 - 17: iiiIIii1IIi % oo00000o0 % Oo0Ooo . IiII
def O0oooo0Oo00 ( url ) :
 ooOo = O0o0Oo ( url )
 if "proxy.link" in ooOo :
  Oo00OOOOO = re . compile ( 'proxy.link=kenh108\*(.+?)&' ) . findall ( ooOo ) [ 0 ]
  O0O = O00o0OO ( Oo00OOOOO )
  print O0O
 if "youtube" in O0O :
  Oo00OOOOO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( O0O )
  I11i1 = Oo00OOOOO [ 0 ] [ len ( Oo00OOOOO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % I11i1
 if "picasaweb" in O0O :
  iIi1ii1I1 = 480
  if oo000 . get_setting ( 'HQ' , bool ) : iIi1ii1I1 = 720
  o0 = ""
  if "lh/photo" not in O0O :
   for I11II1i , IIIII , ooooooO0oo in re . compile ( 'https://picasaweb.google.com/(\d+).*?\?authkey=(.+?)#(\d+)' ) . findall ( O0O ) :
    IIiiiiiiIi1I1 = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?authkey=%s&alt=json" % ( I11II1i , ooooooO0oo , IIIII )
    I1IIIii = json . loads ( urllib2 . urlopen ( IIiiiiiiIi1I1 ) . read ( ) ) [ "feed" ] [ "media$group" ] [ "media$content" ]
    for oOoOooOo0o0 in I1IIIii :
     if ( oOoOooOo0o0 [ "type" ] == "video/mpeg4" ) and ( int ( oOoOooOo0o0 [ "height" ] ) <= iIi1ii1I1 ) :
      o0 = oOoOooOo0o0 [ "url" ]
  else :
   ooOo = urllib2 . urlopen ( O0O ) . read ( )
   IIiiiiiiIi1I1 = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( ooOo ) [ 0 ]
   ooOo = urllib2 . urlopen ( IIiiiiiiIi1I1 ) . read ( )
   I1IIIii = json . loads ( ooOo ) [ "feed" ] [ "media" ] [ "content" ]
   for oOoOooOo0o0 in I1IIIii :
    if ( oOoOooOo0o0 [ "type" ] == "video/mpeg4" ) and ( int ( oOoOooOo0o0 [ "height" ] ) <= iIi1ii1I1 ) :
     o0 = oOoOooOo0o0 [ "url" ]
  return o0
  if 61 - 61: oO0o0ooO0 / ooOoO0o + oo00000o0 * O0oO / O0oO
def o00 ( url , page , route_name ) :
 OoOo = int ( page ) + 1
 ooOo = O0o0Oo ( url % page )
 Oo00OOOOO = re . compile ( '<div class="movie_pix" [^>]* url\((.+?)\) [^>]*><a href="(.+?)"><img [^>]*></a></div><div class="movietitle"><a [^>]*>(.+?)<div class="listmovies_secondtitle" [^>]*>(.*?)</div></a>' ) . findall ( ooOo )
 Oo = [ ]
 for iIo00O , OOO0OOO00oo , Iii111II , iiii11I in Oo00OOOOO :
  IIIiiiiiIii = { }
  Ooo0OO0oOO = ""
  if "<sup>" in Iii111II :
   Ooo0OO0oOO = ii11i1 ( re . compile ( '<sup>(.+?)</sup>' ) . findall ( Iii111II ) [ 0 ] ) . encode ( "utf8" )
  IIIii1II1II = Iii111II . split ( "<" ) [ 0 ] . strip ( )
  IIIii1II1II + Ooo0OO0oOO
  IIIiiiiiIii [ "label" ] = "%s - %s (%s)" % ( IIIii1II1II , iiii11I , Ooo0OO0oOO )
  IIIiiiiiIii [ "thumbnail" ] = iIo00O
  IIIiiiiiIii [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://www.lsb-movies.net/kenh108/" + OOO0OOO00oo . replace ( "/phim/" , "/xem-phim-online/" ) ) )
  Oo . append ( IIIiiiiiIii )
 if len ( Oo ) == oOOo :
  Oo . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , OoOo ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return Oo
 if 42 - 42: o0oOoO00o + O0oO
def O000oo ( search_string , route_name ) :
 ooOo = o0O0o0Oo ( search_string )
 Oo00OOOOO = re . compile ( '<div class="searchresults_image" [^>]*><a href="(index.php\?do=xem&mid=\d+)&image=(.+?)" alt=(.+?)>' ) . findall ( ooOo )
 Oo = [ ]
 for OOO0OOO00oo , iIo00O , Ii11Ii1I in Oo00OOOOO :
  IIIiiiiiIii = { }
  IIIiiiiiIii [ "label" ] = Ii11Ii1I
  IIIiiiiiIii [ "thumbnail" ] = iIo00O
  IIIiiiiiIii [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://www.lsb-movies.net/kenh108/" + OOO0OOO00oo . replace ( "/phim/" , "/xem-phim-online/" ) ) )
  Oo . append ( IIIiiiiiIii )
 return Oo
 if 72 - 72: iIi1IIii11I / I1IiiI * I1Ii111 - Ooo0
def OO00O0O0O00Oo ( murl ) :
 ooOo = O0o0Oo ( murl )
 Oo0O0O0ooO0O = re . compile ( '<div class="noidung_servers">(.+?</div></div>)' ) . findall ( ooOo ) [ 0 ] . replace ( "</div></div>" , "<br>" )
 Oo00OOOOO = re . compile ( '<div class="noidung_servername">(.+?)</div>(.+?)<br>' ) . findall ( Oo0O0O0ooO0O )
 IIIIii = re . compile ( '<title>(.+?)</title>' ) . findall ( ooOo ) [ 0 ] . replace ( "K&#202;NH 108 - " , "" )
 O0o0 = [ ]
 for OO00Oo , O0OOO0OOoO0O in Oo00OOOOO :
  O00Oo000ooO0 = [ ]
  for OoO0O00 , IIiII in re . compile ( '<a class="tapphim" href="(.+?)">(.+?)</a>' ) . findall ( O0OOO0OOoO0O ) :
   II = { }
   II [ "url" ] = "http://www.lsb-movies.net/kenh108/" + OoO0O00
   II [ "name" ] = "Part %s - %s" % ( IIiII , ii11i1 ( IIIIii . strip ( ) . decode ( "utf8" ) ) )
   O00Oo000ooO0 . append ( II )
  o0oOo0Ooo0O = { }
  o0oOo0Ooo0O [ "name" ] = re . sub ( '<[^<]+?>' , '' , ii11i1 ( OO00Oo ) ) . encode ( "utf8" )
  o0oOo0Ooo0O [ "eps" ] = O00Oo000ooO0
  O0o0 . append ( o0oOo0Ooo0O )
 return O0o0
 if 80 - 80: oo0 . O0oO
@ oo000 . cached ( TTL = 60 )
def O0o0Oo ( url ) :
 IIi = urllib2 . Request ( url )
 IIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 IIi . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 IIi . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 IIi . add_header ( 'Referer' , 'http://www.luongson.net/kenh108/index.php' )
 i11iIIIIIi1 = urllib2 . urlopen ( IIi )
 iiII1i1 = i11iIIIIIi1 . read ( )
 i11iIIIIIi1 . close ( )
 if 66 - 66: o0oO0 - II1ii
 if 5 - 5: Ooo0 + o0oOoO00o / I1Ii111 - O0oO
 iiII1i1 = '' . join ( iiII1i1 . splitlines ( ) ) . replace ( '\'' , '"' )
 iiII1i1 = iiII1i1 . replace ( '\n' , '' )
 iiII1i1 = iiII1i1 . replace ( '\t' , '' )
 iiII1i1 = re . sub ( '  +' , ' ' , iiII1i1 )
 iiII1i1 = iiII1i1 . replace ( '> <' , '><' )
 return iiII1i1
 if 63 - 63: o0oO0 % O0oO * O0oO * ooOoO0o / IIII
@ oo000 . cached ( TTL = 60 )
def o0O0o0Oo ( search_string ) :
 IIi = urllib2 . Request ( "http://www.lsb-movies.org/kenh108/index.php?do=timkiem" )
 IIi . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 IIi . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 IIi . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 IIi . add_header ( 'Referer' , 'http://www.luongson.net/kenh108/index.php' )
 o0ooO = { "search_this" : search_string }
 i11iIIIIIi1 = urllib2 . urlopen ( IIi , urllib . urlencode ( o0ooO ) )
 iiII1i1 = i11iIIIIIi1 . read ( )
 i11iIIIIIi1 . close ( )
 if 98 - 98: iIi1IIii11I * iIi1IIii11I / iIi1IIii11I + II1ii
 if 34 - 34: oo00000o0
 iiII1i1 = '' . join ( iiII1i1 . splitlines ( ) ) . replace ( '\'' , '"' )
 iiII1i1 = iiII1i1 . replace ( '\n' , '' )
 iiII1i1 = iiII1i1 . replace ( '\t' , '' )
 iiII1i1 = re . sub ( '  +' , ' ' , iiII1i1 )
 iiII1i1 = iiII1i1 . replace ( '> <' , '><' )
 return iiII1i1
 if 15 - 15: II1ii * oo00000o0 * I1Ii111 % Oo0Ooo % o00O0oo - o0oO0
 if 68 - 68: Ooo0 % I1IiiI . oo0 . IIII
o0oo0oOo = [ 1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 27 , 54 , 108 , 216 , 171 , 77 , 154 , 47 , 94 , 188 , 99 , 198 , 151 , 53 , 106 , 212 , 179 , 125 , 250 , 239 , 197 , 145 ] ;
o000O0o = [ 99 , 124 , 119 , 123 , 242 , 107 , 111 , 197 , 48 , 1 , 103 , 43 , 254 , 215 , 171 , 118 , 202 , 130 , 201 , 125 , 250 , 89 , 71 , 240 , 173 , 212 , 162 , 175 , 156 , 164 , 114 , 192 , 183 , 253 , 147 , 38 , 54 , 63 , 247 , 204 , 52 , 165 , 229 , 241 , 113 , 216 , 49 , 21 , 4 , 199 , 35 , 195 , 24 , 150 , 5 , 154 , 7 , 18 , 128 , 226 , 235 , 39 , 178 , 117 , 9 , 131 , 44 , 26 , 27 , 110 , 90 , 160 , 82 , 59 , 214 , 179 , 41 , 227 , 47 , 132 , 83 , 209 , 0 , 237 , 32 , 252 , 177 , 91 , 106 , 203 , 190 , 57 , 74 , 76 , 88 , 207 , 208 , 239 , 170 , 251 , 67 , 77 , 51 , 133 , 69 , 249 , 2 , 127 , 80 , 60 , 159 , 168 , 81 , 163 , 64 , 143 , 146 , 157 , 56 , 245 , 188 , 182 , 218 , 33 , 16 , 255 , 243 , 210 , 205 , 12 , 19 , 236 , 95 , 151 , 68 , 23 , 196 , 167 , 126 , 61 , 100 , 93 , 25 , 115 , 96 , 129 , 79 , 220 , 34 , 42 , 144 , 136 , 70 , 238 , 184 , 20 , 222 , 94 , 11 , 219 , 224 , 50 , 58 , 10 , 73 , 6 , 36 , 92 , 194 , 211 , 172 , 98 , 145 , 149 , 228 , 121 , 231 , 200 , 55 , 109 , 141 , 213 , 78 , 169 , 108 , 86 , 244 , 234 , 101 , 122 , 174 , 8 , 186 , 120 , 37 , 46 , 28 , 166 , 180 , 198 , 232 , 221 , 116 , 31 , 75 , 189 , 139 , 138 , 112 , 62 , 181 , 102 , 72 , 3 , 246 , 14 , 97 , 53 , 87 , 185 , 134 , 193 , 29 , 158 , 225 , 248 , 152 , 17 , 105 , 217 , 142 , 148 , 155 , 30 , 135 , 233 , 206 , 85 , 40 , 223 , 140 , 161 , 137 , 13 , 191 , 230 , 66 , 104 , 65 , 153 , 45 , 15 , 176 , 84 , 187 , 22 ] ;
iI1iII1 = [ 0 , 0 , 0 , 0 , [ 0 , 1 , 2 , 3 ] , 0 , [ 0 , 1 , 2 , 3 ] , 0 , [ 0 , 1 , 3 , 4 ] ] ;
oO0OOoo0OO = 4 ;
O0 = 6 ;
ii1ii1ii = 12 ;
if 91 - 91: oo0
def O00o0OO ( param1 ) :
 iiIii = [ ]
 ooo0O = [ ]
 oOoO0o00OO0 = i1I1ii ( param1 ) ;
 oOOo0 = 16 ;
 oo00O00oO = [ 1966101078 , 1516336945 , 1263424345 , 1379365717 , 909404232 , 0 , 374550836L , 1278363141L , 125572444L , 1431004681L , 1669271105L , 1669271105L , - 1784093795L , - 644176488L , - 555306812L , - 1951541555L , - 388835188L , - 1951541555L , 680883823L , - 250620937L , 803824435L , - 1539000834L , 1284926834L , - 952386625L , 542348429L , - 782481542L , - 21683127L , 1525780919L , 375913669L , - 782481542L , - 93462979L , 724670791L , - 712721138L , - 1888146247L , - 1726820228L , 1213110022L , - 1790971499L , - 1106351918L , 1804260828L , - 452986523L , 2112694553L , 899923487L , 1437203323L , - 341339223L , - 2144516491L , 1691533072L , 423597577L , 748431382L , 316155343L , - 109070746L , 2035478547L , 494948099L ]
 if 23 - 23: ooOoO0o + ooOoO0o . o0oO0
 ii1ii11IIIiiI = ( len ( oOoO0o00OO0 ) / oOOo0 ) - 1 ;
 if 67 - 67: II1ii * O0oO * IIII + o0oO0 / I1IiiI
 while ii1ii11IIIiiI > 0 :
  ooo0O = I1I111 ( oOoO0o00OO0 [ ii1ii11IIIiiI * oOOo0 : ( ii1ii11IIIiiI + 1 ) * oOOo0 ] , oo00O00oO ) ;
  iiIii = ooo0O + ( iiIii )
  ii1ii11IIIiiI -= 1 ;
  if 82 - 82: Oo0Ooo - iIi1IIii11I * iII111iiiii11 / II1ii
 i1 = I1I111 ( oOoO0o00OO0 [ 0 : int ( oOOo0 ) ] , oo00O00oO )
 if 57 - 57: O0oO . II1ii . I1IiiI
 iiIii = i1 + iiIii ;
 if 42 - 42: II1ii + IIII % OO0OO0O0O0
 iiIii = i1iIIIi1i ( iiIii ) ;
 if 43 - 43: o00O0oo % o0oO0
 return iiIii . split ( '\0' ) [ 0 ] ;
 if 5 - 5: Oo0Ooo - I1IiiI / iiiIIii1IIi
 if 26 - 26: II1ii . iII111iiiii11
def I11i1ii1 ( x ) :
 x = 0xffffffff & x
 if x > 0x7fffffff :
  return - ( ~ ( x - 1 ) & 0xffffffff )
 else : return x
 if 87 - 87: II1ii - iiiIIii1IIi + IiII . iIi1IIii11I
def Oo0oOOOoOooOo ( param1 ) :
 O000ooIIi1I11I1II = [ ]
 OooOoooOo = 0 ;
 while ( OooOoooOo < len ( param1 ) ) :
  O000ooIIi1I11I1II . append ( ord ( param1 [ OooOoooOo ] ) ) ;
  OooOoooOo += 1 ;
  if 46 - 46: iIi1IIii11I
 return O000ooIIi1I11I1II ;
 if 8 - 8: O0oO * o00O0oo - o0oOoO00o - ooOoO0o * o0oO0 % IiII
def i1iIIIi1i ( param1 ) :
 O000ooIIi1I11I1II = ''
 OooOoooOo = 0 ;
 while ( OooOoooOo < len ( param1 ) ) :
  O000ooIIi1I11I1II = O000ooIIi1I11I1II + chr ( param1 [ OooOoooOo ] ) ;
  OooOoooOo += 1 ;
 return O000ooIIi1I11I1II ;
 if 48 - 48: OO0OO0O0O0
def I1IiiIIIi ( param1 ) :
 O000ooIIi1I11I1II = [ [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ]
 OooOoooOo = 0 ;
 while ( OooOoooOo < len ( param1 ) ) :
  O000ooIIi1I11I1II [ 0 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo ] ;
  O000ooIIi1I11I1II [ 1 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 1 ] ;
  O000ooIIi1I11I1II [ 2 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 2 ] ;
  O000ooIIi1I11I1II [ 3 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 3 ] ;
  OooOoooOo = OooOoooOo + 4 ;
 return O000ooIIi1I11I1II ;
 if 41 - 41: o0oOoO00o - OO0OO0O0O0 - OO0OO0O0O0
 if 68 - 68: o0oO0 % Ooo0
def ooO00OO0 ( param1 ) :
 O000ooIIi1I11I1II = [ ]
 OooOoooOo = 0 ;
 while ( OooOoooOo < len ( param1 [ 0 ] ) ) :
  O000ooIIi1I11I1II . append ( param1 [ 0 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 1 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 2 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 3 ] [ OooOoooOo ] ) ;
  OooOoooOo += 1 ;
 return O000ooIIi1I11I1II ;
 if 31 - 31: iIi1IIii11I % iIi1IIii11I % II1ii
 if 69 - 69: ooOoO0o - I1Ii111 + I1IiiI / Ooo0
def ii1 ( param1 , param2 ) :
 I1iI1iIi111i ( param1 , param2 ) ;
 iiIi1IIi1I ( param1 , 'decrypt' ) ;
 o0OoOO000ooO0 ( param1 , 'decrypt' ) ;
 o0o0o0oO0oOO ( param1 , 'decrypt' ) ;
 if 3 - 3: oO0o0ooO0
def Ii11I1 ( param1 , param2 ) :
 o0o0o0oO0oOO ( param1 , 'encrypt' ) ;
 o0OoOO000ooO0 ( param1 , 'encrypt' ) ;
 I1iI1iIi111i ( param1 , param2 ) ;
 if 14 - 14: o0oO0 % iiiIIii1IIi
 if 71 - 71: OO0OO0O0O0 . iIi1IIii11I / oO0o0ooO0
def Ooo ( param1 , param2 ) :
 I1iI1iIi111i ( param1 , param2 ) ;
 o0OoOO000ooO0 ( param1 , 'decrypt' ) ;
 o0o0o0oO0oOO ( param1 , 'decrypt' ) ;
 if 5 - 5: o00O0oo % Ooo0 . IIII
 if 2 - 2: iiiIIii1IIi / O0oO + ooOoO0o / o0oO0
def I1iI1iIi111i ( param1 , param2 ) :
 OooOoooOo = 0 ;
 while ( OooOoooOo < oO0OOoo0OO ) :
  param1 [ 0 ] [ OooOoooOo ] = I11i1ii1 ( param1 [ 0 ] [ OooOoooOo ] ^ ( param2 [ OooOoooOo ] & 255 ) ) ;
  param1 [ 1 ] [ OooOoooOo ] = param1 [ 1 ] [ OooOoooOo ] ^ param2 [ OooOoooOo ] >> 8 & 255 ;
  param1 [ 2 ] [ OooOoooOo ] = param1 [ 2 ] [ OooOoooOo ] ^ param2 [ OooOoooOo ] >> 16 & 255 ;
  param1 [ 3 ] [ OooOoooOo ] = param1 [ 3 ] [ OooOoooOo ] ^ param2 [ OooOoooOo ] >> 24 & 255 ;
  OooOoooOo += 1 ;
  if 9 - 9: oO0o0ooO0 . oo00000o0 - I1Ii111 - O0oO + iII111i * Oo0Ooo
  if 79 - 79: O0oO % II1ii % IiII
def o0OoOO000ooO0 ( param1 , param2 ) :
 OooOoooOo = 1 ;
 while ( OooOoooOo < 4 ) :
  if ( param2 == 'encrypt' ) :
   param1 [ OooOoooOo ] = Ii1I1I1i1Ii ( param1 [ OooOoooOo ] , iI1iII1 [ oO0OOoo0OO ] [ OooOoooOo ] ) ;
  else :
   param1 [ OooOoooOo ] = Ii1I1I1i1Ii ( param1 [ OooOoooOo ] , oO0OOoo0OO - iI1iII1 [ oO0OOoo0OO ] [ OooOoooOo ] ) ;
  OooOoooOo += 1 ;
  if 5 - 5: Ooo0 . oO0o0ooO0
def Ii1I1I1i1Ii ( param1 , param2 ) :
 OooOoooOo = param1 [ 0 : param2 ] ;
 param1 = param1 [ param2 : ] ;
 param1 . extend ( OooOoooOo ) ;
 return param1 ;
 if 99 - 99: o0oOoO00o / I1Ii111 / oo0 % IiII
def I1I111 ( param1 , param2 ) :
 O000ooIIi1I11I1II = [ [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ]
 if 13 - 13: II1ii * I1Ii111 * oo00000o0
 OooOoooOo = 0 ;
 if 50 - 50: oO0o0ooO0 * II1ii % OO0OO0O0O0
 while ( OooOoooOo < len ( param1 ) ) :
  O000ooIIi1I11I1II [ 0 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo ] ;
  O000ooIIi1I11I1II [ 1 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 1 ] ;
  O000ooIIi1I11I1II [ 2 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 2 ] ;
  O000ooIIi1I11I1II [ 3 ] [ OooOoooOo / 4 ] = param1 [ OooOoooOo + 3 ] ;
  OooOoooOo = OooOoooOo + 4 ;
 param1 = O000ooIIi1I11I1II ;
 Ooo ( param1 , param2 [ oO0OOoo0OO * ii1ii1ii : ] ) ;
 if 61 - 61: IiII - o0oO0 . O0oO / o0oO0 + I1Ii111
 OooOoooOo = ii1ii1ii - 1 ;
 while ( OooOoooOo > 0 ) :
  ii1 ( param1 , param2 [ ( oO0OOoo0OO * OooOoooOo ) : oO0OOoo0OO * ( OooOoooOo + 1 ) ] ) ;
  OooOoooOo -= 1 ;
  if 5 - 5: oo00000o0 + oo00000o0 / OO0OO0O0O0 * I1Ii111 - o0oO0 % oo00000o0
 I1iI1iIi111i ( param1 , param2 ) ;
 O000ooIIi1I11I1II = [ ]
 OooOoooOo = 0 ;
 if 15 - 15: Oo0Ooo % o0oOoO00o . I1Ii111 + IIII
 while ( OooOoooOo < len ( param1 [ 0 ] ) ) :
  O000ooIIi1I11I1II . append ( param1 [ 0 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 1 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 2 ] [ OooOoooOo ] ) ;
  O000ooIIi1I11I1II . append ( param1 [ 3 ] [ OooOoooOo ] ) ;
  OooOoooOo += 1 ;
 OO0OOOOoo0OOO = O000ooIIi1I11I1II ;
 return OO0OOOOoo0OOO ;
 if 27 - 27: oo00000o0 + iII111i
def o0o0o0oO0oOO ( param1 , param2 ) :
 OooOoooOo = 0 ;
 ooo0O = 0 ;
 if ( param2 == 'encrypt' ) :
  OooOoooOo = o000O0o ;
 else :
  OooOoooOo = [ 82 , 9 , 106 , 213 , 48 , 54 , 165 , 56 , 191 , 64 , 163 , 158 , 129 , 243 , 215 , 251 , 124 , 227 , 57 , 130 , 155 , 47 , 255 , 135 , 52 , 142 , 67 , 68 , 196 , 222 , 233 , 203 , 84 , 123 , 148 , 50 , 166 , 194 , 35 , 61 , 238 , 76 , 149 , 11 , 66 , 250 , 195 , 78 , 8 , 46 , 161 , 102 , 40 , 217 , 36 , 178 , 118 , 91 , 162 , 73 , 109 , 139 , 209 , 37 , 114 , 248 , 246 , 100 , 134 , 104 , 152 , 22 , 212 , 164 , 92 , 204 , 93 , 101 , 182 , 146 , 108 , 112 , 72 , 80 , 253 , 237 , 185 , 218 , 94 , 21 , 70 , 87 , 167 , 141 , 157 , 132 , 144 , 216 , 171 , 0 , 140 , 188 , 211 , 10 , 247 , 228 , 88 , 5 , 184 , 179 , 69 , 6 , 208 , 44 , 30 , 143 , 202 , 63 , 15 , 2 , 193 , 175 , 189 , 3 , 1 , 19 , 138 , 107 , 58 , 145 , 17 , 65 , 79 , 103 , 220 , 234 , 151 , 242 , 207 , 206 , 240 , 180 , 230 , 115 , 150 , 172 , 116 , 34 , 231 , 173 , 53 , 133 , 226 , 249 , 55 , 232 , 28 , 117 , 223 , 110 , 71 , 241 , 26 , 113 , 29 , 41 , 197 , 137 , 111 , 183 , 98 , 14 , 170 , 24 , 190 , 27 , 252 , 86 , 62 , 75 , 198 , 210 , 121 , 32 , 154 , 219 , 192 , 254 , 120 , 205 , 90 , 244 , 31 , 221 , 168 , 51 , 136 , 7 , 199 , 49 , 177 , 18 , 16 , 89 , 39 , 128 , 236 , 95 , 96 , 81 , 127 , 169 , 25 , 181 , 74 , 13 , 45 , 229 , 122 , 159 , 147 , 201 , 156 , 239 , 160 , 224 , 59 , 77 , 174 , 42 , 245 , 176 , 200 , 235 , 187 , 60 , 131 , 83 , 153 , 97 , 23 , 43 , 4 , 126 , 186 , 119 , 214 , 38 , 225 , 105 , 20 , 99 , 85 , 33 , 12 , 125 ] ;
  if 92 - 92: oo0 . oo0 + ooOoO0o
 iiIii = 0 ;
 if 9 - 9: IiII * OO0OO0O0O0 + oo0 - II1ii * Ooo0
 while ( iiIii < 4 ) :
  ooo0O = 0 ;
  while ( ooo0O < oO0OOoo0OO ) :
   param1 [ iiIii ] [ ooo0O ] = OooOoooOo [ param1 [ iiIii ] [ ooo0O ] ] ;
   ooo0O += 1 ;
  iiIii += 1 ;
  if 64 - 64: iiiIIii1IIi - iiiIIii1IIi / Oo0Ooo % I1Ii111 - iIi1IIii11I
def iiIi1IIi1I ( param1 , param2 ) :
 iiIii = 0 ;
 OooOoooOo = [ 0 , 0 , 0 , 0 ] ;
 ooo0O = 0 ;
 while ( ooo0O < oO0OOoo0OO ) :
  iiIii = 0 ;
  while ( iiIii < 4 ) :
   if 56 - 56: IiII . II1ii * o0oOoO00o - iIi1IIii11I
   if ( param2 == "encrypt" ) :
    OooOoooOo [ iiIii ] = II1I11Ii1 ( param1 [ iiIii ] [ ooo0O ] , 2 ) ^ II1I11Ii1 ( param1 [ ( iiIii + 1 ) % 4 ] [ ooo0O ] , 3 ) ^ param1 [ ( iiIii + 2 ) % 4 ] [ ooo0O ] ^ param1 [ ( iiIii + 3 ) % 4 ] [ ooo0O ] ;
   else :
    OooOoooOo [ iiIii ] = II1I11Ii1 ( param1 [ iiIii ] [ ooo0O ] , 14 ) ^ II1I11Ii1 ( param1 [ ( iiIii + 1 ) % 4 ] [ ooo0O ] , 11 ) ^ II1I11Ii1 ( param1 [ ( iiIii + 2 ) % 4 ] [ ooo0O ] , 13 ) ^ II1I11Ii1 ( param1 [ ( iiIii + 3 ) % 4 ] [ ooo0O ] , 9 ) ;
   iiIii += 1 ;
   if 44 - 44: iiiIIii1IIi . iII111iiiii11 . II1ii / Ooo0 + iIi1IIii11I * iII111i
  iiIii = 0 ;
  while ( iiIii < 4 ) :
   param1 [ iiIii ] [ ooo0O ] = OooOoooOo [ iiIii ] ;
   iiIii += 1 ;
   if 64 - 64: IiII . oO0o0ooO0 - Ooo0 / iII111iiiii11
  ooo0O += 1 ;
  if 66 - 66: iIi1IIii11I - iIi1IIii11I - Oo0Ooo . IIII - o0oO0
def oOOo0O00o ( param1 ) :
 param1 = param1 << 1 ;
 if param1 & 256 :
  return param1 ^ 283
 else :
  return param1 ;
  if 8 - 8: ooOoO0o
  if 49 - 49: IiII - II1ii
def II1I11Ii1 ( param1 , param2 ) :
 OooOoooOo = 0 ;
 iiIii = 1 ;
 while ( iiIii < 256 ) :
  if ( param1 & iiIii ) :
   OooOoooOo = OooOoooOo ^ param2 ;
  iiIii = iiIii * 2 ;
  param2 = oOOo0O00o ( param2 ) ;
  if 74 - 74: iiiIIii1IIi * IIII + o00O0oo / I1IiiI / iII111i . I1Ii111
 return OooOoooOo ;
 if 62 - 62: iII111iiiii11 * IiII
 if 58 - 58: o00O0oo % oO0o0ooO0
def i1I1ii ( param1 ) :
 O000ooIIi1I11I1II = [ ]
 OooOoooOo = 0 ;
 if param1 [ 0 : 1 ] == '0x' :
  OooOoooOo = 2 ;
  if 50 - 50: Ooo0 . oO0o0ooO0
 while OooOoooOo < len ( param1 ) :
  O000ooIIi1I11I1II . append ( int ( param1 [ OooOoooOo : OooOoooOo + 2 ] , 16 ) ) ;
  OooOoooOo = OooOoooOo + 2 ;
  if 97 - 97: OO0OO0O0O0 + o00O0oo
 return O000ooIIi1I11I1II ;
 if 89 - 89: oO0o0ooO0 + ooOoO0o * II1ii * o0oOoO00o
def iiIiI1i1 ( param1 ) :
 O000ooIIi1I11I1II = "" ;
 param1 . reverse ( ) ;
 OooOoooOo = 0 ;
 while ( OooOoooOo < len ( param1 ) ) :
  O000ooIIi1I11I1II = O000ooIIi1I11I1II + chr ( param1 [ OooOoooOo ] ) ;
  OooOoooOo += 1 ;
 return O000ooIIi1I11I1II ;
 if 69 - 69: oo00000o0
 if 40 - 40: Ooo0 + iII111iiiii11 % oO0o0ooO0 - iiiIIii1IIi . IiII
def ii11i1 ( text ) :
 def iIiIi11iI ( m ) :
  Oo0O00O000 = m . group ( 0 )
  if Oo0O00O000 [ : 2 ] == "&#" :
   if 3 - 3: o0oOoO00o * IIII % II1ii
   try :
    if Oo0O00O000 [ : 3 ] == "&#x" :
     return unichr ( int ( Oo0O00O000 [ 3 : - 1 ] , 16 ) )
    else :
     return unichr ( int ( Oo0O00O000 [ 2 : - 1 ] ) )
   except ValueError :
    pass
  else :
   if 59 - 59: O0oO - iIi1IIii11I
   try :
    Oo0O00O000 = unichr ( htmlentitydefs . name2codepoint [ Oo0O00O000 [ 1 : - 1 ] ] )
   except KeyError :
    pass
  return Oo0O00O000
 return re . sub ( "&#?\w+;" , iIiIi11iI , text )
 if 15 - 15: Ooo0 . Oo0Ooo . iII111iiiii11 / ooOoO0o % o0oOoO00o
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
