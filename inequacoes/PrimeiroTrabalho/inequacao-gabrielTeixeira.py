import numpy as np
import matplotlib.pyplot as plt


def obter_dados():
    print("=== Visualizador de Inequações Lineares ===")
    try:
        coef_angular = float(input("Coeficiente angular (a): "))
        coef_linear = float(input("Coeficiente linear (b): "))
        sinal = input("Operador (>, >=, <, <=): ").strip()
        
        if sinal not in ['>', '>=', '<', '<=']:
            raise ValueError("Operador inválido.")
        
        return coef_angular, coef_linear, sinal
    except ValueError as e:
        print(f"Erro: {e}")
        exit()


def calcular_reta(a, b):
    x = np.linspace(-10, 10, 400)
    y = a * x + b
    return x, y


def desenhar_grafico(x, y, a, b, operador):
    plt.figure(figsize=(9, 6))

    # define estilo da linha
    linha = '-' if '=' in operador else '--'

    plt.plot(x, y, color='red', linestyle=linha, label=f"y = {a}x + {b}")

    # área da inequação
    if operador in ['>', '>=']:
        plt.fill_between(x, y, y + 100, alpha=0.3, label="Região solução")
    else:
        plt.fill_between(x, y, y - 100, alpha=0.3, label="Região solução")

    # eixos
    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)

    # limites
    plt.xlim(-10, 10)
    plt.ylim(-20, 20)

    # estética
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.title(f"Inequação: y {operador} {a}x + {b}")
    plt.legend()

    plt.show()


def main():
    a, b, operador = obter_dados()
    x, y = calcular_reta(a, b)
    desenhar_grafico(x, y, a, b, operador)


if __name__ == "__main__":
    main()
