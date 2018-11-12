#!/usr/bin/python
# coding=utf-8
import urllib , requests , re , json , os , uuid , random
from xbmcswift2 import Plugin , xbmc , xbmcgui , xbmcaddon
requests . packages . urllib3 . disable_warnings ( )
oo000 = Plugin ( )
if 9 - 9: Ii . o0o00Oo0O - iI11I1II1I1I
def oooo ( ) :
 iIIii1IIi = requests . get ( "https://docs.google.com/spreadsheets/d/13VzQebjGYac5hxe1I-z1pIvMiNB0gSG7oWJlFHWnqsA/export?format=tsv&gid=126722574" )
 o0OO00 = iIIii1IIi . text . strip ( ) . splitlines ( )
 random . shuffle ( o0OO00 )
 return o0OO00
 if 78 - 78: i11i . oOooOoO0Oo0O
@ oo000 . route ( '/play/<args_json>' )
def iI1 ( args_json = { } ) :
 i1I11i = json . loads ( args_json )
 OoOoOO00 (
 "[Play] %s" % (
 i1I11i [ "title" ] . encode ( "utf8" ) if "title" in i1I11i else "Unknow Title"
 ) ,
 '/play/%s/%s' % (
 i1I11i [ "url" ] ,
 json . dumps ( i1I11i [ "payloads" ] ) if "payloads" in i1I11i else "{}"
 )
 )
 I11i = xbmcgui . DialogProgress ( )
 I11i . create ( 'HPlus.vn' , 'Đang tải, Xin quý khách vui lòng đợi trong giây lát...' )
 oo000 . set_resolved_url ( O0O ( i1I11i [ "url" ] ) , subtitles = "https://raw.githubusercontent.com/vinhcomp/xml/master/xml/sub1.tsv" )
 I11i . close ( )
 del I11i
 if 78 - 78: i11ii11iIi11i . oOoO0oo0OOOo + IiiI / Iii1ii1II11i
def O0O ( url ) :
 iI111iI = "|User-Agent=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F58.0.3029.110%20Safari%2F537.36&Referer=http%3A%2F%2Fhplus.com.vn%2F"
 o0OO00 = requests . Session ( )
 IiII = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' ,
 'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8' ,
 'X-Requested-With' : 'XMLHttpRequest' ,
 'Referer' : url ,
 'Accept-Encoding' : 'gzip, deflate'
 }
 for iI1Ii11111iIi in oooo ( ) :
  try :
   IiII [ "Cookie" ] = "PHPSESSID=" + iI1Ii11111iIi . decode ( "base64" )
   o0OO00 . headers . update ( IiII )
   if 41 - 41: I1II1
   Ooo0OO0oOO = o0OO00 . get ( url )
   oooO0oo0oOOOO = re . search ( 'value="(https*\://.+?m3u8.+?)"' , Ooo0OO0oOO . text ) . group ( 1 )
   O0oO = {
 'url' : oooO0oo0oOOOO ,
 'type' : '1' ,
 'is_mobile' : '1'
 }
   Ooo0OO0oOO = o0OO00 . post ( "http://hplus.com.vn/content/getlinkvideo/" , data = O0oO )
   return Ooo0OO0oOO . text . encode ( "utf8" ) + iI111iI
  except : pass
  if 68 - 68: o00ooo0 / Oo00O0
def OoOoOO00 ( title = "Home" , page = "/" ) :
 try :
  ooO0oooOoO0 = "http://www.google-analytics.com/collect"
  II11i = open ( i1 ) . read ( )
  O0oO = {
 'v' : '1' ,
 'tid' : 'UA-52209804-5' ,
 'cid' : II11i ,
 't' : 'pageview' ,
 'dp' : "HPlus" + page ,
 'dt' : "[HPlus] - %s" % title
 }
  requests . post ( ooO0oooOoO0 , data = urllib . urlencode ( O0oO ) )
 except : pass
 if 64 - 64: oo % O0Oooo00
Ooo0 = xbmc . translatePath ( 'special://userdata' )
if os . path . exists ( Ooo0 ) == False :
 os . mkdir ( Ooo0 )
i1 = os . path . join ( Ooo0 , 'cid' )
if 89 - 89: I111i1i1111i - Ii1Ii1iiii11 % I1I1i1
if os . path . exists ( i1 ) == False :
 with open ( i1 , "w" ) as IiI1i :
  IiI1i . write ( str ( uuid . uuid1 ( ) ) )
  if 61 - 61: oo0O000OoO + IiiIIiiI11 / oooOOOOO * oOooOoO0Oo0O
if __name__ == '__main__' :
 oo000 . run ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
