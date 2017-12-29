# -*- coding: utf-8 -*-

"""
    Exodus Add-on

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
from resources.lib.modules import log_utils
from resources.lib.modules import control

control.execute('RunPlugin(plugin://%s)' % control.get_plugin_url({'action': 'service'}))

try:
    ModuleVersion = control.addon('script.module.exodus').getAddonInfo('version')
    AddonVersion = control.addon('plugin.video.exodus').getAddonInfo('version')
    # RepoVersion = control.addon('repository.exodus').getAddonInfo('version')

    log_utils.log('######################### EXODUS ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT EXODUS VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### EXODUS PLUGIN VERSION: %s ###' % str(AddonVersion), log_utils.LOGNOTICE)
    log_utils.log('### EXODUS SCRIPT VERSION: %s ###' % str(ModuleVersion), log_utils.LOGNOTICE)
    # log_utils.log('### COLOSSUS REPOSITORY VERSION: %s ###' % str(RepoVersion), log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
except:
    log_utils.log('######################### EXODUS ############################', log_utils.LOGNOTICE)
    log_utils.log('####### CURRENT EXODUS VERSIONS REPORT ######################', log_utils.LOGNOTICE)
    log_utils.log('### ERROR GETTING EXODUS VERSIONS - NO HELP WILL BE GIVEN AS THIS IS NOT AN OFFICIAL EXODUS INSTALL. ###', log_utils.LOGNOTICE)
    log_utils.log('###############################################################', log_utils.LOGNOTICE)
