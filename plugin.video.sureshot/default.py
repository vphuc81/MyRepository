#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64,ftplib,json,urllib,urllib2,urlparse,os,re,sys,zipfile
import xbmc,xbmcaddon,xbmcplugin,xbmcgui

from shutil import copyfile
from collections import defaultdict

dialog = xbmcgui.Dialog()
dp = xbmcgui.DialogProgress()
Config = xbmcaddon.Addon()


### FILES ###

path = os.path.join(xbmcaddon.Addon().getAddonInfo('path'))

output_old = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot/resources/database', 'output_old.xml'))
output_new = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot/resources/database', 'output_new.xml'))
source_old = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot/resources/database', 'lastdatabase.txt'))
source_new = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot/resources/database', 'lastdatabase_new.txt'))
output = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot/resources/database', 'output.xml'))
background = xbmc.translatePath(os.path.join('special://home/addons/plugin.video.sureshot', 'fanart.jpg'))

outputfile = output_new, output_old


### CHECK REPO ###

def ExtractAll(_in, _out):
    try:
        zin = zipfile.ZipFile(_in, 'r')
        zin.extractall(_out)
    except Exception, e:
        print str(e)
        return False

    return True
    

def UpdateRepo():
    if os.path.exists(os.path.join(xbmc.translatePath("special://home/addons/").decode("utf-8"), 'repository.docshadrach')):
        return
        
    url = "https://github.com/XBMCSpot/docshadrach.repository/raw/master/zips/repository.docshadrach-1.0.zip"
    addonsDir = xbmc.translatePath(os.path.join('special://home', 'addons')).decode("utf-8")
    packageFile = os.path.join(addonsDir, 'packages', 'isr.zip')
    
    urllib.urlretrieve(url, packageFile)
    ExtractAll(packageFile, addonsDir)
        
    try:
        os.remove(packageFile)
    except:
        pass
            
    xbmc.executebuiltin("UpdateLocalAddons")
    xbmc.executebuiltin("UpdateAddonRepos")


UpdateRepo()


### CHECK FILTERS ###

def get_watchlist(user):

    try:
    
        url = 'http://rss.imdb.com/user/' + user + '/watchlist'
    
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()

        match=re.compile('<link>http://www.imdb.com/title/(.*)/</link>').findall(link)

        return match
    except: pass


def wl_filter():

    if Config.getSetting("imdbwl") == 'true':
        imdbuser = Config.getSetting("imdbuser")
        watchlist = get_watchlist(imdbuser)
    else:
        watchlist = ""

    if watchlist == None:
        dialog.ok('ERROR', 'Invalid IMDb user. Please, enter a valid one.')           
        Config.openSettings()
        sys.exit()
    else: pass

    return watchlist


def filters():

    if Config.getSetting("Action") == 'true':
        tag1 = "Action"
    else:
        tag1 = ""
        

    if Config.getSetting("Adventure") == 'true':
        tag2 = "Adventure"
    else:
        tag2 = ""
        
        
    if Config.getSetting("Animation") == 'true':
        tag3 = "Animation"
    else:
        tag3 = ""
        
        
    if Config.getSetting("Biography") == 'true':
        tag4 = "Biography"
    else:
        tag4 = ""


    if Config.getSetting("Comedy") == 'true':
        tag5 = "Comedy"
    else:
        tag5 = ""
        
        
    if Config.getSetting("Crime") == 'true':
        tag6 = "Crime"
    else:
        tag6 = ""


    if Config.getSetting("Documentary") == 'true':
        tag7 = "Documentary"
    else:
        tag7 = ""
        
        
    if Config.getSetting("Drama") == 'true':
        tag8 = "Drama"
    else:
        tag8 = ""
        
        
    if Config.getSetting("Family") == 'true':
        tag9 = "Family"
    else:
        tag9 = ""
        

    if Config.getSetting("Fantasy") == 'true':
        tag10 = "Fantasy"
    else:
        tag10 = ""
        
        
    if Config.getSetting("History") == 'true':
        tag11 = "History"
    else:
        tag11 = ""


    if Config.getSetting("Horror") == 'true':
        tag12 = "Horror"
    else:
        tag12 = ""
        
        
    if Config.getSetting("Musical") == 'true':
        tag13 = "Musical"
    else:
        tag13 = ""
        
        
    if Config.getSetting("Mystery") == 'true':
        tag14 = "Mystery"
    else:
        tag14 = ""


    if Config.getSetting("Romance") == 'true':
        tag15 = "Romance"
    else:
        tag15 = ""
        
    
    if Config.getSetting("Sci-Fi") == 'true':
        tag16 = "Sci-Fi"
    else:
        tag16 = ""
        
        
    if Config.getSetting("Sport") == 'true':
        tag17 = "Sport"
    else:
        tag17 = ""
        
        
    if Config.getSetting("Thriller") == 'true':
        tag18 = "Thriller"
    else:
        tag18 = ""


    if Config.getSetting("War") == 'true':
        tag19 = "War"
    else:
        tag19 = ""
        
    
    if Config.getSetting("Western") == 'true':
        tag20 = "Western"
    else:
        tag20 = ""
        
        
    alltags = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,tag11,tag12,tag13,tag14,tag15,tag16,tag17,tag18,tag19,tag20]
    
    tags = filter(None, alltags)

    if Config.getSetting("enable_tags") == 'false': tags = []
    else: pass

    return tags


def get_status():

    if Config.getSetting("imdbwl") == 'true':
        status1 = "\n- [COLOR gold]Watchlist filter is [B]ON[/B][/COLOR]"
    else:
        status1 = ""
    
    if Config.getSetting("enable_tags") == 'true':
        status2 = "\n- [COLOR red]Genre filter is [B]ON[/B][/COLOR]"
    else:
        status2 = ""

    if status1 + status2 == "":
        status = '\n\n\n\n\n\n\n[COLOR gray][B]REMEMBER:[/B]\nYou can set filters in\nthe "[B]Add-on settings[/B]".[/COLOR]'
    else:
        status = "\n\n\n\n\n\n\n[COLOR gray][B]REMINDER:[/B][/COLOR]" + status1 + status2

    return status
    

### UPDATING DATABASE ###

def verify_lastupdate(url):

    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link = response.read(2000)
    response.close()

    block = re.split(r'</td></tr>', link)
    lastupdate = re.findall('<td><.*<td>(.............*)', block[3])

    return lastupdate


def verify_localupdate(file, index):

    archivo = open(file, "r+")
    contenido = archivo.read()

    block = re.split(r'</td></tr>', contenido)
    lastupdate = re.findall('<td><.*<td>(.............*)', block[index])

    return lastupdate


def get_fanart(id):

    try:

        url = "http://api.themoviedb.org/3/movie/" +id+ "/images?api_key=4be68d7eab1fbd1b6fd8a3b80a65a95e"

        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link = response.read()
        response.close()

        data = json.loads(link)

        fanart = data["backdrops"]

        return "https://image.tmdb.org/t/p/original" + str(fanart[0]['file_path'])

    except: pass
    

def update_output(lastday):

    fs = open(source_new,"w+")
    urllib.urlretrieve (base64.urlsafe_b64decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3JlemEvZmlsbS8/Qz1NJk89RA=='), source_new)
    fs.close()

    output = output_new
    f = open(output,"w+")

    LISTADEPELIS = []

    archivo = open(source_new, "r+")
    contenido = archivo.read()


    match = re.compile('(<title>Index of /reza/film/</title>.+?)' + lastday, re.DOTALL).findall(contenido)
    
    if match == []:

        lastday = local_database = verify_localupdate(source_old,4)

        match = re.compile('(<title>Index of /reza/film/</title>.+?)' + lastday[0], re.DOTALL).findall(contenido)

        if match == []:

            lastday = local_database = verify_localupdate(source_old,5)

            match = re.compile('(<title>Index of /reza/film/</title>.+?)' + lastday[0], re.DOTALL).findall(contenido)

            if match == []:

                lastday = local_database = verify_localupdate(source_old,6)

                match = re.compile('(<title>Index of /reza/film/</title>.+?)' + lastday[0], re.DOTALL).findall(contenido)

                if match == []:

                    lastday = local_database = verify_localupdate(source_old,15)

                    match = re.compile('(<title>Index of /reza/film/</title>.+?)' + lastday[0], re.DOTALL).findall(contenido)

    else: pass

    block = re.split(r'</td></tr>', match[0])

    total = int(len(block)) - 4

    percent = 100 / total

    lastblock = int(len(block)) - 2


    for i in range(3,int(len(block)) - 2):

        try:

            filename = re.findall('<tr><td><a href="(.*?)">', block[i])

            moviename = re.findall('(.*).201[0-7]', filename[0])

            movienam = str(moviename[0]).replace('.', '+')

            movieyear = re.findall('.*(201[0-7])', filename[0])

            toimdb = "http://www.omdbapi.com/?t=" + movienam + "&y=" + movieyear[0]

            LISTADEPELIS.append(toimdb)

        except: pass


    CLEANLIST = []
    
    for i in LISTADEPELIS:
        if i not in CLEANLIST:
            CLEANLIST.append(i)


    for i in CLEANLIST:

        try:

            url = i

            req = urllib2.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            response = urllib2.urlopen(req)
            link = response.read()
            response.close()

            data = json.loads(link)

            rating = data["imdbRating"]

            rated = rating[:1]

            if int(rated) >= 7 and data["Country"] != "India":
                name = str(data["Title"])
                fixednam = name.replace(':', '')
                fixedname = fixednam.replace(' ', '.') + "." + str(data["Year"])
                pattern1 = re.compile(fixedname + '(.*mkv)"',flags=re.IGNORECASE)
                pattern2 = re.compile(fixedname + '(.*mp4)"',flags=re.IGNORECASE)
                pattern3 = re.compile(fixedname + '(.*avi)"',flags=re.IGNORECASE)
                image = str(data["Poster"])
                imdbid = str(data["imdbID"])
                category = str(data["Genre"])
                f.write("\n<item>\n<id>" +imdbid +"</id>\n")
                f.write("<title>" +name +"</title>\n")
                f.write("<thumbnail>" +image +"</thumbnail>\n")
                f.write("<fanart>" +str(get_fanart(imdbid)) +"</fanart>\n")
                f.write("<category>" +category +"</category>\n")

                MULTILINK = []

                try:
                    for i, line in enumerate(open(source_new)):
                        for match in re.finditer(pattern1, line):
                            urls = match.group(0)
                            multi = MULTILINK.append(urls.replace(('"'),('')))
                        for match in re.finditer(pattern2, line):
                            urls = match.group(0)
                            multi = MULTILINK.append(urls.replace(('"'),('')))
                        for match in re.finditer(pattern3, line):
                            urls = match.group(0)
                            multi = MULTILINK.append(urls.replace(('"'),('')))
                except: pass
                
                if len(MULTILINK) > 1:
                    f.write("<link>" +str(MULTILINK) +"</link>\n</item>\n")
                    print MULTILINK
                elif len(MULTILINK) == 1:
                    f.write("<link>" +MULTILINK[0] +"</link>\n</item>\n")
                    print MULTILINK[0]
                else:
                    f.write("<link>" + "NO LINK" +"</link>\n</item>\n")                    
                    print name + " ------------ no link ---------------- "
                
            else:pass

        except: pass

        dp.update(percent)
        xbmc.sleep(500)
        percent = percent + percent
        
    dp.update(100)
    dp.close()
    f.close()
    print "DONE"


def merge_files():
    
    copyfile(output, output_old)
    with open(output, 'w') as outfile:
        for fname in outputfile:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)


def updater_trigger():

    local_database = verify_localupdate(source_old,3)

    source_database = verify_lastupdate(base64.urlsafe_b64decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3JlemEvZmlsbS8/Qz1NJk89RA=='))

    if local_database != source_database:

        dp.create('Updating database','Please wait...')
        dp.update(0)
        xbmc.sleep(500)

        update_output(local_database[0]), merge_files()
        
        copyfile(source_new, source_old)

    else:

        pass


### HANDLES ###

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)


### XML PARSERS ###

def item_block(source, pattern):    
    matches = re.findall(pattern, source, re.DOTALL)

    return matches
    
def item_element(source, pattern):
    result = ""

    try:    
        matches = re.findall(pattern, source, flags=re.DOTALL)
        result = matches[0]
    except:
        result = ""

    return result


### FINDING DUPLICATES ###

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items() 
                            if len(locs)>1)


### PARSING AND DELETING DUPLICATE INFO ###

def listing():
    
    NAME_LIST = []
    THUMB_LIST = []
    FANART_LIST = []
    LINK_LIST = []
    ID_LIST = []
    CATEGORY_LIST = []
    
    opciones = open(output, "r+")
    contenido = opciones.read()

    matches = item_block(contenido, "<item>(.*?)</item>")
    
    for item in matches:
        NAME = item_element(item, "<title>(.*?)</title>")
        THUMB = item_element(item, "<thumbnail>(.*?)</thumbnail>")
        FANART = item_element(item, "<fanart>(.*?)</fanart>")
        LINK = item_element(item, "<link>(.*?)</link>")
        ID = item_element(item, "<id>(.*?)</id>")
        CATEGORY = item_element(item, "<category>(.*?)</category>")
        
        NAME_LIST.append(NAME)
        THUMB_LIST.append(THUMB)
        FANART_LIST.append(FANART)
        LINK_LIST.append(LINK)
        ID_LIST.append(ID)
        CATEGORY_LIST.append(CATEGORY)


    DUPLICATES = []

    for dup in sorted(list_duplicates(ID_LIST)):
        DUPLICATES.append(dup[1])


    SECONDELEM = [item[1] for item in DUPLICATES]
    RESTANTES = []
    
    for i in range(int(len(DUPLICATES))):
        if int(len(DUPLICATES[i])) > 2:
            DUPLICATES[i].pop(0)
            EXTRAELEMENTS = (set(DUPLICATES[i]).difference(SECONDELEM))
            EXTRA = list(EXTRAELEMENTS)

            for i in EXTRA:
                RESTANTES.append(i)
        else:
            pass
            
    REPETIDAS = SECONDELEM + RESTANTES

    for element in REPETIDAS:

        NAME_LIST[element] = ""
        THUMB_LIST[element] = ""
        FANART_LIST[element] = ""
        LINK_LIST[element] = ""
        ID_LIST[element] = ""
        CATEGORY_LIST[element] = ""

    return NAME_LIST,THUMB_LIST,FANART_LIST,LINK_LIST,ID_LIST,CATEGORY_LIST


### RUNNING ###

updater_trigger()
  

if mode is None:

    index = 0

    NAME_LIST,THUMB_LIST,FANART_LIST,LINK_LIST,ID_LIST,CATEGORY_LIST = listing()

    watchlist = wl_filter()
    if watchlist == "":
        watchlist = ID_LIST

    
    for i in range(0,len(NAME_LIST)):

        if LINK_LIST[index]!= "NO LINK" and LINK_LIST[index]!= "" and all(ext in CATEGORY_LIST[index] for ext in filters()) == True and any(elm in ID_LIST[index] for elm in watchlist) == True: 
            url = build_url({'mode': 'folder', 'foldername': NAME_LIST[index]})
            li = xbmcgui.ListItem(str(NAME_LIST[index]), iconImage=THUMB_LIST[index])
            li.setProperty('fanart_image',background)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url,
                                        listitem=li, isFolder=True)

        else: pass
        index = index + 1

    xbmc.executebuiltin('Container.SetViewMode(500)')
    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':

    NAME_LIST,THUMB_LIST,FANART_LIST,LINK_LIST,ID_LIST,CATEGORY_LIST = listing()
    
    foldername = args['foldername'][0]
    index = NAME_LIST.index(foldername)

    if Config.getSetting("reminder") == 'true':
        status = get_status()
    else:
        status = ""
    
    if LINK_LIST[index].startswith('[') == True:
        MULTILINK = re.compile('\'(.*?[v,i,4])\'').findall(LINK_LIST[index])
        ind = 0
        for link in MULTILINK:
            url = base64.urlsafe_b64decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3JlemEvZmlsbS8=') + str(link)
            li = xbmcgui.ListItem(str(MULTILINK[ind]), iconImage=THUMB_LIST[index])
            li.setInfo(type="Video", infoLabels={"plot": "\n\nGenre:\n\n" + str(CATEGORY_LIST[index]) + status})
            li.setProperty('fanart_image',str(FANART_LIST[index]))
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
            ind = ind + 1
        xbmc.executebuiltin('Container.SetViewMode(503)')
        xbmcplugin.endOfDirectory(addon_handle)

    else:
        url = base64.urlsafe_b64decode('aHR0cDovL2RsLm15LWZpbG0ub3JnL3JlemEvZmlsbS8=') + str(LINK_LIST[index])
        li = xbmcgui.ListItem(str(LINK_LIST[index]), iconImage=THUMB_LIST[index])
        li.setInfo(type="Video", infoLabels={"plot": "\n\nGenre:\n\n" + str(CATEGORY_LIST[index]) + status})
        li.setProperty('fanart_image',str(FANART_LIST[index]))
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
        xbmc.executebuiltin('Container.SetViewMode(503)')
        xbmcplugin.endOfDirectory(addon_handle)


### END ###

