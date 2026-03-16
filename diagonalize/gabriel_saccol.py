# Exemplo 1: Sistema com solução única
print("\n--- Exemplo 1: Sistema com solução única ---")
# 2x + y = 5
# 3x - 2y = 4
matriz_exemplo1 = np.array([
    [2, 1, 5],
    [3, -2, 4]
])
solucao1 = resolver_sistema_gauss(matriz_exemplo1)

if solucao1 is not None:
    print(f"Vetor solução [x, y]: {solucao1}\n")

# Exemplo 2: Sistema sem solução (inconsistente)
print("\n--- Exemplo 2: Sistema inconsistente ---")
# x + y = 1
# x + y = 2
matriz_exemplo2 = np.array([
    [1, 1, 1],
    [1, 1, 2]
])
solucao2 = resolver_sistema_gauss(matriz_exemplo2)

if solucao2 is not None:
    print(f"Vetor solução [x, y]: {solucao2}\n")

# Exemplo 3: Sistema com infinitas soluções (dependente)
print("\n--- Exemplo 3: Sistema dependente ---")
# x + y = 1
# 2x + 2y = 2
matriz_exemplo3 = np.array([
    [1, 1, 1],
    [2, 2, 2]
])
solucao3 = resolver_sistema_gauss(matriz_exemplo3)

if solucao3 is not None:
    print(f"Vetor solução [x, y]: {solucao3}\n")

# Exemplo 4: Matriz com pivô inicial zero que requer troca de linhas
print("\n--- Exemplo 4: Pivô inicial zero ---")
# 0x + y = 3
# 2x + 1y = 7
matriz_exemplo4 = np.array([
    [0, 1, 3],
    [2, 1, 7]
])
solucao4 = resolver_sistema_gauss(matriz_exemplo4)

if solucao4 is not None:
    print(f"Vetor solução [x, y]: {solucao4}\n")
