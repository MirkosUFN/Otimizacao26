# Lista de Exercícios: Programação Linear (Interpretação Geométrica)

### Criar e ativar o ambiente virtual (venv) e instalar as dependências para rodar os exercícios

```txt
python3 -m venv venv

source ./venv/bin/activate (no linux)

./venv/Scripts/activate (no windows) 

pip install numpy matplotlib scipy
```

## Exercício 1  - Otimização de Infraestrutura em Nuvem (IaaS)

```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


c = [20, 50]

A = [
    [-4, -8],   # -4*x1 - 8*x2 <= -40  (vCPUs)
    [-8, -32],  # -8*x1 - 32*x2 <= -96 (RAM)
    [1, 1]      # x1 + x2 <= 12        (Cota total)
]

b = [-40, -96, 12]

# Limites das variáveis (x1 >= 0, x2 >= 0)
x_bounds = (0, None)
y_bounds = (0, None)

# Executa a otimização linear
res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method='highs')

# Extraindo os resultados ótimos
x1_opt, x2_opt = res.x
custo_min = res.fun

print("--- RESULTADO DA OTIMIZAÇÃO ---")
print(f"Instâncias Standard (x1): {x1_opt:.2f} (Ideal: {round(x1_opt)})")
print(f"Instâncias High-Performance (x2): {x2_opt:.2f} (Ideal: {round(x2_opt)})")
print(f"Custo Mínimo Horário: ${custo_min:.2f}")



# === CONSTRUÇÃO DO GRÁFICO ===

x1 = np.linspace(0, 15, 400)

r_vcpu = (40 - 4 * x1) / 8

r_ram = (96 - 8 * x1) / 32
r_cota = 12 - x1

plt.figure(figsize=(10, 8))

plt.plot(x1, r_vcpu, label=r'vCPUs: $4x_1 + 8x_2 \geq 40$', color='blue', linestyle='--')
plt.plot(x1, r_ram, label=r'RAM: $8x_1 + 32x_2 \geq 96$', color='green', linestyle='--')
plt.plot(x1, r_cota, label=r'Cota: $x_1 + x_2 \leq 12$', color='red', linestyle='--')

# Restrições de não-negatividade e limites da região viável para o preenchimento
# Região acima de vCPU e RAM, mas abaixo da Cota máxima
y_inferior = np.maximum(np.maximum((40 - 4 * x1) / 8, (96 - 8 * x1) / 32), 0)
y_superior = 12 - x1

plt.fill_between(x1, y_inferior, y_superior, where=(y_superior >= y_inferior), 
                 color='gray', alpha=0.3, label='Região Viável')

vertices_x = [0, 0, 8, 12]
vertices_y = [5, 12, 1, 0]
plt.scatter(vertices_x, vertices_y, color='black', zorder=5)

plt.scatter(x1_opt, x2_opt, color='magenta', marker='*', s=200, zorder=6, 
            label=f'Solução Ótima: ({int(x1_opt)}, {int(x2_opt)})')

plt.xlim(0, 14)
plt.ylim(0, 14)
plt.xlabel('Instâncias Standard ($x_1$)')
plt.ylabel('Instâncias High-Performance ($x_2$)')
plt.title('Interpretação Geométrica do Problema de Programação Linear')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

plt.show()

```

<img width="993" height="793" alt="image" src="https://github.com/user-attachments/assets/312f3680-8a8b-4361-893c-7e39340f6f16" />


| Componente / Parâmetro | Instâncias Standard (x1) | Instâncias High-Performance (x2) | Restrição / Objetivo |
| :--- | :---: | :---: | :---: |
| **Custo Horário** | $20 | $50 | Minimizar Z = 20x1 + 50x2 |
| **vCPUs** | 4 | 8 | >= 40 |
| **RAM** | 8 GB | 32 GB | >= 96 GB |
| **Limite Total (Cota)** | 1 | 1 | <= 12 |
| **Solução Ótima** | **8 instâncias** | **1 instância** | **Custo Mínimo: $210** |

---

## Exercício 2: Alocação de Banda e Roteamento de Tráfego

```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-3, -5]

A = [
    [2, 4],   # 2*x1 + 4*x2 <= 24  (Switch A)
    [3, 2]    # 3*x1 + 2*x2 <= 22  (Switch B)
]
b = [24, 22]

# Executa a otimização linear
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extraindo os resultados ótimos
x1_opt, x2_opt = res.x
qos_max = -res.fun

print(f"Stream Básico (x1): {x1_opt:.2f} mil")
print(f"Stream Premium (x2): {x2_opt:.2f} mil")
print(f"QoS Máximo: {qos_max:.2f}")


# === CONSTRUÇÃO DO GRÁFICO ===

x1 = np.linspace(0, 10, 400)

r_switch_a = (24 - 2 * x1) / 4
r_switch_b = (22 - 3 * x1) / 2

plt.figure(figsize=(10, 8))

plt.plot(x1, r_switch_a, label='Switch A: 2x1 + 4x2 <= 24', color='blue', linestyle='--')
plt.plot(x1, r_switch_b, label='Switch B: 3x1 + 2x2 <= 22', color='green', linestyle='--')

# Restrições de não-negatividade e limites da região viável para o preenchimento
# Região abaixo de Switch A e Switch B
y_superior = np.minimum(r_switch_a, r_switch_b)
y_superior = np.maximum(y_superior, 0)

plt.fill_between(x1, 0, y_superior, where=(y_superior >= 0), color='gray', alpha=0.3, label='Região Viável')

vertices_x = [0, 0, 5, 22/3]
vertices_y = [0, 6, 3.5, 0]
plt.scatter(vertices_x, vertices_y, color='black', zorder=5)

plt.scatter(x1_opt, x2_opt, color='red', marker='*', s=200, zorder=6, 
            label=f'Ponto Ótimo: ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim(0, 9)
plt.ylim(0, 12)
plt.xlabel('Stream Básico (x1 em milhares)')
plt.ylabel('Stream Premium (x2 em milhares)')
plt.title('Resolução Geométrica - Exercício 2')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()

```

<img width="962" height="767" alt="image" src="https://github.com/user-attachments/assets/4ffed568-f7c6-4e21-beaa-c1905f83760c" />


| Componente / Parâmetro | Stream Básico (x1) | Stream Premium (x2) | Capacidade Máxima / Objetivo |
| :--- | :---: | :---: | :---: |
| **Pontuação QoS** | 3 pontos | 5 pontos | Maximizar Z = 3x1 + 5x2 |
| **Switch A** | 2 Gbps | 4 Gbps | <= 24 Gbps |
| **Switch B** | 3 Gbps | 2 Gbps | <= 22 Gbps |
| **Solução Ótima** | **5 mil conexões** | **3,5 mil conexões** | **QoS Máximo: 32.5** |

---

## Exercício 3: Treinamento de Modelos de Deep Learning (Machine Learning)


```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-4, -3]

A = [
    [3, 1],   # 3*x1 + 1*x2 <= 18  (Tempo de GPU)
    [1, 2]    # 1*x1 + 2*x2 <= 16  (Armazenamento)
]
b = [18, 16]

# Executa a otimização linear
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extraindo os resultados ótimos
x1_opt, x2_opt = res.x
impacto_max = -res.fun

print(f"Modelos NLP (x1): {x1_opt:.2f}")
print(f"Modelos Visão (x2): {x2_opt:.2f}")
print(f"Impacto Científico Máximo: {impacto_max:.2f}")


# === CONSTRUÇÃO DO GRÁFICO ===

x1 = np.linspace(0, 10, 400)

r_gpu = 18 - 3 * x1
r_storage = (16 - x1) / 2

plt.figure(figsize=(10, 8))

plt.plot(x1, r_gpu, label='GPU: 3x1 + x2 <= 18', color='blue', linestyle='--')
plt.plot(x1, r_storage, label='Armazenamento: x1 + 2x2 <= 16', color='green', linestyle='--')

# Restrições de não-negatividade e limites da região viável para o preenchimento
# Região abaixo de GPU e Armazenamento
y_superior = np.minimum(r_gpu, r_storage)
y_superior = np.maximum(y_superior, 0)

plt.fill_between(x1, 0, y_superior, where=(y_superior >= 0), color='gray', alpha=0.3, label='Região Viável')

vertices_x = [0, 0, 4, 6]
vertices_y = [0, 8, 6, 0]
plt.scatter(vertices_x, vertices_y, color='black', zorder=5)

plt.scatter(x1_opt, x2_opt, color='red', marker='*', s=200, zorder=6, 
            label=f'Ponto Ótimo: ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim(0, 8)
plt.ylim(0, 10)
plt.xlabel('Modelos NLP (x1)')
plt.ylabel('Modelos de Visão Computacional (x2)')
plt.title('Resolução Geométrica - Exercício 3')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()

```

<img width="962" height="750" alt="image" src="https://github.com/user-attachments/assets/b5321bd5-3c2b-4d0c-b4d4-b4d65a034a98" />


| Componente / Parâmetro | Modelos NLP (x1) | Modelos Visão (x2) | Capacidade Máxima / Objetivo |
| :--- | :---: | :---: | :---: |
| **Impacto Científico** | 4 pontos | 3 pontos | Maximizar Z = 4x1 + 3x2 |
| **Tempo de GPU** | 3 horas | 1 hora | <= 18 horas |
| **Armazenamento** | 1 TB | 2 TB | <= 16 TB |
| **Solução Ótima** | **4 modelos** | **6 modelos** | **Impacto Máximo: 34** |

---


## Exercício 4: Design de Hardware (Sistemas Embarcados / IoT)


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-5, -4]

A = [
    [2, 3],   # 2*x1 + 3*x2 <= 18  (Área de Silício)
    [2, 1]    # 2*x1 + 1*x2 <= 12  (Dissipação Térmica)
]
b = [18, 12]

# Executa a otimização linear
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extraindo os resultados ótimos
x1_opt, x2_opt = res.x
eficiencia_max = -res.fun

print(f"Blocos de Cache (x1): {x1_opt:.2f}")
print(f"Unidades Aritméticas (x2): {x2_opt:.2f}")
print(f"Eficiência Máxima: {eficiencia_max:.2f}")


# === CONSTRUÇÃO DO GRÁFICO ===

x1 = np.linspace(0, 10, 400)

r_area = (18 - 2 * x1) / 3
r_termica = 12 - 2 * x1

plt.figure(figsize=(10, 8))

plt.plot(x1, r_area, label='Área: 2x1 + 3x2 <= 18', color='blue', linestyle='--')
plt.plot(x1, r_termica, label='Térmica: 2x1 + x2 <= 12', color='green', linestyle='--')

# Restrições de não-negatividade e limites da região viável para o preenchimento
# Região abaixo de Área e Térmica
y_superior = np.minimum(r_area, r_termica)
y_superior = np.maximum(y_superior, 0)

plt.fill_between(x1, 0, y_superior, where=(y_superior >= 0), color='gray', alpha=0.3, label='Região Viável')

vertices_x = [0, 0, 4.5, 6]
vertices_y = [0, 6, 3, 0]
plt.scatter(vertices_x, vertices_y, color='black', zorder=5)

plt.scatter(x1_opt, x2_opt, color='red', marker='*', s=200, zorder=6, 
            label=f'Ponto Ótimo: ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim(0, 10)
plt.ylim(0, 14)
plt.xlabel('Blocos de Cache (x1)')
plt.ylabel('Unidades Aritméticas - ALUs (x2)')
plt.title('Resolução Geométrica - Exercício 4')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()
```

<img width="920" height="739" alt="image" src="https://github.com/user-attachments/assets/5b4b7eab-66bb-44e7-970d-9e63ec51fa15" />


| Componente / Parâmetro | Blocos de Cache (x1) | Unidades Aritméticas (x2) | Capacidade Máxima / Objetivo |
| :--- | :---: | :---: | :---: |
| **Eficiência Energética** | 5 unidades | 4 unidades | Maximizar Z = 5x1 + 4x2 |
| **Área de Silício** | 2 mm² | 3 mm² | <= 18 mm² |
| **Dissipação Térmica** | 2 mW | 1 mW | <= 12 mW |
| **Solução Ótima** | **4,5 blocos** | **3 unidades** | **Eficiência Máxima: 34.5** |

---

## Exercício 5: Planejamento de Sprints (Metodologia Ágil / Engenharia de Software)


```python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-8, -5]

A = [
    [4, 4],   # 4*x1 + 4*x2 <= 32  (Desenvolvimento)
    [2, 1]    # 2*x1 + 1*x2 <= 12  (Testes QA)
]
b = [32, 12]

# Executa a otimização linear
res = linprog(c, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Extraindo os resultados ótimos
x1_opt, x2_opt = res.x
valor_max = -res.fun

print(f"Novas Funcionalidades (x1): {x1_opt:.2f}")
print(f"Refatoração / Bugs (x2): {x2_opt:.2f}")
print(f"Valor de Negócio Máximo: {valor_max:.2f}")


# === CONSTRUÇÃO DO GRÁFICO ===

x1 = np.linspace(0, 10, 400)

r_dev = 8 - x1
r_qa = 12 - 2 * x1

plt.figure(figsize=(10, 8))

plt.plot(x1, r_dev, label='Desenvolvimento: 4x1 + 4x2 <= 32', color='blue', linestyle='--')
plt.plot(x1, r_qa, label='Testes (QA): 2x1 + x2 <= 12', color='green', linestyle='--')

# Restrições de não-negatividade e limites da região viável para o preenchimento
# Região abaixo de Desenvolvimento e Testes
y_superior = np.minimum(r_dev, r_qa)
y_superior = np.maximum(y_superior, 0)

plt.fill_between(x1, 0, y_superior, where=(y_superior >= 0), color='gray', alpha=0.3, label='Região Viável')

vertices_x = [0, 0, 4, 6]
vertices_y = [0, 8, 4, 0]
plt.scatter(vertices_x, vertices_y, color='black', zorder=5)

plt.scatter(x1_opt, x2_opt, color='red', marker='*', s=200, zorder=6, 
            label=f'Ponto Ótimo: ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim(0, 8)
plt.ylim(0, 14)
plt.xlabel('Novas Funcionalidades (x1)')
plt.ylabel('Refatoração / Bugs (x2)')
plt.title('Resolução Geométrica - Exercício 5')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()

```

<img width="879" height="720" alt="image" src="https://github.com/user-attachments/assets/8b8467b1-122b-4c6c-9140-951e0edf16d5" />

| Componente / Parâmetro | Novas Funcionalidades (x1) | Refatoração / Bugs (x2) | Capacidade Máxima / Objetivo |
| :--- | :---: | :---: | :---: |
| **Valor de Negócio** | 8 pontos | 5 pontos | Maximizar Z = 8x1 + 5x2 |
| **Desenvolvimento** | 4 horas | 4 horas | <= 32 horas |
| **Testes (QA)** | 2 horas | 1 hora | <= 12 horas |
| **Solução Ótima** | **4 tarefas** | **4 tarefas** | **Valor Máximo: 52** |

