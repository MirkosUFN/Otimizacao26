#IMPLEMENTAÇÃO
#Os sistemas inicialmente serão na forma de duas
#equações com duas variáveis, consequentemente:

#EOO E01 E02
#E10   E11 E22

#E = ELEMENTO (coeficiente)

#Exemplo:
#x + y = 12
#3x -y = 20

matriz = [[1,-2,4],[3,1,2]]


def checa_diagonal_eh_1():
    for i in range(len(matriz)):
        if matriz[i][i] != 1:
            return False
    return True


def transformar_linha_em_1(i):
    pivo = matriz[i][i]
    if pivo != 1:
        for j in range(len(matriz[i])):
            matriz[i][j] /= pivo

def eliminar_coluna(i):
    n = len(matriz)
    for k in range(n):
        if k != i:
            fator = matriz[k][i]
            for j in range(len(matriz[k])):
                matriz[k][j] -= fator * matriz[i][j]

def calcular_resultado():
  # algo deu errado
  if not checa_diagonal_eh_1():
    print("algo deu errado, a diagonal não é 1")
  
  x = matriz[0][2]
  y = matriz[1][2]
  return [x, y]


print('Matriz original:', matriz)

for i in range(len(matriz)):
    transformar_linha_em_1(i)  # normaliza só a linha i
    eliminar_coluna(i)         # depois zera a coluna i nas outras linhas

print('Matriz escalonada:', matriz)
print('Resultado [x, y]:', calcular_resultado())
