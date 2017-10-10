"""
XBMCLocalProxy 0.1
Copyright 2011 Torben Gerkensmeyer

Modified by Long Hong for Proxy server streaming.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""

import base64
import re
import urlparse
import sys
import traceback
import socket
import random
import SocketServer
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from livestreamer import Livestreamer, StreamError, PluginError, NoPluginError
from common import ShowMessage, infoDialog, Paths
import pyperclip
import xbmcaddon
from xbmcgui import ListItem
from xbmc import executebuiltin, Player
import urllib

myDebugPath = Paths.pluginDataDir
streamer_buf = myDebugPath + "streamer_buf.txt"

settings = xbmcaddon.Addon(id='plugin.video.Pac-12')
hostName = str(settings.getSetting(id="ipaddress"))
portNumber = str(settings.getSetting(id="portNumber"))

def onetv_decrypt(playpath):
    import random,time,md5
    from base64 import b64encode
    infoDialog('Process onetv decrypt..', '[COLOR blue]Kodi Local Proxy[/COLOR]')
    user_agent = 'Mozilla%2F5.0%20%28Linux%3B%20Android%205.1.1%3B%20Nexus%205%20Build%2FLMY48B%3B%20wv%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Version%2F4.0%20Chrome%2F43.0.2357.65%20Mobile%20Safari%2F537.36'
    token = "65rSw"+"UzRad"
    servers = ['185.102.219.67', '185.102.219.72', '185.102.218.56']
    time_stamp = str(int(time.time()) + 144000)
    to_hash = "{0}{1}/hls/{2}".format(token,time_stamp,playpath)
    out_hash = b64encode(md5.new(to_hash).digest()).replace("+", "-").replace("/", "_").replace("=", "")
    server = random.choice(servers);    
    url = "hls://http://{0}/p2p/{1}?st={2}&e={3}".format(server,playpath,out_hash,time_stamp)
    new_playpath = '{url}|User-Agent={user_agent}&referer={referer}'.format(url=url,user_agent=user_agent,referer='6d6f6264726f2e6d65'.decode('hex'))
    new_playpath = base64.b64encode(new_playpath)
    return new_playpath

s = [   '185.39.11.42',
        '185.39.9.34',
        '185.39.9.130',
        '185.39.11.50',
        '185.39.11.34',
        '185.39.9.2',
        '185.39.11.10',
        '185.39.11.26',
        '185.39.9.98',
        '185.39.9.162',
        '185.39.11.2',
        '185.39.11.58',
        '185.39.11.66']

class MyHandler(BaseHTTPRequestHandler):
    """
    Serves a HEAD request
    """
    def do_HEAD(self):
        self.answer_request(0)

    """
    Serves a GET request.
    """
    def do_GET(self):
        self.answer_request(1)

    def answer_request(self, sendData):
        try:
            request_path = self.path[1:]
            urllib.quote_plus(request_path)
            extensions = ['.Vprj', '.edl', '.txt', '.chapters.xml']
            for extension in extensions:
                if request_path.endswith(extension):
                    self.send_response(404)
                    request_path = ''      
            request_path = re.sub(r"\?.*", "", request_path)
            if request_path == "stop":
                infoDialog('request Stopping ...', 'Server Stop', time=1000)
                xbmc.sleep(5)
                sys.exit()
            elif request_path == "version":
                infoDialog('msg version ...', 'Check version', time=1000)
                self.send_response(200)
                self.end_headers()
                self.wfile.write("Livestreamer Proxy: Running - Pac-12 Network\r\n")
                self.wfile.write("Version: 0.1")
            elif request_path[0:13] == "livestreamer/":
                infoDialog('Process livestreamer', '[COLOR aqua]answer_request[/COLOR]', time=3000)
                realpath = request_path[13:]
                infoDialog('process decrypting..', 'onetv decrypt', time=1000)
                if "hls://" not in base64.b64decode(realpath):
					realpath = onetv_decrypt(realpath)
                infoDialog('process sendData..', 'streamer service', time=1000)
                fURL = base64.b64decode(realpath)
                self.serveFile(fURL, sendData)
                infoDialog('[COLOR lime]Done sendData..ready streamer[/COLOR]', 'sendData', time=1000)
            elif request_path[0:13] == "youtubevideo/" or request_path[0:13] == "vodstreamers/" or request_path[0:13] == "f4mstreamers/": 
                infoDialog('Process Video streamers', '[COLOR aqua]answer_request[/COLOR]', time=3000)
                url = self.path[14:]
                urllib.quote_plus(url)
                listitem = ListItem(path=url)
                listitem.setInfo(type="Video", infoLabels={"mediatype": "movie", "title": "LiveTV_VOD"})
                Player().play(url, listitem)
                return
            else:
                self.send_response(403)
        except:
                traceback.print_exc()
                self.wfile.close()
                return
        try:
            self.wfile.close()
        except:
            pass

            
    """
    Sends the requested file and add additional headers.
    """
    def serveFile(self, fURL, sendData):
        session = Livestreamer()
        if '|' in fURL:
                sp = fURL.split('|')
                fURL = sp[0]
                headers = dict(urlparse.parse_qsl(sp[1]))
                if 'cdn.sstream.pw' in fURL:
                    fURL = fURL.replace('cdn.sstream.pw',random.choice(s))
                    headers['Host'] = '6b6473616a6b6c647361646a7361643737353637647361393973616768647368686464732e736974656e6f772e6d65'.decode('hex')
                session.set_option("http-headers", headers)
                session.set_option("http-ssl-verify",False)
                session.set_option("hls-segment-threads",3)
        try:
            streams = session.streams(fURL)
        except:
            traceback.print_exc(file=sys.stdout)
            self.send_response(403)
        self.send_response(200)
        self.end_headers()
        
        if (sendData):
            fileout = self.wfile
            try:
                stream = streams["best"]
                try:
                    response = stream.open()
                    buf = 'INIT'
                    while (buf != None and len(buf) > 0):
                        buf = response.read(200 * 1024)
                        fileout.write(buf)
                        fileout.flush()
                    response.close()
                    fileout.close()
                except socket.error, e:
                    try:
                        response.close()
                        fileout.close()
                    except Exception, e:
                        return
                except Exception, e:
                    traceback.print_exc(file=sys.stdout)
                    response.close()
                    fileout.close()
            except:
                traceback.print_exc()
                self.wfile.close()
                return
        try:
            self.wfile.close()
        except:
            pass


class Server(HTTPServer):
    """HTTPServer class with timeout."""

    def get_request(self):
        """Get the request and client address from the socket."""
        self.socket.settimeout(5.0)
        result = None
        while result is None:
            try:
                result = self.socket.accept()
            except socket.timeout:
                pass
        result[0].settimeout(1000)
        return result

class ThreadedHTTPServer(ThreadingMixIn, Server):
    """Handle requests in a separate thread."""

class SimpleServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)	
	
HOST_NAME = '127.0.0.1'
PORT_NUMBER = 19098

def start_proxy_server():
    socket.setdefaulttimeout(10)
    try:
        httpd = SimpleServer((HOST_NAME, PORT_NUMBER), MyHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        if httpd != None:
			httpd.socket.close()


if __name__ == '__main__':
	start_proxy_server()
