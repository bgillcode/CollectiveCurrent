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
