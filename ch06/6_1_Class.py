def calc_func(a,b):
    x=a
    y=b
    def plus():
        p=x+y
        return p
    def minus():
        m=x-y
        return m
    return plus, minus
p, m = calc_func(10, 20)
print('plus=',p())
print('minus=',m())

class calc_class:
    x = y = 0

    def __init__(self,a,b):
        self.x=a
        self.y=b

    def plus(self):
        p=self.x+self.y
        return p

    def minus(self):
        m=self.x-self.y
        return m

obj = calc_class(10,20)
print('plus=', obj.plus())
print('minus=', obj.minus())



class Car:
    cc=0
    door=0
    carType=None

    def __init__(self, cc, door, carType):
        self.cc=cc
        self.door=door
        self.carType=carType

    def display(self):
        print(self.cc, self.door, self.carType)

car1=Car(2000,4,"car")
car2=Car(3000,5,"SUV")

car1.display()
car2.display()