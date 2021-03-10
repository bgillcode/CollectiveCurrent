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

urlInputted = ''

# Read arguments from the command line
args = parser.parse_args()

checkURLEntered = False

# Check for --url
if args.url:
    if str(args.url).strip().find("http") != -1:
        checkURLEntered = True
    urlInputted = str(args.url)

rangeStart = 1
rangeEnd = 2

if checkURLEntered == False:
    print('Please try again and enter a valid URL to retrieve the images from')
    sys.exit()

else:
    for i in range(rangeStart, rangeEnd):
        url = urlInputted
        req = Request(url, headers={'User-agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page, 'html.parser')

        textGottenContent = soup.find(class_="container-chapter-reader").find_all('img')

        for line in textGottenContent:
            domain = 'https://' + urllib.parse.urlparse(line['src']).netloc + urllib.parse.urlparse(line['src']).path

            print(domain)
            r = requests.get(domain, headers={'Accept': 'image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5', \
            'Accept-Encoding': 'gzip, deflate, br', \
            'referer': 'https://manganelo.com/'})
            print(r)

            a = urlparse(line['src'])
            filenameGotten = os.path.basename(a.path)
            filenameNumber = filenameGotten.split('.')[0].zfill(3) + '.' + filenameGotten.split('.')[1]
            print(filenameNumber)
            open(str(filenameGotten).zfill(3), 'wb').write(r.content)
