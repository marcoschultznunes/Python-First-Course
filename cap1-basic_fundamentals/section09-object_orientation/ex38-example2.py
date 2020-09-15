class Person:
    count = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def getPeopleCount(self):
        return Person.count

    def present(self):
        print('I am ' + self.name + '. I am ' + str(self.age) + ' years old.')

p1 = Person('Marcellus', 33)
p1.present()

p2 = Person('Toni', 42)
p2.present()

p3 = Person('Isabel', 51)
p3.present()

print('There are ' + str(Person.count) + ' people.')

p4 = Person('Luisão', 62)
p4.job = 'Mineirador' # Creating a dynamic attribute that only this object of the class has
p4.presentJob = lambda : print(f'I am {p4.name}. I am a {p4.job}')
p4.presentJob()