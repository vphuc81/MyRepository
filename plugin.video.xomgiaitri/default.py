#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64 , json , logging , requests , urlresolver
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.xomgiaitri'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i ( 'Search' , 'http://www.xomphimbo.com/xem/search/%s/1.html' , 'search' , 'http://www.viettv24.com/addonicons/Search.jpg' )
 ii11i ( 'Phim Lẻ' , 'http://www.xomphimbo.com/xem/the-loai/phim-dien-anh' , 'index' , 'http://www.viettv24.com/addonicons/Movies.jpg' )
 ii11i ( 'Phim Bộ' , 'http://www.xomphimbo.com/xem/the-loai/phim-bo' , 'index' , 'http://www.viettv24.com/addonicons/Series.jpg' )
 ii11i ( 'Phim Bộ theo Quốc Gia' , 'http://www.xomphimbo.com/' , 'videosbyregion' , 'http://www.viettv24.com/addonicons/Regions.jpg' )
 ii11i ( 'Phim Lẻ theo Thể Loại' , 'http://www.xomphimbo.com/' , 'videosbycategory' , 'http://www.viettv24.com/addonicons/Categories.jpg' )
 if 66 - 66: iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
 I11i = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 I11i = xbmc . translatePath ( os . path . join ( I11i , "temp.jpg" ) )
 urllib . urlretrieve ( 'http://drive.google.com/uc?export=jpg&id=0B-ygKtjD8Sc-OUxwbVR5ZzZsbFJFT3A5aS04YlJkdDJtQ3BF' , I11i )
 O0O = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I11i )
 Oo = xbmcgui . WindowDialog ( )
 Oo . addControl ( O0O )
 #Oo . doModal ( )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
def IiII ( ) :
 ii11i ( "Hồng Kong" , "http://www.xomphimbo.com/xem/category/1/phim-bo-hong-kong.html" , "index" , "" )
 ii11i ( "Hồng Kong (VNLT)" , "http://www.xomphimbo.com/xem/category/28/phim-bo-hong-kong-vnlt.html" , "index" , "" )
 ii11i ( "Hàn Quốc" , "http://www.xomphimbo.com/xem/category/4/phim-bo-han-quoc.html" , "index" , "" )
 ii11i ( "Hàn Quốc (vietsub)" , "http://www.xomphimbo.com/xem/category/29/phim-bo-han-quoc-vietsub.html" , "index" , "" )
 ii11i ( "Trung Quốc" , "http://www.xomphimbo.com/xem/category/2/phim-bo-trung-quoc.html" , "index" , "" )
 ii11i ( "Đài Loan" , "http://www.xomphimbo.com/xem/category/3/phim-bo-dai-loan.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/5/phim-bo-viet-nam.html" , "index" , "" )
 ii11i ( "Thái Lan" , "http://www.xomphimbo.com/xem/category/22/phim-bo-thai-lan.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/7/cac-loai-khac.html" , "index" , "" )
 if 28 - 28: Ii11111i * iiI1i1
def i1I1ii1II1iII ( ) :
 ii11i ( "Hành Động" , "http://www.xomphimbo.com/xem/category/8/hanh-dong.html" , "index" , "" )
 ii11i ( "Tình Cảm" , "http://www.xomphimbo.com/xem/category/9/tinh-cam.html" , "index" , "" )
 ii11i ( "Phim Hài" , "http://www.xomphimbo.com/xem/category/10/phim-hai.html" , "index" , "" )
 ii11i ( "Kinh Dị" , "http://www.xomphimbo.com/xem/category/11/kinh-di.html" , "index" , "" )
 ii11i ( "Kiếm Hiệp" , "http://www.xomphimbo.com/xem/category/12/kiem-hiep.html" , "index" , "" )
 ii11i ( "Việt Nam" , "http://www.xomphimbo.com/xem/category/15/viet-nam.html" , "index" , "" )
 ii11i ( "Hài Kịch" , "http://www.xomphimbo.com/xem/category/16/hai-kich.html" , "index" , "" )
 ii11i ( "Ca Nhạc" , "http://www.xomphimbo.com/xem/category/17/ca-nhac.html" , "index" , "" )
 ii11i ( "Cải Lương" , "http://www.xomphimbo.com/xem/category/18/cai-luong.html" , "index" , "" )
 ii11i ( "Phóng Sự" , "http://www.xomphimbo.com/xem/category/19/phong-su.html" , "index" , "" )
 ii11i ( "Các Loại Khác" , "http://www.xomphimbo.com/xem/category/20/cac-loai-khac.html" , "index" , "" )
 if 86 - 86: oO0o
def IIII ( url ) :
 Oo0oO0oo0oO00 = i111I ( url )
 II1Ii1iI1i = re . compile ( '<td align="center"><a href=".(.+?)" title="(.+?)"><img src="(.+?)"[^>]*/></a>' ) . findall ( Oo0oO0oo0oO00 )
 for iiI1iIiI , OOo , Ii1IIii11 in II1Ii1iI1i :
  Ii1IIii11 = Ii1IIii11 . replace ( "xomgiaitri.com" , "mythugian.net" )
  Ii1IIii11 = Ii1IIii11 . replace ( "www." , "" )
  Ii1IIii11 = "/" . join ( Ii1IIii11 . split ( "/" ) [ : - 1 ] ) + "/" + urllib . quote ( Ii1IIii11 . split ( "/" ) [ - 1 ] )
  ii11i ( "[B]" + OOo + "[/B]" , "http://www.xomphimbo.com/xem" + iiI1iIiI , 'mirrors' , Ii1IIii11 )
 Oooo0000 = re . compile ( '<a class="pagelink" [^>]* href="(.+?)"[^>]*>(.+?)</a>' ) . findall ( Oo0oO0oo0oO00 . replace ( "'" , '"' ) )
 for iiI1iIiI , i11 in Oooo0000 :
  ii11i ( i11 , iiI1iIiI . replace ( "./" , "http://www.xomphimbo.com/xem/" ) , 'index' , "" )
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
  OoO000 = [ "Flv :" , "OK :" ]
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
  o0oO0o00oo ( "Part - " + iII11i . replace ( "&nbsp;" , "" ) . strip ( ) , "http://www.xomphimbo.com/xem/" + II1i1Ii11Ii11 , 'loadvideo' , '' , name )
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
   try :
    IIIIIooooooO0oo = re . search ( 'iframe[^>]*src="(http://img.mythugian.net/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
    try :
     IIiiiiiiIi1I1 = re . search ( 'link=(.+?)$' , IIIIIooooooO0oo ) . group ( 1 ) . decode ( "base64" )
     IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIiiiiiiIi1I1 )
    except :
     Oo0oO0oo0oO00 = i111I ( IIIIIooooooO0oo )
     try :
      def OOOO ( url ) :
       OOO00 = requests . get ( url )
       iiiiiIIii = re . search ( ",'(\|*http.+?)'" , OOO00 . text ) . group ( 1 ) . split ( "|" )
       O000OO0 = re . compile ( '"(0\://.+?)"' ) . findall ( OOO00 . text )
       return iiiiiIIii , O000OO0
       if 43 - 43: IIIII - iiI % o0 . oO0o
      def o00 ( enc_url , words ) :
       OooOooo = "0123456789abcdefghijklmnopqrstuvwxyz"
       O000oo0O = ""
       for IiI1I1 in range ( 0 , len ( enc_url ) ) :
        if IiI1I1 != 12 and enc_url [ IiI1I1 ] in OooOooo :
         O000oo0O += words [ OooOooo . index ( enc_url [ IiI1I1 ] ) ]
        else :
         O000oo0O += enc_url [ IiI1I1 ]
       return O000oo0O
       if 66 - 66: IiiIII111iI / OOooOOo - o0 . iiI1i1 / o0 * iiI1i1
      iiiiiIIii , O000OO0 = OOOO ( IIIIIooooooO0oo )
      IIiiiiiiIi1I1 = o00 ( O000OO0 [ 0 ] , iiiiiIIii )
      xbmc . log ( IIiiiiiiIi1I1 )
     except :
      try :
       IIIii1II1II = [ ]
       IIIii1II1II += [ re . search ( 'start\|primary\|(.+?)\|' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
       try :
        IIIii1II1II += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
       except : pass
       IIiiiiiiIi1I1 = oOoOooOo0o0 ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( IIIii1II1II ) ) )
      except :
       try :
        IIIii1II1II = [ ]
        IIIii1II1II += [ re . search ( 'start\|(\w+)\|setup' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
        IIIii1II1II += [ re . search ( '\|google\|(\w+)\|color\|' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
        IIIii1II1II += [ re . search ( 'primary\|(\w+)\|startparam' . decode ( "base64" ) , Oo0oO0oo0oO00 ) . group ( 1 ) ]
        IIiiiiiiIi1I1 = oOoOooOo0o0 ( "https://drive.google.com/file/d/%s/view" . decode ( "base64" ) % ( "-" . join ( IIIii1II1II ) ) )
       except :
        try :
         IIIIIooooooO0oo = re . search ( 'sources = (\[.+?\]);' , Oo0oO0oo0oO00 )
         IIiiiiiiIi1I1 = json . loads ( IIIIIooooooO0oo . group ( 1 ) ) [ - 1 ] [ "file" ]
        except :
         try :
          IIIIIooooooO0oo = re . search ( '"(https://drive.google.com/file/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
          IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIIIIooooooO0oo . replace ( "preview" , "view" ) )
         except :
          IIiiiiiiIi1I1 = re . search ( '"(http\://.+?\.mediafire\.com/.+?)"' , Oo0oO0oo0oO00 ) . group ( 1 )
   except : pass
  elif "drive.google.com/file" in Oo0oO0oo0oO00 :
   IIIIIooooooO0oo = re . search ( '"(https://drive.google.com/file.+?)"' , Oo0oO0oo0oO00 )
   IIiiiiiiIi1I1 = oOoOooOo0o0 ( IIIIIooooooO0oo . group ( 1 ) . replace ( "preview" , "view" ) )
  elif I1IIIii is not None :
   if "http://" not in I1IIIii [ 0 ] :
    I1IIIii [ 0 ] = "http://www.xomphimbo.com/xem/" + I1IIIii [ 0 ]
   IIiiiiiiIi1I1 = I1IIIii [ 0 ]
  elif "app.box.com" in Oo0oO0oo0oO00 :
   i1I1iI = re . compile ( 'https://app.box.com/embed_widget/s/(.+?)\?' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
   oo0OooOOo0 = i111I ( "https://app.box.com/index.php?rm=preview_embed&sharedName=%s" % i1I1iI )
   o0O = json . loads ( oo0OooOOo0 ) [ "file" ] [ "versionId" ]
   IIiiiiiiIi1I1 = "https://app.box.com/representation/file_version_%s/video_480.mp4?shared_name=%s" % ( o0O , i1I1iI )
  elif "openload" in Oo0oO0oo0oO00 :
   try :
    IIiiiiiiIi1I1 = re . compile ( '"(https://openload.+?)"' ) . findall ( Oo0oO0oo0oO00 ) [ 0 ]
    IIiiiiiiIi1I1 = urlresolver . resolve ( IIiiiiiiIi1I1 )
   except :
    pass
  else :
   IIIIIooooooO0oo = re . compile ( "file: '.+?'" ) . findall ( Oo0oO0oo0oO00 )
   if "http://" not in IIIIIooooooO0oo [ 0 ] :
    IIiiiiiiIi1I1 = "http://www.xomphimbo.com/xem/" + IIIIIooooooO0oo [ 0 ]
   else :
    IIiiiiiiIi1I1 = IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIiiiiiiIi1I1 )
 else :
  if "http://" not in IIIIIooooooO0oo [ 0 ] :
   IIIIIooooooO0oo [ 0 ] = "http://www.xomphimbo.com/xem/" + IIIIIooooooO0oo [ 0 ]
  I11II1i . setPath ( IIIIIooooooO0oo [ 0 ] )
 I11II1i . setProperty ( "IsPlayable" , "true" )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11II1i )
 if 72 - 72: oOo0oooo00o / iIiiiI1IiI1I1 * i1 - IIIII
def oOoOooOo0o0 ( url , hq = True ) :
 Oo0O0O0ooO0O = "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"
 IIIIii = {
 'User-Agent' : Oo0O0O0ooO0O ,
 'Accept-Encoding' : 'gzip, deflate, sdch' ,
 }
 oo0OooOOo0 = requests . get ( url , headers = IIIIii )
 O0o0 = oo0OooOOo0 . text
 try :
  IIIIIooooooO0oo = re . compile ( '(\["fmt_stream_map".+?\])' ) . findall ( O0o0 ) [ 0 ]
  OO00Oo = [ "38" , "37" , "46" , "22" , "45" , "18" , "43" ]
  if not hq : OO00Oo . reverse ( )
  O0OOO0OOoO0O = json . loads ( IIIIIooooooO0oo ) [ 1 ] . split ( "," )
  for O00Oo000ooO0 in OO00Oo :
   for OoO0O00 in O0OOO0OOoO0O :
    if OoO0O00 . startswith ( O00Oo000ooO0 + "|" ) :
     url = OoO0O00 . split ( "|" ) [ 1 ]
     IIiII = "|User-Agent=%s&Cookie=%s" % ( urllib . quote_plus ( Oo0O0O0ooO0O ) , urllib . quote_plus ( oo0OooOOo0 . headers [ 'set-cookie' ] ) )
     return url + IIiII
 except :
  try :
   return re . search ( "fmt_stream_map\=18\|(.+?)(\||$)" , O0o0 ) . group ( 1 )
  except : pass
  if 80 - 80: I1i1i1ii . Ii11111i
def IIi ( url ) :
 i11iIIIIIi1 = ""
 iiII1i1 = urllib2 . Request ( url )
 iiII1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 iiII1i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 o00oOO0o = urllib2 . urlopen ( iiII1i1 )
 url = o00oOO0o . geturl ( )
 try :
  i11iIIIIIi1 = re . compile ( '"https://drive.google.com/file/d/(.+?)/.+?"' ) . findall ( url ) [ 0 ]
 except :
  pass
 o00oOO0o . close ( )
 return i11iIIIIIi1
 if 80 - 80: Ii11111i + iiI1i1 - iiI1i1 % oOo0oooo00o
def i111I ( url ) :
 iiII1i1 = urllib2 . Request ( url )
 iiII1i1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 iiII1i1 . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 o00oOO0o = urllib2 . urlopen ( iiII1i1 )
 Oo0oO0oo0oO00 = o00oOO0o . read ( )
 o00oOO0o . close ( )
 Oo0oO0oo0oO00 = '' . join ( Oo0oO0oo0oO00 . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\n' , '' )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '\t' , '' )
 Oo0oO0oo0oO00 = re . sub ( '  +' , ' ' , Oo0oO0oo0oO00 )
 Oo0oO0oo0oO00 = Oo0oO0oo0oO00 . replace ( '> <' , '><' )
 return Oo0oO0oo0oO00
 if 63 - 63: o0 - IiiIII111iI + iiI % oO0o / ii1I / I11iIi1I
def o0oO0o00oo ( name , url , mode , iconimage , mirrorname ) :
 O0o0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 i1Oo00 . setProperty ( "IsPlayable" , "true" )
 O00O0oOO00O00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0o0O00Oo0o0 , listitem = i1Oo00 )
 return O00O0oOO00O00
 if 31 - 31: IIIII . OOooOOo / iiI
def ii11i ( name , url , mode , iconimage ) :
 O0o0O00Oo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 O00O0oOO00O00 = True
 i1Oo00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 i1Oo00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 O00O0oOO00O00 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = O0o0O00Oo0o0 , listitem = i1Oo00 , isFolder = True )
 return O00O0oOO00O00
 if 89 - 89: OOooOOo
def OO0oOoOO0oOO0 ( k , e ) :
 oO0OOoo0OO = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for IiI1I1 in range ( len ( e ) ) :
  O0 = k [ IiI1I1 % len ( k ) ]
  ii1ii1ii = chr ( ( 256 + ord ( e [ IiI1I1 ] ) - ord ( O0 ) ) % 256 )
  oO0OOoo0OO . append ( ii1ii1ii )
 return "" . join ( oO0OOoo0OO )
 if 91 - 91: I1i1i1ii
def iiIii ( parameters ) :
 ooo0O = { }
 if 75 - 75: I11iIi1I % I11iIi1I . IIIII
 if parameters :
  III1iII1I1ii = parameters [ 1 : ] . split ( "&" )
  for oOOo0 in III1iII1I1ii :
   oo00O00oO = oOOo0 . split ( '=' )
   if ( len ( oo00O00oO ) ) == 2 :
    ooo0O [ oo00O00oO [ 0 ] ] = oo00O00oO [ 1 ]
 return ooo0O
 if 23 - 23: ii1IiI1i + ii1IiI1i . iiI1i1
ii1ii11IIIiiI = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 67 - 67: oO0o * Ii11111i * IiiIII111iI + iiI1i1 / iIiiiI1IiI1I1
if os . path . exists ( ii1ii11IIIiiI ) == False :
 os . mkdir ( ii1ii11IIIiiI )
I1I111 = os . path . join ( ii1ii11IIIiiI , 'visitor' )
if 82 - 82: i11iIiiIii - oOo0oooo00o * iIiI / oO0o
if os . path . exists ( I1I111 ) == False :
 from random import randint
 i1oOo = open ( I1I111 , "w" )
 i1oOo . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 i1oOo . close ( )
 if 75 - 75: o0 + i1
def OoooO0oO ( utm_url ) :
 i1iIi = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iiII1i1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : i1iIi }
 )
  o00oOO0o = urllib2 . urlopen ( iiII1i1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return o00oOO0o
 if 68 - 68: i11iIiiIii % IiiIII111iI + i11iIiiIii
def iii ( group , name ) :
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
  II1I = "1.0"
  O0i1II1Iiii1I11 = open ( I1I111 ) . read ( )
  IIIIiiIiI = "XomGiaiTri"
  o00oooO0Oo = "UA-52209804-2"
  o0O0OOO0Ooo = "www.viettv24.com"
  iiIiI = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   I1OOO00O0O = iiIiI + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IIIIiiIiI ) + "&utmac=" + o00oooO0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0i1II1Iiii1I11 , "1" , "1" , "2" ] )
   if 33 - 33: iiI . I1i1i1ii . o0
   if 72 - 72: iIiiiI1IiI1I1 / ii1IiI1i + iIiI - i1
   if 29 - 29: IiiIII111iI + Ii11111i % iiI
   if 10 - 10: oO0o / IIIII - o0 * ii1I - o0
   if 97 - 97: IiiIII111iI + o0 * O00o0o0000o0o + iiI1i1 % oOo0oooo00o
  else :
   if group == "None" :
    I1OOO00O0O = iiIiI + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IIIIiiIiI + "/" + name ) + "&utmac=" + o00oooO0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0i1II1Iiii1I11 , "1" , "1" , "2" ] )
    if 74 - 74: Ii11111i - i1 + iIiI + IIIII / OOooOOo
    if 23 - 23: iiI
    if 85 - 85: O00o0o0000o0o
    if 84 - 84: o0 . ii1I % iIiI + O00o0o0000o0o % iIiI % ii1IiI1i
    if 42 - 42: ii1IiI1i / oO0o / I11iIi1I + oOo0oooo00o / OOooOOo
   else :
    I1OOO00O0O = iiIiI + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( IIIIiiIiI + "/" + group + "/" + name ) + "&utmac=" + o00oooO0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O0i1II1Iiii1I11 , "1" , "1" , "2" ] )
    if 84 - 84: i111IiI * o0OoOoOO00 + i1
    if 53 - 53: oOo0oooo00o % o0OoOoOO00 . I1i1i1ii - ii1I - I1i1i1ii * o0OoOoOO00
    if 77 - 77: ii1I * ii1IiI1i
    if 95 - 95: o0 + i11iIiiIii
    if 6 - 6: i111IiI / i11iIiiIii + oOo0oooo00o * Ii11111i
    if 80 - 80: o0OoOoOO00
  print "============================ POSTING ANALYTICS ============================"
  OoooO0oO ( I1OOO00O0O )
  if 83 - 83: oO0o . i11iIiiIii + o0OoOoOO00 . I11iIi1I * oO0o
  if not group == "None" :
   oooO0 = iiIiI + "?" + "utmwv=" + II1I + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( o0O0OOO0Ooo ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + IIIIiiIiI + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( IIIIiiIiI ) + "&utmac=" + o00oooO0Oo + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O0i1II1Iiii1I11 , "1" , "2" ] )
   if 46 - 46: IIIII
   if 60 - 60: I11iIi1I
   if 25 - 25: ii1IiI1i
   if 62 - 62: iiI1i1 + iiI
   if 98 - 98: I11iIi1I
   if 51 - 51: i1 - Ii11111i + o0OoOoOO00 * O00o0o0000o0o . oO0o + Ii11111i
   if 78 - 78: i11iIiiIii / oOo0oooo00o - O00o0o0000o0o / iiI1i1 + Ii11111i
   if 82 - 82: O00o0o0000o0o
   try :
    print "============================ POSTING TRACK EVENT ============================"
    OoooO0oO ( oooO0 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 46 - 46: iIiI . i11iIiiIii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 94 - 94: I11iIi1I * O00o0o0000o0o / i1 / O00o0o0000o0o
oO0 = iiIii ( sys . argv [ 2 ] )
O0OO0O = oO0 . get ( 'mode' )
II111iiii = oO0 . get ( 'url' )
OO = oO0 . get ( 'name' )
if type ( II111iiii ) == type ( str ( ) ) :
 II111iiii = urllib . unquote_plus ( II111iiii )
if type ( OO ) == type ( str ( ) ) :
 OO = urllib . unquote_plus ( OO )
 if 83 - 83: iiI / o0 - ii1IiI1i - iiI1i1
iI1i11iII111 = str ( sys . argv [ 1 ] )
if O0OO0O == 'index' :
 iii ( "Browse" , OO )
 IIII ( II111iiii )
elif O0OO0O == 'search' :
 iii ( "None" , "Search" )
 I1 ( )
elif O0OO0O == 'videosbyregion' :
 iii ( "Browse" , OO )
 IiII ( )
elif O0OO0O == 'videosbycategory' :
 iii ( "Browse" , OO )
 i1I1ii1II1iII ( )
elif O0OO0O == 'mirrors' :
 iii ( "Browse" , OO )
 i1Ii ( II111iiii )
elif O0OO0O == 'episodes' :
 iii ( "Browse" , OO )
 iIi ( II111iiii , OO )
elif O0OO0O == 'loadvideo' :
 iii ( "Play" , OO + "/" + II111iiii )
 Iii1IIII11I = xbmcgui . DialogProgress ( )
 Iii1IIII11I . create ( 'xomgiaitri.com' , 'Loading video. Please wait...' )
 I11ii1 ( II111iiii , OO )
 Iii1IIII11I . close ( )
 del Iii1IIII11I
else :
 iii ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( iI1i11iII111 ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
