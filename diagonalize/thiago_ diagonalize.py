# Escrever uma função que diagonalize uma matriz (2x3) de coeficientes. O trabalho pode ser em duplas.
# O sistema deve retornar um vetor [x,y] e mostrar cada etapa do cálculo de linhas na matriz.

def mostrar_etapa(n, matriz):
    print(f"--- Etapa {n} ---")
    for linha in matriz:
        print(linha)

def diagonalizar(matriz):
    # Etapa 1: normaliza L0 pelo pivo
    pivo = matriz[0][0]
    matriz[0] = [v / pivo for v in matriz[0]]
    mostrar_etapa(1, matriz)

    # Etapa 2: zera coluna 0 de L1
    fator = matriz[1][0]
    matriz[1] = [matriz[1][j] - fator * matriz[0][j] for j in range(len(matriz[1]))]
    mostrar_etapa(2, matriz)

    # Etapa 3: normaliza L1 pelo pivo
    pivo = matriz[1][1]
    matriz[1][1:] = [v / pivo for v in matriz[1][1:]]
    mostrar_etapa(3, matriz)

    # Etapa 4: zera coluna 1 de L0
    fator = matriz[0][1]
    matriz[0][1:] = [matriz[0][j] - fator * matriz[1][j] for j in range(1, len(matriz[0]))]
    mostrar_etapa(4, matriz)

    return [matriz[0][2], matriz[1][2]]


def __main__():
    matriz = [
        [2, 1, 7],
        [1, 2, 11]
    ]

    valores = diagonalizar(matriz)
    print(valores)


if __name__ == "__main__":    __main__()