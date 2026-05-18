from fractions import Fraction


def exibir_matriz(m):
    """
    Mostra a matriz formatada.
    """

    for linha in m:

        linha_formatada = []

        for valor in linha:

            if valor.denominator == 1:
                linha_formatada.append(str(valor.numerator))
            else:
                linha_formatada.append(
                    f"{valor.numerator}/{valor.denominator}"
                )

        print(linha_formatada)

    print()


def entrada_matriz():
    """
    Recebe uma matriz 2x3.
    """

    matriz = []

    print("Digite os valores da matriz:")
    print("Exemplo: 2 1 5")

    for i in range(2):

        while True:

            try:

                valores = input(f"Linha {i+1}: ").split()

                if len(valores) != 3:
                    raise ValueError

                linha = []

                for numero in valores:
                    linha.append(Fraction(int(numero)))

                matriz.append(linha)

                break

            except ValueError:
                print("Digite exatamente 3 números inteiros.")

    return matriz


def gauss_jordan(m):
    """
    Faz a diagonalização da matriz.
    """

    total_linhas = 2
    total_colunas = 3

    for coluna_pivo in range(total_linhas):

        # Verifica pivô zero
        if m[coluna_pivo][coluna_pivo] == 0:

            for prox in range(coluna_pivo + 1, total_linhas):

                if m[prox][coluna_pivo] != 0:

                    m[coluna_pivo], m[prox] = m[prox], m[coluna_pivo]

                    print(
                        f"Trocando L{coluna_pivo+1} por L{prox+1}"
                    )

                    exibir_matriz(m)

                    break

        pivo = m[coluna_pivo][coluna_pivo]

        if pivo != 0:

            # Divide toda linha pelo pivô
            nova_linha = []

            for valor in m[coluna_pivo]:
                nova_linha.append(valor / pivo)

            m[coluna_pivo] = nova_linha

            print(f"Dividindo L{coluna_pivo+1} por {pivo}")

            exibir_matriz(m)

        # Eliminação
        for linha in range(total_linhas):

            if linha != coluna_pivo:

                multiplicador = m[linha][coluna_pivo]

                if multiplicador != 0:

                    nova_linha = []

                    for c in range(total_colunas):

                        resultado = (
                            m[linha][c]
                            - multiplicador * m[coluna_pivo][c]
                        )

                        nova_linha.append(resultado)

                    m[linha] = nova_linha

                    print(
                        f"L{linha+1} = L{linha+1} - "
                        f"({multiplicador}) x L{coluna_pivo+1}"
                    )

                    exibir_matriz(m)

    return m


def mostrar_resultado(m):
    """
    Mostra o vetor solução.
    """

    x = m[0][2]
    y = m[1][2]

    print("Resultado final:")

    exibir_matriz(m)

    print(f"Vetor solução = [{x}, {y}]")


# ------------------ MAIN ------------------ #

def main():

    matriz = entrada_matriz()

    print("\nMatriz inicial:")

    exibir_matriz(matriz)

    matriz_final = gauss_jordan(matriz)

    mostrar_resultado(matriz_final)


if __name__ == "__main__":
    main()
