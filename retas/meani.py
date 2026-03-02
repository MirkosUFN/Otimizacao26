import matplotlib.pyplot as plt

def calculate(a, b, x0, x1):
  # a: inclinação da reta
  # b: onde corta o eixo y
  result = []

  for x in range(x0, x1 + 1): # segundo parametro soma +1 para alcançar
    result.append((a * x) + b)

  return result

# plotar duas retas e informar em qual situação elas se encontram:
# paralelas > a0 = a1
# se cortam em 2 pontos (iguais) > a0 = a1 && b0 = b1
# se cortam em 1 ponto > a0 != a1

# mostrar o ponto de interseção se elas se encontram
  # igualando as duas equações
  # a0​x + b0 ​= a1​x + b1​
  # e então isolando o x
  # x(a0 ​− a1​) = b1 ​− b0​ > x= b1 - b0 / a0 - a1

def plot(x0, x1, list):
  y0 = list[0]
  y1 = list[len(list) - 1]
  plt.plot((x0, x1), [y0, y1])
  plt.show

def check(a0, b0, a1, b1):
  intersection = None
  if a0 == a1:
    if b0 == b1:
      scenario = 'retas iguais'
    else:
      scenario = 'retas paralelas'
  else:
    scenario = 'retas se cruzam em um ponto'
    ix = (b1 - b0) / (a0 - a1)
    iy = a0 * ix + b0
    intersection = (ix, iy)

  return scenario, intersection

a0 = 6
b0 = -10
x0 = -2
x1 = 5
r0 = calculate(a0, b0, x0, x1)
print(r0)

a1 = 7
b1 = -11

r1 = calculate(a1, b1, x0, x1)
print(r1)

plot(a0, b0, r0)
plot(a1, b1, r1)

scenario, intersection = check(a0, b0, a1, b1)

print((scenario, intersection) if intersection != None else scenario)