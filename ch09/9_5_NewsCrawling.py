import urllib.request as req
from bs4 import BeautifulSoup

url="https://finance.yahoo.com/"
res=req.urlopen(url)
source=res.read()

source=source.decode("utf-8")

html=BeautifulSoup(source, 'html.parser')

atags=html.select('a[class=link_txt]')
print('a tag=', len(atags))

crawling_data=[]

cnt=0
for atag in atags:
    cnt += 1
    atagStr=str(atag.string)
    crawling_data.append(atagStr.strip())

print('result')
print(crawling_data)

import pickle
file=open('data.pickle', mode='wb')
pickle.dump(crawling_data,file)

file=open('data.pickle', mode='rb')
crawling_data=pickle.load(file)
print('pickle load')
print(crawling_data)