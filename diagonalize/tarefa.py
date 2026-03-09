from fractions import Fraction #biblioteca pra nao transformar em numeros com virgula

def resolver(matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]

    if a == 0:
        a, b, c, d, e, f = d, e, f, a, b, c

    if a == 0:
        return None

    m = d / a
    e = e - m * b
    f = f - m * c

    if e == 0:
        return None

    y = f / e
    x = (c - b * y) / a

    return [x, y]



if __name__ == '__main__':
    print("Digite os valores:")
    print("Equacao 1: a*x + b*y = c")
    a = Fraction(input("a: "))
    b = Fraction(input("b: "))
    c = Fraction(input("c: "))

    print("Equacao 2: d*x + e*y = f")
    d = Fraction(input("d: "))
    e = Fraction(input("e: "))
    f = Fraction(input("f: "))

    matriz = [
        [a, b, c],
        [d, e, f]
    ]

    resultado = resolver(matriz)

    if resultado is None:
        print("Resultado sem solucao")
    else:
        x, y = resultado
        print(f"Resultado: [x, y] = [{x}, {y}]")
