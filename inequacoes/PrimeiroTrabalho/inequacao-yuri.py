"""
Como executar: python script.py 2 -3 ">=" solucao1
Como commitar: 
git add script.py inequacao-solucao1.png
git commit -m "feat: adiciona algoritmo de inequacao"
git push
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

def gerar_grafico(a, b, operador, nome):
    x = np.linspace(-10, 10, 400)
    y = a * x + b
    plt.figure(figsize=(8, 6))
    estilo = '-' if '=' in operador else '--'
    plt.plot(x, y, color='red', linestyle=estilo)
    
    if '<' in operador:
        plt.fill_between(x, y, -100, color='blue', alpha=0.3)
    elif '>' in operador:
        plt.fill_between(x, y, 100, color='blue', alpha=0.3)
        
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True)
    
    arquivo = f"inequacao-{nome}.png"
    plt.savefig(arquivo)

if __name__ == "__main__":
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    operador = sys.argv[3]
    nome = sys.argv[4]
    gerar_grafico(a, b, operador, nome)
