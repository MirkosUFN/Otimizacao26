import matplotlib.pyplot as plt

def desenho(x, y):
    plt.scatter(x, y, color='green')
    plt.grid(True)
    plt.show()

# O usuário digita os valores separados por vírgula (ex: 1, 2, 3)
px = [float(i) for i in input("Digite os valores de X (separados por vírgula): ").split(',')]
py = [float(i) for i in input("Digite os valores de Y (separados por vírgula): ").split(',')]

desenho(px, py)
