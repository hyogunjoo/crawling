#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

i = 1
f = open("새파일.txt", 'w')
with urlopen('https://www.naver.com') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.select("p.login_msg"):
        data = str(i) + "위 : " + anchor.get_text() + "\n"
        i = i + 1
        f.write(data)
f.close()
