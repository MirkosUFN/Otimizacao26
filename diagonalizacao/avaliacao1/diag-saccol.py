# Método de Elminação de Gauss para resolver sistemas lineares
def print_matriz(m):
    for linha in m:
        print(linha)
    print()

def gauss(m):
    n = len(m)

    # Eliminação (zerar abaixo da diagonal)
    for i in range(n):
        for j in range(i+1, n):
            fator = m[j][i] / m[i][i]
            for k in range(n+1):
                m[j][k] -= fator * m[i][k]

        print(f"Passo {i+1}:")
        print_matriz(m)

    # Substituição regressiva
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = m[i][n]
        for j in range(i+1, n):
            x[i] -= m[i][j]*x[j]
        x[i] /= m[i][i]

    return x

# -------- MAIN --------
n = int(input("Número de variáveis: "))

matriz = []
print("Digite os coeficientes e o resultado (ex: 3 2 4):")

for i in range(n):
    linha = list(map(float, input().split()))
    matriz.append(linha)

print("\nMatriz inicial:")
print_matriz(matriz)

sol = gauss(matriz)

print("Solução:")
for i, v in enumerate(sol):
    print(f"x{i+1} = {v:.2f}")
