lst=[1,3,5]
for i,c in enumerate(lst):
    print('index: ',i,end=', ')
    print('element: ', c)

dit={'name':'Alex', 'job':'salesman', 'addr':'Seoul'}
for i, k in enumerate(dit):
    print('order: ', i, end=', ')
    print('key: ', k, end=', ')
    print('element: ', dit[k])

import datetime
from datetime import date, time
help(date)
today=date(2019,10,23)
print(today)
print(today.year)
print(today.month)
print(today.day)

w=today.weekday()
print('day: ',w)

help(time)
currTime=time(21,4,30)
print(currTime)
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

isoTime=currTime.isoformat()
print(isoTime)