# -*- coding: utf-8 -*-

"""
    Exodus Add-on
    ///Updated for Exodus///

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
"""


from resources.lib.modules import trakt
from resources.lib.modules import cleantitle
from resources.lib.modules import cleangenre
from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import cache
from resources.lib.modules import playcount
from resources.lib.modules import workers
from resources.lib.modules import views
from resources.lib.modules import utils
from resources.lib.modules import log_utils

import six
from six.moves import urllib_parse, urllib_request

import os,sys,re,zipfile,datetime#,base64
import simplejson as json

try: from cStringIO import StringIO
except: from io import BytesIO as StringIO

import requests

params = dict(urllib_parse.parse_qsl(sys.argv[2].replace('?',''))) if len(sys.argv) > 1 else dict()

action = params.get('action')

class seasons:
    def __init__(self):
        self.list = []

        self.lang = control.apiLanguage()['tvdb']
        self.showunaired = control.setting('showunaired') or 'true'
        self.specials = control.setting('tv.specials') or 'true'
        self.ratings = control.setting('ep.ratings') or 'false'
        self.datetime = datetime.datetime.utcnow()# - datetime.timedelta(hours = 5)
        self.today_date = self.datetime.strftime('%Y-%m-%d')
        #self.etvdb_key = 'Sk1DTzhMUUhJWFg3NkNHTg=='
        self.tvdb_key = 'JMCO8LQHIXX76CGN'#base64.b64decode(self.etvdb_key)#

        self.tvdb_info_link = 'https://thetvdb.com/api/%s/series/%s/all/%s.zip' % (self.tvdb_key, '%s', '%s')
        self.tvdb_by_imdb = 'https://thetvdb.com/api/GetSeriesByRemoteID.php?imdbid=%s'
        self.tvdb_by_query = 'https://thetvdb.com/api/GetSeries.php?seriesname=%s'
        self.tvdb_image = 'https://thetvdb.com/banners/'
        self.tvdb_poster = 'https://thetvdb.com/banners/_cache/'


    def get(self, tvshowtitle, year, imdb, tvdb, idx=True, create_directory=True):
        if control.window.getProperty('PseudoTVRunning') == 'True':
            return episodes().get(tvshowtitle, year, imdb, tvdb)

        if idx == True:
            self.list = cache.get(self.tvdb_list, 24, tvshowtitle, year, imdb, tvdb, self.lang)
            if create_directory == True: self.seasonDirectory(self.list)
            return self.list
        else:
            self.list = self.tvdb_list(tvshowtitle, year, imdb, tvdb, 'en')
            return self.list


    def tvdb_list(self, tvshowtitle, year, imdb, tvdb, lang, limit=''):
        try:
            if imdb == '0':
                try:
                    imdb = trakt.SearchTVShow(tvshowtitle, year, full=False)[0]
                    imdb = imdb.get('show', '0')
                    imdb = imdb.get('ids', {}).get('imdb', '0')
                    imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))

                    if not imdb: imdb = '0'
                except:
                    imdb = '0'

            if tvdb == '0' and not imdb == '0':
                url = self.tvdb_by_imdb % imdb

                #result = client.request(url, timeout='10')
                result = requests.get(url, timeout=10, verify=True).content
                result = control.six_decode(result)

                try: tvdb = client.parseDOM(result, 'seriesid')[0]
                except: tvdb = '0'

                try: name = client.parseDOM(result, 'SeriesName')[0]
                except: name = '0'
                dupe = re.compile('[***]Duplicate (\d*)[***]').findall(name)
                if len(dupe) > 0: tvdb = str(dupe[0])

                if tvdb == '': tvdb = '0'


            if tvdb == '0':
                url = self.tvdb_by_query % (urllib_parse.quote_plus(tvshowtitle))

                years = [str(year), str(int(year)+1), str(int(year)-1)]

                #tvdb = client.request(url, timeout='10')
                tvdb = requests.get(url, timeout=10, verify=True).content
                tvdb = re.sub(r'[^\x00-\x7F]+', '', tvdb)
                tvdb = client.replaceHTMLCodes(tvdb)
                tvdb = client.parseDOM(tvdb, 'Series')
                tvdb = [(x, client.parseDOM(x, 'SeriesName'), client.parseDOM(x, 'FirstAired')) for x in tvdb]
                tvdb = [(x, x[1][0], x[2][0]) for x in tvdb if len(x[1]) > 0 and len(x[2]) > 0]
                tvdb = [x for x in tvdb if cleantitle.get(tvshowtitle) == cleantitle.get(x[1])]
                tvdb = [x[0][0] for x in tvdb if any(y in x[2] for y in years)][0]
                tvdb = client.parseDOM(tvdb, 'seriesid')[0]

                if tvdb == '': tvdb = '0'
        except:
            import traceback
            failure = traceback.format_exc()
            log_utils.log('tvdb-list0 Exception: ' + str(failure))
            return


        try:
            if tvdb == '0': return

            url = self.tvdb_info_link % (tvdb, 'en')
            #data = urllib_request.urlopen(url, timeout=30).read()
            data = requests.get(url, timeout=30, verify=True).content
            zip = zipfile.ZipFile(StringIO(data))
            result = zip.read('en.xml')
            artwork = zip.read('banners.xml')
            zip.close()

            result = control.six_decode(result)
            artwork = control.six_decode(artwork)
            dupe = client.parseDOM(result, 'SeriesName')[0]
            dupe = re.compile('[***]Duplicate (\d*)[***]').findall(dupe)

            if len(dupe) > 0:
                tvdb = six.ensure_str(str(dupe[0]))

                url = self.tvdb_info_link % (tvdb, 'en')
                #data = urllib_request.urlopen(url, timeout=30).read()
                data = requests.get(url, timeout=30, verify=True).content
                zip = zipfile.ZipFile(StringIO(data))
                result = zip.read('en.xml')
                artwork = zip.read('banners.xml')
                zip.close()

            if not lang == 'en':
                url = self.tvdb_info_link % (tvdb, lang)
                #data = urllib_request.urlopen(url, timeout=30).read()
                data = requests.get(url, timeout=30, verify=True).content
                zip = zipfile.ZipFile(StringIO(data))
                result2 = zip.read('%s.xml' % lang)
                zip.close()
            else:
                result2 = result


            artwork = artwork.split('<Banner>')
            artwork = [i for i in artwork if '<Language>en</Language>' in i and '<BannerType>season</BannerType>' in i]
            artwork = [i for i in artwork if not 'seasonswide' in re.findall('<BannerPath>(.+?)</BannerPath>', i)[0]]


            result = result.split('<Episode>')
            result2 = control.six_decode(result2)
            result2 = result2.split('<Episode>')

            item = result[0] ; item2 = result2[0]

            episodes = [i for i in result if '<EpisodeNumber>' in i]

            if self.specials == 'true':
                episodes = [i for i in episodes]
            else:
                episodes = [i for i in episodes if not '<SeasonNumber>0</SeasonNumber>' in i]
                episodes = [i for i in episodes if not '<EpisodeNumber>0</EpisodeNumber>' in i]

            seasons = [i for i in episodes if '<EpisodeNumber>1</EpisodeNumber>' in i]

            locals = [i for i in result2 if '<EpisodeNumber>' in i]

            result = '' ; result2 = ''

            if limit == '':
                episodes = []
            elif limit == '-1':
                seasons = []
            else:
                episodes = [i for i in episodes if '<SeasonNumber>%01d</SeasonNumber>' % int(limit) in i]
                seasons = []


            try: poster = client.parseDOM(item, 'poster')[0]
            except: poster = ''
            if not poster == '': poster = self.tvdb_image + poster
            else: poster = '0'
            poster = client.replaceHTMLCodes(poster)
            poster = six.ensure_str(poster)

            try: banner = client.parseDOM(item, 'banner')[0]
            except: banner = ''
            if not banner == '': banner = self.tvdb_image + banner
            else: banner = '0'
            banner = client.replaceHTMLCodes(banner)
            banner = six.ensure_str(banner)

            try: fanart = client.parseDOM(item, 'fanart')[0]
            except: fanart = ''
            if not fanart == '': fanart = self.tvdb_image + fanart
            else: fanart = '0'
            fanart = client.replaceHTMLCodes(fanart)
            fanart = six.ensure_str(fanart)

            if not poster == '0': pass
            elif not fanart == '0': poster = fanart
            elif not banner == '0': poster = banner

            if not banner == '0': pass
            elif not fanart == '0': banner = fanart
            elif not poster == '0': banner = poster

            try: status = client.parseDOM(item, 'Status')[0]
            except: status = ''
            if status == '': status = 'Ended'
            status = client.replaceHTMLCodes(status)
            status = six.ensure_str(status)

            try: studio = client.parseDOM(item, 'Network')[0]
            except: studio = ''
            if studio == '': studio = '0'
            studio = client.replaceHTMLCodes(studio)
            studio = six.ensure_str(studio)

            try: genre = client.parseDOM(item, 'Genre')[0]
            except: genre = ''
            genre = [x for x in genre.split('|') if not x == '']
            genre = ' / '.join(genre)
            if genre == '': genre = '0'
            genre = client.replaceHTMLCodes(genre)
            genre = six.ensure_str(genre)

            try: duration = client.parseDOM(item, 'Runtime')[0]
            except: duration = ''
            if duration == '': duration = '0'
            duration = client.replaceHTMLCodes(duration)
            duration = six.ensure_str(duration)

            # try: rating = client.parseDOM(item, 'Rating')[0]
            # except: rating = ''
            # if rating == '': rating = '0'
            # rating = client.replaceHTMLCodes(rating)
            # rating = six.ensure_str(rating)

            # try: votes = client.parseDOM(item, 'RatingCount')[0]
            # except: votes = '0'
            # if votes == '': votes = '0'
            # votes = client.replaceHTMLCodes(votes)
            # votes = six.ensure_str(votes)

            try: mpaa = client.parseDOM(item, 'ContentRating')[0]
            except: mpaa = ''
            if mpaa == '': mpaa = '0'
            mpaa = client.replaceHTMLCodes(mpaa)
            mpaa = six.ensure_str(mpaa)

            try: cast = client.parseDOM(item, 'Actors')[0]
            except: cast = ''
            cast = [x for x in cast.split('|') if not x == '']
            try: cast = [(six.ensure_str(x), '') for x in cast]
            except: cast = []

            try: label = client.parseDOM(item2, 'SeriesName')[0]
            except: label = '0'
            label = client.replaceHTMLCodes(label)
            label = six.ensure_str(label)

            try: plot = client.parseDOM(item2, 'Overview')[0]
            except: plot = ''
            if plot == '': plot = '0'
            plot = client.replaceHTMLCodes(plot)
            plot = six.ensure_str(plot)

            unaired = ''
        except:
            import traceback
            failure = traceback.format_exc()
            log_utils.log('tvdb-list1 Exception: ' + str(failure))
            pass


        for item in seasons:
            try:
                premiered = client.parseDOM(item, 'FirstAired')[0]
                if premiered == '' or '-00' in premiered: premiered = '0'
                premiered = client.replaceHTMLCodes(premiered)
                premiered = six.ensure_str(premiered)

                if status == 'Ended': pass
                elif premiered == '0': raise Exception()
                elif int(re.sub('[^0-9]', '', str(premiered))) > int(re.sub('[^0-9]', '', str(self.today_date))):
                    unaired = 'true'
                    if self.showunaired != 'true': raise Exception()

                season = client.parseDOM(item, 'SeasonNumber')[0]
                season = '%01d' % int(season)
                season = six.ensure_str(season)

                thumb = [i for i in artwork if client.parseDOM(i, 'Season')[0] == season]
                try: thumb = client.parseDOM(thumb[0], 'BannerPath')[0]
                except: thumb = ''
                if not thumb == '': thumb = self.tvdb_image + thumb
                else: thumb = '0'
                thumb = client.replaceHTMLCodes(thumb)
                thumb = six.ensure_str(thumb)

                if thumb == '0': thumb = poster

                self.list.append({'season': season, 'tvshowtitle': tvshowtitle, 'label': label, 'year': year, 'premiered': premiered, 'status': status, 'studio': studio, 'genre': genre, 'duration': duration,
                                  'mpaa': mpaa, 'cast': cast, 'plot': plot, 'imdb': imdb, 'tvdb': tvdb, 'poster': poster, 'banner': banner, 'fanart': fanart, 'thumb': thumb, 'unaired': unaired})
                self.list = sorted(self.list, key=lambda k: int(k['season']))
            except:
                import traceback
                failure = traceback.format_exc()
                log_utils.log('tvdb-list2 Exception: ' + str(failure))
                pass


        for item in episodes:
            try:
                premiered = client.parseDOM(item, 'FirstAired')[0]
                if premiered == '' or '-00' in premiered: premiered = '0'
                premiered = client.replaceHTMLCodes(premiered)
                premiered = six.ensure_str(premiered)

                if status == 'Ended': pass
                elif premiered == '0': raise Exception()
                elif int(re.sub('[^0-9]', '', str(premiered))) > int(re.sub('[^0-9]', '', str(self.today_date))):
                    unaired = 'true'
                    if self.showunaired != 'true': raise Exception()

                season = client.parseDOM(item, 'SeasonNumber')[0]
                season = '%01d' % int(season)
                season = six.ensure_str(season)

                episode = client.parseDOM(item, 'EpisodeNumber')[0]
                episode = re.sub('[^0-9]', '', '%01d' % int(episode))
                episode = six.ensure_str(episode)

                title = client.parseDOM(item, 'EpisodeName')[0]
                if title == '': title = '0'
                title = client.replaceHTMLCodes(title)
                title = six.ensure_str(title)


                try: thumb = client.parseDOM(item, 'filename')[0]
                except: thumb = ''
                if not thumb == '': thumb = self.tvdb_image + thumb
                else: thumb = '0'
                thumb = client.replaceHTMLCodes(thumb)
                thumb = six.ensure_str(thumb)

                if not thumb == '0': pass
                elif not fanart == '0': thumb = fanart.replace(self.tvdb_image, self.tvdb_poster)
                elif not poster == '0': thumb = poster

                if self.ratings == 'true':
                    try:
                        rating, votes = trakt.getEpisodeRating(imdb, int(season), int(episode))
                    except:
                        rating, votes = '0', '0'
                    if rating == None or rating == '0.0':
                        rating = '0'
                    if votes == None:
                        votes = '0'
                else:
                    try: rating = client.parseDOM(item, 'Rating')[0]
                    except: rating = ''
                    if rating == '': rating = '0'
                    rating = client.replaceHTMLCodes(rating)
                    rating = six.ensure_str(rating)

                    try: votes = client.parseDOM(item, 'RatingCount')[0]
                    except: votes = '0'
                    if votes == '': votes = '0'
                    votes = client.replaceHTMLCodes(votes)
                    votes = six.ensure_str(votes)

                try: director = client.parseDOM(item, 'Director')[0]
                except: director = ''
                director = [x for x in director.split('|') if not x == '']
                director = ' / '.join(director)
                if director == '': director = '0'
                director = client.replaceHTMLCodes(director)
                director = six.ensure_str(director)

                try: writer = client.parseDOM(item, 'Writer')[0]
                except: writer = ''
                writer = [x for x in writer.split('|') if not x == '']
                writer = ' / '.join(writer)
                if writer == '': writer = '0'
                writer = client.replaceHTMLCodes(writer)
                writer = six.ensure_str(writer)

                try:
                    local = client.parseDOM(item, 'id')[0]
                    local = [x for x in locals if '<id>%s</id>' % str(local) in x][0]
                except:
                    local = item

                label = client.parseDOM(local, 'EpisodeName')[0]
                if label == '': label = '0'
                label = client.replaceHTMLCodes(label)
                label = six.ensure_str(label)

                try:
                    episodeplot = client.parseDOM(local, 'Overview')[0]
                    if episodeplot == '': episodeplot = client.parseDOM(item, 'Overview')[0]
                    if episodeplot == '': episodeplot = '0'
                except:
                    episodeplot = '0'
                if episodeplot == '0': episodeplot = plot
                episodeplot = client.replaceHTMLCodes(episodeplot)
                try: episodeplot = six.ensure_str(episodeplot)
                except: pass

                self.list.append({'title': title, 'label': label, 'season': season, 'episode': episode, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'status': status,
                                  'studio': studio, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast,
                                  'plot': episodeplot, 'imdb': imdb, 'tvdb': tvdb, 'poster': poster, 'banner': banner, 'fanart': fanart, 'thumb': thumb, 'unaired': unaired})
                self.list = sorted(self.list, key=lambda k: (int(k['season']), int(k['episode'])))
            except:
                import traceback
                failure = traceback.format_exc()
                log_utils.log('tvdb_list3 Exception: ' + str(failure))
                pass

        return self.list


    def seasonDirectory(self, items):
        if items == None or len(items) == 0: control.idle() ; sys.exit()

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        addonPoster, addonBanner = control.addonPoster(), control.addonBanner()

        addonFanart, settingFanart = control.addonFanart(), control.setting('fanart')

        traktCredentials = trakt.getTraktCredentialsInfo()

        try: isOld = False ; control.item().getArt('type')
        except: isOld = True

        try: indicators = playcount.getSeasonIndicators(items[0]['imdb'])
        except: pass

        watchedMenu = six.ensure_str(control.lang(32068)) if trakt.getTraktIndicatorsInfo() == True else six.ensure_str(control.lang(32066))

        unwatchedMenu = six.ensure_str(control.lang(32069)) if trakt.getTraktIndicatorsInfo() == True else six.ensure_str(control.lang(32067))

        queueMenu = six.ensure_str(control.lang(32065))

        traktManagerMenu = six.ensure_str(control.lang(32070))

        labelMenu = six.ensure_str(control.lang(32055))

        playRandom = six.ensure_str(control.lang(32535))

        addToLibrary = six.ensure_str(control.lang(32551))

        infoMenu = six.ensure_str(control.lang(32101))


        for i in items:
            try:
                label = '%s %s' % (labelMenu, i['season'])
                try:
                    if i['unaired'] == 'true':
                        label = '[COLOR crimson][I]%s[/I][/COLOR]' % label
                except:
                    pass
                systitle = sysname = urllib_parse.quote_plus(i['tvshowtitle'])

                imdb, tvdb, year, season = i['imdb'], i['tvdb'], i['year'], i['season']

                meta = dict((k,v) for k, v in six.iteritems(i) if not v == '0')
                meta.update({'code': imdb, 'imdbnumber': imdb, 'imdb_id': imdb})
                meta.update({'tvdb_id': tvdb})
                meta.update({'mediatype': 'tvshow'})
                meta.update({'trailer': '%s?action=trailer&name=%s' % (sysaddon, sysname)})
                if not 'duration' in i: meta.update({'duration': '60'})
                elif i['duration'] == '0': meta.update({'duration': '60'})
                try: meta.update({'duration': str(int(meta['duration']) * 60)})
                except: pass
                try: meta.update({'genre': cleangenre.lang(meta['genre'], self.lang)})
                except: pass
                try: meta.update({'tvshowtitle': i['label']})
                except: pass
                try:
                    seasonYear = i['premiered']
                    seasonYear = re.findall('(\d{4})', seasonYear)[0]
                    seasonYear = six.ensure_str(seasonYear)
                    meta.update({'year': seasonYear})
                except:
                    pass

                try:
                    if season in indicators: meta.update({'playcount': 1, 'overlay': 7})
                    else: meta.update({'playcount': 0, 'overlay': 6})
                except:
                    pass


                url = '%s?action=episodes&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s&season=%s' % (sysaddon, systitle, year, imdb, tvdb, season)


                cm = []

                cm.append((playRandom, 'RunPlugin(%s?action=random&rtype=episode&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s&season=%s)' % (sysaddon, urllib_parse.quote_plus(systitle), urllib_parse.quote_plus(year), urllib_parse.quote_plus(imdb), urllib_parse.quote_plus(tvdb), urllib_parse.quote_plus(season))))

                cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

                cm.append((watchedMenu, 'RunPlugin(%s?action=tvPlaycount&name=%s&imdb=%s&tvdb=%s&season=%s&query=7)' % (sysaddon, systitle, imdb, tvdb, season)))

                cm.append((unwatchedMenu, 'RunPlugin(%s?action=tvPlaycount&name=%s&imdb=%s&tvdb=%s&season=%s&query=6)' % (sysaddon, systitle, imdb, tvdb, season)))

                if traktCredentials == True:
                    cm.append((traktManagerMenu, 'RunPlugin(%s?action=traktManager&name=%s&tvdb=%s&content=tvshow)' % (sysaddon, sysname, tvdb)))

                if isOld == True:
                    cm.append((infoMenu, 'Action(Info)'))

                cm.append((addToLibrary, 'RunPlugin(%s?action=tvshowToLibrary&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s)' % (sysaddon, systitle, year, imdb, tvdb)))

                item = control.item(label=label)

                art = {}

                if 'thumb' in i and not i['thumb'] == '0':
                    art.update({'icon': i['thumb'], 'thumb': i['thumb'], 'poster': i['thumb']})
                elif 'poster' in i and not i['poster'] == '0':
                    art.update({'icon': i['poster'], 'thumb': i['poster'], 'poster': i['poster']})
                else:
                    art.update({'icon': addonPoster, 'thumb': addonPoster, 'poster': addonPoster})

                if 'banner' in i and not i['banner'] == '0':
                    art.update({'banner': i['banner']})
                elif 'fanart' in i and not i['fanart'] == '0':
                    art.update({'banner': i['fanart']})
                else:
                    art.update({'banner': addonBanner})

                if settingFanart == 'true' and 'fanart' in i and not i['fanart'] == '0':
                    item.setProperty('Fanart_Image', i['fanart'])
                elif not addonFanart == None:
                    item.setProperty('Fanart_Image', addonFanart)

                item.setArt(art)
                item.addContextMenuItems(cm)
                item.setInfo(type='Video', infoLabels = control.metadataClean(meta))

                video_streaminfo = {'codec': 'h264'}
                item.addStreamInfo('video', video_streaminfo)

                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=True)
            except:
                import traceback
                failure = traceback.format_exc()
                log_utils.log('season-dir Exception: ' + str(failure))
                pass

        try: control.property(syshandle, 'showplot', items[0]['plot'])
        except: pass

        control.content(syshandle, 'seasons')
        control.directory(syshandle, cacheToDisc=True)
        views.setView('seasons', {'skin.estuary': 55, 'skin.confluence': 500})


class episodes:
    def __init__(self):
        self.list = []

        self.trakt_link = 'https://api.trakt.tv'
        self.tvmaze_link = 'https://api.tvmaze.com'
        #self.etvdb_key = 'Sk1DTzhMUUhJWFg3NkNHTg=='
        self.tvdb_key = 'JMCO8LQHIXX76CGN'#base64.b64decode(self.etvdb_key)#
        self.datetime = datetime.datetime.utcnow()# - datetime.timedelta(hours = 5)
        self.systime = self.datetime.strftime('%Y%m%d%H%M%S%f')
        self.today_date = self.datetime.strftime('%Y-%m-%d')
        self.trakt_user = control.setting('trakt.user').strip()
        self.lang = control.apiLanguage()['tvdb']
        self.showunaired = control.setting('showunaired') or 'true'
        self.specials = control.setting('tv.specials') or 'true'
        self.ratings = control.setting('ep.ratings') or 'false'

        self.tvdb_info_link = 'https://thetvdb.com/api/%s/series/%s/all/%s.zip' % (self.tvdb_key, '%s', '%s')
        self.tvdb_image = 'https://thetvdb.com/banners/'
        self.tvdb_poster = 'https://thetvdb.com/banners/_cache/'

        self.added_link = 'https://api.tvmaze.com/schedule'
        #https://api.trakt.tv/calendars/all/shows/date[30]/31 #use this for new episodes?
        #self.mycalendar_link = 'https://api.trakt.tv/calendars/my/shows/date[29]/60/'
        self.mycalendar_link = 'https://api.trakt.tv/calendars/my/shows/date[30]/31/' #go back 30 and show all shows aired until tomorrow
        self.trakthistory_link = 'https://api.trakt.tv/users/me/history/shows?limit=40'
        self.progress_link = 'https://api.trakt.tv/users/me/watched/shows'
        self.hiddenprogress_link = 'https://api.trakt.tv/users/hidden/progress_watched?limit=1000&type=show'
        self.calendar_link = 'https://api.tvmaze.com/schedule?date=%s'
        self.onDeck_link = 'https://api.trakt.tv/sync/playback/episodes?limit=20'
        self.traktlists_link = 'https://api.trakt.tv/users/me/lists'
        self.traktlikedlists_link = 'https://api.trakt.tv/users/likes/lists?limit=1000000'
        self.traktlist_link = 'https://api.trakt.tv/users/%s/lists/%s/items'


    def get(self, tvshowtitle, year, imdb, tvdb, season=None, episode=None, idx=True, create_directory=True):
        try:
            if idx == True:
                if season == None and episode == None:
                    self.list = cache.get(seasons().tvdb_list, 1, tvshowtitle, year, imdb, tvdb, self.lang, '-1')
                elif episode == None:
                    self.list = cache.get(seasons().tvdb_list, 1, tvshowtitle, year, imdb, tvdb, self.lang, season)
                else:
                    self.list = cache.get(seasons().tvdb_list, 1, tvshowtitle, year, imdb, tvdb, self.lang, '-1')
                    num = [x for x,y in enumerate(self.list) if y['season'] == str(season) and  y['episode'] == str(episode)][-1]
                    self.list = [y for x,y in enumerate(self.list) if x >= num]

                if create_directory == True: self.episodeDirectory(self.list)
                return self.list
            else:
                self.list = seasons().tvdb_list(tvshowtitle, year, imdb, tvdb, 'en', '-1')
                return self.list
        except:
            pass


    def calendar(self, url):
        try:

            try: url = getattr(self, url + '_link')
            except: pass

            if self.trakt_link in url and url == self.onDeck_link:
                self.blist = cache.get(self.trakt_episodes_list, 720, url, self.trakt_user, self.lang)
                self.list = []
                self.list = self.trakt_episodes_list(url, self.trakt_user, self.lang)
                self.list = self.list[::-1]

            elif self.trakt_link in url and url == self.progress_link:
                self.blist = cache.get(self.trakt_progress_list, 720, url, self.trakt_user, self.lang)
                self.list = []
                self.list = cache.get(self.trakt_progress_list, 0, url, self.trakt_user, self.lang)

            elif self.trakt_link in url and url == self.mycalendar_link:
                self.blist = cache.get(self.trakt_episodes_list, 720, url, self.trakt_user, self.lang)
                self.list = []
                self.list = cache.get(self.trakt_episodes_list, 0, url, self.trakt_user, self.lang)

            elif self.trakt_link in url and '/users/' in url:
                self.list = cache.get(self.trakt_list, 0.3, url, self.trakt_user)
                self.list = self.list[::-1]

            elif self.trakt_link in url:
                self.list = cache.get(self.trakt_list, 1, url, self.trakt_user)


            elif self.tvmaze_link in url and url == self.added_link:
                urls = [i['url'] for i in self.calendars(idx=False)][:5]
                self.list = []
                for url in urls:
                    self.list += cache.get(self.tvmaze_list, 720, url, True)

            elif self.tvmaze_link in url:
                self.list = cache.get(self.tvmaze_list, 1, url, False)


            self.episodeDirectory(self.list)
            return self.list
        except:
            pass


    def widget(self):
        if trakt.getTraktIndicatorsInfo() == True:
            setting = control.setting('tv.widget.alt')
        else:
            setting = control.setting('tv.widget')

        if setting == '2':
            self.calendar(self.progress_link)
        elif setting == '3':
            self.calendar(self.mycalendar_link)
        else:
            self.calendar(self.added_link)


    def calendars(self, idx=True):
        m = six.ensure_str(control.lang(32060)).split('|')
        try: months = [(m[0], 'January'), (m[1], 'February'), (m[2], 'March'), (m[3], 'April'), (m[4], 'May'), (m[5], 'June'), (m[6], 'July'), (m[7], 'August'), (m[8], 'September'), (m[9], 'October'), (m[10], 'November'), (m[11], 'December')]
        except: months = []

        d = six.ensure_str(control.lang(32061)).split('|')
        try: days = [(d[0], 'Monday'), (d[1], 'Tuesday'), (d[2], 'Wednesday'), (d[3], 'Thursday'), (d[4], 'Friday'), (d[5], 'Saturday'), (d[6], 'Sunday')]
        except: days = []

        for i in list(range(0, 30)):
            try:
                name = (self.datetime - datetime.timedelta(days = i))
                name = (six.ensure_str(control.lang(32062)) % (name.strftime('%A'), six.ensure_str(name.strftime('%d %B'))))
                for m in months: name = name.replace(m[1], m[0])
                for d in days: name = name.replace(d[1], d[0])
                try: name = six.ensure_str(name)
                except: pass

                url = self.calendar_link % (self.datetime - datetime.timedelta(days = i)).strftime('%Y-%m-%d')

                self.list.append({'name': name, 'url': url, 'image': 'calendar.png', 'action': 'calendar'})
            except:
                pass
        if idx == True: self.addDirectory(self.list)
        return self.list


    def userlists(self):
        try:
            userlists = []
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            activity = trakt.getActivity()
        except:
            pass

        try:
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            try:
                if activity > cache.timeout(self.trakt_user_list, self.traktlists_link, self.trakt_user): raise Exception()
                userlists += cache.get(self.trakt_user_list, 720, self.traktlists_link, self.trakt_user)
            except:
                userlists += cache.get(self.trakt_user_list, 0, self.traktlists_link, self.trakt_user)
        except:
            pass
        try:
            self.list = []
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            try:
                if activity > cache.timeout(self.trakt_user_list, self.traktlikedlists_link, self.trakt_user): raise Exception()
                userlists += cache.get(self.trakt_user_list, 720, self.traktlikedlists_link, self.trakt_user)
            except:
                userlists += cache.get(self.trakt_user_list, 0, self.traktlikedlists_link, self.trakt_user)
        except:
            pass

        self.list = userlists
        for i in list(range(0, len(self.list))): self.list[i].update({'image': 'userlists.png', 'action': 'calendar'})
        self.addDirectory(self.list, queue=True)
        return self.list


    def trakt_list(self, url, user):
        try:
            for i in re.findall('date\[(\d+)\]', url):
                url = url.replace('date[%s]' % i, (self.datetime - datetime.timedelta(days = int(i))).strftime('%Y-%m-%d'))

            q = dict(urllib_parse.parse_qsl(urllib_parse.urlsplit(url).query))
            q.update({'extended': 'full'})
            q = (urllib_parse.urlencode(q)).replace('%2C', ',')
            u = url.replace('?' + urllib_parse.urlparse(url).query, '') + '?' + q

            itemlist = []
            items = trakt.getTraktAsJson(u)
        except:
            print("Unexpected error in info builder script:", sys.exc_info()[0])
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_type, exc_tb.tb_lineno)
            return


        for item in items:
            try:
                title = item['episode']['title']
                if title == None or title == '': raise Exception()
                title = client.replaceHTMLCodes(title)

                season = item['episode']['season']
                season = re.sub('[^0-9]', '', '%01d' % int(season))
                if season == '0': raise Exception()

                episode = item['episode']['number']
                episode = re.sub('[^0-9]', '', '%01d' % int(episode))
                if episode == '0': raise Exception()

                tvshowtitle = item['show']['title']
                if tvshowtitle == None or tvshowtitle == '': raise Exception()
                tvshowtitle = client.replaceHTMLCodes(tvshowtitle)

                year = item['show']['year']
                year = re.sub('[^0-9]', '', str(year))

                imdb = item['show']['ids']['imdb']
                if imdb == None or imdb == '': imdb = '0'
                else: imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))

                tvdb = item['show']['ids']['tvdb']
                if tvdb == None or tvdb == '': raise Exception()
                tvdb = re.sub('[^0-9]', '', str(tvdb))

                premiered = item['episode']['first_aired']
                try: premiered = re.compile('(\d{4}-\d{2}-\d{2})').findall(premiered)[0]
                except: premiered = '0'

                studio = item['show']['network']
                if studio == None: studio = '0'

                genre = item['show']['genres']
                genre = [i.title() for i in genre]
                if genre == []: genre = '0'
                genre = ' / '.join(genre)

                try: duration = str(item['show']['runtime'])
                except: duration = '0'
                if duration == None: duration = '0'

                try: rating = str(item['episode']['rating'])
                except: rating = '0'
                if rating == None or rating == '0.0': rating = '0'

                try: votes = str(item['episode']['votes'])
                except: votes = '0'
                try: votes = str(format(int(votes),',d'))
                except: pass
                if votes == None: votes = '0'

                mpaa = item['show']['certification']
                if mpaa == None: mpaa = '0'

                plot = item['episode']['overview']
                if plot == None or plot == '': plot = item['show']['overview']
                if plot == None or plot == '': plot = '0'
                plot = client.replaceHTMLCodes(plot)

                try:
                    if self.lang == 'en': raise Exception()

                    item = trakt.getTVShowTranslation(imdb, lang=self.lang, season=season, episode=episode,  full=True)

                    title = item.get('title') or title
                    plot = item.get('overview') or plot

                    tvshowtitle = trakt.getTVShowTranslation(imdb, lang=self.lang) or tvshowtitle
                except:
                    pass

                itemlist.append({'title': title, 'season': season, 'episode': episode, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'status': 'Continuing', 'studio': studio,
                                 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'plot': plot, 'imdb': imdb, 'tvdb': tvdb, 'poster': '0', 'thumb': '0'})
            except:
                pass

        itemlist = itemlist[::-1]
        return itemlist


    def trakt_progress_list(self, url, user, lang):
        try:
            url += '?extended=full'
            result = trakt.getTraktAsJson(url)
            items = []
        except:
            return

        sortorder = control.setting('prgr.sortorder')
        for item in result:
            try:
                num_1 = 0
                for i in list(range(0, len(item['seasons']))):
                    if item['seasons'][i]['number'] > 0: num_1 += len(item['seasons'][i]['episodes'])
                num_2 = int(item['show']['aired_episodes'])
                if num_1 >= num_2: raise Exception()

                season = str(item['seasons'][-1]['number'])

                episode = [x for x in item['seasons'][-1]['episodes'] if 'number' in x]
                episode = sorted(episode, key=lambda x: x['number'])
                episode = str(episode[-1]['number'])

                tvshowtitle = item['show']['title']
                if tvshowtitle == None or tvshowtitle == '': raise Exception()
                tvshowtitle = client.replaceHTMLCodes(tvshowtitle)

                year = item['show']['year']
                year = re.sub('[^0-9]', '', str(year))
                if int(year) > int(self.datetime.strftime('%Y')): raise Exception()

                imdb = item['show']['ids']['imdb']
                if imdb == None or imdb == '': imdb = '0'

                tvdb = item['show']['ids']['tvdb']
                if tvdb == None or tvdb == '': raise Exception()
                tvdb = re.sub('[^0-9]', '', str(tvdb))

                studio = item.get('show').get('network', '0')
                if studio == None or studio == '': studio = '0'

                last_watched = item['last_watched_at']
                if last_watched == None or last_watched == '': last_watched = '0'
                items.append({'imdb': imdb, 'tvdb': tvdb, 'tvshowtitle': tvshowtitle, 'year': year, 'studio': studio, 'snum': season, 'enum': episode, '_last_watched': last_watched})
            except:
                pass

        try:
            result = trakt.getTraktAsJson(self.hiddenprogress_link)
            result = [str(i['show']['ids']['tvdb']) for i in result]

            items = [i for i in items if not i['tvdb'] in result]
        except:
            pass

        def items_list(i):
            try:
                item = [x for x in self.blist if x['tvdb'] == i['tvdb'] and x['snum'] == i['snum'] and x['enum'] == i['enum']][0]
                item['action'] = 'episodes'
                self.list.append(item)
                return
            except:
                pass

            try:
                url = self.tvdb_info_link % (i['tvdb'], lang)
                #data = urllib_request.urlopen(url, timeout=10).read()
                data = requests.get(url, timeout=10, verify=True).content
                zip = zipfile.ZipFile(StringIO(data))
                result = zip.read('%s.xml' % lang)
                artwork = zip.read('banners.xml')
                zip.close()

                result = control.six_decode(result)
                result = result.split('<Episode>')
                item0 = [x for x in result if '<EpisodeNumber>' in x and not re.compile(r'<SeasonNumber>(.+?)</SeasonNumber>').findall(x)[0] == '0']
                item1 = sorted(item0, key=lambda k:(int(re.compile(r'<SeasonNumber>(\d+)</SeasonNumber>').findall(k)[-1]), int(re.compile(r'<EpisodeNumber>(\d+)</EpisodeNumber>').findall(k)[-1])))
                item2 = result[0]

                num = [x for x,y in enumerate(item1) if re.compile(r'<SeasonNumber>(.+?)</SeasonNumber>').findall(y)[0] == str(i['snum']) and re.compile(r'<EpisodeNumber>(.+?)</EpisodeNumber>').findall(y)[0] == str(i['enum'])][-1]
                item = [y for x,y in enumerate(item1) if x > num][0]

                #print(lang)
                #print(item)

                premiered = client.parseDOM(item, 'FirstAired')[0]
                if premiered == '' or '-00' in premiered: premiered = '0'
                premiered = client.replaceHTMLCodes(premiered)
                premiered = six.ensure_str(premiered)

                try: status = client.parseDOM(item2, 'Status')[0]
                except: status = ''
                if status == '': status = 'Ended'
                status = client.replaceHTMLCodes(status)
                status = six.ensure_str(status)

                unaired = ''

                if status == 'Ended': pass
                elif premiered == '0': raise Exception()
                elif int(re.sub(r'[^0-9]', '', str(premiered))) > int(re.sub(r'[^0-9]', '', str(self.today_date))):
                    unaired = 'true'
                    if self.showunaired != 'true': raise Exception()

                title = client.parseDOM(item, 'EpisodeName')[0]
                if title == '': title = '0'
                title = client.replaceHTMLCodes(title)
                title = six.ensure_str(title)

                season = client.parseDOM(item, 'SeasonNumber')[0]
                season = '%01d' % int(season)
                season = six.ensure_str(season)
                #if int(season) == 0:# and self.specials != 'true':
                    #raise Exception()

                episode = client.parseDOM(item, 'EpisodeNumber')[0]
                episode = re.sub(r'[^0-9]', '', '%01d' % int(episode))
                episode = six.ensure_str(episode)

                tvshowtitle = i['tvshowtitle']
                imdb, tvdb = i['imdb'], i['tvdb']

                year = i['year']
                try: year = six.ensure_str(year)
                except: pass

                try: poster = client.parseDOM(item2, 'poster')[0]
                except: poster = ''
                if not poster == '': poster = self.tvdb_image + poster
                else: poster = '0'
                poster = client.replaceHTMLCodes(poster)
                poster = six.ensure_str(poster)

                try: banner = client.parseDOM(item2, 'banner')[0]
                except: banner = ''
                if not banner == '': banner = self.tvdb_image + banner
                else: banner = '0'
                banner = client.replaceHTMLCodes(banner)
                banner = six.ensure_str(banner)

                try: fanart = client.parseDOM(item2, 'fanart')[0]
                except: fanart = ''
                if not fanart == '': fanart = self.tvdb_image + fanart
                else: fanart = '0'
                fanart = client.replaceHTMLCodes(fanart)
                fanart = six.ensure_str(fanart)

                try: thumb = client.parseDOM(item, 'filename')[0]
                except: thumb = ''
                if not thumb == '': thumb = self.tvdb_image + thumb
                else: thumb = '0'
                thumb = client.replaceHTMLCodes(thumb)
                thumb = six.ensure_str(thumb)

                if not poster == '0': pass
                elif not fanart == '0': poster = fanart
                elif not banner == '0': poster = banner

                if not banner == '0': pass
                elif not fanart == '0': banner = fanart
                elif not poster == '0': banner = poster

                if not thumb == '0': pass
                elif not fanart == '0': thumb = fanart.replace(self.tvdb_image, self.tvdb_poster)
                elif not poster == '0': thumb = poster

                # try: studio = client.parseDOM(item2, 'Network')[0]
                # except: studio = ''
                # if studio == '': studio = '0'
                # studio = client.replaceHTMLCodes(studio)
                # studio = six.ensure_str(studio)

                try: genre = client.parseDOM(item2, 'Genre')[0]
                except: genre = ''
                genre = [x for x in genre.split('|') if not x == '']
                genre = ' / '.join(genre)
                if genre == '': genre = '0'
                genre = client.replaceHTMLCodes(genre)
                genre = six.ensure_str(genre)

                try: duration = client.parseDOM(item2, 'Runtime')[0]
                except: duration = ''
                if duration == '': duration = '0'
                duration = client.replaceHTMLCodes(duration)
                duration = six.ensure_str(duration)

                if self.ratings == 'true':
                    try:
                        rating, votes = trakt.getEpisodeRating(imdb, int(season), int(episode))
                    except:
                        rating, votes = '0', '0'
                    if rating == None or rating == '0.0':
                        rating = '0'
                    if votes == None:
                        votes = '0'
                else:
                    try: rating = client.parseDOM(item, 'Rating')[0]
                    except: rating = ''
                    if rating == '': rating = '0'
                    rating = client.replaceHTMLCodes(rating)
                    rating = six.ensure_str(rating)

                    try: votes = client.parseDOM(item2, 'RatingCount')[0]
                    except: votes = '0'
                    if votes == '': votes = '0'
                    votes = client.replaceHTMLCodes(votes)
                    votes = six.ensure_str(votes)

                try: mpaa = client.parseDOM(item2, 'ContentRating')[0]
                except: mpaa = ''
                if mpaa == '': mpaa = '0'
                mpaa = client.replaceHTMLCodes(mpaa)
                mpaa = six.ensure_str(mpaa)

                try: director = client.parseDOM(item, 'Director')[0]
                except: director = ''
                director = [x for x in director.split('|') if not x == '']
                director = ' / '.join(director)
                if director == '': director = '0'
                director = client.replaceHTMLCodes(director)
                director = six.ensure_str(director)

                try: writer = client.parseDOM(item, 'Writer')[0]
                except: writer = ''
                writer = [x for x in writer.split('|') if not x == '']
                writer = ' / '.join(writer)
                if writer == '': writer = '0'
                writer = client.replaceHTMLCodes(writer)
                writer = six.ensure_str(writer)

                try: cast = client.parseDOM(item2, 'Actors')[0]
                except: cast = ''
                cast = [x for x in cast.split('|') if not x == '']
                try: cast = [(six.ensure_str(x), '') for x in cast]
                except: cast = []

                try: plot = client.parseDOM(item, 'Overview')[0]
                except: plot = ''
                if plot == '':
                    try: plot = client.parseDOM(item2, 'Overview')[0]
                    except: plot = ''
                if plot == '': plot = '0'
                plot = client.replaceHTMLCodes(plot)
                plot = six.ensure_str(plot)

                self.list.append({'title': title, 'season': season, 'episode': episode, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'status': status, 'studio': i['studio'], 'genre': genre,
                                  'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot, 'imdb': imdb, 'tvdb': tvdb, 'poster': poster,
                                  'banner': banner, 'fanart': fanart, 'thumb': thumb, 'snum': i['snum'], 'enum': i['enum'], 'action': 'episodes', 'unaired': unaired, '_last_watched': i['_last_watched'],
                                  '_sort_key': max(i['_last_watched'],premiered)})
            except:
                import traceback
                failure = traceback.format_exc()
                log_utils.log('TProgress: ' + str(failure))
                pass


        items = items[:100]

        threads = []
        for i in items: threads.append(workers.Thread(items_list, i))
        [i.start() for i in threads]
        [i.join() for i in threads]


        try:
            if sortorder == '0':
                self.list = sorted(self.list, key=lambda k: k['premiered'], reverse=True)
            else:
                self.list = sorted(self.list, key=lambda k: k['_sort_key'], reverse=True)
        except: pass

        return self.list


    def trakt_episodes_list(self, url, user, lang):
        items = self.trakt_list(url, user)

        def items_list(i):
            try:
                item = [x for x in self.blist if x['tvdb'] == i['tvdb'] and x['season'] == i['season'] and x['episode'] == i['episode']][0]
                if item['poster'] == '0': raise Exception()
                self.list.append(item)
                return
            except:
                pass

            try:
                url = self.tvdb_info_link % (i['tvdb'], lang)
                #data = urllib_request.urlopen(url, timeout=10).read()
                data = requests.get(url, timeout=10, verify=True).content
                zip = zipfile.ZipFile(StringIO(data))
                result = zip.read('%s.xml' % lang)
                artwork = zip.read('banners.xml')
                zip.close()

                result = control.six_decode(result)
                result = result.split('<Episode>')
                item = [(re.findall('<SeasonNumber>%01d</SeasonNumber>' % int(i['season']), x), re.findall('<EpisodeNumber>%01d</EpisodeNumber>' % int(i['episode']), x), x) for x in result]
                item = [x[2] for x in item if len(x[0]) > 0 and len(x[1]) > 0][0]
                item2 = result[0]

                premiered = client.parseDOM(item, 'FirstAired')[0]
                if premiered == '' or '-00' in premiered: premiered = '0'
                premiered = client.replaceHTMLCodes(premiered)
                premiered = six.ensure_str(premiered)

                try: status = client.parseDOM(item2, 'Status')[0]
                except: status = ''
                if status == '': status = 'Ended'
                status = client.replaceHTMLCodes(status)
                status = six.ensure_str(status)

                title = client.parseDOM(item, 'EpisodeName')[0]
                if title == '': title = '0'
                title = client.replaceHTMLCodes(title)
                title = six.ensure_str(title)

                season = client.parseDOM(item, 'SeasonNumber')[0]
                season = '%01d' % int(season)
                season = six.ensure_str(season)
                if int(season) == 0 and self.specials != 'true':
                    raise Exception()

                episode = client.parseDOM(item, 'EpisodeNumber')[0]
                episode = re.sub('[^0-9]', '', '%01d' % int(episode))
                episode = six.ensure_str(episode)

                tvshowtitle = i['tvshowtitle']
                imdb, tvdb = i['imdb'], i['tvdb']

                year = i['year']
                try: year = six.ensure_str(year)
                except: pass

                try: poster = client.parseDOM(item2, 'poster')[0]
                except: poster = ''
                if not poster == '': poster = self.tvdb_image + poster
                else: poster = '0'
                poster = client.replaceHTMLCodes(poster)
                poster = six.ensure_str(poster)

                try: banner = client.parseDOM(item2, 'banner')[0]
                except: banner = ''
                if not banner == '': banner = self.tvdb_image + banner
                else: banner = '0'
                banner = client.replaceHTMLCodes(banner)
                banner = six.ensure_str(banner)

                try: fanart = client.parseDOM(item2, 'fanart')[0]
                except: fanart = ''
                if not fanart == '': fanart = self.tvdb_image + fanart
                else: fanart = '0'
                fanart = client.replaceHTMLCodes(fanart)
                fanart = six.ensure_str(fanart)

                try: thumb = client.parseDOM(item, 'filename')[0]
                except: thumb = ''
                if not thumb == '': thumb = self.tvdb_image + thumb
                else: thumb = '0'
                thumb = client.replaceHTMLCodes(thumb)
                thumb = six.ensure_str(thumb)

                if not poster == '0': pass
                elif not fanart == '0': poster = fanart
                elif not banner == '0': poster = banner

                if not banner == '0': pass
                elif not fanart == '0': banner = fanart
                elif not poster == '0': banner = poster

                if not thumb == '0': pass
                elif not fanart == '0': thumb = fanart.replace(self.tvdb_image, self.tvdb_poster)
                elif not poster == '0': thumb = poster

                try: studio = client.parseDOM(item2, 'Network')[0]
                except: studio = ''
                if studio == '': studio = '0'
                studio = client.replaceHTMLCodes(studio)
                studio = six.ensure_str(studio)

                try: genre = client.parseDOM(item2, 'Genre')[0]
                except: genre = ''
                genre = [x for x in genre.split('|') if not x == '']
                genre = ' / '.join(genre)
                if genre == '': genre = '0'
                genre = client.replaceHTMLCodes(genre)
                genre = six.ensure_str(genre)

                try: duration = client.parseDOM(item2, 'Runtime')[0]
                except: duration = ''
                if duration == '': duration = '0'
                duration = client.replaceHTMLCodes(duration)
                duration = six.ensure_str(duration)

                if self.ratings == 'true':
                    try:
                        rating, votes = trakt.getEpisodeRating(imdb, int(season), int(episode))
                    except:
                        rating, votes = '0', '0'
                    if rating == None or rating == '0.0':
                        rating = '0'
                    if votes == None:
                        votes = '0'
                else:
                    try: rating = client.parseDOM(item, 'Rating')[0]
                    except: rating = ''
                    if rating == '': rating = '0'
                    rating = client.replaceHTMLCodes(rating)
                    rating = six.ensure_str(rating)

                    try: votes = client.parseDOM(item2, 'RatingCount')[0]
                    except: votes = '0'
                    if votes == '': votes = '0'
                    votes = client.replaceHTMLCodes(votes)
                    votes = six.ensure_str(votes)

                try: mpaa = client.parseDOM(item2, 'ContentRating')[0]
                except: mpaa = ''
                if mpaa == '': mpaa = '0'
                mpaa = client.replaceHTMLCodes(mpaa)
                mpaa = six.ensure_str(mpaa)

                try: director = client.parseDOM(item, 'Director')[0]
                except: director = ''
                director = [x for x in director.split('|') if not x == '']
                director = ' / '.join(director)
                if director == '': director = '0'
                director = client.replaceHTMLCodes(director)
                director = six.ensure_str(director)

                try: writer = client.parseDOM(item, 'Writer')[0]
                except: writer = ''
                writer = [x for x in writer.split('|') if not x == '']
                writer = ' / '.join(writer)
                if writer == '': writer = '0'
                writer = client.replaceHTMLCodes(writer)
                writer = six.ensure_str(writer)

                try: cast = client.parseDOM(item2, 'Actors')[0]
                except: cast = ''
                cast = [x for x in cast.split('|') if not x == '']
                try: cast = [(six.ensure_str(x), '') for x in cast]
                except: cast = []

                try: plot = client.parseDOM(item, 'Overview')[0]
                except: plot = ''
                if plot == '':
                    try: plot = client.parseDOM(item2, 'Overview')[0]
                    except: plot = ''
                if plot == '': plot = '0'
                plot = client.replaceHTMLCodes(plot)
                plot = six.ensure_str(plot)

                self.list.append({'title': title, 'season': season, 'episode': episode, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'status': status, 'studio': studio,
                                  'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot,
                                  'imdb': imdb, 'tvdb': tvdb, 'poster': poster, 'banner': banner, 'fanart': fanart, 'thumb': thumb})
            except:
                pass


        items = items[:100]

        threads = []
        for i in items: threads.append(workers.Thread(items_list, i))
        [i.start() for i in threads]
        [i.join() for i in threads]

        return self.list


    def trakt_user_list(self, url, user):
        try:
            items = trakt.getTraktAsJson(url)
        except:
            pass

        for item in items:
            try:
                try: name = item['list']['name']
                except: name = item['name']
                name = client.replaceHTMLCodes(name)

                try: url = (trakt.slug(item['list']['user']['username']), item['list']['ids']['slug'])
                except: url = ('me', item['ids']['slug'])
                url = self.traktlist_link % url
                url = six.ensure_str(url)

                self.list.append({'name': name, 'url': url, 'context': url})
            except:
                pass

        self.list = sorted(self.list, key=lambda k: utils.title_key(k['name']))
        return self.list


    def tvmaze_list(self, url, limit):
        try:
            result = client.request(url)

            itemlist = []
            items = json.loads(result)
        except:
            return

        for item in items:
            try:
                if not 'english' in item['show']['language'].lower(): raise Exception()

                if limit == True and not 'scripted' in item['show']['type'].lower(): raise Exception()

                title = item['name']
                if title == None or title == '': raise Exception()
                title = client.replaceHTMLCodes(title)
                title = six.ensure_str(title)

                season = item['season']
                season = re.sub('[^0-9]', '', '%01d' % int(season))
                if season == '0': raise Exception()
                season = six.ensure_str(season)

                episode = item['number']
                episode = re.sub('[^0-9]', '', '%01d' % int(episode))
                if episode == '0': raise Exception()
                episode = six.ensure_str(episode)

                tvshowtitle = item['show']['name']
                if tvshowtitle == None or tvshowtitle == '': raise Exception()
                tvshowtitle = client.replaceHTMLCodes(tvshowtitle)
                tvshowtitle = six.ensure_str(tvshowtitle)

                year = item['show']['premiered']
                year = re.findall('(\d{4})', year)[0]
                year = six.ensure_str(year)

                imdb = item['show']['externals']['imdb']
                if imdb == None or imdb == '': imdb = '0'
                else: imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))
                imdb = six.ensure_str(imdb)

                tvdb = item['show']['externals']['thetvdb']
                if tvdb == None or tvdb == '': raise Exception()
                tvdb = re.sub('[^0-9]', '', str(tvdb))
                tvdb = six.ensure_str(tvdb)

                poster = '0'
                try: poster = item['show']['image']['original']
                except: poster = '0'
                if poster == None or poster == '': poster = '0'
                poster = six.ensure_str(poster)

                try: thumb1 = item['show']['image']['original']
                except: thumb1 = '0'
                try: thumb2 = item['image']['original']
                except: thumb2 = '0'
                if thumb2 == None or thumb2 == '0': thumb = thumb1
                else: thumb = thumb2
                if thumb == None or thumb == '': thumb = '0'
                thumb = six.ensure_str(thumb)

                premiered = item['airdate']
                try: premiered = re.findall('(\d{4}-\d{2}-\d{2})', premiered)[0]
                except: premiered = '0'
                premiered = six.ensure_str(premiered)

                try: studio = item['show']['network']['name']
                except: studio = '0'
                if studio == None: studio = '0'
                studio = six.ensure_str(studio)

                try: genre = item['show']['genres']
                except: genre = '0'
                genre = [i.title() for i in genre]
                if genre == []: genre = '0'
                genre = ' / '.join(genre)
                genre = six.ensure_str(genre)

                try: duration = item['show']['runtime']
                except: duration = '0'
                if duration == None: duration = '0'
                duration = str(duration)
                duration = six.ensure_str(duration)

                if self.ratings == 'true':
                    try:
                        rating, votes = trakt.getEpisodeRating(imdb, int(season), int(episode))
                    except:
                        rating, votes = '0', '0'
                    if rating == None or rating == '0.0':
                        rating = '0'
                    if votes == None:
                        votes = '0'
                else:
                    try: rating = item['show']['rating']['average']
                    except: rating = '0'
                    if rating == None or rating == '0.0': rating = '0'
                    rating = str(rating)
                    rating = six.ensure_str(rating)

                    votes = '0'

                try: plot = item['show']['summary']
                except: plot = '0'
                if plot == None: plot = '0'
                plot = re.sub('<.+?>|</.+?>|\n', '', plot)
                plot = client.replaceHTMLCodes(plot)
                plot = six.ensure_str(plot)

                itemlist.append({'title': title, 'season': season, 'episode': episode, 'tvshowtitle': tvshowtitle, 'year': year, 'premiered': premiered, 'status': 'Continuing', 'studio': studio,
                                 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'plot': plot, 'imdb': imdb, 'tvdb': tvdb, 'poster': poster, 'thumb': thumb})
            except:
                pass

        itemlist = itemlist[::-1]

        return itemlist


    def episodeDirectory(self, items):
        if items == None or len(items) == 0: control.idle() ; sys.exit()

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        addonPoster, addonBanner = control.addonPoster(), control.addonBanner()

        addonFanart, settingFanart = control.addonFanart(), control.setting('fanart')

        traktCredentials = trakt.getTraktCredentialsInfo()

        try: isOld = False ; control.item().getArt('type')
        except: isOld = True

        isPlayable = 'true' if not 'plugin' in control.infoLabel('Container.PluginName') else 'false'

        indicators = playcount.getTVShowIndicators(refresh=True)

        try: multi = [i['tvshowtitle'] for i in items]
        except: multi = []
        multi = len([x for y,x in enumerate(multi) if x not in multi[:y]])
        multi = True if multi > 1 else False

        try: sysaction = items[0]['action']
        except: sysaction = ''

        isFolder = False if not sysaction == 'episodes' else True

        playbackMenu = six.ensure_str(control.lang(32063)) if control.setting('hosts.mode') == '2' else six.ensure_str(control.lang(32064))

        watchedMenu = six.ensure_str(control.lang(32068)) if trakt.getTraktIndicatorsInfo() == True else six.ensure_str(control.lang(32066))

        unwatchedMenu = six.ensure_str(control.lang(32069)) if trakt.getTraktIndicatorsInfo() == True else six.ensure_str(control.lang(32067))

        queueMenu = six.ensure_str(control.lang(32065))

        traktManagerMenu = six.ensure_str(control.lang(32070))

        tvshowBrowserMenu = six.ensure_str(control.lang(32071))

        addToLibrary = six.ensure_str(control.lang(32551))

        infoMenu = six.ensure_str(control.lang(32101))

        clearProviders = six.ensure_str(control.lang(32081))

        for i in items:
            try:
                if not 'label' in i: i['label'] = i['title']

                if i['label'] == '0':
                    label = '%sx%02d . %s %s' % (i['season'], int(i['episode']), 'Episode', i['episode'])
                else:
                    label = '%sx%02d . %s' % (i['season'], int(i['episode']), i['label'])
                if multi == True:
                    label = '%s - %s' % (i['tvshowtitle'], label)
                
                try:
                    if i['unaired'] == 'true':
                        label = '[COLOR crimson][I]%s[/I][/COLOR]' % label
                except:
                    pass

                imdb, tvdb, year, season, episode = i['imdb'], i['tvdb'], i['year'], i['season'], i['episode']

                systitle = urllib_parse.quote_plus(i['title'])
                systvshowtitle = urllib_parse.quote_plus(i['tvshowtitle'])
                syspremiered = urllib_parse.quote_plus(i['premiered'])

                meta = dict((k,v) for k, v in six.iteritems(i) if not v == '0')
                meta.update({'mediatype': 'episode'})
                meta.update({'code': imdb, 'imdbnumber': imdb})
                meta.update({'trailer': '%s?action=trailer&name=%s' % (sysaddon, systvshowtitle)})
                if not 'duration' in i: meta.update({'duration': '60'})
                elif i['duration'] == '0': meta.update({'duration': '60'})
                try: meta.update({'duration': str(int(meta['duration']) * 60)})
                except: pass
                try: meta.update({'genre': cleangenre.lang(meta['genre'], self.lang)})
                except: pass
                try: meta.update({'year': re.findall('(\d{4})', i['premiered'])[0]})
                except: pass
                try: meta.update({'title': i['label']})
                except: pass

                try: meta.update({'tvshowyear': i['year']}) # Kodi uses the year (the year the show started) as the year for the episode. Change it from the premiered date.
                except: pass

                sysmeta = urllib_parse.quote_plus(json.dumps(meta))


                url = '%s?action=play&title=%s&year=%s&imdb=%s&tvdb=%s&season=%s&episode=%s&tvshowtitle=%s&premiered=%s&meta=%s&t=%s' % (sysaddon, systitle, year, imdb, tvdb, season, episode, systvshowtitle, syspremiered, sysmeta, self.systime)
                sysurl = urllib_parse.quote_plus(url)

                path = '%s?action=play&title=%s&year=%s&imdb=%s&tvdb=%s&season=%s&episode=%s&tvshowtitle=%s&premiered=%s' % (sysaddon, systitle, year, imdb, tvdb, season, episode, systvshowtitle, syspremiered)

                if isFolder == True:
                    url = '%s?action=episodes&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s&season=%s&episode=%s' % (sysaddon, systvshowtitle, year, imdb, tvdb, season, episode)


                cm = []

                cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

                if multi == True:
                    cm.append((tvshowBrowserMenu, 'Container.Update(%s?action=seasons&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s,return)' % (sysaddon, systvshowtitle, year, imdb, tvdb)))

                try:
                    overlay = int(playcount.getEpisodeOverlay(indicators, imdb, tvdb, season, episode))
                    if overlay == 7:
                        cm.append((unwatchedMenu, 'RunPlugin(%s?action=episodePlaycount&imdb=%s&tvdb=%s&season=%s&episode=%s&query=6)' % (sysaddon, imdb, tvdb, season, episode)))
                        meta.update({'playcount': 1, 'overlay': 7})
                    else:
                        cm.append((watchedMenu, 'RunPlugin(%s?action=episodePlaycount&imdb=%s&tvdb=%s&season=%s&episode=%s&query=7)' % (sysaddon, imdb, tvdb, season, episode)))
                        meta.update({'playcount': 0, 'overlay': 6})
                except:
                    pass

                if traktCredentials == True:
                    cm.append((traktManagerMenu, 'RunPlugin(%s?action=traktManager&name=%s&tvdb=%s&content=tvshow)' % (sysaddon, systvshowtitle, tvdb)))

                if isFolder == False:
                    cm.append((playbackMenu, 'RunPlugin(%s?action=alterSources&url=%s&meta=%s)' % (sysaddon, sysurl, sysmeta)))

                if isOld == True:
                    cm.append((infoMenu, 'Action(Info)'))

                cm.append((addToLibrary, 'RunPlugin(%s?action=tvshowToLibrary&tvshowtitle=%s&year=%s&imdb=%s&tvdb=%s)' % (sysaddon, systvshowtitle, year, imdb, tvdb)))

                cm.append((clearProviders, 'RunPlugin(%s?action=clearCacheProviders)' % sysaddon))

                item = control.item(label=label)

                art = {}

                if 'poster' in i and not i['poster'] == '0':
                    art.update({'poster': i['poster'], 'tvshow.poster': i['poster'], 'season.poster': i['poster']})
                else:
                    art.update({'poster': addonPoster})

                if 'thumb' in i and not i['thumb'] == '0':
                    art.update({'icon': i['thumb'], 'thumb': i['thumb'], 'poster': i['thumb']})
                elif 'fanart' in i and not i['fanart'] == '0':
                    art.update({'icon': i['fanart'], 'thumb': i['fanart']})
                elif 'poster' in i and not i['poster'] == '0':
                    art.update({'icon': i['poster'], 'thumb': i['poster']})
                else:
                    art.update({'icon': addonFanart, 'thumb': addonFanart})

                if 'banner' in i and not i['banner'] == '0':
                    art.update({'banner': i['banner']})
                elif 'fanart' in i and not i['fanart'] == '0':
                    art.update({'banner': i['fanart']})
                else:
                    art.update({'banner': addonBanner})

                if settingFanart == 'true' and 'fanart' in i and not i['fanart'] == '0':
                    item.setProperty('Fanart_Image', i['fanart'])
                elif not addonFanart == None:
                    item.setProperty('Fanart_Image', addonFanart)

                item.setArt(art)
                item.addContextMenuItems(cm)
                item.setProperty('IsPlayable', isPlayable)
                item.setInfo(type='Video', infoLabels = control.metadataClean(meta))

                video_streaminfo = {'codec': 'h264'}
                item.addStreamInfo('video', video_streaminfo)

                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)
            except:
                pass

        control.content(syshandle, 'episodes')
        control.directory(syshandle, cacheToDisc=True)
        views.setView('episodes', {'skin.estuary': 55, 'skin.confluence': 504})


    def addDirectory(self, items, queue=False):
        if items == None or len(items) == 0: control.idle() ; sys.exit()

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        addonFanart, addonThumb, artPath = control.addonFanart(), control.addonThumb(), control.artPath()

        queueMenu = six.ensure_str(control.lang(32065))

        for i in items:
            try:
                name = i['name']

                if i['image'].startswith('http'): thumb = i['image']
                elif not artPath == None: thumb = os.path.join(artPath, i['image'])
                else: thumb = addonThumb

                url = '%s?action=%s' % (sysaddon, i['action'])
                try: url += '&url=%s' % urllib_parse.quote_plus(i['url'])
                except: pass

                cm = []

                if queue == True:
                    cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

                item = control.item(label=name)

                item.setArt({'icon': thumb, 'thumb': thumb})
                if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)

                item.addContextMenuItems(cm)

                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=True)
            except:
                pass

        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)


