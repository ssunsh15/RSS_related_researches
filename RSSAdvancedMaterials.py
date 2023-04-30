import feedparser

# ----------------------------- RSS crawling and parsing from the journal "Advanced Materials" (sort : most recent)

parse_rss = feedparser.parse("https://onlinelibrary.wiley.com/feed/15214095/most-recent")

# ----------------------------- RSS filtering keywords import from "DatabaseKeywords.txt"

f = open("DatabaseKeywords.txt", 'r')
lines = f.readlines()

keywords = []

for line in lines:
    key = line.split('\n')
    keywords.append(key[0])
    
f.close()

# ----------------------------- Import Previous DOIs

f = open("DatabaseAdvanDOI.txt", 'r')
lines = f.readlines()

Database = []

for line in lines:
    key = line.split('\n')
    Database.append(key[0])
    
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

# ----------------------------- Only new feed detection

newDOI = []
newSequence = []
i = -1

for new in RelatedRSSDOI:
    i = i + 1
    valid = True
    for prev in Database:
        if new in prev:
            valid = False
            break
        else:
            continue
    if valid:
        newDOI.append(new)
        newSequence.append(Sequence[i])
    else:
        continue
        
# ----------------------------- Database renewal

f = open("DatabaseAdvanDOI.txt", 'w')

Database = newDOI + Database

for doi in Database:
    f.write(doi + '\n')
    
f.close()

# ----------------------------- new feed summary html generator

j=0

for i in newSequence:
    html_text = ("<p>" + parse_rss.entries[i].title + "<p>" + 
    parse_rss.entries[i].published + "<br>" + 
    parse_rss.entries[i].link + "<br>" + 
    parse_rss.entries[i].content[1].value)
    
    if j<10:
        num = '00'+str(j)
    elif j<100:
        num = '0'+str(j)
    else:
        num = str(j)
    
    html_file = open('newFeeds/Advan' + num + '.html', 'w', encoding='utf-16')
    html_file.write(html_text)
    html_file.close()
    j = j + 1
