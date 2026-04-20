import matplotlib.pyplot as plt
import numpy as np

print("--- Plotador de Inequações ---")

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
operador = input("Digite o sinal da inequação (>, >=, <, <=): ")

# cálculo
valores_x = np.linspace(-10, 10, 400)
valores_y_reta = a * valores_x + b

plt.figure(figsize=(8, 6))

estilo_linha = '-' if '=' in operador else '--'
plt.plot(valores_x, valores_y_reta, color='red', linestyle=estilo_linha, label=f'y = {a}x + {b}')

# área de solução (acima ou abaixo da reta)
if '>' in operador:
    # pinta o espaço entre a reta e um limite superior (área de cima)
    plt.fill_between(valores_x, valores_y_reta, valores_y_reta + 100, color='skyblue', alpha=0.4, label='Área de Solução')
elif '<' in operador:
    # pinta o espaço entre a reta e um limite inferior (área de baixo)
    plt.fill_between(valores_x, valores_y_reta, valores_y_reta - 100, color='skyblue', alpha=0.4, label='Área de Solução')


plt.axhline(0, color='black', linewidth=1)  # linha do eixo X
plt.axvline(0, color='black', linewidth=1)  # linha do eixo Y
plt.xlim([-10, 10])
plt.ylim([-20, 20])
plt.grid(True, linestyle=':', alpha=0.6)
plt.title(f'Área de Solução para: y {operador} {a}x + {b}')
plt.legend()

plt.show()