import os
import sys
import os
import json

import feedparser
from bs4 import BeautifulSoup

from BeautifulSoup import BeautifulStoneSoup
from nltk import clean_html

FEED_URL = 'http://whiteafrican.com/feed/atom/'


def clean_HTML(html):
    doc = BeautifulSoup(html)
    return doc

fp = feedparser.parse(FEED_URL)

print "Fetched %s entries from '%s'" % (len(fp.entries[0].title), fp.feed.title)

blog_posts = []
for entry in fp.entries:
    blog_posts.append({'title': entry.title, 
			'content': clean_HTML(entry.content[0].value), 
			'link': entry.links[0].href})

output_file = os.path.join('data', 'webpages', 'feed.json')

f = open(output_file, 'w')
f.write(json.dumps(blog_posts, indent=1))
f.close()

print "Wrote output file to %s" % (f.name)

