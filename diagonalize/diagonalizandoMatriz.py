import os
from fractions import Fraction # Biblioteca para trabalhar com frações sem transformar em números com virgula

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_matriz(matriz):
    print("\nMatriz Atual:")
    for linha in matriz:
        l0 = str(linha[0])
        l1 = str(linha[1])
        l2 = str(linha[2])
        print(f"[ {l0:>5} {l1:>5} | {l2:>5} ]") # >5 diz que quero um espaçamento de 5 caracteres entre os valores
    print("-" * 35)

def diagonalizar():
    limpar_tela()
    print("=== Diagonalização de Matriz 2x3 (Método de Gauss-Jordan) ===")
    print("Insira os coeficientes para o sistema:")
    print("Linha 1: aX + bY = LD1")
    print("Linha 2: cX + dY = LD2\n")

    # Entrada de dados convertendo para Fraction para evitar os numeros com virgula
    try:
        x1 = Fraction(input("Linha 1 - Valor de X: "))
        y1 = Fraction(input("Linha 1 - Valor de Y: "))
        ld1 = Fraction(input("Linha 1 - Valor de LD: "))
        
        x2 = Fraction(input("Linha 2 - Valor de X: "))
        y2 = Fraction(input("Linha 2 - Valor de Y: "))
        ld2 = Fraction(input("Linha 2 - Valor de LD: "))
    except ValueError:
        print("Erro: Por favor, insira números válidos (ex: 2, 0.5, 3/4).")
        return

    matriz = [
        [x1, y1, ld1],
        [x2, y2, ld2]
    ]

    exibir_matriz(matriz)

    # PASSO 1: Fazer M[0][0] ser 1
    pivo1 = matriz[0][0]
    if pivo1 == 0:
        # Troca de linhas se o pivô for zero
        print("Aviso: Pivô L1C1 é zero. Trocando linhas...")
        matriz[0], matriz[1] = matriz[1], matriz[0]
        pivo1 = matriz[0][0]
        exibir_matriz(matriz)

    if pivo1 != 1:
        print(f"\nOperação: L1 = L1 / {pivo1}")
        print(f"Cálculo L1: [{matriz[0][0]}/{pivo1}, {matriz[0][1]}/{pivo1}, {matriz[0][2]}/{pivo1}]")
        matriz[0] = [val / pivo1 for val in matriz[0]]
        exibir_matriz(matriz)

    # PASSO 2: Fazer M[1][0] ser 0 
    fator = matriz[1][0]  # O fator é o valor multiplicador usado para zerar o elemento (torná-lo 0), 
                          # no caso o fator é o numero que queremos zerar após transformar o pivo em 1, devemos sempre transformar o pivô em 1 antes de zerar os outros elementos
    if fator != 0:
        print(f"\nOperação: L2 = L2 - ({fator} * L1)")
        print(f"Cálculo L2: [{matriz[1][0]} - ({fator} * {matriz[0][0]}), "
              f"{matriz[1][1]} - ({fator} * {matriz[0][1]}), "
              f"{matriz[1][2]} - ({fator} * {matriz[0][2]})]")
        matriz[1] = [matriz[1][i] - (fator * matriz[0][i]) for i in range(3)]
        exibir_matriz(matriz)

    # PASSO 3: Fazer M[1][1] ser 1 
    pivo2 = matriz[1][1]
    if pivo2 == 0:
        print("\nErro: O sistema não possui solução única (pivô L2C2 é zero).")
        return

    if pivo2 != 1:
        print(f"\nOperação: L2 = L2 / {pivo2}")
        print(f"Cálculo L2: [{matriz[1][0]}/{pivo2}, {matriz[1][1]}/{pivo2}, {matriz[1][2]}/{pivo2}]")
        matriz[1] = [val / pivo2 for val in matriz[1]]
        exibir_matriz(matriz)

    # PASSO 4: Fazer M[0][1] ser 0
    fator = matriz[0][1]
    if fator != 0:
        print(f"\nOperação: L1 = L1 - ({fator} * L2)")
        print(f"Cálculo L1: [{matriz[0][0]} - ({fator} * {matriz[1][0]}), "
              f"{matriz[0][1]} - ({fator} * {matriz[1][1]}), "
              f"{matriz[0][2]} - ({fator} * {matriz[1][2]})]")
        matriz[0] = [matriz[0][i] - (fator * matriz[1][i]) for i in range(3)]
        exibir_matriz(matriz)

    print("\n=== Resultado Final (Matriz Diagonalizada) ===")
    exibir_matriz(matriz)
    print(f"X = {matriz[0][2]}")
    print(f"Y = {matriz[1][2]}")

if __name__ == "__main__":
    diagonalizar()
