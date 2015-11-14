import urllib2
from xml.etree import ElementTree as etree
#reddit parse
reddit_file = urllib2.urlopen('http://www.reddit.com/r/videos/top/.rss')
#convert to string:
reddit_data = reddit_file.read()
#print reddit_data
#close file because we dont need it anymore:
reddit_file.close()

#entire feed
reddit_root = etree.fromstring(reddit_data)
item = reddit_root.findall('channel/item')
#print item

reddit_titles=[]
reddit_urls=[]
for entry in item:
    #get description, url, and thumbnail
    desc = entry.findtext('title')
    reddit_titles.append([desc])

for title in reddit_titles:
    print title