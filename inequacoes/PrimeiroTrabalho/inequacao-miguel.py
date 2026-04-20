import matplotlib.pyplot as plt
import numpy as np

def resolver_inequacao(a, b, sinal):
    # 1. Criamos um intervalo de X para desenhar a reta
    x = np.linspace(-10, 10, 100)
    
    # 2. Calculamos a reta base (a fronteira)
    y_reta = a * x + b
    
    plt.figure(figsize=(8, 6))
    
    # 3. Lógica para pintar a área de solução
    if sinal == '>':
        # Pinta de y_reta até um valor muito alto (ex: 100)
        plt.fill_between(x, y_reta, 100, color='lightblue', alpha=0.5, label='Solução: y > ax + b')
    elif sinal == '>=':
        plt.fill_between(x, y_reta, 100, color='lightblue', alpha=0.5, label='Solução: y >= ax + b')
    elif sinal == '<':
        # Pinta de um valor muito baixo (ex: -100) até y_reta
        plt.fill_between(x, -100, y_reta, color='lightcoral', alpha=0.5, label='Solução: y < ax + b')
    elif sinal == '<=':
        plt.fill_between(x, -100, y_reta, color='lightcoral', alpha=0.5, label='Solução: y <= ax + b')

    # 4. Desenha a linha da reta para marcar a fronteira
    # Se for "estritamente maior/menor", a linha costuma ser tracejada na matemática
    estilo_linha = '--' if sinal in ['>', '<'] else '-'
    plt.plot(x, y_reta, color='black', linestyle=estilo_linha, linewidth=2, label='Fronteira')

    # Configurações do gráfico
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True, linestyle=':')
    plt.title(f"Área de Solução para: y {sinal} {a}x + {b}")
    plt.legend()
    plt.show()

# Teste do algoritmo
val_a = float(input("Digite o valor de a: "))
val_b = float(input("Digite o valor de b: "))
op_sinal = input("Digite o sinal (>, >=, <, <=): ")

resolver_inequacao(val_a, val_b, op_sinal)