import random

class GerarNumero:
    def __init__(self):self.numeros = []



    def gerar_numero(self):
        for _ in range(50):
            numero = random.randint(0, 49)
            self.numeros.append(numero)

        self.numeros.sort()
        print("Lista gerada:")
        print(self.numeros)




    def calcular_media(self):
        if not self.numeros:
            return

        soma = sum(self.numeros)
        media = soma / len(self.numeros)

        # Encontrar número mais próximo da média
        mais_proximo = self.numeros[0]
        menor_diferenca = abs(mais_proximo - media)

        for n in self.numeros:
            diff = abs(n - media)
            if diff < menor_diferenca:
                menor_diferenca = diff
                mais_proximo = n

        limite_inferior = mais_proximo - 3
        limite_superior = mais_proximo + 3

        numeros_no_range = [
            n for n in self.numeros
            if limite_inferior <= n <= limite_superior
        ]



        print(f"\nMédia: {media:.2f}")
        print(f"Referência (mais próximo da média): {mais_proximo}")
        print(f"Números no intervalo [{limite_inferior} - {limite_superior}]:")
        print(numeros_no_range)



if __name__ == "__main__":
    gerador = GerarNumero()
    gerador.gerar_numero()
    gerador.calcular_media()