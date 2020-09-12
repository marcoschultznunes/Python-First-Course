sum = lambda n1, n2: n1+n2

print(sum(2, 3))

# https://www.w3schools.com/python/python_lambda.asp
def multiplier(m): 
    return lambda n: n*m 

mult2 = multiplier(2)
mult3 = multiplier(3)
mult4 = multiplier(4)

print(mult2(5))
print(mult3(27))
print()

# Map example
grades = [4.2, 5, 6.6, 7.2, 8.5, 3.5, 5.9, 6.9]
roundGrades = lambda g : round(g)

roundedGrades = list(map(roundGrades, grades))

print(roundedGrades)
print()