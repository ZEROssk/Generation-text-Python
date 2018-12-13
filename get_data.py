# -*- coding:utf-8 -*-

import requests
import re
import os
import sys
from bs4 import BeautifulSoup

file_path = './text_data/'

URL = 'http://lovegundam.dtiblog.com/blog-category-7.html'

while True:
    baseHTML = requests.get(URL).text.replace('<br />', '\n')

    parsedHTML = BeautifulSoup(baseHTML, 'html.parser')

    nextLink = parsedHTML.find(
        'a',
        class_  = 'gray',
        text    = re.compile('次'),
    )

    texts = parsedHTML.find_all(
        'div',
        class_  = 'body',
    )

    for text in texts:
        print(text.text)

    if nextLink is None:
        break

    URL = 'http://lovegundam.dtiblog.com/' + nextLink.get('href')


