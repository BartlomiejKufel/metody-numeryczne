import math

def function(x):
    return 3*x - math.cos(x) - 1

def new_x(a, b):
    return (a * function(b) - b * function(a)) / (function(b) - function(a))

E = 0.00001
section = [0.25, 0.75]

n = 1
xn = new_x(section[0], section[1])
print(f"x{n} = {xn}; f(x{n}) = {function(xn)}")
if function(section[0]) * function(section[1]) < 0:
    while True:
        if function(section[0]) * function(xn) < 0:
            xn = new_x(xn, section[0])
        elif function(section[1]) * function(xn) < 0:
            xn = new_x(xn, section[1])

        n+=1
        print(f"x{n} = {xn}; f(x{n}) = {function(xn)}")
        if abs(function(xn)) <= E:  # warunek wyjścia
            break