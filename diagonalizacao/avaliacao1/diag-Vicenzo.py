from fractions import Fraction


def imprimirMatriz(matriz, titulo="Matriz Atual:", operacao=None):
    if operacao:
        print(f"\nOperacao: {operacao}\n")

    print(titulo)
    for linha in matriz:
        coeficientes = "".join([str(x).rjust(8) for x in linha[:-1]])
        resultado = str(linha[-1]).rjust(8)
        print(f"[{coeficientes} | {resultado} ]")
    print("-" * 45)


def gauss():
    print("Resolvedor de Sistemas via Gauss-Jordan")

    # 1- Receber um tamanho inicial para o sistema.
    while True:
        try:
            n = int(input("Digite o numero de equacoes do sistema: "))
            if n > 0:
                break
            print("O numero deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um numero inteiro valido.")

    matriz = []

    # 2- Receber as equacoes
    print("\nPara cada equacao, digite os coeficientes e o resultado separados por espaco.")
    print("Exemplo com 2 variaveis: 1 1 2  (representa 1x + 1y = 2)")

    i = 0
    while i < n:
        while True:
            try:
                entrada = input(f"Equacao {i + 1}: ")
                valores = [Fraction(x) for x in entrada.split()]

                if len(valores) < 2:
                    print("Erro: Digite pelo menos 1 coeficiente e 1 resultado.")
                    continue

                if i == 0:
                    variaveis_inferidas = len(valores) - 1
                    if variaveis_inferidas != n:
                        print(
                            f"A primeira equacao indica um sistema com {variaveis_inferidas} variaveis. "
                            f"Ajustando o sistema para {variaveis_inferidas} equacoes."
                        )
                        n = variaveis_inferidas

                if len(valores) != n + 1:
                    print(f"Erro: Voce deve digitar {n} coeficientes e 1 resultado.")
                    continue

                matriz.append(valores)
                break
            except ValueError:
                print("Erro: Digite apenas numeros validos (ex: 2, -3, 5/2).")
        i += 1

    print()
    imprimirMatriz(matriz, "Matriz Inicial:")

    # 3- Processo de diagonalizacao
    for i in range(n):
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    imprimirMatriz(matriz, "Matriz Atual:", f"Troca de Linhas: L{i + 1} <-> L{k + 1}")
                    break

        pivo = matriz[i][i]

        if pivo == 0:
            print("\nO sistema nao possui solucao unica.")
            return

        if pivo != 1:
            for j in range(n + 1):
                matriz[i][j] /= pivo
            imprimirMatriz(matriz, "Matriz Atual:", f"L{i + 1} = L{i + 1} / {pivo}")

        for k in range(n):
            if k != i:
                fator = matriz[k][i]
                if fator != 0:
                    for j in range(n + 1):
                        matriz[k][j] -= fator * matriz[i][j]
                    operacao_str = f"L{k + 1} = L{k + 1} - ({fator} * L{i + 1})"
                    imprimirMatriz(matriz, "Matriz Atual:", operacao_str)

    # 4- Resultado final
    print("\nResultado Final")
    print("\nMatriz Atual:")
    for linha in matriz:
        coeficientes = "".join([str(x).rjust(8) for x in linha[:-1]])
        resultado = str(linha[-1]).rjust(8)
        print(f"[{coeficientes} | {resultado} ]")
    print("-" * 45)

    print("\nValores:")
    for i in range(n):
        print(f"X{i + 1} -> {matriz[i][n]}")


if __name__ == "__main__":
    gauss()
