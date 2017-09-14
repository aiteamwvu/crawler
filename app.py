import feedparser
feed = feedparser.parse('http://reddit.com/.rss')
for entry in feed['entries']:
    print(entry['title'])
