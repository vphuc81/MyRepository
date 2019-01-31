

import re
import traceback

from resources.lib.modules import cleantitle, client, log_utils, proxy


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['my-project-free.tv']
        self.base_link = 'https://www8.project-free-tv.ag/'
        self.search_link = '/episode/%s-season-%s-episode-%s'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(tvshowtitle)
            url = clean_title
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('MyProjectFreeTV - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return
            tvshowtitle = url
            url = self.base_link + self.search_link % (tvshowtitle, int(season), int(episode))
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('MyProjectFreeTV - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = client.request(url)
            try:
                data = re.compile("callvalue\('.+?','.+?','(.+?)://(.+?)/(.+?)'\)", re.DOTALL).findall(r)
                for http, host, url in data:
                    url = '%s://%s/%s' % (http, host, url)
                    sources.append({
                        'source': host,
                        'quality': 'SD',
                        'language': 'en',
                        'url': url,
                        'direct': False,
                        'debridonly': False
                    })
            except Exception:
                pass
            return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('MyProjectFreeTV - Exception: \n' + str(failure))
            return

    def resolve(self, url):
        return url
