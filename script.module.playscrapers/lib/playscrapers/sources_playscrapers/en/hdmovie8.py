# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 10-16-2019 by PressPlay in PressPlay.
# py2/3 compatibility fix for PressPlay

import re

from six import ensure_text

from playscrapers.modules import cleantitle
from playscrapers.modules import source_utils
from playscrapers import cfScraper
from playscrapers import urljoin

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['hdmovie8.com']
        self.base_link = custom_base or 'https://hdmovie8.com'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            movietitle = cleantitle.geturl(title)
            url = urljoin(self.base_link, '/movies/%s-%s/' % (movietitle, year))
            return url
        except:
            return


    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = cleantitle.geturl(tvshowtitle)
            return url
        except:
            return


    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None:
                return
            tvshowtitle = url
            url = urljoin(self.base_link, '/episodes/%s-%sx%s/' % (tvshowtitle, season, episode))
            return url
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            if url == None:
                return sources
            hostDict = hostDict + hostprDict
            sourcePage = ensure_text(cfScraper.get(url).content, errors='replace')
            thesources = re.compile('<tbody>(.+?)</tbody>', re.DOTALL).findall(sourcePage)[0]
            links = re.compile("<a href=\'(.+?)\' target=\'_blank\'>Download</a>", re.DOTALL).findall(thesources)
            for link in links:
                linkPage = ensure_text(cfScraper.get(link).content, errors='replace')
                vlink = re.compile('<a id="link" rel="nofollow" href="(.+?)" class="btn"', re.DOTALL).findall(linkPage)
                for zlink in vlink:
                    valid, host = source_utils.is_host_valid(zlink, hostDict)
                    if valid:
                        quality, info = source_utils.get_release_quality(zlink, zlink)
                        sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': zlink, 'info': info, 'direct': False, 'debridonly': False})
            return sources
        except:
            return sources


    def resolve(self, url):
        return url


