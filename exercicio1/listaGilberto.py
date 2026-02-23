import random

lista = [random.randint(0, 100) for _ in range(50)]
# Média
m = sum(lista) / len(lista)
# Menor distância
md = min(abs(x - m) for x in lista)
# Mais próximo
mp = [x for x in lista if abs(x - m) == md]

print(sorted(lista))
print("\nMédia:", m)
print("Números mais próximos da média:", mp)