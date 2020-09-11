import random

a = random.randint(10, 31)

while a > 0:
    if a % 5 == 0:
        break # Stops the loop entirely
    print(a)
    a -= 1

print()

a = random.randint(10, 31)

while a > 0:
    
    if a % 5 == 0:
        a -= 1
        continue # Skips current iteration

    print(a)
    a -= 1