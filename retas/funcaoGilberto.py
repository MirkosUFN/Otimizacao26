# fx = ax + b
import matplotlib.pyplot as plt
import numpy as np

def funcao(a, b, x0, x1):
    x = np.arange(x0, x1 + 1)   
    y = a * x + b               
    return x, y

a = 5
b = -11
x0 = -2
x1 = 5

x, y = funcao(a, b, x0, x1)

print("x =", x)
print("f(x) =", y)

fig, ax = plt.subplots()

ax.plot(x, y, marker='o')
ax.set_title(f"Gráfico da função f(x) = {a}x + ({b})")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)

plt.show()