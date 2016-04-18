from __future__ import unicode_literals
from resources.lib.modules import client,convert,webutils
from resources.lib.modules.log_utils import log
from resources.lib.modules import praw

import re,sys,urlparse
class info():
    def __init__(self):
    	self.mode = 'reddit_soccer'
        self.name = 'reddit/r/soccerstreams'
        self.icon = 'reddit.png'
        self.categorized = False
        self.paginated = False
        self.multilink = True

class main():
	def __init__(self, url='http://www.iptvlinks.eu/'):
		self.base = 'http://www.iptvlinks.eu/'
		self.url = url

	def events(self):
		new = []
		r = praw.Reddit(user_agent='Kodi Castaway')
		r.config.api_request_delay = 0
		for submission in r.get_subreddit('soccerstreams').get_hot(limit=30):
			if 'match thread' in submission.title.lower():
				url = submission.id
				title = submission.title
				title = re.sub('Match Thread\s*(?:\[.+?\])?:?','',title).encode('utf-8')
				new.append((url,title))
		return new

	
	
	
	def links(self,url):
		r = praw.Reddit(user_agent='Kodi Castaway')
		r.config.api_request_delay = 0
		submission = r.get_submission(submission_id=url)
		links=[]
		regex = re.compile(r'([-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?)',re.IGNORECASE)
		link = re.findall(regex, submission.selftext.encode('utf-8'))
		links = links + link
		flat_comments = praw.helpers.flatten_tree(submission.comments)
		for comment in flat_comments:
			if not isinstance(comment,praw.objects.Comment):
				flat_comments.remove(comment)
		try:
			flat_comments.sort(key=lambda comment: comment.score , reverse=True)
		except:
			pass
		for comment in flat_comments:
			try:
				link = re.findall(regex, comment.body.encode('utf-8'))
				links = links + link
			except:
				pass

		return self.__prepare_links(links)	

	def __prepare_links(self,links):
		new = []
		for l in links:
			log(l)
			url = l[0]
			title = (l[0]+l[1]).replace('www.','').replace('http://','').replace('https://','')#urlparse.urlparse(l[0]).netloc.replace('www.','')
			if 'koora' in l[0] or 'reddit' in l[0]:
				continue
			new.append((url,title))
		return new

	def resolve(self,url):
		import liveresolver
		return liveresolver.resolve(url)