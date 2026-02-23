import random

numeros = [random.randint(1, 100) for _ in range(50)]

media = sum(numeros) / len(numeros)

menores = [n for n in numeros if n < media]
maiores = [n for n in numeros if n > media]

mais_proximo_antes = max(menores) if menores else None
mais_proximo_depois = min(maiores) if maiores else None

resultado = [mais_proximo_antes, media, mais_proximo_depois]

print("Lista:", numeros)
print("Média:", media)
print("Resultado:", resultado)