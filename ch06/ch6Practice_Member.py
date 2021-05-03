#3
class Person:
    name=None
    gender=None
    age=0

    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    def display(self):
        if self.gender == 'female':
            self.gender = "female"
        else:
            self.gender = "male"
        print("Name: %s, Gender: %s"%(self.name, self.gender))
        print("Age:", self.age)

name = input('Name: ')
age = int(input('Age: '))
gender = input('Gender(male/female): ')

p = Person(name, gender, age)
p.display()