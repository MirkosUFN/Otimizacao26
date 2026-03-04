import numpy as np
import matplotlib.pyplot as plt

def desenhar_retas(a1, b1, a2, b2):
    x = np.linspace(-10, 10, 200)

    y1 = a1 * x + b1
    y2 = a2 * x + b2

    plt.plot(x, y1, label=f"f(x) = {a1}x + {b1}", color="blue")
    plt.plot(x, y2, label=f"g(x) = {a2}x + {b2}", color="green")

    if a1 == a2:
        if b1 == b2:
            print("As retas são IDÊNTICAS!")
            plt.title("Retas Idênticas")
        else:
            print("As retas são PARALELAS!")
            plt.title("Retas Paralelas")
    else:
        print("As retas são CONCORRENTES!")
        plt.title("Retas Concorrentes")

        x_int = (b2 - b1) / (a1 - a2)
        y_int = a1 * x_int + b1

        print(f"Ponto de interseção: ({x_int:.2f}, {y_int:.2f})")

        plt.plot(x_int, y_int, 'ro', label="Interseção")

    # Desenho dos eixos
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

# Exemplos de teste:
# Retas paralelas
desenhar_retas(2, 1, 2, 4)

# Retas concorrentes
# desenhar_retas(2, 1, -1, 3)

# Retas idênticas
# desenhar_retas(2, 1, 2, 1)