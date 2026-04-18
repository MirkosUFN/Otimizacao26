import numpy as np
import matplotlib.pyplot as plt

def desenhar_inequacao(a, b, operador):
    """
    Desenha o gráfico e a área de solução para uma inequação linear.
    """
    # 1. Gerar os pontos do eixo X (de -10 a 10, 400 pontos para ficar suave)
    x = np.linspace(-10, 10, 400)
    
    # 2. Calcular os pontos Y correspondentes da reta base (y = ax + b)
    y = a * x + b

    plt.figure(figsize=(8, 6))

    # 3. Determinar o estilo da linha (tracejada ou contínua)
    estilo_linha = '--' if operador in ['>', '<'] else '-'

    # Desenha a reta base
    plt.plot(x, y, color='blue', linestyle=estilo_linha, linewidth=2, label=f'Reta base: y = {a}x + {b}')

    # 4. Determinar a área de preenchimento (sombreamento)
    if operador in ['>', '>=']:
        # Preencher tudo que está acima da reta (usamos 20 como limite visual superior)
        plt.fill_between(x, y, 20, color='lightblue', alpha=0.5, label=f'Solução: y {operador} {a}x + {b}')
    elif operador in ['<', '<=']:
        # Preencher tudo que está abaixo da reta (usamos -20 como limite visual inferior)
        plt.fill_between(x, y, -20, color='lightcoral', alpha=0.5, label=f'Solução: y {operador} {a}x + {b}')
    else:
        print("Operador inválido. Use '>', '>=', '<' ou '<='.")
        return

    # 5. Configurações visuais do gráfico
    plt.axhline(0, color='black', linewidth=1) # Eixo X horizontal
    plt.axvline(0, color='black', linewidth=1) # Eixo Y vertical
    plt.xlim(-10, 10)
    plt.ylim(-15, 15) # Limites visuais do gráfico
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title(f'Gráfico da Inequação: y {operador} {a}x + {b}')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    
    # Mostrar o gráfico
    plt.show()

# --- Execução do Programa ---
print("=== Solucionador Visual de Inequações ===")
try:
    valor_a = float(input("Digite o valor de 'a': "))
    valor_b = float(input("Digite o valor de 'b': "))
    simbolo = input("Digite a inequação (>, >=, <, <=): ").strip()
    
    desenhar_inequacao(valor_a, valor_b, simbolo)
except ValueError:
    print("Erro: Por favor, digite apenas números para 'a' e 'b'.")