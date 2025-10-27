import math

def function(x):
    return math.sin(x)-(x/2)

#pochodna 1 stopnia
def derivative1_function(x):
    return math.cos(x)-(1/2)

#pochodna 2 stopnia
def derivative2_function(x):
    return -math.cos(x)

E = 0.01
section = [(math.pi/2),math.pi]
n=0
x=0

if function(section[0]) * function(section[1]) < 0:

    #wybranie, która połowa będzie x0
    if function(section[0]) * derivative2_function(section[0]) > 0:
        x = section[0]
    elif function(section[1]) * derivative1_function(section[1]) > 0:
        x = section[1]

    print(f"x{n} = {x}")
    while True:
        xn = x - (function(x)/derivative1_function(x)) #obliczenie xn+1
        x = xn #ustawienie nowego xn
        n+=1
        print(f"x{n} = {xn}")

        if abs(function(xn)) <= E: #warunek wyjścia
            break
