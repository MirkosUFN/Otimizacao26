import numpy as np

def carregar_problema(caminho_arquivo):
    """Lê o problema de um arquivo txt e retorna matrizes do numpy."""
    try:
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()
            
        # A primeira linha contém os coeficientes da função objetivo (c)
        c = np.array([float(x) for x in linhas[0].strip().split()])
        
        A = []
        b = []
        # As linhas subsequentes contêm a matriz de restrições (A) e o vetor de limites (b)
        for linha in linhas[1:]:
            if linha.strip(): # Ignora linhas em branco
                valores = [float(x) for x in linha.strip().split()]
                A.append(valores[:-1]) # Todos menos o último
                b.append(valores[-1])  # Apenas o último
                
        return c, np.array(A), np.array(b)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None, None, None

def simplex(c, A, b):
    """Executa o algoritmo Simplex para maximização na forma canônica."""
    num_restricoes, num_variaveis = A.shape
    
    # 1. Montar o Tableau inicial
    # Formato do Tableau:
    # [ A | I | b ]
    # [-c | 0 | 0 ]
    
    tableau = np.zeros((num_restricoes + 1, num_variaveis + num_restricoes + 1))
    
    # Preencher a matriz A e vetor b
    tableau[:num_restricoes, :num_variaveis] = A
    tableau[:num_restricoes, -1] = b
    
    # Preencher a matriz identidade (representando as variáveis de folga)
    tableau[:num_restricoes, num_variaveis:num_variaveis + num_restricoes] = np.eye(num_restricoes)
    
    # Preencher a linha da função objetivo (invetendo o sinal para max)
    tableau[-1, :num_variaveis] = -c
    
    iteracao = 1
    while True:
        # 2. Condição de parada: Se todos os valores na última linha (exceto o resultado) forem >= 0, é ótimo.
        if np.all(np.round(tableau[-1, :-1], 10) >= 0):
            break
            
        # 3. Escolher a Coluna Pivô (variável que entra na base: o mais negativo da última linha)
        coluna_pivo = np.argmin(tableau[-1, :-1])
        
        # 4. Escolher a Linha Pivô (variável que sai da base: teste da razão mínima)
        razoes = []
        for i in range(num_restricoes):
            if tableau[i, coluna_pivo] > 0:
                razao = tableau[i, -1] / tableau[i, coluna_pivo]
                razoes.append(razao)
            else:
                razoes.append(np.inf) # Ignora divisões por zero ou negativos
                
        linha_pivo = np.argmin(razoes)
        
        # Se todas as razões forem infinitas, o problema é ilimitado
        if razoes[linha_pivo] == np.inf:
            raise ValueError("O problema tem solução ilimitada (região viável não é limitada).")
            
        # 5. Operações de pivoteamento de Gauss-Jordan
        elemento_pivo = tableau[linha_pivo, coluna_pivo]
        
        # Divide a linha pivô pelo elemento pivô para que ele se torne 1
        tableau[linha_pivo, :] /= elemento_pivo
        
        # Zera os outros elementos na coluna pivô
        for i in range(num_restricoes + 1):
            if i != linha_pivo:
                fator = tableau[i, coluna_pivo]
                tableau[i, :] -= fator * tableau[linha_pivo, :]
                
        iteracao += 1
        
    # 6. Extrair a solução do Tableau final
    solucao = np.zeros(num_variaveis)
    for j in range(num_variaveis):
        coluna = tableau[:-1, j]
        # Uma variável está na base se sua coluna tem exatamente um '1' e o resto '0'
        if np.count_nonzero(np.round(coluna, 10) == 1) == 1 and np.count_nonzero(np.round(coluna, 10) == 0) == num_restricoes - 1:
            linha_indice = np.where(np.round(coluna, 10) == 1)[0][0]
            solucao[j] = tableau[linha_indice, -1]
            
    valor_otimo = tableau[-1, -1]
    
    return solucao, valor_otimo, iteracao

# --- Execução do Script ---
if __name__ == "__main__":
    arquivo = 'problema.txt' # Nome do seu arquivo txt
    print(f"Lendo dados de '{arquivo}'...\n")
    
    c, A, b = carregar_problema(arquivo)
    
    if c is not None:
        try:
            solucao, valor_otimo, iteracoes = simplex(c, A, b)
            
            print("=== SOLUÇÃO OBTIDA ===")
            print(f"Iterações realizadas: {iteracoes - 1}")
            print(f"Valor ótimo (Z): {valor_otimo:.4f}")
            print("Valores das variáveis de decisão:")
            for i, val in enumerate(solucao):
                print(f"  x_{i+1} = {val:.4f}")
                
        except ValueError as erro:
            print(f"Erro na resolução: {erro}")