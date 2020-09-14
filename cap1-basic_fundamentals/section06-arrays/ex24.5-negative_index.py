# In python you can get the elements from the end to the start of the array

arr = ['Oi', 'Hello', 'Hi', 'Guten Tag']

print(arr[-1]) # Prints last element
print(arr[-2]) # Second to last
print(arr[::-1]) # Reverse list
print(arr[-3:-1]) # Does not work properly, as last element is not included