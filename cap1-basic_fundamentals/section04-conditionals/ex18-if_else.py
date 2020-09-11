import random

#if '8' > 5 : => Error: String and Int cannot even be compared this way in python
if 8 > 5 :
    print('8 > 5')
else:
    print('5 > 8')

print()

# elif => Replaces else if (because why not.)
a = random.randint(-5, 6)

if(a < 0):
    print('A é negativo') 
elif(a == 0):
    print('A é 0')
else:
    print('A é positivo')
    