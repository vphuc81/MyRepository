

import re
import traceback

from resources.lib.modules import cfscrape, cleantitle, log_utils, source_utils


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
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLAYMOVIES - Exception: \n' + str(failure))
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
                    sources.append({'source': host, 'quality': quality, 'language': 'en',
                                    'url': url, 'direct': False, 'debridonly': False})
            except Exception:
                return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PLAYMOVIES - Exception: \n' + str(failure))
            return sources
        return sources

    def resolve(self, url):
        return url
