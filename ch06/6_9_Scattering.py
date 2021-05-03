import myPackage.scattering
data=[1,3,1.5,2,1,3.2]
print('average: ', myPackage.scattering.Avg(data))

var,sd= myPackage.scattering.var_sd(data)
print('var: ',var)
print('sd: ',sd)

from myPackage.scattering import Avg, var_sd
print('avg: ',Avg(data))
var,sd=var_sd(data)
print('var: ',var)
print('sd: ',sd)



from statistics import mean
from math import sqrt

def Avg(data):
    avg=mean(data)
    return avg
def var_sd(data):
    avg=Avg(data)
    diff=[(d-avg)**2 for d in data]
    var=sum(diff)/(len(data)-1)
    sd=sqrt(var)

    return var,sd

if __name__ == "__main__":
    data = [1,3,5,7]
    print('avg= ', Avg(data))
    var, sd = var_sd(data)
    print('var= ',var)
    print('sd= ',sd)