from __future__ import unicode_literals
from resources.lib.modules import client,webutils,control
from resources.lib.modules.log_utils import log
import re,os

AddonPath = control.addonPath
IconPath = AddonPath + "/resources/media/"
def icon_path(filename):
    return os.path.join(IconPath, filename)


class info():
    def __init__(self):
    	self.mode = 'videosport'
        self.name = 'antenasport.com'
        self.icon = 'live.png'
        self.paginated = False
        self.categorized = False
        self.multilink = False

class main():
	def __init__(self):
		self.base = 'http://antenasport.com'

	def channels(self):
		html = client.request(self.base)
		channels = webutils.bs(html).findAll('a',{'target':'_top'})
		events = self.__prepare_channels(channels)
		return events

	def __prepare_channels(self,channels):
		new=[]
		urls=[]
		img= icon_path(info().icon)
		for channel in channels:
			url = channel['href']
			if self.base not in url:
				if 'http:' in url:
					continue
				url = self.base + '/' + url
			title = channel.getText()
			if url not in urls:
				new.append((url,title,img))
				urls.append(url)
		return new



	def resolve(self,url):
		import liveresolver
		return liveresolver.resolve(url,cache_timeout=0)