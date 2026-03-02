import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    result = []
    for i in range(x0, x1 + 1):
        result.append((a * i) + b)
    return result

a = 5
b = -11
x0 = -2
x1 = 5

valores_y = funcao(a, b, x0, x1)
valores_x = list(range(x0, x1 + 1))

plt.plot(valores_x, valores_y, marker='o', linestyle='-', color='b', label='y = 5x - 11')
plt.title('Gráfico da Função Linear')
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')
plt.grid(True)
plt.legend()  
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1) 

plt.show()
