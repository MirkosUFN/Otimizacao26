def imprimir_matriz(matriz, titulo):
    """Função auxiliar para mostrar a matriz formatada."""
    
    print("\n" + f"{titulo}")
    for linha in matriz:
        linha_formatada = [round(valor, 4) for valor in linha]
        print(linha_formatada)

def resolver_matriz(matriz):
    print("=== Resolvedor de Gauss-Jordan ===\n")

    n = len(matriz)

    imprimir_matriz(matriz, "=== MATRIZ INICIAL ===")

    #Eliminação para baixo (forma escalonada) ===
    for i in range(n):
        # 1. Pivoteamento (troca de linhas se a diagonal for zero)
        if matriz[i][i] == 0.0:
            for k in range(i+1, n):
                if matriz[k][i] != 0.0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    print(f"-> L{i+1} <-> L{k+1} (Troca de linhas)")
                    imprimir_matriz(matriz, "Ajuste para evitar divisão por zero")
                    break

        pivo = matriz[i][i]

        if pivo == 0.0:
            print("\nErro: O sistema não possui uma solução única.")
            return

        # 2. Transformar o pivô em 1
        if pivo != 1.0:
            print(f"-> L{i+1} = L{i+1} / {round(pivo, 4)}")
            for j in range(n + 1):
                matriz[i][j] = matriz[i][j] / pivo
            imprimir_matriz(matriz, f"Pivô da linha {i+1} transformado em 1")

        # 3. Zerar apenas ABAIXO do pivô
        for k in range(i+1, n):
            multiplicador = matriz[k][i]
            if multiplicador != 0.0:
                sinal = "-" if multiplicador > 0 else "+"
                fator_abs = abs(round(multiplicador, 4))
                print(f"-> L{k+1} = L{k+1} {sinal} {fator_abs} * L{i+1}")
                for j in range(n + 1):
                    matriz[k][j] = matriz[k][j] - (multiplicador * matriz[i][j])
                imprimir_matriz(matriz, f"Zerando elemento da linha {k+1}")

    # === zerar ACIMA da diagonal
    for i in range(n-1, -1, -1):
        for k in range(i-1, -1, -1):
            multiplicador = matriz[k][i]
            if multiplicador != 0.0:
                sinal = "-" if multiplicador > 0 else "+"
                fator_abs = abs(round(multiplicador, 4))
                print(f"-> L{k+1} = L{k+1} {sinal} {fator_abs} * L{i+1}")
                for j in range(n + 1):
                    matriz[k][j] = matriz[k][j] - (multiplicador * matriz[i][j])
                imprimir_matriz(matriz, f"Zerando elemento da linha {k+1}")

    # Exibindo a solução final
    print("\n=== SOLUÇÃO FINAL ===")
    for i in range(n):
        print(f"Variável {i+1} = {round(matriz[i][n], 4)}")

if __name__ == "__main__":
    
    minha_matriz = [
        [ 2.0, 1.0, -3.0, 5.0, -32.0],
        [ 5.0, -6.0, 0.0, -3.0, -4.0],
        [1.0, -4.0, 5.0, 2.0,  1.0],
        [3.0, 1.0, -2.0, 1.0,  -15]
    ]

    resolver_matriz(minha_matriz)
