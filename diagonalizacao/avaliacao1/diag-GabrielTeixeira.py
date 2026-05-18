# Arquivo: diag-gabriel.py

def imprimir_matriz(matriz, descricao_passo):
    """Função auxiliar para imprimir a matriz de forma formatada."""
    print(f"\n--- {descricao_passo} ---")
    for linha in matriz:
        # Formata com 2 casas decimais para facilitar a leitura
        linha_formatada = ["{x:7.2f}".format(x=val) for val in linha]
        print("[" + " ".join(linha_formatada) + " ]")

def resolver_sistema_diagonalizacao(matriz):
    """
    Resolve um sistema de equações lineares utilizando a Eliminação de Gauss-Jordan.
    A matriz de entrada deve ser a matriz aumentada do sistema.
    """
    n = len(matriz)
    
    # Validação da regra: número de equações = número de variáveis
    # Uma matriz aumentada de N variáveis deve ter N linhas e N+1 colunas.
    for linha in matriz:
        if len(linha) != n + 1:
            raise ValueError("Erro: O sistema deve possuir o número de equações igual ao número de variáveis.")
            
    imprimir_matriz(matriz, "Estado Inicial da Matriz")
    
    # Percorre cada coluna (e consequentemente, cada linha pivô)
    for i in range(n):
        # 1. Pivoteamento Parcial (Evita divisões por zero caso o pivô atual seja 0)
        max_linha = i
        for k in range(i + 1, n):
            if abs(matriz[k][i]) > abs(matriz[max_linha][i]):
                max_linha = k
                
        if matriz[max_linha][i] == 0:
            raise ValueError("Erro: O sistema não possui solução única (Matriz Singular).")
            
        # Troca a linha atual com a linha do maior pivô, se necessário
        if max_linha != i:
            matriz[i], matriz[max_linha] = matriz[max_linha], matriz[i]
            imprimir_matriz(matriz, f"Troca: Linha {i+1} permutada com Linha {max_linha+1}")
        
        # 2. Tornar o pivô da diagonal igual a 1
        pivo = matriz[i][i]
        for j in range(i, n + 1):
            matriz[i][j] /= pivo
            
        imprimir_matriz(matriz, f"Diagonal: Pivô da Linha {i+1} dividido por {pivo:.2f} (tornado 1)")
        
        # 3. Tornar os valores acima e abaixo da diagonal iguais a zero
        for k in range(n):
            if k != i:  # Pula a linha do próprio pivô
                fator = matriz[k][i]
                if fator != 0:
                    for j in range(i, n + 1):
                        matriz[k][j] -= fator * matriz[i][j]
                    imprimir_matriz(matriz, f"Zerando: Linha {k+1} subtraída de {fator:.2f} * Linha {i+1}")

    print("\n" + "="*40)
    print("SISTEMA RESOLVIDO COM SUCESSO")
    print("="*40)
    
    # Extrai os resultados (a última coluna)
    resultados = [linha[-1] for linha in matriz]
    for idx, res in enumerate(resultados):
        print(f"Variável X{idx+1} = {res:.2f}")
        
    return resultados

# ==========================================
# EXECUTANDO O ALGORITMO COM UM EXEMPLO
# ==========================================
if __name__ == "__main__":
    # Exemplo de um sistema 3x3:
    # 2x +  y -  z =   8
    # -3x - y + 2z = -11
    # -2x + y +  2z = -3
    
    # Representado como matriz aumentada (lista de listas):
    sistema = [
        [ 2,  1, -1,   8],
        [-3, -1,  2, -11],
        [-2,  1,  2,  -3]
    ]
    
    print("Iniciando a resolução do sistema por diagonalização...")
    resolver_sistema_diagonalizacao(sistema)