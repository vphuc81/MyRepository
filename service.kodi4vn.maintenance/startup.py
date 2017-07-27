#!/usr/bin/python
#coding=utf-8
import os , xbmc , urllib , zipfile , contextlib , re , platform
if 64 - 64: i11iIiiIii
def OO0o ( ) :
 Oo0Ooo = xbmc . translatePath ( "special://temp" )
 O0O0OO0O0O0 = next ( os . walk ( Oo0Ooo ) ) [ 2 ]
 if 5 - 5: iiI / ii1I
 for ooO0OO000o in O0O0OO0O0O0 :
  if ".fi" in ooO0OO000o :
   os . remove ( os . path . join ( Oo0Ooo , ooO0OO000o ) )
   if 4 - 4: IiII1IiiIiI1 / iIiiiI1IiI1I1
def o0OoOoOO00 ( ) :
 if "armv8l" in platform . uname ( ) :
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.useamcodec", "value":false},"id":1}' )
 else :
  xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.useamcodec", "value":true},"id":1}' )
  if 27 - 27: OOOo0 / Oo - Ooo00oOo00o . I1IiI
def o0OOO ( ) :
 iIiiiI = xbmc . translatePath ( 'special://home/addons' )
 if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
 o0oO0 = xbmc . translatePath ( 'special://temp' )
 oo00 = False
 if 88 - 88: O0Oo0oO0o . II1iI . i1iIii1Ii1II
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://home/addons/repository.smash' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "http://mediarepos.net/Repos/smashrepo/repository.smash/repository.smash-1.1.3.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( iIiiiI )
   oo00 = True
 except : pass
 if 86 - 86: iiiii11iII1 % O0o
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://home/addons/repository.podgod' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "http://offshoregit.com/podgod/repo/zips/repository.podgod/repository.podgod-1.7.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( iIiiiI )
   oo00 = True
 except : pass
 if 97 - 97: I1IiI . iiIIIII1i1iI
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://home/addons/repository.unofficialsportsdevil-' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "https://offshoregit.com/unofficialsportsdevil/repository.unofficialsportsdevil/repository.unofficialsportsdevil-1.0.0.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( iIiiiI )
   oo00 = True
 except : pass
 if 32 - 32: Ooo00oOo00o - OOOo0 - i11iIiiIii % iiiii11iII1
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://home/addons/repository.cthlo-kodi-repo' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "https://cthlo.github.io/cthlo-kodi-repo/zips/repository.cthlo-kodi-repo/repository.cthlo-kodi-repo-1.0.0.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( iIiiiI )
   oo00 = True
 except : pass
 if 54 - 54: oO0o0ooO0 % iiI + Oo - II1iI / iiIIIII1i1iI
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://home/addons/xbmc.repo.xshare' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "https://github.com/thaitni/xbmc.repo.xshare/raw/master/xbmc.repo.xshare/xbmc.repo.xshare-1.0.0.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( iIiiiI )
   oo00 = True
 except : pass
 if 31 - 31: I1IiI + OOOo0
 try :
  i1I1Iiii1111 = xbmc . translatePath ( 'special://profile/addon_data/xbmc.repo.xshare' )
  if not os . path . isdir ( i1I1Iiii1111 ) :
   i11 = "https://thongld.github.io/plugin.video.xshare.zip"
   I11 = xbmc . translatePath ( os . path . join ( o0oO0 , "temp.zip" ) )
   urllib . urlretrieve ( i11 , I11 )
   with contextlib . closing ( zipfile . ZipFile ( I11 , "r" ) ) as Oo0o0000o0o0 :
    Oo0o0000o0o0 . extractall ( xbmc . translatePath ( 'special://profile/addon_data' ) )
   oo00 = True
 except : pass
 if 13 - 13: oO0o0ooO0 * ii1II11I1ii1I * Oo
 if oo00 :
  xbmc . executebuiltin ( "XBMC.UpdateLocalAddons()" )
  xbmc . executebuiltin ( "XBMC.UpdateAddonRepos()" )
  if 55 - 55: OOOo0
try :
 o0OoOoOO00 ( )
except : pass
try :
 OO0o ( )
except : pass
try :
 o0OOO ( )
except : pass
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
