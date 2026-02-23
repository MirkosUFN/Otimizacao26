import random

lista = []

for _ in range(50):

    num = random.randint(0,100)
    lista.append(num)

media = sum(lista)/ len(lista)

menor = min(abs(x-media) for x in lista)
maior = [x for x in lista if (abs(x-media)) == menor]

print(lista)
print(menor)
print(maior)



