import random
from fractions import Fraction

def imprimir_matriz(matriz):
    for linha in matriz:
        print([str(num) for num in linha])

def diagonalizar(matriz):
    # Normaliza primeira linha
    matriz[0] = [Fraction(l1, matriz[0][0]) for l1 in matriz[0]]
    print("\nApos normalizar linha 0:")
    imprimir_matriz(matriz)

    # Zera primeiro elemento da segunda linha
    pivo = matriz[1][0]
    matriz[1] = [matriz[1][i] - pivo * matriz[0][i] for i in range(3)]
    print("Apos zerar coluna 0 na linha 1:")
    imprimir_matriz(matriz)

    # Zera segundo elemento da segunda linha
    matriz[1] = [l2 / matriz[1][1] for l2 in matriz[1]]
    print("Apos normalizar linha 1:")
    imprimir_matriz(matriz)

    # Elimina segundo elemento da primeira linha
    pivo = matriz[0][1]
    matriz[0] = [matriz[0][i] - pivo * matriz[1][i] for i in range(3)]
    print("Apos zerar coluna 1 na linha 0:")
    imprimir_matriz(matriz)

    return matriz

# Gerar matriz 2x3 aleatoria
matriz = [[random.randint(0, 10) for _ in range(3)] for _ in range(2)]

print("\nMatriz original:")
imprimir_matriz(matriz)

matriz_diag = diagonalizar(matriz)

print("\nMatriz diagonalizada:")
imprimir_matriz(matriz_diag)