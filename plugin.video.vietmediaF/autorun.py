# -*- coding: utf-8 -*-

import xbmc, xbmcaddon

addon = xbmcaddon.Addon(id='plugin.video.vietmediaF')

on_off = addon.getSetting('on_off')

if on_off == 'true':				
    xbmc.executebuiltin("RunAddon(plugin.video.vietmediaF)")