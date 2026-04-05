import matplotlib.pyplot as plt


def coletar_pontos():
    pontos = []
    print("--- Traçador de Pontos ---")

    while True:
        try:
            x = float(input("Digite a coordenada X do ponto: "))
            y = float(input("Digite a coordenada Y do ponto: "))

            if (x, y) in pontos:
                print("Ponto duplicado, ignorado.")
            else:
                pontos.append((x, y))

            if input("Quer adicionar outro ponto? (s/n): ").strip().lower() != "s":
                break
        except ValueError:
            print("Por favor, digite um número válido.")

    return pontos


def plotar_pontos(pontos):
    if not pontos:
        print("Nenhum ponto para plotar.")
        return

    x_coords, y_coords = zip(*pontos)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.scatter(x_coords, y_coords, color="red", s=100, zorder=3, label="Pontos inseridos")

    for x, y in pontos:
        ax.annotate(
            f"({x}, {y})",
            (x, y),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=9,
            ha="left",
        )

    # Eixos cartesianos
    ax.axhline(0, color="black", linewidth=1.2)
    ax.axvline(0, color="black", linewidth=1.2)

    # Garante que a origem fique visível
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    margem_x = max((x_max - x_min) * 0.2, 1)
    margem_y = max((y_max - y_min) * 0.2, 1)
    ax.set_xlim(min(x_min - margem_x, -1), max(x_max + margem_x, 1))
    ax.set_ylim(min(y_min - margem_y, -1), max(y_max + margem_y, 1))

    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    ax.set_title("Visualização de Pontos no Plano Cartesiano")
    ax.legend()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    pontos = coletar_pontos()
    plotar_pontos(pontos)
