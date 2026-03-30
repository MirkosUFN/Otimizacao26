import matplotlib.pyplot as plt

valorX = []
valorY = []

print("Digite as coordenadas. Quando quiser ver o grafico apenas aperte ENTER")

while True:
    entradaX = input("Digite a coordenada X (ou ENTER para sair): ")
    if entradaX == "":
        break  
    entradaY = input("Digite a coordenada Y: ")
    valorX.append(float(entradaX))
    valorY.append(float(entradaY))

plt.plot(valorX, valorY, marker='o', color='blue', linestyle='-')
plt.grid(True)
plt.show()