import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Identificação do problema
    print("1. Formulação do Problema de Programação Linear")
    print("Objetivo: Maximizar Z = 4*x1 + 3*x2 (Impacto Científico)")
    print("Sujeito a:")
    print("  3*x1 + 1*x2 <= 18   (Tempo de GPU - horas)")
    print("  1*x1 + 2*x2 <= 16   (Armazenamento - TB)")
    print("  x1, x2 >= 0         (Não-negatividade)\n")

    # 2. Resolução geométrica
    # Definindo intervalo de x1
    x1 = np.linspace(0, 10, 400)

    # Isolando x2 nas equações das restrições para plotar:
    # 3*x1 + x2 <= 18  => x2 <= 18 - 3*x1
    x2_gpu = 18 - 3 * x1

    # x1 + 2*x2 <= 16  => x2 <= (16 - x1) / 2
    x2_storage = (16 - x1) / 2

    # Plotando as linhas das restrições
    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_gpu, label='3*x1 + x2 = 18 (GPU)', color='blue')
    plt.plot(x1, x2_storage, label='x1 + 2*x2 = 16 (Armazenamento)', color='green')

    # Região viável
    # A região viável precisa respeitar x2 <= x2_gpu e x2 <= x2_storage
    x2_max = np.minimum(x2_gpu, x2_storage)
    
    # A região só é válida se os valores forem positivos (x1 >= 0 e x2 >= 0)
    plt.fill_between(x1, 0, x2_max, where=(x2_max >= 0) & (x1 >= 0), 
                     color='gray', alpha=0.3, label='Região Viável')

    # Eixos x e y (restrições de não-negatividade)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Cálculo dos vértices da região viável:
    # O(0, 0): Origem
    # A(0, 8): Eixo Y limitando pelo Armazenamento (16/2)
    # B(4, 6): Interseção do GPU e Armazenamento -> 3x1 + x2 = 18 e x1 + 2x2 = 16
    # C(6, 0): Eixo X limitando pela GPU (18/3)
    vertices = [
        (0, 0),
        (0, 8),
        (4, 6),
        (6, 0)
    ]

    # 3. Determinar combinação ideal (ponto extremo que maximiza o impacto)
    print("3. Avaliação dos vértices e combinação ideal")
    melhor_x1, melhor_x2 = 0, 0
    impacto_maximo = -1

    for c_x1, c_x2 in vertices:
        impacto = 4 * c_x1 + 3 * c_x2
        print(f"Vértice ({c_x1}, {c_x2}) -> Impacto: 4*({c_x1}) + 3*({c_x2}) = {impacto}")
        
        if impacto > impacto_maximo:
            impacto_maximo = impacto
            melhor_x1 = c_x1
            melhor_x2 = c_x2

    print(f"\n=> Solução ótima:")
    print(f"Modelos NLP (x1): {melhor_x1}")
    print(f"Modelos de Visão (x2): {melhor_x2}")
    print(f"Impacto Científico Máximo: {impacto_maximo}")

    # Destacando a solução ótima no gráfico
    plt.plot(melhor_x1, melhor_x2, 'ro', markersize=8, label=f'Solução Ótima ({melhor_x1}, {melhor_x2})')

    # Configurações estéticas do gráfico
    plt.xlim(-1, 10)
    plt.ylim(-1, 20)
    plt.xlabel('x1 (Modelos NLP)')
    plt.ylabel('x2 (Modelos de Visão Computacional)')
    plt.title('Interpretação Geométrica - Modelos de ML')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Exibir gráfico
    plt.show()

if __name__ == "__main__":
    main()
