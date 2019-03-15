# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Yoda
# Addon id: plugin.video.Yoda
# Addon Provider: Supremacy

import re,urllib,urlparse

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import proxy


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['watchepisodes4.com']
        self.base_link = 'https://watchepisodes4.com/'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(tvshowtitle)
            url = self.base_link + clean_title
            return url
        except:
            return
 
    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url: return
            r = client.request(url)
            try:
                match = re.compile('<a title=".+? Season '+season+' Episode '+episode+' .+?" href="(.+?)">',re.DOTALL).findall(r)
                for url in match: return url
            except:
                return
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = client.request(url)
            match = re.compile('class="watch-button" data-actuallink="(.+?)://(.+?)/(.+?)"',re.DOTALL).findall(r)
            for http,host,ext in match:
                url = '%s://%s/%s' % (http,host,ext)
                sources.append({'source': host,'quality': 'SD','language': 'en','url': url,'direct': False,'debridonly': False}) 
        except Exception:
            return

        return sources

    def resolve(self, url):
        return url