def a():

    print('a')
    def b():
        print('b')
    return b
b=a()
b()

data=list(range(1,101))
def outer_func(data):
    dataSet=data
    def tot():
        tot_val=sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val=tot_val/len(dataSet)
        return avg_val
    return tot, avg

tot,avg=outer_func(data)
tot_val=tot()
print('tot=',tot_val)
avg_val=avg(tot_val)
print('avg=',avg_val)



from statistics import mean
from math import sqrt
data = [4, 5, 3.5, 2.5, 6.3, 5.5]
def scattering_func(data):
    dataSet = data

    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    def var_func(avg):
        diff = [(data-avg)**2 for data in dataSet]
        print(sum(diff))
        var_val = sum(diff)/(len(dataSet)-1)
        return var_val
    def std_func(var):
        std_val = sqrt(var)
        return std_val
    return avg_func, var_func, std_func

avg, var, std = scattering_func(data)

print('avg: ', avg())
print('var: ', var(avg()))
print('std: ', std(var(avg())))



def wrap(func):
    def decorated():
        print('hello!')
        func()
        print('bye!')
    return decorated

@wrap
def hello():
    print('Hi,', "Brandon")

hello()



def Counter(n):
    if n==0:
        return 0
    else:
        Counter(n-1)

print('n=0: ', Counter(0))
Counter(5)


def Adder(n):
    if n==1:
        return 1
    else:
        result = n+Adder(n-1)
        print(n, end=' ')
        return result

print('n=1 ', Adder(1))
print('\nn=5 ', Adder(5))