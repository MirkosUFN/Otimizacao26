import matplotlib.pyplot as plt
import random

def criar_grafico_aleatorio(a, b):
    # 1. Gerar 5 valores de X aleatórios sem repetir e colocar em ordem
    x_pontos = sorted(random.sample(range(-10, 11), 5))
    
    # 2. Calcular os valores de Y usando a fórmula y = ax + b
    y_pontos = []
    for x in x_pontos:
        resultado_y = a * x + b
        y_pontos.append(resultado_y)
    
    # 3. Configurar o desenho
    plt.figure(figsize=(8, 5))
    
    # Desenha a linha que passa pelos pontos
    plt.plot(x_pontos, y_pontos, color='blue', label=f'Reta: y = {a}x + {b}')
    
    # Desenha os 5 pontos específicos em vermelho
    plt.scatter(x_pontos, y_pontos, color='red', zorder=5, label='Pontos Sorteados')

    # Adiciona rótulos com as coordenadas de cada ponto
    for i in range(5):
        plt.text(x_pontos[i], y_pontos[i] + 0.5, f'({x_pontos[i]}, {y_pontos[i]})')

    # Desenha os eixos principais (X e Y)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Finalização do gráfico
    plt.title("Reta Gerada com 5 Pontos Aleatórios")
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()

# Definindo os coeficientes e chamando a função
inclinação = 2 # Coeficiente 'a'
altura = 3     # Coeficiente 'b' (onde corta o eixo Y)

criar_grafico_aleatorio(inclinação, altura)