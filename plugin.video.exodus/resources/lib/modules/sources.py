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


import sys,re,random,datetime,time,traceback
import simplejson as json

import six
from six.moves import urllib_parse, zip, reduce

from resources.lib.modules import trakt
from resources.lib.modules import tvmaze
from resources.lib.modules import cache
from resources.lib.modules import control
from resources.lib.modules import cleantitle
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import workers
from resources.lib.modules import source_utils
from resources.lib.modules import log_utils
#from resources.lib.modules import thexem

try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

try: import urlresolver
except: pass

try: import xbmc
except: pass

class sources:
    def __init__(self):
        self.getConstants()
        self.sources = []

    def play(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select):

        try:
            url = None

            items = self.getSources(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered)

            select = control.setting('hosts.mode') if select == None else select

            title = tvshowtitle if not tvshowtitle == None else title
            title = self.getTitle(title)

            if len(items) > 0:

                if select == '1' and 'plugin' in control.infoLabel('Container.PluginName'):
                    control.window.clearProperty(self.itemProperty)
                    control.window.setProperty(self.itemProperty, json.dumps(items))

                    control.window.clearProperty(self.metaProperty)
                    control.window.setProperty(self.metaProperty, meta)

                    control.sleep(200)

                    return control.execute('Container.Update(%s?action=addItem&title=%s)' % (sys.argv[0], urllib_parse.quote_plus(title)))

                elif select == '0' or select == '1':
                    url = self.sourcesDialog(items)

                else:
                    url = self.sourcesDirect(items)


            if url == 'close://' or url == None:
                self.url = url
                return self.errorForSources()

            try: meta = json.loads(meta)
            except: pass

            from resources.lib.modules.player import player
            player().run(title, year, season, episode, imdb, tvdb, url, meta)
        except:
            pass


    def addItem(self, title):

        def sourcesDirMeta(metadata):
            if metadata == None: return metadata
            allowed = ['icon', 'poster', 'poster2', 'poster3', 'fanart', 'fanart2', 'thumb', 'title', 'year', 'tvshowtitle', 'season', 'episode', 'rating', 'plot', 'trailer', 'mediatype']
            return {k: v for k, v in six.iteritems(metadata) if k in allowed}

        control.playlist.clear()
        items = control.window.getProperty(self.itemProperty)
        items = json.loads(items)

        if items == None or len(items) == 0: control.idle() ; sys.exit()

        meta = control.window.getProperty(self.metaProperty)
        meta = json.loads(meta)
        meta = sourcesDirMeta(meta)

        # (Kodi bug?) [name,role] is incredibly slow on this directory, [name] is barely tolerable, so just nuke it for speed!
        #if 'cast' in meta: del(meta['cast'])

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        downloads = True if control.setting('downloads') == 'true' and not (control.setting('movie.download.path') == '' or control.setting('tv.download.path') == '') else False

        listMeta = control.setting('source.list.meta')

        systitle = sysname = urllib_parse.quote_plus(title)

        if 'tvshowtitle' in meta and 'season' in meta and 'episode' in meta:
            sysname += urllib_parse.quote_plus(' S%02dE%02d' % (int(meta['season']), int(meta['episode'])))
        elif 'year' in meta:
            sysname += urllib_parse.quote_plus(' (%s)' % meta['year'])


        poster = meta.get('poster3') or meta.get('poster2') or meta.get('poster') or control.addonPoster()

        fanart = meta.get('fanart2') or meta.get('fanart') or control.addonFanart()

        thumb = meta.get('thumb') or poster or fanart

        if not control.setting('fanart') == 'true': fanart = control.addonFanart()

        #banner = meta['banner'] if 'banner' in meta else '0'
        #if banner == '0': banner = poster
        #if banner == '0': banner = control.addonBanner()

        sysimage = urllib_parse.quote_plus(six.ensure_str(poster))

        downloadMenu = six.ensure_str(control.lang(32403))


        for i in list(range(len(items))):
            try:
                label = str(items[i]['label'])

                syssource = urllib_parse.quote_plus(json.dumps([items[i]]))

                sysurl = '%s?action=playItem&title=%s&source=%s' % (sysaddon, systitle, syssource)

                cm = []

                if downloads == True:
                    cm.append((downloadMenu, 'RunPlugin(%s?action=download&name=%s&image=%s&source=%s)' % (sysaddon, sysname, sysimage, syssource)))

                item = control.item(label=label)
                item.addContextMenuItems(cm)

                if listMeta == 'true':
                    item.setArt({'thumb': thumb, 'icon': thumb, 'poster': poster, 'fanart': fanart})
                    video_streaminfo = {'codec': 'h264'}
                    item.addStreamInfo('video', video_streaminfo)
                    item.setInfo(type='video', infoLabels=control.metadataClean(meta))

                else:
                    item.setArt({'thumb': thumb})
                    item.setInfo(type='video', infoLabels=None)

                control.addItem(handle=syshandle, url=sysurl, listitem=item, isFolder=False)
            except:
                pass

        control.content(syshandle, 'files')
        control.directory(syshandle, cacheToDisc=True)


    def playItem(self, title, source):
        try:
            meta = control.window.getProperty(self.metaProperty)
            meta = json.loads(meta)

            year = meta['year'] if 'year' in meta else None
            season = meta['season'] if 'season' in meta else None
            episode = meta['episode'] if 'episode' in meta else None

            imdb = meta['imdb'] if 'imdb' in meta else None
            tvdb = meta['tvdb'] if 'tvdb' in meta else None

            next = [] ; prev = [] ; total = []

            for i in list(range(1,1000)):
                try:
                    u = control.infoLabel('ListItem(%s).FolderPath' % str(i))
                    if u in total: raise Exception()
                    total.append(u)
                    u = dict(urllib_parse.parse_qsl(u.replace('?','')))
                    u = json.loads(u['source'])[0]
                    next.append(u)
                except:
                    break
            for i in range(-1000,0)[::-1]:
                try:
                    u = control.infoLabel('ListItem(%s).FolderPath' % str(i))
                    if u in total: raise Exception()
                    total.append(u)
                    u = dict(urllib_parse.parse_qsl(u.replace('?','')))
                    u = json.loads(u['source'])[0]
                    prev.append(u)
                except:
                    break

            items = json.loads(source)
            items = [i for i in items+next+prev][:40]

            header = control.addonInfo('name') + ': Resolving...'

            progressDialog = control.progressDialog if control.setting('progress.dialog') == '0' else control.progressDialogBG
            progressDialog.create(header, '')
            #progressDialog.update(0)

            block = None

            for i in list(range(len(items))):
                try:
                    label = re.sub(' {2,}', ' ', str(items[i]['label']))
                    try:
                        if progressDialog.iscanceled(): break
                        progressDialog.update(int((100 / float(len(items))) * i), label)
                    except:
                        progressDialog.update(int((100 / float(len(items))) * i), str(header) + '[CR]' + label)

                    if items[i]['source'] == block: raise Exception()

                    w = workers.Thread(self.sourcesResolve, items[i])
                    w.start()

                    #offset = 60 * 2 if items[i].get('source') in self.hostcapDict else 0

                    if items[i].get('source').lower() in self.hostcapDict:
                        offset = 60 * 2
                    elif 'torrent' in items[i].get('source').lower():
                        offset = float('inf')
                    else:
                        offset = 0

                    m = ''

                    for x in list(range(3600)):
                        try:
                            if control.monitor.abortRequested(): return sys.exit()
                            if progressDialog.iscanceled(): return progressDialog.close()
                        except:
                            pass

                        k = control.condVisibility('Window.IsActive(virtualkeyboard)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30 + offset) and not k: break
                        k = control.condVisibility('Window.IsActive(yesnoDialog)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30 + offset) and not k: break
                        time.sleep(0.5)


                    for x in list(range(30)):
                        try:
                            if control.monitor.abortRequested(): return sys.exit()
                            if progressDialog.iscanceled(): return progressDialog.close()
                        except:
                            pass

                        if m == '': break
                        if w.is_alive() == False: break
                        time.sleep(0.5)


                    if w.is_alive() == True: block = items[i]['source']

                    if self.url == None: raise Exception()

                    try: progressDialog.close()
                    except: pass

                    control.sleep(200)
                    control.execute('Dialog.Close(virtualkeyboard)')
                    control.execute('Dialog.Close(yesnoDialog)')

                    from resources.lib.modules.player import player
                    player().run(title, year, season, episode, imdb, tvdb, self.url, meta)

                    return self.url
                except:
                    pass

            try: progressDialog.close()
            except: pass
            del progressDialog

            self.errorForSources()
        except:
            pass

    def getSources(self, title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, quality='HD', timeout=30):
        progressDialog = control.progressDialog if control.setting('progress.dialog') == '0' else control.progressDialogBG
        if progressDialog == control.progressDialogBG:
            control.idle()

        progressDialog.create(self.module_name)
        #progressDialog.update(0)

        self.prepareSources()

        sourceDict = self.sourceDict

        progressDialog.update(0, six.ensure_str(control.lang(32600)))
        content = 'movie' if tvshowtitle == None else 'episode'
        if content == 'movie':
            sourceDict = [(i[0], i[1], getattr(i[1], 'movie', None)) for i in sourceDict]
            genres = trakt.getGenre('movie', 'imdb', imdb)
        else:
            sourceDict = [(i[0], i[1], getattr(i[1], 'tvshow', None)) for i in sourceDict]
            genres = trakt.getGenre('show', 'tvdb', tvdb)

        sourceDict = [(i[0], i[1], i[2]) for i in sourceDict if not hasattr(i[1], 'genre_filter') or not i[1].genre_filter or any(x in i[1].genre_filter for x in genres)]
        sourceDict = [(i[0], i[1]) for i in sourceDict if not i[2] == None]

        language = self.getLanguage()
        sourceDict = [(i[0], i[1], i[1].language) for i in sourceDict]
        sourceDict = [(i[0], i[1]) for i in sourceDict if any(x in i[2] for x in language)]

        try: sourceDict = [(i[0], i[1], control.setting('provider.' + i[0])) for i in sourceDict]
        except: sourceDict = [(i[0], i[1], 'true') for i in sourceDict]
        sourceDict = [(i[0], i[1]) for i in sourceDict if not i[2] == 'false']

        if control.setting('cf.disable') == 'true':
            sourceDict = [(i[0], i[1]) for i in sourceDict if not any(x in i[0].lower() for x in self.sourcecfDict)]

        sourceDict = [(i[0], i[1], i[1].priority) for i in sourceDict]

        random.shuffle(sourceDict)
        sourceDict = sorted(sourceDict, key=lambda i: i[2])

        threads = []

        if content == 'movie':
            #title = self.getTitle(title)
            title, year = cleantitle.scene_rls(title, year)
            #log_utils.log('movtitle is '+title+' year is '+year)
            localtitle = self.getLocalTitle(title, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtitle, content)
            for i in sourceDict: threads.append(workers.Thread(self.getMovieSource, title, localtitle, aliases, year, imdb, i[0], i[1]))
        else:
            #tvshowtitle = self.getTitle(tvshowtitle)
            tvshowtitle, year, season, episode = cleantitle.scene_tvrls(tvshowtitle, year, season, episode)
            #log_utils.log('tvtitle is '+tvshowtitle+' year is '+year+' season is '+season)
            localtvshowtitle = self.getLocalTitle(tvshowtitle, imdb, tvdb, content)
            aliases = self.getAliasTitles(imdb, localtvshowtitle, content)
            #Disabled on 11/11/17 due to hang. Should be checked in the future and possible enabled again.
            #season, episode = thexem.get_scene_episode_number(tvdb, season, episode)
            for i in sourceDict: threads.append(workers.Thread(self.getEpisodeSource, title, year, imdb, tvdb, season, episode, tvshowtitle, localtvshowtitle, aliases, premiered, i[0], i[1]))

        s = [i[0] + (i[1],) for i in zip(sourceDict, threads)]
        s = [(i[3].getName(), i[0], i[2]) for i in s]

        # mainsourceDict = [i[0] for i in s if i[2] == 0]
        sourcelabelDict = dict([(i[0], i[1].upper()) for i in s])

        [i.start() for i in threads]

        string1 = six.ensure_str(control.lang(32404))
        string2 = six.ensure_str(control.lang(32405))
        string3 = six.ensure_str(control.lang(32406))
        string4 = six.ensure_str(control.lang(32601))
        string5 = six.ensure_str(control.lang(32602))
        string6 = six.ensure_str(control.lang(32606))
        string7 = six.ensure_str(control.lang(32607))

        try: timeout = int(control.setting('scrapers.timeout.1'))
        except: pass

        start_time = time.time()
        end_time = start_time + timeout

        max_quality = control.setting('hosts.quality') or '0'
        max_quality = int(max_quality)
        min_quality = control.setting('min.quality') or '3'
        min_quality = int(min_quality)

        size_filters = control.setting('size.filters') or 'false'
        mov_min_size = control.setting('min.size.mov') or 0
        mov_min_size = float(mov_min_size)
        mov_max_size = control.setting('max.size.mov') or 100
        mov_max_size = float(mov_max_size)
        ep_min_size = control.setting('min.size.ep') or 0
        ep_min_size = float(ep_min_size)
        ep_max_size = control.setting('max.size.ep') or 20
        ep_max_size = float(ep_max_size)

        line1 = line3 = ""
        debrid_only = control.setting('debrid.only')

        pre_emp = control.setting('preemptive.termination')
        pre_emp_limit = int(control.setting('preemptive.limit'))

        source_4k = source_1080 = source_720 = source_sd = total = 0

        total_format = '[COLOR %s][B]%s[/B][/COLOR]'
        pdiag_format = '4K: %s  |  1080P: %s  |  720P: %s  |  SD: %s %s: %s' % ('%s','%s','%s','%s','[CR]TOTAL','%s') if not progressDialog == control.progressDialogBG else \
                       '4K: %s | 1080P: %s | 720P: %s | SD: %s %s: %s' % ('%s','%s','%s','%s','| T','%s')

        # for i in list(range(0, 4 * timeout)):
        for i in list(range(0, 2 * timeout)):

            try:

                if control.monitor.abortRequested(): return sys.exit()
                try:
                    if progressDialog.iscanceled(): break
                except:
                    pass

                if pre_emp == 'true':
                    if size_filters == 'true':
                        if content == 'movie':
                            if max_quality == 0:
                                if len([e for e in self.sources if e['quality'] in ['4k', '4K'] and (mov_min_size <= e.get('size') <= mov_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 1:
                                if len([e for e in self.sources if e['quality'] in ['1080p', '1080P'] and (mov_min_size <= e.get('size') <= mov_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 2:
                                if len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD'] and (mov_min_size <= e.get('size') <= mov_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 3:
                                if len([e for e in self.sources if e['quality'] in ['sd', 'SD'] and (mov_min_size <= e.get('size') <= mov_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                        elif content == 'episode':
                            if max_quality == 0:
                                if len([e for e in self.sources if e['quality'] in ['4k', '4K'] and (ep_min_size <= e.get('size') <= ep_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 1:
                                if len([e for e in self.sources if e['quality'] in ['1080p', '1080P'] and (ep_min_size <= e.get('size') <= ep_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 2:
                                if len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD'] and (ep_min_size <= e.get('size') <= ep_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break
                            elif max_quality == 3:
                                if len([e for e in self.sources if e['quality'] in ['sd', 'SD'] and (ep_min_size <= e.get('size') <= ep_max_size or e.get('size', 0.0) == 0.0)]) >= pre_emp_limit:
                                    break

                    else:
                        if max_quality == 0:
                            if source_4k >= pre_emp_limit: break
                        elif max_quality == 1:
                            if source_1080 >= pre_emp_limit: break
                        elif max_quality == 2:
                            if source_720 >= pre_emp_limit: break
                        elif max_quality == 3:
                            if source_sd >= pre_emp_limit: break

                if len(self.sources) > 0:
                    if min_quality == 0:
                        source_4k = len([e for e in self.sources if e['quality'] in ['4k', '4K']])
                    elif min_quality == 1:
                        source_1080 = len([e for e in self.sources if e['quality'] in ['1080p', '1080P']])
                        if max_quality == 0:
                            source_4k = len([e for e in self.sources if e['quality'] in ['4k', '4K']])
                    elif min_quality == 2:
                        source_720 = len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD']])
                        if max_quality == 0:
                            source_4k = len([e for e in self.sources if e['quality'] in ['4k', '4K']])
                            source_1080 = len([e for e in self.sources if e['quality'] in ['1080p', '1080P']])
                        elif max_quality == 1:
                            source_1080 = len([e for e in self.sources if e['quality'] in ['1080p', '1080P']])
                    elif min_quality == 3:
                        source_sd = len([e for e in self.sources if e['quality'] in ['sd', 'scr', 'cam', 'SD', 'SCR', 'CAM']])
                        if max_quality == 0:
                            source_4k = len([e for e in self.sources if e['quality'] in ['4k', '4K']])
                            source_1080 = len([e for e in self.sources if e['quality'] in ['1080p', '1080P']])
                            source_720 = len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD']])
                        elif max_quality == 1:
                            source_1080 = len([e for e in self.sources if e['quality'] in ['1080p', '1080P']])
                            source_720 = len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD']])
                        elif max_quality == 2:
                            source_720 = len([e for e in self.sources if e['quality'] in ['720p', 'hd', '720P', 'HD']])

                    total = source_4k + source_1080 + source_720 + source_sd

                source_4k_label = total_format % ('red', source_4k) if source_4k == 0 else total_format % ('lime', source_4k)
                source_1080_label = total_format % ('red', source_1080) if source_1080 == 0 else total_format % ('lime', source_1080)
                source_720_label = total_format % ('red', source_720) if source_720 == 0 else total_format % ('lime', source_720)
                source_sd_label = total_format % ('red', source_sd) if source_sd == 0 else total_format % ('lime', source_sd)
                source_total_label = total_format % ('red', total) if total == 0 else total_format % ('lime', total)

                # if (i / 2) < timeout:
                try:
                    # mainleft = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True and x.getName() in mainsourceDict]
                    info = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True]
                    # if i >= timeout and len(mainleft) == 0 and len(self.sources) >= 100 * len(info): break # improve responsiveness
                    line1 = pdiag_format % (source_4k_label, source_1080_label, source_720_label, source_sd_label, source_total_label)
                    if len(info) > 6: line3 = string3 % (str(len(info)))
                    elif len(info) > 0: line3 = string3 % (', '.join(info).replace('[COLOR %s]' % (control.setting('orion.color').upper()), '').replace('[/COLOR]', ''))
                    else: break
                    # percent = int(100 * float(i) / (2 * timeout) + 0.5)
                    current_time = time.time()
                    current_progress = current_time - start_time
                    percent = int((current_progress / float(timeout)) * 100)
                    if not progressDialog == control.progressDialogBG: progressDialog.update(max(1, percent), line1 + '[CR]' + line3)
                    else: progressDialog.update(max(1, percent), self.module_name, line1 + '[CR]' + line3)
                    # if len(mainleft) == 0: break
                    if end_time < current_time: break
                except Exception as e:
                    log_utils.log('Source fetching dialog exception : %s' % str(e), log_utils.LOGERROR)
                    break
                # else: # old implementation that makes "priority: 0" scrapers to ignore the timeout setting
                    # try:
                        # mainleft = [sourcelabelDict[x.getName()] for x in threads if x.is_alive() == True and x.getName() in mainsourceDict]
                        # info = mainleft
                        # if len(info) > 6: line3 = 'Waiting for: %s' % (str(len(info)))
                        # elif len(info) > 0: line3 = 'Waiting for: %s' % (', '.join(info))
                        # else: break
                        # percent = int(100 * float(i) / (2 * timeout) + 0.5) % 100
                        # if not progressDialog == control.progressDialogBG: progressDialog.update(max(1, percent), line1 + '[CR]' + line3)
                        # else: progressDialog.update(max(1, percent), line1 + '[CR]' + line3)
                    # except Exception as e:
                        # log_utils.log('Exception Raised: %s' % str(e), log_utils.LOGERROR)
                        # break

                control.sleep(500)
            except:
                failure = traceback.format_exc()
                log_utils.log('sourcefail: ' + str(failure))
                pass

        try: progressDialog.close()
        except: pass
        del progressDialog

        self.sourcesFilter(content)

        return self.sources

    def prepareSources(self):
        try:
            control.makeFile(control.dataPath)

            dbcon = database.connect(self.sourceFile)
            dbcur = dbcon.cursor()
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_url (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""rel_url TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
            dbcur.execute("CREATE TABLE IF NOT EXISTS rel_src (""source TEXT, ""imdb_id TEXT, ""season TEXT, ""episode TEXT, ""hosts TEXT, ""added TEXT, ""UNIQUE(source, imdb_id, season, episode)"");")
        except:
            pass


    def getMovieSource(self, title, localtitle, aliases, year, imdb, source, call):

        try:
            dbcon = database.connect(self.sourceFile)
            dbcur = dbcon.cursor()
        except:
            pass

        ''' Fix to stop items passed with a 0 IMDB id pulling old unrelated sources from the database. '''
        if imdb == '0':
            try:
                dbcur.execute("DELETE FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
                dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
                dbcon.commit()
            except:
                pass
        ''' END '''

        try:
            sources = []
            dbcur.execute("SELECT * FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            match = dbcur.fetchone()
            t1 = int(re.sub('[^0-9]', '', str(match[5])))
            t2 = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
            update = abs(t2 - t1) > 60
            if update == False:
                sources = eval(six.ensure_str(match[4]))
                return self.sources.extend(sources)
        except:
            pass

        try:
            url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            url = dbcur.fetchone()
            url = eval(six.ensure_str(url[4]))
        except:
            pass

        try:
            if url == None: url = call.movie(imdb, title, localtitle, aliases, year)
            if url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, '', '', repr(url)))
            dbcon.commit()
        except:
            pass

        try:
            sources = []
            sources = call.sources(url, self.hostDict, self.hostprDict)
            if sources == None or sources == []: raise Exception()
            sources = [json.loads(t) for t in set(json.dumps(d, sort_keys=True) for d in sources)]
            for i in sources: i.update({'provider': source})
            self.sources.extend(sources)
            dbcur.execute("DELETE FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_src Values (?, ?, ?, ?, ?, ?)", (source, imdb, '', '', repr(sources), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            dbcon.commit()
        except:
            pass


    def getEpisodeSource(self, title, year, imdb, tvdb, season, episode, tvshowtitle, localtvshowtitle, aliases, premiered, source, call):
        try:
            dbcon = database.connect(self.sourceFile)
            dbcur = dbcon.cursor()
        except:
            pass

        try:
            sources = []
            dbcur.execute("SELECT * FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            match = dbcur.fetchone()
            t1 = int(re.sub('[^0-9]', '', str(match[5])))
            t2 = int(datetime.datetime.now().strftime("%Y%m%d%H%M"))
            update = abs(t2 - t1) > 60
            if update == False:
                sources = eval(six.ensure_str(match[4]))
                return self.sources.extend(sources)
        except:
            pass

        try:
            url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            url = dbcur.fetchone()
            url = eval(six.ensure_str(url[4]))
        except:
            pass

        try:
            if url == None: url = call.tvshow(imdb, tvdb, tvshowtitle, localtvshowtitle, aliases, year)
            if url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, '', ''))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, '', '', repr(url)))
            dbcon.commit()
        except:
            pass

        try:
            ep_url = None
            dbcur.execute("SELECT * FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            ep_url = dbcur.fetchone()
            ep_url = eval(six.ensure_str(ep_url[4]))
        except:
            pass

        try:
            if url == None: raise Exception()
            if ep_url == None: ep_url = call.episode(url, imdb, tvdb, title, premiered, season, episode)
            if ep_url == None: raise Exception()
            dbcur.execute("DELETE FROM rel_url WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            dbcur.execute("INSERT INTO rel_url Values (?, ?, ?, ?, ?)", (source, imdb, season, episode, repr(ep_url)))
            dbcon.commit()
        except:
            pass

        try:
            sources = []
            sources = call.sources(ep_url, self.hostDict, self.hostprDict)
            if sources == None or sources == []: raise Exception()
            sources = [json.loads(t) for t in set(json.dumps(d, sort_keys=True) for d in sources)]
            for i in sources: i.update({'provider': source})
            self.sources.extend(sources)
            dbcur.execute("DELETE FROM rel_src WHERE source = '%s' AND imdb_id = '%s' AND season = '%s' AND episode = '%s'" % (source, imdb, season, episode))
            dbcur.execute("INSERT INTO rel_src Values (?, ?, ?, ?, ?, ?)", (source, imdb, season, episode, repr(sources), datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
            dbcon.commit()
        except:
            pass


    def alterSources(self, url, meta):

        try:
            if control.setting('hosts.mode') == '2': url += '&select=1'
            else: url += '&select=2'
            control.execute('RunPlugin(%s)' % url)
        except:
            pass


    def clearSources(self):
        try:
            control.idle()

            yes = control.yesnoDialog(six.ensure_str(control.lang(32407)))
            if not yes: return

            control.makeFile(control.dataPath)
            dbcon = database.connect(control.providercacheFile)
            dbcur = dbcon.cursor()
            dbcur.execute("DROP TABLE IF EXISTS rel_src")
            dbcur.execute("DROP TABLE IF EXISTS rel_url")
            dbcur.execute("VACUUM")
            dbcon.commit()

            control.infoDialog(six.ensure_str(control.lang(32408)), sound=True, icon='INFO')
        except:
            pass


    def uniqueSourcesGen(self, sources):
        uniqueURLs = set()
        for source in sources:
            url = source.get('url')
            if isinstance(url, six.string_types):
                if 'magnet:' in url:
                    url = url[:60]
                    #url = re.findall(u'btih:(\w{40})', url)[0]
                if url not in uniqueURLs:
                    uniqueURLs.add(url)
                    yield source # Yield the unique source.
                else:
                    pass # Ignore duped sources.
            else:
                yield source # Always yield non-string url sources.


    def sourcesProcessTorrents(self, torrent_sources):#adjusted Exodus code
        if len(torrent_sources) == 0: return
        for i in torrent_sources:
            if not i.get('debrid', '') in ['Real-Debrid', 'AllDebrid', 'Premiumize.me', 'Debrid-Link.fr']:
                return torrent_sources
        start_time = time.time()
        timeout = 20
        try:
            while time.time() < start_time + timeout:
                from resources.lib.modules import debridcheck
                control.sleep(500)
                DBCheck = debridcheck.DebridCheck()
                hashList = []
                cachedTorrents = []
                uncachedTorrents = []
                #uncheckedTorrents = []
                for i in torrent_sources:
                    try:
                        r = re.findall(r'btih:(\w{40})', str(i['url']))[0]
                        if r:
                            infoHash = r.lower()
                            i['info_hash'] = infoHash
                            hashList.append(infoHash)
                    except: torrent_sources.remove(i)
                if len(torrent_sources) == 0: return torrent_sources
                torrent_sources = [i for i in torrent_sources if 'info_hash' in i]
                hashList = list(set(hashList))
                control.sleep(500)
                cachedRDHashes, cachedADHashes, cachedPMHashes, cachedDLHashes = DBCheck.run(hashList)
                #cached
                cachedRDSources = [dict(i.items()) for i in torrent_sources if (any(v in i.get('info_hash') for v in cachedRDHashes) and i.get('debrid', '') == 'Real-Debrid')]
                cachedTorrents += cachedRDSources
                cachedADSources = [dict(i.items()) for i in torrent_sources if (any(v in i.get('info_hash') for v in cachedADHashes) and i.get('debrid', '') == 'AllDebrid')]
                cachedTorrents += cachedADSources
                cachedPMSources = [dict(i.items()) for i in torrent_sources if (any(v in i.get('info_hash') for v in cachedPMHashes) and i.get('debrid', '') == 'Premiumize.me')]
                cachedTorrents += cachedPMSources
                cachedDLSources = [dict(i.items()) for i in torrent_sources if (any(v in i.get('info_hash') for v in cachedDLHashes) and i.get('debrid', '') == 'Debrid-Link.fr')]
                cachedTorrents += cachedDLSources
                for i in cachedTorrents: i.update({'source': 'cached torrent'})
                #uncached
                uncachedRDSources = [dict(i.items()) for i in torrent_sources if (not any(v in i.get('info_hash') for v in cachedRDHashes) and i.get('debrid', '') == 'Real-Debrid')]
                uncachedTorrents += uncachedRDSources
                uncachedADSources = [dict(i.items()) for i in torrent_sources if (not any(v in i.get('info_hash') for v in cachedADHashes) and i.get('debrid', '') == 'AllDebrid')]
                uncachedTorrents += uncachedADSources
                uncachedPMSources = [dict(i.items()) for i in torrent_sources if (not any(v in i.get('info_hash') for v in cachedPMHashes) and i.get('debrid', '') == 'Premiumize.me')]
                uncachedTorrents += uncachedPMSources
                uncachedDLSources = [dict(i.items()) for i in torrent_sources if (not any(v in i.get('info_hash') for v in cachedDLHashes) and i.get('debrid', '') == 'Debrid-Link.fr')]
                uncachedTorrents += uncachedDLSources
                for i in uncachedTorrents: i.update({'source': '[COLOR dimgrey]uncached torrent[/COLOR]'})
                #uncheckedTorrents += [dict(i.items()) for i in torrent_sources if i.get('source').lower() == 'torrent']
                time.sleep(0.1)
                return cachedTorrents + uncachedTorrents# + uncheckedTorrents
            else:
                return
        except:
            failure = traceback.format_exc()
            log_utils.log('Torrent check - Exception: ' + str(failure))
            control.infoDialog('Error Processing Torrents')
            return


    def sourcesFilter(self, _content):

        max_quality = control.setting('hosts.quality') or '0'
        max_quality = int(max_quality)
        min_quality = control.setting('min.quality') or '3'
        min_quality = int(min_quality)
        remove_cam = control.setting('remove.cam') or 'false'

        size_filters = control.setting('size.filters') or 'false'
        mov_min_size = control.setting('min.size.mov') or 0
        mov_min_size = float(mov_min_size)
        mov_max_size = control.setting('max.size.mov') or 100
        mov_max_size = float(mov_max_size)
        ep_min_size = control.setting('min.size.ep') or 0
        ep_min_size = float(ep_min_size)
        ep_max_size = control.setting('max.size.ep') or 20
        ep_max_size = float(ep_max_size)

        debrid_only = control.setting('debrid.only') or 'false'

        remove_captcha = control.setting('remove.captcha') or 'false'

        remove_hevc = control.setting('remove.hevc') or 'false'

        sort_provider = control.setting('hosts.sort.provider') or 'true'

        size_sort = control.setting('torr.sort.size') or 'true'

        remove_dups = control.setting('remove.dups') or 'true'

        check_torr_cache = control.setting('check.torr.cache') or 'true'

        remove_uncached = control.setting('remove.uncached') or 'false'

        random.shuffle(self.sources)

        local = [i for i in self.sources if 'local' in i and i['local'] == True]
        for i in local: i.update({'language': self._getPrimaryLang() or 'en'})
        self.sources = [i for i in self.sources if not i in local]

        multi = [i['language'] for i in self.sources]
        multi = [x for y,x in enumerate(multi) if x not in multi[:y]]
        multi = True if len(multi) > 1 else False

        for i in list(range(len(self.sources))):
            if self.sources[i]['quality'] in ['hd', 'HD']:
                self.sources[i].update({'quality': '720p'})

        if sort_provider == 'true':
            self.sources = sorted(self.sources, key=lambda k: k['provider'])

        if size_sort == 'true':
            self.sources = sorted(self.sources, key=lambda k: k.get('size', 0.0), reverse=True)

        if remove_hevc == 'true':
            self.sources = [i for i in self.sources if not any(value in i['url'] for value in ['hevc', 'h265', 'h.265', 'x265', 'x.265', 'HEVC', 'H265', 'H.265', 'X265', 'X.265'])]

        if remove_captcha == 'true':
            self.sources = [i for i in self.sources if not (i['source'].lower() in self.hostcapDict and not 'debrid' in i)]

        self.sources = [i for i in self.sources if not i['source'].lower() in self.hostblockDict]

        # for i in self.sources:
            # if 'checkquality' in i and i['checkquality'] == True:
                # if not i['source'].lower() in self.hosthqDict and i['quality'] not in ['SD', 'SCR', 'CAM']: i.update({'quality': 'SD'})

        if size_filters == 'true':
            if _content == 'movie':
                self.sources = [i for i in self.sources if (mov_min_size <= i.get('size') <= mov_max_size) or i.get('size', 0.0) == 0.0]
            elif _content == 'episode':
                self.sources = [i for i in self.sources if (ep_min_size <= i.get('size') <= ep_max_size) or i.get('size', 0.0) == 0.0]

        try:
            if remove_dups == 'true' and len(self.sources) > 1:
                stotal = len(self.sources)
                self.sources = list(self.uniqueSourcesGen(self.sources))
                dupes = str(stotal - len(self.sources))
                control.infoDialog(six.ensure_str(control.lang(32089)).format(dupes), icon='INFO', time=2000)
        except:
            failure = traceback.format_exc()
            log_utils.log('DUP - Exception: ' + str(failure))
            control.infoDialog('Dupes filter failed', icon='INFO', sound=True)

        filter = []

        for d in debrid.debrid_resolvers:
            valid_hoster = set([i['source'] for i in self.sources])
            valid_hoster = [i for i in valid_hoster if d.valid_url('', i)]

            if check_torr_cache == 'true':
                try:
                    for i in self.sources:
                        if 'magnet:' in i['url']:
                            i.update({'debrid': d.name})
                    torrentSources = self.sourcesProcessTorrents([i for i in self.sources if 'magnet:' in i['url']])
                    cached = [i for i in torrentSources if i.get('source') == 'cached torrent']
                    filter += cached
                    unchecked = [i for i in torrentSources if i.get('source').lower() == 'torrent']
                    filter += unchecked
                    if remove_uncached == 'false' or len(cached) == 0:
                        uncached = [i for i in torrentSources if i.get('source') == '[COLOR dimgrey]uncached torrent[/COLOR]']
                        filter += uncached
                    filter += [dict(list(i.items()) + [('debrid', d.name)]) for i in self.sources if i['source'] in valid_hoster and 'magnet:' not in i['url']]
                except:
                    filter += [dict(list(i.items()) + [('debrid', d.name)]) for i in self.sources if i.get('source').lower() == 'torrent']
                    filter += [dict(list(i.items()) + [('debrid', d.name)]) for i in self.sources if i['source'] in valid_hoster and 'magnet:' not in i['url']]

            else:
                filter += [dict(list(i.items()) + [('debrid', d.name)]) for i in self.sources if i.get('source').lower() == 'torrent']
                filter += [dict(list(i.items()) + [('debrid', d.name)]) for i in self.sources if i['source'] in valid_hoster and 'magnet:' not in i['url']]

        if debrid_only == 'false' or debrid.status() == False:
            filter += [i for i in self.sources if not i['source'].lower() in self.hostprDict and i['debridonly'] == False]

        self.sources = filter

        filter = []
        filter += local

        if max_quality == 0:
            filter += [i for i in self.sources if i['quality'] in ['4K', '4k']]
        if max_quality <= 1 and min_quality >= 1:
            filter += [i for i in self.sources if i['quality'] in ['1080p', '1080P']]
        if max_quality <= 2 and min_quality >= 2:
            filter += [i for i in self.sources if i['quality'] in ['720p', '720P']]
        if max_quality <= 3 and min_quality >= 3:
            filter += [i for i in self.sources if i['quality'] in ['sd', 'SD']]
            if remove_cam == 'false':
                filter += [i for i in self.sources if i['quality'] in ['scr', 'cam', 'SCR', 'CAM']]
        self.sources = filter

        if multi == True:
            self.sources = [i for i in self.sources if not i['language'] == 'en'] + [i for i in self.sources if i['language'] == 'en']

        self.sources = self.sources[:4000]

        control.idle()

        prem_color = control.setting('prem.identify')
        prem_identify = self.getPremColor(prem_color)
        if prem_identify == '': prem_identify = 'gold'

        sec_color = control.setting('sec.identify')
        sec_identify = self.getPremColor(sec_color)
        if sec_identify == '': sec_identify = 'cyan'

        double_line = control.setting('linesplit') == '1'
        simple = control.setting('linesplit') == '2'
        single_line = control.setting('linesplit') == '0'

        name_setting = control.setting('sources.name') == '0'

        for i in list(range(len(self.sources))):

            try: d = self.sources[i]['debrid']
            except: d = self.sources[i]['debrid'] = ''

            t = source_utils.getFileType(self.sources[i]['url'])

            u = self.sources[i]['url']

            p = self.sources[i]['provider']

            q = self.sources[i]['quality']

            s = self.sources[i]['source']

            s = s.rsplit('.', 1)[0]

            l = self.sources[i]['language']

            try:
                f = (' / '.join(['%s' % info.strip() for info in self.sources[i]['info'].split('|')]))
                if name_setting:
                    if 'name' in self.sources[i] and not self.sources[i]['name'] == '':
                        size_info = self.sources[i]['info'].split(' |')[0]
                        if size_info.rstrip().lower().endswith('gb'):
                            f = size_info + ' / ' + cleantitle.get_title(self.sources[i]['name'])
                        else:
                            f = cleantitle.get_title(self.sources[i]['name'])
                        t = ''
            except:
                f = ''


            if d.lower() == 'alldebrid': d = 'AD'
            if d.lower() == 'debrid-link.fr': d = 'DL.FR'
            if d.lower() == 'linksnappy': d = 'LS'
            if d.lower() == 'megadebrid': d = 'MD'
            if d.lower() == 'premiumize.me': d = 'PM'
            if d.lower() == 'real-debrid': d = 'RD'
            if d.lower() == 'zevera': d = 'ZVR'


            if double_line:
                if not d == '':
                    label = '[COLOR %s]%03d' % (prem_identify, int(i+1))
                    if multi == True and not l == 'en': label += ' | [B]%s[/B]' % l
                    label += ' | %s | [B]%s[/B] | %s | [B]%s[/B][/COLOR][CR]    [COLOR %s][I]%s /%s[/I][/COLOR]' % (d, q, p, s, sec_identify, f, t)

                else:
                    label = '%03d' % int(i+1)
                    if multi == True and not l == 'en': label += ' | [B]%s[/B]' % l
                    label += ' | [B]%s[/B] | %s | [B]%s[/B][CR]    [COLOR %s][I]%s /%s[/I][/COLOR]' % (q, p, s, sec_identify, f, t)

            elif simple:
                label = '%03d' % int(i+1)
                if multi == True and not l == 'en': label += ' | [B]%s[/B]' % l
                label += ' | %s | [B]%s[/B] | %s | [B]%s[/B]' % (d, q, p, s)

            else:
                if not d == '':
                    label = '[COLOR %s]%03d' % (prem_identify, int(i+1))
                    if multi == True and not l == 'en': label += ' | [B]%s[/B]' % l
                    label += ' | %s | [B]%s[/B] | %s | [B]%s[/B] | [/COLOR][COLOR %s][I]%s /%s[/I][/COLOR]' % (d, q, p, s, sec_identify, f, t)

                else:
                    label = '%03d' % int(i+1)
                    if multi == True and not l == 'en': label += ' | [B]%s[/B]' % l
                    label += ' | [B]%s[/B] | %s | [B]%s[/B] | [COLOR %s][I]%s /%s[/I][/COLOR]' % (q, p, s, sec_identify, f, t)

            label = label.replace(' |  |', ' |').replace('| 0 |', '|').replace('[I] /[/I]', '').replace('[I] /%s[/I]' % t, '[I]%s[/I]' % t).replace('[I]%s /[/I]' % f, '[I]%s[/I]' % f)

            # nasty
            if double_line:
                label_up = label.split('[CR]')[0]
                label_up_clean = label_up.replace('[COLOR %s]' % prem_identify, '').replace('[/COLOR]', '').replace('[B]', '').replace('[/B]', '')
                label_down = label.split('[CR]')[1]
                label_down_clean = label_down.replace('[COLOR %s]' % sec_identify, '').replace('[/COLOR]', '').replace('[I]', '').replace('[/I]', '')
                if len(label_down_clean) > len(label_up_clean):
                    label_up += (len(label_down_clean) - len(label_up_clean)) * '  '
                    label = label_up + '[CR]' + label_down

            self.sources[i]['label'] = '[UPPERCASE]' + label + '[/UPPERCASE]'

        self.sources = [i for i in self.sources if 'label' in i]

        return self.sources


    def sourcesResolve(self, item, info=False):
        try:
            self.url = None

            u = url = item['url']

            d = item['debrid'] ; direct = item['direct']
            local = item.get('local', False)

            provider = item['provider']
            call = [i[1] for i in self.sourceDict if i[0] == provider][0]
            u = url = call.resolve(url)

            if url == None or (not '://' in url and not local and 'magnet:' not in url): raise Exception()

            if not local:
                url = url[8:] if url.startswith('stack:') else url

                urls = []
                for part in url.split(' , '):
                    u = part
                    if not d == '':
                        part = debrid.resolver(part, d)

                    elif not direct == True:
                        hmf = urlresolver.HostedMediaFile(url=u, include_disabled=True, include_universal=False)
                        if hmf.valid_url() == True: part = hmf.resolve()
                    urls.append(part)

                url = 'stack://' + ' , '.join(urls) if len(urls) > 1 else urls[0]

            if url == False or url == None: raise Exception()

            ext = url.split('?')[0].split('&')[0].split('|')[0].rsplit('.')[-1].replace('/', '').lower()
            if ext == 'rar': raise Exception()

            try: headers = url.rsplit('|', 1)[1]
            except: headers = ''
            headers = urllib_parse.quote_plus(headers).replace('%3D', '=') if ' ' in headers else headers
            headers = dict(urllib_parse.parse_qsl(headers))


            if url.startswith('http') and '.m3u8' in url:
                try: result = client.request(url.split('|')[0], headers=headers, output='geturl', timeout='20')
                except: pass
                #if result == None: raise Exception()

            elif url.startswith('http'):
                try: result = client.request(url.split('|')[0], headers=headers, output='chunk', timeout='20')
                except: pass
                #if result == None: raise Exception()


            self.url = url
            return url
        except:
            if info == True: self.errorForSources()
            return


    def sourcesDialog(self, items):
        try:

            labels = [i['label'] for i in items]

            select = control.selectDialog(labels)
            if select == -1: return 'close://'

            next = [y for x,y in enumerate(items) if x >= select]
            prev = [y for x,y in enumerate(items) if x < select][::-1]

            items = [items[select]]
            items = [i for i in items+next+prev][:40]

            header = control.addonInfo('name') + ': Resolving...'

            progressDialog = control.progressDialog if control.setting('progress.dialog') == '0' else control.progressDialogBG
            progressDialog.create(header, '')
            #progressDialog.update(0)

            block = None

            for i in list(range(len(items))):
                try:
                    if items[i]['source'] == block: raise Exception()

                    w = workers.Thread(self.sourcesResolve, items[i])
                    w.start()

                    label = re.sub(' {2,}', ' ', str(items[i]['label']))

                    try:
                        if progressDialog.iscanceled(): break
                        progressDialog.update(int((100 / float(len(items))) * i), label)
                    except:
                        progressDialog.update(int((100 / float(len(items))) * i), str(header) + '[CR]' + label)

                    if items[i].get('source').lower() in self.hostcapDict:
                        offset = 60 * 2
                    elif 'torrent' in items[i].get('source').lower():
                        offset = float('inf')
                    else:
                        offset = 0

                    m = ''

                    for x in list(range(3600)):
                        try:
                            if control.monitor.abortRequested(): return sys.exit()
                            if progressDialog.iscanceled(): return progressDialog.close()
                        except:
                            pass

                        k = control.condVisibility('Window.IsActive(virtualkeyboard)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30 + offset) and not k: break
                        k = control.condVisibility('Window.IsActive(yesnoDialog)')
                        if k: m += '1'; m = m[-1]
                        if (w.is_alive() == False or x > 30 + offset) and not k: break
                        time.sleep(0.5)


                    for x in list(range(30)):
                        try:
                            if control.monitor.abortRequested(): return sys.exit()
                            if progressDialog.iscanceled(): return progressDialog.close()
                        except:
                            pass

                        if m == '': break
                        if w.is_alive() == False: break
                        time.sleep(0.5)


                    if w.is_alive() == True: block = items[i]['source']

                    if self.url == None: raise Exception()

                    self.selectedSource = items[i]['label']

                    try: progressDialog.close()
                    except: pass

                    control.execute('Dialog.Close(virtualkeyboard)')
                    control.execute('Dialog.Close(yesnoDialog)')
                    return self.url
                except:
                    pass

            try: progressDialog.close()
            except: pass
            del progressDialog

        except Exception as e:
            try: progressDialog.close()
            except: pass
            del progressDialog
            log_utils.log('Error %s' % str(e), log_utils.LOGNOTICE)


    def sourcesDirect(self, items):
        filter = [i for i in items if i['source'].lower() in self.hostcapDict and i['debrid'] == '']
        items = [i for i in items if not i in filter]

        filter = [i for i in items if i['source'].lower() in self.hostblockDict]# and i['debrid'] == '']
        items = [i for i in items if not i in filter]

        items = [i for i in items if ('autoplay' in i and i['autoplay'] == True) or not 'autoplay' in i]

        if control.setting('autoplay.sd') == 'true':
            items = [i for i in items if not i['quality'] in ['4k', '1080p', '720p', 'hd', '4K', '1080P', '720P', 'HD']]

        u = None

        header = control.addonInfo('name') + ': Resolving...'

        try:
            control.sleep(1000)

            progressDialog = control.progressDialog if control.setting('progress.dialog') == '0' else control.progressDialogBG
            progressDialog.create(header, '')
            #progressDialog.update(0)
        except:
            pass

        for i in list(range(len(items))):
            label = re.sub(' {2,}', ' ', str(items[i]['label']))
            try:
                if progressDialog.iscanceled(): break
                progressDialog.update(int((100 / float(len(items))) * i), label)
            except:
                progressDialog.update(int((100 / float(len(items))) * i), str(header) + '[CR]' + label)

            try:
                if control.monitor.abortRequested(): return sys.exit()

                url = self.sourcesResolve(items[i])
                if u == None: u = url
                if not url == None: break
            except:
                pass

        try: progressDialog.close()
        except: pass
        del progressDialog

        return u

    def errorForSources(self):
        control.infoDialog(six.ensure_str(control.lang(32401)), sound=False, icon='INFO')


    def getLanguage(self):
        langDict = {'English': ['en'], 'French': ['fr'], 'French+English': ['fr', 'en'], 'German': ['de'], 'German+English': ['de','en'], 'Greek': ['gr'], 'Greek+English': ['gr', 'en'], 'Italian': ['it'], 'Italian+English': ['it', 'en'], 'Korean': ['ko'], 'Korean+English': ['ko', 'en'], 'Polish': ['pl'], 'Polish+English': ['pl', 'en'], 'Portuguese': ['pt'], 'Portuguese+English': ['pt', 'en'], 'Russian': ['ru'], 'Russian+English': ['ru', 'en'], 'Spanish': ['es'], 'Spanish+English': ['es', 'en']}
        name = control.setting('providers.lang')
        return langDict.get(name, ['en'])


    def getLocalTitle(self, title, imdb, tvdb, content):
        lang = self._getPrimaryLang()
        if not lang:
            return title

        if content == 'movie':
            t = trakt.getMovieTranslation(imdb, lang)
        else:
            t = tvmaze.tvMaze().getTVShowTranslation(tvdb, lang)

        return t or title


    def getAliasTitles(self, imdb, localtitle, content):
        lang = self._getPrimaryLang()

        try:
            t = trakt.getMovieAliases(imdb) if content == 'movie' else trakt.getTVShowAliases(imdb)
            t = [i for i in t if i.get('country', '').lower() in [lang, '', 'us'] and i.get('title', '').lower() != localtitle.lower()]
            return t
        except:
            return []

    def _getPrimaryLang(self):
        langDict = {'English': 'en', 'German': 'de', 'German+English': 'de', 'French': 'fr', 'French+English': 'fr', 'Portuguese': 'pt', 'Portuguese+English': 'pt', 'Polish': 'pl', 'Polish+English': 'pl', 'Korean': 'ko', 'Korean+English': 'ko', 'Russian': 'ru', 'Russian+English': 'ru', 'Spanish': 'es', 'Spanish+English': 'es', 'Italian': 'it', 'Italian+English': 'it', 'Greek': 'gr', 'Greek+English': 'gr'}
        name = control.setting('providers.lang')
        lang = langDict.get(name)
        return lang

    def getTitle(self, title):
        title = cleantitle.normalize(title)
        return title

    def getConstants(self):
        self.itemProperty = 'plugin.video.exodus.container.items'

        self.metaProperty = 'plugin.video.exodus.container.meta'

        self.sourceFile = control.providercacheFile

        if control.condVisibility('System.HasAddon(script.module.exoscrapers)'):
            scraperSetting = control.setting('module.provider')
        else:
            scraperSetting = control.setting('module.provider.alt')

        oas_module_name = 'PlayScrapers (' + str(control.addon('script.module.playscrapers').getSetting('package.folder')) + ' set):' \
                          if control.addon('script.module.playscrapers').getSetting('package.folder') != 'Playscrapers' else 'PlayScrapers:'

        import playscrapers
        sourceDir1 = playscrapers.sources()
        from resources.lib import sources
        sourceDir2 = sources.sources()
        try:
            import openscrapers
            sourceDir3 = openscrapers.sources()
        except:
            pass

        try:
            if scraperSetting == 'Play Scrapers':
                self.sourceDict = sourceDir1
                self.module_name = oas_module_name
            elif scraperSetting == 'Play Scrapers':
                self.sourceDict = sourceDir3
                self.module_name = 'ExoScrapers:'
            elif scraperSetting == 'Built-in':
                self.sourceDict = sourceDir2
                self.module_name = 'Built-in providers:'
            elif scraperSetting == 'Play + Built-in':
                self.sourceDict = sourceDir1 + sourceDir2
                self.module_name = 'Built-in + ' + oas_module_name
            elif scraperSetting == 'Exo + Built-in':
                self.sourceDict = sourceDir3 + sourceDir2
                self.module_name = 'Built-in + ExoScrapers:'
            else:
                self.sourceDict = sourceDir1
                self.module_name = oas_module_name
                control.setSetting('module.provider', 'Play Scrapers')
        except:
            return

        try:
            self.hostDict = urlresolver.relevant_resolvers(order_matters=True)
            self.hostDict = [i.domains for i in self.hostDict if not '*' in i.domains]
            self.hostDict = [i.lower() for i in reduce(lambda x, y: x+y, self.hostDict)]
            self.hostDict = [x for y,x in enumerate(self.hostDict) if x not in self.hostDict[:y]]
        except:
            self.hostDict = []

        self.hostprDict = ['1fichier.com', 'dailyuploads.net', 'ddl.to', 'ddownload.com', 'dropapk.to', 'earn4files.com', 'filefactory.com', 'hexupload.net', 'mega.nz', 'multiup.org', 'nitroflare.com', 'oboom.com',
                           'rapidgator.net', 'rg.to', 'rockfile.co', 'rockfile.eu', 'speed-down.org', 'turbobit.net', 'ul.to', 'uploaded.net', 'uploaded.to', 'uploadgig.com', 'uploadrocket.net', 'usersdrive.com']

        self.hostcapDict = ['openload.io', 'openload.co', 'oload.tv', 'oload.stream', 'oload.win', 'oload.download', 'oload.info', 'oload.icu', 'oload.fun', 'oload.life', 'openload.pw',
                            'vev.io', 'vidup.me', 'vidup.tv', 'vidup.io', 'vshare.io', 'vshare.eu', 'flashx.tv', 'flashx.to', 'flashx.sx', 'flashx.bz', 'flashx.cc',
                            'hugefiles.net', 'hugefiles.cc', 'thevideo.me', 'streamin.to', 'uptobox.com', 'uptostream.com', 'jetload.net', 'jetload.tv', 'jetload.to']

        self.hosthqDict = ['gvideo', 'google.com', 'thevideo.me', 'raptu.com', 'filez.tv', 'uptobox.com', 'uptostream.com',
                           'xvidstage.com', 'xstreamcdn.com', 'idtbox.com']

        self.hostblockDict = ['zippyshare.com', 'youtube.com', 'facebook.com', 'twitch.tv', 'streamango.com', 'streamcherry.com',
                              'openload.io', 'openload.co', 'openload.pw', 'oload.tv', 'oload.stream', 'oload.win', 'oload.download', 'oload.info', 'oload.icu', 'oload.fun', 'oload.life', 'oload.space', 'oload.monster',
                              'rapidvideo.com', 'rapidvideo.is', 'rapidvid.to']

        self.sourcecfDict = ['123123movies', '123movieshubz', 'extramovies', 'movie4kis', 'projectfree', 'rapidmoviez', 'rlsbb', 'scenerls', 'timewatch', 'tvmovieflix', '1337x', 'btdb', 'ytsam',
                             'animebase', 'filmpalast', 'hdfilme', 'iload', 'movietown', '1putlocker', 'animetoon', 'azmovie', 'cartoonhdto', 'cmoviestv', 'freefmovies', 'ganoolcam', 'projectfreetv', 'putlockeronl',
                             'sharemovies', 'solarmoviefree', 'tvbox', 'xwatchseries', '0day', '2ddl', 'doublr', 'pirateiro']

    def getPremColor(self, n):
        if n == '0': n = 'blue'
        elif n == '1': n = 'red'
        elif n == '2': n = 'yellow'
        elif n == '3': n = 'deeppink'
        elif n == '4': n = 'cyan'
        elif n == '5': n = 'lawngreen'
        elif n == '6': n = 'gold'
        elif n == '7': n = 'magenta'
        elif n == '8': n = 'yellowgreen'
        elif n == '9': n = 'white'
        elif n == '10': n = 'black'
        elif n == '11': n = 'crimson'
        elif n == '12': n = 'goldenrod'
        elif n == '13': n = 'powderblue'
        elif n == '14': n = 'deepskyblue'
        elif n == '15': n = 'springgreen'
        elif n == '16': n = 'darkcyan'
        elif n == '17': n = 'aquamarine'
        elif n == '18': n = 'mediumturquoise'
        elif n == '19': n = 'khaki'
        elif n == '20': n = 'darkorange'
        elif n == '21': n = 'none'
        else: n = 'gold'
        return n
