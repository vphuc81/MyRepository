# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, os 

mysettings = xbmcaddon.Addon(id = 'plugin.video.ccloud.tv')
local_choice = mysettings.getSetting('local_choice')
online_choice = mysettings.getSetting('online_choice')
auto_run = mysettings.getSetting('enable_autorun')

xmlfile = xbmc.translatePath("special://home/userdata/addon_data/plugin.video.ccloud.tv/settings.xml")

def delete_local_path():
	with open(xmlfile, 'r') as f:
		lines = f.readlines()
	with open(xmlfile, 'w') as f:
		for line in lines:
			if ('id="local_path"' not in line): 
				 f.write(line) 

def delete_online_path():
	with open(xmlfile, 'r') as f:
		lines = f.readlines()
	with open(xmlfile, 'w') as f:
		for line in lines:
				if ('id="online_path"' not in line):
				 f.write(line)                     

try:
	if os.path.exists(xmlfile):
		if local_choice == 'false':
			delete_local_path()
		if online_choice == 'false':
			delete_online_path()
except:
	pass        

if auto_run == 'true':
    xbmc.executebuiltin("RunAddon(plugin.video.ccloud.tv)")