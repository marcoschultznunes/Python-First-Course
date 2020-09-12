def br():
    print()

# Kwargs => Requires named params and transforms them into a dictionary (Python collection)
# Dictionary => Associative array, JSON

# Kwargs => Keyword Arguments
def printUser(**kwargs):
    print(kwargs)

br()
printUser(name='Marcellus', country='Spain', job='Pope', age=52)
br()

# Print k, v in a dictionary
def printUserData(**kwargs):
    for k, v in kwargs.items():
        print(f'{k.title()} - {v}')

printUserData(name='Marcellus', country='Spain', job='Pope', age=52)
br()

# Pass dictionary as param
dic = {'name':'Josef', 'country':'Russia', 'job':'Baker', 'age':41}
printUserData(**dic) # Need to write **dictionary so that it is turned into many params
br()