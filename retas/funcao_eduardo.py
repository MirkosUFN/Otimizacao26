import numpy as np
import matplotlib.pyplot as plt

def funcao_primeiro_grau(a, b, x):
    return a * x + b

def gerar_valores_x(inicio, fim, quantidade):
    return np.linspace(inicio, fim, quantidade)

def plotar_reta(a, b, inicio=-10, fim=10, pontos=10):
    x = gerar_valores_x(inicio, fim, pontos)
    y = funcao_primeiro_grau(a, b, x)

    plt.plot(x, y)
    plt.title(f"f(x) = {a}x + {b}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()

# Teste
plotar_reta(2, 1)
