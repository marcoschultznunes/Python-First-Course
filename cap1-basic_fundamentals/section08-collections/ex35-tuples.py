#   Tuples => Unchangeable Lists

#   - You cannot change the values of tuples without converting it to a list first
#   - Behaves like a frozen list
#   - Cannot be sorted

tp = ('Aces', 'Clubs', 'Hearts', 'Diamonds')
print(tp[3])
print(tp)

# Join two tuples
tp2 = ('Joker', ) # Single item tuple: Needs a ',' after the value so that it isn't a string
tp3 = tp + tp2
print(tp3)

# Converting to list to modify
tp4 = list(tp3)
tp4.sort()
tp3 = tuple(tp4)
print(tp3)