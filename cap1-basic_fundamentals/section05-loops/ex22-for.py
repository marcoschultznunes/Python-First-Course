# Behaves very differently from other languages. 
# it is more like a foreach.


# Numbered
a = [1, 4, 16, 64, 256]

for n in range(4, 11): # 4 to 10
    print(n)

print()

for n in range(len(a)): # 0 to the last index of the array
    print(a[n])

print()


# Foreach
phrase = "Hello There"

for char in phrase: # Foreach replacement
    print(char)
