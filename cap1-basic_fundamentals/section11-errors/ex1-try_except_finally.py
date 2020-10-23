# In python 'catch' is 'except'

import random

r = random.randint(1, 2) # 1-2

try: 
    if(r == 1): 
        print('1' + 3)
    else:
        print(int('Hello'))

except TypeError:
    print('Cannot convert add strings and numbers in Python')
except:
    print('Generic error')
    
finally:
    print(r)