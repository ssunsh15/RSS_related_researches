import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup
import pickle

# RSS crawling and parsing from the journal "Advanced Materials" (sort : most recent)

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")
print(parse_rss.entries[0].title)       # parsing validation

# RSS filtering keywords import from "keywords.txt"

f = open("keywords.txt", 'r')
lines = f.readlines()

keywords = []

for line in lines:
    key = line.split('\n')
    keywords.append(key[0])
    
f.close()

# RSS keyword filtering

RelatedRSSDOI = []

for p in parse_rss.entries:
    if p == None:
        break
    else:
        for keyword in keywords:
            if keyword in p.title:
                RelatedRSSDOI.append(p.id)
                break
            else:
                continue

print(RelatedRSSDOI)

# RSS duplicated test from pickle database
