# In Python, all attributes and functions are public

class Person:
    
    kind = 'Person' # STATIC Attribute

    def __init__(self, name, age, gender): # Constructor. Note the 'self' as the first argument
        self.name = name
        self.age = age
        self.gender = gender

    def present(self):
        print(self.name + " is a " + self.kind)

p1 = Person('Abel', 58, 'M') # Object
p1.present()
print(p1.gender)

p2 = Person('C3PO', 400, 'R') 
p2.kind = 'Robot' # Changes its private attribute to Robot
p2.present()
print(p2.gender)

p3 = Person('Jonas', 22, 'M')
p3.present() # Will still be a person

print()


Person.kind = 'Dog' # STATICALLY changes the class attribute (making 'dog' default for new objects)

p4 = Person('Rex', 8, 'M')
p4.present() # Dog

p5 = Person('Totó', 2, 'M')
p5.present()

print()


# Name Mangling => Use __attribute to denote that the attribute should be used as private