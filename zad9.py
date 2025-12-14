# linki do wzorów
# https://chatgpt.com/s/t_6919d5e1c79c8191b7a381461cad3463
# https://pl.wikipedia.org/wiki/Ca%C5%82kowanie_numeryczne <- link do błędu
from sympy import Symbol, exp, sin, diff

def define_parts(n, a, b):
    result = []

    for i in range(0, n + 1):
        result.append(a + (i / n) * (b - a))

    return result

x = Symbol('x')


a = -3
b = 1
f = sin(x) * exp(-3*x) + x ** 3 # exp = E do potęgi


n = 4 #n musi być parzyste

if n % 2 == 0:
    h = (b - a)/ n
    parts = define_parts(n, a, b)

    s_even = 0 # suma parzystych indexów
    s_odd = 0 # suma nieparzystych indeksów
    for i in range(1, n):
        if i % 2 == 0:
            s_even += f.subs(x, parts[i])
        else:
            s_odd += f.subs(x, parts[i])

    s = f.subs(x, a) + f.subs(x, b) + (2 * s_even) + (4 * s_odd)
    s *= h/3

    print(f"całka[{a},{b}] = {f} * dx")
    print(f"całka[{a},{b}] ≈ {float(s)}")

    # Liczenie błędu
    f4 = diff(f,x,4)
    max_f4 = max(abs(f4.subs(x,a)), abs(f4.subs(x,b)))
    R = ((b-a)*h**4)/180 * max_f4
    print(f"Błąd ≈ {float(R)}")
else:
    print("n musi być parzyste")
