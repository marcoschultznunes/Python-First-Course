# In Python there is NO DO-WHILE loop. There is only while.
import random

b = random.randint(6, 14)

while b > 0:
    print(b)
    b -= 1 # There is also no decrement/increment ops. Use this instead.
