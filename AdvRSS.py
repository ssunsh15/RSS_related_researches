import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")
print(parse_rss.entries[0].title)
