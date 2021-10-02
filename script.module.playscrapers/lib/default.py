# -*- coding: utf-8 -*-

import sys, base64
import six
from six.moves import urllib_parse
from playscrapers import sources_playscrapers
from playscrapers.modules import control
from playscrapers import providerSources, providerNames


params = dict(urllib_parse.parse_qsl(sys.argv[2].replace('?', '')))
action = params.get('action')
mode = params.get('mode')
query = params.get('query')

def ScraperChoice():
    from playscrapers import providerSources
    sourceList = providerSources()
    control.idle()
    select = control.selectDialog([i for i in sourceList])
    if select == -1: return
    module_choice = sourceList[select]
    control.setSetting('package.folder', module_choice)
    control.sleep(200)
    control.openSettings('0.1')

def ToggleProviderAll(enable):
    from playscrapers import providerNames
    sourceList = providerNames()
    (setting, open_id) = ('true', '0.3') if enable else ('false', '0.2')
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, setting)
    control.sleep(200)
    control.openSettings(open_id)


if action == "playscrapersettings":
    control.openSettings('0.0', 'script.module.playscrapers')

elif mode == "playscrapersettings":
    control.openSettings('0.0', 'script.module.playscrapers')


elif action == "ScraperChoice":
    ScraperChoice()


elif mode == "ScraperChoice":
    ScraperChoice()


elif action == "toggleAll":
    sourceList = []
    sourceList = sources_playscrapers.all_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All providers = %s' % sourceList,2)
    control.sleep(200)
    control.openSettings(query, "script.module.playscrapers")


elif action == "ToggleProviderAll":
    ToggleProviderAll(False if params['action'] == "DisableModuleAll" else True)


elif action == "toggleAllHosters":
    sourceList = []
    sourceList = sources_playscrapers.hoster_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Hoster providers = %s' % sourceList,2)
    control.sleep(200)
    control.openSettings(query, "script.module.playscrapers")


elif action == "toggleAllForeign":
    sourceList = []
    sourceList = sources_playscrapers.all_foreign_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Foregin providers = %s' % sourceList,2)
    control.sleep(200)
    control.openSettings(query, "script.module.playscrapers")


elif action == "toggleAllGreek":
    sourceList = []
    sourceList = sources_playscrapers.greek_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Greek providers = %s' % sourceList,2)
    control.sleep(200)
    control.openSettings(query, "script.module.playscrapers")


elif action == "toggleAllTorrent":
    sourceList = []
    sourceList = sources_playscrapers.torrent_providers
    for i in sourceList:
        source_setting = 'provider.' + i
        control.setSetting(source_setting, params['setting'])
#    xbmc.log('All Torrent providers = %s' % sourceList,2)
    control.sleep(200)
    control.openSettings(query, "script.module.playscrapers")


# elif action == "Defaults":
    # sourceList = ['123fox','123hbo','123movieshubz','animetoon','azmovies','bnwmovies','cartoonhd',
    # 'extramovies','fmovies','freefmovies','freeputlockers','gostream','Hdmto','hdpopcorns',
    # 'kattv','l23movies','iwaatch','openloadmovie','primewire','putlocker','reddit','rlsbb','scenerls',
    # 'seehd','series9','seriesfree','seriesonline','solarmoviez','tvbox','vidics','watchseries',
    # 'xwatchseries','vdonip','downflix','ymovies','ddlspot','filmxy','kickass2','sezonlukdizi']
    # for i in sourceList:
        # source_setting = 'provider.' + i
        # control.setSetting(source_setting, params['setting'])
    # control.sleep(200)
    # control.openSettings(query, "script.module.playscrapers")

