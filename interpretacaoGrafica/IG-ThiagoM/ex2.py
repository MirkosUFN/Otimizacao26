import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Identificação do problema
    print("1. Formulação do Problema de Programação Linear")
    print("Objetivo: Maximizar Z = 3*x1 + 5*x2 (QoS)")
    print("Sujeito a:")
    print("  2*x1 + 4*x2 <= 24   (Switch A)")
    print("  3*x1 + 2*x2 <= 22   (Switch B)")
    print("  x1, x2 >= 0         (Não-negatividade)\n")

    # 2. Resolução geométrica
    # Definindo intervalo de x1
    x1 = np.linspace(0, 15, 400)

    # Isolando x2 nas equações das restrições para plotar:
    # 2*x1 + 4*x2 <= 24  => x2 <= (24 - 2*x1) / 4
    x2_switch_a = (24 - 2 * x1) / 4

    # 3*x1 + 2*x2 <= 22  => x2 <= (22 - 3*x1) / 2
    x2_switch_b = (22 - 3 * x1) / 2

    # Plotando as linhas das restrições
    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_switch_a, label='2*x1 + 4*x2 = 24 (Switch A)', color='blue')
    plt.plot(x1, x2_switch_b, label='3*x1 + 2*x2 = 22 (Switch B)', color='green')

    # Região viável
    # A região viável precisa respeitar x2 <= x2_switch_a e x2 <= x2_switch_b
    x2_max = np.minimum(x2_switch_a, x2_switch_b)
    
    # A região só é válida se os valores forem positivos (x1 >= 0 e x2 >= 0)
    plt.fill_between(x1, 0, x2_max, where=(x2_max >= 0) & (x1 >= 0), 
                     color='gray', alpha=0.3, label='Região Viável')

    # Eixos x e y (restrições de não-negatividade)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Cálculo dos vértices da região viável:
    # O(0, 0): Origem
    # A(0, 6): Eixo Y limitando pelo Switch A
    # B(5, 3.5): Interseção do Switch A e Switch B -> 2x1 + 4x2 = 24 e 3x1 + 2x2 = 22
    # C(22/3, 0): Eixo X limitando pelo Switch B
    vertices = [
        (0, 0),
        (0, 6),
        (5, 3.5),
        (22/3, 0)
    ]

    # 3. Determinar combinação ideal (ponto extremo que maximiza o QoS)
    print("3. Avaliação dos vértices e combinação ideal")
    melhor_x1, melhor_x2 = 0, 0
    qos_maximo = -1

    for c_x1, c_x2 in vertices:
        qos = 3 * c_x1 + 5 * c_x2
        print(f"Vértice ({c_x1:.2f}, {c_x2:.2f}) -> QoS: 3*({c_x1:.2f}) + 5*({c_x2:.2f}) = {qos:.2f}")
        
        if qos > qos_maximo:
            qos_maximo = qos
            melhor_x1 = c_x1
            melhor_x2 = c_x2

    print(f"\n=> Solução ótima:")
    print(f"Stream Básico (x1): {melhor_x1:.2f} (em milhares)")
    print(f"Stream Premium (x2): {melhor_x2:.2f} (em milhares)")
    print(f"QoS Máximo: {qos_maximo:.2f}")

    # Destacando a solução ótima no gráfico
    plt.plot(melhor_x1, melhor_x2, 'ro', markersize=8, label=f'Solução Ótima ({melhor_x1:.2f}, {melhor_x2:.2f})')

    # Configurações estéticas do gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 10)
    plt.xlabel('x1 (Stream Básico - milhares)')
    plt.ylabel('x2 (Stream Premium - milhares)')
    plt.title('Interpretação Geométrica - QoS e Roteamento de Tráfego')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Exibir gráfico
    plt.show()

if __name__ == "__main__":
    main()
