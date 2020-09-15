# isinstance => Check if object belongs to class

class A:
    pass

class B:
    pass

o1 = A()
o2 = B()

print(isinstance(o1, A)) # True
print(isinstance(o1, B)) # False
print(isinstance(o2, B)) # True
print()

# issubclass => Check if class inherits another

class C:
    pass

class D:
    pass

class E(D):
    pass

print(issubclass(C, D)) # False
print(issubclass(D, E)) # False
print(issubclass(E, D)) # True