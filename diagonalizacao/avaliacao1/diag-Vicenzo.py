from fractions import Fraction

def imprimirMatriz(matriz, titulo="Matriz Atual:", operacao=None):
    if operacao:
        print(f"\nOperação: {operacao}\n")
    
    print(titulo)
    for linha in matriz:
        coeficientes = "".join([str(x).rjust(8) for x in linha[:-1]])
        resultado = str(linha[-1]).rjust(8)
        
        print(f"[{coeficientes} | {resultado} ]")
    print("-" * 45)

def gauss():
    print("Resolvedor de Sistemas via Gauss-Jordan")
    
    #1- Receber o tamanho do sistema
    while True:
        try:
            n = int(input("Digite o número de variáveis (que será igual ao de equações): "))
            if n > 0:
                break
            print("O número deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    matriz = []

    # 2- Receber as equacoes
    print("\nPara cada equação, digite os coeficientes e o resultado separados por espaço.")
    
    for i in range(n):
        while True:
            try:
                entrada = input(f"Equação {i + 1}: ")
                valores = [Fraction(x) for x in entrada.split()]
                
                if len(valores) != n + 1:
                    print(f"Erro: Você deve digitar {n} coeficientes e 1 resultado.")
                    continue
                
                matriz.append(valores)
                break
            except ValueError:
                print("Erro: Digite apenas números válidos (ex: 2, -3, 5/2).")

    print()
    imprimirMatriz(matriz, "Matriz Inicial:")

    #3- Processo de diagonalizacao
    for i in range(n):
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    imprimirMatriz(matriz, "Matriz Atual:", f"Troca de Linhas: L{i+1} <-> L{k+1}")
                    break

        pivo = matriz[i][i]
        
        if pivo == 0:
            print("\nO sistema não possui solução única.")
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
                    if fator < 0:
                        operacao_str = f"L{k + 1} = L{k + 1} - ({fator} * L{i + 1})"
                    else:
                        operacao_str = f"L{k + 1} = L{k + 1} - ({fator} * L{i + 1})"
                        
                    imprimirMatriz(matriz, "Matriz Atual:", operacao_str)

    # 4- resultado final
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
