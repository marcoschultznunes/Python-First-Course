class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1    
        self.id_person = Person.count

    def present_person(self):
        print(f'Person number {self.id_person}: {self.name}')

p1 = Person('Nappa', 28)
p2 = Person('Carl', 30)
p3 = Person('Tomas', 45)

p1.present_person()
p2.present_person()
p3.present_person()

class Professor(Person): # Class child (Class Mother)
    count = 0

    def __init__(self, name, age, discipline):
        super().__init__(name, age) # Super Constructor
        self.discipline = discipline
        Professor.count += 1
        self.id_professor = Professor.count
        
    def present_professor(self):
        print(f'Professor number {self.id_professor}: {self.name}')

p4 = Professor('Tiago', 62, 'Math')
p5 = Professor('Jagos', 42, 'Chemistry')
p6 = Person('Tom', 31)
p7 = Professor('Toni', 26, 'Portuguese')

p4.present_person()
p4.present_professor()
p5.present_professor()
p6.present_person()
p7.present_professor()