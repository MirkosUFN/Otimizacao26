import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Problema soclitiado
    print("1. Formulação do Problema de Programação Linear")
    print("Objetivo: Minimizar Z = 20*x1 + 50*x2")
    print("Sujeito a:")
    print("  4*x1 + 8*x2 >= 40   (vCPUs)")
    print("  8*x1 + 32*x2 >= 96  (RAM)")
    print("  x1 + x2 <= 12       (Total de instâncias)")
    print("  x1, x2 >= 0         (Não-negatividade)\n")

    # 2. Resolução geométrica
    x1 = np.linspace(0, 15, 400)

    # Isolando x2 nas equações das restrições para plotar:
    x2_vcpu = (40 - 4 * x1) / 8
    x2_ram = (96 - 8 * x1) / 32
    x2_total = 12 - x1

    # Plotando as linhas das restrições
    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_vcpu, label='4*x1 + 8*x2 = 40 (vCPU)', color='blue')
    plt.plot(x1, x2_ram, label='8*x1 + 32*x2 = 96 (RAM)', color='green')
    plt.plot(x1, x2_total, label='x1 + x2 = 12 (Total)', color='red')

    # Região viável
    x2_min = np.maximum(x2_vcpu, x2_ram)
    x2_min = np.maximum(x2_min, 0) # Não-negatividade
    
    plt.fill_between(x1, x2_min, x2_total, where=(x2_min <= x2_total) & (x1 >= 0), 
                     color='gray', alpha=0.3, label='Região Viável')

    # Eixos (Não negatividade)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Os vértices da região viável podem ser achados resolvendo os sistemas:
    # A(0, 12): Eixo Y com limite total
    # B(0, 5): Eixo Y com vCPU (0, 5) -> RAM nesse ponto = 32*5 = 160 (ok), Total = 5 (ok)
    vertices = [
        (0, 12), 
        (0, 5),  
        (8, 1),  
        (12, 0)  
    ]

    # 3. Determinar combinação ideal e custo mínimo
    print("3. Avaliação dos vértices e combinação ideal")
    melhor_x1, melhor_x2 = 0, 0
    custo_minimo = float('inf')

    for c_x1, c_x2 in vertices:
        custo = 20 * c_x1 + 50 * c_x2
        print(f"Vértice ({c_x1}, {c_x2}) -> Custo: 20*({c_x1}) + 50*({c_x2}) = ${custo}")
        
        if custo < custo_minimo:
            custo_minimo = custo
            melhor_x1 = c_x1
            melhor_x2 = c_x2

    print(f"\n=> Solução ótima:")
    print(f"Instâncias Standard (x1): {melhor_x1}")
    print(f"Instâncias High-Performance (x2): {melhor_x2}")
    print(f"Custo Mínimo: ${custo_minimo}")

    # Destacando a solução ótima no gráfico
    plt.plot(melhor_x1, melhor_x2, 'ro', markersize=8, label=f'Solução Ótima ({melhor_x1}, {melhor_x2})')

    # Configurações estéticas do gráfico
    plt.xlim(-1, 15)
    plt.ylim(-1, 15)
    plt.xlabel('x1 (Instâncias Standard)')
    plt.ylabel('x2 (Instâncias High-Performance)')
    plt.title('Interpretação Geométrica - IaaS')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Exibir gráfico
    plt.show()

if __name__ == "__main__":
    main()
