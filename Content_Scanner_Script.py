from bs4 import BeautifulSoup
import requests
import re
import pyautogui
import webbrowser
import time
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

def display_title_bar():
    os.system('clear')
    cprint(figlet_format('Content  Scanner'))

display_title_bar()
time.sleep(2)

cwd = os.getcwd()
folder = 'screenshots'
try:
    os.mkdir(folder)
except OSError as error:
    pass

keywords = 'Keywords.txt'

wordlist = [line.strip() for line in open(keywords, encoding='utf-8-sig')]

websites = 'URLs.csv'

with open(websites, encoding='utf-8-sig') as f:
    URLs = [line.split()[0] for line in f]

print('<====================================================>')
print('<================= Process Starting =================>')
print('<====================================================>')
print('')
print('')
time.sleep(2)
for i in wordlist:
    for url in URLs:
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.body.find_all(string=re.compile(i))
        if len(word) > 0:
            print('Found matching result of',i,'on '+url)
            print('')
            webbrowser.open(url, 2)
            time.sleep(5)
            f = open(cwd + '/screenshots/%s.png' %(i), 'w+')
            Screenshot = pyautogui.screenshot()
            Screenshot.save(cwd + '/screenshots/%s.png' %(i))
            print('Taking screenshot and saving to screenshot folder...')
            print('')
            time.sleep(2)
print('')
print('')
print('<=====================================================>')
print('<================= Process Completed =================>')
print('<=====================================================>')
time.sleep(3)
display_title_bar()
print('\n <================= Thankyou for using Content Scanner =================>')