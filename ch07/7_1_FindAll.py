import re
from re import findall

stl = '1234 abcDEF ABC_555_6 QWER'

print(findall('1234', stl))
print(findall('[0-9]', stl))
print(findall('[0-9]{3}', stl))
print(findall('[0-9]{3,', stl))
print(findall('\\d{3,}', stl))

print(findall('[a-z]{3}', stl))
print(findall('[a-x|A-Z]{3}', stl))

st2 = 'test1abcABC 123mbc 45test'

print(findall('^test', st2))
print(findall('st$', st2))
print('.bc', st2)
print('t.', st2)

st3 = 'test^ABC abc df*gh 123$tbc'
words = findall('\\w{3,}', st3)
print(words)
print(findall('[^^*$]+', st3))