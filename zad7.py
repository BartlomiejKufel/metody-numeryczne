#link do wzorów
#https://eduinf.waw.pl/inf/alg/004_int/0003.php
from sympy import Symbol, sqrt


def define_parts(n, a, b):
    result = []

    for i in range(0,n+1):
        result.append(a + (i/n)*(b-a))

    return result


x = Symbol('x')

a = 0
b = 1
f =  sqrt(1+x)
n=3
parts = define_parts(n, a, b)

h = (b - a) / n
s=0
for i in range(1, n):
    s += f.subs(x, parts[i])

s += (f.subs(x, a) + f.subs(x, b))/2
s *= h
print(f"całka[{a},{b}] = {f} * dx")
print(f"całka[{a},{b}] ≈ {float(s)}")
