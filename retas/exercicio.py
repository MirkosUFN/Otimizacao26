import numpy as np
import matplotlib.pyplot as plt
#y=ax+b -> codigo

def funcao(a, b, x0, x1): 
  result = []
  for x in range(x0, x1):
    result.append(a*x + b)
  return result

a = 5
b = -11
#Intervalo de x
x0 = -2
x1 = 5


print(funcao(a, b, x0, x1))

#Desenhar a reta
plt.plot(funcao(a, b, x0, x1))
plt.show()