import random
import matplotlib.pyplot as plt

def gerar_y(a, b, x):
    """
    Calcula os valores de y usando a fórmula da reta.
    Fórmula: y = ax + b
    """
    y = []
    for i in range(len(x)):
        y.append(a * x[i] + b)
    return y


def gerar_x():
    """
    Gera 5 valores aleatórios sem repetir
    e organiza em ordem crescente.
    """
    x = random.sample(range(0, 11), 5)
    x.sort()
    return x


def plotar_pontos(x, y):
    """
    Mostra o gráfico da reta e destaca os pontos.
    """
    plt.figure(figsize=(8, 6))

    # Desenha a linha da reta
    plt.plot(x, y, linestyle='-', linewidth=2, label='Reta')

    # Marca os pontos no gráfico
    plt.scatter(x, y, color='red', label='Pontos')

    # Nome dos eixos
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')

    # Mostra a grade
    plt.grid(True)

    # Escreve o nome de cada ponto
    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i] + 0.1, f'P{i+1}({x[i]}, {y[i]})')

    # Mostra legenda
    plt.legend()

    # Exibe o gráfico
    plt.show()


# Programa principal
print("Gráfico da função do 1º grau")
print("Fórmula:", "y = ax + b")

# Recebe os valores digitados pelo usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

# Gera os valores de x
x = gerar_x()
print("Valores de x:", x)

# Calcula os valores de y
y = gerar_y(a, b, x)
print("Valores de y:", y)

# Mostra o gráfico
plotar_pontos(x, y)