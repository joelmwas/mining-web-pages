import feedparser

if __name__ == '__main__':
    FEED_URL = 'http://whiteafrican.com/feed/atom/'
    fp = feedparser.parse(FEED_URL)
    for e in fp.entries:
	print e.title
	print e.links[0].href
	print e.content[0].value
