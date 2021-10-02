# -*- coding: UTF-8 -*-
#######################################################################
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# @PressPlay wrote this file.  As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return. - Muad'Dib
# ----------------------------------------------------------------------------
#######################################################################



import re

from playscrapers import parse_qs, urlencode, quote_plus
from playscrapers.modules import cache, cleantitle, client, debrid, source_utils, log_utils

from playscrapers import custom_base_link
custom_base = custom_base_link(__name__)


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['eztv.re', 'eztv.tf', 'eztv.yt', 'eztv.unblockit.uno']
        self.base_link = custom_base
        self.search_link = '/search/%s'

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        if debrid.status() is False:
            return

        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urlencode(url)
            return url
        except Exception:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        if debrid.status() is False:
            return

        try:
            if url is None:
                return

            url = parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['title'], url['premiered'], url['season'], url['episode'] = title, premiered, season, episode
            url = urlencode(url)
            return url
        except Exception:
            return

    def sources(self, url, hostDict, hostprDict):
        sources = []
        try:

            if url is None:
                return sources

            data = parse_qs(url)
            data = dict([(i, data[i][0]) if data[i] else (i, '') for i in data])

            title = data['tvshowtitle']
            title = cleantitle.get_query(title)

            hdlr = 'S%02dE%02d' % (int(data['season']), int(data['episode']))

            query = '%s S%02dE%02d' % (
                title,
                int(data['season']),
                int(data['episode'])) if 'tvshowtitle' in data else '%s %s' % (
                title,
                data['year'])
            query = re.sub('(\\\|/| -|:|;|\*|\?|"|<|>|\|)', ' ', query)

            query = self.search_link % (quote_plus(query).replace('+', '-'))
            r, self.base_link = client.list_request(self.base_link or self.domains, query)
            #log_utils.log('eztv base: ' + self.base_link)

            try:
                results = client.parseDOM(r, 'table', attrs={'class': 'forum_header_border'})
                for result in results:
                    if 'magnet:' in result:
                        results = result
                        break
            except Exception:
                return sources
            rows = re.findall('<tr name="hover" class="forum_header_border">(.+?)</tr>', results, re.DOTALL)
            if rows is None:
                return sources

            for entry in rows:
                try:
                    try:
                        columns = re.findall('<td\s.+?>(.*?)</td>', entry, re.DOTALL)
                        derka = re.findall('href="magnet:(.+?)" class="magnet" title="(.+?)"', columns[2], re.DOTALL)[0]
                        name = derka[1]
                        link = 'magnet:%s' % (str(client.replaceHTMLCodes(derka[0]).split('&tr')[0]))
                        t = name.split(hdlr)[0]
                        if not cleantitle.get(re.sub('(|)', '', t)) == cleantitle.get(title):
                            continue
                    except Exception:
                        continue
                    y = re.findall('[\.|\(|\[|\s](\d{4}|S\d*E\d*|S\d*)[\.|\)|\]|\s]', name)[-1].upper()
                    if not y == hdlr:
                        continue

                    quality, info = source_utils.get_release_quality(name, name)

                    try:
                        size = re.findall('((?:\d+\.\d+|\d+\,\d+|\d+)\s*(?:GB|GiB|MB|MiB))', name)[-1]
                        dsize, isize = source_utils._size(size)
                    except Exception:
                        dsize, isize = 0.0, ''

                    info.insert(0, isize)

                    info = ' | '.join(info)
                    sources.append({'source': 'Torrent', 'quality': quality, 'language': 'en',
                                    'url': link, 'info': info, 'direct': False, 'debridonly': True, 'size': dsize, 'name': name})
                except Exception:
                    continue

            check = [i for i in sources if not i['quality'] == 'CAM']
            if check:
                sources = check

            return sources
        except:
            log_utils.log('eztv_exc', 1)
            return sources

    def resolve(self, url):
        return url
