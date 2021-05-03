help(len)
dataset=list(range(1,6))
print(dataset)

print('len=',len(dataset))
print('sum=',sum(dataset))
print('max=',max(dataset))
print('min=',min(dataset))

import statistics
from statistics import variance, stdev

print('mean=', statistics.mean(dataset))
print('median=',statistics.median(dataset))
print('variance=',statistics.variance(dataset))
print('sd=',statistics.stdev(dataset))

def userFunc(x,y):
    print('userFunc')
    tot=x+y
    sub=x-y
    mul=x*y
    div=x/y

    return tot,sub,mul,div
x=int(input('x: '))
y=int(input('y: '))

t,s,m,d=userFunc(x,y)
print('tot= ',t)
print('sub= ',s)
print('mul= ',m)
print('div= ',d)