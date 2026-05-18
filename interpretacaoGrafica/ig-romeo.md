## Exercício 1

```python
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 15, 400)
x2_vcpu = (40 - 4*x1) / 8
x2_ram = (96 - 8*x1) / 32
x2_limite = 12 - x1

plt.figure(figsize=(10, 8))

plt.plot(x1, x2_vcpu, label=r'$4x_1 + 8x_2 \geq 40$', color='blue')
plt.plot(x1, x2_ram, label=r'$8x_1 + 32x_2 \geq 96$', color='green')
plt.plot(x1, x2_limite, label=r'$x_1 + x_2 \leq 12$', color='orange')

y_lower = np.maximum(np.maximum(x2_vcpu, x2_ram), 0)
plt.fill_between(x1, y_lower, x2_limite, where=(x2_limite >= y_lower), 
                 color='gray', alpha=0.3, label='Região Viável')

vertices = [(12, 0), (8, 1), (0, 5), (0, 12)]

plt.plot(8, 1, 'ro', markersize=10, label='Ponto Ótimo (8, 1) -> Z=$210')

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('Instâncias Standard ($x_1$)', fontsize=12)
plt.ylabel('Instâncias High-Performance ($x_2$)', fontsize=12)
plt.title('Otimização de Infraestrutura em Nuvem (Método Gráfico)', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
```

<img width="987" height="810" alt="{2871DCBB-07BC-4C09-A017-F0C43F0F5602}" src="https://github.com/user-attachments/assets/51270746-d5d0-4397-bdda-5c1fcfb6d3a4" />

---

## Exercício 2

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-3, -5] 
A = [[2, 4], 
     [3, 2]]
b = [24, 22]

limites = [(0, None), (0, None)]

resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')
x1_opt, x2_opt = resultado.x
qos_maximo = -resultado.fun

print(f"Ponto extremo ideal (Vértice): x1 = {x1_opt:.2f}, x2 = {x2_opt:.2f}")
print(f"Pontuação Máxima de QoS: {qos_maximo:.2f}")

x1 = np.linspace(0, 15, 200)

x2_retaA = (24 - 2*x1) / 4
x2_retaB = (22 - 3*x1) / 2

plt.figure(figsize=(8, 6))

plt.plot(x1, x2_retaA, label=r'$2x_1 + 4x_2 \leq 24$', color='blue')
plt.plot(x1, x2_retaB, label=r'$3x_1 + 2x_2 \leq 22$', color='red')

plt.fill_between(x1, np.minimum(x2_retaA, x2_retaB), where=(x1 >= 0) & (np.minimum(x2_retaA, x2_retaB) >= 0), 
                 color='gray', alpha=0.3, label='Região Viável')

plt.scatter(x1_opt, x2_opt, color='green', zorder=5, s=100, label=f'Ponto Ótimo ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim((0, 10))
plt.ylim((0, 12))
plt.xlabel('Stream Básico ($x_1$)')
plt.ylabel('Stream Premium ($x_2$)')
plt.title('Polígono da Região Viável e Ponto Ótimo')
plt.legend()
plt.grid(True)
plt.show()
```

<img width="790" height="618" alt="{60C64825-AB22-4111-9B65-787DB7094B5E}" src="https://github.com/user-attachments/assets/5b7af518-6dde-45ca-88c5-98bdfe5646ae" />

---

## Exercício 3


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-4, -3] 
A = [[3, 1], 
     [1, 2]]
b = [18, 16]

limites = [(0, None), (0, None)]

resultado = linprog(c, A_ub=A, b_ub=b, bounds=limites, method='highs')
x1_opt, x2_opt = resultado.x
impacto_maximo = -resultado.fun

print("--- RESULTADOS ---")
print(f"Modelos NLP (x1): {x1_opt:.2f}")
print(f"Modelos de Visão (x2): {x2_opt:.2f}")
print(f"Impacto Científico Máximo: {impacto_maximo:.2f} pontos")

x1 = np.linspace(0, 10, 200)
x2_gpu = 18 - 3 * x1
x2_storage = (16 - x1) / 2

plt.figure(figsize=(8, 6))

plt.plot(x1, x2_gpu, label=r'$3x_1 + x_2 \leq 18$ (gpU)', color='blue')
plt.plot(x1, x2_storage, label=r'$x_1 + 2x_2 \leq 16$ (storage)', color='red')

plt.fill_between(x1, 0, np.minimum(x2_gpu, x2_storage), 
                 where=(x1 >= 0) & (np.minimum(x2_gpu, x2_storage) >= 0), 
                 color='gray', alpha=0.3, label='Região viavel')

plt.scatter(x1_opt, x2_opt, color='green', zorder=5, s=100, label=f'Ponto otimo ({x1_opt:.1f}, {x2_opt:.1f})')

plt.xlim((0, 8))
plt.ylim((0, 20))
plt.xlabel('Modelos NLP ($x_1$)')
plt.ylabel('Modelos de Visão ($x_2$)')
plt.title('Maximização do Impacto Científico - Região Viável')
plt.legend()
plt.grid(True)
plt.show()
```

<img width="791" height="616" alt="{F8A6C990-71D4-4B6A-9C85-B8001D940E7E}" src="https://github.com/user-attachments/assets/b3910637-9d79-4840-b010-5f012fe7fdbc" />

---

## Exercício 4

```python
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 400)
x2_area = (18 - 2*x1) / 3
x2_termica = 12 - 2*x1

plt.figure(figsize=(10, 8))

plt.plot(x1, x2_area, label=r'$2x_1 + 3x_2 \leq 18$ (Área)', color='blue')
plt.plot(x1, x2_termica, label=r'$2x_1 + x_2 \leq 12$ (Térmica)', color='red')

y_upper = np.minimum(x2_area, x2_termica)
plt.fill_between(x1, 0, y_upper, where=(y_upper >= 0), 
                 color='gray', alpha=0.3, label='Região Viável')

vertices = [(0, 0), (0, 6), (6, 0), (4.5, 3)]

plt.plot(4.5, 3, 'ro', markersize=10, label='Ponto Ótimo Teórico (4.5, 3)')

x2_nivel = (34.5 - 5*x1) / 4
plt.plot(x1, x2_nivel, 'g--', label=r'Reta de Nível Ótima ($Z = 34.5$)', linewidth=2)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Blocos de Memória Cache ($x_1$)', fontsize=12)
plt.ylabel('Unidades Aritméticas (ALUs) ($x_2$)', fontsize=12)
plt.title('Maximização de Eficiência do Chip (Método Gráfico)', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
```

<img width="987" height="809" alt="{7BF31D86-266A-4AC6-A6AB-838C44965A1F}" src="https://github.com/user-attachments/assets/e8c7d6c7-04fc-43b5-b2ef-2dc2e10abba3" />

---

## Exercício 5

```python
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 400)
x2_dev = 8 - x1
x2_qa = 12 - 2*x1

plt.figure(figsize=(10, 8))

plt.plot(x1, x2_dev, label=r'$4x_1 + 4x_2 \leq 32$ (Dev)', color='blue')
plt.plot(x1, x2_qa, label=r'$2x_1 + x_2 \leq 12$ (QA)', color='green')

y_upper = np.minimum(x2_dev, x2_qa)
plt.fill_between(x1, 0, y_upper, where=(y_upper >= 0) & (x1 >= 0), 
                 color='gray', alpha=0.3, label='Região Viável')

vertices = [(0, 0), (6, 0), (0, 8), (4, 4)]

plt.plot(4, 4, 'ro', markersize=10, label='Ponto Ótimo (4, 4) -> Z=52')

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Novas Funcionalidades ($x_1$)', fontsize=12)
plt.ylabel('Refatoração ($x_2$)', fontsize=12)
plt.title('Planejamento da Sprint: Maximização de Valor', fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()
```

<img width="990" height="818" alt="{D3B714FA-EF31-4F93-86F0-EAB4B23AB9B5}" src="https://github.com/user-attachments/assets/fe493248-3ef8-48c1-8e55-fbe6ec484145" />

---
