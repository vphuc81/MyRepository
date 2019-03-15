# -*- coding: UTF-8 -*-
#######################################################################
 # ----------------------------------------------------------------------------
 # "THE BEER-WARE LICENSE" (Revision 42):
 # @tantrumdev wrote this file.  As long as you retain this notice you
 # can do whatever you want with this stuff. If we meet some day, and you think
 # this stuff is worth it, you can buy me a beer in return. - Muad'Dib
 # ----------------------------------------------------------------------------
#######################################################################

# Addon Name: Supremacy
# Addon id: plugin.video.Supremacy
# Addon Provider: Supremacy

import re
from resources.lib.modules import cleantitle
from resources.lib.modules import cfscrape
from resources.lib.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['playmovies.es']
        self.base_link = 'http://playmovies.es'
        self.search_link = '/%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title)
            url = self.base_link + self.search_link % title
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            scraper = cfscrape.create_scraper()
            r = scraper.get(url).content
            try:
                qual = re.compile('class="quality">(.+?)<').findall(r)
                print qual
                for i in qual:
                    if 'HD' in i:
                        quality = '1080p'
                    else:
                        quality = 'SD'
                match = re.compile('<iframe src="(.+?)"').findall(r)
                for url in match:
                    valid, host = source_utils.is_host_valid(url, hostDict)
                    sources.append({'source': host,'quality': quality,'language': 'en','url': url,'direct': False,'debridonly': False})
            except:
                return
        except Exception:
            return
        return sources

    def resolve(self, url):
        return url
