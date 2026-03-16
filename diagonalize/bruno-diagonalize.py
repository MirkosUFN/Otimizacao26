import random
from fractions import Fraction

def imprimir_matriz(matriz):
    for linha in matriz:
        print([str(num) for num in linha])

def diagonalizar(matriz):
    matriz[0] = [Fraction(l1, matriz[0][0]) for l1 in matriz[0]]
    print("\nLinha 0 normalizada:")
    imprimir_matriz(matriz)

    pivo = matriz[1][0]
    matriz[1] = [matriz[1][i] - pivo * matriz[0][i] for i in range(3)]
    print("Linha 1 com coluna 0 zerada:")
    imprimir_matriz(matriz)

    matriz[1] = [l2 / matriz[1][1] for l2 in matriz[1]]
    print("Linha 1 normalizada:")
    imprimir_matriz(matriz)

    pivo = matriz[0][1]
    matriz[0] = [matriz[0][i] - pivo * matriz[1][i] for i in range(3)]
    print("Linha 0 com coluna 1 zerada:")
    imprimir_matriz(matriz)

    return matriz

matriz = [[random.randint(0, 10) for _ in range(3)] for _ in range(2)]

print("\nMatriz original:")
imprimir_matriz(matriz)

matriz_diag = diagonalizar(matriz)

print("\nMatriz diagonalizada:")
imprimir_matriz(matriz_diag)
