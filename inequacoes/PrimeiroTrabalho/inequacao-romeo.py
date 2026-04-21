import numpy as np
import matplotlib.pyplot as plt

def plotar_inequacao(a, b, operador):
    """
    Plota a reta y = ax + b e preenche a área de solução da inequação.
    
    Parâmetros:
    a (float): Coeficiente angular.
    b (float): Coeficiente linear.
    operador (str): Inequação a ser avaliada ('>', '<', '>=', '<=').
    """
    # 1. Validação e Configuração de Estilo
    operadores_validos = {
        '>': ('--', 'acima'),
        '<': ('--', 'abaixo'),
        '>=': ('-', 'acima'),
        '<=': ('-', 'abaixo')
    }

    if operador not in operadores_validos:
        raise ValueError("Operador inválido! Use '>', '<', '>=', ou '<='.")

    estilo_linha, direcao = operadores_validos[operador]

    # 2. Definição do Domínio (valores de x)
    x = np.linspace(-10, 10, 400)

    # 3. Cálculo da Função da Reta
    y = a * x + b

    # 4. Inicialização do Gráfico
    fig, ax = plt.subplots(figsize=(8, 6))

    # Desenho dos eixos cartesianos (X=0 e Y=0)
    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)

    # 5. Plotagem da Reta
    # Formata o texto da equação para a legenda e título
    sinal_b = f'+ {b}' if b >= 0 else f'- {abs(b)}'
    equacao_label = f'{a}x {sinal_b}'
    
    ax.plot(x, y, linestyle=estilo_linha, color='blue', linewidth=2, label=f'Reta: y = {equacao_label}')

    # 6. Preenchimento da Região Solução
    # Usamos valores altos para garantir que o preenchimento vaze além da tela visível
    y_lim_sup = y + 100 
    y_lim_inf = y - 100

    if direcao == 'acima':
        ax.fill_between(x, y, y_lim_sup, color='lightblue', alpha=0.4, label='Área de Solução')
    else:
        ax.fill_between(x, y, y_lim_inf, color='lightblue', alpha=0.4, label='Área de Solução')

    # 7. Ajustes Finais e Renderização
    ax.set_title(f'Solução da Inequação: y {operador} {equacao_label}', fontsize=14, fontweight='bold')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-20, 20) # Limites fixos para melhor visualização
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.legend()

    plt.show()

# Exemplos de Teste (Basta descomentar para rodar)
plotar_inequacao(2, 3, '>=')
# plotar_inequacao(-1, 5, '<')
# plotar_inequacao(0.5, -2, '>')