import urllib.request
from bs4 import BeautifulSoup

url='http://www.google.com'

res=urllib.request.urlopen(url)
data=res.read()

src=data.decode("utf-8")
print(src)

html=BeautifulSoup(src, 'html.parser')
print(html)

a=html.find('a')
print('a tag: ',a)
print('a tag context: ', a.string)