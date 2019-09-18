import math
def f(x):
    return int(2**(b-x**2))* 10**(-9) 
un, b = input().split()
un = float(un)
b = float(b)
for _ in range(10**12):
        un1 = un
        un = f( un1)
print(un + un1)