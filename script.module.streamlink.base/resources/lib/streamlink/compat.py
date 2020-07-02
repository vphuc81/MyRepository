import os
import sys
import inspect

is_py2 = (sys.version_info[0] == 2)
is_py3 = (sys.version_info[0] == 3)
is_py33 = (sys.version_info[0] == 3 and sys.version_info[1] == 3)
is_win32 = os.name == "nt"

# win/nix compatible devnull
try:
    from subprocess import DEVNULL

    def devnull():
        return DEVNULL
except ImportError:
    def devnull():
        return open(os.path.devnull, 'w')

if is_py2:
    _str = str
    str = unicode
    range = xrange
    from itertools import izip

    def bytes(b, enc="ascii"):
        return _str(b)

elif is_py3:
    bytes = bytes
    str = str
    range = range
    izip = zip

try:
    from urllib.parse import (
        urlparse, urlunparse, urljoin, quote, unquote, parse_qsl, urlencode, urlsplit, urlunsplit, unquote_plus
    )
    import queue
    from shutil import which
except ImportError:
    from urlparse import urlparse, urlunparse, urljoin, parse_qsl, urlsplit, urlunsplit
    from urllib import quote, unquote, urlencode, unquote_plus
    import Queue as queue
    from streamlink.utils.shutil_which import shutil_which
    which = shutil_which.backport_which

if sys.version_info < (2, 7, 0):
    from streamlink.utils.ordereddict import OrderedDict
else:
    from collections import OrderedDict

try:
    from html import unescape as html_unescape
except ImportError:
    from HTMLParser import HTMLParser
    html_unescape = unescape = HTMLParser().unescape

getargspec = getattr(inspect, "getfullargspec", inspect.getargspec)

__all__ = [
    "is_py2", "is_py3", "is_py33", "is_win32", "str", "bytes", "urlparse", "urlunparse", "urljoin", "parse_qsl",
    "quote", "unquote", "queue", "range", "urlencode", "devnull", "which", "izip", "urlsplit", "urlunsplit",
    "getargspec", "html_unescape", "OrderedDict", "unquote_plus"
]
