#!/usr/bin/python
#coding=utf-8
import os , xbmc , urllib , zipfile , contextlib , re , platform , requests , json
requests . packages . urllib3 . disable_warnings ( )
oo000 = xbmc . translatePath ( 'special://home/addons' )
ii = xbmc . translatePath ( 'special://temp' )
oOOo = {
 "User-Agent" : "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/7.0)" ,
 "Accept-Encoding" : "gzip, deflate, sdch, br"
 }
if 59 - 59: Oo0Ooo . OO0OO0O0O0 * iiiIIii1IIi . iII111iiiii11 % I1IiiI
def IIi1IiiiI1Ii ( ) :
 I11i11Ii = next ( os . walk ( ii ) ) [ 2 ]
 if 65 - 65: i1iIi11iIIi1I
 for Oo in I11i11Ii :
  if ".fi" in Oo :
   os . remove ( os . path . join ( ii , Oo ) )
   if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11i / Ii1I
def IiiIII111iI ( ) :
 if "armv8l" in platform . uname ( ) :
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.useamcodec", "value":false},"id":1}' )
 else :
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.useamcodec", "value":true},"id":1}' )
  if 34 - 34: iii1I1I / O00oOoOoO0o0O . O0oo0OO0 + Oo0ooO0oo0oO . I1i1iI1i - II
def OoI1Ii11I1Ii1i ( ) :
 Ooo = "https://docs.google.com/spreadsheets/d/1zL6Kw4ZGoNcIuW9TAlHWZrNIJbDU5xHTtz-o8vpoJss/gviz/tq?gid=1514365674&headers=1&tq=select%20A%2CB%2CC%2CD%2CE"
 o0oOoO00o = requests . get ( Ooo , headers = oOOo ) . text
 i1oOOoo00O0O = "google.visualization.Query.setResponse\((.+?)\);"
 i1111 = json . loads ( re . compile ( i1oOOoo00O0O ) . findall ( o0oOoO00o ) [ 0 ] )
 if 22 - 22: OOo000 . O0
 I11i1i11i1I = [ ]
 for Iiii in i1111 [ "table" ] [ "rows" ] :
  OOO0O = { }
  OOO0O [ "label" ] = oo0ooO0oOOOOo ( Iiii [ "c" ] [ 0 ] ) . encode ( "utf-8" )
  OOO0O [ "label2" ] = oo0ooO0oOOOOo ( Iiii [ "c" ] [ 4 ] )
  OOO0O [ "thumbnail" ] = oo0ooO0oOOOOo ( Iiii [ "c" ] [ 2 ] )
  OOO0O [ "info" ] = { "plot" : oo0ooO0oOOOOo ( Iiii [ "c" ] [ 3 ] ) }
  OOO0O [ "path" ] = oo0ooO0oOOOOo ( Iiii [ "c" ] [ 1 ] )
  if ":/" not in OOO0O [ "label2" ] :
   oO000OoOoo00o = xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Addons.GetAddonDetails", "params":{"addonid":"%s", "properties":["version"]}, "id":1}' % OOO0O [ "label" ] )
   iiiI11 = json . loads ( oO000OoOoo00o )
   if "version" in oO000OoOoo00o and OOooO ( iiiI11 [ "result" ] [ "addon" ] [ "version" ] , OOO0O [ "label2" ] ) >= 0 :
    pass
   else :
    try :
     OOO0O [ "path" ] = "http" + OOO0O [ "path" ] . split ( "http" ) [ - 1 ]
     OOoO00o ( urllib . unquote_plus ( OOO0O [ "path" ] ) , OOO0O [ "label" ] )
    except : pass
  else :
   if not os . path . exists ( xbmc . translatePath ( OOO0O [ "label2" ] ) ) :
    try :
     OOO0O [ "path" ] = "http" + OOO0O [ "path" ] . split ( "http" ) [ - 1 ]
     OOoO00o ( urllib . unquote_plus ( OOO0O [ "path" ] ) , OOO0O [ "label2" ] )
    except : pass
    if 9 - 9: o0 - Oo0ooO0oo0oO % I1IiiI % iII111iiiii11
 xbmc . executebuiltin ( "XBMC.UpdateLocalAddons()" )
 xbmc . executebuiltin ( "XBMC.UpdateAddonRepos()" )
 if 3 - 3: I1i1iI1i + OO0OO0O0O0
def OOoO00o ( download_path , repo_id ) :
 if repo_id == "" : repo_id = "temp"
 if ":/" not in repo_id :
  I1Ii = xbmc . translatePath ( os . path . join ( ii , "%s.zip" % repo_id ) )
  urllib . urlretrieve ( download_path , I1Ii )
  with contextlib . closing ( zipfile . ZipFile ( I1Ii , "r" ) ) as o0oOo0Ooo0O :
   o0oOo0Ooo0O . extractall ( oo000 )
 else :
  I1Ii = xbmc . translatePath ( os . path . join ( ii , "%s.zip" % repo_id . split ( "/" ) [ - 1 ] ) )
  urllib . urlretrieve ( download_path , I1Ii )
  with contextlib . closing ( zipfile . ZipFile ( I1Ii , "r" ) ) as o0oOo0Ooo0O :
   o0oOo0Ooo0O . extractall ( xbmc . translatePath ( "/" . join ( repo_id . split ( "/" ) [ : - 1 ] ) ) )
   if 81 - 81: Ii1I * II * O0oo0OO0 - I1i1iI1i - I11i
def oo0ooO0oOOOOo ( colid ) :
 if colid is not None and colid [ "v" ] is not None : return colid [ "v" ]
 else : return ""
 if 90 - 90: i1iIi11iIIi1I + iii1I1I / I11i % i1iIi11iIIi1I - OO0OO0O0O0
def OOooO ( local_version , download_version ) :
 def iIii1 ( v ) :
  return [ int ( oOOoO0 ) for oOOoO0 in re . sub ( r'(\.0+)*$' , '' , v ) . split ( "." ) ]
 return cmp ( iIii1 ( local_version ) , iIii1 ( download_version ) )
 if 59 - 59: Oo0ooO0oo0oO * Oo0Ooo + Oo0ooO0oo0oO + O0 * ii1IiI1i
try :
 OoI1Ii11I1Ii1i ( )
except : pass
try :
 IiiIII111iI ( )
except : pass
try :
 IIi1IiiiI1Ii ( )
except : pass
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
