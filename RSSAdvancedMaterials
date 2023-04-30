import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup
import pickle

# ----------------------------- RSS crawling and parsing from the journal "Advanced Materials" (sort : most recent)

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")

# RSS filtering keywords import from "keywords.txt"

f = open("keywords.txt", 'r')
lines = f.readlines()

keywords = []

for line in lines:
    key = line.split('\n')
    keywords.append(key[0])
    
f.close()

# ----------------------------- RSS keyword filtering

RelatedRSSDOI = []

for p in parse_rss.entries:
    if p == None:
        break
    else:
        for kw in keywords:
            if kw in p.title:
                RelatedRSSDOI.append(p.id)
                break
            else:
                if kw in p.content[0].value:
                    RelatedRSSDOI.append(p.id)
                    break
                else:
                    continue

# ----------------------------- RSS duplicated test from pickle database

AdvMatDOIDatabase = ['10.1002/adma.202205326', '10.1002/adma.202370097', '10.1002/adma.202211579']

with open('AdvMatDOIDatabase.pickle', 'wb') as f:
    pickle.dump(AdvMatDOIDatabase, f, pickle.HIGHEST_PROTOCOL)

