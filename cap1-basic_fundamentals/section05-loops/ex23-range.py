# Range => returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and ends at a specified number.
#
# https://www.w3schools.com/python/python_for_loops.asp

print(list(range(1, 11))) # Array from 1 to 10
print()

# Range
for n in range(5): # 0 to 4
    print(n)
print()

for n in range(3, 8): # 3 to 7
    print(n)
print()

# Range with 3 arguments => 3rd argument defines the jumps

for n in range(1, 13, 3): # Will be jumping 3 numbers: 1, 4, 7, 10
    print(n)
print()

# Inverse range
for n in range(5, 0, -1): # 5 to 1
    print(n)
print()