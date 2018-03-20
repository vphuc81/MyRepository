# -*- coding: UTF-8 -*-

'''
    Fantastic Add-on


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import re, urlparse, urllib, base64

from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import cache
from resources.lib.modules import dom_parser2


class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['xmovies8.es']
        self.base_link = 'https://xmovies8.es'
        self.search_link = '/search-movies/%s.html'


    def movie(self, imdb, title, localtitle, aliases, year):
        try:
            clean_title = cleantitle.geturl(title)
            search_url = urlparse.urljoin(self.base_link, self.search_link % clean_title.replace('-', '+'))
            r = cache.get(client.request, 1, search_url)
            r = client.parseDOM(r, 'div', {'id': 'movie-featured'})
            r = [(client.parseDOM(i, 'a', ret='href'),
                  re.findall('.+?elease:\s*(\d{4})</', i),
                  re.findall('<b><i>(.+?)</i>', i)) for i in r]
            r = [(i[0][0], i[1][0], i[2][0]) for i in r if
                 (cleantitle.get(i[2][0]) == cleantitle.get(title) and i[1][0] == year)]
            url = r[0][0]

            return url
        except Exception:
            return

    def tvshow(self, imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year):
        try:
            url = {'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year}
            url = urllib.urlencode(url)
            return url
        except:
            return

    def episode(self, url, imdb, tvdb, title, premiered, season, episode):
        try:
            if url == None: return

            url = urlparse.parse_qs(url)
            url = dict([(i, url[i][0]) if url[i] else (i, '') for i in url])
            url['premiered'], url['season'], url['episode'] = premiered, season, episode
            try:
                clean_title = cleantitle.geturl(url['tvshowtitle'])+'-season-%d' % int(season)
                search_url = urlparse.urljoin(self.base_link, self.search_link % clean_title.replace('-', '+'))
                r = cache.get(client.request, 1, search_url)
                r = client.parseDOM(r, 'div', {'id': 'movie-featured'})
                r = [(client.parseDOM(i, 'a', ret='href'),
                      re.findall('<b><i>(.+?)</i>', i)) for i in r]
                r = [(i[0][0], i[1][0]) for i in r if
                     cleantitle.get(i[1][0]) == cleantitle.get(clean_title)]
                url = r[0][0]
            except:
                pass
            data = client.request(url)
            data = client.parseDOM(data, 'div', attrs={'id': 'details'})
            data = zip(client.parseDOM(data, 'a'), client.parseDOM(data, 'a', ret='href'))
            url = [(i[0], i[1]) for i in data if i[0] == str(int(episode))]

            return url[0][1]
        except:
            return

    def sources(self, url, hostDict, hostprDict):
        try:
            sources = []
            r = cache.get(client.request, 1, url)
            try:
                v = re.findall('document.write\(Base64.decode\("(.+?)"\)', r)[0]
                b64 = base64.b64decode(v)
                url = client.parseDOM(b64, 'iframe', ret='src')[0]
                try:
                    host = re.findall('([\w]+[.][\w]+)$', urlparse.urlparse(url.strip().lower()).netloc)[0]
                    host = client.replaceHTMLCodes(host)
                    host = host.encode('utf-8')
                    sources.append({
                        'source': host,
                        'quality': 'SD',
                        'language': 'en',
                        'url': url.replace('\/', '/'),
                        'direct': False,
                        'debridonly': False
                    })
                except:
                    pass
            except:
                pass
            r = client.parseDOM(r, 'div', {'class': 'server_line'})
            r = [(client.parseDOM(i, 'a', ret='href')[0], client.parseDOM(i, 'p', attrs={'class': 'server_servername'})[0]) for i in r]
            if r:
                for i in r:
                    try:
                        host = re.sub('Server|Link\s*\d+', '', i[1]).lower()
                        url = i[0]
                        host = client.replaceHTMLCodes(host)
                        host = host.encode('utf-8')
                        if 'other'in host: continue
                        sources.append({
                            'source': host,
                            'quality': 'SD',
                            'language': 'en',
                            'url': url.replace('\/', '/'),
                            'direct': False,
                            'debridonly': False
                        })
                    except:
                        pass
            return sources
        except Exception:
            return

    def resolve(self, url):
        return url

    def __get_episode_url(self, data, hostDict):
        scraper = cfscrape.create_scraper()
        try:
            value = "/seasons/" + cleantitle.geturl(data['tvshowtitle']) + '-season-' + data['season']
            url = self.base_link + value
            print("INFO - " + url)
            html = scraper.get(self.base_link)
            html = scraper.get(url)
            page_list = BeautifulSoup(html.text, 'html.parser')
            page_list = page_list.find_all('div', {'class':'episodiotitle'})
            ep_page = ''
            for i in page_list:
                if re.sub(r'\W+', '', data['title'].lower()) in re.sub(r'\W+', '', i.text.lower()):
                    ep_page = i.prettify()
            if ep_page == '': return ''
            ep_page = BeautifulSoup(ep_page, 'html.parser').find_all('a')[0]['href']
            html = scraper.get(ep_page)
            embed = re.findall('<iframe.+?src=\"(.+?)\"', html.text)[0]
            url = embed
            sources = []
            if 'mehliz' in url:
                html = scraper.get(url, headers={'referer': self.base_link + '/'})
                files = re.findall('file: \"(.+?)\".+?label: \"(.+?)\"', html.text)

                for i in files:
                    try:
                        sources.append({
                            'source': 'gvideo',
                            'quality': i[1],
                            'language': 'en',
                            'url': i[0] + "|Referer=https:// xmovies8.es",
                            'direct': True,
                            'debridonly': False
                        })

                    except Exception:
                        pass

            else:
                valid, hoster = source_utils.is_host_valid(url, hostDict)
                if not valid: return ''
                urls, host, direct = source_utils.check_directstreams(url, hoster)

                sources.append({
                    'source': host,
                    'quality': urls[0]['quality'],
                    'language': 'en',
                    'url': url + "|Referer=https:// xmovies8.es",
                    'direct': False,
                    'debridonly': False
                })


            return sources

        except Exception:
            print("Unexpected error in Mehlix _get_episode_url Script:")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            return ""

    def __get_movie_url(self, data, hostDict):
        scraper = cfscrape.create_scraper()
        try:
            html = scraper.get(self.base_link +"/movies/"+cleantitle.geturl(data['title']))
            embeds = re.findall('play-box-iframe.+\s<iframe.+?src=\"(.+?)\"', html.text)[0]
            print("INFO - " + embeds)
            url = embeds
            sources = []
            if 'mehliz' in url:
                html = scraper.get(url, headers={'referer': self.base_link + '/'})
                files = re.findall('file: \"(.+?)\".+?label: \"(.+?)\"', html.text)

                for i in files:
                    try:
                        sources.append({
                            'source': 'gvideo',
                            'quality': i[1],
                            'language': 'en',
                            'url': i[0] + "|Referer=https:// xmovies8.es",
                            'direct': True,
                            'debridonly': False
                        })

                    except Exception:
                        pass

            else:
                valid, hoster = source_utils.is_host_valid(url, hostDict)
                if not valid: return ''
                urls, host, direct = source_utils.check_directstreams(url, hoster)

                sources.append({
                    'source': host,
                    'quality': urls[0]['quality'],
                    'language': 'en',
                    'url': url + "|Referer=https:// xmovies8.es",
                    'direct': False,
                    'debridonly': False
                })

            return sources

        except Exception:
            print("Unexpected error in Mehliz getMovieURL Script:")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            return ""
