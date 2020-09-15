# 1. __init__ => constructor

# 2. __del__ => destruct. Also triggers when all objects are destroyed at the end of the execution

# 3. __repr__ => to string

# 4. __len__ => length

# 5. __add__ => Defines the return of a sum between 2 objects of that class

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __del__(self):
        print(f'Book "{self.title}" has been destroyed!')

    def __repr__(self):
        ret = ""

        for k, v in vars(self).items():
            ret += f"{k.title()}: {v} \n"
        
        return ret

    def __len__(self):
        return self.pages

    def __add__(self, other_book):
        return f'{self.title} & {other_book.title}'

b1 = Book('Lord of The Rings', 'Tolkkien', 500)
print(b1)

b2 = Book('Dom Casmurro', 'Machado de Assis', 200)

if len(b1) > len(b2): # __len__
    print(f'The book "{b1.title}" has more pages than "{b2.title}". \n')
else:
    print(f'The book "{b2.title}" has more pages than "{b1.title}". \n')

print(b1 + b2 + '\n') # __add__

# There are many other magic methods
# https://www.tutorialsteacher.com/python/magic-methods-in-python