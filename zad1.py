x = int(input("Podaj x: "))

print(f"x = {x}")


n = int(input("Podaj ilość współczynników wielomianu: "))
W = []
polynomial = "W(x) =" #polynomial oznacza wielomian
for i in range(n):
    W.append(int(input(f"Podaj współczynnik dla x^{n - i - 1}: ")))

    if W[i]==0:
        polynomial += ""
    elif i == 0:
         polynomial += f"{W[i]}x^{n - i - 1}"
    elif i == n-1:
        polynomial += f" {'+' if W[i] >= 0 else ''}{W[i]}"
    else:
        polynomial += f" {'+' if W[i] >= 0 else ''}{W[i]}x^{n - i - 1}"

print(polynomial)

result = 0

for i in range(n):
    if i == n-1:
        result += W[i]
    else:
        result += W[i]*pow(x, n - i - 1)

print(f"W({x}) = {result}")

