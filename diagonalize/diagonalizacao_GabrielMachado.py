def imprimir_matriz(msg, matriz):
    print(f"\n=> {msg}")
    for linha in matriz:
        print(f"   [ {linha[0]:.2f}  {linha[1]:.2f} | {linha[2]:.2f} ]")

def resolver_sistema_2x3(m_entrada):
    m = [linha[:] for linha in m_entrada]
    
    imprimir_matriz("Matriz Inicial:", m)

    pivo1 = m[0][0]
  
    if pivo1 == 0:
        m[0], m[1] = m[1], m[0]
        pivo1 = m[0][0]
        imprimir_matriz("Troca de linhas (L1 <-> L2):", m)

    m[0] = [elemento / pivo1 for elemento in m[0]]
    imprimir_matriz(f"Normalizar L1 (L1 = L1 / {pivo1:.2f}):", m)

    fator = m[1][0]
    m[1] = [m[1][i] - fator * m[0][i] for i in range(3)]
    imprimir_matriz(f"Zerar Coluna 1 na L2 (L2 = L2 - ({fator:.2f} * L1)):", m)

    pivo2 = m[1][1]
  
    if pivo2 == 0:
        return "O sistema não possui solução única (pivô nulo na L2)."
    
    m[1] = [elemento / pivo2 for elemento in m[1]]
    imprimir_matriz(f"Normalizar L2 (L2 = L2 / {pivo2:.2f}):", m)

    fator_reverso = m[0][1]
    m[0] = [m[0][i] - fator_reverso * m[1][i] for i in range(3)]
    imprimir_matriz(f"Zerar Coluna 2 na L1 (L1 = L1 - ({fator_reverso:.2f} * L2)):", m)

    x = m[0][2]
    y = m[1][2]
    return [x, y]

matriz_coeficientes = [
    [2.0, 1.0, 5.0],
    [1.0, -3.0, -1.0]
]

vetor_solucao = resolver_sistema_2x3(matriz_coeficientes)

print("\n" + "="*30)
print(f"Vetor Solução [x, y]: {vetor_solucao}")
print("="*30)
