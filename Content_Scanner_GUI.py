#!/usr/bin/env python3

import PySimpleGUI as sg
from bs4 import BeautifulSoup
import requests
import re
import pyautogui
import webbrowser
import time
import os
import sys


cwd = os.getcwd()
folder = 'screenshots'
try:
    os.mkdir(folder)
except OSError as error:
    pass

sg.theme('Light Blue 2')

layout = [[sg.Text('Choose files for your wordlist and URL list')],
          [sg.Text('Keywords', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('URLs', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('Both Keywords and URL files should have only one value on each line!')],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Content Scanner', layout)

event, values = window.Read()
window.close()

print(f'You clicked {event}')
print(f'You chose filenames {values[0]} and {values[1]}')



keywords = values[0]

wordlist = [line.strip() for line in open(keywords, encoding='utf-8-sig')]

websites = values[1]

with open(websites, encoding='utf-8-sig') as f:
    URLs = [line.split()[0] for line in f]
 
print(wordlist)
print(URLs)

print('<================= Process Starting =================>')
print('')
print('')
for i in wordlist:
    for url in URLs:
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.body.find_all(string=re.compile(i))
        if len(word) > 0:
            print('Found matching result of',i,'on '+url)
            webbrowser.open(url, 2)
            time.sleep(5)
            f = open(cwd + '/screenshots/%s.png' %(i), 'w+')
            Screenshot = pyautogui.screenshot()
            Screenshot.save(cwd + '/screenshots/%s.png' %(i))
            print('Taking screenshot and saving to screenshot folder...')
            print('')
print('')
print('')
print('<================= Process Completed =================>')

sg.Popup('Process Completed!', font=('cambria', 14))