import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")
print(parse_rss.entries[0].title)

f = open("keywords.txt", 'r')
lines = f.readlines()

keywords = []

for line in lines:
    key = line.split('\n')
    keywords.append(key[0]);
    
f.close()

print(keywords)
