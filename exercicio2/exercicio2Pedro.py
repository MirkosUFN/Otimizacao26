import matplotlib.pyplot as plt
from fractions import Fraction

print("Informe o Ponto 1:")
x1 = float(input("  Digite o valor de x1: "))
y1 = float(input("  Digite o valor de y1: "))

print("Informe o Ponto 2:")
x2 = float(input("  Digite o valor de x2: "))
y2 = float(input("  Digite o valor de y2: "))

if not ((x1 == 0 and y2 == 0) or (y1 == 0 and x2 == 0)):
    print("\nErro! Um ponto deve ter x=0 e o outro deve ter y=0.")
    print("Exemplo válido: (0, 2) e (-1, 0)")
else:
    a = Fraction(y2 - y1) / Fraction(x2 - x1)
    b = Fraction(y1) - a * Fraction(x1)

    print(f"\nPonto 1: ({x1}, {y1})")
    print(f"Ponto 2: ({x2}, {y2})")

    if b > 0:
        formula = f"y = {a}x + {b}"
    elif b < 0:
        formula = f"y = {a}x - {abs(b)}"
    else:
        formula = f"y = {a}x"

    print(f"Fórmula da reta: {formula}")

    x_reta = list(range(-7, 8))
    y_reta = [float(a) * x + float(b) for x in x_reta]

    plt.plot(x_reta, y_reta, color='red', label=formula)
    plt.scatter([x1, x2], [y1, y2], color='green', zorder=5, label=f'Pontos: ({x1},{y1}) e ({x2},{y2})')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.xlim(-7, 7)
    plt.ylim(-7, 7)
    plt.grid(True)
    plt.title('Reta y = ax + b')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    plt.show()
