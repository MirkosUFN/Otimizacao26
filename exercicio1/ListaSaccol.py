import random

# for i in range(50):
# numero = random.randint(1, 100)
# numeros.append(numero)

# Mostrando a lista
print("Lista de números:")
print(numeros)

# 3 Calculando a média
soma = sum(numeros)
media = soma / len(numeros)

print("\nMédia dos valores:", media)
# 4 Encontrando o número mais próximo da média

# Pegando o primeiro número como referência
mais_proximo = numeros[0]
menor_diferenca = abs(numeros[0] - media)

# Comparando com os outros números
for numero in numeros:
    diferenca = abs(numero - media)
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        mais_proximo = numero

print("\nNúmero mais próximo da média:", mais_proximo)
