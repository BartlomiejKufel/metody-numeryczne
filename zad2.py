a = int(input("Podaj a, dla dwumianu: "))

#G(x) = x-a
if a > 0:
    print(f"G(x) = x-{a}")
else:
    print(f"G(x) = x+{a*-1}")

n = int(input("Podaj ilość współczynników wielomianu: "))
primalW = [] #wielomian przed
polynomial = "W(x) =" #polynomial oznacza wielomian
for i in range(n):
    primalW.append(int(input(f"Podaj współczynnik dla x^{n - i - 1}: ")))

    if primalW[i]==0:
        polynomial += ""
    elif i == 0:
         polynomial += f"{primalW[i]}x^{n - i - 1}"
    elif i == n-1:
        polynomial += f" {'+' if primalW[i] >= 0 else ''}{primalW[i]}"
    else:
        polynomial += f" {'+' if primalW[i] >= 0 else ''}{primalW[i]}x^{n - i - 1}"


print(polynomial)

result = "W(x) = ("
afterW = [] #wielomian po
for i in range(n):
    if i == 0:
        afterW.append(primalW[i])
    else:
        afterW.append(a * afterW[i-1] + primalW[i])

for i in range(n-1):

    if afterW[i] == 0:
        polynomial += ""
    elif i == 0:
        result += f"{afterW[i]}x^{n - i - 2}"
    elif i == n-2:
        result += f" {'+' if afterW[i] >= 0 else ''}{afterW[i]}"
    else:
        result += f" {'+' if afterW[i] >= 0 else ''}{afterW[i]}x^{n - i - 2}"

result +=")"


if a > 0:
    result += f"(x-{a})"
else:
    result += f"(x+{a*-1})"

if afterW[n-1] != 0:
    result += f" {'+' if afterW[n - 1] > 0 else ''}{afterW[n - 1]}"


print(result)