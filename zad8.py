#link do wzorów
#https://eduinf.waw.pl/inf/alg/004_int/0002.php
from sympy import Symbol

def define_parts(n, a, b):
    result = []

    for i in range(0,n+1):
        result.append(a + (i/n)*(b-a))

    return result

x = Symbol('x')

a = 1
b = 4
f =  (0.06*(x**2))+2
n=3
parts = define_parts(n, a, b)

h = (b - a) / n
s=0

for i in range(n):
    s += f.subs(x, parts[i])

s *= h
print(f"całka[{a},{b}] = {f} * dx")
print(f"całka[{a},{b}] ≈ {float(s)}")
