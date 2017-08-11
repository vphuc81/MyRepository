#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask , request , redirect
import re , json , urllib
import requests , YDStreamExtractor
from operator import itemgetter
requests . packages . urllib3 . disable_warnings ( )
YDStreamExtractor . disableDASHVideo ( True )
if 64 - 64: i11iIiiIii
OO0o = Flask ( __name__ )
if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
@ OO0o . route ( '/play' )
def ii11i ( ) :
 return oOooOoO0Oo0O ( )
 if 10 - 10: IIiI1I11i11
@ OO0o . route ( '/play.m3u8' )
def oOooOoO0Oo0O ( ) :
 ooOO00oOo = ""
 try :
  ooOO00oOo = request . args . get ( "url" )
 except : return ""
 if "livestream.com" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   if "events" not in ooOO00oOo :
    Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
    IiIi11iIIi1Ii = re . search ( "accounts/\d+/events/\d+" , Oooo000o . text )
    ooOO00oOo = "https://livestream.com/api/%s" % IiIi11iIIi1Ii . group ( )
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   Oo0O = Oooo000o . json ( )
   ooOO00oOo = Oo0O [ "stream_info" ] [ "m3u8_url" ]
  except : pass
 elif "talktv.vn" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   IiI = re . search ( 'loadPlayer.manifestUrl = "(.+?)"' , Oooo000o . text ) . group ( 1 )
   ooOO00oOo = IiI
  except : pass
 elif "ustream.tv" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   ooOo = re . search ( "tv/embed/(\d+)" , Oooo000o . text ) . group ( 1 )
   ooOO00oOo = "http://iphone-streaming.ustream.tv/uhls/%s/streams/live/iphone/playlist.m3u8" % ooOo
  except : pass
 elif "youtube.com" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   IiIi11iIIi1Ii = re . search ( '"hlsvp":".+?"' , Oooo000o . text )
   Oo0O = json . loads ( '{%s}' % IiIi11iIIi1Ii . group ( ) )
   ooOO00oOo = Oo0O [ "hlsvp" ]
  except :
   try :
    ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( )
   except : pass
 elif "vtvgo-" in ooOO00oOo :
  Oo = ooOO00oOo . split ( "-" ) [ - 1 ]
  ooOO00oOo = "http://vtvgo.vn/get-program-channel-detail?epg_id=%s&id=%s&type=1" % ( Oo , Oo )
  OOOo0 = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 }
  if 67 - 67: O00ooOO . I1iII1iiII
  iI1Ii11111iIi = requests . get ( "aHR0cDovL3Z0dmdvLnZuL3hlbS10cnVjLXR1eWVuLmh0bWw=" . decode ( "base64" ) , headers = OOOo0 )
  i1i1II = re . compile ( "'(\w{32})'\)\;" ) . findall ( iI1Ii11111iIi . text . encode ( "utf8" ) ) [ 0 ]
  try :
   O0oo0OO0 = re . compile ( 'epg_id=(\d+)' ) . findall ( ooOO00oOo ) [ 0 ]
   I1i1iiI1 = re . compile ( 'type=(\d+)' ) . findall ( ooOO00oOo ) [ 0 ]
   OOOo0 = {
 "X-Requested-With" : "XMLHttpRequest" ,
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 "Cookie" : "csrf_security=1"
 }
   iiIIIII1i1iI = {
 "epg_id" : O0oo0OO0 ,
 "type" : I1i1iiI1 ,
 "secret_token" : i1i1II ,
 "csrf_security" : "1"
 }
   o0oO0 = requests . post ( ooOO00oOo , headers = OOOo0 , data = iiIIIII1i1iI ) . json ( )
   ooOO00oOo = o0oO0 [ "data" ]
  except : pass
 elif "facebook.com" in ooOO00oOo :
  oo00 = re . search ( "videos/(\d+)" , ooOO00oOo ) . group ( 1 )
  ooOO00oOo = "https://www.facebook.com/video/playback/playlist.m3u8?v=%s" % oo00
 elif "twitch.tv" in ooOO00oOo :
  try :
   o00 = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"
   ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( ) . split ( "|" ) [ 0 ] + o00
  except : pass
 elif "://" not in ooOO00oOo :
  if ooOO00oOo . startswith ( "uno-" ) :
   Oo0oO0ooo = ooOO00oOo . strip ( ) . replace ( "uno-" , "" )
   o0oOoO00o = "NTg4N2RkZmZjMzEyYmYxMDk0ZGU0YmQ1" . decode ( "base64" )
   i1 = {
 "Content-Type" : "application/x-www-form-urlencoded" ,
 "User-Agent" : "Dalvik/2.1.0" ,
 "Accept-Encoding" : "gzip"
 }
   oOOoo00O0O = {
 "serial_id" : o0oOoO00o ,
 "query" : Oo0oO0ooo
 }
   i1111 = requests . post (
 "http://stbapi.v247tv.com/api/stb_channel2" ,
 headers = i1 ,
 data = oOOoo00O0O
 ) . json ( ) [ "data" ]
   i11 = requests . get ( "aHR0cDovL2VjaGlwc3RvcmUuY29tOjgwMDAvdW5vLw==" . decode ( "base64" ) + urllib . quote_plus ( i1111 ) )
   Oo0O = re . compile ( "(\{.+?\})" ) . findall ( i11 . text . strip ( ) ) [ 0 ]
   ooOO00oOo = json . loads ( Oo0O ) [ "url" ]
   if "smil:" in ooOO00oOo :
    I11 = re . search ( 'https*://.+?/' , ooOO00oOo ) . group ( )
   else :
    I11 = ooOO00oOo . split ( "playlist" ) [ 0 ]
   Oo0o0000o0o0 = requests . get ( ooOO00oOo ) . text . strip ( )
   ooOO00oOo = I11 + oOo0oooo00o ( Oo0o0000o0o0 )
  elif ooOO00oOo . startswith ( "nexttv-" ) :
   Oo0oO0ooo = ooOO00oOo . strip ( ) . replace ( "nexttv-" , "" )
   i11 = requests . get ( "http://m.tivi8k.net/htv7-2.php" )
   oO0o0o0ooO0oO = re . search ( '"(http://api.tivi8k.net/viettel/.+?)"' , i11 . text ) . group ( 1 )
   i11 = requests . get ( oO0o0o0ooO0oO )
   oo0o0O00 = re . search ( 'VOD_RequestID=(.+?)($|&)' , i11 . text ) . group ( 1 )
   ooOO00oOo = "http://27.67.80.6:18080/%s.m3u8?AdaptiveType=HLS&VOD_RequestID=%s" % ( Oo0oO0ooo , oo0o0O00 )
  elif ooOO00oOo . startswith ( "beeb-" ) :
   Oo0oO0ooo = ooOO00oOo . strip ( ) . replace ( "beeb-" , "" )
   oO = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" ,
 "X-Requested-With" : "XMLHttpRequest" ,
 "Accept-Encoding" : "gzip, deflate, sdch"
 }
   if 34 - 34: oOOoo * I1IiIiiIII
   iI1Ii11111iIi = requests . get (
 "http://tv.beeb.vn/site/player?channel=" + Oo0oO0ooo ,
 headers = oO )
   iI11 = re . search ( 'stream = "(.+?)"' , iI1Ii11111iIi . text ) . group ( 1 )
   ooOO00oOo = iI11 if "http://" in iI11 else "http://tv.beeb.vn" + iI11
   ooOO00oOo = requests . head (
 ooOO00oOo ,
 headers = oO ) . headers [ "location" ]
  else :
   iII111ii = requests . get ( "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRDaGFubmVsc0FwcEJveC5waHA=" . decode ( "base64" ) ) . json ( )
   for i1iIIi1 in iII111ii [ "channels" ] :
    if i1iIIi1 [ "channel_url" ] == ooOO00oOo :
     ii11iIi1I = "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRTdHJlYW1pbmdTZXJ2ZXIucGhw" . decode ( "base64" )
     i1111 = { 'strname' : '%s-' % i1iIIi1 [ "channel_id" ] }
     ooOO00oOo = requests . post ( ii11iIi1I , data = i1111 ) . text . strip ( )
     Oo0o0000o0o0 = requests . get ( ooOO00oOo ) . text . strip ( )
     I11 = re . search ( 'https*://.+?/.+?/.+?/' , ooOO00oOo ) . group ( )
     ooOO00oOo = I11 + oOo0oooo00o ( Oo0o0000o0o0 )
 else :
  try :
   ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( )
  except : pass
 return redirect ( ooOO00oOo )
 if 6 - 6: I1I11I1I1I * OooO0OO
def oOo0oooo00o ( text ) :
 IiIi11iIIi1Ii = re . compile ( 'BANDWIDTH=(\d+),.+?\n(.+?)$' , re . M ) . findall ( text )
 iiiIi = [ ]
 for IiIIIiI1I1 , OoO000 in IiIi11iIIi1Ii :
  iiiIi += [ [ int ( IiIIIiI1I1 ) , OoO000 ] ]
 iiiIi = sorted ( iiiIi , key = itemgetter ( 0 ) )
 return iiiIi [ - 1 ] [ - 1 ]
 if 42 - 42: oOoO - iiIiIIi % iI - I11iii / OO0O00
if __name__ == '__main__' :
 OO0o . run ( host = '0.0.0.0' , threaded = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
