# ============================================================
# Método de Gauss-Jordan para resolução de sistemas lineares
# Diagonaliza a matriz aumentada, tornando a diagonal = 1
# e todos os outros elementos = 0
# ============================================================


# Exibe a matriz formatada com separador entre coeficientes e termo independente
def imprimir_matriz(matriz, titulo=""):
    if titulo:
        print(f"\n  {titulo}")
    print("  " + "-" * (10 * (len(matriz[0]))))
    for i, linha in enumerate(matriz):
        valores = "  | "
        for j, v in enumerate(linha):
            if j == len(linha) - 1:
                valores += " | "  
            valores += f"{v:8.2f} "
        valores += "|"
        print(valores)
    print("  " + "-" * (10 * (len(matriz[0]))))


def calcular(matriz):
    n = len(matriz)  # Número de equações
    passo = 1

    print("\n" + "=" * 60)
    print("  MÉTODO DE GAUSS-JORDAN — DIAGONALIZAÇÃO")
    print("=" * 60)
    print("\n  Matriz inicial (coeficientes | termos independentes):")
    imprimir_matriz(matriz)

    # Percorre por cada coluna 
    for i in range(n):
        print(f"\n{'=' * 60}")
        print(f"  PASSO {passo}: Trabalhando na coluna {i + 1} (variável x{i + 1})")
        print(f"{'=' * 60}")
        passo += 1

        pivo = matriz[i][i]

        #  Troca de linhas se o pivô for zero 
        # não pode ser dividido por zero, entao procura por uma linha abaixo para trocar
        if pivo == 0:
            print(f'matriz[{i}][{i}] = {pivo}')
            trocou = False
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    print(f"\n  [!] Pivô zero detectado na linha {i + 1}.")
                    print(f"      Trocando linha {i + 1} com linha {k + 1}.")
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    imprimir_matriz(matriz, f"Após troca: L{i+1} <-> L{k+1}")
                    trocou = True
                    break
            if not trocou:
                # Nenhuma linha válida encontrada: sistema sem solução única
                print(f"\n  [ERRO] Sistema sem solução única (coluna {i+1} é nula).")
                return None

        # Etapa a: tornar pivô = 1
        # Divide toda a linha pelo valor do pivô: L_i = L_i / pivô
        print(f'\n pivo matriz[{i}][{i}] = {pivo}')
        if pivo != 1:
            print(f"\n  Etapa {passo - 1}a: tornar pivo = 1")
            print(f"  Operação: L{i+1} = L{i+1} / {pivo:.2f}")
            for j in range(n + 1):
                matriz[i][j] /= pivo
            imprimir_matriz(matriz, f"Após L{i+1} = L{i+1} / {pivo:.2f}")
        else:
            print(f"\n  Etapa {passo - 1}a: Pivô já é 1.")

        #  Etapa b: Zerar todos os outros elementos da coluna i 
        # Para cada linha k ≠ i, aplica: L_k = L_k - fator * L_i
        # onde fator é o valor atual de matriz[k][i]
        print(f"\n  Etapa {passo - 1}b: Zerar os demais elementos da coluna {i + 1}")
        alguma_operacao = False
        for k in range(n):
            if k != i and matriz[k][i] != 0:
                fator = matriz[k][i]  # Valor que queremos eliminar na linha k
                sinal = "-" if fator > 0 else "+"
                print(f"  Operação: L{k+1} = L{k+1} {sinal} {abs(fator):.2f} * L{i+1}")
                for j in range(n + 1):
                    matriz[k][j] -= fator * matriz[i][j]
                alguma_operacao = True

        if alguma_operacao:
            imprimir_matriz(matriz, f"Após zerar coluna {i + 1}")
        else:
            print("  Coluna já zerada, nenhuma operação necessária.")

    ## FINAL
    print(f"\n{'=' * 60}")
    print("  MATRIZ DIAGONALIZADA (Identidade | Solução)")
    print(f"{'=' * 60}")
    imprimir_matriz(matriz)

    # O resultado na última coluna da matriz 
    resultado = [matriz[i][n] for i in range(n)]

    print(f"\n{'=' * 60}")
    print("  Resultado final")
    print(f"{'=' * 60}")
    for i, val in enumerate(resultado):
        print(f"  x{i + 1} = {val:.2f}")
    print()

    return resultado


# Lê o sistema linear do terminal: número de variáveis e coeficientes de cada equação
def iniciar():
    print("=" * 60)
    print("  RESOLUÇÃO DE SISTEMA LINEAR — GAUSS-JORDAN")
    print("=" * 60)
    while True:
        try:
            n = int(input("\n  Quantas variáveis (e equações) o sistema possui? "))
            if n < 1:
                print("  Digite um número maior que 0.")
                continue
            break
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")

    print(f"\n  Digite os coeficientes de cada equação seguidos do termo independente.")
    print(f"  Exemplo para 3 variáveis: 2 1 -1 3  (representa 2x + 1y - 1z = 3)\n")

    matriz = []
    for i in range(n):
        while True:
            try:
                entrada = input(f"  Equação {i + 1} ({n + 1} valores): ").split()
                if len(entrada) != n + 1:
                    print(f"  Esperado {n + 1} valores, recebeu {len(entrada)}. Tente novamente.")
                    continue
                linha = [float(v) for v in entrada]  # Converte strings para float
                matriz.append(linha)
                break
            except ValueError:
                print("  Entrada inválida. Use apenas números.")

    return matriz

matriz = iniciar()

print("Matriz nao formatada:")
for linha in matriz:
    print(linha)
calcular(matriz)
