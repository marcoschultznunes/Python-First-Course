def br():
    print()

br()
print('Oi')
br()

# Function with params
def add(n1, n2):
    return n1 + n2

print(add(4, 8))
br()

# Multiple params
def addition(*nums):
    res = 0
    for n in nums:
        res += n
    return res

print(addition(5, 8, 7, 6))
br()

# Default value
def sayName(name = 'unknown person'):
    print(f"Hello {name}") # Variable in string

sayName()
sayName('Michael')
br()

# Pass list as param
arr = [2, 4, 6]
res = addition(*arr) # Need to write *list so that the list is turned into many params
print(res)
br()