

import re
import traceback

from resources.lib.modules import cfscrape, client, log_utils, source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['hackimdb.com']
        self.base_link = 'https://hackimdb.com'
        self.search_link = '/title/&%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            url = self.base_link + self.search_link % imdb
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('HackIMDB - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            scraper = cfscrape.create_scraper()
            r = scraper.get(url).content
            try:
                match = re.compile('<iframe .+?src="(.+?)"').findall(r)
                for url in match:
                    if 'youtube' in url:
                        continue
                    valid, hoster = source_utils.is_host_valid(url, hostDict)
                    if not valid:
                        continue
                    sources.append({
                        'source': hoster,
                        'quality': 'SD',
                        'language': 'en',
                        'url': url,
                        'direct': False,
                        'debridonly': False
                    })
            except Exception:
                return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('HackIMDB - Exception: \n' + str(failure))
            return sources
        return sources

    def resolve(self, url):
        return url
