import random
from fractions import Fraction

def imprimir_matriz(matriz):
    """
    Imprime a matriz de forma organizada.
    """
    for linha in matriz:
        print([str(num) for num in linha])
    print()


def diagonalizar(matriz):
    """
    Aplica o método de Gauss-Jordan para diagonalizar a matriz.
    """
    n = len(matriz)

    for i in range(n):
        # 0. Pivoteamento (evitar divisão por zero)
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    print(f"Troca de linhas: L{i} <-> L{k}")
                    imprimir_matriz(matriz)
                    break

        pivo = matriz[i][i]

        # Se ainda for zero, não dá pra continuar
        if pivo == 0:
            print("Erro: sistema sem solução única.")
            return matriz

        # 1. Normalizar a linha do pivô (tornar o pivô = 1)
        matriz[i] = [Fraction(x, pivo) for x in matriz[i]]

        print(f"Apos normalizar linha {i}:")
        imprimir_matriz(matriz)

        # 2. Zerar os outros elementos da coluna
        for j in range(n):
            if j != i:
                fator = matriz[j][i]

                matriz[j] = [
                    matriz[j][k] - fator * matriz[i][k]
                    for k in range(n + 1)
                ]

                print(f"Apos zerar coluna {i} na linha {j}:")
                imprimir_matriz(matriz)

    return matriz


# -------- CONFIGURAÇÃO --------
n = 3  # numero de variaveis

# Gerar matriz aumentada (n x n+1)
matriz = [
    [random.randint(1, 10) for _ in range(n + 1)]
    for _ in range(n)
]

print("Matriz original:")
imprimir_matriz(matriz)

matriz_diag = diagonalizar(matriz)

print("Matriz diagonalizada:")
imprimir_matriz(matriz_diag)