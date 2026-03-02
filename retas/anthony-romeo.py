import matplotlib.pyplot as plt

def funcao(a, b, x0, x1):
    x_values = list(range(x0, x1)) 
    result = []
    for x in x_values:
        result.append((a * x) + b)
    return x_values, result 

# definicao de parametros
a = 2
b = -11
x0 = -2
x1 = 5

# chamando a funcao
eixo_x, eixo_y = funcao(a, b, x0, x1)

# cria o grafico
plt.figure(figsize=(10, 5)) 
plt.plot(eixo_x, eixo_y, marker='o', linestyle='-', color='b') 

# detalhes do grafico
plt.title(f'Gráfico da função f(x) = {a}x + {b}')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True) 

# exibe o grafico
plt.show()
