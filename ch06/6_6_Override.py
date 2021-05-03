class Employee:
    name=None
    pay=0

    def __init__(self, name):
        self.name=name
    def pay_calc(self):
        pass

class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, base, bonus):
        self.pay=base+bonus
        print('total: ', format(self.pay, '3,d'), 'won')

class Temporary(Employee):
    def __init__(self,name):
        super().__init__(name)
    def pay_calc(self, tpay, time):
        self.pay=tpay*time
        print('total: ', format(self.pay, '3,d'), 'won')

p=Permanent("Sandra Smith")
p.pay_calc(3000000, 200000)
t=Temporary("Mike Miller")
t.pay_calc(15000, 80)