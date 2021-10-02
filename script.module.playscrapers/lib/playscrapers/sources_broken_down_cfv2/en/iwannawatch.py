# -*- coding: UTF-8 -*-
# -Cleaned and Checked on 08-24-2019 by PressPlay in PressPlay.

import re,requests,urlparse
from playscrapers.modules import cleantitle
from playscrapers.modules import source_utils


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['iwannawatch.is']
        self.base_link = 'https://www.iwannawatch.is'
        self.search_link = '/search/%s+%s/feed/rss2/'
        self.User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            search_id = cleantitle.getsearch(title)
            url = urlparse.urljoin(self.base_link, self.search_link)
            url = url  % (search_id.replace(' ', '+').replace('-', '+').replace('++', '+'), year)
            headers = {'User-Agent': self.User_Agent}
            search_results = requests.get(url, headers=headers, timeout=10).content
            items = re.compile('<item>(.+?)</item>', re.DOTALL).findall(search_results)
            for item in items:
                match = re.compile('<title>(.+?)</title>.+?<link>(.+?)</link>', re.DOTALL).findall(item)
                for row_title, row_url in match:
                    if cleantitle.get(title) in cleantitle.get(row_title):
                        if year in str(row_title):
                            return row_url
            return
        except:
            return


    def sources(self, url, hostDict, hostprDict):
        try:
            hostDict = hostprDict + hostDict
            sources = []
            if url == None:
                return sources
            headers = {'User-Agent': self.User_Agent}
            html = requests.get(url, headers=headers, timeout=10).content
            qual = re.compile('<div class="cf">.+?class="quality">(.+?)</td>', re.DOTALL).findall(html)
            for i in qual:
                quality = source_utils.check_url(i)
            links = re.compile('data-href="(.+?)"', re.DOTALL).findall(html)
            for link in links:
                if 'http' not in link:
                    link = 'https://' + link
                valid, host = source_utils.is_host_valid(link, hostDict)
                if valid:
                    sources.append({'source': host, 'quality': quality, 'language': 'en', 'url': link, 'direct': False, 'debridonly': False})
            return sources
        except:
            return sources


    def resolve(self, url):
        return url


