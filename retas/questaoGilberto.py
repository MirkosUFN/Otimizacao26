import matplotlib.pyplot as plt
import numpy as np

# função
def funcao(a, b, x):
    return a*x + b

# primeira reta
a1 = 5
b1 = -11

# segunda reta
a2 = -2
b2 = 4

# intervalo
x = np.linspace(-5, 5, 100)

# valores das funções
y1 = funcao(a1, b1, x)
y2 = funcao(a2, b2, x)

# cálculo do ponto de interseção
x_i = (b2 - b1) / (a1 - a2)
y_i = funcao(a1, b1, x_i)

print(f"Ponto de interseção: ({x_i:.2f}, {y_i:.2f})")

fig, ax = plt.subplots()

ax.plot(x, y1, label=f"f(x) = {a1}x + ({b1})")
ax.plot(x, y2, label=f"g(x) = {a2}x + ({b2})")

ax.plot(x_i, y_i, 'ro')
ax.annotate(f"({x_i:.2f}, {y_i:.2f})",
            (x_i, y_i),
            textcoords="offset points",
            xytext=(10,10))

ax.set_title("Interseção entre duas retas")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()

plt.show()