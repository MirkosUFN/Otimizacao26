import matplotlib.pyplot as plt
import numpy as np

def plotar_reta_matematica():
    # Cria 10 valores espaçados igualmente entre 0 e 10 para o eixo X
    x = np.linspace(0, 10, 10)
    
    # Define os valores do eixo Y usando uma equação de reta (ex: y = 2x + 1)
    y = 2 * x + 1
    
    # Cria o gráfico de linha (reta)
    plt.plot(x, y, color='blue', marker='o', label='Reta: y = 2x + 1')
    
    # Formatação do gráfico
    plt.title('Gráfico de uma Reta Simples')
    plt.xlabel('Valores de X')
    plt.ylabel('Valores de Y')
    plt.grid(True)     # Adiciona a grade ao fundo
    plt.legend()       # Mostra a legenda
    
    # Exibe o gráfico na tela
    plt.show()

# Executa a função
plotar_reta_matematica()