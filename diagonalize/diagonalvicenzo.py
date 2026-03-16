#x - 2y = 4
#3x + y = 2
a11, a12 = 1, -2
a21, a22 = 3, 1
b1, b2 = 4, 2

determinante = a11 * a22 - a12 * a21
x = (b1 * a22 - a12 * b2) /determinante
y = (a11 * b2 - b1 * a21) / determinante

print(f"x = {x}")
print(f"y = {y}")