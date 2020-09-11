# Arrays in Python => are called 'Lists'

words = ['gum', 'yellow', 'can', 'lantern', 'pine', 'tree']
print(words)
print(words[3])

words[3] = 'ball'
print(words)
print()

# Length => len()
print(len(words))
print()

# Append => add a new element at the end of the array
words.append('tea') # accepts only one param.
words.append(['dog', 'garden']) # this will put an array inside the array
print(words)

# Extend => add multiple elements at the end
words.extend(['house', 'fire', 'grade']) 
print(words)
print()

# Pop => remove items
words.pop() # No param => removes last item
words.pop(4) # Removes the item of specified index
print(words)
