# Trabalho - Gilberto Morales
# EX 1

import pulp
import numpy as np
import matplotlib.pyplot as plt

custo_high = 90 

prob = pulp.LpProblem("Otimizacao_IaaS", pulp.LpMinimize)

x = pulp.LpVariable('Standard', lowBound=0, cat='Integer')
y = pulp.LpVariable('High_Performance', lowBound=0, cat='Integer')

prob += 50 * x + custo_high * y, "Custo_Total"

prob += 4 * x + 8 * y >= 40, "Min_vCPU"
prob += 8 * x + 32 * y >= 96, "Min_RAM"
prob += x + y <= 12, "Cota_Maxima"

prob.solve()

print("RESULTADO DA OTIMIZAÇÃO")
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Qtd Instâncias Standard (x): {x.varValue}")
print(f"Qtd Instâncias High-Performance (y): {y.varValue}")
print(f"Custo Mínimo: R$ {pulp.value(prob.objective)}")

x_vals = np.linspace(0, 15, 400)

# Restrição 1: 4x + 8y = 40  =>  8y = 40 - 4x  =>  y = (40 - 4x) / 8
y1 = (40 - 4 * x_vals) / 8

# Restrição 2: 8x + 32y = 96 =>  32y = 96 - 8x =>  y = (96 - 8x) / 32
y2 = (96 - 8 * x_vals) / 32

# Restrição 3: x + y = 12    =>  y = 12 - x
y3 = 12 - x_vals

plt.figure(figsize=(10, 8))

plt.plot(x_vals, y1, label=r'$4x + 8y \geq 40$ (vCPU)', color='blue')
plt.plot(x_vals, y2, label=r'$8x + 32y \geq 96$ (RAM)', color='green')
plt.plot(x_vals, y3, label=r'$x + y \leq 12$ (Cota)', color='red')

y_min_viavel = np.maximum(y1, y2)
plt.fill_between(x_vals, y_min_viavel, y3, where=(y3 >= y_min_viavel), 
                 color='gray', alpha=0.3, label='Região Viável')

if prob.status == pulp.LpStatusOptimal:
    plt.plot(x.varValue, y.varValue, 'ko', markersize=8, label='Ponto Ótimo')
    plt.annotate(f'  Ótimo\n  ({int(x.varValue)}, {int(y.varValue)})', 
                 (x.varValue, y.varValue), textcoords="offset points", xytext=(10,0), ha='left')

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('Instâncias Standard (x)')
plt.ylabel('Instâncias High-Performance (y)')
plt.title('Interpretação Geométrica: Otimização IaaS')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# EX 2
import pulp
import numpy as np
import matplotlib.pyplot as plt

custo_high = 90

prob = pulp.LpProblem("Otimizacao_IaaS", pulp.LpMinimize)

x = pulp.LpVariable('Standard', lowBound=0, cat='Integer')
y = pulp.LpVariable('High_Performance', lowBound=0, cat='Integer')

prob += 50 * x + custo_high * y

prob += 4 * x + 8 * y >= 40
prob += 8 * x + 32 * y >= 96
prob += x + y <= 12

prob.solve()

print("=== RESULTADO DA OTIMIZAÇÃO ===")
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Qtd Instâncias Standard (x): {x.varValue}")
print(f"Qtd Instâncias High-Performance (y): {y.varValue}")
print(f"Custo Mínimo: R$ {pulp.value(prob.objective)}")

x_vals = np.linspace(0, 15, 400)

y1 = (40 - 4 * x_vals) / 8
y2 = (96 - 8 * x_vals) / 32
y3 = 12 - x_vals

plt.figure(figsize=(10, 8))

plt.plot(x_vals, y1, label=r'$4x + 8y \geq 40$ (vCPU)', color='blue')
plt.plot(x_vals, y2, label=r'$8x + 32y \geq 96$ (RAM)', color='green')
plt.plot(x_vals, y3, label=r'$x + y \leq 12$ (Cota)', color='red')

y_min_viavel = np.maximum(y1, y2)

plt.fill_between(
    x_vals,
    y_min_viavel,
    y3,
    where=(y3 >= y_min_viavel),
    color='gray',
    alpha=0.3,
    label='Região Viável'
)

if prob.status == pulp.LpStatusOptimal:
    plt.plot(x.varValue, y.varValue, 'ko', markersize=8, label='Ponto Ótimo')

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('Instâncias Standard (x)')
plt.ylabel('Instâncias High-Performance (y)')
plt.title('Interpretação Geométrica: Otimização IaaS')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

# EX 3

import pulp
import numpy as np
import matplotlib.pyplot as plt

prob = pulp.LpProblem("Otimizacao_DeepLearning", pulp.LpMaximize)

x = pulp.LpVariable('Modelos_NLP', lowBound=0, cat='Integer')
y = pulp.LpVariable('Modelos_Visao', lowBound=0, cat='Integer')

prob += 4 * x + 3 * y

prob += 3 * x + 1 * y <= 18
prob += 1 * x + 2 * y <= 16

prob.solve()

print("=== RESULTADO DA OTIMIZAÇÃO (EXERCÍCIO 3) ===")
print(f"Status: {pulp.LpStatus[prob.status]}")
print(f"Modelos NLP (x): {int(x.varValue)}")
print(f"Modelos de Visão (y): {int(y.varValue)}")
print(f"Impacto Científico Máximo: {int(pulp.value(prob.objective))} pontos")

x_vals = np.linspace(0, 10, 400)

y1 = 18 - 3 * x_vals
y2 = (16 - x_vals) / 2

plt.figure(figsize=(10, 8))

plt.plot(x_vals, y1, label=r'$3x + y \leq 18$ (Horas de GPU)', color='blue')
plt.plot(x_vals, y2, label=r'$x + 2y \leq 16$ (Storage NVMe)', color='green')

y_max_viavel = np.minimum(y1, y2)
y_max_viavel = np.maximum(y_max_viavel, 0)

plt.fill_between(
    x_vals,
    0,
    y_max_viavel,
    color='gray',
    alpha=0.3,
    label='Região Viável'
)

if prob.status == pulp.LpStatusOptimal:
    plt.plot(x.varValue, y.varValue, 'ko', markersize=8, label='Ponto Ótimo')

plt.xlim(0, 10)
plt.ylim(0, 20)
plt.xlabel('Quantidade de Modelos NLP (x)')
plt.ylabel('Quantidade de Modelos de Visão (y)')
plt.title('Interpretação Geométrica: Treino de Modelos AI')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

# EX 4 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, CheckButtons

fig, ax = plt.subplots(figsize=(10, 8))
plt.subplots_adjust(bottom=0.25, left=0.15)

x_vals = np.linspace(0, 10, 400)

y1 = (18 - 2 * x_vals) / 3
y2 = 12 - 2 * x_vals

ax.plot(x_vals, y1, label=r'$2x + 3y \leq 18$ (Área)', color='blue')
ax.plot(x_vals, y2, label=r'$2x + y \leq 12$ (Térmica)', color='red')

y_max_viavel = np.minimum(y1, y2)
y_max_viavel = np.maximum(y_max_viavel, 0)

ax.fill_between(
    x_vals,
    0,
    y_max_viavel,
    color='lightgreen',
    alpha=0.4,
    label='Região Viável'
)

ax.plot(4.5, 3, 'ko', markersize=8, label='Ótimo Contínuo (4.5, 3) Z=34.5')

pontos_x = []
pontos_y = []

for i in range(10):
    for j in range(10):
        if 2*i + 3*j <= 18 and 2*i + j <= 12:
            pontos_x.append(i)
            pontos_y.append(j)

scatter_inteiros = ax.scatter(
    pontos_x,
    pontos_y,
    color='purple',
    s=30,
    zorder=5,
    label='Pontos Inteiros Viáveis',
    visible=False
)

ponto_otimo_inteiro, = ax.plot(
    5,
    2,
    'ro',
    markersize=10,
    zorder=6,
    label='Ótimo Inteiro (5, 2) Z=33',
    visible=False
)

Z_init = 10

linha_Z, = ax.plot(
    x_vals,
    (Z_init - 5*x_vals)/4,
    'k--',
    label=r'Função Objetivo ($5x+4y=Z$)'
)

ax.set_xlim(0, 8)
ax.set_ylim(0, 8)

ax.set_xlabel('Quantidade de Blocos de Cache (x)')
ax.set_ylabel('Quantidade de ALUs (y)')

ax.set_title('Ex 4: Design de Hardware - Solução Contínua vs Inteira')

ax.legend(loc='upper right')

ax.grid(True, linestyle='--', alpha=0.6)

ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])

slider_z = Slider(ax_slider, 'Eficiência (Z)', 0, 40, valinit=Z_init)

def update(val):
    z_atual = slider_z.val
    linha_Z.set_ydata((z_atual - 5*x_vals) / 4)
    fig.canvas.draw_idle()

slider_z.on_changed(update)

ax_check = plt.axes([0.8, 0.02, 0.15, 0.15])

check = CheckButtons(ax_check, ['Mostrar\nInteiros'], [False])

def toggle_inteiros(label):
    vis = scatter_inteiros.get_visible()
    scatter_inteiros.set_visible(not vis)
    ponto_otimo_inteiro.set_visible(not vis)
    fig.canvas.draw_idle()

check.on_clicked(toggle_inteiros)

plt.show()

# EX 5

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 400)

y1 = (32 - 4*x1) / 4
y2 = 12 - 2*x1

plt.figure(figsize=(8, 6))

plt.plot(x1, y1, label='4x1 + 4x2 <= 32 (Horas Dev)', color='blue')
plt.plot(x1, y2, label='2x1 + x2 <= 12 (Horas QA)', color='orange')

plt.fill(
    [0, 0, 4, 6],
    [0, 8, 4, 0],
    color='lightgreen',
    alpha=0.4,
    label='Região Viável'
)

plt.plot(4, 4, 'ro', markersize=10, label='Solução Ótima (4, 4)')

plt.xlim(0, 8)
plt.ylim(0, 10)

plt.xlabel('x1 (Novas Funcionalidades)')
plt.ylabel('x2 (Tarefas de Refatoração)')

plt.title('Exercicio 5: Planeamento de Sprint (Ágil)')

plt.legend()
plt.grid(True)

plt.show()
