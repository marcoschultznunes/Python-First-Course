a = True
b = False

print(type(a)) #bool
print(type(b)) #bool
print(a) #True
print(b) #False
print()

#Numbers
print(bool(0)) # 0 is the only number that converts to False
print(bool(1))
print(bool(15393))
print(bool(-24))
print()

#Strings
print(bool('')) # An empty string is the only that convert to False
print(bool('0')) # True
print(bool(' ')) # This string is not empty, as it has a space, therefore it is True
print(bool('Oi'))
print(bool('-2'))
print()

#Other
print(bool(None)) # False
print(bool()) # False
print()

#Not => in Python you must write 'not' instead of ! before the variable
print(not True)
print(not False)