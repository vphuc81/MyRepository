# -*- coding: utf-8 -*-

'''
    PressPlay Add-on
    Copyright (C) 2017 PressPlay

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
'''

import pkgutil
import os

from resources.lib.modules import log_utils, control

__all__ = [x[1] for x in os.walk(os.path.dirname(__file__))][0]


def sources():
    try:
        sourceDict = []
        orion_color = control.setting('orion.color')
        for i in __all__:
            for loader, module_name, is_pkg in pkgutil.walk_packages([os.path.join(os.path.dirname(__file__), i)]):
                if is_pkg:
                    continue

                try:
                    module = loader.find_module(module_name).load_module(module_name)

                    # [ORION/]
                    if module_name == 'orionoid':
                        if not orion_color == 'No color':
                            module_name = '[COLOR %s]orion[/COLOR]' % orion_color
                        else: module_name = 'orion'
                    # [/ORION]

                    sourceDict.append((module_name, module.source()))
                except Exception as e:
                    log_utils.log('Could not load "%s": %s' % (module_name, e), log_utils.LOGDEBUG)
        return sourceDict
    except:
        return []


