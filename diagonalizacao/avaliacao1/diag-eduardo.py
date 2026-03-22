def imprimir_matriz(matriz, titulo):
    """Função auxiliar para mostrar a matriz formatada."""
    print(f"{titulo}")
    for linha in matriz:
        linha_formatada = [round(valor, 4) for valor in linha]
        print(linha_formatada)
    print("-" * 30)

def resolver_sistema():
    print("=== Resolvedor de Sistemas (Gauss-Jordan) ===\n")
    n = int(input("Digite o número de variáveis (e equações) do sistema: "))
    
    matriz = []
    
    print("\nInsira os coeficientes de cada equação.")
    for i in range(n):
        print(f"\nEquação {i+1}:")
        linha = []
        for j in range(n):
            coeficiente = float(input(f"  Coeficiente da variável {j+1}: "))
            linha.append(coeficiente)
        resultado = float(input(f"  Resultado da equação {i+1}: "))
        linha.append(resultado)
        matriz.append(linha)
        
    print("\n")
    imprimir_matriz(matriz, "=== MATRIZ INICIAL ===")
    
    for i in range(n):
        # 1. Pivoteamento (Troca de linhas se a diagonal for zero)
        if matriz[i][i] == 0.0:
            for k in range(i+1, n):
                if matriz[k][i] != 0.0:
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    print(f"-> OPERAÇÃO: L{i+1} <-> L{k+1} (Troca de linhas)")
                    imprimir_matriz(matriz, "Ajuste para evitar divisão por zero")
                    break
                    
        pivo = matriz[i][i]
        
        if pivo == 0.0:
            print("\nErro: O sistema não possui uma solução única.")
            return

        # 2. Transformar o pivô em 1 (se já não for 1)
        if pivo != 1.0:
            print(f"-> OPERAÇÃO: L{i+1} = L{i+1} / {round(pivo, 4)}")
            for j in range(n + 1):
                matriz[i][j] = matriz[i][j] / pivo
            imprimir_matriz(matriz, f"Pivô da linha {i+1} transformado em 1")

        # 3. Zerar os elementos acima e abaixo do pivô
        for k in range(n):
            if k != i:
                fator_multiplicador = matriz[k][i]
                
                # Só faz a operação se o número não for zero
                if fator_multiplicador != 0.0:
                    # Lógica para mostrar o sinal de + ou - corretamente no print
                    sinal = "-" if fator_multiplicador > 0 else "+"
                    fator_abs = abs(round(fator_multiplicador, 4))
                    
                    print(f"-> OPERAÇÃO: L{k+1} = L{k+1} {sinal} {fator_abs} * L{i+1}")
                    
                    for j in range(n + 1):
                        matriz[k][j] = matriz[k][j] - (fator_multiplicador * matriz[i][j])
                        
                    imprimir_matriz(matriz, f"Zerando elemento da linha {k+1}")

    # Exibindo a solução final
    print("\n=== SOLUÇÃO FINAL DO SISTEMA ===")
    for i in range(n):
        print(f"Variável {i+1} = {round(matriz[i][n], 4)}")

if __name__ == "__main__":
    resolver_sistema()