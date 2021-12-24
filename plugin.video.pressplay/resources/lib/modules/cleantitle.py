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

import re
import unicodedata
from six import ensure_str, ensure_text, PY2


def get(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = re.sub(r'&#(\d+);', '', title)
    title = re.sub(r'(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace(r'&quot;', '\"').replace(r'&amp;', '&').replace(r'–', '-').replace(r'!', '')
    title = re.sub(r'\n|([[].+?[]])|([(].+?[)])|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    return title


def get_title(title):
    if title is None: return
    from six.moves import urllib_parse
    try:
        title = ensure_str(title)
    except:
        pass
    title = urllib_parse.unquote(title).lower()
    title = re.sub('[^a-z0-9 ]+', ' ', title)
    title = re.sub(' {2,}', ' ', title)
    return title


def geturl(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.lower()
    title = title.rstrip()
    try: title = title.translate(None, ':*?"\'\.<>|&!,')
    except: title = title.translate(str.maketrans('', '', ':*?"\'\.<>|&!,'))
    title = title.replace('/', '-')
    title = title.replace(' ', '-')
    title = title.replace('--', '-')
    title = title.replace('–', '-')
    title = title.replace('!', '')
    return title


def get_url(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace(' ', '%20').replace('–', '-').replace('!', '')
    return title


def get_gan_url(title):
    if title is None:
        return
    title = title.lower()
    title = title.replace('-','+')
    title = title.replace(' + ', '+-+')
    title = title.replace(' ', '%20')
    return title


def get_query_(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace(' ', '_').replace("'", "_").replace('-', '_').replace('–', '_').replace(':', '').replace(',', '').replace('!', '')
    return title.lower()


def get_simple(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.lower()
    title = re.sub('(\d{4})', '', title)
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-')
    title = re.sub('\n|\(|\)|\[|\]|\{|\}|\s(vs|v[.])\s|(:|;|-|–|"|,|\'|\_|\.|\?)|\s', '', title).lower()
    return title


def getsearch(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.lower()
    title = re.sub('&#(\d+);', '', title)
    title = re.sub('(&#[0-9]+)([^;^0-9]+)', '\\1;\\2', title)
    title = title.replace('&quot;', '\"').replace('&amp;', '&').replace('–', '-')
    title = re.sub('\\\|/|-|–|:|;|!|\*|\?|"|\'|<|>|\|', '', title).lower()
    return title


def query(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace('\'', '').rsplit(':', 1)[0].rsplit(' -', 1)[0].replace('-', ' ').replace('–', ' ').replace('!', '')
    return title


def get_query(title):
    if title is None: return
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace(':', '').replace("'", "").lower()
    return title


def normalize(title):
    try:
        if PY2:
            try: return ensure_str(ensure_text(title, encoding='ascii'))
            except: pass
        return ''.join(c for c in unicodedata.normalize('NFKD', ensure_text(ensure_str(title))) if unicodedata.category(c) != 'Mn')
    except:
        return title


def clean_search_query(url):
    url = url.replace('-','+').replace(' ', '+').replace('–', '+').replace('!', '')
    return url


def scene_title(title, year):
    title = normalize(title)
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace('&', 'and').replace('-', ' ').replace('–', ' ').replace('/', ' ').replace('*', ' ').replace('!', '').replace('?', '').replace('...', '').replace(',', '')
    title = re.sub(' {2,}', ' ', title)
    if title.startswith('Birdman or') and year == '2014': title = 'Birdman'
    if title == 'Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)' and year == '2020': title = 'Birds of Prey'
    if title == "Roald Dahl's The Witches" and year == '2020': title = 'The Witches'
    return title, year


def scene_tvtitle(title, year, season, episode):
    title = normalize(title)
    try:
        title = ensure_str(title)
    except:
        pass
    title = title.replace('&', 'and').replace('-', ' ').replace('–', ' ').replace('/', ' ').replace('*', ' ').replace('!', '').replace('?', '').replace('...', '').replace(',', '')
    title = re.sub(' {2,}', ' ', title)
    if title in ['The Haunting', 'The Haunting of Bly Manor', 'The Haunting of Hill House'] and year == '2018':
        if season == '1': title = 'The Haunting of Hill House'
        elif season == '2': title = 'The Haunting of Bly Manor'; year = '2020'; season = '1'
    if title in ['Cosmos', 'Cosmos: A Spacetime Odyssey', 'Cosmos: Possible Worlds'] and year == '2014':
        if season == '1': title = 'Cosmos: A Spacetime Odyssey'
        elif season == '2': title = 'Cosmos: Possible Worlds'; year = '2020'; season = '1'
    if 'Special Victims Unit' in title: title = title.replace('Special Victims Unit', 'SVU')
    if title == 'Cobra Kai' and year == '1984': year = '2018'
    if title == 'The End of the F ing World': title = 'The End of the Fucking World'
    if title == 'M A S H': title = 'MASH'
    if title == "Grey's Anatomy": title = 'Greys Anatomy'
    return title, year, season, episode

