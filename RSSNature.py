import pandas as pd
import feedparser
import requests
from bs4 import BeautifulSoup

rss_list = ["https://www.nature.com/nature.rss",
           "https://www.nature.com/ncomms.rss",
           "https://www.nature.com/nmat.rss",
           "https://www.nature.com/nchem.rss",
           "https://www.nature.com/nnano.rss",
           "https://www.nature.com/nenergy.rss"]

parse_rss = feedparser.parse(rss_list[1])
parse_rss.entries[0]
