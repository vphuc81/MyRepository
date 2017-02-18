# -*- coding: utf-8 -*-
import urllib
import re
import json
import api
import urlparse

class Source:
	def __init__(self, cache_path):
		self.cache_path = cache_path
		self.base_url = 'http://www.kenh88.com/'


	def __get_page__(self, url, cacheTime=3600000):
		return api.SOUPKit(cache_path=self.cache_path).SOUPFromURL(url, cacheTime=cacheTime)


	def base_url(self):
		return self.base_url


	def menu(self):
		page = self.__get_page__(self.base_url)
		menu = {}
		content = page.find('div', {'class': 'menu'})
		ul = content.find('ul')
		for l in ul.children:
			a = l.find('a')
			if type(a) is int and a < 0: continue
			if a['href'] == '/': continue
			if 'javascript' in a['href']:
				submenu = []
				sub_ul = l.find('ul', {'class': 'sub-menu'})
				for s in sub_ul.find_all('a'):
					submenu.append({'label': s.text, 'href': self.base_url + s['href']})
				menu[unicode(a.text)] = submenu
			else:
				menu[unicode(a.text)] = self.base_url + a['href']

		return menu


	def contents(self, url):
		page = self.__get_page__(url)
		contents = []
		duplicates = []

		for c in page.find_all('div', {'class': 'row'}):
			for d in c.find_all('div'):
				duration = d.find('span', {'class': 'process_r'})
				if duration <> None:
					duration = duration.text
				info = d.find('span', {'class': 'status'})
				if info <> None:
					info = info.text
				a = d.find('a')
				href = a['href']
				if href.startswith('/'):
					href = href[1:]
				href = self.base_url + href
				poster = self.base_url + a.find('img')['src']
				poster = poster.replace(' ', '%20')
				title1 = self.normalize_str(d.find('h2').find('a').text)
				title2 = self.normalize_str(d.find('h2').text)
				if href not in duplicates:
					duplicates.append(href)
					contents.append({'title1': unicode(title1), 'title2': unicode(title2), 'href': href, 'duration': unicode(duration), 'info': unicode(info), 'poster': poster})

		next_page = self.__next_page__(page)
		return {'items': contents, 'next_page': next_page}


	def media_items(self, url):
		page = self.__get_page__(url)
		#info
		poster = page.find('div', {'class': 'mCSB_container mCS_no_scrollbar'}).find('img')
		if poster <> None:
			poster = poster['src']
		else:
			poster = page.find('img', {'class': 'poster'})['src']
		if poster <> None:
			poster = self.base_url + poster
			poster = poster.replace(' ', '%20')

		title1 = page.find('div', {'class': 'movie'}).find('h1').text.strip()
		url = url.replace('phim', 'xem-phim-online')
		page = self.__get_page__(url)

		media_items = {}
		serverList = page.find('div', {'class': 'serverlist'})
		for server in serverList.find_all('div', {'class': 'server'}):
			serverName = server.find('div', {'class': 'label'}).text
			serverName = serverName.replace(':', '').strip()
			for e in server.find_all('a'):
				ep_title = e.text.replace('full', '')
				ep_title = u''.join([u'Tập ', ep_title])
				href = e['href']
				if href.startswith('/'):
					href = href[1:]
				href = self.base_url + href
				s = []
				if ep_title in media_items:
					s = media_items[unicode(ep_title)]
				s.append({'title1': unicode(title1), 'title2': '', 'ep_title': ep_title, 'poster': poster, 'banner': '', 'server_name': unicode(serverName), 'href': href})
				media_items[unicode(ep_title)] = s
		if media_items == {}:
			media_items['DEFAULT'] = [{'title1': unicode(title1), 'title2': '', 'ep_title': '', 'poster': poster, 'banner': '', 'server_name': unicode('Server 1'), 'href': url}]
		return media_items


	def search(self, query):
		search_url = self.base_url + 'film/search?' + urllib.urlencode({'keyword': urllib.quote_plus(query)})
		return self.contents(search_url)


	def __next_page__(self, page):
		pages = page.find('ul', {'class': 'pagination'})
		if pages is None:
			return None

		n = pages.find('a', {'class': 'next'})

		if n is None:
			return None

		return self.base_url + n['href']


	def normalize_str(self, string):
		s = re.sub(r'\s+', ' ', string)
		return s.strip()


	def resolve_stream(self, url):
		page = self.__get_page__(url)
		play = page.find('div', {'class': 'play'})
		iframe = play.find('iframe')
		if iframe:
			page = self.__get_page__(iframe['src'])

		for s in page.find_all('script'):
			if re.search('(?i).*jwplayer\("player"\).*', s.text):
				return self.xtubeth(s.text)
			if re.search('(?i).*gkpluginsphp.*', s.text):
				return self.gkplugin(s.text)
		return None


	def xtubeth(self, txt):
		d = txt[txt.index('[{') +1 : txt.rindex('}]') + 1]
		d = d.replace('file', '"file"').replace('type', '"type"').replace('label', '"label"').replace('sources', '"sources"').replace("'", '"')
		d = json.loads(d)
		for s in d['sources']:
			if '720' in s['label']:
				return s['file']
		return None

	def gkplugin(self, txt):
		m = txt[txt.index('{'): txt.index('}') + 1]
		m = m.replace('link', '"link"')
		m = json.loads(m)
		d = api.JSONKit(cache_path=self.cache_path).ObjectFromURL('http://www.kenh88.com/gkphp/plugins/gkpluginsphp.php', values=m)
		return d['link']
