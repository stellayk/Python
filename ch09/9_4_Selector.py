from bs4 import BeautifulSoup

file=open('html03.html', mode='r', encoding='utf-8')
source=file.read()

html=BeautifulSoup(source, 'html.parser')

print('>> table selector <<')
table=html.select_one('#tab')
print(table)

print('>> id selector <<')
ths=html.select('#tab>tr>th')
print(ths)

trs=html.select('#tab>.odd')
print('>> class selector <<')
print(trs)

trs=html.select("tr[class=odd]")

print('>> tr>td print <<')
for tr in trs:
    tds=tr.find_all('td')
    for td in tds:
        print(td.string)