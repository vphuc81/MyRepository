# -*- coding: utf-8 -*-

import api
import xbmc
import source

if __name__ == '__main__':
	cache_path = xbmc.translatePath('special://temp')
	src = source.Source(cache_path)
	api.AddonMain(int(sys.argv[1]), src)
