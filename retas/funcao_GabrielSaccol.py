import matplotlib.pyplot as plt
import numpy as np

# Criar valores para o eixo x
x = np.linspace(0, 10, 100)

# Criar valores para o eixo y (uma função linear diferente)
y = 3 * x - 2

# Plotar a reta
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 3x - 2', color='red')
plt.title('Plot de uma Reta Diferente')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()
plt.show()
