#!/usr/bin/env python3

from bs4 import BeautifulSoup
import csv
import requests
import re

#This script uses the words in the keywords.txt file to iteratively scan through the websites found in the file.csv file.

#First, the keywords.txt file is read and the keywords are extracted from it.

keywords = []
with open('keywords.txt') as y:
    keywords = [line.split()[0] for line in y]
y.close()
keywords.pop(0)

#Then we do the same thing for the URL containing .csv file.

with open('file.csv') as f:
    csvs = [line.split()[0] for line in f]
csvs.pop(0)

#Lastly, we actually do the work of searcing the html source code from each of our websites to see if our keyword is present.

print('=================Process Starting=================')
print('')
print('')
for i in keywords:
    for url in csvs:
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        words = soup.body.find_all(string=re.compile(i))
        if len(words) > 0:
            print('Found matching result of',i,'on '+url)
            print('')
print('')
print('')
print('=================Process Completed=================')