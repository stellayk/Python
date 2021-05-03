from bs4 import BeautifulSoup

file=open('html02.html', mode='r', encoding='utf-8')
source=file.read()

html=BeautifulSoup(source, 'html.parser')

links=html.find_all('a')
print('links size=', len(links))

for link in links:
    try:
        print(link.attrs['href'])
        print(link.attrs['target'])
    except Exception as e:
        print('Exception: ', e)

import re
print('Find the pattern')
patt=re.compile('http://')
links=html.find_all(href=patt)
print(links)