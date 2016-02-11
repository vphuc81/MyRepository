# -*- coding: utf-8 -*-
#------------------------------------------------------------
# RadioReference.com
#------------------------------------------------------------
# Based on code from pelisalacarta
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
#------------------------------------------------------------

#Code Upated by: Blazetamer 2014
#Code Updated by: idleloop @ 2014, Oct

import urlparse,urllib2,urllib,re
import os, sys

from core import logger
from core import config
from core import scrapertools
from core.item import Item

DEBUG = config.get_setting("debug")
URL = "http://www.earthcam.com/network/"
IMAGES = os.path.join(config.get_runtime_path(),"resources")

def isGeneric():
    return True

def mainlist(item):
    logger.info("[channel.py] mainlist")
    itemlist=[]
    itemlist.append( Item(action="cams",      title="Featured Cams" , url=URL ) )
    itemlist.append( Item(action="usa",       title="USA" , url=URL ) )
    itemlist.append( Item(action="worldwide", title="Worldwide" , url=URL ) )
    return itemlist

def worldwide(item):
    logger.info("[channel.py] worldwide")
    itemlist = []

    data = scrapertools.cache_page(item.url)
    patron  = ';" href="([^"]+)" class="locationLink">(.+?)</a>'
    #patron  = '<p class="location"><a\s+onclick="[^"]+" href="(/network/index.php\?page\=world\&country\=[^"]+)" class="[^"]+">([^<]+)</a></p>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if (DEBUG==True): scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        url = url.replace('[','').replace(']','')
        print'WORLDWIDE PARSED IS ' +url
        title = scrapedtitle.strip()
        if (DEBUG==True): logger.info("title=["+title+"], url=["+url+"]")
        if 'page=world' in url:
            itemlist.append( Item(action="cams", title=title , url=url, fanart=os.path.join(IMAGES,"fanart.jpg") ) )

    return itemlist

def usa(item):
    logger.info("[channel.py] usa")
    itemlist = []

    data = scrapertools.cache_page(item.url)
    patron  = ';" href="([^"]+)" class="locationLink">(.+?)</a>'
    #patron  = '<p class="location"><a  onclick="[^"]+" href="(index.php?country=us&[^"]+)" class="[^"]+">([^<]+)</a>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    #match=re.compile(';" href="(.+?)" class="locationLink">(.+?)</a>').findall(link)
    if (DEBUG==True): scrapertools.printMatches(matches)

    for scrapedurl,scrapedtitle in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        print'USA PARSED IS ' +url
        title = scrapedtitle.strip()
        if (DEBUG==True): logger.info("title=["+title+"], url=["+url+"]")
        if 'country=us'in url:
         itemlist.append( Item(action="cams", title=title , url=url, fanart=os.path.join(IMAGES,"fanart.jpg") ) )

    return itemlist

def cams(item):
    logger.info("[channel.py] cams")
    itemlist = []

    item.url.replace(" ","%20")
    data = scrapertools.cache_page(item.url.replace(" ","%20"))
    #logger.info("data="+data)
    
    patron  = '<div[^<]+'
    patron += '<div[^<]+<a[^<]+<div[^<]+<img\s+class="[^"]*"\s+src="([^"]+)"[^<]+</div>[^<]+'
    patron += '</a></div>[^<]+'
    patron += '<div[^<]+'
    patron += '<p[^<]+<img[^<]+<a href="([^"]+)" class="featuredTitleLink"><span class="featuredTitle">([^<]+)</span></a></p>[^<]+'
    patron += '<p style="[^"]+" class="featuredCity">([^<]+)</p>[^<]+'
    patron += '<p style="[^"]+" class="featuredDescription">([^<]+)</p>'
    matches = re.compile(patron,re.DOTALL).findall(data)
    if (DEBUG==True): scrapertools.printMatches(matches)

    if len(matches)==0:
        patron  = '<div[^<]+'
        patron += '<div[^<]+<a[^<]+<div[^<]+<img\s+class="[^"]*"\s+src="([^"]+)"[^<]+</div>[^<]+'
        patron += '</a></div>[^<]+'
        patron += '<div[^<]+'
        patron += '<p[^<]+<a href="([^"]+)"[^<]+<span[^>]+>([^<]+)</span></a></p>[^<]+'
        patron += '<p style="[^"]+"[^>]+>([^<]+)</p>[^<]+'
        patron += '<p style="[^"]+"[^>]+>([^<]+)</p>'
        matches = re.compile(patron,re.DOTALL).findall(data)
        if (DEBUG==True): scrapertools.printMatches(matches)
    
    for scrapedthumbnail,scrapedurl,scrapedtitle,location,scrapedplot in matches:
        url = urlparse.urljoin(item.url,scrapedurl)
        logger.info(url)
        thumbnail = urlparse.urljoin(item.url,scrapedthumbnail)
        title = scrapedtitle.strip()+" ("+location+")"
        plot = scrapedplot.strip()
        if (DEBUG==True): logger.info("title=["+title+"], url=["+url+"]")
        if url.startswith("http://www.earthcam.com") and not url.startswith("http://www.earthcam.com/client/"):
            item=Item(action="previous_play", title=title , url=url, thumbnail=thumbnail, 
                fanart=thumbnail, plot=plot )
            item_thereafter=previous_play(item, True)
            try:
                if len(item_thereafter) == 1:
                    item=Item( action="play", title=title , url=item_thereafter[0].url, thumbnail=item_thereafter[0].thumbnail, 
                    fanart=item_thereafter[0].fanart, plot=item_thereafter[0].plot, folder=False )
                elif not item_thereafter: # hide empty menus :-(
                    continue
                itemlist.append( item )
            except: print "Not listing bad url"    

    return itemlist

def previous_play(item, just_check=False):
    itemlist = []

    data = scrapertools.cache_page(item.url)
    logger.info("item.url="+item.url)
    # Extracts json info
    json_text=''
    try:
        json_text = scrapertools.get_match(data,'flashvars.path\s+\=\s*"([^"]+)"')
    except Exception, e:
        pass
    if len(json_text) < 100:
        try:
            json_text = (re.search( r'flashvars.json\s+\=\s*"([^"]+)"', data )).group(1)
        except Exception, e:
            pass
    if len(json_text) < 100:
        try:        
            json_text = (re.search( r'json_base\s+\=\s*(.+);', data )).group(1)
        except Exception, e:
            pass
    if len(json_text) < 100:
        try:
            # array of pages for deeper inspection throu new previous_play(): so new folder
            cams = [m.groupdict() for m in 
                (re.finditer( r' href="(?P<url>index.php\?cam=[^"]+)">.+?<img src="(?P<thumbnail>[^"]+)".+?title="(?P<title>[^"]+)"', 
                    data, flags=re.DOTALL))]
            if not cams:
                return []
            if (DEBUG==True): logger.info("portal of cams=" + str(cams))
            for cam_id in cams:
                new_item=Item(action="previous_play", title=cam_id["title"] , url=item.url + cam_id["url"], thumbnail=cam_id["thumbnail"], 
                    fanart=cam_id["thumbnail"], plot=cam_id["title"] )
                itemlist.append( new_item )
            return itemlist
        except Exception, e:
            logger.info("[earthcam] channel.py " + str(e))
            return []
    if (DEBUG==True): logger.info("json_text="+json_text)
    json_decoded = urllib.unquote(json_text)
    if (DEBUG==True): logger.info("json_decoded="+json_decoded)
    json_object = load_json(json_decoded)
    if (DEBUG==True): logger.info("json_object="+str(json_object))
    
    #http://www.earthcam.com/usa/newyork/timessquare/?cam=tsstreet
    #if "?cam=" in item.url:
    video_url=""
    #try:
    #    # Extract cam_id
    #    cam_id = item.url.split("?")[1].split("=")[1]
    #    logger.info("cam_id="+cam_id)
    #    cam_data=json_object["cam"][cam_id]
    #    if (DEBUG==True): logger.info("cam_data="+str(cam_data))

    #    offline = cam_data["showOfflineMessage"]
    #    logger.info("offline="+offline)
    #    liveon = cam_data["liveon"]
    #    logger.info("liveon="+liveon)
    
    #    video_url = cam_data["worldtour_path"]
    #    logger.info("video_url="+video_url)
    #    url = calculate_url(video_url)
    #    itemlist.append( Item(action="play", title=item.title , server="directo", url=url, 
    #        fanart=item.thumbnail, thumbnail=item.thumbnail, folder=False) )
    #except:
    #   logger.info("NO cam_id")
    try:
        cam_data=json_object["cam"]
        logger.info("len(cam_data)=%d" % len(cam_data))
        for cam_id in cam_data:
            if (just_check==True and len(itemlist)>1): # just checking how menu submenus are here... if >1, info is already enough
                return itemlist
            logger.info("cam_id="+str(cam_id))
            liveon = cam_data[cam_id]["liveon"]
            logger.info("liveon="+liveon)
            if liveon!="disabled":
                ###video_url = cam_data[cam_id]["worldtour_path"]
                video_url
                try:
                    if "worldtour_path" in cam_data[cam_id] and re.search( r'(\.flv|\.mp4|\.jpg|\.png)$', cam_data[cam_id]["worldtour_path"] ):
                        video_url = cam_data[cam_id]["worldtour_path"]
                    elif "livestreamingpath" in cam_data[cam_id] and re.search( r'(\.flv|\.mp4)$', cam_data[cam_id]["livestreamingpath"] ):
                        video_url = cam_data[cam_id]["streamingdomain"] + cam_data[cam_id]["livestreamingpath"]
                    elif "timelapsepath" in cam_data[cam_id] and re.search( r'(\.flv|\.mp4)$', cam_data[cam_id]["timelapsepath"] ):
                        video_url = cam_data[cam_id]["timelapsedomain"] + cam_data[cam_id]["timelapsepath"]
                    elif "archivepath" in cam_data[cam_id] and re.search( r'(\.flv|\.mp4)$', cam_data[cam_id]["archivepath"] ):
                        video_url = cam_data[cam_id]["archivedomain"] + cam_data[cam_id]["archivepath"]
                    else:
                        continue
                    video_url.replace("//","/")
                    url = calculate_url(video_url)
                    item=Item(action="play", url=url, 
                            folder=False)
                    try:
                        item.title=cam_data[cam_id]["title"]
                    except Exception, e:
                        item.title=str(cam_id)
                    try:
                        item.fanart='http://static.earthcamcdn.com'+cam_data[cam_id]["offlineimage"]
                    except Exception, e:
                        logger.info("[channel.py] [play] ERROR: no fanart")
                    try:
                        item.thumbnail=cam_data[cam_id]["thumbimage"]
                    except Exception, e:
                        logger.info("[channel.py] [play] ERROR: no thumbnail")
                    try:
                        item.plot = re.sub(r'</?span[^>]*>', '', 
                            cam_data[cam_id]["description"].replace('+', ' '), 
                            flags=re.IGNORECASE )
                        item.plot = re.sub(r'<[^>]+>', "\n", item.plot)
                    except Exception, e:
                        logger.info("[channel.py] [play] ERROR: no plot")
                    itemlist.append( item )
                except Exception, e:
                    logger.info("[channel.py] [play] ERROR:"+url)
        
        return itemlist
    except: print "bad url given"

def play(item):
    itemlist = []
    if re.search( r'(\.flv|\.mp4|\.jpg|\.png)$', item.url ) or item.url.startswith("rtmp"):
        itemlist.append( item )
    else:   # for backward compatitbility with v1.0.7 favorites
        itemlist=previous_play( item )
    return itemlist

def calculate_url(video_url):
    #video_url2 = scrapertools.get_match(json_decoded,'"worldtour_path"\:"([^"]+)"')
    #logger.info("video_url2="+video_url2)
    #video_url = "rtmp://video2.earthcam.com/fecnetwork/hdtimes11.flv"
    #./rtmpdump-2.4 -r "rtmp://video2.earthcam.com/fecnetwork/4828.flv" --swfVfy "http://www.earthcam.com/swf/cam_player_v2/ecnPlayer.swf?20121010" --pageUrl "http://www.earthcam.com/world/turkey/istanbul/" --tcUrl "rtmp://video2.earthcam.com/fecnetwork" --app fecnetwork --live --playpath "4828.flv" -o out.flv
    # Taken from http://forum.xbmc.org/archive/index.php/thread-120418-20.html
    # rtmp://video2.earthcam.com/ app=fecnetwork swfUrl=http://www.earthcam.com/swf/cam_player_v2/ecnPlayer.swf playpath=fridaysHD1.flv live=true timeout=180
    if video_url.lower().endswith(".jpg") or video_url.lower().endswith(".png"):
        url = video_url
    elif video_url.lower().startswith("http://") or video_url.lower().endswith(".mp4"):
        url = video_url
    else:
        rtmp_url = scrapertools.get_match(video_url,"(rtmp\://[^\/]+/)")
        app = scrapertools.get_match(video_url,"rtmp\://[^\/]+/([a-z]+)/")
        ###playpath = scrapertools.get_match(video_url,"rtmp\://[^\/]+/[a-z]+/([a-zA-Z0-9]+\.flv)")
        playpath = scrapertools.get_match(video_url,"rtmp\://[^\/]+/[a-z]+/(.+\.flv)")
        swfurl = "http://www.earthcam.com/swf/cam_player_v2/ecnPlayer.swf"
        url=rtmp_url + " app=" + app + " swfUrl=" + swfurl + " playpath=" + playpath + " live=true timeout=180"
    logger.info("url="+url)
    return url


def load_json(data):
    # callback to transform json string values to utf8
    def to_utf8(dct):
        rdct = {}
        for k, v in dct.items() :
            if isinstance(v, (str, unicode)) :
                rdct[k] = v.encode('utf8', 'ignore')
            else :
                rdct[k] = v
        return rdct
    try :        
        import json
        json_data = json.loads(data, object_hook=to_utf8)
        return json_data
    except:
        import sys
        for line in sys.exc_info():
            logger.error( "%s" % line ) 
