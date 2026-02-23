import random

numeros = [random.randint(1, 100) for _ in range(50)]
media = sum(numeros) / len(numeros)

menor_diferenca = min(abs(num - media) for num in numeros)
mais_proximos = [num for num in numeros if abs(num - media) == menor_diferenca]
mais_proximos_unicos = list(set(mais_proximos))

print(f"Lista de números:\n{numeros}")
print(f"Média dos números:\n{media:.2f}")
print(f"Menor diferença da média:\n{menor_diferenca:.2f}")
print(f"Número(s) mais próximo(s) da média:\n{mais_proximos_unicos}")
