from fractions import Fraction


def imprimir_matriz(matriz):
    """
    Imprime a matriz aumentada de forma organizada.
    """
    for linha in matriz:
        print(["{}/{}".format(x.numerator, x.denominator) if isinstance(x, Fraction) else str(x) for x in linha])
    print()


def ler_matriz(n):
    """
    Lê uma matriz aumentada (n x n+1) a partir da entrada do usuário.
    """
    matriz = []
    print(f"Digite cada equação com {n + 1} valores (coeficientes + resultado):")

    for i in range(n):
        while True:
            try:
                entrada = input(f"Equação {i + 1}: ").split()
                if len(entrada) != n + 1:
                    raise ValueError

                linha = [Fraction(int(x)) for x in entrada]
                matriz.append(linha)
                break
            except ValueError:
                print("Entrada inválida! Digite números inteiros separados por espaço.")

    return matriz


def verificar_tipo_solucao(matriz):
    """
    Verifica se o sistema possui:
    - solução única
    - infinitas soluções
    - nenhuma solução
    """
    n = len(matriz)

    for linha in matriz:
        if all(valor == 0 for valor in linha[:-1]) and linha[-1] != 0:
            return "sem_solucao"

    postos = sum(1 for i in range(n) if matriz[i][i] != 0)

    if postos < n:
        return "infinitas"

    return "unica"


def diagonalizar(matriz):
    """
    Aplica o método de Gauss-Jordan para diagonalizar a matriz.
    Mostra cada passo da transformação.
    """
    n = len(matriz)

    for i in range(n):
        # 1. Pivoteamento parcial
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    print(f"Troca de linhas: L{i+1} <-> L{k+1}")
                    imprimir_matriz(matriz)
                    break

        pivo = matriz[i][i]

        if pivo == 0:
            continue  # pode indicar sistema sem solução única

        # 2. Normalizar linha (pivô = 1)
        matriz[i] = [x / pivo for x in matriz[i]]
        print(f"Normalizando L{i+1} (pivô = 1):")
        imprimir_matriz(matriz)

        # 3. Zerar coluna
        for j in range(n):
            if j != i:
                fator = matriz[j][i]

                if fator != 0:
                    matriz[j] = [
                        matriz[j][k] - fator * matriz[i][k]
                        for k in range(n + 1)
                    ]

                    print(f"Zerando coluna {i+1} na linha {j+1}:")
                    imprimir_matriz(matriz)

    return matriz


def mostrar_solucao(matriz):
    """
    Exibe a solução do sistema, se existir.
    """
    tipo = verificar_tipo_solucao(matriz)

    if tipo == "sem_solucao":
        print("O sistema NÃO possui solução.")
    elif tipo == "infinitas":
        print("O sistema possui INFINITAS soluções.")
    else:
        print("Solução única encontrada:")
        for i in range(len(matriz)):
            print(f"x{i+1} = {matriz[i][-1]}")


# ---------------- MAIN ----------------

def main():
    """
    Função principal do programa.
    """
    try:
        n = int(input("Digite o número de variáveis: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Número inválido!")
        return

    matriz = ler_matriz(n)

    print("\nMatriz original:")
    imprimir_matriz(matriz)

    matriz_diag = diagonalizar(matriz)

    print("Matriz diagonalizada:")
    imprimir_matriz(matriz_diag)

    mostrar_solucao(matriz_diag)


if __name__ == "__main__":
    main()