import matplotlib.pyplot as plt
import numpy as np

def resolver_sistema_inequacoes(inequacoes):
    x = np.linspace(0, 10, 400)
    y = np.linspace(0, 10, 400)
    X, Y = np.meshgrid(x, y)

    # Começa com tudo como válido
    regiao = np.ones_like(X, dtype=bool)

    # Aplicar inequações
    for a, b, c, sinal in inequacoes:
        if sinal == '<=':
            cond = a * X + b * Y <= c
        elif sinal == '>=':
            cond = a * X + b * Y >= c
        elif sinal == '<':
            cond = a * X + b * Y < c
        elif sinal == '>':
            cond = a * X + b * Y > c
        else:
            print(f"Sinal inválido: {sinal}")
            return
        
        regiao &= cond

    # Restrição ao 1º quadrante
    regiao &= (X >= 0)
    regiao &= (Y >= 0)

    plt.figure(figsize=(8, 6))

    # Pintar região válida
    plt.contourf(X, Y, regiao, levels=[0.5, 1], alpha=0.4)

    # Plotar retas
    for a, b, c, sinal in inequacoes:
        estilo = '--' if sinal in ['<', '>'] else '-'

        if b != 0:
            y_reta = (c - a * x) / b
            plt.plot(x, y_reta, linestyle=estilo, linewidth=2)
        else:
            x_reta = c / a
            plt.axvline(x_reta, linestyle=estilo, linewidth=2)

    # Eixos
    plt.axhline(0)
    plt.axvline(0)

    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid(True)
    plt.title("Região solução (1º quadrante)")

    plt.show()


if __name__ == "__main__":
    inequacoes = []

    try:
        n = int(input("Quantas inequações deseja inserir? "))

        for i in range(n):
            print(f"\nInequação {i+1}: formato ax + by ? c")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            sinal = input("Digite o sinal (>, >=, <, <=): ")

            inequacoes.append((a, b, c, sinal))

        resolver_sistema_inequacoes(inequacoes)

    except ValueError:
        print("Erro: entrada inválida.")
