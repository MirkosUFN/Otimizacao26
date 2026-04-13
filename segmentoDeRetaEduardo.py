import random
import matplotlib.pyplot as plt

def gerar_y(a, b, x):
    """
    Calcula os valores do eixo Y com base na equação da reta (y = ax + b).
    
    Parâmetros:
    a (int/float): Coeficiente angular (define a inclinação da reta).
    b (int/float): Coeficiente linear (ponto onde a reta cruza o eixo Y).
    x (list): Lista contendo as coordenadas do eixo X.
    
    Retorna:
    list: Uma nova lista com os valores calculados de Y.
    """
    y = []
    for i in range(len(x)):
        y.append(a * x[i] + b)
    return y

def gerar_x():
    """
    Gera uma lista de 5 valores únicos e ordenados para o eixo X.
    
    Utiliza random.sample para garantir que não existam números duplicados
    no intervalo de 0 a 10. A lista é ordenada para que o desenho da 
    reta no gráfico seja contínuo da esquerda para a direita.
    
    Retorna:
    list: Lista de 5 números inteiros únicos e ordenados.
    """
    # range(0, 11) inclui os números de 0 até 10. 
    # O '5' indica a quantidade de números a serem escolhidos.
    x = random.sample(range(0, 11), 5)
    
    # Ordena a lista em ordem crescente para o gráfico ficar com uma linha reta
    x.sort() 
    
    return x

def plotar_pontos(x, y):
    """
    Desenha o plano cartesiano com a reta e destaca os pontos gerados.
    
    Parâmetros:
    x (list): Coordenadas do eixo X.
    y (list): Coordenadas do eixo Y calculadas previamente.
    """
    plt.figure(figsize=(8, 6))
    
    # Desenha a linha conectando os pontos
    plt.plot(x, y, linestyle='-', color='b', label='reta')
    
    # Desenha as bolinhas vermelhas em cima de cada coordenada exata
    plt.scatter(x, y, color='red', marker='o', label='pontos')
    
    # Nomeia os eixos
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True) # Adiciona a grade de fundo

    # Adiciona o texto 'P(x, y)' ao lado de cada ponto no gráfico
    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i] + 0.1, f'P{i+1}({x[i]}, {y[i]})')

    plt.legend() # Mostra a legenda (reta e pontos)
    plt.show() # Exibe o gráfico final

# --- Início do Programa Principal ---

# 1. Definição das constantes da equação da reta
a = float(input("Digite o valor do coeficiente 'a' (inclinação): "))
b = float(input("Digite o valor do coeficiente 'b' (interseção no eixo Y): "))

# 2. Geração das coordenadas sem repetição e ordenadas
x = gerar_x()
print(f"Pontos de X: {x}")

y = gerar_y(a, b, x)
print(f"Pontos de Y: {y}")

# 3. Chamada da função para desenhar o gráfico
plotar_pontos(x, y)