import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    x_values = list(range(x0, x1)) 
    result = []
    for x in x_values:
        result.append((a * x) + b)
    return x_values, result 

# definicao de parametros
a = 2
b = -9
x0 = -2
x1 = 5

c = 3
d = -7
z0 = -2
z1 = 5

# chamando a funcao
eixo_x, eixo_y = funcao(a, b, x0, x1)
eixo_x2, eixo_y2 = funcao(c, d, z0, z1)

# cria o grafico
plt.figure(figsize=(10, 5)) 
plt.plot(eixo_x, eixo_y, marker='o', linestyle='-', color='b') 
plt.plot(eixo_x2,eixo_y2,  marker='o', linestyle='-', color='b')

# detalhes do grafico
if a!=c:
    plt.title(f'Gráfico da função f(x) = {a}x + {b} e intersecção com f(x) = {c}x + {d}')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True) 

    # exibe o grafico
    plt.show()

elif a==c and b!=d:
    plt.title(f'Gráfico da função f(x) = {a}x + {b} paralela com f(x) = {c}x + {d}')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True) 

    plt.show()

else:
    plt.title(f'Gráfico da função f(x) = {a}x + {b} em mesma reta com f(x) = {c}x + {d}')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.grid(True) 

    
# exibe o grafico
plt.show()
    

##retas se cruzam em 1 ponto, ou não se cruzam e ficam paralelas, ou fica uma sobre a outra