# -*- coding: utf-8 -*-
"""
speedvid resolveurl plugin
Copyright (C) 2017 jsergio
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
from lib import aadecode
from resolveurl import common
from resolveurl.resolver import ResolverError
import requests

logger = common.log_utils.Logger.get_logger(__name__)
logger.disable()

net = common.Net()


def get_media_url(url, media_id):
    headers = {'User-Agent': common.RAND_UA}
    s = requests.Session()
    s.get("https://www.speedvid.net/", headers=headers)
    html = s.get(url, headers=headers).content
    if html:
        html = html.encode('utf-8')
        aa_text = re.findall("""(ﾟωﾟﾉ\s*=\s*/｀ｍ´\s*）\s*ﾉ.+?)</SCRIPT>""", html, re.I)
        if aa_text:
            try:
                aa_decoded = ''
                for i in aa_text:
                    try:
                        aa_decoded += str(aadecode.decode(
                            re.sub('\(+ﾟДﾟ\)+\s*\[ﾟoﾟ\]\)*\s*\+(.+?)\(+ﾟДﾟ\s*\)+\[ﾟoﾟ\]\)+',
                                   r'(ﾟДﾟ)[ﾟoﾟ]+\1(ﾟДﾟ)[ﾟoﾟ])', i)))
                    except:
                        pass
                href = re.search("""location\.href=.*/(.*?html)""", aa_decoded)
                if href:
                    href = href.group(1)
                    if href.startswith("https"):
                        location = href
                    elif href.startswith("//"):
                        location = "https:%s" % href
                    else:
                        location = "https://www.speedvid.net/%s" % href
                    #headers.update({'Referer': url, 'Cookie': str(
                    #    (int(math.floor((900 - 100) * random()) + 100)) * (int(time.time())) * (128 / 8))})

                    headers = {
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'DNT': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.67 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Referer': url,
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                    }

                    _html = s.get(location, headers=headers).content
                    #_html = net.http_GET(location, headers=headers).content
                    test = re.findall("""(\|net\|speedvid.*?)\'\.split""", _html)[-1].split("|")
                    link = "http://%s.speedvid.net:%s/%s/v.mp4" % (test[12], test[11], test[61])
                    return link
            except Exception as e:
                raise ResolverError(e)

    raise ResolverError('File not found')