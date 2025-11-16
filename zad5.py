def function(x):
    return pow(x,3)+ pow(x,2)-3*x-3

def new_x(x, xn):
    return x - function(x) * ((xn - x)/(function(xn) - function(x)))


E = 0.0001
section = [1,2]

xn = section[0]
xn1 = section[1]

n=0
print(f"x{n} = {xn}; f(x{n}) = {function(xn)}")
n=1
print(f"x{n} = {xn1}; f(x{n}) = {function(xn1)}")
n=2
if function(xn) * function(xn1) < 0:
    while True:
        print(f"x{n} = {new_x(xn, xn1)}; f(x{n}) = {function(new_x(xn, xn1))}")
        xn,xn1 = xn1, new_x(xn, xn1)
        n+=1
        if abs(function(xn1)) <= E:  # warunek wyjścia
            break
