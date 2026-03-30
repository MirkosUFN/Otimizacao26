import matplotlib.pyplot as plt

pontos_x = []
pontos_y = []

print("Digite as coordenadas")

while True:
    entrada_x = input("Coordenada X: ")
    entrada_y = input("Coordenada Y: ")

    try:
        x = float(entrada_x)
        y = float(entrada_y)
    except ValueError:
        print("Digite apenas números!")
        continue

    pontos_x.append(x)
    pontos_y.append(y)

    fechar = input("Deseja parar? (s/n): ")
    if fechar.lower() == 's':
        break

plt.figure(figsize=(6, 6))
plt.scatter(pontos_x, pontos_y, color='red', zorder=5)

plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

for i in range(len(pontos_x)):
    plt.text(pontos_x[i] + 0.1, pontos_y[i] + 0.1,
             f'({pontos_x[i]}, {pontos_y[i]})')

plt.grid(True, linestyle='--', alpha=0.7)
plt.title("Gráfico de Pontos")
plt.show()