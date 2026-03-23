def print_matrix(m):
    for row in m:
        print(["{:.2f}".format(x) for x in row])
    print()

n = int(input("Digite o número de variáveis/equações: (incluindo o resultado)"))

matrix = []
for i in range(n):
    while True:
        row = list(map(float, input(f"Digite os {n+1} valores da equação {i+1}: ").split()))
        if len(row) == n + 1:
            matrix.append(row)
            break
        else:
            print("Quantidade incorreta de valores, tente novamente.")

print("\nMatriz inicial:")
print_matrix(matrix)

for i in range(n):
    pivot = matrix[i][i]
    for j in range(n + 1):
        matrix[i][j] /= pivot
    print_matrix(matrix)

    for k in range(n):
        if k != i:
            factor = matrix[k][i]
            for j in range(n + 1):
                matrix[k][j] -= factor * matrix[i][j]
            print_matrix(matrix)

solution = [matrix[i][n] for i in range(n)]

print("Solução:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.2f}")
