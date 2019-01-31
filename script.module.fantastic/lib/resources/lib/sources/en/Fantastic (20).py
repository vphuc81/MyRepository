

import re
import traceback

from resources.lib.modules import cleantitle, client, log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['putlocker.onl']
        self.base_link = 'https://www5.putlocker.onl/'
        self.tv_link = '/show/%s/season/%s/episode/%s'
        self.movie_link = '/movie/%s'

    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            title = cleantitle.geturl(title)
            url = self.base_link + self.movie_link % title
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockerONL - Exception: \n' + str(failure))
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            tvshowtitle = cleantitle.geturl(tvshowtitle)
            url = tvshowtitle
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockerONL - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return
            tvshowtitle = url
            url = self.base_link + self.tv_link % (tvshowtitle, season, episode)
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockerONL - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = client.request(url)
            try:
                match = re.compile('<IFRAME.+?SRC=.+?//(.+?)/(.+?)"').findall(r)
                for host, url in match:
                    url = 'http://%s/%s' % (host, url)
                    host = host.replace('www.', '')
                    sources.append({
                        'source': host,
                        'quality': 'SD',
                        'language': 'en',
                        'url': url,
                        'direct': False,
                        'debridonly': False
                    })
            except Exception:
                failure = traceback.format_exc()
                log_utils.log('PutlockerONL - Exception: \n' + str(failure))
                return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockerONL - Exception: \n' + str(failure))
            return sources
        return sources

    def resolve(self, url):
        return url
