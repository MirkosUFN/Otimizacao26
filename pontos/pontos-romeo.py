import random
import matplotlib.pyplot as plt

# Função para calcular os valores de y usando y = ax + b
def gerar_y(a, b, x):
    y = []
    for i in range(len(x)):
        y.append(a * x[i] + b)
    return y

# Função para gerar 5 valores aleatórios de x
def gerar_x():
    x = []
    for i in range(5):
        x.append(random.randint(0, 10))
    return x

# Função para desenhar os pontos e a reta no gráfico
def plotar_pontos(x, y):
    plt.figure(figsize=(8, 6))
    
    # Desenha a reta
    plt.plot(x, y, linestyle='-', color='b', label='reta')
    
    # Desenha os pontos
    plt.scatter(x, y, color='red', marker='o', label='pontos')
    
    # Nome dos eixos
    plt.xlabel('X')
    plt.ylabel('Y')
    
    # Mostra grade no gráfico
    plt.grid(True)

    # Escreve o nome de cada ponto no gráfico
    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i] + 0.1, f'P{i+1}({x[i]}, {y[i]})')

    # Mostra a legenda
    plt.legend()
    plt.show()

# Valores da função y = 2x + 4
a = 2
b = 4

# Gera os valores de x
x = gerar_x()
x.sort()  # Organiza os valores em ordem crescente
print("Pontos de x:", x)

# Calcula os valores de y
y = gerar_y(a, b, x)
print("Pontos de y:", y)

# Mostra o gráfico
plotar_pontos(x, y)