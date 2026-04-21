import matplotlib.pyplot as plt
import numpy as np

def resolver_inequacao(a, b, sinal):
    # Intervalo de valores de X
    x = np.linspace(-10, 10, 400)
    
    # Equação da reta
    y_reta = a * x + b

    # Limites do gráfico
    y_min = -10
    y_max = 10

    plt.figure(figsize=(8, 6))

    # Validação do sinal
    if sinal not in ['>', '>=', '<', '<=']:
        print("Sinal inválido!")
        return

    # Pintura da região
    if sinal == '>' or sinal == '>=':
        plt.fill_between(x, y_reta, y_max, alpha=0.4)
        descricao = f"y {sinal} {a}x + {b}"
    else:
        plt.fill_between(x, y_min, y_reta, alpha=0.4)
        descricao = f"y {sinal} {a}x + {b}"

    # Linha da reta (fronteira)
    estilo = '--' if sinal in ['>', '<'] else '-'
    plt.plot(x, y_reta, linestyle=estilo, linewidth=2, label='Fronteira')

    # Eixos
    plt.axhline(0)
    plt.axvline(0)

    # Configurações
    plt.xlim(-10, 10)
    plt.ylim(y_min, y_max)
    plt.grid(True)
    plt.title(f"Solução da inequação: {descricao}")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        sinal = input("Digite o sinal (>, >=, <, <=): ")

        resolver_inequacao(a, b, sinal)

    except ValueError:
        print("Erro: digite valores numéricos válidos.")
