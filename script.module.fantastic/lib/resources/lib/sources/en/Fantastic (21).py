

import base64
import re
import traceback

from resources.lib.modules import cleantitle, client, log_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['putlockers.gs']
        self.base_link = 'http://www1.putlockers.gs/'
        self.search_link = '/search-movies/%s.html'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = cleantitle.geturl(tvshowtitle)
            url = url.replace('-', '+')
            return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockersGS - Exception: \n' + str(failure))
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if not url:
                return
            query = url + '+season+' + season
            find = query.replace('+', '-')
            url = self.base_link + self.search_link % query
            r = client.request(url)
            match = re.compile('<a href="http://putlockers.gs/watch/(.+?)-' + find + '.html"').findall(r)
            for url_id in match:
                url = 'http://putlockers.gs/watch/' + url_id + '-' + find + '.html'
                r = client.request(url)
                match = re.compile('<a class="episode episode_series_link" href="(.+?)">' + episode + '</a>').findall(r)
                for url in match:
                    return url
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockersGS - Exception: \n' + str(failure))
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = client.request(url)
            try:
                match = re.compile(
                    '<p class="server_version"><img src="http://putlockers.gs/themes/movies/img/icon/server/(.+?).png" width="16" height="16" /> <a href="(.+?)">').findall(r)
                for host, url in match:
                    if host == 'internet':
                        pass
                    else:
                        sources.append({'source': host, 'quality': 'SD', 'language': 'en',
                                        'url': url, 'direct': False, 'debridonly': False})
            except Exception:
                failure = traceback.format_exc()
                log_utils.log('PutlockersGS - Exception: \n' + str(failure))
                return sources
        except Exception:
            failure = traceback.format_exc()
            log_utils.log('PutlockersGS - Exception: \n' + str(failure))
            return sources
        return sources

    def resolve(self, url):
        r = client.request(url)
        match = re.compile('decode\("(.+?)"').findall(r)
        for info in match:
            info = base64.b64decode(info)
            match = re.compile('src="(.+?)"').findall(info)
            for url in match:
                return url
