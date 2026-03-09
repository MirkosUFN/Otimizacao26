from fractions import Fraction

def resolver_sistema(matriz):
    # converter tudo para Fraction
    m = [[Fraction(x) for x in linha] for linha in matriz]

    # pivô linha 1
    pivo = m[0][0]
    for j in range(3):
        m[0][j] /= pivo

    # zerar abaixo
    fator = m[1][0]
    for j in range(3):
        m[1][j] -= fator * m[0][j]

    # pivô linha 2
    pivo = m[1][1]
    for j in range(1,3):
        m[1][j] /= pivo

    # zerar acima
    fator = m[0][1]
    for j in range(1,3):
        m[0][j] -= fator * m[1][j]

    x = m[0][2]
    y = m[1][2]

    # converter para inteiro se possível
    x = x.numerator if x.denominator == 1 else x
    y = y.numerator if y.denominator == 1 else y

    return [x, y]

matriz = [
    [2,1,5], # [2,1,1]
    [1,1,3]  # [1,3,1]
]

print(resolver_sistema(matriz))