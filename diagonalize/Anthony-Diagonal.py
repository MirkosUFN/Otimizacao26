import numpy as np

matriz = [
    [1,-2,4],
    [3,1,2]
]

tamanho = len(matriz)

for i in range (tamanho):
    
    diagonal = matriz[i][i]
    if diagonal == 0:
        print("erro diagonal com zero")
    
    elif diagonal != 0:
        for j in range(len(matriz[i])):

            matriz[i][j] = matriz[i][j]/diagonal
        
        for k in range(tamanho):
            if i != k:
                multiplicador = matriz[k][i]
                for j in range(len(matriz[k])):
                    matriz[k][j] = matriz[k][j] - multiplicador * matriz[i][j]

print("matriz:")
for n in matriz:
    print(n)

x = matriz[0][2]
y = matriz[1][2]

print("->")
print("x = ", x)
print("y = ", y)