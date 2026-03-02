import numpy as np
import matplotlib.pyplot as plt

def desenhar_retas(a1, b1, a2, b2):
    # Cria valores de x no intervalo de -1 até 1
    x = np.linspace(-10, 10, 100)

    # Calcula y para cada reta
    y1 = a1 * x + b1
    y2 = a2 * x + b2

    # Plota a reta
    plt.plot(x, y1, label=f"f(x) = {a1}x + {b1}")
    plt.plot(x, y2, label=f"f(x) = {a2}x + {b2}")

    # Verificação
    if a1 == a2:
        if b1 == b2:
            print("As retas são idênticas!")
        else:
            print("As retas são paralelas!")
    else:
        print("As retas são concorrentes!")
        # Calcular ponto de intersecção
        x_int = (b2 - b1) / (a1 - a2)
        y_int = (a1 * x_int + b1)
        print(f"Ponto de intersecção: ({x_int}, {y_int})")
        plt.plot(x_int, y_int, marker='o', color='red', label="Interseção")

    # Desenha os eixos do plano cartesiano
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Configurações do gráfico
    plt.title("Gráfico de duas retas")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Exibe o gráfico
    plt.show()

desenhar_retas(2,1,2,4)