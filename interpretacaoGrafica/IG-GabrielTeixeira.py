import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# EXERCÍCIO 1: Otimização de Infraestrutura em Nuvem (Minimização)
# =============================================================================
plt.figure(figsize=(8, 6))
x = np.linspace(0, 15, 400)

# Restrições
y1 = (40 - 4*x) / 8  # 4x1 + 8x2 >= 40
y2 = (96 - 8*x) / 32 # 8x1 + 32x2 >= 96
y3 = 12 - x          # x1 + x2 <= 12

# Plotando as retas
plt.plot(x, np.maximum(0, y1), label=r'$4x_1 + 8x_2 \geq 40$ (vCPUs)', color='blue')
plt.plot(x, np.maximum(0, y2), label=r'$8x_1 + 32x_2 \geq 96$ (RAM)', color='orange')
plt.plot(x, np.maximum(0, y3), label=r'$x_1 + x_2 \leq 12$ (Cota)', color='green')

# Região Viável (x2 >= y1, x2 >= y2, x2 <= y3)
y_min = np.maximum(y1, y2)
y_max = y3
plt.fill_between(x, y_min, y_max, where=(y_max >= y_min) & (x >= 0), color='gray', alpha=0.3, label='Região Viável')

# Ponto Ótimo
plt.scatter(8, 1, color='red', zorder=5, s=100, label='Ponto Ótimo (8, 1)')
plt.annotate('  Custo: $210', (8, 1), textcoords="offset points", xytext=(10,5), ha='left', fontsize=10)

plt.xlim(0, 15)
plt.ylim(0, 15)
plt.xlabel('Instâncias Standard ($x_1$)')
plt.ylabel('Instâncias High-Performance ($x_2$)')
plt.title('Ex 1: Otimização de Nuvem')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# =============================================================================
# EXERCÍCIO 2: Alocação de Banda (Maximização)
# =============================================================================
plt.figure(figsize=(8, 6))
x = np.linspace(0, 10, 400)

# Restrições
y1 = (24 - 2*x) / 4  # 2x1 + 4x2 <= 24
y2 = (22 - 3*x) / 2  # 3x1 + 2x2 <= 22

plt.plot(x, y1, label=r'$2x_1 + 4x_2 \leq 24$ (Switch A)', color='blue')
plt.plot(x, y2, label=r'$3x_1 + 2x_2 \leq 22$ (Switch B)', color='orange')

# Região Viável
y_max = np.minimum(y1, y2)
plt.fill_between(x, 0, y_max, where=(y_max >= 0) & (x >= 0), color='gray', alpha=0.3, label='Região Viável')

# Ponto Ótimo
plt.scatter(5, 3.5, color='red', zorder=5, s=100, label='Ponto Ótimo (5, 3.5)')
plt.annotate('  QoS: 32.5', (5, 3.5), textcoords="offset points", xytext=(10,5), ha='left', fontsize=10)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Stream Básico ($x_1$)')
plt.ylabel('Stream Premium ($x_2$)')
plt.title('Ex 2: Alocação de Banda')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# =============================================================================
# EXERCÍCIO 3: Modelos de Deep Learning (Maximização)
# =============================================================================
plt.figure(figsize=(8, 6))
x = np.linspace(0, 10, 400)

# Restrições
y1 = 18 - 3*x        # 3x1 + x2 <= 18
y2 = (16 - 1*x) / 2  # x1 + 2x2 <= 16

plt.plot(x, y1, label=r'$3x_1 + x_2 \leq 18$ (GPU)', color='blue')
plt.plot(x, y2, label=r'$x_1 + 2x_2 \leq 16$ (Armazenamento)', color='orange')

# Região Viável
y_max = np.minimum(y1, y2)
plt.fill_between(x, 0, y_max, where=(y_max >= 0) & (x >= 0), color='gray', alpha=0.3, label='Região Viável')

# Ponto Ótimo
plt.scatter(4, 6, color='red', zorder=5, s=100, label='Ponto Ótimo (4, 6)')
plt.annotate('  Impacto: 34', (4, 6), textcoords="offset points", xytext=(10,5), ha='left', fontsize=10)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Modelos NLP ($x_1$)')
plt.ylabel('Modelos de Visão ($x_2$)')
plt.title('Ex 3: Treinamento Deep Learning')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# =============================================================================
# EXERCÍCIO 4: Design de Hardware (Maximização)
# =============================================================================
plt.figure(figsize=(8, 6))
x = np.linspace(0, 10, 400)

# Restrições
y1 = (18 - 2*x) / 3  # 2x1 + 3x2 <= 18
y2 = 12 - 2*x        # 2x1 + x2 <= 12

plt.plot(x, y1, label=r'$2x_1 + 3x_2 \leq 18$ (Área)', color='blue')
plt.plot(x, y2, label=r'$2x_1 + x_2 \leq 12$ (Térmica)', color='orange')

# Região Viável
y_max = np.minimum(y1, y2)
plt.fill_between(x, 0, y_max, where=(y_max >= 0) & (x >= 0), color='gray', alpha=0.3, label='Região Viável')

# Ponto Ótimo
plt.scatter(4.5, 3, color='red', zorder=5, s=100, label='Ponto Ótimo (4.5, 3)')
plt.annotate('  Eficiência: 34.5', (4.5, 3), textcoords="offset points", xytext=(10,5), ha='left', fontsize=10)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Blocos de Cache ($x_1$)')
plt.ylabel('ALUs ($x_2$)')
plt.title('Ex 4: Design de Hardware')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# =============================================================================
# EXERCÍCIO 5: Planejamento de Sprints (Maximização)
# =============================================================================
plt.figure(figsize=(8, 6))
x = np.linspace(0, 10, 400)

# Restrições
y1 = (32 - 4*x) / 4  # 4x1 + 4x2 <= 32 (Simplifica para x1 + x2 <= 8)
y2 = 12 - 2*x        # 2x1 + x2 <= 12

plt.plot(x, y1, label=r'$4x_1 + 4x_2 \leq 32$ (Desenvolvimento)', color='blue')
plt.plot(x, y2, label=r'$2x_1 + x_2 \leq 12$ (Testes/QA)', color='orange')

# Região Viável
y_max = np.minimum(y1, y2)
plt.fill_between(x, 0, y_max, where=(y_max >= 0) & (x >= 0), color='gray', alpha=0.3, label='Região Viável')

# Ponto Ótimo
plt.scatter(4, 4, color='red', zorder=5, s=100, label='Ponto Ótimo (4, 4)')
plt.annotate('  Valor: 52', (4, 4), textcoords="offset points", xytext=(10,5), ha='left', fontsize=10)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel('Novas Funcionalidades ($x_1$)')
plt.ylabel('Refatoração ($x_2$)')
plt.title('Ex 5: Planejamento de Sprints')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()