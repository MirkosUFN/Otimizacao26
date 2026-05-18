import random

def encontrar_proximos_da_media():
    # 1. Gera uma lista com 50 números inteiros aleatórios (ex: entre 1 e 100)
    numeros = [random.randint(1, 100) for _ in range(50)]
    
    # 2. Calcula a média dos valores
    media = sum(numeros) / len(numeros)
    
    # 3. Encontra a menor diferença (distância absoluta) entre a média e os números
    menor_distancia = min(abs(num - media) for num in numeros)
    
    # 4. Filtra os números que possuem essa exata menor distância
    # Usamos set() para remover duplicatas caso o mesmo número apareça várias vezes na lista
    mais_proximos = list(set(num for num in numeros if abs(num - media) == menor_distancia))
    
    # Exibição dos resultados
    print(f"Lista gerada ({len(numeros)} números):")
    print(numeros)
    print("-" * 50)
    print(f"Média dos valores: {media:.2f}")
    print(f"Número(s) mais próximo(s) da média: {mais_proximos}")

# Executa o algoritmo
encontrar_proximos_da_media()