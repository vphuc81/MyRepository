import xbmcaddon, xbmc, os, xbmcgui

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo("id")
ADDON_NAME = ADDON.getAddonInfo("name")
ADDON_PROFILE = ADDON.getAddonInfo("profile")
LOG = xbmc.translatePath('special://logpath/')
PROFILE = xbmc.translatePath('special://profile/')

def notify(message='', header=None, time=5000, image=None):
  	if header is None:
  		header = ADDON_NAME
  	if image is None:
  		path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
    	image = xbmc.translatePath(os.path.join(path, "icon.png"))
  	xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' % (header, message, time, image))

def notify1(message='', header=None, time=10000, image=None):
  	if header is None:
  		header = ADDON_NAME
  	if image is None:
  		path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('path')).decode("utf-8")
    	image = xbmc.translatePath(os.path.join(path, "icon.png"))
  	xbmc.executebuiltin('Notification("%s", "%s", "%d", "%s")' % (header, message, time, image))

def alert(message,title="VietMedia"):
  	xbmcgui.Dialog().ok(title,"",message)