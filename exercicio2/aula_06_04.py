import numpy as np
import matplotlib.pyplot as plt

n = 5
ang = np.linspace(0, 2*np.pi, n, endpoint=False)
x, y = np.cos(ang), np.sin(ang)

plt.figure(figsize=(6,6))

for i in range(n):
    j = (i + 2) % n
    plt.plot([x[i], x[j]], [y[i], y[j]])

plt.scatter(x, y)

plt.axis('equal')
plt.axis('off')
plt.show()