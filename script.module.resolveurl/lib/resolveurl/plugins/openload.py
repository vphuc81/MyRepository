# -*- coding: utf-8 -*-
"""
openload.io resolveurl plugin
Copyright (C) 2015 tknorris

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import base64
import re
import json
from lib import helpers
from resolveurl import common
from resolveurl.common import i18n
from resolveurl.resolver import ResolveUrl, ResolverError
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf8')

logger = common.log_utils.Logger.get_logger(__name__)
logger.disable()

API_BASE_URL = 'https://api.openload.co/1'
INFO_URL = API_BASE_URL + '/streaming/info'
GET_URL = API_BASE_URL + '/streaming/get?file={media_id}'
FILE_URL = API_BASE_URL + '/file/info?file={media_id}'

class OpenLoadResolver(ResolveUrl):
    name = "openload"
    domains = ["openload.io", "openload.co", "oload.tv", "oload.stream", "oload.win", "oload.download", "oload.info", "oload.icu", "oload.fun", "openload.pw"]
    pattern = '(?://|\.)(o(?:pen)??load\.(?:io|co|tv|stream|win|download|info|icu|fun|pw))/(?:embed|f)/([0-9a-zA-Z-_]+)'

    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        try:
            if not self.__file_exists(media_id):
                raise ResolverError('File Not Available')
            try:
                url = "https://openload.co/embed/"+str(media_id)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}
                data = requests.get(url, headers=headers).content
                marker = 'ﾟωﾟﾉ= /｀ｍ´）ﾉ'
                orgData = str(data)
                orgData = re.search("""ﾟωﾟﾉ= \/｀ｍ´）ﾉ(.*?}\);)""", orgData)
                try:
                    orgData = marker + orgData.group(1)
                except:
                    return
                orgData = orgData.replace("]='\\'; (", "]='\\\\'; (")
                orgData = re.sub('''if\s*\([^\}]+?typeof[^\}]+?\}''', '', orgData)
                orgData = re.sub('''if\s*\([^\}]+?document[^\}]+?\}''', '', orgData)

                encTab = re.search("""<p.*id="(.*)">(.*?)<\/p>""", data)
                encTab = encTab.group(2)

                for e in encTab:
                    if len(e) > 40:
                        encTab.insert(0, e)
                        break

                jscode = base64.b64decode(
                    '''ICAgICAgICAgICAgICAgICAgICB2YXIgaWQgPSAiJXMiDQogICAgICAgICAgICAgICAgICAgICAgLCBkZWNvZGVkDQogICAgICAgICAgICAgICAgICAgICAgLCBkb2N1bWVudCA9IHt9DQogICAgICAgICAgICAgICAgICAgICAgLCB3aW5kb3cgPSB0aGlzDQogICAgICAgICAgICAgICAgICAgICAgLCAkID0gZnVuY3Rpb24oKXsNCiAgICAgICAgICAgICAgICAgICAgICAgICAgcmV0dXJuIHsNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICB0ZXh0OiBmdW5jdGlvbihhKXsNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmKGEpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRlY29kZWQgPSBhOw0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZWxzZQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICByZXR1cm4gaWQ7DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgfSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICByZWFkeTogZnVuY3Rpb24oYSl7DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhKCkNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9DQogICAgICAgICAgICAgICAgICAgICAgICAgIH0NCiAgICAgICAgICAgICAgICAgICAgICAgIH07DQogICAgICAgICAgICAgICAgICAgIChmdW5jdGlvbihkLCB3KXsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgZiA9IGZ1bmN0aW9uKCl7fTsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgcyA9ICcnOw0KICAgICAgICAgICAgICAgICAgICAgIHZhciBvID0gbnVsbDsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgYiA9IGZhbHNlOw0KICAgICAgICAgICAgICAgICAgICAgIHZhciBuID0gMDsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgZGYgPSBbJ2Nsb3NlJywnY3JlYXRlQXR0cmlidXRlJywnY3JlYXRlRG9jdW1lbnRGcmFnbWVudCcsJ2NyZWF0ZUVsZW1lbnQnLCdjcmVhdGVFbGVtZW50TlMnLCdjcmVhdGVFdmVudCcsJ2NyZWF0ZU5TUmVzb2x2ZXInLCdjcmVhdGVSYW5nZScsJ2NyZWF0ZVRleHROb2RlJywnY3JlYXRlVHJlZVdhbGtlcicsJ2V2YWx1YXRlJywnZXhlY0NvbW1hbmQnLCdnZXRFbGVtZW50QnlJZCcsJ2dldEVsZW1lbnRzQnlOYW1lJywnZ2V0RWxlbWVudHNCeVRhZ05hbWUnLCdpbXBvcnROb2RlJywnb3BlbicsJ3F1ZXJ5Q29tbWFuZEVuYWJsZWQnLCdxdWVyeUNvbW1hbmRJbmRldGVybScsJ3F1ZXJ5Q29tbWFuZFN0YXRlJywncXVlcnlDb21tYW5kVmFsdWUnLCd3cml0ZScsJ3dyaXRlbG4nXTsNCiAgICAgICAgICAgICAgICAgICAgICBkZi5mb3JFYWNoKGZ1bmN0aW9uKGUpe2RbZV09Zjt9KTsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgZG9fID0gWydhbmNob3JzJywnYXBwbGV0cycsJ2JvZHknLCdkZWZhdWx0VmlldycsJ2RvY3R5cGUnLCdkb2N1bWVudEVsZW1lbnQnLCdlbWJlZHMnLCdmaXJzdENoaWxkJywnZm9ybXMnLCdpbWFnZXMnLCdpbXBsZW1lbnRhdGlvbicsJ2xpbmtzJywnbG9jYXRpb24nLCdwbHVnaW5zJywnc3R5bGVTaGVldHMnXTsNCiAgICAgICAgICAgICAgICAgICAgICBkb18uZm9yRWFjaChmdW5jdGlvbihlKXtkW2VdPW87fSk7DQogICAgICAgICAgICAgICAgICAgICAgdmFyIGRzID0gWydVUkwnLCdjaGFyYWN0ZXJTZXQnLCdjb21wYXRNb2RlJywnY29udGVudFR5cGUnLCdjb29raWUnLCdkZXNpZ25Nb2RlJywnZG9tYWluJywnbGFzdE1vZGlmaWVkJywncmVmZXJyZXInLCd0aXRsZSddOw0KICAgICAgICAgICAgICAgICAgICAgIGRzLmZvckVhY2goZnVuY3Rpb24oZSl7ZFtlXT1zO30pOw0KICAgICAgICAgICAgICAgICAgICAgIHZhciB3YiA9IFsnY2xvc2VkJywnaXNTZWN1cmVDb250ZXh0J107DQogICAgICAgICAgICAgICAgICAgICAgd2IuZm9yRWFjaChmdW5jdGlvbihlKXt3W2VdPWI7fSk7DQogICAgICAgICAgICAgICAgICAgICAgdmFyIHdmID0gWydhZGRFdmVudExpc3RlbmVyJywnYWxlcnQnLCdhdG9iJywnYmx1cicsJ2J0b2EnLCdjYW5jZWxBbmltYXRpb25GcmFtZScsJ2NhcHR1cmVFdmVudHMnLCdjbGVhckludGVydmFsJywnY2xlYXJUaW1lb3V0JywnY2xvc2UnLCdjb25maXJtJywnY3JlYXRlSW1hZ2VCaXRtYXAnLCdkaXNwYXRjaEV2ZW50JywnZmV0Y2gnLCdmaW5kJywnZm9jdXMnLCdnZXRDb21wdXRlZFN0eWxlJywnZ2V0U2VsZWN0aW9uJywnbWF0Y2hNZWRpYScsJ21vdmVCeScsJ21vdmVUbycsJ29wZW4nLCdwb3N0TWVzc2FnZScsJ3Byb21wdCcsJ3JlbGVhc2VFdmVudHMnLCdyZW1vdmVFdmVudExpc3RlbmVyJywncmVxdWVzdEFuaW1hdGlvbkZyYW1lJywncmVzaXplQnknLCdyZXNpemVUbycsJ3Njcm9sbCcsJ3Njcm9sbEJ5Jywnc2Nyb2xsVG8nLCdzZXRJbnRlcnZhbCcsJ3NldFRpbWVvdXQnLCdzdG9wJ107DQogICAgICAgICAgICAgICAgICAgICAgd2YuZm9yRWFjaChmdW5jdGlvbihlKXt3W2VdPWY7fSk7DQogICAgICAgICAgICAgICAgICAgICAgdmFyIHduID0gWydkZXZpY2VQaXhlbFJhdGlvJywnaW5uZXJIZWlnaHQnLCdpbm5lcldpZHRoJywnbGVuZ3RoJywnb3V0ZXJIZWlnaHQnLCdvdXRlcldpZHRoJywncGFnZVhPZmZzZXQnLCdwYWdlWU9mZnNldCcsJ3NjcmVlblgnLCdzY3JlZW5ZJywnc2Nyb2xsWCcsJ3Njcm9sbFknXTsNCiAgICAgICAgICAgICAgICAgICAgICB3bi5mb3JFYWNoKGZ1bmN0aW9uKGUpe3dbZV09bjt9KTsNCiAgICAgICAgICAgICAgICAgICAgICB2YXIgd28gPSBbJ2FwcGxpY2F0aW9uQ2FjaGUnLCdjYWNoZXMnLCdjcnlwdG8nLCdleHRlcm5hbCcsJ2ZyYW1lRWxlbWVudCcsJ2ZyYW1lcycsJ2hpc3RvcnknLCdpbmRleGVkREInLCdsb2NhbFN0b3JhZ2UnLCdsb2NhdGlvbicsJ2xvY2F0aW9uYmFyJywnbWVudWJhcicsJ25hdmlnYXRvcicsJ29uYWJvcnQnLCdvbmFuaW1hdGlvbmVuZCcsJ29uYW5pbWF0aW9uaXRlcmF0aW9uJywnb25hbmltYXRpb25zdGFydCcsJ29uYmVmb3JldW5sb2FkJywnb25ibHVyJywnb25jYW5wbGF5Jywnb25jYW5wbGF5dGhyb3VnaCcsJ29uY2hhbmdlJywnb25jbGljaycsJ29uY29udGV4dG1lbnUnLCdvbmRibGNsaWNrJywnb25kZXZpY2Vtb3Rpb24nLCdvbmRldmljZW9yaWVudGF0aW9uJywnb25kcmFnJywnb25kcmFnZW5kJywnb25kcmFnZW50ZXInLCdvbmRyYWdsZWF2ZScsJ29uZHJhZ292ZXInLCdvbmRyYWdzdGFydCcsJ29uZHJvcCcsJ29uZHVyYXRpb25jaGFuZ2UnLCdvbmVtcHRpZWQnLCdvbmVuZGVkJywnb25lcnJvcicsJ29uZm9jdXMnLCdvbmhhc2hjaGFuZ2UnLCdvbmlucHV0Jywnb25pbnZhbGlkJywnb25rZXlkb3duJywnb25rZXlwcmVzcycsJ29ua2V5dXAnLCdvbmxhbmd1YWdlY2hhbmdlJywnb25sb2FkJywnb25sb2FkZWRkYXRhJywnb25sb2FkZWRtZXRhZGF0YScsJ29ubG9hZHN0YXJ0Jywnb25tZXNzYWdlJywnb25tb3VzZWRvd24nLCdvbm1vdXNlZW50ZXInLCdvbm1vdXNlbGVhdmUnLCdvbm1vdXNlbW92ZScsJ29ubW91c2VvdXQnLCdvbm1vdXNlb3ZlcicsJ29ubW91c2V1cCcsJ29ub2ZmbGluZScsJ29ub25saW5lJywnb25wYWdlaGlkZScsJ29ucGFnZXNob3cnLCdvbnBhdXNlJywnb25wbGF5Jywnb25wbGF5aW5nJywnb25wb3BzdGF0ZScsJ29ucHJvZ3Jlc3MnLCdvbnJhdGVjaGFuZ2UnLCdvbnJlc2V0Jywnb25yZXNpemUnLCdvbnNjcm9sbCcsJ29uc2Vla2VkJywnb25zZWVraW5nJywnb25zZWxlY3QnLCdvbnNob3cnLCdvbnN0YWxsZWQnLCdvbnN0b3JhZ2UnLCdvbnN1Ym1pdCcsJ29uc3VzcGVuZCcsJ29udGltZXVwZGF0ZScsJ29udG9nZ2xlJywnb250cmFuc2l0aW9uZW5kJywnb251bmxvYWQnLCdvbnZvbHVtZWNoYW5nZScsJ29ud2FpdGluZycsJ29ud2Via2l0YW5pbWF0aW9uZW5kJywnb253ZWJraXRhbmltYXRpb25pdGVyYXRpb24nLCdvbndlYmtpdGFuaW1hdGlvbnN0YXJ0Jywnb253ZWJraXR0cmFuc2l0aW9uZW5kJywnb253aGVlbCcsJ29wZW5lcicsJ3BhcmVudCcsJ3BlcmZvcm1hbmNlJywncGVyc29uYWxiYXInLCdzY3JlZW4nLCdzY3JvbGxiYXJzJywnc2VsZicsJ3Nlc3Npb25TdG9yYWdlJywnc3BlZWNoU3ludGhlc2lzJywnc3RhdHVzYmFyJywndG9vbGJhcicsJ3RvcCddOw0KICAgICAgICAgICAgICAgICAgICAgIHdvLmZvckVhY2goZnVuY3Rpb24oZSl7d1tlXT1vO30pOw0KICAgICAgICAgICAgICAgICAgICAgIHZhciB3cyA9IFsnbmFtZSddOw0KICAgICAgICAgICAgICAgICAgICAgIHdzLmZvckVhY2goZnVuY3Rpb24oZSl7d1tlXT1zO30pOw0KICAgICAgICAgICAgICAgICAgICB9KShkb2N1bWVudCwgd2luZG93KTsNCiAgICAgICAgICAgICAgICAgICAgJXM7DQogICAgICAgICAgICAgICAgICAgIHByaW50KGRlY29kZWQpOw==''') % (
                             encTab, orgData)

                blad = re.findall(r"(case'\\x31'.*?)continue", jscode)[0]

                jscode = jscode.replace(blad, """case'\x31':for(i=0x0;_0x45ae41[_0x5949('0x2')](i,_0x439a49[_0x5949('0x3')]);i+=0x8){_0x41e0ff=_0x45ae41[_0x5949('0x4')](i,0x8);var _0x40b427=_0x439a49[_0x5949('0x5')](i,_0x45ae41[_0x5949('0x6')](i,0x8));var _0x577716=_0x45ae41[_0x5949('0x7')](parseInt,_0x40b427,0x10);with(_0x31f4aa){ke[_0x5949('0xa')](_0x577716);}}""")
                data = {
                    'LanguageChoiceWrapper': '17',
                    'EditorChoiceWrapper': '1',
                    'LayoutChoiceWrapper': '1',
                    'Program': unicode(jscode),
                    'Input': '',
                    'Privacy': '',
                    'PrivacyUsers': '',
                    'Title': '',
                    'SavedOutput': '',
                    'WholeError': '',
                    'WholeWarning': '',
                    'StatsToSave': '',
                    'CodeGuid': '',
                    'IsInEditMode': 'False',
                    'IsLive': 'False'
                }

                response = requests.post('https://rextester.com/rundotnet/Run', headers=headers, data=data)
                result = json.loads(response.content)

                if result[u'Errors']:
                    pass
                else:
                    return 'https://openload.co/stream/%s?mime=true|User-Agent=Mozilla/5.0' % result[u'Result'].replace("\n", "")
            except Exception as e:
                pass
            video_url = self.__check_auth(media_id)
            if not video_url:
                video_url = self.__auth_ip(media_id)
        except ResolverError:
            raise

        if video_url:
            headers = {'User-Agent': common.RAND_UA}
            video_url = video_url + helpers.append_headers(headers)
            return video_url
        else:
            raise ResolverError(i18n('no_ol_auth'))

    def get_url(self, host, media_id):
        return 'http://openload.co/embed/%s' % (media_id)

    def __file_exists(self, media_id):
        js_data = self.__get_json(FILE_URL.format(media_id=media_id))
        return js_data.get('result', {}).get(media_id, {}).get('status') == 200

    def __auth_ip(self, media_id):
        js_data = self.__get_json(INFO_URL)
        pair_url = js_data.get('result', {}).get('auth_url', '')
        if pair_url:
            pair_url = pair_url.replace('\/', '/')
            header = i18n('ol_auth_header')
            line1 = i18n('auth_required')
            line2 = i18n('visit_link')
            line3 = i18n('click_pair').decode('utf-8') % (pair_url)
            with common.kodi.CountdownDialog(header, line1, line2, line3) as cd:
                return cd.start(self.__check_auth, [media_id])

    def __check_auth(self, media_id):
        try:
            js_data = self.__get_json(GET_URL.format(media_id=media_id))
        except ResolverError as e:
            status, msg = e
            if status == 403:
                return
            else:
                raise ResolverError(msg)
        
        return js_data.get('result', {}).get('url')

    def __get_json(self, url):
        result = self.net.http_GET(url).content
        common.logger.log(result)
        js_result = json.loads(result)
        if js_result['status'] != 200:
            raise ResolverError(js_result['status'], js_result['msg'])
        return js_result

    @classmethod
    def get_settings_xml(cls):
        xml = super(cls, cls).get_settings_xml()
        xml.append('<setting id="%s_auto_update" type="bool" label="%s" default="true"/>' % (cls.__name__, i18n('auto_update')))
        xml.append('<setting id="%s_url" type="text" label="    %s" default="" visible="eq(-1,true)"/>' % (cls.__name__, i18n('update_url')))
        xml.append('<setting id="%s_key" type="text" label="    %s" default="" option="hidden" visible="eq(-2,true)"/>' % (cls.__name__, i18n('decrypt_key')))
        xml.append('<setting id="%s_etag" type="text" default="" visible="false"/>' % (cls.__name__))
        return xml

    @classmethod
    def isPopup(self):
        return True