# Multiple Inheritance => can be direct or indirect. Both of them have the same results

# Directly
class A:
    n1 = 4
class B:
    n2 = 9
class C:
    n3 = 16

class Son(A, B, C):
    pass # pass => In python, to write an empty block of code we must use the word 'pass'

s1 = Son()
print(f'{s1.n1}, {s1.n2}, {s1.n3}')

# Indirectly
class D:
    n1 = 25
class E(D):
    n2 = 36
class F(E):
    n3 = 49

class Son2(F):
    pass

s2 = Son2()
print(f'{s2.n1}, {s2.n2}, {s2.n3}')