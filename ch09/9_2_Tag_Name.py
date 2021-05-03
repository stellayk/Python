from bs4 import BeautifulSoup

file=open('html01.html', mode='r', encoding='utf-8')
text=file.read()

html=BeautifulSoup(text, 'html.parser')

h1=html.html.body.h1
print('h1: ', h1.string)

h2=html.find('h2')
print('h2: ', h2.string)

lis=html.find_all('li')
print(lis)

for li in lis:
    print(li.string)