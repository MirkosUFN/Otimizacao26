print("| número de equações deve ser igual ao número de variáveis |")

tamanho = int(input("Digite a quantidade de variáveis e equações do sistema: "))
matriz = []

print("\nInclua o resultado da equação no final.")
print("Exemplo: para x + y + z = 3, digite: 1 1 1 3\n")

for i in range(tamanho):
    texto = input(f"Linha {i + 1} -> coeficientes + resultado: ").split()

    if len(texto) != tamanho + 1:
        print(f"Erro: digite exatamente {tamanho + 1} valores.")
        exit()

    linha_numeros = [float(item) for item in texto]
    matriz.append(linha_numeros)

print("\n---> Iniciando o método de Gauss-Jordan <---")

for i in range(tamanho):
    diagonal = matriz[i][i]

    if diagonal == 0:
        for k in range(i + 1, tamanho):
            if matriz[k][i] != 0:
                matriz[i], matriz[k] = matriz[k], matriz[i]
                print(f"Linha {i+1} trocada com linha {k+1}")
                diagonal = matriz[i][i]
                break
        else:
            print("Erro: sistema não resolvível.")
            exit()

    for j in range(len(matriz[i])):
        matriz[i][j] /= diagonal

    for k in range(tamanho):
        if i != k:
            multiplicador = matriz[k][i]
            for j in range(len(matriz[k])):
                matriz[k][j] -= multiplicador * matriz[i][j]

    print(f"\nPasso {i + 1}:")
    for linha in matriz:
        print(["{:.2f}".format(x) for x in linha])

print("\n-> Resultados:")
for i in range(tamanho):
    print(f"Variável {i + 1} = {matriz[i][-1]:.2f}")