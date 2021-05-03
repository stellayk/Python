print('start!')
x=[10, 30, 25.2, 'num', 14, 51]

for i in x:
    print(i)
    y=i**2
    print('y=',y)
print('end!')

print('start!')
for i in x:
    try:
        y=i**2
        print('i=',i,'y=',y)
    except:
        print('not number: ',i)
print('end')


print('Exceptions')
try:
    div=1000/2.53
    print('div=%5.2f' %(div))
    div=1000/0
    f=open('C:\\test.txt')
    num=int(input('number: '))
    print('num=', num)

except ZeroDivisonError as e:
    print('error: ', e)
except FileNotFoundError as e:
    print('error: ', e)
except Exception as e:
    print('error: ', e)

finally:
    print('finally always works')