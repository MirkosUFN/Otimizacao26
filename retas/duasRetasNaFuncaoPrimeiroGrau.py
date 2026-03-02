import matplotlib.pyplot as plt

def calcular_pontos(a, b, x_inicio, x_fim, letraFuncao):
    print(f"\n\n--- Gerando pontos para a função {letraFuncao}(x) = {a}x + {b} ---\n")
    
    lista_x = []
    lista_y = []

    for x in range(x_inicio, x_fim + 1):
        y = (a * x) + b
        
        lista_x.append(x)
        lista_y.append(y)
        
        print(f"Loop: {letraFuncao}({x}) -> {a}*{x} + {b} = {y}")
        
    return lista_x, lista_y

def plotar_com_analise(x1, y1, x2, y2, a1, b1, a2, b2):
    plt.figure(figsize=(9, 6))
    
    plt.plot(x1, y1, marker='o', linestyle='-', color='red', label=f'Reta f(x) = {a1}x + {b1}')
    plt.plot(x2, y2, marker='s', linestyle='--', color='blue', label=f'Reta g(x) = {a2}x + {b2}')

    mensagem = ""
    
    # Checando se são paralelas ou coincidentes
    if a1 == a2:
        if b1 == b2:
            mensagem = "Status: Retas Coincidentes (São a mesma reta)"
        else:
            mensagem = "Status: Retas Paralelas (Nunca se cruzam)"
    else:

        # Cálculo matemático do ponto de intersecção:
        x_inter = (b2 - b1) / (a1 - a2)
        y_inter = a1 * x_inter + b1
        
        mensagem = f"Status: Intersecção em ({x_inter:.1f}, {y_inter:.1f})"
        

        # Marcando no gráfico
        plt.plot(x_inter, y_inter, marker='X', color='green', markersize=12, label='Intersecção')
        plt.annotate(f'Intersecção: ({x_inter:.1f}, {y_inter:.1f})', xy=(x_inter, y_inter), xytext=(x_inter + 1, y_inter + 1),arrowprops=dict(facecolor='black', shrink=0.05))

    plt.axhline(0, color='black', linewidth=1) 
    plt.axvline(0, color='black', linewidth=1) 
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.title(f'Análise de Retas:\n{mensagem}')
    plt.legend()
    plt.show()

# f(x)
a1, b1 = 2, -1
# f(g)
a2, b2 = -1, 3 

x1, y1 = calcular_pontos(a1, b1, -5, 5, "f")
x2, y2 = calcular_pontos(a2, b2, -5, 5, "g")

plotar_com_analise(x1, y1, x2, y2, a1, b1, a2, b2)