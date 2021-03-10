import time
import os
import sys
import subprocess
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.parse
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", help="Set URL to retrieve the images from.")
parser.add_argument("--startrange", "-s", help="Set the number to START the range from for the chapter.\
For example 1, this will start the count to retrieve from chapter 1. If set to 3 it will start downloading from chapter 3.")
parser.add_argument("--endrange", "-e", help="Set the number to END the range from for the chapter. For example 5, \
this will get all of the chapters from the startrange set up to 5.\
If set to 10, it will retrieve all images from for all of the chapters within the range up to chapter 10.")

urlInputted = ''
startRangeInputted = 0
endRangeInputted = 0
args = parser.parse_args()

checkURLEnteredFlag = False
if args.url:
    if str(args.url).strip().find("http") != -1:
        checkURLEnteredFlag = True
    urlInputted = str(args.url)

startRangeEnteredFlag = False
if args.startrange:
    if str(args.startrange) != -1:
        startRangeEnteredFlag = True
    startRangeInputted = str(args.url)

endRangeEnteredFlag = False
if args.endrange:
    if str(args.endrange) != -1:
        endRangeEnteredFlag = True
    endRangeInputted = str(args.url)

# Get the chapter links
chapterURL = urlInputted
reqChapters = Request(chapterURL, headers={'User-agent': 'Mozilla/5.0'})
pageChapter = urlopen(reqChapters).read()
soupChapters = BeautifulSoup(pageChapter, 'html.parser')
textGottenContentChapter = soupChapters.find_all(class_="chapter-name text-nowrap", href=True)
textGottenContentChapter = textGottenContentChapter[::-1]

print(textGottenContentChapter)

if startRangeInputted == 0:
    # Download from the first chapter onwards if the start range is not given
    rangeStart = 0
elif startRangeInputted == 1:
    rangeStart = 0
else:
    rangeStart = int(startRangeInputted)

if endRangeInputted == 0:
    # Download all of the chapters up the end if an end range is not given
    rangeEnd = len(textGottenContentChapter)
else:
    rangeEnd = int(endRangeInputted)

if checkURLEnteredFlag == False:
    print('Please try again and enter a valid URL to retrieve the images from')
    sys.exit()

else:
    for i in range(rangeStart, rangeEnd + 1):
        url = textGottenContentChapter[i]['href']
        req = Request(url, headers={'User-agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')

        thisReferer = ''
        if url.strip().find("nelo") != -1:
            thisReferer = 'https://manganelo.com/'
        elif url.strip().find("kakalot") != -1:
            thisReferer = 'https://mangakakalot.com/'

        textGottenContent = soup.find(class_="container-chapter-reader").find_all('img')

        for m in textGottenContent:
            domain = 'https://' + urllib.parse.urlparse(m['src']).netloc +\
             urllib.parse.urlparse(m['src']).path

            print(domain)
            r = requests.get(domain, headers= \
            {'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', \
            'Accept-Encoding': 'gzip, deflate, br', \
            'referer': thisReferer})
            print(r)

            a = urlparse(m['src'])
            filenameGotten = os.path.basename(a.path)
            filenameNumber = filenameGotten.split('.')[0].zfill(3) + '.' + filenameGotten.split('.')[1]
            print(filenameNumber)
            open(str(filenameNumber), 'wb').write(r.content)
