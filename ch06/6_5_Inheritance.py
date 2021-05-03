class Super:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print('name: %s, age: %d'%(self.name, self.age))
sup = Super('parent', 55)
sup.display()

class Sub(Super):
    gender = None

    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        print('name: %s, age: %d, gender: %s'%(self.name, self.age, self.gender))
sub = Sub('child', 25, 'male')
sub.display()



class Parent:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def display(self):
        print('name: {}, job: {}'.format(self.name, self.job))

p=Parent("Michelle Jackson", "CEO")
p.display()

class Children(Parent):
    gender =None

    def __init__(self, name, job, gender):
        super().__init__(name, job)
        self.gender = gender
    def display(self):
        print('name: {}, job: {}, gender: {}'.format(self.name, self.job, self.gender))

chil=Children("John Lee", "Nurse", "Male")
chil.display()