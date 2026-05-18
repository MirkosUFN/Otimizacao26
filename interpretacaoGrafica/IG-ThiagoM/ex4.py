import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Identificação do problema
    print("1. Formulação do Problema de Programação Linear")
    print("Objetivo: Maximizar Z = 5*x1 + 4*x2 (Eficiência Energética)")
    print("Sujeito a:")
    print("  2*x1 + 3*x2 <= 18   (Área de Silício - mm²)")
    print("  2*x1 + 1*x2 <= 12   (Dissipação Térmica - mW)")
    print("  x1, x2 >= 0         (Não-negatividade)\n")

    # 2. Resolução geométrica
    x1 = np.linspace(0, 10, 400)

    # 2*x1 + 3*x2 <= 18 => x2 <= (18 - 2*x1) / 3
    x2_area = (18 - 2 * x1) / 3

    # 2*x1 + x2 <= 12   => x2 <= 12 - 2*x1
    x2_potencia = 12 - 2 * x1

    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_area, label='2*x1 + 3*x2 = 18 (Área)', color='blue')
    plt.plot(x1, x2_potencia, label='2*x1 + x2 = 12 (Potência)', color='green')

    x2_max = np.minimum(x2_area, x2_potencia)
    plt.fill_between(x1, 0, x2_max, where=(x2_max >= 0) & (x1 >= 0), color='gray', alpha=0.3, label='Região Viável')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Vértices calculados (interseções dos limites)
    vertices = [(0, 0), (0, 6), (4.5, 3), (6, 0)]

    print("3. Avaliação dos vértices e combinação ideal")
    melhor_x1, melhor_x2 = 0, 0
    eficiencia_maxima = -1

    for c_x1, c_x2 in vertices:
        eficiencia = 5 * c_x1 + 4 * c_x2
        print(f"Vértice ({c_x1}, {c_x2}) -> Eficiência: 5*({c_x1}) + 4*({c_x2}) = {eficiencia}")
        
        if eficiencia > eficiencia_maxima:
            eficiencia_maxima = eficiencia
            melhor_x1, melhor_x2 = c_x1, c_x2

    print(f"\n=> Solução ótima:")
    print(f"Blocos de Cache (x1): {melhor_x1}")
    print(f"ALUs (x2): {melhor_x2}")
    print(f"Eficiência Energética Máxima: {eficiencia_maxima}")

    plt.plot(melhor_x1, melhor_x2, 'ro', markersize=8, label=f'Solução Ótima ({melhor_x1}, {melhor_x2})')
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.xlabel('x1 (Blocos de Memória Cache)')
    plt.ylabel('x2 (ALUs)')
    plt.title('Interpretação Geométrica - Design de Hardware')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
