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


import re,sys,time,xbmc
import simplejson as json
import hashlib,os,base64,codecs,gzip#,urllib,xmlrpclib, StringIO

import six
from six.moves import urllib_parse, xmlrpc_client

try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

from resources.lib.modules import control
from resources.lib.modules import cleantitle
from resources.lib.modules import playcount
from resources.lib.modules import trakt



class player(xbmc.Player):
    def __init__ (self):
        xbmc.Player.__init__(self)


    def run(self, title, year, season, episode, imdb, tvdb, url, meta):
        try:
            control.sleep(200)

            self.totalTime = 0 ; self.currentTime = 0

            self.content = 'movie' if season == None or episode == None else 'episode'

            self.title = title ; self.year = year
            self.name = urllib_parse.quote_plus(title) + urllib_parse.quote_plus(' (%s)' % year) if self.content == 'movie' else urllib_parse.quote_plus(title) + urllib_parse.quote_plus(' S%01dE%01d' % (int(season), int(episode)))
            self.name = urllib_parse.unquote_plus(self.name)
            self.season = '%01d' % int(season) if self.content == 'episode' else None
            self.episode = '%01d' % int(episode) if self.content == 'episode' else None

            self.DBID = None
            self.imdb = imdb if not imdb == None else '0'
            self.tvdb = tvdb if not tvdb == None else '0'
            self.ids = {'imdb': self.imdb, 'tvdb': self.tvdb}
            self.ids = dict((k,v) for k, v in six.iteritems(self.ids) if not v == '0')

            self.offset = bookmarks().get(self.name, season, episode, imdb, self.year)

            poster, thumb, meta = self.getMeta(meta)

            item = control.item(path=url)
            item.setArt({'icon': thumb, 'thumb': thumb, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster})
            item.setInfo(type='video', infoLabels = control.metadataClean(meta))

            if 'plugin' in control.infoLabel('Container.PluginName'):
                control.player.play(url, item)

            control.resolve(int(sys.argv[1]), True, item)

            control.window.setProperty('script.trakt.ids', json.dumps(self.ids))

            self.keepPlaybackAlive()

            control.window.clearProperty('script.trakt.ids')
        except:
            return


    def getMeta(self, meta):
        try:
            poster = meta['poster'] if 'poster' in meta else '0'
            thumb = meta['thumb'] if 'thumb' in meta else poster

            if poster == '0': poster = control.addonPoster()

            return (poster, thumb, meta)
        except:
            pass

        try:
            if not self.content == 'movie': raise Exception()

            meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetMovies", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties" : ["title", "originaltitle", "year", "genre", "studio", "country", "runtime", "rating", "votes", "mpaa", "director", "writer", "plot", "plotoutline", "tagline", "thumbnail", "file"]}, "id": 1}' % (self.year, str(int(self.year)+1), str(int(self.year)-1)))
            meta = six.ensure_text(meta, errors='ignore')
            meta = json.loads(meta)['result']['movies']

            t = cleantitle.get(self.title)
            meta = [i for i in meta if self.year == str(i['year']) and (t == cleantitle.get(i['title']) or t == cleantitle.get(i['originaltitle']))][0]

            for k, v in six.iteritems(meta):
                if type(v) == list:
                    try: meta[k] = str(' / '.join([six.ensure_str(i) for i in v]))
                    except: meta[k] = ''
                else:
                    try: meta[k] = str(six.ensure_str(v))
                    except: meta[k] = str(v)

            if not 'plugin' in control.infoLabel('Container.PluginName'):
                self.DBID = meta['movieid']

            poster = thumb = meta['thumbnail']

            return (poster, thumb, meta)
        except:
            pass

        try:
            if not self.content == 'episode': raise Exception()

            meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetTVShows", "params": {"filter":{"or": [{"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}, {"field": "year", "operator": "is", "value": "%s"}]}, "properties" : ["title", "year", "thumbnail", "file"]}, "id": 1}' % (self.year, str(int(self.year)+1), str(int(self.year)-1)))
            meta = six.ensure_text(meta, errors='ignore')
            meta = json.loads(meta)['result']['tvshows']

            t = cleantitle.get(self.title)
            meta = [i for i in meta if self.year == str(i['year']) and t == cleantitle.get(i['title'])][0]

            tvshowid = meta['tvshowid'] ; poster = meta['thumbnail']

            meta = control.jsonrpc('{"jsonrpc": "2.0", "method": "VideoLibrary.GetEpisodes", "params":{ "tvshowid": %d, "filter":{"and": [{"field": "season", "operator": "is", "value": "%s"}, {"field": "episode", "operator": "is", "value": "%s"}]}, "properties": ["title", "season", "episode", "showtitle", "firstaired", "runtime", "rating", "director", "writer", "plot", "thumbnail", "file"]}, "id": 1}' % (tvshowid, self.season, self.episode))
            meta = six.ensure_text(meta, errors='ignore')
            meta = json.loads(meta)['result']['episodes'][0]

            for k, v in six.iteritems(meta):
                if type(v) == list:
                    try: meta[k] = str(' / '.join([six.ensure_str(i) for i in v]))
                    except: meta[k] = ''
                else:
                    try: meta[k] = str(six.ensure_str(v))
                    except: meta[k] = str(v)

            if not 'plugin' in control.infoLabel('Container.PluginName'):
                self.DBID = meta['episodeid']

            thumb = meta['thumbnail']

            return (poster, thumb, meta)
        except:
            pass


        poster, thumb, meta = '', '', {'title': self.name}
        return (poster, thumb, meta)


    def keepPlaybackAlive(self):
        pname = '%s.player.overlay' % control.addonInfo('id')
        control.window.clearProperty(pname)


        if self.content == 'movie':
            overlay = playcount.getMovieOverlay(playcount.getMovieIndicators(), self.imdb)

        elif self.content == 'episode':
            overlay = playcount.getEpisodeOverlay(playcount.getTVShowIndicators(), self.imdb, self.tvdb, self.season, self.episode)

        else:
            overlay = '6'


        for i in list(range(0, 240)):
            if self.isPlayingVideo(): break
            xbmc.sleep(1000)


        if overlay == '7':

            while self.isPlayingVideo():
                try:
                    self.totalTime = self.getTotalTime()
                    self.currentTime = self.getTime()
                except:
                    pass
                xbmc.sleep(2000)


        elif self.content == 'movie':

            while self.isPlayingVideo():
                try:
                    self.totalTime = self.getTotalTime()
                    self.currentTime = self.getTime()

                    watcher = (self.currentTime / self.totalTime >= .9)
                    property = control.window.getProperty(pname)

                    if watcher == True and not property == '7':
                        control.window.setProperty(pname, '7')
                        playcount.markMovieDuringPlayback(self.imdb, '7')

                    elif watcher == False and not property == '6':
                        control.window.setProperty(pname, '6')
                        playcount.markMovieDuringPlayback(self.imdb, '6')
                except:
                    pass
                xbmc.sleep(2000)


        elif self.content == 'episode':

            while self.isPlayingVideo():
                try:
                    self.totalTime = self.getTotalTime()
                    self.currentTime = self.getTime()

                    watcher = (self.currentTime / self.totalTime >= .9)
                    property = control.window.getProperty(pname)

                    if watcher == True and not property == '7':
                        control.window.setProperty(pname, '7')
                        playcount.markEpisodeDuringPlayback(self.imdb, self.tvdb, self.season, self.episode, '7')

                    elif watcher == False and not property == '6':
                        control.window.setProperty(pname, '6')
                        playcount.markEpisodeDuringPlayback(self.imdb, self.tvdb, self.season, self.episode, '6')
                except:
                    pass
                xbmc.sleep(2000)


        control.window.clearProperty(pname)


    def libForPlayback(self):
        try:
            if self.DBID == None: raise Exception()

            if self.content == 'movie':
                rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetMovieDetails", "params": {"movieid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)
            elif self.content == 'episode':
                rpc = '{"jsonrpc": "2.0", "method": "VideoLibrary.SetEpisodeDetails", "params": {"episodeid" : %s, "playcount" : 1 }, "id": 1 }' % str(self.DBID)

            control.jsonrpc(rpc)
            control.refresh()
        except:
            pass


    def idleForPlayback(self):
        for i in list(range(0, 400)):
            if control.condVisibility('Window.IsActive(busydialog)') == 1 or control.condVisibility('Window.IsActive(busydialognocancel)') == 1:
                control.sleep(100)
            else:
                control.execute('Dialog.Close(all,true)')
                break


    def onAVStarted(self):
        control.execute('Dialog.Close(all,true)')

        if control.setting('bookmarks') == 'true' and not self.offset == '0' and self.isPlayingVideo(): 
            if control.setting('bookmarks.auto') == 'true':
                self.seekTime(float(self.offset))
            else:
                self.pause()
                minutes, seconds = divmod(float(self.offset), 60);
                hours, minutes = divmod(minutes, 60)
                label = '%02d:%02d:%02d' % (hours, minutes, seconds)
                label = (control.lang2(12022).format(label))
                if control.setting('rersume.source') == '1' and trakt.getTraktCredentialsInfo() == True:
                    yes = control.yesnoDialog(label + '[CR]  (Trakt scrobble)', heading=control.lang2(13404))
                else:
                    yes = control.yesnoDialog(label, heading=control.lang2(13404))
                if yes:
                    self.seekTime(float(self.offset))
                self.pause()

        subtitles().get(self.name, self.imdb, self.season, self.episode)
        self.idleForPlayback()


    def onPlayBackStarted(self):
        if int(control.getKodiVersion()) < 18:
            control.execute('Dialog.Close(all,true)')

            if control.setting('bookmarks') == 'true' and not self.offset == '0' and self.isPlayingVideo(): 
                if control.setting('bookmarks.auto') == 'true':
                    self.seekTime(float(self.offset))
                else:
                    self.pause()
                    minutes, seconds = divmod(float(self.offset), 60);
                    hours, minutes = divmod(minutes, 60)
                    label = '%02d:%02d:%02d' % (hours, minutes, seconds)
                    label = (six.ensure_str(control.lang2(12022).format(label)))
                    if control.setting('rersume.source') == '1' and trakt.getTraktCredentialsInfo() == True:
                        yes = control.yesnoDialog(label + '[CR]  (Trakt scrobble)', heading=control.lang2(13404))
                    else:
                        yes = control.yesnoDialog(label, heading=six.ensure_str(control.lang2(13404)))
                    if yes:
                        self.seekTime(float(self.offset))
                    self.pause()

            subtitles().get(self.name, self.imdb, self.season, self.episode)
            self.idleForPlayback()
        else:
            self.onAVStarted()


    def onPlayBackStopped(self):
        #control.sleep(3000)
        if int(self.currentTime) > 120:
            if control.setting('bookmarks') == 'true':
                bookmarks().reset(self.currentTime, self.totalTime, self.name, self.year)
            if (trakt.getTraktCredentialsInfo() == True and control.setting('trakt.scrobble') == 'true'):
                bookmarks().set_scrobble(self.currentTime, self.totalTime, self.content, self.imdb, self.tvdb, self.season, self.episode)

        try:
            if float(self.currentTime / self.totalTime) >= 0.92:
                self.libForPlayback()
        except:
            pass

        if control.setting('crefresh') == 'true':
            control.refresh()


    def onPlayBackEnded(self):
        self.libForPlayback()


class subtitles:
    def get(self, name, imdb, season, episode):
        try:
            if not control.setting('subtitles') == 'true': raise Exception()


            langDict = {'Afrikaans': 'afr', 'Albanian': 'alb', 'Arabic': 'ara', 'Armenian': 'arm', 'Basque': 'baq', 'Bengali': 'ben', 'Bosnian': 'bos', 'Breton': 'bre', 'Bulgarian': 'bul', 'Burmese': 'bur', 'Catalan': 'cat', 'Chinese': 'chi', 'Croatian': 'hrv', 'Czech': 'cze', 'Danish': 'dan', 'Dutch': 'dut', 'English': 'eng', 'Esperanto': 'epo', 'Estonian': 'est', 'Finnish': 'fin', 'French': 'fre', 'Galician': 'glg', 'Georgian': 'geo', 'German': 'ger', 'Greek': 'ell', 'Hebrew': 'heb', 'Hindi': 'hin', 'Hungarian': 'hun', 'Icelandic': 'ice', 'Indonesian': 'ind', 'Italian': 'ita', 'Japanese': 'jpn', 'Kazakh': 'kaz', 'Khmer': 'khm', 'Korean': 'kor', 'Latvian': 'lav', 'Lithuanian': 'lit', 'Luxembourgish': 'ltz', 'Macedonian': 'mac', 'Malay': 'may', 'Malayalam': 'mal', 'Manipuri': 'mni', 'Mongolian': 'mon', 'Montenegrin': 'mne', 'Norwegian': 'nor', 'Occitan': 'oci', 'Persian': 'per', 'Polish': 'pol', 'Portuguese': 'por,pob', 'Portuguese(Brazil)': 'pob,por', 'Romanian': 'rum', 'Russian': 'rus', 'Serbian': 'scc', 'Sinhalese': 'sin', 'Slovak': 'slo', 'Slovenian': 'slv', 'Spanish': 'spa', 'Swahili': 'swa', 'Swedish': 'swe', 'Syriac': 'syr', 'Tagalog': 'tgl', 'Tamil': 'tam', 'Telugu': 'tel', 'Thai': 'tha', 'Turkish': 'tur', 'Ukrainian': 'ukr', 'Urdu': 'urd'}

            codePageDict = {'ara': 'cp1256', 'ar': 'cp1256', 'ell': 'cp1253', 'el': 'cp1253', 'heb': 'cp1255', 'he': 'cp1255', 'tur': 'cp1254', 'tr': 'cp1254', 'rus': 'cp1251', 'ru': 'cp1251'}

            quality = ['bluray', 'hdrip', 'brrip', 'bdrip', 'dvdrip', 'webrip', 'hdtv']


            langs = []
            try:
                try: langs = langDict[control.setting('subtitles.lang.1')].split(',')
                except: langs.append(langDict[control.setting('subtitles.lang.1')])
            except: pass
            try:
                try: langs = langs + langDict[control.setting('subtitles.lang.2')].split(',')
                except: langs.append(langDict[control.setting('subtitles.lang.2')])
            except: pass

            try: subLang = xbmc.Player().getSubtitles()
            except: subLang = ''
            if subLang == langs[0]: raise Exception()

            un = control.setting('os.user')
            pw = control.setting('os.pass')

            server = xmlrpc_client.Server('http://api.opensubtitles.org/xml-rpc', verbose=0)
            token = server.LogIn(un, pw, 'en', 'XBMC_Subtitles_Unofficial_v5.2.14')['token']

            sublanguageid = ','.join(langs) ; imdbid = re.sub('[^0-9]', '', imdb)

            if not (season == None or episode == None):
                result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid, 'season': season, 'episode': episode}])['data']
                fmt = ['hdtv']
            else:
                result = server.SearchSubtitles(token, [{'sublanguageid': sublanguageid, 'imdbid': imdbid}])['data']
                try: vidPath = xbmc.Player().getPlayingFile()
                except: vidPath = ''
                fmt = re.split('\.|\(|\)|\[|\]|\s|\-', vidPath)
                fmt = [i.lower() for i in fmt]
                fmt = [i for i in fmt if i in quality]

            filter = []
            result = [i for i in result if i['SubSumCD'] == '1']

            for lang in langs:
                filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in fmt)]
                filter += [i for i in result if i['SubLanguageID'] == lang and any(x in i['MovieReleaseName'].lower() for x in quality)]
                filter += [i for i in result if i['SubLanguageID'] == lang]

            try: lang = xbmc.convertLanguage(filter[0]['SubLanguageID'], xbmc.ISO_639_1)
            except: lang = filter[0]['SubLanguageID']

            subname = str(filter[0]['SubFileName'])

            content = [filter[0]['IDSubtitleFile'],]
            content = server.DownloadSubtitles(token, content)
            content = base64.b64decode(content['data'][0]['data'])
            content = gzip.GzipFile(fileobj=six.BytesIO(content)).read()
            if six.PY3: content = six.ensure_text(content)

            subtitle = control.transPath('special://temp/')
            subtitle = os.path.join(subtitle, 'TemporarySubs.%s.srt' % lang)

            codepage = codePageDict.get(lang, '')
            if codepage and control.setting('subtitles.utf') == 'true':
                try:
                    content_encoded = codecs.decode(content, codepage)
                    content = codecs.encode(content_encoded, 'utf-8')
                except:
                    pass

            file = control.openFile(subtitle, 'w')
            file.write(str(content))
            file.close()

            xbmc.sleep(1000)
            xbmc.Player().setSubtitles(subtitle)

            if control.setting('subtitles.notify') == 'true':
                if xbmc.Player().isPlaying() and xbmc.Player().isPlayingVideo():
                    control.execute('Dialog.Close(all,true)')
                    xbmc.sleep(3000)
                    control.infoDialog(subname, heading='{} subtitles downloaded'.format(str(lang).upper()), time=6000)
        except:
            pass


class bookmarks:
    def get(self, name, season, episode, imdb, year='0'):
        offset = '0'

        if control.setting('rersume.source') == '1' and trakt.getTraktCredentialsInfo() == True:
            try:

                if not episode is None:

                    # Looking for a Episode progress
                    traktInfo = trakt.getTraktAsJson('https://api.trakt.tv/sync/playback/episodes?extended=full')
                    for i in traktInfo:
                        if imdb == i['show']['ids']['imdb']:
                            # Checking Episode Number
                            if int(season) == i['episode']['season'] and int(episode) == i['episode']['number']:
                                # Calculating Offset to seconds
                                offset = (float(i['progress'] / 100) * int(i['episode']['runtime']) * 60)
                                seekable = 1 < i['progress'] < 95
                                if not seekable:
                                    offset = '0'
                else:

                    # Looking for a Movie Progress
                    traktInfo = trakt.getTraktAsJson('https://api.trakt.tv/sync/playback/movies?extended=full')
                    for i in traktInfo:
                        if imdb == i['movie']['ids']['imdb']:
                            # Calculating Offset to seconds
                            offset = (float(i['progress'] / 100) * int(i['movie']['runtime']) * 60)
                            seekable = 1 < i['progress'] < 95
                            if not seekable:
                                offset = '0'

                return offset

            except:
                return '0'

        else:
            try:
                offset = '0'

                idFile = hashlib.md5()
                for i in name: idFile.update(str(i))
                for i in year: idFile.update(str(i))
                idFile = str(idFile.hexdigest())

                dbcon = database.connect(control.bookmarksFile)
                dbcur = dbcon.cursor()
                dbcur.execute("SELECT * FROM bookmark WHERE idFile = '%s'" % idFile)
                match = dbcur.fetchone()
                self.offset = str(match[1])
                dbcon.commit()
                if self.offset == '0':
                    raise Exception()

                return self.offset
            except:
                return offset


    def reset(self, current_time, total_time, _name, _year='0'):
        try:
            timeInSeconds = str(current_time)
            ok = int(current_time) > 120 and (current_time / total_time) <= .95

            idFile = hashlib.md5()
            for i in _name: idFile.update(str(i))
            for i in _year: idFile.update(str(i))
            idFile = str(idFile.hexdigest())
            control.makeFile(control.dataPath)
            dbcon = database.connect(control.bookmarksFile)
            dbcur = dbcon.cursor()
            dbcur.execute("CREATE TABLE IF NOT EXISTS bookmark (""idFile TEXT, ""timeInSeconds TEXT, ""UNIQUE(idFile)"");")
            dbcur.execute("DELETE FROM bookmark WHERE idFile = '%s'" % idFile)
            if ok: dbcur.execute("INSERT INTO bookmark Values (?, ?)", (idFile, timeInSeconds))
            dbcon.commit()
        except:
            pass


    def set_scrobble(self, current_time, total_time, _content, _imdb='', _tvdb='', _season='', _episode=''):
        try:
            percent = float((current_time / total_time)) * 100
            if percent < 95:
                trakt.scrobbleMovie(_imdb, percent) if _content == 'movie' else trakt.scrobbleEpisode(_tvdb, _season, _episode, percent)
                if control.setting('trakt.scrobble.notify') == 'true':
                    control.infoDialog('Trakt: Scrobbled')
        except:
            import traceback
            from resources.lib.modules import log_utils
            failure = traceback.format_exc()
            log_utils.log('Scrobble - Exception: ' + str(failure))
            control.infoDialog('Scrobble Failed')


