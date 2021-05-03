var1="Hello Python"
print(var1)
print(id(var1))
print(type(var1))

var1=100
print(var1)
print(id(var1))
print(type(var1))

var2=150.25
print(var2)
print(id(var2))
print(type(var2))

var3=True
print(var3)
print(id(var3))
print(type(var3))

import keyword
python_keyword=keyword.kwlist
print(python_keyword)
print(type(python_keyword))
print(len(python_keyword))

a=int(10.5)
b=int(20.42)
add=a+b
print('add = ', add)

a=float(10)
b=float(20)
add2=a+b
print('add2 = ',add2)

print(int(True))
print(int(False))

st='10'
print(int(st)**2)