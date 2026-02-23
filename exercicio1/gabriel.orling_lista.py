import random
import statistics

numeros = [random.randint(1, 100) for _ in range(50)]

media = statistics.mean(numeros)

proximos = sorted(numeros, key=lambda x: abs(x - media))

print(f"--- Resultados ---")
print(f"Lista gerada: {numeros}")
print(f"\nMédia aritmética: {media:.2f}")

encontrou = False
for numero in numeros:
    if (media - 3) <= numero <= (media + 3):
        print(f"-> {numero}")
        encontrou = True

if not encontrou:
    print("Nenhum número encontrado neste intervalo.")
