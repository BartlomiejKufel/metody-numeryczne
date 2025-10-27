E = 0.01
section = [0,1]
equation = [1,0,1,-1]# len-index równa się potędze x
approximations =[] #lista przyblizeń


def function(x):
    n = len(equation)
    result = 0
    for i in range(n):
        if i == n-1:
            result += equation[i]
        else:
            result += equation[i]*pow(x, n - i - 1)
    return result



if function(section[0]) * function(section[1]) < 0:
    print(f"Funkcja ma rozwiązanie w przedziale [{section[0]}; {section[1]}]")

    while True:
        xn = (section[0] + section[1]) / 2
        fxn = function(xn)
        approximations.append(fxn)

        if abs(fxn) < E :
            print(f"x{len(approximations)} = {xn}")
            print(f"Końcowy przedział: {section}")
            print(f"Lista przybliżeń: {approximations}")
            break
        elif fxn * function(section[0]) < 0:
            section[1] = xn
        elif fxn * function(section[1]) < 0:
            section[0] = xn



else:
    print(f"Funkcja nie ma rozwiązania w przedziale [{section[0]}; {section[1]}]")



