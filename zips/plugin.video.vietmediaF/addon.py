import xbmcaddon, xbmc, os, xbmcgui
import datetime as dt, time
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

def TextBoxes(heading,announce):
	class TextBox():
		WINDOW=10147
		CONTROL_LABEL=1
		CONTROL_TEXTBOX=5
		def __init__(self,*args,**kwargs):
			xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) 
			self.win=xbmcgui.Window(self.WINDOW) 
			xbmc.sleep(500) # 
			self.setControls()
		def setControls(self):
			self.win.getControl(self.CONTROL_LABEL).setLabel(heading) # set heading
			try: f=open(announce); text=f.read()
			except: text=announce
			self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
			return
	TextBox()
	while xbmc.getCondVisibility('Window.IsVisible(10147)'):
		time.sleep(.5)