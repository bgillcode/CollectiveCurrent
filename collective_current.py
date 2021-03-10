import time
import os
import sys
import subprocess
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import urllib.parse
import requests
import threading

rangeStart = 1
rangeEnd = 2

for i in range(rangeStart, rangeEnd):
    # Pass in the page that you want
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
        filenameNumber = filenameGotten.split('.')[0].zfill(3)
        print(filenameNumber)
        open(str(filenameGotten).zfill(3), 'wb').write(r.content)
