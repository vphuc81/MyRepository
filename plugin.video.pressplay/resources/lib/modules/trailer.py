# -*- coding: utf-8 -*-

"""
    PressPlay Add-on
    ///Updated for PressPlay///

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

import sys
import simplejson as json
import re
import base64
import six
from six.moves import urllib_parse

from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import api_keys
from resources.lib.modules import log_utils


class trailer:
    def __init__(self):
        self.mode = control.setting('trailer.select')
        self.content = control.infoLabel('Container.Content')
        self.base_link = 'https://www.youtube.com'
        self.key = control.addon('plugin.video.youtube').getSetting('youtube.api.key')
        if self.key == '': self.key = api_keys.yt_key
        try: self.key_link = '&key=%s' % self.key
        except: pass
        if self.mode == '1':
            self.search_link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=9&q=%s' + self.key_link
        elif self.mode == '2':
            if self.content in ['seasons', 'episodes']:
                self.search_link = 'https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&maxResults=9&q=%s' + self.key_link
            else:
                self.search_link = 'https://www.googleapis.com/youtube/v3/search?part=id&type=video&maxResults=1&q=%s' + self.key_link
        else:
            self.search_link = 'https://www.googleapis.com/youtube/v3/search?part=id&type=video&maxResults=1&q=%s' + self.key_link
        self.youtube_watch = 'https://www.youtube.com/watch?v=%s'

    def play(self, name='', url='', windowedtrailer=0):
        try:
            name = control.infoLabel('ListItem.Title')
            if not name:
                name = control.infoLabel('ListItem.Label')
            if self.content == 'movies':
                name += ' ' + control.infoLabel('ListItem.Year')
            name += ' trailer'
            if self.content in ['seasons', 'episodes']:
                season = control.infoLabel('ListItem.Season')
                episode = control.infoLabel('ListItem.Episode')
                if not season is '':
                    name = control.infoLabel('ListItem.TVShowTitle')
                    name += ' season %01d trailer' % int(season)
                    if not episode is '':
                        name = name.replace('season ', '').replace(' trailer', '')
                        name += 'x%02d' % int(episode)

            url = self.worker(name, url)
            if not url:return

            icon = control.infoLabel('ListItem.Icon')

            item = control.item(label=name, path=url)
            item.setArt({'icon': icon, 'thumb': icon, 'poster': icon})
            item.setInfo(type="video", infoLabels={"title": name})

            item.setProperty('IsPlayable', 'true')
            control.resolve(handle=int(sys.argv[1]), succeeded=True, listitem=item)
            if windowedtrailer == 1:
                # The call to the play() method is non-blocking. So we delay further script execution to keep the script alive at this spot.
                # Otherwise this script will continue and probably already be garbage collected by the time the trailer has ended.
                control.sleep(1000)  # Wait until playback starts. Less than 900ms is too short (on my box). Make it one second.
                while control.player.isPlayingVideo():
                    control.sleep(1000)
                # Close the dialog.
                # Same behaviour as the fullscreenvideo window when :
                # the media plays to the end,
                # or the user pressed one of X, ESC, or Backspace keys on the keyboard/remote to stop playback.
                control.execute("Dialog.Close(%s, true)" % control.getCurrentDialogId)
        except:
            pass

    def worker(self, name, url):
        try:
            if url.startswith(self.base_link):
                url = self.resolve(url)
                if not url: raise Exception()
                return url
            elif not url.startswith('http'):
                url = self.youtube_watch % url
                url = self.resolve(url)
                if not url: raise Exception()
                return url
            else:
                raise Exception()
        except:
            query = self.search_link % urllib_parse.quote_plus(name)
            return self.search(query)

    def search(self, url):
        try:
            apiLang = control.apiLanguage().get('youtube', 'en')

            if apiLang != 'en':
                url += "&relevanceLanguage=%s" % apiLang

            result = client.request(url)
            if result == None:
                log_utils.log('yt_api_failed_resp: ' + str(result))
                control.infoDialog('Please utilise your own API key[CR]on YouTube add-on', 'API key quota limit reached', time=5000)
                return
            result = six.ensure_text(result)

            json_items = json.loads(result).get('items', [])
            items = [i.get('id', {}).get('videoId') for i in json_items]

            if self.mode == '1':
                labels = [i.get('snippet', {}).get('title') for i in json_items]
                labels = [client.replaceHTMLCodes(i) for i in labels]
                select = control.selectDialog(labels, control.lang(32121))
                if select == -1: return
                items = [items[select]]

            elif self.mode == '2':
                if self.content in ['seasons', 'episodes']:
                    labels = [i.get('snippet', {}).get('title') for i in json_items]
                    labels = [client.replaceHTMLCodes(i) for i in labels]
                    select = control.selectDialog(labels, control.lang(32121))
                    if select == -1: return
                    items = [items[select]]

            for vid_id in items:
                url = self.resolve(vid_id)
                if url:
                    return url
        except:
            return

    def resolve(self, url):
        try:
            id = url.split('?v=')[-1].split('/')[-1].split('?')[0].split('&')[0]
            result = client.request(self.youtube_watch % id)

            message = client.parseDOM(result, 'div', attrs={'id': 'unavailable-submessage'})
            message = ''.join(message)

            alert = client.parseDOM(result, 'div', attrs={'id': 'watch7-notification-area'})

            if len(alert) > 0: raise Exception()
            if re.search('[a-zA-Z]', message): raise Exception()

            url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % id
            return url
        except:
            return
