from sympy import Matrix

def print_matrix(M):
    for row in M.tolist():
        print(row)

A = Matrix([
    [3, 0, 6],
    [1, 2, 8],
    [4, 5, -2]
])

b = Matrix([-12, -12, 39])
M = A.row_join(b)
n = M.rows

print("Macierz początkowa:")
print_matrix(M)

for k in range(n):
    max_row = max(range(k, n), key=lambda i: abs(M[i, k]))
    if max_row != k:
        M.row_swap(k, max_row)

    for i in range(k + 1, n):
        factor = M[i, k] / M[k, k]
        M.row_op(i, lambda v, j: v - factor * M[k, j])

    print(f"Po eliminacji w kolumnie {k+1}:")
    print_matrix(M)

x = [0] * n
for i in range(n - 1, -1, -1):
    s = sum(M[i, j] * x[j] for j in range(i + 1, n))
    x[i] = (M[i, n] - s) / M[i, i]

print("Rozwiązanie:")
for i, xi in enumerate(x):
    print(f"x{i+1} =", xi)
