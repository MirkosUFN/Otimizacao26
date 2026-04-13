import random
import matplotlib.pyplot as plt

def gerar_dados_x(quantidade, valor_min=0, valor_max=10):
    """Gera uma lista de valores aleatórios para X e os ordena."""
    x = [random.randint(valor_min, valor_max) for i in range(quantidade)]
    x.sort() 
    return x

def calcular_valores_y(lista_x, inclinação_a, intercepto_b):
    """Aplica a fórmula da função afim: y = ax + b."""
    return [inclinação_a * x_val + intercepto_b for x_val in lista_x]

def exibir_grafico(x, y, a, b):
    plt.figure(figsize=(10, 6))
    
    # Desenha a linha azul (reta) e os pontos vermelhos (dados)
    plt.plot(x, y, linestyle='--', color='blue', alpha=0.6, label=f'Reta: y = {a}x + {b}')
    plt.scatter(x, y, color='red', s=80, edgecolors='black', label='Pontos Calculados', zorder=5)

    # Adicionando os rótulos em cada ponto
    for i in range(len(x)):
        plt.text(x[i] + 0.2, y[i], f'({x[i]}, {y[i]})', fontsize=9, fontweight='bold')

    plt.title('Representação Gráfica da Função Linear', fontsize=14)
    plt.xlabel('Eixo X (Entrada)', fontsize=12)
    plt.ylabel('Eixo Y (Saída)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Definição dos coeficientes da função
    COEF_ANGULAR = 2  # Valor de 'a'
    COEF_LINEAR = 4   # Valor de 'b'
    QTD_PONTOS = 5    # Quantidade de amostras

    # Geração dos dados
    dados_x = gerar_dados_x(QTD_PONTOS)
    dados_y = calcular_valores_y(dados_x, COEF_ANGULAR, COEF_LINEAR)

    print(f"Valores de X: {dados_x}")
    print(f"Valores de Y: {dados_y}")

    exibir_grafico(dados_x, dados_y, COEF_ANGULAR, COEF_LINEAR)
