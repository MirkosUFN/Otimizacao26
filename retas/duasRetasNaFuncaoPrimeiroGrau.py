import matplotlib.pyplot as plt

def calcular_pontos(a, b, x_inicio, x_fim, letraFuncao):

    print(f"\n\n=== FUNÇÃO DO TIPO: f({letraFuncao}) ===\n")

    lista_x = []
    lista_y = []

    for x in range(x_inicio, x_fim + 1):
        
        y = (a * x) + b
        
        lista_x.append(x)   # Lista com os valores do inicio e fim
        lista_y.append(y)   # Lista com os resultados das funções de primeiro grau
        
        print(f"Loop: {letraFuncao}={x} -> f({x}) = {a}*({x}) + {b} = {y}")
        
    return lista_x, lista_y


def plotar_duas_retas(x1, y1, x2, y2, a1, b1, a2, b2):
    plt.figure(figsize=(8, 6))
    
    # Primeira reta
    plt.plot(x1, y1, marker='o', linestyle='-', color='red', label=f'Reta 1: $f(x) = {a1}x + {b1}$')
    
    # Segunda reta
    plt.plot(x2, y2, marker='s', linestyle='--', color='blue', label=f'Reta 2: $g(x) = {a2}x + {b2}$')

    
    plt.axhline(0, color='black', linewidth=1) # Eixo X
    plt.axvline(0, color='black', linewidth=1) # Eixo Y
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.title(f'Comparando duas funções de primeiro grau: $f(x) = {a1}x + {b1}$ & $g(x) = {a2}x + {b2}$ ')
    plt.legend()
    plt.show()


# f(x)
a1, b1 = 2, -1
x1, y1 = calcular_pontos(a1, b1, -5, 5, "x")

# g(x)
a2, b2 = 3, -1
x2, y2 = calcular_pontos(a2, b2, -5, 5, "g")

plotar_duas_retas(x1,y1, x2,y2,a1,b1,a2,b2)