#4
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name=name

class Permanent(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name)
        self.pay=self.base+self.bonus

class Temporary(Employee):
    def __init__(self, name, time, tpay):
        super().__init__(name)
        self.pay = tpay * time

empType = input('Choose your status. (permanent<P>, temporary<T>): ')

if empType == 'P':
    name = input('Name: ')
    base = int(input('Base: '))
    bonus = int(input('bonus: '))
    p = Permanent(name, base, bonus)
    print('='*30)
    print('Status: Permanent')
    print('name: ',p.name)
    print('salary: ', format(p.pay, '3,d'))
elif empType == 'T':
    name = input('Name: ')
    tpay = int(input('Hourly wage: '))
    time = int(input('Working hours: '))
    t = Temporary(name, time, tpay)
    print('='*30)
    print('Status: Permanent')
    print('name: ', t.name)
    print('salary: ', format(t.pay, '3,d'))
else:
    print('='*30)
    print('error')
