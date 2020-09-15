# MRO => Method Resolution Order:
#   The property that is the first param in an inheritance has the highest MRO

class A:
    def say(self): 
        print('Oi')

class B:
    def say(self):
        print('Hello')

class C:
    def say(self):
        print('Ola')

class D(A, B, C): # First param (A) => highest MRO
    pass

d1 = D()
d1.say() # Prints "Oi" => A.say()

print(D.__mro__) # View the MRO of the class. In this case, A > B > C


class E(B, C, A): # First param (B) => highest MRO
    pass

e1 = E()
e1.say() # Prints "Hello" => B.say()

