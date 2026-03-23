def imprimir_matriz(matriz, descricao_passo):
    """Imprime a matriz formatada com uma descrição do passo atual."""
    print(f"\n--- {descricao_passo} ---")
    for linha in matriz:
        # Formata os números para 3 casas decimais para facilitar a leitura
        linha_formatada = ["{:.3f}".format(valor) for valor in linha]
        print("[" + ", ".join(linha_formatada) + "]")

def gauss_jordan(matriz):
    n = len(matriz)
    
    # Validação da regra: número de equações = número de variáveis
    # Uma matriz com n variáveis terá n linhas e n+1 colunas (a última é o resultado)
    for linha in matriz:
        if len(linha) != n + 1:
            raise ValueError("Erro: O sistema deve ter o mesmo número de equações e variáveis.")

    imprimir_matriz(matriz, "Matriz Inicial (Sistema Original)")

    # Percorre cada coluna/linha da diagonal principal
    for i in range(n):
        # 1. Pivoteamento parcial: Evita divisão por zero se o elemento da diagonal for 0
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    # Troca a linha atual por uma linha abaixo que tenha valor diferente de zero na coluna
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    imprimir_matriz(matriz, f"Troca da Linha {i+1} com a Linha {k+1} para evitar pivô zero")
                    break
                    
        pivo = matriz[i][i]
        if pivo == 0:
            print("\nO sistema não possui solução única (pivô nulo encontrado).")
            return None

        # 2. Tornar o elemento da diagonal principal (pivô) igual a 1
        if pivo != 1:
            for j in range(n + 1):
                matriz[i][j] /= pivo
            imprimir_matriz(matriz, f"Linha {i+1} dividida pelo pivô ({pivo:.3f}) para criar o '1' na diagonal")

        # 3. Zerar os elementos acima e abaixo do pivô na coluna atual
        for k in range(n):
            if k != i:  # Pula a linha do próprio pivô
                fator_multiplicacao = matriz[k][i]
                if fator_multiplicacao != 0:
                    for j in range(n + 1):
                        # Linha K = Linha K - (fator * Linha do Pivô)
                        matriz[k][j] -= fator_multiplicacao * matriz[i][j]
                    imprimir_matriz(matriz, f"Linha {k+1} subtraída por ({fator_multiplicacao:.3f} * Linha {i+1}) para zerar a coluna {i+1}")

    # A solução estará na última coluna da matriz resultante
    solucao = [linha[n] for linha in matriz]
    return solucao

# --- Testando o Código ---
# Exemplo de sistema de 3 equações e 3 variáveis (x, y, z):
#  2x +  y -  z =   8
# -3x -  y + 2z = -11
# -2x +  y + 2z =  -3

matriz_sistema = [
    [ 2,  1, -1,   8],
    [-3, -1,  2, -11],
    [-2,  1,  2,  -3]
]

try:
    resultados = gauss_jordan(matriz_sistema)
    if resultados:
        print("\n=== Solução Final Encontrada ===")
        variaveis = ['x', 'y', 'z', 'w', 'v'] # Suporta mais, se necessário
        for i, res in enumerate(resultados):
            var_nome = variaveis[i] if i < len(variaveis) else f"Variável {i+1}"
            print(f"{var_nome} = {res:.3f}")
except ValueError as e:
    print(e)
