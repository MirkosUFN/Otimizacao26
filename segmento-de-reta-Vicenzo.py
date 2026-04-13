import matplotlib.pyplot as plt

def obter_coordenadas():
    listaCoord = []

    while True:
        try:
            val_x = float(input("Informe o valor para X: "))
            val_y = float(input("Informe o valor para Y: "))

            if (val_x, val_y) in listaCoord:
                print("Atenção: Coordenada já registrada. Pulando...")
            else:
                listaCoord.append((val_x, val_y))

            if input("Continuar inserindo? [s/n]: ").strip().lower() != "s":
                break
        except ValueError:
            print("Erro: Entrada inválida. Use apenas números.")

    return listaCoord

def gerar_grafico(dados):
    if not dados:
        print("Não há dados suficientes para criar o gráfico.")
        return

    eixo_x, eixo_y = zip(*dados)

    figura, plano = plt.subplots(figsize=(8, 6))

    plano.plot(eixo_x, eixo_y, color="blue", linewidth=1.5, zorder=2, label="Trajeto")
    plano.scatter(eixo_x, eixo_y, color="red", s=100, zorder=3, label="Locais marcados")

    for vx, vy in dados:
        plano.annotate(
            f"({vx}, {vy})",
            (vx, vy),
            textcoords="offset points",
            xytext=(6, 6),
            fontsize=9,
            ha="left",
        )

    plano.axhline(0, color="black", linewidth=1.2)
    plano.axvline(0, color="black", linewidth=1.2)

    min_x, max_x = min(eixo_x), max(eixo_x)
    min_y, max_y = min(eixo_y), max(eixo_y)
    espaçamento_x = max((max_x - min_x) * 0.2, 1)
    espaçamento_y = max((max_y - min_y) * 0.2, 1)
    
    plano.set_xlim(min(min_x - espaçamento_x, -1), max(max_x + espaçamento_x, 1))
    plano.set_ylim(min(min_y - espaçamento_y, -1), max(max_y + espaçamento_y, 1))

    plano.grid(True, linestyle="--", alpha=0.6)
    plano.set_xlabel("Abscissas (X)")
    plano.set_ylabel("Ordenadas (Y)")
    plano.set_title("Representação Gráfica das Coordenadas")
    plano.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    registro = obter_coordenadas()
    gerar_grafico(registro)