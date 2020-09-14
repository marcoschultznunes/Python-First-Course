#   Sets => Unrepeatable elements

#   - Sets are unordered, so you cannot be sure in which order the items will appear
#   - Sets are unindexed, so you cannot access a specific element

s = {'Tree', 'Dog', 'Plant', 'Pizza', 'Cellphone'}

for e in s:
    print(e)

print(type(s))
print('')

# Add => add 1 element
s.add('Park')
print(s)

# Update => add multiple elements
s.update(['Chair', 'Toothbrush', 'Sandwich']) # Takes a list instead of multiple params
print(s)
print('')

# Remove => causes an error if fails
s.remove('Chair')
print(s)

# Discard => ignored if fails
s.discard('Walrus')
print(s)

# Other functions:
#
# Union => set1.union(set2)
# Set Constructor => thisset = set(("apple", "banana", "cherry"))
#
# https://www.w3schools.com/python/python_sets.asp