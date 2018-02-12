import csv
import requests
from bs4 import BeautifulSoup
base = "http://ausweisung.ivw-online.de/online/index.php?mz="

with open("ivwdata2.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(["title","visits","year","month"])

for year in range(2002,2015):
    for month in range(1,13):

        if month <=9:
            url = base+str(year)+"0"+str(month)

        else:
            url = base + str(year) + str(month)

        print(url)

        r = requests.get(url)
        soup = BeautifulSoup(r.content,"lxml")

        out = []
        title = []

        for i in soup.find_all("table", {"class": "auswla"}):
            for j in i.find_all("td", {"class": "n"}):
                title.append(j.text)

            for j in i.find_all("td", {"class": "s"}):
                out.append(j.text)

            # format change after 2009-10.
            if (
                year >= 2009 and month > 10
            ) or year > 2009:
                visits = out[::3]

            else:
                visits = out[::2]

            y = [year] * len(title)
            print(y)
            m = [month] * len(title)
            print(m)

        rows = zip(title, visits, y, m)

        with open("ivwdata2.csv", "a") as file:
            writer = csv.writer(file, lineterminator='\n')
            for row in rows:
                writer.writerow(row)

# Test
import csv
import requests
from bs4 import BeautifulSoup

url = "http://ausweisung.ivw-online.de/online/index.php?mz=200911"

r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

year = 2009
month = 11
out = []
title = []

with open("testdata.csv", "w") as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(["title","visits","year","month"])

for i in soup.find_all("table", {"class": "auswla"}):
    for j in i.find_all("td", {"class": "n"}):
        title.append(j.text)

    for j in i.find_all("td", {"class": "s"}):
        out.append(j.text)

    visits=out[::3]
    y=[year]*len(title)
    m=[month]*len(title)


rows=zip(title,visits,y,m)
with open("testdata.csv", "a") as file:
    writer = csv.writer(file, lineterminator='\n')
    for row in rows:
        writer.writerow(row)







