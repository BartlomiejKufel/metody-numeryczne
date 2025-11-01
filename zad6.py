import math
import sympy as sp

def function(x):
    return 3*x - math.cos(x) - 1

def newX(a,b):
    return (a * function(b) - b * function(a)) / (function(b) - function(a))

E = 0.00001
section = [0.25, 0.75]

i = 1
xi = newX(section[0],section[1])
print(f"x{i} = {xi}; f(x{i}) = {function(xi)}")
if function(section[0]) * function(section[1]) < 0:
    while True:
        if function(section[0]) * function(xi) < 0:
            xi = newX(xi,section[0])
        elif function(section[1]) * function(xi) < 0:
            xi = newX(xi,section[1])

        i+=1
        print(f"x{i} = {xi}; f(x{i}) = {function(xi)}")
        if abs(function(xi)) <= E:  # warunek wyjścia
            break