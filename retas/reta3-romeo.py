import numpy as np
import matplotlib.pyplot as plt

def funcao(a, b, x):
    return a * x + b

# parâmetros das retas
a, b = 3, -9
c, d = 2, -10

# eixo x contínuo
x = np.linspace(-5, 5, 100)

# cálculo das funções
y1 = funcao(a, b, x)
y2 = funcao(c, d, x)

plt.figure(figsize=(10, 5))
plt.plot(x, y1, label=f'f(x) = {a}x + {b}')
plt.plot(x, y2, label=f'g(x) = {c}x + {d}')

# cálculo da interseção
if a != c:
    x_intersec = (d - b) / (a - c)
    y_intersec = funcao(a, b, x_intersec)

    plt.scatter(x_intersec, y_intersec)
    plt.annotate(f'({x_intersec:.2f}, {y_intersec:.2f})',
                 (x_intersec, y_intersec),
                 textcoords="offset points",
                 xytext=(10,10))

    plt.title("Retas concorrentes (1 ponto de interseção)")

elif a == c and b != d:
    plt.title("Retas paralelas (não possuem interseção)")

else:
    plt.title("Retas coincidentes (infinitos pontos em comum)")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.legend()
plt.show()