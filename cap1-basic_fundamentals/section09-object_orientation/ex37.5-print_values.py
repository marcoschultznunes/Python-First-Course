class Person:
    def __init__(self, height, peso, gender):
        self.height = height
        self.peso = peso
        self.gender = gender

p1 = Person(1.82, 81, 'M')

print(vars(p1)) # vars => Converts object attributes to dictionary
print(type(vars(p1))) # Dictionary

for v in vars(p1).values():
    print(v)