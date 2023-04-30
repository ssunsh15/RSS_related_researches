import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup

# ----------------------------- RSS crawling and parsing from the journal "Advanced Materials" (sort : most recent)

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")

# RSS filtering keywords import from "keywords.txt"

f = open("DatabaseKeywords.txt", 'r')
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

# ----------------------------- RSS duplicated test from txt database

f = open("DatabaseAdvanDOI.txt", 'r')
lines = f.readlines()

Database = []

for line in lines:
    key = line.split('\n')
    Database.append(key[0])
    
f.close()

duptest = []

for new in RelatedRSSDOI:
    for prev in Database:
        valid = True
        if new in prev:
            valid = False
            break
        else:
            continue
    duptest.append(valid)
   
print(duptest)
