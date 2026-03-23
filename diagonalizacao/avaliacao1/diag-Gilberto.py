import os
from fractions import Fraction

def mostrar_matriz(mat, title="Estado da Matriz"):
    """Mostra a matriz aumentada de forma organizada."""
    print(f"\n{title}")
    size = len(mat)

    for row in mat:
        left = " ".join(f"{str(x):>7}" for x in row[:-1])
        right = f"{str(row[-1]):>7}"
        print(f"| {left} || {right} |")

    print("-" * (10 * (size + 1)))

def ler_valores():
    """Lê os dados do usuário e monta a matriz."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Método de Gauss-Jordan ===")

    try:
        size = int(input("Quantidade de variáveis: "))
        if size <= 0:
            print("Valor inválido.")
            return None
    except:
        print("Entrada inválida.")
        return None

    matrix = []

    for i in range(size):
        print(f"\nEquação {i+1}")
        line = []

        for j in range(size):
            val = input(f"Coeficiente x{j+1}: ")
            line.append(Fraction(val))

        result = input("Termo independente: ")
        line.append(Fraction(result))

        matrix.append(line)

    return matrix

def gauss_jordan():
    mat = ler_valores()
    if mat is None:
        return

    n = len(mat)
    mostrar_matriz(mat, "Matriz Inicial")

    for col in range(n):

        # Pivotamento
        if mat[col][col] == 0:
            for row in range(col + 1, n):
                if mat[row][col] != 0:
                    print(f"\nTroca: L{col+1} <-> L{row+1}")
                    mat[col], mat[row] = mat[row], mat[col]
                    mostrar_matriz(mat)
                    break
            else:
                print("\nSistema sem solução única.")
                return

        # Normalização
        pivot = mat[col][col]
        if pivot != 1:
            print(f"\nL{col+1} = L{col+1} / {pivot}")
            mat[col] = [x / pivot for x in mat[col]]
            mostrar_matriz(mat)

        # Eliminação
        for row in range(n):
            if row != col:
                factor = mat[row][col]
                if factor != 0:
                    print(f"\nL{row+1} = L{row+1} - ({factor}) * L{col+1}")
                    mat[row] = [
                        mat[row][k] - factor * mat[col][k]
                        for k in range(n + 1)
                    ]
                    mostrar_matriz(mat)

    print("\n=== Solução ===")
    mostrar_matriz(mat)

    for i in range(n):
        print(f"x{i+1} = {mat[i][-1]}")

if __name__ == "__main__":
    try:
        gauss_jordan()
    except Exception as err:
        print(f"Erro: {err}")
