def funcao(matriz):
    pivo = matriz[0][0]
    for i in range(len(matriz[0])):
        matriz[0][i] = matriz[0][i] / pivo
    print(matriz)

    fator = matriz[1][0]
    for i in range(len(matriz[1])):
        matriz[1][i] = matriz[1][i] - fator * matriz[0][i]
    print(30*'===')
    print(matriz)

    pivo = matriz[1][1]
    for i in range(1, len(matriz[1])):
        matriz[1][i] = matriz[1][i] / pivo
    print(30*'===')
    print(matriz)

    fator = matriz[0][1]
    for i in range(1, len(matriz[0])):
        matriz[0][i] = matriz[0][i] - fator * matriz[1][i]
    print(30*'===')
    print(matriz)

    return [matriz[0][2], matriz[1][2]]


matriz = [
    [3, 2, 6],
    [2, 3, 5]
]

valores = funcao(matriz)
print(valores)

    