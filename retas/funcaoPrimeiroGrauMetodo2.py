import matplotlib.pyplot as plt

def funcao(a, b, x_inicio, x_final):
    eixo_x = []
    eixo_y = []

    for x in range(x_inicio, x_final + 1):
        resultado = (a * x) + b
        eixo_x.append(x)
        eixo_y.append(resultado)
    
    # --- Configuração do Gráfico ---
    plt.plot(eixo_x, eixo_y, marker='o', linestyle='-', color='red', label=f'f(x)={a}x+{b}')
    
    # Adicionando detalhes para parecer um plano cartesiano
    plt.axhline(0, color='black', linewidth=1) # Linha do horizonte (Eixo X)
    plt.axvline(0, color='black', linewidth=1) # Linha vertical (Eixo Y)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.title("Gráfico da Função")
    
    plt.show() # Abre a janela com o gráfico
    
    return eixo_y

# Testando
print(funcao(5, -11, -2, 5))
