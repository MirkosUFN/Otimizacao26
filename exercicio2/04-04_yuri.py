import numpy as np
import matplotlib.pyplot as plt

def funcao(a, b, x):
    return a * x + b

a, b = 2, 4

x = np.random.randint(0, 11, size=5) 
x.sort()

y = funcao(a, b, x)

print(f'x: {x}')
print(f'y: {y}')

plt.scatter(x, y, color='red', label='Pontos Aleatórios') 
plt.plot(x, y, linestyle='-', color='b', label=f'Reta y = {a}x + {b}')

plt.title('Gráfico com Pontos Aleatórios')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.legend()
plt.show()
