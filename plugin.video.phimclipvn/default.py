#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.phimclipvn'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = "http://phim.clip.vn"
ooo0OO = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
ooo0OO = xbmc . translatePath ( os . path . join ( ooo0OO , "icon.png" ) )
if 18 - 18: II111iiii . OOO0O / II1Ii / oo * OoO0O00
def IIiIiII11i ( ) :
 o0oOOo0O0Ooo ( 'Search' , '' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
 o0oOOo0O0Ooo ( 'Phim lẻ' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=1' , 'indexajax' , 'http://echipstore.net/addonicons/Movies.jpg' )
 o0oOOo0O0Ooo ( 'Phim lẻ theo Quốc gia' , 'http://m.phim.clip.vn' , 'moviesbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
 o0oOOo0O0Ooo ( 'Phim lẻ theo Thể loại' , 'http://m.phim.clip.vn' , 'moviesbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 o0oOOo0O0Ooo ( 'Phim bộ' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=2' , 'indexajax' , 'http://echipstore.net/addonicons/Series.jpg' )
 o0oOOo0O0Ooo ( 'Phim bộ theo Quốc gia' , 'http://m.phim.clip.vn' , 'seriesbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' )
 o0oOOo0O0Ooo ( 'Phim bộ theo Thế loại' , 'http://m.phim.clip.vn' , 'seriesbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' )
 o0oOOo0O0Ooo ( 'Tuyển tập' , 'http://m.phim.clip.vn/collections?p=1' , 'indexcollection' , 'http://echipstore.net/addonicons/Cinema.jpg' )
 o0oOOo0O0Ooo ( 'Phim chiếu rạp' , 'http://m.phim.clip.vn/cinema?p=1' , 'index' , 'http://echipstore.net/addonicons/Cinema.jpg' )
 if 2 - 2: o0 * i1 * ii1IiI1i % OOooOOo / I11i / Ii1I
 IiiIII111iI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 if 49 - 49: IiiIII111iI = xbmc . translatePath ( os . path . join ( IiiIII111iI , "temp.jpg" ) )
 if 49 - 49: urllib . urlretrieve ( 'https://googledrive.com/host/0B-ygKtjD8Sc-S04wUUxMMWt5dmM/images/clipvn.jpg' , IiiIII111iI )
 if 49 - 49: IiII = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiiIII111iI )
 if 49 - 49: iI1Ii11111iIi = xbmcgui . WindowDialog ( )
 if 49 - 49: iI1Ii11111iIi . addControl ( IiII )
 if 49 - 49: iI1Ii11111iIi . doModal ( )
 if 41 - 41: I1II1
def Ooo0OO0oOO ( m ) :
 o0oOOo0O0Ooo ( 'Việt Nam' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=viet-nam' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hàn Quốc' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=han-quoc' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Trung Quốc' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=trung-quoc' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hồng Kông' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=hong-kong' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Đài Loan' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=dai-loan' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Thái Lan' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=thai-lan' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Philippines' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=philippines' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Malaysia' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=malaysia' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Anh' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=anh' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Mỹ' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=my' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Nga' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=nga' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Ý' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=y' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Pháp' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=phap' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Đức' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=duc' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Nhật' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=nhat' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Ấn Độ' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=an-do' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Tây Ban Nha' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=tay-ban-nha' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Canada' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=ca-na-da' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Úc' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=uc' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Na Uy' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=na-uy' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Kazakhstan' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=kazakhstan' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Venezuela' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=venezuela' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Nam Phi' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=nam-phi' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Mexico' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=mexico' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hà Lan' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=ha-lan' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'New Zealand' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=new-zealand' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Đan Mạch' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=dan-mach' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Áo' , 'http://m.phim.clip.vn/browse?m=%s&p=1&c=ao' % m , 'indexajax' , 'icon' )
 if 86 - 86: oO0o
def IIII ( m ) :
 o0oOOo0O0Ooo ( 'Hài hước' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=hai-huoc' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Võ thuật' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=vo-thuat' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hoạt hình' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=hoat-hinh' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hành động' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=hanh-dong' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Tình cảm lãng mạn' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=tinh-cam-lang-man' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Kinh dị - Bí ẩn' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=kinh-di-bi-an' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Phiêu lưu' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=phieu-luu' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Khoa học viễn tưởng' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=khoa-hoc-vien-tuong' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Hình sự' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=hinh-su' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Thần thoại' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=than-thoai' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Lịch sử - Tiểu sử' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=lich-su-tieu-su' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Cổ trang' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=co-trang' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Gia đình' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=gia-dinh' % m , 'indexajax' , 'icon' )
 o0oOOo0O0Ooo ( 'Tâm lý' , 'http://m.phim.clip.vn/film/ajaxLoadMoreFilm?p=1&m=%s&g=tam-ly' % m , 'indexajax' , 'icon' )
 if 59 - 59: II1i * o00ooo0 / o00 * Oo0oO0ooo
def o0oOoO00o ( url ) :
 i1oOOoo00O0O = i1111 ( url )
 i11 = int ( re . compile ( 'p=(\d+)' ) . findall ( url ) [ 0 ] ) + 1
 I11 = re . compile ( '<li class="item clearfix"><a href="(.+?)"><div [^>]*><img [^>]* src="(.+?)"/></div><div [^>]*><span [^>]*>(.+?)</span><span [^>]*>(.+?)</span><span [^>]*>(.+?)</span>' ) . findall ( i1oOOoo00O0O )
 for Oo0o0000o0o0 , oOo0oooo00o , oO0o0o0ooO0oO , oo0o0O00 , oO in I11 :
  o0oOOo0O0Ooo ( "[B]%s - %s[/B] (%s)" % ( oO0o0o0ooO0oO , oo0o0O00 , oO ) , Oo0o0000o0o0 , 'episodes' , oOo0oooo00o )
 o0oOOo0O0Ooo ( "[B]Next Page >>[/B]" , re . sub ( 'p=(\d+)' , 'p=%s' % i11 , url ) , 'indexajax' , ooo0OO )
 i1iiIIiiI111 = xbmc . getSkinDir ( )
 if i1iiIIiiI111 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 62 - 62: iIIIIiI - OoOO
def I1iiiiI1iII ( url ) :
 i1oOOoo00O0O = i1111 ( url )
 i11 = int ( re . compile ( 'p=(\d+)' ) . findall ( url ) [ 0 ] ) + 1
 I11 = re . compile ( '<a title="(.+?)" href="(.+?)"><img src="(.+?)" [^>]*>' ) . findall ( i1oOOoo00O0O )
 for IiIi11i , Oo0o0000o0o0 , oOo0oooo00o in I11 :
  o0oOOo0O0Ooo ( "[B]%s[/B]" % IiIi11i , Oo0o0000o0o0 , 'episodes' , oOo0oooo00o )
 o0oOOo0O0Ooo ( "[B]Next Page >>[/B]" , re . sub ( 'p=(\d+)' , 'p=%s' % i11 , url ) , 'indexcollection' , ooo0OO )
 i1iiIIiiI111 = xbmc . getSkinDir ( )
 if i1iiIIiiI111 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 43 - 43: I11i * II111iiii
def I111I11 ( url ) :
 i1oOOoo00O0O = i1111 ( url )
 i11 = int ( re . compile ( 'p=(\d+)' ) . findall ( url ) [ 0 ] ) + 1
 I11 = re . compile ( '<li [^>]*><a href="(.+?)"><div [^>]*><img[^>]*src="(.+?)"[^>]*></div><div [^>]*><span [^>]*>(.+?)</span><span [^>]*>(.+?)</span><span [^>]*>(.+?)</span>' ) . findall ( i1oOOoo00O0O )
 for Oo0o0000o0o0 , oOo0oooo00o , oO0o0o0ooO0oO , oo0o0O00 , oO in I11 :
  o0oOOo0O0Ooo ( "[B]%s - %s[/B] (%s)" % ( oO0o0o0ooO0oO , oo0o0O00 , oO ) , iiiii + Oo0o0000o0o0 , 'episodes' , oOo0oooo00o )
 if ( "cinema" not in url ) :
  o0oOOo0O0Ooo ( "[B]Next Page >>[/B]" , re . sub ( 'p=(\d+)' , 'p=%s' % i11 , url ) , 'index' , ooo0OO )
 i1iiIIiiI111 = xbmc . getSkinDir ( )
 if i1iiIIiiI111 == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 62 - 62: o00 - Oo0oO0ooo - OOooOOo % oo / I1II1
def OoooooOoo ( ) :
 try :
  OO = xbmc . Keyboard ( '' , 'Enter search text' )
  OO . doModal ( )
  if ( OO . isConfirmed ( ) ) :
   oO0O = urllib . quote_plus ( OO . getText ( ) )
  OOoO000O0OO = 'http://m.phim.clip.vn/search?p=1&keyword=' + oO0O + '/'
  I111I11 ( OOoO000O0OO )
 except : pass
 if 23 - 23: i11iIiiIii + o0
def oOo ( url , name ) :
 i1oOOoo00O0O = i1111 ( url )
 oOoOoO = re . compile ( '<div class="item active">(.+?)</div>' ) . findall ( i1oOOoo00O0O )
 if len ( oOoOoO ) > 0 :
  oOoOoO = re . compile ( '<a href="(.+?)" [^>]*>(.+?)</a>' ) . findall ( oOoOoO [ 0 ] )
  for ii1I , OooO0 in oOoOoO :
   OooO0 = re . sub ( '<.*?>' , '' , OooO0 )
   ii1I = "http://m.clip.vn/embed/" + re . compile ( ',(.+?)/' ) . findall ( ii1I ) [ 0 ]
   II11iiii1Ii ( "[%s] Part - %s" % ( urllib . unquote_plus ( name ) , OooO0 . strip ( ) . encode ( "utf-8" ) ) , ii1I , 'loadvideo' , '' , name . encode ( "utf-8" ) )
 else :
  ii1I = re . compile ( '<link rel="alternate" href="(.+?)" media="handheld"/>' ) . findall ( i1oOOoo00O0O ) [ 0 ]
  ii1I = "http://m.clip.vn/embed/" + ii1I . split ( "," ) [ 1 ]
  II11iiii1Ii ( "Play %s" % urllib . unquote_plus ( name ) , ii1I , 'loadvideo' , '' , name . encode ( "utf-8" ) )
  if 70 - 70: I1II1 / OOO0O % OoOO % i11iIiiIii . o0
def O0o0Oo ( url , name ) :
 Oo00OOOOO = O0O ( url )
 O00o0OO = re . compile ( '<a href="javascript:" onclick="CLIP.play(.+?)">' ) . findall ( Oo00OOOOO ) [ 0 ]
 I11i1 ( "direct" , O00o0OO . replace ( '("' , '' ) . replace ( '")' , '' ) . encode ( "utf-8" ) )
 if 25 - 25: i1 - Oo0oO0ooo . II1Ii
def I11i1 ( videoType , videoId ) :
 OOoO000O0OO = ""
 if ( videoType == "youtube" ) :
  OOoO000O0OO = 'plugin://plugin.video.youtube?path=/root/video&action=play_video&videoid=' + videoId . replace ( '?' , '' )
  xbmc . executebuiltin ( "xbmc.PlayMedia(" + OOoO000O0OO + ")" )
 elif ( videoType == "vimeo" ) :
  OOoO000O0OO = 'plugin://plugin.video.vimeo/?action=play_video&videoID=' + videoId
 elif ( videoType == "tudou" ) :
  OOoO000O0OO = 'plugin://plugin.video.tudou/?mode=3&url=' + videoId
 else :
  I11ii1 = xbmc . Player ( )
  I11ii1 . play ( videoId )
  if 9 - 9: o00ooo0 + I1II1 % o00ooo0 + oo . oO0o
def i1111 ( url ) :
 III1i1i = urllib2 . Request ( url )
 iiI1 = urllib2 . urlopen ( III1i1i )
 i1oOOoo00O0O = iiI1 . read ( )
 iiI1 . close ( )
 i1oOOoo00O0O = '' . join ( i1oOOoo00O0O . splitlines ( ) ) . replace ( '\'' , '"' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\n' , '' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\t' , '' )
 i1oOOoo00O0O = re . sub ( '  +' , ' ' , i1oOOoo00O0O )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '> <' , '><' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '" >' , '">' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '" />' , '"/>' )
 return i1oOOoo00O0O
 if 19 - 19: II1i + OoOO
def O0O ( url ) :
 III1i1i = urllib2 . Request ( url )
 III1i1i . add_header ( 'User-Agent' , 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; da-dk) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3' )
 iiI1 = urllib2 . urlopen ( III1i1i )
 i1oOOoo00O0O = iiI1 . read ( )
 iiI1 . close ( )
 i1oOOoo00O0O = '' . join ( i1oOOoo00O0O . splitlines ( ) ) . replace ( '\'' , '"' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\n' , '' )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '\t' , '' )
 i1oOOoo00O0O = re . sub ( '  +' , ' ' , i1oOOoo00O0O )
 i1oOOoo00O0O = i1oOOoo00O0O . replace ( '> <' , '><' )
 return i1oOOoo00O0O
 if 53 - 53: II1Ii . oo
def II11iiii1Ii ( name , url , mode , iconimage , mirrorname ) :
 ii1I1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&mirrorname=" + urllib . quote_plus ( mirrorname )
 OOoo0O0 = True
 iiiIi1i1I = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 iiiIi1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOoo0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1I1i1I , listitem = iiiIi1i1I )
 return OOoo0O0
 if 80 - 80: OOooOOo - ii1IiI1i
def o0oOOo0O0Ooo ( name , url , mode , iconimage ) :
 ii1I1i1I = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOoo0O0 = True
 iiiIi1i1I = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 iiiIi1i1I . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOoo0O0 = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = ii1I1i1I , listitem = iiiIi1i1I , isFolder = True )
 return OOoo0O0
 if 87 - 87: I1II1 / II1i - oo * oO0o / II1Ii . II111iiii
def iii11I111 ( parameters ) :
 OOOO00ooo0Ooo = { }
 if 69 - 69: I11i * II111iiii + ii1IiI1i . OoO0O00 / II111iiii
 if parameters :
  O000oo0O = parameters [ 1 : ] . split ( "&" )
  for OOOO in O000oo0O :
   i11i1 = OOOO . split ( '=' )
   if ( len ( i11i1 ) ) == 2 :
    OOOO00ooo0Ooo [ i11i1 [ 0 ] ] = i11i1 [ 1 ]
 return OOOO00ooo0Ooo
 if 29 - 29: Ii1I % o0 + OoOO / I11i + oO0o * I11i
i1I1iI = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 93 - 93: OOO0O % I1II1 * oo
if os . path . exists ( i1I1iI ) == False :
 os . mkdir ( i1I1iI )
Ii11Ii1I = os . path . join ( i1I1iI , 'visitor' )
if 72 - 72: o00 / oo * i1 - iIIIIiI
if os . path . exists ( Ii11Ii1I ) == False :
 from random import randint
 Oo0O0O0ooO0O = open ( Ii11Ii1I , "w" )
 Oo0O0O0ooO0O . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 Oo0O0O0ooO0O . close ( )
 if 15 - 15: Ii1I + OOooOOo - II1Ii / oO0o
def oo000OO00Oo ( k , e ) :
 O0OOO0OOoO0O = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O00Oo000ooO0 in range ( len ( e ) ) :
  OoO0O00IIiII = k [ O00Oo000ooO0 % len ( k ) ]
  o0ooOooo000oOO = chr ( ( 256 + ord ( e [ O00Oo000ooO0 ] ) - ord ( OoO0O00IIiII ) ) % 256 )
  O0OOO0OOoO0O . append ( o0ooOooo000oOO )
 return "" . join ( O0OOO0OOoO0O )
 if 59 - 59: OoO0O00 + II1Ii * OOooOOo + oo
def Oo0OoO00oOO0o ( utm_url ) :
 OOO00O = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  III1i1i = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : OOO00O }
 )
  iiI1 = urllib2 . urlopen ( III1i1i ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iiI1
 if 84 - 84: I1II1 * ii1IiI1i / II1i - II111iiii
def IiI1 ( group , name ) :
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
  Oo0O00Oo0o0 = "1.0"
  O00O0oOO00O00 = open ( Ii11Ii1I ) . read ( )
  i1Oo00 = "ClipVN"
  i1i = "UA-52209804-2"
  iiI111I1iIiI = "www.viettv24.com"
  II = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
   if 65 - 65: o00ooo0 . OOO0O / II111iiii - o00ooo0
   if 21 - 21: o0 * OOO0O
   if 91 - 91: Oo0oO0ooo
   if 15 - 15: OoO0O00
   if 18 - 18: i11iIiiIii . oo % II1Ii / II111iiii
  else :
   if group == "None" :
    Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 + "/" + name ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
    if 75 - 75: OOooOOo % I11i % I11i . iIIIIiI
    if 5 - 5: I11i * OoOO + OOooOOo . oO0o + OOooOOo
    if 91 - 91: II111iiii
    if 61 - 61: OoO0O00
    if 64 - 64: OoOO / OOooOOo - II111iiii - II1i
   else :
    Ii1I1IIii1II = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( i1Oo00 + "/" + group + "/" + name ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , O00O0oOO00O00 , "1" , "1" , "2" ] )
    if 86 - 86: II1i % OOooOOo / o0 / OOooOOo
    if 42 - 42: ii1IiI1i
    if 67 - 67: iIIIIiI . o00 . II111iiii
    if 10 - 10: Ii1I % Ii1I - OOO0O / oO0o + o00ooo0
    if 87 - 87: I1II1 * Ii1I + oO0o / OOO0O / o00
    if 37 - 37: o00 - OoOO * I1II1 % i11iIiiIii - iIIIIiI
  print "============================ POSTING ANALYTICS ============================"
  Oo0OoO00oOO0o ( Ii1I1IIii1II )
  if 83 - 83: II1i / o0
  if not group == "None" :
   iIIiIi1iIII1 = II + "?" + "utmwv=" + Oo0O00Oo0o0 + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iiI111I1iIiI ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + i1Oo00 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( i1Oo00 ) + "&utmac=" + i1i + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , O00O0oOO00O00 , "1" , "2" ] )
   if 78 - 78: II111iiii . I1II1 . OoO0O00 % oO0o
   if 49 - 49: o00ooo0 / ii1IiI1i . OoO0O00
   if 68 - 68: i11iIiiIii % Ii1I + i11iIiiIii
   if 31 - 31: OoO0O00 . o0
   if 1 - 1: i1 / I11i % o00 * Oo0oO0ooo . i11iIiiIii
   if 2 - 2: Ii1I * II1i - OOO0O + o0 . I1II1 % o00
   if 92 - 92: o00
   if 25 - 25: i1 - o0 / II1Ii / I11i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    Oo0OoO00oOO0o ( iIIiIi1iIII1 )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 12 - 12: o0 * o00 % oo % OOO0O
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 20 - 20: oO0o % o00ooo0 / o00ooo0 + o00ooo0
III1IiiI = iii11I111 ( sys . argv [ 2 ] )
iI = III1IiiI . get ( 'mode' )
OOoO000O0OO = III1IiiI . get ( 'url' )
i1IIIII11I1IiI = III1IiiI . get ( 'name' )
if type ( OOoO000O0OO ) == type ( str ( ) ) :
 OOoO000O0OO = urllib . unquote_plus ( OOoO000O0OO )
 if 16 - 16: OOO0O
oOooOOOoOo = str ( sys . argv [ 1 ] )
if iI == 'index' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 I111I11 ( OOoO000O0OO )
elif iI == 'indexajax' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 o0oOoO00o ( OOoO000O0OO )
elif iI == 'indexcollection' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 I1iiiiI1iII ( OOoO000O0OO )
elif iI == 'search' :
 IiI1 ( "None" , "Search" )
 OoooooOoo ( )
elif iI == 'moviesbyregion' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 Ooo0OO0oOO ( "1" )
elif iI == 'moviesbycategory' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 IIII ( "1" )
elif iI == 'seriesbyregion' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 Ooo0OO0oOO ( "2" )
elif iI == 'seriesbycategory' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 IIII ( "2" )
elif iI == 'episodes' :
 IiI1 ( "Browse" , i1IIIII11I1IiI )
 oOo ( OOoO000O0OO , i1IIIII11I1IiI )
elif iI == 'loadvideo' :
 IiI1 ( "Play" , i1IIIII11I1IiI + "/" + OOoO000O0OO )
 i1Iii1i1I = xbmcgui . DialogProgress ( )
 i1Iii1i1I . create ( 'ClipVN' , 'Loading video. Please wait...' )
 O0o0Oo ( OOoO000O0OO , i1IIIII11I1IiI )
 i1Iii1i1I . close ( )
 del i1Iii1i1I
else :
 IiI1 ( "None" , "None" )
 IIiIiII11i ( )
xbmcplugin . endOfDirectory ( int ( oOooOOOoOo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
