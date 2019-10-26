# -*- coding: utf-8 -*-
# XStreamCDN resolver for ResolveURL
# Feb 22 2019

import re
import requests

from resolveurl.resolver import ResolveUrl, ResolverError


class XStreamCDNResolver(ResolveUrl):
    name = 'XStreamCDN'
    domains = ["vidspace.io"]
    pattern = '(?://|\.)((?:vidspace\.io))/([\w-]+)'  # Host and media-id pattern.

    def get_media_url(self, host, media_id):
        try:
            url = self.get_url(host, media_id)

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'pl,en-US;q=0.7,en;q=0.3',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0',
                'TE': 'Trailers',
            }

            response = requests.get(url, headers=headers, verify=False).text
            video = re.findall(r"src: \"(.*?)\"", response)[0]
            return video
        except:
            raise ResolverError('Unable to locate video')

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='http://{host}/{media_id}.html')
