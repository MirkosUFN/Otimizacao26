import numpy as np
import matplotlib.pyplot as plt


def gerar_reta(x_vals, m, n):
    """Retorna os valores de y para a reta."""
    return m * x_vals + n


def obter_configuracao(operador):
    """Define estilo da linha e tipo de preenchimento."""
    if operador == '>':
        return '--', 'acima'
    elif operador == '<':
        return '--', 'abaixo'
    elif operador == '>=':
        return '-', 'acima'
    elif operador == '<=':
        return '-', 'abaixo'
    else:
        raise Exception("Operador inválido!")


def configurar_eixos(ax):
    """Desenha os eixos principais."""
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.grid(True, linestyle=':', alpha=0.6)


def draw_regiao(ax, x, y, modo):
    """Preenche a região da solução."""
    limite_superior = y.max() + 60
    limite_inferior = y.min() - 60

    if modo == 'acima':
        ax.fill_between(x, y, limite_superior, alpha=0.25)
    else:
        ax.fill_between(x, y, limite_inferior, alpha=0.25)


def inequacao_grafico(a, b, op):
    # 1. Validação e configuração inicial
    estilo_linha, direcao = obter_configuracao(op)

    # 2. Domínio
    valores_x = np.linspace(-10, 10, 300)

    # 3. Cálculo da função
    valores_y = gerar_reta(valores_x, a, b)

    # 4. Criação do gráfico
    figura, eixo = plt.subplots(figsize=(8, 5))

    configurar_eixos(eixo)

    # 5. Plot da reta
    eixo.plot(valores_x, valores_y, estilo_linha, label=f'{a}x + {b}')

    # 6. Região solução
    draw_regiao(eixo, valores_x, valores_y, direcao)

    # 7. Finalização
    eixo.set_title(f'y {op} {a}x + {b}')
    eixo.set_xlim(-10, 10)
    eixo.set_ylim(valores_y.min() - 5, valores_y.max() + 5)
    eixo.legend()

    plt.show()


# Teste
inequacao_grafico(2, 3, '>=')
