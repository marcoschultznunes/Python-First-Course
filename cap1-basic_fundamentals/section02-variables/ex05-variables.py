# Python is a STRONGLY TYPED language, but it is ALSO DYNAMICALLY TYPED, 
# with no type declaration and with type changing
#
# Ex: I cannot change the type of 1 by adding the string '12', 
# but I can choose what types i store in a variable and change that during the program's run time.
#
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed

print()


a = 10
print(a)
print(type(a)) # int

print()


a = 2.5
print(a)
print(type(a)) # float

print()


a = 3.8 + 4 # Ok.
print(a)
print(type(a)) # float

print()


a = 2 + '4' # Due to python's strong typing, this causes an error.
print(a)
print(type(a))

print('I am number ' + 1) # Also wrong for the same reason. Cannot concat an int/float to a string.