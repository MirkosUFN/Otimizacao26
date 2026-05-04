import matplotlib.pyplot as plt
import numpy as np

def resolver_inequacoes():
    print("--- Sistema de Inequações com Vértices ---")
    
    while True:
        try:
            n = int(input("Quantas inequações compõem o sistema? "))
            if n > 0: break
            print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    limite = 20
    x_range = np.linspace(-limite, limite, 1000)
    y_range = np.linspace(-limite, limite, 1000)
    X, Y = np.meshgrid(x_range, y_range)
    
    interseccao = (X >= 0) & (Y >= 0)
    
    # Lista para armazenar as restrições: (a1, a2, v_dir, sinal)
    # Começamos com as restrições do primeiro quadrante: x >= 0 e y >= 0
    restricoes = [
        (1, 0, 0, '>='), # x >= 0
        (0, 1, 0, '>=')  # y >= 0
    ]
    
    plt.figure(figsize=(12, 9))
    
    for i in range(n):
        print(f"\n--- Inequação {i+1} ---")
        try:
            a1 = float(input("Digite o coeficiente a1 (de X): "))
            a2 = float(input("Digite o coeficiente a2 (de Y): "))
            sinal = input("Sinal (<, <=, >, >=): ").strip()
            v_dir = float(input("Digite o valorDireito: "))
            
            restricoes.append((a1, a2, v_dir, sinal))
            
            expressao = a1 * X + a2 * Y
            if sinal == '<': interseccao &= (expressao < v_dir)
            elif sinal == '<=': interseccao &= (expressao <= v_dir)
            elif sinal == '>': interseccao &= (expressao > v_dir)
            elif sinal == '>=': interseccao &= (expressao >= v_dir)
            
            # Desenha a linha
            if a2 != 0:
                y_fronteira = (v_dir - a1 * x_range) / a2
                plt.plot(x_range, y_fronteira, label=f'{a1}x + {a2}y {sinal} {v_dir}')
            else:
                plt.axvline(v_dir/a1, label=f'{a1}x {sinal} {v_dir}')
                
        except (ValueError, ZeroDivisionError):
            print("Erro nos valores. Pulando esta inequação.")

    # --- CÁLCULO DOS VÉRTICES ---
    vertices_x = []
    vertices_y = []

    for i in range(len(restricoes)):
        for j in range(i + 1, len(restricoes)):
            # Resolve o sistema entre a reta i e a reta j:
            # a1*x + a2*y = v1
            # b1*x + b2*y = v2
            a1, a2, v1, _ = restricoes[i]
            b1, b2, v2, _ = restricoes[j]
            
            determinante = a1 * b2 - a2 * b1
            
            if determinante != 0: # As retas não são paralelas
                px = (v1 * b2 - v2 * a2) / determinante
                py = (a1 * v2 - b1 * v1) / determinante
                
                # Verifica se o ponto (px, py) respeita TODAS as inequações
                valido = True
                for c1, c2, vd, s in restricoes:
                    res = c1 * px + c2 * py
                    # Usamos uma pequena tolerância (1e-9) para erros de ponto flutuante
                    if s == '<' and not (res < vd + 1e-9): valido = False
                    elif s == '<=' and not (res <= vd + 1e-9): valido = False
                    elif s == '>' and not (res > vd - 1e-9): valido = False
                    elif s == '>=' and not (res >= vd - 1e-9): valido = False
                
                if valido:
                    vertices_x.append(px)
                    vertices_y.append(py)

    # Plota a área sombreada
    plt.imshow(interseccao, extent=(x_range.min(), x_range.max(), y_range.min(), y_range.max()), 
               origin='lower', cmap='YlGn', alpha=0.3, aspect='auto')

    # Plota os vértices encontrados
    if vertices_x:
        plt.scatter(vertices_x, vertices_y, color='red', zorder=5, label='Vértices')
        for vx, vy in zip(vertices_x, vertices_y):
            plt.annotate(f'({vx:.1f}, {vy:.1f})', (vx, vy), textcoords="offset points", 
                         xytext=(0,10), ha='center', fontsize=9, color='darkred', fontweight='bold')

    # Configurações de exibição
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.xlim(-2, limite) # Ajustado para focar mais no 1º quadrante
    plt.ylim(-2, limite)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title("Área de Viabilidade e Vértices")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    resolver_inequacoes()
