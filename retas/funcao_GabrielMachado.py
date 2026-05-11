import numpy as np
import matplotlib.pyplot as plt

def funcao_primeiro_grau(a, b, x):
    return a * x + b

def gerar_valores_x(inicio, fim, quantidade):
    return np.linspace(inicio, fim, quantidade)

def plotar_reta(a, b, inicio=-10, fim=10, pontos=100):
    x = gerar_valores_x(inicio, fim, pontos)
    y = funcao_primeiro_grau(a, b, x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"f(x) = {a}x + {b}", color='blue')
    
    plt.title(f"Gráfico da Função: f(x) = {a}x + {b}")
    plt.xlabel("Eixo x")
    plt.ylabel("Eixo f(x)")
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()

def main():
    print("--- Gerador de Funções do Primeiro Grau ---")
    
    coef_angular = 2
    coef_linear = 1
    
    plotar_reta(coef_angular, coef_linear)

if __name__ == "__main__":
    main()
