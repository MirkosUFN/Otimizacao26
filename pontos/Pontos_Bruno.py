import random
import matplotlib.pyplot as plt

def gerar_y(a, b, x):
    y = []
    for i in range(len(x)):
        y.append(a * x[i] + b)
    return y

def gerar_x():
    x = []
    for i in range(5):
        x.append(random.randint(0, 10))
    return x

def plotar_pontos(x, y):
    plt.figure(figsize=(8, 6))
    
    plt.plot(x, y, linestyle='-', color='b', label='Reta')
    plt.scatter(x, y, color='red', marker='o', label='Pontos Coletados')
    
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Representação Gráfica da Reta e Pontos')
    plt.grid(True)

    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i] + 0.1, f'P{i+1}({x[i]}, {y[i]})', fontsize=9)

    plt.legend()
    plt.show()

a = 2
b = 4

x = gerar_x()
x.sort()

y = gerar_y(a, b, x)

print("--- COORDENADAS GERADAS ---")
print(f"Valores de X: {x}")
print(f"Valores de Y: {y}")
print("---------------------------")

plotar_pontos(x, y)
