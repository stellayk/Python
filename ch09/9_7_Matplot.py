import matplotlib.pyplot as plt
import random
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False

print(random.randint(a=1, b=5))
print(random.random())
print(random.normalvariate(mu=0, sigma=1))

help(plt.plot)
'''
plot(x,y)
plot(x,y,'bo')
plot(y)
plot(y,'r+')
'''

data=range(10)
plt.plot(data)
plt.plot(data, 'r+')
plt.show()

data2=[random.random() for i in range(10)]
plt.plot(data, data2)
plt.plot(data, data2, 'ro')
plt.show()