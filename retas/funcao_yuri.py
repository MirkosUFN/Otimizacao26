import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    result = []
    x_values = list(range(x0, x1 + 1))
    
    for x in x_values:
        result.append((a * x) + b)
    
    return x_values, result 

# Simulação y = 5x - 11 no intervalo [-2, 5]
x_coords, y_coords = funcao(5, -11, -2, 5)

plt.plot(x_coords, y_coords, marker='o', color='b', linestyle='-')
plt.title("Gráfico da Função $y = 5x - 11$")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.grid(True)
plt.show()