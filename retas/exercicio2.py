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
x0 = -10
x1 = 10

a1 = -5
b1 = 10
x01 = -10
x11 = 10

resultado = funcao(a, b, x0, x1)
resultado1 = funcao(a1, b1, x01, x11)

#verificar se as retas sao paralelas
if a == a1: 
  if b == b1:
    print("As retas sao identicas")
  else: 
    print("As retas sao paralelas")
else:
  print("As retas se interceptam")

plt.title("Exercicio 2")
plt.plot(resultado)
plt.plot(resultado1)
plt.show()