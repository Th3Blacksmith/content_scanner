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

keywords = values[0]

wordlist = [line.strip() for line in open(keywords, encoding='utf-8-sig')]

websites = values[1]

with open(websites, encoding='utf-8-sig') as f:
    URLs = [line.split()[0] for line in f]
 
for i in wordlist:
    for url in URLs:
        page = requests.get(url)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.body.find_all(string=re.compile(i))
        if len(word) > 0:
            webbrowser.open(url, 2)
            time.sleep(5)
            f = open(cwd + '/screenshots/%s.png' %(i), 'w+')
            Screenshot = pyautogui.screenshot()
            Screenshot.save(cwd + '/screenshots/%s.png' %(i))

sg.Popup('Process Completed!', font=('cambria', 14))