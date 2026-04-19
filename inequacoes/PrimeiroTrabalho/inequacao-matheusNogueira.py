"""
=== OBJETIVO DO CÓDIGO ===

Construir um algoritmo que receba como parâmetros os valores de 'a' e 'b'
para a equação da reta y = ax + b, além do operador da inequação (>, >=, < ou <=).

Com base nesses parâmetros, o algoritmo desenha a área de solução para a
inequação resultante utilizando a biblioteca Matplotlib.


=== EXEMPLO DE USO ===

Para representar a inequação y >= 2x + 1:
- a = 2
- b = 1
- operador = '>='
O gráfico mostrará uma reta contínua e a área sombreada englobando todos os pontos do plano acima dela.
"""

import matplotlib.pyplot as plt
import numpy as np


def plotar_inequacao(a: float, b: float, operador: str) -> None: # Define as tipagens dos parâmetros e não retorna nada na função
    """
    Desenha o gráfico e a área de solução correspondente para a inequação y [operador] ax + b.
    
    Parâmetros:
      a (float): Coeficiente angular da reta.
      b (float): Coeficiente linear da reta.
      operador (str): Operador relacional ('>', '>=', '<', '<=').
    """
    # Define os pontos do eixo X e calcula os correspondentes em Y para a reta base
    valores_x = np.linspace(-10, 10, 400)
    valores_y_reta = a * valores_x + b
    
    plt.figure(figsize=(10, 6))
    
    # Define o estilo da reta: contínua se incluir a igualdade, tracejada se for estrita
    estilo_linha = '-' if '=' in operador else '--'
    rotulo_equacao = f'y = {a}x + {b}'
    
    plt.plot(valores_x, valores_y_reta, color='red', linestyle=estilo_linha, linewidth=2, label=rotulo_equacao)
    
    # Preenche a área de solução com base no operador
    limite_superior = valores_y_reta + 100
    limite_inferior = valores_y_reta - 100
    
    if '>' in operador:
        plt.fill_between(valores_x, valores_y_reta, limite_superior, color='skyblue', alpha=0.4, label='Espaço de Solução')
    elif '<' in operador:
        plt.fill_between(valores_x, valores_y_reta, limite_inferior, color='skyblue', alpha=0.4, label='Espaço de Solução')
    
    plt.axhline(0, color='black', linewidth=1)  # Origem Eixo X
    plt.axvline(0, color='black', linewidth=1)  # Origem Eixo Y
    
    plt.xlim([-10, 10])
    plt.ylim([min(valores_y_reta) - 5, max(valores_y_reta) + 5])
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title(f'Área de Solução para a Inequação: $y {operador} {a}x + {b}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    
    plt.show()


if __name__ == '__main__':
    print("--- Plotador de Inequações ---")
    valor_a = float(input("Digite o valor de 'a' (coeficiente angular): "))
    valor_b = float(input("Digite o valor de 'b' (coeficiente linear): "))
    sinal_operador = input("Digite o sinal da inequação (>, >=, <, <=): ")
    
    plotar_inequacao(valor_a, valor_b, sinal_operador)