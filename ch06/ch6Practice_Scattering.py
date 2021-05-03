#2
from statistics import mean
from math import sqrt

class Scattering:
    def __init__(self,data):
        self.data = data

    def var_func(self):
        avg = mean(self.data)
        dev = [(d-avg)**2 for d in self.data]
        var = sum(dev)/(len(self.data)-1)
        print('variance:', var)
        return var

    def std_func(self, var):
        std = sqrt(var)
        print('sd:', std)
        return std

x = [5, 9, 1, 7, 4, 6]
scr = Scattering(x)
scr.std_func(scr.var_func())
#call both var_func and std_func