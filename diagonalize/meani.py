# Escrever uma função que diagonalize uma matriz (2x3) de coeficientes. O trabalho pode ser em duplas.
# O sistema deve retornar um vetor [x,y] e mostrar cada etapa do cálculo de linhas na matriz.

def solve_matrix(matrix):
    m = [row[:] for row in matrix]
    print_matrix(m, "matriz inicial")

    # tornar m[0][0] = 1
    pivot1 = m[0][0]
    if pivot1 == 0:
        m[0], m[1] = m[1], m[0]
        pivot1 = m[0][0]
        print("Troca de linhas pois primeiro elemento era 0")

    if pivot1 == 0:
        print("Sistema não possui solução única (coluna 1 zerada)")
        return None

    m[0] = [x / pivot1 for x in m[0]]
    print_matrix(m, "1. pivot da linha 1 (L1 / {:.2f})".format(pivot1))

    # zerar abaixo do pivot 1 (m[1][0] = 0)
    coefficient = m[1][0]
    m[1] = [m[1][i] - (coefficient * m[0][i]) for i in range(3)]
    print_matrix(m, "2. zerar abaixo do pivot (L2 - {:.2f} * L1)".format(coefficient))

    # tornar m[1][1] = 1
    pivot2 = m[1][1]

    m[1] = [x / pivot2 for x in m[1]]
    print_matrix(m, "3. pivot da Linha 2 (L2 / {:.2f})".format(pivot2))

    # zerar acima do pivot 2 (m[0][1] = 0)
    upper_coefficient = m[0][1]
    m[0] = [m[0][i] - (upper_coefficient * m[1][i]) for i in range(3)]
    print_matrix(m, "4. zerar acima do pivot (L1 - {:.2f} * L2)".format(upper_coefficient))

    result = [round(m[0][2], 4), round(m[1][2], 4)]
    # print(f"resultado final: x = {result[0]}, y = {result[1]}")
    print(f"resultado final: {result}")

    return result

def print_matrix(m, step):
    print(f"\n> {step}:")
    for line in m:
        print(f"  [ {line[0]:6.2f} {line[1]:6.2f} | {line[2]:6.2f} ]")

matrix = [
    [2, 1, 5],
    [1, -1, 1]
]

result = solve_matrix(matrix)