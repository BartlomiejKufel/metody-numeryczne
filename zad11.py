from sympy import Symbol, Point, Matrix, simplify

P = [Point(0, 4),Point(3, 5),Point(6, 4),Point(9, 1),Point(12, 2)]

m = 3  # stopień wielomianu
n = len(P)
x = Symbol('x')

if n <= m:
    print(f"Do aproksymacji stopnia {m} potrzebujesz minimum {m+1} punktów")
else:
    sum_x = []
    for k in range(2*m + 1):
        sum_x.append(sum(p.x**k for p in P))

    sum_yx = []
    for k in range(m + 1):
        sum_yx.append(sum(p.y * p.x**k for p in P))

    A = []
    for i in range(m + 1):
        row = []
        for j in range(m + 1):
            row.append(sum_x[i + j])
        A.append(row)

    A = Matrix(A)
    B = Matrix(sum_yx)

    coeffs = A.solve(B)

    W = 0
    for i in range(m + 1):
        W += coeffs[i] * x**i

    print("Funkcja aproksymująca:")
    print(W, "\n")
