import numpy as np
import matplotlib.pyplot as plt

def main():
    # 1. Identificação do problema
    print("1. Formulação do Problema de Programação Linear")
    print("Objetivo: Maximizar Z = 8*x1 + 5*x2 (Valor Entregue na Sprint)")
    print("Sujeito a:")
    print("  4*x1 + 4*x2 <= 32   (Tempo de Desenvolvimento - horas)")
    print("  2*x1 + 1*x2 <= 12   (Tempo de Testes/QA - horas)")
    print("  x1, x2 >= 0         (Não-negatividade)\n")

    # 2. Resolução geométrica
    x1 = np.linspace(0, 10, 400)

    # 4*x1 + 4*x2 <= 32 => x2 <= (32 - 4*x1) / 4 => x2 <= 8 - x1
    x2_dev = 8 - x1

    # 2*x1 + x2 <= 12 => x2 <= 12 - 2*x1
    x2_qa = 12 - 2 * x1

    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_dev, label='4*x1 + 4*x2 = 32 (Dev)', color='blue')
    plt.plot(x1, x2_qa, label='2*x1 + x2 = 12 (QA)', color='green')

    x2_max = np.minimum(x2_dev, x2_qa)
    plt.fill_between(x1, 0, x2_max, where=(x2_max >= 0) & (x1 >= 0), color='gray', alpha=0.3, label='Região Viável')

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)

    # Vértices da interseção das restrições
    vertices = [(0, 0), (0, 8), (4.0, 4.0), (6, 0)]

    print("3. Avaliação dos vértices e combinação ideal")
    melhor_x1, melhor_x2 = 0, 0
    valor_maximo = -1

    for c_x1, c_x2 in vertices:
        valor = 8 * c_x1 + 5 * c_x2
        print(f"Vértice ({c_x1}, {c_x2}) -> Valor: 8*({c_x1}) + 5*({c_x2}) = {valor}")
        
        if valor > valor_maximo:
            valor_maximo = valor
            melhor_x1, melhor_x2 = c_x1, c_x2

    print(f"\n=> Solução ótima:")
    print(f"Novas Funcionalidades (x1): {melhor_x1}")
    print(f"Refatoração de Código (x2): {melhor_x2}")
    print(f"Valor Máximo Entregue: {valor_maximo}")
    
    # Discussão da terceira parte do enunciado
    print("\n[ Discussão sobre Valores Inteiros ]")
    if float(melhor_x1).is_integer() and float(melhor_x2).is_integer():
        print("A solução encontrada possui valores perfeitamente inteiros (4 funcionalidades e 4 refatorações).")
        print("Isso é fundamental no contexto de Engenharia de Software porque as tarefas (User Stories)")
        print("são itens atômicos em um backlog (não se entrega \"meia\" funcionalidade em uma Sprint).")
        print("A ausência de valores fracionários indica que esta solução pode ser aplicada na prática sem")
        print("a necessidade de recorrer à Programação Linear Inteira (PLI) ou métodos de arredondamento.")
    else:
        print("A solução contém valores fracionários. Seria necessário aplicar Programação Linear Inteira.")

    plt.plot(melhor_x1, melhor_x2, 'ro', markersize=8, label=f'Solução Ótima ({melhor_x1}, {melhor_x2})')
    plt.xlim(-1, 10)
    plt.ylim(-1, 10)
    plt.xlabel('x1 (Novas Funcionalidades)')
    plt.ylabel('x2 (Refatorações / Correções)')
    plt.title('Interpretação Geométrica - Planejamento de Sprints')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
