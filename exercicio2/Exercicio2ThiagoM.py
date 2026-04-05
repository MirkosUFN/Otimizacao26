import matplotlib.pyplot as plt
import numpy as np


def calcular_e_plotar_reta():
    print("--- Gerador de Equação da Reta ---")
    try:
        x1 = float(input("Digite x1: "))
        y1 = float(input("Digite y1: "))
        x2 = float(input("Digite x2: "))
        y2 = float(input("Digite y2: "))

        if x1 == x2 and y1 == y2:
            print("\nErro: Os pontos são idênticos, não é possível definir uma reta única.")
            return

        plotar_grafico(x1, y1, x2, y2)

    except ValueError:
        print("Erro: Por favor, insira apenas valores numéricos.")


def plotar_grafico(x1, y1, x2, y2):
    fig, ax = plt.subplots(figsize=(8, 6))

    vertical = (x1 == x2)

    if vertical:
        label_reta = f"x = {x1:.2f}"
        margem = abs(y2 - y1) * 0.5 or 5
        ax.axvline(x=x1, color="blue", label=label_reta)
        ax.set_ylim(min(y1, y2) - margem, max(y1, y2) + margem)
        print(f"\nReta Vertical: {label_reta}")
    else:
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1
        sinal = "+" if b >= 0 else "-"
        label_reta = f"y = {a:.2f}x {sinal} {abs(b):.2f}"
        print(f"\nEquação da reta: {label_reta}")

        margem = abs(x2 - x1) * 0.5 or 5
        x_range = np.linspace(min(x1, x2) - margem, max(x1, x2) + margem, 100)
        ax.plot(x_range, a * x_range + b, color="blue", label=label_reta)

  
    ax.scatter([x1, x2], [y1, y2], color="red", zorder=5, label="Pontos Informados")
    ax.annotate(f"({x1}, {y1})", (x1, y1), textcoords="offset points", xytext=(8, 6), fontsize=9)
    ax.annotate(f"({x2}, {y2})", (x2, y2), textcoords="offset points", xytext=(8, 6), fontsize=9)

    # Eixos cartesianos
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.grid(True, linestyle="--", alpha=0.7)
    ax.legend()
    ax.set_title("Gráfico da Reta")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    calcular_e_plotar_reta()
