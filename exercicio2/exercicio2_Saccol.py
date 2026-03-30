import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

def calcular_reta(x1, y1, x2, y2):
    # Verifica se a reta é vertical
    if x1 == x2:
        return None, None
    
    # Coeficiente angular (a)
    a = (y2 - y1) / (x2 - x1)
    
    # Coeficiente linear (b)
    b = y1 - a * x1
  
    return a, b

def desenho(x1, y1, x2, y2, a, b):
    plt.scatter([x1, x2], [y1, y2], color='green', label='Pontos')
    
#Valores de X para a reta:
    x_vals = np.linspace(min(x1, x2) - 1, max(x1, x2) + 1, 100)
    
    if a is not None:
        y_vals = a * x_vals + b
        plt.plot(x_vals, y_vals, label='Reta')
    
    plt.grid(True)
    plt.legend()
    plt.show()

# Entrada do usuário
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

# Cálculo da reta
a, b = calcular_reta(x1, y1, x2, y2)

# Saída
if a is None:
    print(f"A reta é vertical: x = {x1}")
else:
    print(f"Equação da reta: y = {a:.2f}x + {b:.2f}")

# Desenho
desenho(x1, y1, x2, y2, a, b)
