lst = [1,2,3,4,5]
print(lst)
print(type(lst))
for i in lst:
    print(lst[:i])


x=list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index increased by 2')
print(x[::2])
print(x[1::2])


a = ['a', 'b', 'c']
print(a)

b=[10,20,a,5,True]
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])
print(b[3:])


num=['one','two','three','four']
print(num)
print(len(num))
num.append('five')
print(num)
num.remove('five')
print(num)
num[3]='4'
print(num)
num.insert(0, 'zero')
print(num)

x=[1,2,3,4]
y=[1.5, 2.5]
z=x+y
print(z)

x.extend(y)
print(x)
x.append(y)
print(x)

lst=[1,2,3,4]
result=lst*2
print(result)

result=["banana", "mango", "honeydew", "pineapple", "mandarin"]
result.sort()
print(result)
result.sort(reverse=True)
print(result)

import random
r = []
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r:
    print('true')
else:
    print('false')


x = [2,4,1,5,7]
lst = [i**2 for i in x]
print(lst)

num=list(range(1,11))
lst2 = [i*2 for i in num if i%2==0]
print(lst2)