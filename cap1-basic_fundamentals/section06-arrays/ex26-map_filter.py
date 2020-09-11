import math

# Map
nums = [1, 2, 4, 9, 16, 25, 36, 49]

sqrts = list(map(math.sqrt, nums))
print(sqrts)

# Filter
def isPair(n):
    return True if(n % 2 == 0) else False

pairs = list(filter(isPair, nums))
print(pairs)

# https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/