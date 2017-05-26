#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i ( 'Search' , 'http://www.mythugian.net/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 ii11i ( 'Phim Lẻ' , 'http://www.mythugian.net/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 ii11i ( 'Phim Bộ' , 'http://www.mythugian.net/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 ii11i ( 'Phim Bộ theo Quốc Gia' , 'http://www.mythugian.net/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 ii11i ( 'Phim Lẻ theo Thể Loại' , 'http://www.mythugian.net/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
 I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i = xbmc . translatePath ( os . path . join ( I11i , "temp.jpg" ) )
 urllib . urlretrieve ( 'http://drive.google.com/uc?export=jpg&id=0B-ygKtjD8Sc-OUxwbVR5ZzZsbFJFT3A5aS04YlJkdDJtQ3BF' , I11i )
 O0O = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i )
 Oo = xbmcgui . WindowDialog ( )
 Oo . addControl ( O0O )
# Oo . doModal ( )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
def IiII ( ) :
 ii11i ( "Hồng Kong" , "http://www.mythugian.net/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ii11i ( "Hồng Kong (VNLT)" , "http://www.mythugian.net/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ii11i ( "Hàn Quốc" , "http://www.mythugian.net/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ii11i ( "Hàn Quốc (vietsub)" , "http://www.mythugian.net/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ii11i ( "Trung Quốc" , "http://www.mythugian.net/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ii11i ( "Đài Loan" , "http://www.mythugian.net/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.mythugian.net/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ii11i ( "Thái Lan" , "http://www.mythugian.net/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.mythugian.net/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 ii11i ( "Hành Động" , "http://www.mythugian.net/xem/category/8/hanh-dong.html" , "index" , "" )
 ii11i ( "Tình Cảm" , "http://www.mythugian.net/xem/category/9/tinh-cam.html" , "index" , "" )
 ii11i ( "Phim Hài" , "http://www.mythugian.net/xem/category/10/phim-hai.html" , "index" , "" )
 ii11i ( "Kinh Dị" , "http://www.mythugian.net/xem/category/11/kinh-di.html" , "index" , "" )
 ii11i ( "Kiếm Hiệp" , "http://www.mythugian.net/xem/category/12/kiem-hiep.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.mythugian.net/xem/category/15/viet-nam.html" , "index" , "" )
 ii11i ( "Hài Kịch" , "http://www.mythugian.net/xem/category/16/hai-kich.html" , "index" , "" )
 ii11i ( "Ca Nhạc" , "http://www.mythugian.net/xem/category/17/ca-nhac.html" , "index" , "" )
 ii11i ( "Cải Lương" , "http://www.mythugian.net/xem/category/18/cai-luong.html" , "index" , "" )
 ii11i ( "Phóng Sự" , "http://www.mythugian.net/xem/category/19/phong-su.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.mythugian.net/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( url ) :
 Oo0oO0oo0oO00 = i111I ( url )
 II1Ii1iI1i = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( Oo0oO0oo0oO00 )
 for iiI1iIiI , OOo , Ii1IIii11 in II1Ii1iI1i :
  Ii1IIii11 = Ii1IIii11 . replace ( "xomgiaitri.com" , "mythugian.net" )
  Ii1IIii11 = Ii1IIii11 . replace ( "www." , "" )
  Ii1IIii11 = "/" . join ( Ii1IIii11 . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( Ii1IIii11 . split ( "/" ) [ - 1 ] )
  ii11i ( "[B]" + OOo + "[/B]" , "http://www.mythugian.net/xem" + iiI1iIiI , 'mirrors' , Ii1IIii11 )
 Oooo0000 = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( Oo0oO0oo0oO00 . replace ( "'" , '"' ) )
 for iiI1iIiI , i11 in Oooo0000 :
  ii11i ( i11 , iiI1iIiI . replace ( "./" , "http://www.mythugian.net/xem/" ) , 'index' , "" )
  if 41 - 41: O00o0o0000o0o . oOo0oooo00o * I1i1i1ii - IIIII
def I1 ( ) :
 try :
  O0OoOoo00o = xbmc . Keyboard ( '' , 'Enter search text' )
  O0OoOoo00o . doModal ( )
  if 31 - 31: i111IiI + o0OoOoOO00 . ii1IiI1i
  if ( O0OoOoo00o . isConfirmed ( ) ) :
   OOoO00o = urllib . quote_plus ( O0OoOoo00o . getText ( ) )
  IIII ( II111iiii % OOoO00o )
 except : pass
 if 48 - 48: ii1IiI1i . iIiI - OOooOOo % iiI1i1 / O00o0o0000o0o . O00o0o0000o0o
def i1Ii ( url ) :
 I111I11 = O0O00Ooo ( url )
 Oo0oO0oo0oO00 = i111I ( I111I11 )
 OOoooooO = re . compile ( '<span class="name"[^>]*>(.+?)</span>' ) . findall ( Oo0oO0oo0oO00 )
 if 14 - 14: oO0o % iiI
 if "VIP A : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP A : " ) ) )
 if "VIP D : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP D : " ) ) )
 if "VIP B : " in OOoooooO :
  OOoooooO . insert ( 0 , OOoooooO . pop ( OOoooooO . index ( "VIP B : " ) ) )
 for IiI1I1 in range ( len ( OOoooooO ) ) :
  OoO000 = [ "Flv :" ]
  if not any ( x in OOoooooO [ IiI1I1 ] for x in OoO000 ) :
   ii11i ( "[%d] - %s" % ( IiI1I1 + 1 , OOoooooO [ IiI1I1 ] ) , I111I11 . encode ( "utf-8" ) , 'episodes' , "" )
   if 42 - 42: Ii11111i - iIiiiI1IiI1I1 / i11iIiiIii + iiI1i1 + ii1IiI1i
def iIi ( url , name ) :
 Oo0oO0oo0oO00 = i111I ( url )
 if 40 - 40: Ii11111i . OOooOOo . i1 . iIiiiI1IiI1I1
 name = name . split ( "] - " ) [ 1 ]
 I11iii = re . compile ( '<div class="listserver"><span class="name"[^>]*>%s</span>(.+?)</div>' % name ) . findall ( Oo0oO0oo0oO00 )
 OO0O00 = re . compile ( '<a href="(.+?)"><font[^>]*><b>(.+?)</b></font></a>' ) . findall ( I11iii [ 0 ] )
 if ( "episode_bg_2" in I11iii [ 0 ] ) :
  ii1 = re . compile ( '<font class="episode_bg_2">(.+?)</font>' ) . findall ( I11iii [ 0 ] )
  o0oO0o00oo ( "Part - " + ii1 [ 0 ] . replace ( "&nbsp;" , "" ) . strip ( ) . encode ( "utf8" ) , url , 'loadvideo' , '' , name )
 for II1i1Ii11Ii11 , iII11i in OO0O00 :
  o0oO0o00oo ( "Part - " + iII11i . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.mythugian.net/xem/" + II1i1Ii11Ii11 , 'loadvideo' , '' , name )
  if 97 - 97: oO0o % oO0o + o0OoOoOO00 * oOo0oooo00o
def O0O00Ooo ( url ) :
 o0o00o0 = i111I ( url )
 return re . compile ( '<p class="w_now"><a href="(.+?)" title="Xem phim trực tuyến">' ) . findall ( o0o00o0 ) [ 0 ]
 if 25 - 25: i1 - I1i1i1ii . iIiI
def I11ii1 ( url , name ) :
 I11II1i = xbmcgui . ListItem ( name )
 Oo0oO0oo0oO00 = i111I ( url )
 if "proxy.link" in Oo0oO0oo0oO00 :
  IIIIIooooooO0oo = re . compile ( "'proxy.link', '(.+?)'" ) . findall ( Oo0oO0oo0oO00 )
  Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo [ 0 ] )
 IIIIIooooooO0oo = re . compile ( '<source src="(.+?)" type="video/mp4">' ) . findall ( Oo0oO0oo0oO00 )
 if ( len ( IIIIIooooooO0oo ) == 0 ) :
  IIiiiiiiIi1I1 = None
  I1IIIii = re . compile ( 'file\: "(.+?)"' ) . findall ( Oo0oO0oo0oO00 )
  if 'iframe src="http://play.mythugian.net/' in Oo0oO0oo0oO00 :
   IIIIIooooooO0oo = re . compile ( 'iframe src="(http://play.mythugian.net/.+?)"' ) . findall ( Oo0oO0oo0oO00 )
   Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo [ 0 ] )
   IIIIIooooooO0oo = re . compile ( '(\[\{"label".+?\}\])' ) . findall ( Oo0oO0oo0oO00 )
   try :
    IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo [ 0 ] ) [ - 1 ] [ "file" ]
   except :
    IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo [ 0 ] ) [ - 1 ] [ "src" ]
  elif 'iframe src="http://img.mythugian.net/' in Oo0oO0oo0oO00 :
   IIIIIooooooO0oo = re . compile ( 'iframe src="(http://img.mythugian.net/.+?)"' ) . findall ( Oo0oO0oo0oO00 )
   Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo [ 0 ] )
   IIIIIooooooO0oo = re . compile ( 'sources = (\[.+?\])' ) . findall ( Oo0oO0oo0oO00 )
   IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo [ 0 ] ) [ 0 ] [ "file" ]
  elif I1IIIii is not None :
   if "http://" not in I1IIIii [ 0 ] :
    I1IIIii [ 0 ] = "http://www.mythugian.net/xem/" + I1IIIii [ 0 ]
   IIiiiiiiIi1I1 = I1IIIii [ 0 ]
  elif "app.box.com" in Oo0oO0oo0oO00 :
   oOoOooOo0o0 = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
   OOOO = i111I ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % oOoOooOo0o0 )
   OOO00 = json . loads ( OOOO ) [ "file" ] [ "versionId" ]
   IIiiiiiiIi1I1 = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( OOO00 , oOoOooOo0o0 )
  elif "drive.google.com/file" in Oo0oO0oo0oO00 :
   iiiiiIIii = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
   IIiiiiiiIi1I1 = O000OO0 ( iiiiiIIii )
   I11II1i . setPath ( IIiiiiiiIi1I1 )
  elif "openload" in Oo0oO0oo0oO00 :
   try :
    IIiiiiiiIi1I1 = re . compile ( '"(https://openload.+?)"' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
    IIiiiiiiIi1I1 = urlresolver . resolve ( IIiiiiiiIi1I1 )
   except :
    pass
  else :
   IIIIIooooooO0oo = re . compile ( "file: '.+?'" ) . findall ( Oo0oO0oo0oO00 )
   if "http://" not in IIIIIooooooO0oo [ 0 ] :
    IIiiiiiiIi1I1 = "http://www.mythugian.net/xem/" + IIIIIooooooO0oo [ 0 ]
   else :
    IIiiiiiiIi1I1 = IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIiiiiiiIi1I1 )
 else :
  if "http://" not in IIIIIooooooO0oo [ 0 ] :
   IIIIIooooooO0oo [ 0 ] = "http://www.mythugian.net/xem/" + IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIIIIooooooO0oo [ 0 ] )
 I11II1i . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 if 43 - 43: IIIII - iiI % o0 . oO0o
def O000OO0 ( drive_id ) :
 o00 = "https://drive.google.com/uc?export=download&id=%s" % drive_id
 OOOO = requests . get ( "https://drive.google.com/file/d/%s" % drive_id )
 if "fmt_stream_map" in OOOO . text :
  OooOooo = json . loads ( re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( OOOO . text ) [ 0 ] )
  try :
   o00 = re . compile ( "22\|(.+?)," ) . findall ( OooOooo [ 1 ] ) [ 0 ]
  except :
   o00 = re . compile ( "18\|(.+?)," ) . findall ( OooOooo [ 1 ] ) [ 0 ]
  O000oo0O = "|User-Agent=%s&Cookie=%s" % ( urllib . quote ( OOOO . request . headers [ "User-Agent" ] ) , urllib . quote ( OOOO . headers [ "Set-Cookie" ] ) )
  o00 += O000oo0O
  if 66 - 66: IiiIII111iI / OOooOOo - o0 . iiI1i1 / o0 * iiI1i1
 else :
  IIIii1II1II = requests . Session ( )
  OOOO = IIIii1II1II . head ( o00 )
  i1I1iI = ""
  for oo0OooOOo0 , o0O in OOOO . cookies . iteritems ( ) :
   if "download_warning_" in oo0OooOOo0 :
    i1I1iI = o0O
  if i1I1iI != "" :
   O00oO = "%s&confirm=%s" % ( o00 , i1I1iI )
   OOOO = IIIii1II1II . head ( O00oO )
   if OOOO . status_code == 302 :
    o00 = O00oO
 return o00
 if 39 - 39: I1i1i1ii - o0OoOoOO00 * ii1IiI1i % I11iIi1I * o0OoOoOO00 % o0OoOoOO00
def OoOOOOO ( url ) :
 iiiiiIIii = ""
 iIi1i111II = urllib2 . Request ( url )
 iIi1i111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 iIi1i111II . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OoOO00O = urllib2 . urlopen ( iIi1i111II )
 url = OoOO00O . geturl ( )
 try :
  iiiiiIIii = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 OoOO00O . close ( )
 return iiiiiIIii
 if 53 - 53: ii1IiI1i % iIiI - OOooOOo
def i111I ( url ) :
 iIi1i111II = urllib2 . Request ( url )
 iIi1i111II . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 iIi1i111II . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 OoOO00O = urllib2 . urlopen ( iIi1i111II )
 Oo0oO0oo0oO00 = OoOO00O . read ( )
 OoOO00O . close ( )
 Oo0oO0oo0oO00 = '' . join ( Oo0oO0oo0oO00 . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\n' , '' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\t' , '' )
 Oo0oO0oo0oO00 = re . sub ( '  +' , ' ' , Oo0oO0oo0oO00 )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '> <' , '><' )
 return Oo0oO0oo0oO00
 if 97 - 97: Ii11111i % I1i1i1ii * I1i1i1ii
def o0oO0o00oo ( name , url , mode , iconimage , mirrorname ) :
 i11iiI111I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 II11i1iIiII1 = True
 iIi1iIiii111 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 iIi1iIiii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 iIi1iIiii111 . setProperty ( "IsPlayable" , "true" )
 II11i1iIiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iiI111I , listitem = iIi1iIiii111 )
 return II11i1iIiII1
 if 16 - 16: IiiIII111iI + ii1IiI1i - o0OoOoOO00
def ii11i ( name , url , mode , iconimage ) :
 i11iiI111I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 II11i1iIiII1 = True
 iIi1iIiii111 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iIi1iIiii111 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 II11i1iIiII1 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = i11iiI111I , listitem = iIi1iIiii111 , isFolder = True )
 return II11i1iIiII1
 if 85 - 85: OOooOOo + iIiiiI1IiI1I1
def Oo0OoO00oOO0o ( k , e ) :
 OOO00O = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for IiI1I1 in range ( len ( e ) ) :
  OOoOO0oo0ooO = k [ IiI1I1 % len ( k ) ]
  O0o0O00Oo0o0 = chr ( ( 256 + ord ( e [ IiI1I1 ] ) - ord ( OOoOO0oo0ooO ) ) % 256 )
  OOO00O . append ( O0o0O00Oo0o0 )
 return "" . join ( OOO00O )
 if 87 - 87: i111IiI * i1 % i11iIiiIii % OOooOOo - iiI1i1
def O0ooo0O0oo0 ( parameters ) :
 oo0oOo = { }
 if 89 - 89: OOooOOo
 if parameters :
  OO0oOoOO0oOO0 = parameters [ 1 : ] . split ( "&" )
  for oO0OOoo0OO in OO0oOoOO0oOO0 :
   O0 = oO0OOoo0OO . split ( '=' )
   if ( len ( O0 ) ) == 2 :
    oo0oOo [ O0 [ 0 ] ] = O0 [ 1 ]
 return oo0oOo
 if 25 - 25: IiiIII111iI
Ii1i = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 15 - 15: I1i1i1ii . ii1I . iIiI / i11iIiiIii - O00o0o0000o0o . iIiiiI1IiI1I1
if os . path . exists ( Ii1i ) == False :
 os . mkdir ( Ii1i )
i1O0OoO0o = os . path . join ( Ii1i , 'visitor' )
if 79 - 79: OOooOOo - iiI * ii1IiI1i + OOooOOo % iiI * iiI
if os . path . exists ( i1O0OoO0o ) == False :
 from random import randint
 oOOo0 = open ( i1O0OoO0o , "w" )
 oOOo0 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 oOOo0 . close ( )
 if 54 - 54: iiI - I1i1i1ii % iiI1i1
def OOoO ( utm_url ) :
 iII = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iIi1i111II = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : iII }
 )
  OoOO00O = urllib2 . urlopen ( iIi1i111II ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return OoOO00O
 if 38 - 38: IIIII
def Ii1 ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  OOooOO000 = "1.0"
  OOoOoo = open ( i1O0OoO0o ) . read ( )
  oO0000OOo00 = "XomGiaiTri"
  iiIi1IIiIi = "UA-52209804-2"
  oOO00Oo = "www.viettv24.com"
  i1iIIIi1i = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   iI1iIIiiii = i1iIIIi1i + "?" + "utmwv=" + OOooOO000 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0000OOo00 ) + "&utmac=" + iiIi1IIiIi + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOoOoo , "1" , "1" , "2" ] )
   if 26 - 26: oO0o . iIiI
   if 39 - 39: oOo0oooo00o - iiI % i11iIiiIii * IIIII . I1i1i1ii
   if 58 - 58: ii1IiI1i % i11iIiiIii . oOo0oooo00o / Ii11111i
   if 84 - 84: oOo0oooo00o . IiiIII111iI / i1 - o0 / iIiI / I11iIi1I
   if 12 - 12: o0 * oOo0oooo00o % iIiiiI1IiI1I1 % ii1I
  else :
   if group == "None" :
    iI1iIIiiii = i1iIIIi1i + "?" + "utmwv=" + OOooOO000 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0000OOo00 + "/" + name ) + "&utmac=" + iiIi1IIiIi + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOoOoo , "1" , "1" , "2" ] )
    if 20 - 20: iiI1i1 % O00o0o0000o0o / O00o0o0000o0o + O00o0o0000o0o
    if 45 - 45: Ii11111i - I1i1i1ii - iIiI - ii1IiI1i . o0OoOoOO00 / iiI
    if 51 - 51: iiI + oOo0oooo00o
    if 8 - 8: Ii11111i * OOooOOo - O00o0o0000o0o - ii1IiI1i * iiI1i1 % o0
    if 48 - 48: iiI
   else :
    iI1iIIiiii = i1iIIIi1i + "?" + "utmwv=" + OOooOO000 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oO0000OOo00 + "/" + group + "/" + name ) + "&utmac=" + iiIi1IIiIi + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OOoOoo , "1" , "1" , "2" ] )
    if 11 - 11: oO0o + iIiI - ii1IiI1i / I11iIi1I + i1 . o0OoOoOO00
    if 41 - 41: O00o0o0000o0o - iiI - iiI
    if 68 - 68: iiI1i1 % IIIII
    if 88 - 88: ii1I - i111IiI + iiI1i1
    if 40 - 40: o0 * O00o0o0000o0o + iiI1i1 % oOo0oooo00o
    if 74 - 74: Ii11111i - i1 + iIiI + IIIII / OOooOOo
  print "============================ POSTING ANALYTICS ============================"
  OOoO ( iI1iIIiiii )
  if 23 - 23: iiI
  if not group == "None" :
   o00oO0oOo00 = i1iIIIi1i + "?" + "utmwv=" + OOooOO000 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( oOO00Oo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oO0000OOo00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oO0000OOo00 ) + "&utmac=" + iiIi1IIiIi + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , OOoOoo , "1" , "2" ] )
   if 81 - 81: ii1IiI1i
   if 42 - 42: ii1IiI1i / oO0o / I11iIi1I + oOo0oooo00o / OOooOOo
   if 84 - 84: i111IiI * o0OoOoOO00 + i1
   if 53 - 53: oOo0oooo00o % o0OoOoOO00 . I1i1i1ii - ii1I - I1i1i1ii * o0OoOoOO00
   if 77 - 77: ii1I * ii1IiI1i
   if 95 - 95: o0 + i11iIiiIii
   if 6 - 6: i111IiI / i11iIiiIii + oOo0oooo00o * Ii11111i
   if 80 - 80: o0OoOoOO00
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OOoO ( o00oO0oOo00 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 83 - 83: oO0o . i11iIiiIii + o0OoOoOO00 . I11iIi1I * oO0o
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 53 - 53: o0OoOoOO00
i1Ii1Ii = O0ooo0O0oo0 ( sys . argv [ 2 ] )
oOO = i1Ii1Ii . get ( 'mode' )
II111iiii = i1Ii1Ii . get ( 'url' )
ii1iII1II = i1Ii1Ii . get ( 'name' )
if type ( II111iiii ) == type ( str ( ) ) :
 II111iiii = urllib . unquote_plus ( II111iiii )
if type ( ii1iII1II ) == type ( str ( ) ) :
 ii1iII1II = urllib . unquote_plus ( ii1iII1II )
 if 48 - 48: o0OoOoOO00 * O00o0o0000o0o . oO0o + Ii11111i
OoO0o = str ( sys . argv [ 1 ] )
if oOO == 'index' :
 Ii1 ( "Browse" , ii1iII1II )
 IIII ( II111iiii )
elif oOO == 'search' :
 Ii1 ( "None" , "Search" )
 I1 ( )
elif oOO == 'videosbyregion' :
 Ii1 ( "Browse" , ii1iII1II )
 IiII ( )
elif oOO == 'videosbycategory' :
 Ii1 ( "Browse" , ii1iII1II )
 i1I1ii1II1iII ( )
elif oOO == 'mirrors' :
 Ii1 ( "Browse" , ii1iII1II )
 i1Ii ( II111iiii )
elif oOO == 'episodes' :
 Ii1 ( "Browse" , ii1iII1II )
 iIi ( II111iiii , ii1iII1II )
elif oOO == 'loadvideo' :
 Ii1 ( "Play" , ii1iII1II + "/" + II111iiii )
 oO0o0Ooooo = xbmcgui . DialogProgress ( )
 oO0o0Ooooo . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 I11ii1 ( II111iiii , ii1iII1II )
 oO0o0Ooooo . close ( )
 del oO0o0Ooooo
else :
 Ii1 ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( OoO0o ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
