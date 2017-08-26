# -*- coding: utf-8 -*-

"""
    testings.py --- functions dealing with local testings xml file
    Copyright (C) 2017, Midraal

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
import os

import xbmc
import xbmcaddon
import xbmcvfs

from koding import route
from resources.lib.util.xml import BobList
from resources.lib.util.xml import display_list

@route(mode="Testings", args=["file_name"])
def testings(file_name="testings.xml"):
    """
parses local xml file as a bob list
    :param str file_name: local file name to parse
    :return: list of bob items
    :rtype: list[dict[str,str]]
    """
    profile_path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode('utf-8')
    test_file = xbmcvfs.File(os.path.join(profile_path, file_name))
    xml = test_file.read()
    test_file.close()
    display_list(BobList(xml).get_list(), "videos")
