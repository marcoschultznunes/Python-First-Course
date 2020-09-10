import random

#int
a=2

#float
b=4.5

#complex
c=2j


print(5/2) # 2.5
print(int(5/2)) # Casting. Floors the number.
print(int(6.9)) # Again, it floors.
print(float('5.5')) # Casting from String. int('5.5') would have caused an error.
print()

# Python does not have range limit for numbers. The limit is the computer's capability.
print(2**10000)
print()

# You can fill nums with underlines to separate thousands, millions, billions, etc.
print(1_000_000_000)
print()

#random number => from 1 to 3 (it excludes last number)
print(random.randrange(1, 4))