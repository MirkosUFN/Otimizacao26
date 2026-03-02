import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    result = []
    for x in range(x0, x1 + 1):
        result.append((a * x) + b)
    
    return result

a = 5
b = -11
x0 = -2
x1 = 5

valores_x = list(range(x0, x1 + 1))
valores_y = funcao(a, b, x0, x1)

plt.figure(figsize=(8, 5))
plt.plot(valores_x, valores_y, marker='o', linestyle='-', color='b', label=f'y = {a}x + {b}')

plt.title('Gráfico da Função Linear')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=1) # Eixo X central
plt.axvline(0, color='black', linewidth=1) # Eixo Y central
plt.legend()

plt.show()