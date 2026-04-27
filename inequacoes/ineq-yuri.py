import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

LIM = 10
RES = 500
x = np.linspace(0, LIM, RES)
y = np.linspace(0, LIM, RES)
X, Y = np.meshgrid(x, y)

def resolver():
    print("--- Plotter de Inequações (1º Quadrante) ---")
    nome_arq = input("Nome do arquivo: ").strip() or "resultado"
    
    inequacoes = []
    while True:
        entrada = input("Digite (a1 a2 SINAL c) ou 'fim': ").split()
        if not entrada or entrada[0].lower() == 'fim': break
        
        # Converte os dados (suporta frações como 1/2)
        a1 = float(Fraction(entrada[0]))
        a2 = float(Fraction(entrada[1]))
        sinal = entrada[2]
        c = float(Fraction(entrada[3]))
        inequacoes.append((a1, a2, sinal, c))

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(7, 7))
    mascara_total = np.ones(X.shape, dtype=bool)

    for a1, a2, sinal, c in inequacoes:
        # Define a operação matemática baseada no sinal
        ops = {"<": X*a1 + Y*a2 < c, "<=": X*a1 + Y*a2 <= c,
               ">": X*a1 + Y*a2 > c, ">=": X*a1 + Y*a2 >= c}
        mascara = ops[sinal]
        
        # Pinta a área individual desta inequação
        ax.contourf(X, Y, mascara, levels=[0.5, 1], colors=['blue'], alpha=0.1)
        
        # Desenha a linha da fronteira
        if a2 != 0:
            ax.plot(x, (c - a1*x)/a2, label=f"{a1}x + {a2}y {sinal} {c}")
        
        # Acumula a intersecção (Região Viável)
        mascara_total &= mascara

    # Pinta a intersecção de amarelo 
    if mascara_total.any():
        ax.contourf(X, Y, mascara_total, levels=[0.5, 1], colors=['yellow'], alpha=0.5)

    ax.set_xlim(0, LIM); ax.set_ylim(0, LIM)
    ax.grid(True, linestyle=":")
    ax.legend()
    
    nome_limpo = "".join(c for c in nome_arq if c.isalnum())
    plt.savefig(f"{nome_limpo}.png")
    print(f"Sucesso! Salvo como {nome_limpo}.png")
    plt.show()

if __name__ == "__main__":
    resolver()