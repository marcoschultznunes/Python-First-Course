a = 'Zé Pikenow'

# Length => len(string)
print(len(a))
print()

# Slice 
print(a[0:4]) # Slice from 0 to 3 (the last parameter is reduced by 1) => 'biG'
print(a[4::]) # Slice from 4 to end => Chungus

#Obs: Python does not have an indexed string insert or replace.

# Char at
print(a[2]) # Char of index 2 => G
print()

# Split
print(a.split()) # Will split by word
print(a.split('u')) # Will split by every 'u', removing it
print(a.split('u', 1)) # Second parameter => maximum number of splits

# Other
print(a.upper())
print(a.lower())
print(a.capitalize()) # First letter to upper
print(a.title()) # Upper every word's first letter
print(a.replace('u', 'y')) # Replaces all ocurrences