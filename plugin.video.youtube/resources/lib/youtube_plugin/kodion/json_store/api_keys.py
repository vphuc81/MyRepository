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


'''
url = "https://pastebin.com/raw/yifXvWah"
source = requests.get(url, headers=headers).text
key_b64 = re.findall('key: "(.*?)"', source)[0]
key = base64.b64decode(key_b64)
cid_b64 = re.findall('cid: "(.*?)"', source)[0]
cid = base64.b64decode(cid_b64)
csc_b64 = re.findall('csc: "(.*?)"', source)[0]
csc = base64.b64decode(csc_b64)
'''

#key = base64.b64decode('QUl6YVN5RExCM0NtV0dOOEpqV0k0U0xMdEdMZVhGaWl1cldJWHRz')
#key = base64.b64decode('QUl6YVN5Qjc3cHlqbmltRy1SQWR2Y3dtVTNlc0dJUThXOVg1RDRZ')
#key = base64.b64decode('QUl6YVN5Q2lnYS0tUktZWGplNzMzZExwU3pSZ211NUFnWG5DX1o4')
#cid = base64.b64decode('ODc0NzQ5OTE4OC03NTFyZmw4ZXA3b2VtOWZxaTgyaTUycG82dTlwNzdmYg==')
#cid = base64.b64decode('OTkyMjE2NjE2NTcwLTVvN2Y1cmdwM2RmcXY5ODRpM3Npb3NqYWozZ2szdDVnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29t')
#csc = base64.b64decode('X1RoNjdpRXdKQnNGN0Q0Q1F2SWlBSmEt')
#csc = base64.b64decode('Mm9ZOG92VmFZakV4TEtXQlNLT3Q3T01m')

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