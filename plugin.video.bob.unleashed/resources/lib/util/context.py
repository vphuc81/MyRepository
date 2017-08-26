# -*- coding: utf-8 -*-

"""
    context.py --- functions to generate a context menu for bob items
    Copyright (C) 2017, Midraal

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, ordepends
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from resources.lib.util.url import get_addon_url
from resources.lib.util.views import save_view_mode
import resources.lib.external.tvdb_api as tvdb_api
import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
if ADDON.getSetting("language_id") == "system":
    LANG = xbmc.getLanguage(
        xbmc.ISO_639_1)
else:
    LANG = ADDON.getSetting("language_id")

tvdb = tvdb_api.Tvdb(
    "0629B785CE550C8D",
    language=LANG,
    cache=xbmc.translatePath(ADDON.getAddonInfo("profile")))


def get_context_items(item):
    """generate context menu for item
    Keyword Arguments:
    item -- BobItem to generate menu for
    """
    context = []
    content = item["content"]

    # information
    context.append((xbmcaddon.Addon().getLocalizedString(30708),
                    "XBMC.Action(Info)"))

    # view modes
    if content == "movie":
        context.append(("Set Movie View",
                        "RunPlugin({0})".format(
                            get_addon_url("save_view_mode", "movies"))))
    elif content == "tvshow":
        context.append(("Set TV Show View",
                        "RunPlugin({0})".format(
                            get_addon_url("save_view_mode", "tvshows"))))
    elif content == "season":
        context.append(("Set Season View",
                        "RunPlugin({0})".format(
                            get_addon_url("save_view_mode", "seasons"))))
    elif content == "episode":
        context.append(("Set Episode View",
                        "RunPlugin({0})".format(
                            get_addon_url("save_view_mode", "episodes"))))
    else:
        context.append(("Set View",
                        "RunPlugin({0})".format(
                            get_addon_url("save_view_mode", "othe"))))

    # extended info mod/qlickplay
    if xbmc.getCondVisibility("system.hasaddon(script.qlickplay)") or \
       xbmc.getCondVisibility("system.hasaddon(script.extendedinfo)"):
        if content == "movie":
            context.append(("Extended info",
                            "RunPlugin({0})".format(
                                get_addon_url("movie_extended_info",
                                              item["imdb"]))))
        elif content == "tvshow":
            context.append(("Extended info",
                            "RunPlugin({0})".format(
                                get_addon_url("tvshow_extended_info",
                                              item["imdb"]))))
        elif content == "season":
            url = "{'imdb': '%s', 'season': %s}" %\
                  (item["imdb"], item["season"])
            context.append(("Extended info",
                            "RunPlugin({0})".format(
                                get_addon_url("season_extended_info",
                                              url))))
        elif content == "episode":
            url = "{'imdb': '%s', 'season': %s, 'episode': %s}" %\
                  (item["imdb"], item["season"], item["episode"])
            context.append(("Extended info",
                            "RunPlugin({0})".format(
                                get_addon_url("episode_extended_info",
                                              url))))

    # metalliq
    if xbmc.getCondVisibility("system.hasaddon(plugin.video.metalliq)"):
        imdb = item.get("imdb", "")
        if imdb.startswith("tt"):
            if content == "movie":
                path = "plugin://plugin.video.metalliq/movies/add_to_library_parsed/imdb/%s/direct.bob.unleashed.m" % imdb
                context.append(("Add Movie To Library",
                                "RunPlugin({0})".format(path)))
            elif content in ["tvshow", "season", "episode"]:
                path = "plugin://plugin.video.metalliq/tv/add_to_library_parsed/%s/direct.bob.unleashed.m" % imdb
                context.append(("Add Show To Library",
                                "RunPlugin({0})".format(path)))

    # queue
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    if playlist.size() > 0:
        context.append(("Play Queue",
                        "RunPlugin({0})".format(
                            get_addon_url("play_queue"))))
        context.append(('Show Queue',
                        'Action("Playlist")'))
        context.append(("Clear Queue",
                        "RunPlugin({0})".format(
                            get_addon_url("clear_queue"))))

    if content == "movie":
        context.append(("Queue Movie",
                        "RunPlugin({0})".format(
                            get_addon_url("queue",
                                          item.item_string))))
    elif content == "tvshow":
        context.append(("Queue TV Show",
                        "RunPlugin({0})".format(
                            get_addon_url("queue",
                                          item.item_string))))
    elif content == "season":
        context.append(("Queue Season",
                        "RunPlugin({0})".format(
                            get_addon_url("queue",
                                          item.item_string))))
    elif content == "episode":
        context.append(("Queue Episode",
                        "RunPlugin({0})".format(
                            get_addon_url("queue",
                                          item.item_string))))
    else:
        context.append(("Queue Item",
                        "RunPlugin({0})".format(
                            get_addon_url("queue",
                                          item.item_string))))

    return context
