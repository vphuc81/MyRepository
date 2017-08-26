
import xbmc
import xbmcgui
import xbmcaddon
import urllib
import urlparse
import requests
from resources.lib.util.xml import BobItem, BobList
from resources.lib.sources import Sources, choose_quality
from resources.lib.util.info import get_info
from Queue import Queue
from threading import Thread

q = Queue()


class background_queue():
    @classmethod
    def put(cls, item):
        xbmcgui.Window(10008).setProperty('Bob_Queue', repr(item))

    @classmethod
    def get(cls):
        try:
            item = xbmc.getInfoLabel('Window(10008).Property(Bob_Queue)')
            xbmcgui.Window(10008).clearProperty('Bob_Queue')
            return item
        except Exception:
            return ""


def worker():
    while True:
        if xbmc.abortRequested:
            break
        item = background_queue.get()
        if item:
            q.put(item)
        xbmc.sleep(500)


def main():
    t = Thread(target=worker)
    t.start()
    while True:
        if xbmcaddon.Addon().getSetting("disable_service") == "true":
            xbmc.log("Bob Unleashed: Disabling Service")
            break
        if xbmc.abortRequested:
            break
        xbmc.sleep(1000)
        try:
            item = q.get_nowait()
            if item:
                bg_queue(item)
            q.task_done()
        except Exception:
            pass


def bg_queue(item, depth=0, selected_link=None):
    if type(item) == dict:
        bob_item = eval(item)
    else:
        bob_item = BobItem(item)
    playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
    if selected_link is None:
        if xbmcaddon.Addon().getSetting('default_link') != 'BOTH':
            selected_link = xbmcaddon.Addon().getSetting('default_link')
        elif xbmcgui.Dialog().yesno('Select the quality to queue', '', '',
                                    yeslabel='HD', nolabel='SD'):
            selected_link = "HD"
        else:
            selected_link = "SD"
    if "<item>" in str(bob_item):
        play = False
        if xbmcaddon.Addon().getSetting("autostart_queue") == "true":
            if playlist.size() == 0:
                play = True
        resolved = resolve_item(item, selected_link)
        xbmc.log("resolved: " + repr(resolved), xbmc.LOGNOTICE)
        if resolved:
            playlist.add(resolved,
                         xbmcgui.ListItem(bob_item["title"],
                                          iconImage=bob_item.get("thumbnail",
                                                                 "")))
        if play:
            from resources.lib.sources import play_queue
            play_queue()
    else:
        link = bob_item.get("url", bob_item.get("link", ""))
        if link:
            xbmc.log("fetching sublist: " + repr(link))
            boblist = BobList(link).get_raw_list()
            for list_item in boblist:
                bg_queue(str(list_item), depth + 1, selected_link)


def resolve_item(item, selected_link):
    if item.startswith("<plugin>"):
        # link to plugin
        link = BobItem(item)["link"]
        sublinks = BobItem(link).getAll("sublink")
        if sublinks:
            if len(sublinks) > 1:
                link = choose_quality(link)
            else:
                link = sublinks[0]
        link = link.replace("&amp;", "&")
        return link
    item = BobItem(item)

    link = item["link"]
    meta = BobItem(item["meta"])
    title = meta["title"]
    year = meta["year"].split("-")[0].strip()
    imdb = meta["imdb"]
    tvdb = meta.get("tvdb", "")
    season = meta.get("season", "")
    episode = meta.get("episode", "")
    tvshowtitle = meta.get("tvshowtitle", None)
    premiered = meta.get("premiered", "")
    try:
        premiered = premiered.split("-")[0].strip()
    except Exception:
        if len(premiered) == 4:
            pass
        else:
            xbmc.log("wrong premiered format")
    icon = xbmcaddon.Addon().getAddonInfo('icon')
    preset = choose_quality(link, selected_link=selected_link)
    infolabels = {}
    if preset:
        preset = preset.replace("&amp;", "&")
        listitem = None
        fetch_meta = xbmcaddon.Addon().getSetting("metadata") == "true"
        listitem = xbmcgui.ListItem(path=link,
                                    iconImage=item.get("thumbnail", icon),
                                    thumbnailImage=item.get("thumbnail",
                                                            icon))
        if fetch_meta and imdb != "0":  # only try valid items with imdb
            infolabels = get_info([item.item_string])[0]
        listitem.setInfo(type="video", infoLabels=infolabels)
        listitem.setLabel(item.get("title", item.get("name", "")))
        if "search" in preset:
            # nanscraper link
            resolved = Sources.get_sources(
                title, year, imdb, tvdb, season, episode, tvshowtitle,
                premiered, preset=preset, listitem=listitem,
                output_function=check_playable, skip_selector=True)
            return resolved
        elif preset.startswith("http") or preset.startswith("plugin"):
            # direct link
            if "/playlist" in preset:
                return preset
            elif "plugin://plugin.video.youtube/play/?video_id=" in preset:
                return preset
            elif item["content"] == "image":
                return
            else:
                return preset
        else:
            # who knows
            xbmc.log("unknown link type: " + repr(preset), xbmc.LOGDEBUG)
            raise Exception()


def check_playable(url, showbusy=False, ignore_dp=False, item=None):
    try:
        try:
            hmf = urlresolver.HostedMediaFile(url=url, include_disabled=False, include_universal=True)
            if hmf.valid_url() == True:
                url = hmf.resolve()
                return url
        except:
            pass
        headers = ''

        result = None

        if url.startswith('http') and '.m3u8' in url:
            result = requests.head(url, timeout=5)
            if result is None:
                return None

        elif url.startswith('http'):
            result = requests.head(url, timeout=5)
            if result is None:
                return None

        if url == "http://m4ufree.info" or "drive" in url:
            return None

        return url
    except:
        return None

if __name__ == '__main__':
    main()
