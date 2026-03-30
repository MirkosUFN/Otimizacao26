import matplotlib.pyplot as plt

pontos = []

# Entrada de pontos
while True:
    print("\nDigite as coordenadas do ponto:")
    x = float(input("Valor de x: "))
    y = float(input("Valor de y: "))
    
    pontos.append((x, y))
    
    continuar = input("Deseja adicionar outro ponto? (s/n): ").lower()
    if continuar != 's':
        break

# Separar coordenadas
x_vals = [p[0] for p in pontos]
y_vals = [p[1] for p in pontos]

# Criar gráfico
plt.figure(figsize=(6,6))

# Plotar pontos
plt.scatter(x_vals, y_vals, color='red')

# Nomear pontos com coordenadas
for i, (x, y) in enumerate(pontos, start=1):
    plt.text(x + 0.1, y + 0.1, f'P{i} ({x:.2f}, {y:.2f})')

# Desenhar eixos
plt.axhline(0, color='black', linewidth=1.5, label='Eixo X')
plt.axvline(0, color='black', linewidth=1.5, label='Eixo Y')

# Ajustar limites automaticamente, garantindo que 0 esteja incluído
plt.xlim(min(min(x_vals), 0) - 3, max(max(x_vals), 0) + 3)
plt.ylim(min(min(y_vals), 0) - 3, max(max(y_vals), 0) + 3)

# Adicionar grade
plt.grid(True, linestyle='--', alpha=0.6)

# Legenda
plt.legend()

# Título
plt.title("Plano Cartesiano com Pontos")

# Mostrar gráfico
plt.show()