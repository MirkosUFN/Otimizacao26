import matplotlib.pyplot as plt

def gerar_reta(a, b, x0, x1):
    x_values = list(range(x0, x1 + 1))
    y_values = [(a * x) + b for x in x_values]
    return x_values, y_values

def verificar_retas(a1, b1, a2, b2):
    if a1 == a2 and b1 == b2:
        return "As retas são COINCIDENTES (mesma reta)"
    elif a1 == a2:
        return "As retas são PARALELAS"
    else:
        return "As retas SE CRUZAM"

a1, b1 = 2, 5
a2, b2 = 2, -3
a3, b3 = -1, 2

x1, y1 = gerar_reta(a1, b1, -5, 5) # linha 1
x2, y2 = gerar_reta(a2, b2, -5, 5) # li
x3, y3 = gerar_reta(a3, b3, -5, 5)

print("Reta 1 e Reta 2:", verificar_retas(a1, b1, a2, b2))
print("Reta 1 e Reta 3:", verificar_retas(a1, b1, a3, b3))

plt.figure(figsize=(8, 6))

plt.plot(x1, y1, label="Reta 1 (y=2x+5)", color='blue')
plt.plot(x2, y2, label="Reta 2 (y=2x-3)", color='cyan', linestyle='--')
plt.plot(x3, y3, label="Reta 3 (y=-x+2)", color='red')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.title("Comparação de Retas")
plt.show()