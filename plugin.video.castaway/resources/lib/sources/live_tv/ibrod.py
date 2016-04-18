from __future__ import unicode_literals
from resources.lib.modules import client, webutils
from BeautifulSoup import BeautifulSoup as bs
import re,sys,xbmcgui,os
from addon.common.addon import Addon
addon = Addon('plugin.video.castaway', sys.argv)

AddonPath = addon.get_path()
IconPath = AddonPath + "/resources/media/"
def icon_path(filename):
    return os.path.join(IconPath, filename)


class info():
    def __init__(self):
    	self.mode = 'ibrod'
        self.name = 'iBrod.tv'
        self.icon = 'ibrod.png'
        self.paginated = False
        self.categorized = False
        self.multilink = False
class main():
	def __init__(self):
		self.base = 'http://www.ibrod.tv'

	def channels(self):
		soup = webutils.get_soup(self.base)
		headers = soup.findAll('a',{'class':'menuitem submenuheader'})
		headers.pop(0)
		items = soup.findAll('div',{'class':'submenu'})
		items.pop(0)
		events = self.__prepare_channels(headers,items)

		return events

	def __prepare_channels(self,headers,items):
		new=[]
		i = 0
		for header in headers:
			new.append(('','[COLOR yellow]%s[/COLOR]'%header.getText(),info().icon))
			channels = items[i].findAll('li')
			for channel in channels:
				url = self.base + '/' + channel.find('a')['href']
				title = channel.getText()
				new.append((url,title,icon_path(info().icon)))
			i+=1
		return new

	def resolve(self,url):
		import liveresolver
		return liveresolver.resolve(url)


