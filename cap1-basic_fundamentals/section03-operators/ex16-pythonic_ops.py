# Is, In

# Is vs ==
print(1 is True) # False
print(1 == True) # True
print()

# is checks that 2 arguments refer to the same object, 
# == checks that 2 arguments have the same value.

# Just always use a == b except in two cases:
# For more readable comparisons to the singleton values like x is None.
# For mutable values, when you need to know whether mutating x will affect the y.



# In => Membership Operator

a = [20, 30, 55, 39]

print(39 in a) # True
print('20' in a) # False