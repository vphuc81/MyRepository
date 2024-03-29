"""
    Plugin for UrlResolver
    Copyright (C) 2021 gujal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import re
import base64
from urlresolver.plugins.lib import helpers, jsunhunt
from urlresolver import common
from urlresolver.resolver import UrlResolver, ResolverError


class UpVideoResolver(UrlResolver):
    name = "upvideo.to"
    domains = ['upvideo.to', 'videoloca.xyz', 'tnaket.xyz', 'makaveli.xyz']
    pattern = r'(?://|\.)((?:upvideo|videoloca|makaveli|tnaket)\.(?:to|xyz))/(?:e|v)/([0-9a-zA-Z]+)'

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.CHROME_USER_AGENT}
        html = self.net.http_GET(web_url, headers=headers).content
        headers.update({'Referer': web_url})

        if 'sorry' in html:
            raise ResolverError("Video Deleted")

        if jsunhunt.detect(html):
            html = re.findall('<head>(.+?)</head>', html, re.DOTALL)[0]
            html = jsunhunt.unhunt(html)

        r = re.search(r'var\s*ebdbcdbeffbe\s*=\s*"([^"]+)', html)
        if r:
            surl = r.group(1).replace('MDZhYTRhMDViOWZkNzlkZjE5ODAzNDNkYTljY2ZkZmU', '')
            surl = surl.replace('NzU1ODRlMDM3NGIzZjk1NTIxZGUzZTQ3MDRiOTNjOTY=', '')
            surl = base64.b64decode(surl).decode('utf-8')
            return surl.replace(' ', '%20') + helpers.append_headers(headers)

        raise ResolverError("Video not found")

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://{host}/e/{media_id}')
