import matplotlib.pyplot as plt
#Anthony e Gabriel Teixeira
# y = ax + b
px1 = []
py1 = []
px2 = []
py2 = []


def equacao():
    px1.append(float(input("Digite o valor de X do Ponto 1: ")))
    py1.append(float(input("Digite o valor de Y do Ponto 1: ")))
    px2.append(float(input("Digite o valor de X do Ponto 2: ")))
    py2.append(float(input("Digite o valor de Y do Ponto 2: ")))


    a = (py2[0] - py1[0]) / (px2[0] - px1[0])
    b = py1[0] - a * px1[0]

    sinal_b = "+" if b >= 0 else "-"
    print(f"\n--- Resultado ---\nEquação da reta: y = {a:.2f}x {sinal_b} {abs(b):.2f}")

    return px1[0], py1[0], px2[0], py2[0], a, b


def desenhar(x1, y1, x2, y2, a, b):
    # pontos X para a linha ser mais longa que apenas a distância entre P1 e P2
    x_linha = [x1 - 3, x2 + 3]

    # equação y = ax + b
    y_linha = [(a * x) + b for x in x_linha]

    # desenhamos da reta
    plt.plot(x_linha, y_linha, color='blue', label='Reta')

    # desenho dos pontos
    plt.scatter([x1, x2], [y1, y2], color='red', zorder=5, label='Pontos P1 e P2')

    plt.axhline(0, color='black', linewidth=1)  # eixo X
    plt.axvline(0, color='black', linewidth=1)  # eixo Y
    plt.grid(True, linestyle='--')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    dados = equacao()
    if dados is not None:
        x1, y1, x2, y2, a, b = dados
        desenhar(x1, y1, x2, y2, a, b)