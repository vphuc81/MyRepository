# -*- coding: UTF-8 -*-

'''
    PlayScrapers module
'''


import re

from playscrapers.modules import client
from playscrapers.modules import dom_parser
from playscrapers.modules import source_utils
from playscrapers.modules import log_utils
from playscrapers import urljoin

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['imdbbox.com']
        self.base_link = custom_base or 'https://imdbbox.com'
        self.search_link = '/d/movie/%s'
        self.search2_link = '/e/movie/%s'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = imdb
            return url
        except Exception:
            log_utils.log('imdbbox Exception', 1)
            return


    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:
            hostDict = hostprDict + hostDict
            if url == None:
                return sources
            imdb = url

            try:
                url = urljoin(self.base_link, self.search_link % imdb)
                html = client.r_request(url)
                items = dom_parser.parse_dom(html, 'a', req='class')
                for item in items:
                    try:
                        link = item.attrs['href']
                        try:
                            link = re.findall('&url=(.+?)&format=', link)[0]
                        except:
                            link = link.split('&url=')[1]
                        link = "https:" + link if not link.startswith('http') else link
                        qual = item.content
                        #log_utils.log('imdbbox search_link2 link: \n' + repr(link))
                        valid, host = source_utils.is_host_valid(link, hostDict)
                        host = host.replace('uptobox', 'uptb')
                        quality, info = source_utils.get_release_quality(qual, link)
                        sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'info': info, 'direct': True, 'debridonly': False})
                    except:
                        pass
            except:
                url2 = urljoin(self.base_link, self.search2_link % imdb)
                html2 = client.r_request(url2)
                regex = r'''\{\s*file:\s*"(.+?)",\s*label:\s*"(.+?)"\s*\}'''
                urls = re.compile(regex).findall(html2)
                if urls:
                    for link, qual in urls:
                        link =  "https:" + link if not link.startswith('http') else link
                        log_utils.log('imdbbox search_link link: \n' + repr(link))
                        valid, host = source_utils.is_host_valid(link, hostDict)
                        quality, info = source_utils.get_release_quality(qual, link)
                        sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'info': info, 'direct': False, 'debridonly': False})

            return sources
        except:
            log_utils.log('imdbbox Exception', 1)
            return sources


    def resolve(self, url):
        return url

