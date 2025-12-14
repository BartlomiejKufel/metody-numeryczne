#Wzory
# Interpolacja Lagrange'a - https://pl.wikipedia.org/wiki/Interpolacja_wielomianowa#:~:text=.-,Wielomian%20Lagrange%E2%80%99a,-%5Bedytuj%20%7C
# https://chatgpt.com/share/693eb2d9-d1b0-8011-b984-9aa8ad9d76a1

from sympy import Symbol, Point, simplify

def Li(i):
    L = 1
    for j in range(len(P)):
        if j != i:
            L *= (x - P[j].x)/(P[i].x - P[j].x)

    return L

x = Symbol('x')
P = [Point(1,5), Point(2,7), Point(3,6)] # węzły

Wx =0

for i in range(len(P)):
    Wx += P[i].y * Li(i)

print(f"Interpolacja Lagrange'a: {simplify(Wx)}")

# Interpolacja Newtona - https://pl.wikipedia.org/wiki/Posta%C4%87_Newtona_wielomianu


# iloraz różnicowy
def diff(i, j):
    if i == j:
        return P[i].y
    return (diff(i+1, j) - diff(i, j-1)) / (P[j].x - P[i].x)

Wx = 0
product = 1

for i in range(len(P)):
    Wx += diff(0, i) * product
    product *= (x - P[i].x)

print(f"Interpolacja Newtona: {simplify(Wx)}")

