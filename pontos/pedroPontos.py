import matplotlib.pyplot as plt
import random
 
pontos_x = []
pontos_y = []
 
i = 0
while i < 5:
    pontos_x.append(random.randint(-6 6))
    pontos_y.append(random.randint(-6, 6))
    i += 1
 
plt.scatter(pontos_x, pontos_y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlim(-7, 7)
plt.ylim(-7, 7)
plt.grid(True)
plt.title('5 Pontos')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()
 
