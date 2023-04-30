import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup

# ----------------------------- RSS crawling and parsing from the journal "Advanced Materials" (sort : most recent)

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")

# RSS filtering keywords import from "DatabaseKeywords.txt"

f = open("DatabaseKeywords.txt", 'r')
lines = f.readlines()

keywords = []

for line in lines:
    key = line.split('\n')
    keywords.append(key[0])
    
f.close()

# ----------------------------- RSS keyword filtering

RelatedRSSDOI = []
Sequence = []
i = -1          # parse_rss.entries[i], i only for related researches

for p in parse_rss.entries:
    i = i + 1
    if p == None:
        break
    else:
        for kw in keywords:
            if kw in p.title:
                RelatedRSSDOI.append(p.id)
                Sequence.append(i)
                break
            else:
                if kw in p.content[0].value:
                    RelatedRSSDOI.append(p.id)
                    Sequence.append(i)
                    break
                else:
                    continue
                    
print(Sequence) #   -----------------------------------------------------------------------------

# ----------------------------- RSS duplicated test from txt database

f = open("DatabaseAdvanDOI.txt", 'r')
lines = f.readlines()

Database = []

for line in lines:
    key = line.split('\n')
    Database.append(key[0])
    
f.close()

newDOI = []             # DOIs of new feeds
newSequence = []        # parse_rss.entries[i], i for new feed & include keywords
i = -1

for new in RelatedRSSDOI:
    i = i + 1
    for prev in Database:
        if new in prev:
            break
        else:
            continue
    newDOI.append(new)
    newSequence.append(Sequence[i])
   
print(newSequence) #   -----------------------------------------------------------------------------
