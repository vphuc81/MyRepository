# -*- coding: utf-8 -*-
"""

    Copyright (C) 2018-2018 plugin.video.youtube

    SPDX-License-Identifier: GPL-2.0-only
    See LICENSES/GPL-2.0-only for more information.
"""

from . import JSONStore
import base64
import re, requests, random

headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
			'Accept-Encoding': 'gzip, deflate',
		}

#it will get key again(random key) when click on youtube
url = "https://pastebin.com/raw/ArS0rS5B"
source = requests.get(url, headers=headers).text
codes = re.findall('<code>(.*?)(?s)</code>', source)[:]
random_len = random.randint(0,len(codes)-1)
#code = re.findall('<code>(.*?)(?s)</code>', source)[random_len]
code = codes[random_len]
key_b64 = re.findall('key: "(.*?)"', code)[0]
key = base64.b64decode(key_b64)
cid_b64 = re.findall('cid: "(.*?)"', code)[0]
cid = base64.b64decode(cid_b64)
csc_b64 = re.findall('csc: "(.*?)"', code)[0]
csc = base64.b64decode(csc_b64)

class APIKeyStore(JSONStore):
    def __init__(self):
        JSONStore.__init__(self, 'api_keys.json')

    def set_defaults(self):
        data = self.get_data()
        if 'keys' not in data:
            #data = {'keys': {'personal': {'api_key': '', 'client_id': '', 'client_secret': ''}, 'developer': {}}}
            data = {'keys': {'personal': {'api_key': key, 'client_id': cid, 'client_secret': csc}, 'developer': {}}}
        if 'keys' in data:
            data = {'keys': {'personal': {'api_key': key, 'client_id': cid, 'client_secret': csc}, 'developer': {}}}
        if 'personal' not in data['keys']:
            data['keys']['personal'] = {'api_key': '', 'client_id': '', 'client_secret': ''}
        if 'developer' not in data['keys']:
            data['keys']['developer'] = {}
        self.save(data)
