# -*- coding: utf-8 -*-

import base64, sys
from six import ensure_text


def chk():
    return False
    fix = 'wd4dFZuxWbiZDO5x0d4dFZuxWbiZmWYF2aWJjYmJFShxWOXlFMoJDT'.encode('utf-8')
    d = base64.b64decode(base64.b64decode(fix[::-1]+ b'=='))[::-1].replace(b'_', b'.')
    d = six.ensure_text(d)
    if sys.argv[0] == d:
        return True

tmdb_key = ensure_text(base64.b64decode(b'MjBkMTFlYjEyYTU4NzhkYzgxNzU5Mzg1ZDE0NjE0MGE='))[::-1] if chk else ''
tvdb_key = ensure_text(base64.b64decode(b'TkdDNjdYWElIUUw4T0NNSg=='))[::-1] if chk else ''
fanarttv_key = ensure_text(base64.b64decode(b'ZTJhZGFmNjZkYmQ0MTE5ZjFjYWMwMzRiMzExMzU2MzM='))[::-1] if chk else ''
yt_key = ensure_text(base64.b64decode(b'Y19QN0xsOHRHeWEwZ1RLRWFrZFZ4V1dOaW9QdzZfX3dEeVNheklB'))[::-1] if chk else ''
trakt_client_id = ensure_text(base64.b64decode(b'ZTQ2MmM2NjRkNzg5NzdiNTQ4YTRiMjQzZjM0ZWM1YzYzZTQzYzM1Zjg3MzZiMTY2MGRiMTVkMDRmMzU4NjlkOA=='))[::-1] if chk else ''
trakt_secret = ensure_text(base64.b64decode(b'OThlMjRlZGRjOTdiOTU0OTZkZDU0YTY5YjU4ODliNzllZjljMzhhZTkxOGNjYzg2ZDZlODczN2FiNDMwZDY4NQ=='))[::-1] if chk else ''
orion_key = ensure_text(base64.b64decode(b'SExFRVJHS0JBTEozQkJFQ043SDlGQThLSzVMU0tYSFU='))[::-1] if chk else ''

