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
 if 49 - 49: I11i11Ii = xbmc . translatePath ( os . path . join ( I11i11Ii , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/kenh108.jpg' , I11i11Ii )
 if 49 - 49: oO00oOo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i11Ii )
 if 49 - 49: OOOo0 = xbmcgui . WindowDialog ( )
 if 49 - 49: OOOo0 . addControl ( oO00oOo )
 if 49 - 49: OOOo0 . doModal ( )
 if 54 - 54: i1 - o0 * i1oOo0OoO * iIIIiiIIiiiIi % Oo
 o0O = [
 { 'label' : 'Recently Updated Videos' , 'path' : '%s/updated/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=recently_updated&page=%s' ) , 1 ) } ,
 { 'label' : 'Recently Added Videos' , 'path' : '%s/added/%s/%s' % ( ii , urllib . quote_plus ( 'http://www.lsb-movies.net/kenh108/index.php?do=list&type=more&page=%s' ) , 1 ) } ,
 { 'label' : 'Search' , 'path' : '%s/search' % ii }
 ]
 return oo000 . finish ( o0O )
 if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
@ oo000 . route ( '/updated/<murl>/<page>' )
def O0oOO0o0 ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'updated' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
@ oo000 . route ( '/added/<murl>/<page>' )
def o0oOoO00o ( murl , page ) :
 o0O = i1ii1iIII ( murl , page , 'added' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 43 - 43: O0OOo . OO0OO0O0O0
@ oo000 . route ( '/search/' )
def O0Oooo00 ( ) :
 Ooo0 = oo000 . keyboard ( heading = 'Tìm kiếm' )
 if Ooo0 :
  oo00000o0 = '%s/search/%s' % ( ii , urllib . quote_plus ( Ooo0 ) )
  oo000 . redirect ( oo00000o0 )
  if 34 - 34: o00 % i1 % iiiIIii1IIi % o00 * o00ooo0 / Oo
@ oo000 . route ( '/search/<search_string>' )
def Iiii ( search_string ) :
 o0O = OOO0O ( search_string , 'search' )
 if xbmc . getSkinDir ( ) == 'skin.xeebo' and oo000 . get_setting ( 'thumbview' , bool ) :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
 return oo000 . finish ( o0O )
 if 94 - 94: O0OOo
@ oo000 . route ( '/mirrors/<murl>' )
def IiI1i ( murl ) :
 o0O = [ ]
 for OOo0o0 in O0OoOoo00o ( murl ) :
  iiiI11 = { }
  iiiI11 [ "label" ] = OOo0o0 [ "name" ] . strip ( )
  OOooO = str ( uuid . uuid1 ( ) )
  OOoO00o = oo000 . get_storage ( OOooO )
  OOoO00o [ "list" ] = OOo0o0 [ "eps" ]
  iiiI11 [ "path" ] = '%s/eps/%s' % ( ii , urllib . quote_plus ( OOooO ) )
  o0O . append ( iiiI11 )
 return oo000 . finish ( o0O )
 if 9 - 9: o0 - II1i % I1IiiI % iII111iiiii11
@ oo000 . route ( '/eps/<eps_list>' )
def i1iIIi1 ( eps_list ) :
 o0O = [ ]
 for ii11iIi1I in oo000 . get_storage ( eps_list ) [ "list" ] :
  iiiI11 = { }
  iiiI11 [ "label" ] = ii11iIi1I [ "name" ] . strip ( )
  iiiI11 [ "is_playable" ] = True
  iiiI11 [ "path" ] = '%s/play/%s' % ( ii , urllib . quote_plus ( ii11iIi1I [ "url" ] ) )
  o0O . append ( iiiI11 )
 return oo000 . finish ( o0O )
 if 6 - 6: Oo * o00ooo0
@ oo000 . route ( '/play/<url>' )
def O00O0O0O0 ( url ) :
 ooO0O = xbmcgui . DialogProgress ( )
 ooO0O . create ( 'kenh108.com' , 'Loading video. Please wait...' )
 oo000 . set_resolved_url ( oo ( url ) )
 ooO0O . close ( )
 del ooO0O
 if 28 - 28: iiiIIii1IIi - I1IiiI
def oo ( url ) :
 OO = oO0O ( url )
 if "proxy.link" in OO :
  OOoO000O0OO = re . compile ( 'proxy.link=kenh108\*(.+?)&' ) . findall ( OO ) [ 0 ]
  iiI1IiI = II ( OOoO000O0OO )
  print iiI1IiI
 if "youtube" in iiI1IiI :
  OOoO000O0OO = re . compile ( '(youtu\.be\/|youtube-nocookie\.com\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v|user)\/))([^\?&"\'>]+)' ) . findall ( iiI1IiI )
  ooOoOoo0O = OOoO000O0OO [ 0 ] [ len ( OOoO000O0OO [ 0 ] ) - 1 ] . replace ( 'v/' , '' )
  return 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % ooOoOoo0O
 if "picasaweb" in iiI1IiI :
  OooO0 = 480
  if oo000 . get_setting ( 'HQ' , bool ) : OooO0 = 720
  II11iiii1Ii = ""
  if "lh/photo" not in iiI1IiI :
   for OO0o , Ooo , O0o0Oo in re . compile ( 'https://picasaweb.google.com/(\d+).*?\?authkey=(.+?)#(\d+)' ) . findall ( iiI1IiI ) :
    Oo00OOOOO = "https://picasaweb.google.com/data/feed/api/user/%s/photoid/%s?authkey=%s&alt=json" % ( OO0o , O0o0Oo , Ooo )
    O0O = json . loads ( urllib2 . urlopen ( Oo00OOOOO ) . read ( ) ) [ "feed" ] [ "media$group" ] [ "media$content" ]
    for O00o0OO in O0O :
     if ( O00o0OO [ "type" ] == "video/mpeg4" ) and ( int ( O00o0OO [ "height" ] ) <= OooO0 ) :
      II11iiii1Ii = O00o0OO [ "url" ]
  else :
   OO = urllib2 . urlopen ( iiI1IiI ) . read ( )
   Oo00OOOOO = re . compile ( '(https://picasaweb.google.com/data/feed/tiny/user/\d+/photoid/\d+\?alt=jsonm&gupi=.+?)"' ) . findall ( OO ) [ 0 ]
   OO = urllib2 . urlopen ( Oo00OOOOO ) . read ( )
   O0O = json . loads ( OO ) [ "feed" ] [ "media" ] [ "content" ]
   for O00o0OO in O0O :
    if ( O00o0OO [ "type" ] == "video/mpeg4" ) and ( int ( O00o0OO [ "height" ] ) <= OooO0 ) :
     II11iiii1Ii = O00o0OO [ "url" ]
  return II11iiii1Ii
  if 44 - 44: o00 / OO0OO0O0O0 % I1IiiI * I1Ii111 + i1oOo0OoO
def i1ii1iIII ( url , page , route_name ) :
 Ii1I = int ( page ) + 1
 OO = oO0O ( url % page )
 OOoO000O0OO = re . compile ( '<div class="movie_pix" [^>]* url\((.+?)\) [^>]*><a href="(.+?)"><img [^>]*></a></div><div class="movietitle"><a [^>]*>(.+?)<div class="listmovies_secondtitle" [^>]*>(.*?)</div></a>' ) . findall ( OO )
 o0O = [ ]
 for Oo0o0 , III1ii1iII , oo0oooooO0 , i11Iiii in OOoO000O0OO :
  iiiI11 = { }
  iI = ""
  if "<sup>" in oo0oooooO0 :
   iI = I1i1I1II ( re . compile ( '<sup>(.+?)</sup>' ) . findall ( oo0oooooO0 ) [ 0 ] ) . encode ( "utf8" )
  i1IiIiiI = oo0oooooO0 . split ( "<" ) [ 0 ] . strip ( )
  i1IiIiiI + iI
  iiiI11 [ "label" ] = "%s - %s (%s)" % ( i1IiIiiI , i11Iiii , iI )
  iiiI11 [ "thumbnail" ] = Oo0o0
  iiiI11 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://www.lsb-movies.net/kenh108/" + III1ii1iII . replace ( "/phim/" , "/xem-phim-online/" ) ) )
  o0O . append ( iiiI11 )
 if len ( o0O ) == oOOo :
  o0O . append ( { 'label' : 'Next >>' , 'path' : '%s/%s/%s/%s' % ( ii , route_name , urllib . quote_plus ( url ) , Ii1I ) , 'thumbnail' : 'http://icons.iconarchive.com/icons/rafiqul-hassan/blogger/128/Arrow-Next-icon.png' } )
 return o0O
 if 31 - 31: II1i . II1i - iII111i / iIIIiiIIiiiIi + O0OOo * o0
def OOO0O ( search_string , route_name ) :
 OO = O0ooOooooO ( search_string )
 OOoO000O0OO = re . compile ( '<div class="searchresults_image" [^>]*><a href="(index.php\?do=xem&mid=\d+)&image=(.+?)" alt=(.+?)>' ) . findall ( OO )
 o0O = [ ]
 for III1ii1iII , Oo0o0 , o00O in OOoO000O0OO :
  iiiI11 = { }
  iiiI11 [ "label" ] = o00O
  iiiI11 [ "thumbnail" ] = Oo0o0
  iiiI11 [ "path" ] = '%s/%s/%s' % ( ii , "mirrors" , urllib . quote_plus ( "http://www.lsb-movies.net/kenh108/" + III1ii1iII . replace ( "/phim/" , "/xem-phim-online/" ) ) )
  o0O . append ( iiiI11 )
 return o0O
 if 69 - 69: I1Ii111 % Oo0oO0ooo - iII111i + Oo0oO0ooo - OO0OO0O0O0 % iII111iiiii11
def O0OoOoo00o ( murl ) :
 OO = oO0O ( murl )
 Iii111II = re . compile ( '<div class="noidung_servers">(.+?</div></div>)' ) . findall ( OO ) [ 0 ] . replace ( "</div></div>" , "<br>" )
 OOoO000O0OO = re . compile ( '<div class="noidung_servername">(.+?)</div>(.+?)<br>' ) . findall ( Iii111II )
 iiii11I = re . compile ( '<title>(.+?)</title>' ) . findall ( OO ) [ 0 ] . replace ( "K&#202;NH 108 - " , "" )
 Ooo0OO0oOO = [ ]
 for ii11i1 , IIIii1II1II in OOoO000O0OO :
  i1I1iI = [ ]
  for oo0OooOOo0 , o0OO00oO in re . compile ( '<a class="tapphim" href="(.+?)">(.+?)</a>' ) . findall ( IIIii1II1II ) :
   ii11iIi1I = { }
   ii11iIi1I [ "url" ] = "http://www.lsb-movies.net/kenh108/" + oo0OooOOo0
   ii11iIi1I [ "name" ] = "Part %s - %s" % ( o0OO00oO , I1i1I1II ( iiii11I . strip ( ) . decode ( "utf8" ) ) )
   i1I1iI . append ( ii11iIi1I )
  OOo0o0 = { }
  OOo0o0 [ "name" ] = re . sub ( '<[^<]+?>' , '' , I1i1I1II ( ii11i1 ) ) . encode ( "utf8" )
  OOo0o0 [ "eps" ] = i1I1iI
  Ooo0OO0oOO . append ( OOo0o0 )
 return Ooo0OO0oOO
 if 39 - 39: o00 - i1 * iIIIiiIIiiiIi % iII111i * i1 % i1
@ oo000 . cached ( TTL = 60 )
def oO0O ( url ) :
 OoOOOOO = urllib2 . Request ( url )
 OoOOOOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 OoOOOOO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 OoOOOOO . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 OoOOOOO . add_header ( 'Referer' , 'http://www.luongson.net/kenh108/index.php' )
 iIi1i111II = urllib2 . urlopen ( OoOOOOO )
 OoOO00O = iIi1i111II . read ( )
 iIi1i111II . close ( )
 if 53 - 53: iIIIiiIIiiiIi % iII111iiiii11 - Oo
 if 97 - 97: I1Ii111 % o00 * o00
 OoOO00O = '' . join ( OoOO00O . splitlines ( ) ) . replace ( '\'' , '"' )
 OoOO00O = OoOO00O . replace ( '\n' , '' )
 OoOO00O = OoOO00O . replace ( '\t' , '' )
 OoOO00O = re . sub ( '  +' , ' ' , OoOO00O )
 OoOO00O = OoOO00O . replace ( '> <' , '><' )
 return OoOO00O
 if 39 - 39: II1i % o00
@ oo000 . cached ( TTL = 60 )
def O0ooOooooO ( search_string ) :
 OoOOOOO = urllib2 . Request ( "http://www.lsb-movies.org/kenh108/index.php?do=timkiem" )
 OoOOOOO . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36' )
 OoOOOOO . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' )
 OoOOOOO . add_header ( 'Accept-Encoding' , 'gzip, deflate, sdch' )
 OoOOOOO . add_header ( 'Referer' , 'http://www.luongson.net/kenh108/index.php' )
 i111IiI1I = { "search_this" : search_string }
 iIi1i111II = urllib2 . urlopen ( OoOOOOO , urllib . urlencode ( i111IiI1I ) )
 OoOO00O = iIi1i111II . read ( )
 iIi1i111II . close ( )
 if 70 - 70: II1i . i1oOo0OoO / iII111i . II1i - OO0OO0O0O0 / o00
 if 62 - 62: iiiIIii1IIi * Oo
 OoOO00O = '' . join ( OoOO00O . splitlines ( ) ) . replace ( '\'' , '"' )
 OoOO00O = OoOO00O . replace ( '\n' , '' )
 OoOO00O = OoOO00O . replace ( '\t' , '' )
 OoOO00O = re . sub ( '  +' , ' ' , OoOO00O )
 OoOO00O = OoOO00O . replace ( '> <' , '><' )
 return OoOO00O
 if 26 - 26: o00ooo0 . Oo0oO0ooo
 if 68 - 68: iIIIiiIIiiiIi
IIi1iIIiI = [ 1 , 2 , 4 , 8 , 16 , 32 , 64 , 128 , 27 , 54 , 108 , 216 , 171 , 77 , 154 , 47 , 94 , 188 , 99 , 198 , 151 , 53 , 106 , 212 , 179 , 125 , 250 , 239 , 197 , 145 ] ;
O0OoO = [ 99 , 124 , 119 , 123 , 242 , 107 , 111 , 197 , 48 , 1 , 103 , 43 , 254 , 215 , 171 , 118 , 202 , 130 , 201 , 125 , 250 , 89 , 71 , 240 , 173 , 212 , 162 , 175 , 156 , 164 , 114 , 192 , 183 , 253 , 147 , 38 , 54 , 63 , 247 , 204 , 52 , 165 , 229 , 241 , 113 , 216 , 49 , 21 , 4 , 199 , 35 , 195 , 24 , 150 , 5 , 154 , 7 , 18 , 128 , 226 , 235 , 39 , 178 , 117 , 9 , 131 , 44 , 26 , 27 , 110 , 90 , 160 , 82 , 59 , 214 , 179 , 41 , 227 , 47 , 132 , 83 , 209 , 0 , 237 , 32 , 252 , 177 , 91 , 106 , 203 , 190 , 57 , 74 , 76 , 88 , 207 , 208 , 239 , 170 , 251 , 67 , 77 , 51 , 133 , 69 , 249 , 2 , 127 , 80 , 60 , 159 , 168 , 81 , 163 , 64 , 143 , 146 , 157 , 56 , 245 , 188 , 182 , 218 , 33 , 16 , 255 , 243 , 210 , 205 , 12 , 19 , 236 , 95 , 151 , 68 , 23 , 196 , 167 , 126 , 61 , 100 , 93 , 25 , 115 , 96 , 129 , 79 , 220 , 34 , 42 , 144 , 136 , 70 , 238 , 184 , 20 , 222 , 94 , 11 , 219 , 224 , 50 , 58 , 10 , 73 , 6 , 36 , 92 , 194 , 211 , 172 , 98 , 145 , 149 , 228 , 121 , 231 , 200 , 55 , 109 , 141 , 213 , 78 , 169 , 108 , 86 , 244 , 234 , 101 , 122 , 174 , 8 , 186 , 120 , 37 , 46 , 28 , 166 , 180 , 198 , 232 , 221 , 116 , 31 , 75 , 189 , 139 , 138 , 112 , 62 , 181 , 102 , 72 , 3 , 246 , 14 , 97 , 53 , 87 , 185 , 134 , 193 , 29 , 158 , 225 , 248 , 152 , 17 , 105 , 217 , 142 , 148 , 155 , 30 , 135 , 233 , 206 , 85 , 40 , 223 , 140 , 161 , 137 , 13 , 191 , 230 , 66 , 104 , 65 , 153 , 45 , 15 , 176 , 84 , 187 , 22 ] ;
OOI1III = [ 0 , 0 , 0 , 0 , [ 0 , 1 , 2 , 3 ] , 0 , [ 0 , 1 , 2 , 3 ] , 0 , [ 0 , 1 , 3 , 4 ] ] ;
OO0O0OoOO0 = 4 ;
iiiI1I11i1 = 6 ;
IIi1i11111 = 12 ;
if 81 - 81: Oo0Ooo % Oo - ooOoO0o
def II ( param1 ) :
 O0ooo0O0oo0 = [ ]
 oo0oOo = [ ]
 o000O0o = iI1iII1 ( param1 ) ;
 oO0OOoo0OO = 16 ;
 O0 = [ 1966101078 , 1516336945 , 1263424345 , 1379365717 , 909404232 , 0 , 374550836L , 1278363141L , 125572444L , 1431004681L , 1669271105L , 1669271105L , - 1784093795L , - 644176488L , - 555306812L , - 1951541555L , - 388835188L , - 1951541555L , 680883823L , - 250620937L , 803824435L , - 1539000834L , 1284926834L , - 952386625L , 542348429L , - 782481542L , - 21683127L , 1525780919L , 375913669L , - 782481542L , - 93462979L , 724670791L , - 712721138L , - 1888146247L , - 1726820228L , 1213110022L , - 1790971499L , - 1106351918L , 1804260828L , - 452986523L , 2112694553L , 899923487L , 1437203323L , - 341339223L , - 2144516491L , 1691533072L , 423597577L , 748431382L , 316155343L , - 109070746L , 2035478547L , 494948099L ]
 if 25 - 25: IiII
 Ii1i = ( len ( o000O0o ) / oO0OOoo0OO ) - 1 ;
 if 15 - 15: o00 . iiiIIii1IIi . iII111iiiii11 / Oo0Ooo - II1i . I1IiiI
 while Ii1i > 0 :
  oo0oOo = i1O0OoO0o ( o000O0o [ Ii1i * oO0OOoo0OO : ( Ii1i + 1 ) * oO0OOoo0OO ] , O0 ) ;
  O0ooo0O0oo0 = oo0oOo + ( O0ooo0O0oo0 )
  Ii1i -= 1 ;
  if 79 - 79: Oo - OO0OO0O0O0 * iIIIiiIIiiiIi + Oo % OO0OO0O0O0 * OO0OO0O0O0
 oOOo0 = i1O0OoO0o ( o000O0o [ 0 : int ( oO0OOoo0OO ) ] , O0 )
 if 54 - 54: OO0OO0O0O0 - o00 % ooOoO0o
 O0ooo0O0oo0 = oOOo0 + O0ooo0O0oo0 ;
 if 77 - 77: Oo / o0 / iIIIiiIIiiiIi + iIIIiiIIiiiIi . ooOoO0o
 O0ooo0O0oo0 = ii1ii11IIIiiI ( O0ooo0O0oo0 ) ;
 if 67 - 67: o00O0oo * I1Ii111 * IiII + ooOoO0o / I1IiiI
 return O0ooo0O0oo0 . split ( '\0' ) [ 0 ] ;
 if 11 - 11: II1i + o00ooo0 - O0OOo * I1Ii111 % Oo0Ooo - Oo0oO0ooo
 if 83 - 83: o00O0oo / o0
def iIIiIi1iIII1 ( x ) :
 x = 0xffffffff & x
 if x > 0x7fffffff :
  return - ( ~ ( x - 1 ) & 0xffffffff )
 else : return x
 if 78 - 78: OO0OO0O0O0 . I1Ii111 . i1 % ooOoO0o
def i1iIi ( param1 ) :
 ooOOoooooo = [ ]
 II1I = 0 ;
 while ( II1I < len ( param1 ) ) :
  ooOOoooooo . append ( ord ( param1 [ II1I ] ) ) ;
  II1I += 1 ;
  if 84 - 84: o00 . Oo0Ooo . o00 * IiII - o00O0oo
 return ooOOoooooo ;
 if 42 - 42: Oo0Ooo
def ii1ii11IIIiiI ( param1 ) :
 ooOOoooooo = ''
 II1I = 0 ;
 while ( II1I < len ( param1 ) ) :
  ooOOoooooo = ooOOoooooo + chr ( param1 [ II1I ] ) ;
  II1I += 1 ;
 return ooOOoooooo ;
 if 33 - 33: o00ooo0 - OO0OO0O0O0 * I1IiiI * iII111i - i1oOo0OoO
def iiIiI ( param1 ) :
 ooOOoooooo = [ [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ]
 II1I = 0 ;
 while ( II1I < len ( param1 ) ) :
  ooOOoooooo [ 0 ] [ II1I / 4 ] = param1 [ II1I ] ;
  ooOOoooooo [ 1 ] [ II1I / 4 ] = param1 [ II1I + 1 ] ;
  ooOOoooooo [ 2 ] [ II1I / 4 ] = param1 [ II1I + 2 ] ;
  ooOOoooooo [ 3 ] [ II1I / 4 ] = param1 [ II1I + 3 ] ;
  II1I = II1I + 4 ;
 return ooOOoooooo ;
 if 91 - 91: o00ooo0 % I1IiiI % iiiIIii1IIi
 if 20 - 20: ooOoO0o % II1i / II1i + II1i
def III1IiiI ( param1 ) :
 ooOOoooooo = [ ]
 II1I = 0 ;
 while ( II1I < len ( param1 [ 0 ] ) ) :
  ooOOoooooo . append ( param1 [ 0 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 1 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 2 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 3 ] [ II1I ] ) ;
  II1I += 1 ;
 return ooOOoooooo ;
 if 31 - 31: iII111i . o0
 if 46 - 46: o00ooo0
def IIIII11I1IiI ( param1 , param2 ) :
 i1I ( param1 , param2 ) ;
 OoOO ( param1 , 'decrypt' ) ;
 ooOOO0 ( param1 , 'decrypt' ) ;
 o0o ( param1 , 'decrypt' ) ;
 if 73 - 73: o00 * IiII + o0 . O0OOo
def o0oO00000 ( param1 , param2 ) :
 o0o ( param1 , 'encrypt' ) ;
 ooOOO0 ( param1 , 'encrypt' ) ;
 i1I ( param1 , param2 ) ;
 if 69 - 69: iIIIiiIIiiiIi - i1oOo0OoO + I1IiiI / Oo0oO0ooo
 if 49 - 49: OO0OO0O0O0 . o00ooo0
def I1iI1iIi111i ( param1 , param2 ) :
 i1I ( param1 , param2 ) ;
 ooOOO0 ( param1 , 'decrypt' ) ;
 o0o ( param1 , 'decrypt' ) ;
 if 44 - 44: I1IiiI % i1 + o00O0oo
 if 45 - 45: o00ooo0 / o00ooo0 + Oo0oO0ooo + O0OOo
def i1I ( param1 , param2 ) :
 II1I = 0 ;
 while ( II1I < OO0O0OoOO0 ) :
  param1 [ 0 ] [ II1I ] = iIIiIi1iIII1 ( param1 [ 0 ] [ II1I ] ^ ( param2 [ II1I ] & 255 ) ) ;
  param1 [ 1 ] [ II1I ] = param1 [ 1 ] [ II1I ] ^ param2 [ II1I ] >> 8 & 255 ;
  param1 [ 2 ] [ II1I ] = param1 [ 2 ] [ II1I ] ^ param2 [ II1I ] >> 16 & 255 ;
  param1 [ 3 ] [ II1I ] = param1 [ 3 ] [ II1I ] ^ param2 [ II1I ] >> 24 & 255 ;
  II1I += 1 ;
  if 47 - 47: iII111i + O0OOo
  if 82 - 82: i1 . o00 - iiiIIii1IIi - o00 * i1
def ooOOO0 ( param1 , param2 ) :
 II1I = 1 ;
 while ( II1I < 4 ) :
  if ( param2 == 'encrypt' ) :
   param1 [ II1I ] = ooO0oOOooOo0 ( param1 [ II1I ] , OOI1III [ OO0O0OoOO0 ] [ II1I ] ) ;
  else :
   param1 [ II1I ] = ooO0oOOooOo0 ( param1 [ II1I ] , OO0O0OoOO0 - OOI1III [ OO0O0OoOO0 ] [ II1I ] ) ;
  II1I += 1 ;
  if 38 - 38: Oo0oO0ooo
def ooO0oOOooOo0 ( param1 , param2 ) :
 II1I = param1 [ 0 : param2 ] ;
 param1 = param1 [ param2 : ] ;
 param1 . extend ( II1I ) ;
 return param1 ;
 if 84 - 84: iiiIIii1IIi % o00ooo0 / iiiIIii1IIi % o00O0oo
def i1O0OoO0o ( param1 , param2 ) :
 ooOOoooooo = [ [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] , [ 0 , 0 , 0 , 0 ] ]
 if 45 - 45: OO0OO0O0O0
 II1I = 0 ;
 if 26 - 26: o00O0oo - iiiIIii1IIi - o0 / iIIIiiIIiiiIi . Oo % iiiIIii1IIi
 while ( II1I < len ( param1 ) ) :
  ooOOoooooo [ 0 ] [ II1I / 4 ] = param1 [ II1I ] ;
  ooOOoooooo [ 1 ] [ II1I / 4 ] = param1 [ II1I + 1 ] ;
  ooOOoooooo [ 2 ] [ II1I / 4 ] = param1 [ II1I + 2 ] ;
  ooOOoooooo [ 3 ] [ II1I / 4 ] = param1 [ II1I + 3 ] ;
  II1I = II1I + 4 ;
 param1 = ooOOoooooo ;
 I1iI1iIi111i ( param1 , param2 [ OO0O0OoOO0 * IIi1i11111 : ] ) ;
 if 91 - 91: iII111i . iiiIIii1IIi / I1Ii111 + I1IiiI
 II1I = IIi1i11111 - 1 ;
 while ( II1I > 0 ) :
  IIIII11I1IiI ( param1 , param2 [ ( OO0O0OoOO0 * II1I ) : OO0O0OoOO0 * ( II1I + 1 ) ] ) ;
  II1I -= 1 ;
  if 42 - 42: O0OOo . iII111i . O0OOo - IiII
 i1I ( param1 , param2 ) ;
 ooOOoooooo = [ ]
 II1I = 0 ;
 if 40 - 40: O0OOo - Oo0Ooo / II1i
 while ( II1I < len ( param1 [ 0 ] ) ) :
  ooOOoooooo . append ( param1 [ 0 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 1 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 2 ] [ II1I ] ) ;
  ooOOoooooo . append ( param1 [ 3 ] [ II1I ] ) ;
  II1I += 1 ;
 I11iiI1i1 = ooOOoooooo ;
 return I11iiI1i1 ;
 if 47 - 47: o00ooo0 - II1i . i1 + iII111iiiii11 . Oo0Ooo
def o0o ( param1 , param2 ) :
 II1I = 0 ;
 oo0oOo = 0 ;
 if ( param2 == 'encrypt' ) :
  II1I = O0OoO ;
 else :
  II1I = [ 82 , 9 , 106 , 213 , 48 , 54 , 165 , 56 , 191 , 64 , 163 , 158 , 129 , 243 , 215 , 251 , 124 , 227 , 57 , 130 , 155 , 47 , 255 , 135 , 52 , 142 , 67 , 68 , 196 , 222 , 233 , 203 , 84 , 123 , 148 , 50 , 166 , 194 , 35 , 61 , 238 , 76 , 149 , 11 , 66 , 250 , 195 , 78 , 8 , 46 , 161 , 102 , 40 , 217 , 36 , 178 , 118 , 91 , 162 , 73 , 109 , 139 , 209 , 37 , 114 , 248 , 246 , 100 , 134 , 104 , 152 , 22 , 212 , 164 , 92 , 204 , 93 , 101 , 182 , 146 , 108 , 112 , 72 , 80 , 253 , 237 , 185 , 218 , 94 , 21 , 70 , 87 , 167 , 141 , 157 , 132 , 144 , 216 , 171 , 0 , 140 , 188 , 211 , 10 , 247 , 228 , 88 , 5 , 184 , 179 , 69 , 6 , 208 , 44 , 30 , 143 , 202 , 63 , 15 , 2 , 193 , 175 , 189 , 3 , 1 , 19 , 138 , 107 , 58 , 145 , 17 , 65 , 79 , 103 , 220 , 234 , 151 , 242 , 207 , 206 , 240 , 180 , 230 , 115 , 150 , 172 , 116 , 34 , 231 , 173 , 53 , 133 , 226 , 249 , 55 , 232 , 28 , 117 , 223 , 110 , 71 , 241 , 26 , 113 , 29 , 41 , 197 , 137 , 111 , 183 , 98 , 14 , 170 , 24 , 190 , 27 , 252 , 86 , 62 , 75 , 198 , 210 , 121 , 32 , 154 , 219 , 192 , 254 , 120 , 205 , 90 , 244 , 31 , 221 , 168 , 51 , 136 , 7 , 199 , 49 , 177 , 18 , 16 , 89 , 39 , 128 , 236 , 95 , 96 , 81 , 127 , 169 , 25 , 181 , 74 , 13 , 45 , 229 , 122 , 159 , 147 , 201 , 156 , 239 , 160 , 224 , 59 , 77 , 174 , 42 , 245 , 176 , 200 , 235 , 187 , 60 , 131 , 83 , 153 , 97 , 23 , 43 , 4 , 126 , 186 , 119 , 214 , 38 , 225 , 105 , 20 , 99 , 85 , 33 , 12 , 125 ] ;
  if 94 - 94: iII111i * II1i / i1oOo0OoO / II1i
 O0ooo0O0oo0 = 0 ;
 if 87 - 87: i1oOo0OoO . o00
 while ( O0ooo0O0oo0 < 4 ) :
  oo0oOo = 0 ;
  while ( oo0oOo < OO0O0OoOO0 ) :
   param1 [ O0ooo0O0oo0 ] [ oo0oOo ] = II1I [ param1 [ O0ooo0O0oo0 ] [ oo0oOo ] ] ;
   oo0oOo += 1 ;
  O0ooo0O0oo0 += 1 ;
  if 75 - 75: O0OOo + Oo + iII111i * o00O0oo % I1Ii111 . o00ooo0
def OoOO ( param1 , param2 ) :
 O0ooo0O0oo0 = 0 ;
 II1I = [ 0 , 0 , 0 , 0 ] ;
 oo0oOo = 0 ;
 while ( oo0oOo < OO0O0OoOO0 ) :
  O0ooo0O0oo0 = 0 ;
  while ( O0ooo0O0oo0 < 4 ) :
   if 55 - 55: ooOoO0o . o0
   if ( param2 == "encrypt" ) :
    II1I [ O0ooo0O0oo0 ] = oOo0O0o00o ( param1 [ O0ooo0O0oo0 ] [ oo0oOo ] , 2 ) ^ oOo0O0o00o ( param1 [ ( O0ooo0O0oo0 + 1 ) % 4 ] [ oo0oOo ] , 3 ) ^ param1 [ ( O0ooo0O0oo0 + 2 ) % 4 ] [ oo0oOo ] ^ param1 [ ( O0ooo0O0oo0 + 3 ) % 4 ] [ oo0oOo ] ;
   else :
    II1I [ O0ooo0O0oo0 ] = oOo0O0o00o ( param1 [ O0ooo0O0oo0 ] [ oo0oOo ] , 14 ) ^ oOo0O0o00o ( param1 [ ( O0ooo0O0oo0 + 1 ) % 4 ] [ oo0oOo ] , 11 ) ^ oOo0O0o00o ( param1 [ ( O0ooo0O0oo0 + 2 ) % 4 ] [ oo0oOo ] , 13 ) ^ oOo0O0o00o ( param1 [ ( O0ooo0O0oo0 + 3 ) % 4 ] [ oo0oOo ] , 9 ) ;
   O0ooo0O0oo0 += 1 ;
   if 64 - 64: ooOoO0o % iiiIIii1IIi * I1Ii111
  O0ooo0O0oo0 = 0 ;
  while ( O0ooo0O0oo0 < 4 ) :
   param1 [ O0ooo0O0oo0 ] [ oo0oOo ] = II1I [ O0ooo0O0oo0 ] ;
   O0ooo0O0oo0 += 1 ;
   if 79 - 79: OO0OO0O0O0
  oo0oOo += 1 ;
  if 78 - 78: IiII + ooOoO0o - Oo0oO0ooo
def IIIIii1I ( param1 ) :
 param1 = param1 << 1 ;
 if param1 & 256 :
  return param1 ^ 283
 else :
  return param1 ;
  if 39 - 39: i1 / O0OOo + Oo0oO0ooo / Oo
  if 13 - 13: o00 + OO0OO0O0O0 + o00ooo0 % o0 / iII111i . o00
def oOo0O0o00o ( param1 , param2 ) :
 II1I = 0 ;
 O0ooo0O0oo0 = 1 ;
 while ( O0ooo0O0oo0 < 256 ) :
  if ( param1 & O0ooo0O0oo0 ) :
   II1I = II1I ^ param2 ;
  O0ooo0O0oo0 = O0ooo0O0oo0 * 2 ;
  param2 = IIIIii1I ( param2 ) ;
  if 86 - 86: I1Ii111 * iII111i % I1IiiI . II1i . Oo0Ooo
 return II1I ;
 if 56 - 56: IiII % OO0OO0O0O0 - o0
 if 100 - 100: II1i - OO0OO0O0O0 % I1Ii111 * ooOoO0o + o0
def iI1iII1 ( param1 ) :
 ooOOoooooo = [ ]
 II1I = 0 ;
 if param1 [ 0 : 1 ] == '0x' :
  II1I = 2 ;
  if 88 - 88: iII111iiiii11 - iIIIiiIIiiiIi * OO0OO0O0O0 * iII111iiiii11 . iII111iiiii11
 while II1I < len ( param1 ) :
  ooOOoooooo . append ( int ( param1 [ II1I : II1I + 2 ] , 16 ) ) ;
  II1I = II1I + 2 ;
  if 33 - 33: Oo0oO0ooo + o00ooo0 * I1Ii111 / iiiIIii1IIi - o0
 return ooOOoooooo ;
 if 54 - 54: Oo0oO0ooo / ooOoO0o . I1Ii111 % o00ooo0
def OoO0OOOOo0O ( param1 ) :
 ooOOoooooo = "" ;
 param1 . reverse ( ) ;
 II1I = 0 ;
 while ( II1I < len ( param1 ) ) :
  ooOOoooooo = ooOOoooooo + chr ( param1 [ II1I ] ) ;
  II1I += 1 ;
 return ooOOoooooo ;
 if 81 - 81: OO0OO0O0O0 / iIIIiiIIiiiIi . I1IiiI + o0 - o00O0oo
 if 74 - 74: iiiIIii1IIi * IiII + Oo / I1IiiI / i1 . i1oOo0OoO
def I1i1I1II ( text ) :
 def oooOo0OOOoo0 ( m ) :
  OOoO = m . group ( 0 )
  if OOoO [ : 2 ] == "&#" :
   if 89 - 89: iII111i + iIIIiiIIiiiIi * o00O0oo * II1i
   try :
    if OOoO [ : 3 ] == "&#x" :
     return unichr ( int ( OOoO [ 3 : - 1 ] , 16 ) )
    else :
     return unichr ( int ( OOoO [ 2 : - 1 ] ) )
   except ValueError :
    pass
  else :
   if 37 - 37: iII111iiiii11 - OO0OO0O0O0 - iII111i
   try :
    OOoO = unichr ( htmlentitydefs . name2codepoint [ OOoO [ 1 : - 1 ] ] )
   except KeyError :
    pass
  return OOoO
 return re . sub ( "&#?\w+;" , oooOo0OOOoo0 , text )
 if 77 - 77: ooOoO0o * iiiIIii1IIi
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
