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

import re
import urllib
import urlparse, sys
from bs4 import BeautifulSoup
import requests

from resources.lib.modules import cache
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import source_utils
from resources.lib.modules import dom_parser2
from resources.lib.modules import cfscrape


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['movie4k.is','movie4k.ws']
        self.base_link = 'https://movie4k.is'
        self.search_link = '/?s=%s'
        self.scraper = cfscrape.create_scraper()

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'title': title, 'year': year}
            return url
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []

            if url == None: return sources

            year = url['year']
            h = {'User-Agent': client.randomagent()}
            title = cleantitle.geturl(url['title']).replace('-', '+')
            url = urlparse.urljoin(self.base_link, self.search_link % title)
            r = self.scraper.get(url, headers=h)
            r = BeautifulSoup(r.text, 'html.parser').find('div', {'class': 'item'})
            r = r.find('a')['href']
            r = self.scraper.get(r, headers=h)
            r = BeautifulSoup(r.content, 'html.parser')
            quality = r.find('span', {'class': 'calidad2'}).text
            url = r.find('div', {'class':'movieplay'}).find('iframe')['src']
            if not quality in ['1080p', '720p']:
                quality = 'SD'

            valid, host = source_utils.is_host_valid(url, hostDict)
            sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': url, 'direct': False, 'debridonly': False})
            return sources
        except:
            return sources

    def resolve(self, url):
        try:
            return url
        except:
            return