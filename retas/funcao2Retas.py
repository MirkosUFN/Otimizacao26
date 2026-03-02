import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    result = []
    for x in range(x0, x1 + 1):
        result.append((a * x) + b)
    return result

def plotar(x0, x1, a, b, a2, b2):
    valorx = list(range(x0, x1 + 1))
    valory = funcao(a, b, x0, x1)

    valorx2 = list(range(x0, x1 + 1))
    valory2 = funcao(a2, b2, x0, x1)
    
    plt.plot(valorx, valory, marker='o', linestyle='-', color='b', label=f'y = {a}x + {b}') 
    plt.plot(valorx2, valory2, marker='o', linestyle='-', color='b', label=f'y = {a2}x + {b2}') 

    plt.title('gráfico')
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()

a = 2
b = -11
a2 = -2
b2 = 4  
x0 = -2
x1 = 5

plotar(x0, x1, a, b, a2, b2)