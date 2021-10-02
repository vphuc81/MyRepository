# -*- coding: UTF-8 -*-

import os, xbmcgui
from resources.lib.modules import control

def get():
        changelogfile = os.path.join(control.addonPath, 'changelog.txt')
        r = open(changelogfile)
        text = r.read()
        id = 10147
        control.execute('ActivateWindow(%d)' % id)
        control.sleep(500)
        win = xbmcgui.Window(id)
        retry = 50
        while (retry > 0):
            try:
                control.sleep(10)
                retry -= 1
                win.getControl(1).setLabel('[COLOR gold]Exodus [/COLOR] --Changelog--')
                win.getControl(5).setText(text)
                return
            except:
                pass


