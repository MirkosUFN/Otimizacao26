def input_matrix():
  qtt = int(input("quantity of variables/expressions: "))
  matrix = []

  print(f"\ninput the {qtt} coefficients and the result for each row, separated by spaces.")
  print("example: for 2x + 3y = 10 -> 2 3 10")

  for i in range(qtt):
    row_input = input(f"equation {i+1}: ")
    row = [float(x) for x in row_input.split()]
    matrix.append(row)

  return matrix

def print_matrix(m):
  for line in m:
    variables = line[:-1]
    res = line[-1]
    vars_str = " ".join([f"{v:6.2f}" for v in variables])
    print(f"\t  [ {vars_str} | {res:6.2f} ]")

def equalize(m):
  tam = len(m)
  print("original matrix:")
  print_matrix(m)

  for i in range(tam):
    print(f"\ncolumn {i}")
    pivo = m[i][i]
    if pivo == 0:
      print(f"pivo [{i}][{i}] is zero")
      return None

    # 1. pivotamento:
    #   elemento da diagonal (pivo) deve ser 1
    #   ação: dividir toda linha pelo pivo
    print(f"\tturning pivo m[{i}][{i}] ({pivo:.2f}) into 1")
    for j in range(len(m[i])):
      print(f"\t{m[i][j]} = {m[i][j]} / {pivo}")
      m[i][j] = m[i][j] / pivo

    print_matrix(m)

    # 2. zerar outros elementos abaixo/acima do pivo
    #   ação: subtrai da linha atual a linha anterior/próxima multiplicada pelo fator
    print(f"\n\tturning all other elements into 0")
    for x in range(tam):
        if x != i:
          fator = m[x][i]
          if fator != 0:
            print(f"\tL{x} <- L{x} - ({fator:.2f} * L{i})")
            for y in range(len(m[x])):
              m[x][y] = m[x][y] - (fator * m[i][y])
          else:
            print(f"L{x} element is zero, skipping")

    print("\n\tcurrent matrix:")
    print_matrix(m)
    print(f"\n {"-" * 45}")

  print("\nfinished processing")
  return m

matrix = input_matrix()
res = equalize(matrix)
if res:
  print_matrix(res)


