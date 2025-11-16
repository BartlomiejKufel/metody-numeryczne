from sympy import Symbol, exp, sin

x = Symbol('x')


a = -3
b = 1
f = sin(x) * exp(-3*x) + x ** 3 # exp = E do potęgi
print(f)

n = 5
h = (b - a)/(2 * n)
