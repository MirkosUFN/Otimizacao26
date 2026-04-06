import random

def gerar_y(a, b, x):
  y = []
  for i in range(len(x)):
    y.append(a * x[i] + b)
  return y

def gerar_x():
  x = []
  for i in range(5):
    x.append(random.randint(0, 10))
  return x


def plotar_pontos(x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linestyle='-', color='b', label='reta')
    plt.scatter(x, y, color='red', marker='o', label='pontos')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    for i in range(len(x)):
        plt.text(x[i] + 0.1, y[i] + 0.1, f'P{i+1}({x[i]}, {y[i]})')

    plt.legend()
    plt.show()

a = 2
b = 4
x = gerar_x()
print(f"pontos de x", x)

y = gerar_y(a, b, x)
print(f"pontos de y", y)

plotar_pontos(x, y)