print("| número de equações deve ser igual ao número de variáveis |")
tamanho = int(input("Digite a quantidade de variáveis e equações) do seu sistema: "))
matriz = []


print("\n incluir o resultado da equação no final.")
print("Exemplo: para 1x + 1y = 3, digite: 1 1 3\n")

for i in range(tamanho):
    # valores da linha digitados com espaço
    texto = input(f"Linha {i + 1} -> coeficientes + resultado (com espaços): ").split()

    linha_numeros = []
    #converte tudo para decimal
    for item in texto:
        linha_numeros.append(float(item))

    matriz.append(linha_numeros)

print("\n---> Iniciando a Diagonalização <---")

#algoritmo
for i in range(tamanho):
    diagonal = matriz[i][i]

    if diagonal == 0:
        print("Erro: zero na diagonal principal")
    else:
        #divide a linha pelo pivô para virar 1
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] / diagonal

        #zera o resto da coluna atual (acima e abaixo do 1)
        for k in range(tamanho):
            if i != k:
                multiplicador = matriz[k][i]
                for j in range(len(matriz[k])):
                    matriz[k][j] = matriz[k][j] - multiplicador * matriz[i][j]


        print(f"\nPasso {i + 1}:")
        for linha in matriz:
            print(linha)

print("\nMatriz final:")
for n in matriz:
    print(n)

print("\n-> Resultados:")
#valor final sempre fica na última coluna (índic -1)
for i in range(tamanho):
    print(f"Variável {i + 1} = {matriz[i][-1]}")