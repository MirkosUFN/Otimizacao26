import random

lista = [random.randint (1,100) for i in range(50)]
media = sum(lista) / len(lista)
menor = min(abs(n - media) for n in lista)
proximos = [n for n in lista if abs(n - media) == menor]

print(f"Lista: {lista}")
print(f"Média: {media}")
print(f"Mais próximos: {proximos}")