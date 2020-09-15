# Polymorphism:

# Static: overloading => 2 functions with the same name, but different params
#
# Dynamic: Passing a generic class which multiple classes inherit as param. 
#   So you can pass any of those classes

# Static => does not work on Python
# Dynamic => Also does not work on Python, as you cannot declare type to function params


# The only type that works in python is overriding methods from inherited classes:
class Say:
    def __init__(self, name):
        self.name = name

    def say(self):
        print(f'{self.name}')

class SayFull(Say):
    def __init__(self, name, surname):
        super().__init__(name)
        self.surname = surname

    def say(self): # Overriding inherited function
        print(f'{self.name} {self.surname}')

p1 = SayFull('Dog', 'Johnson Davis')
p1.say()