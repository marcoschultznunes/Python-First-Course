# Dictionaries => Collection that works like an associative array and resembles a JSON

u1 = {
    'login' : 'Xabá Jubilau',
    'password' : 'cachacha lampola',
    'rights' : 'user'    
}

print(u1)

# Accessing the values by key
print(u1['password'])

u1['login'] = 'Xaveco Peteco'
print(u1.get('login'))
print()

# Add and remove items
u1['dog'] = 'Milongas' # Add
print(u1)
u1.pop('dog') # Remove
print(u1)
print()

# Loop keys
for k in u1:
    print(k)
print()

# Loop values
for k in u1:
    print(u1[k])
print()

for v in u1.values():
    print(v)
print()

# Loop keys and values
for k, v in u1.items():
    print(f'{k} - {v}')
print()


# Check if key exists
if 'rights' in u1:
    print('Rights exists in u1')
print()