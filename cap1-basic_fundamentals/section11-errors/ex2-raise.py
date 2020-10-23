# In python 'throw' is 'raise'

def divide(n, div):
    if div == 0:
        raise ValueError('Divisor must not be 0') # Error with message
    else:
        return n/div

print(divide(5, 2))
print(divide(10, 7))
print(divide(31, 4))

try:
    print(divide(5, 0))
except ValueError as e: # To grab the error
    print(e) # And display the error message