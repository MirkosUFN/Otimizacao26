import matplotlib.pyplot as plt

def grafico(a,b,xF,yF):
    result = []
    for x in range(xF,yF+1):
        result.append(a*x+b)
    return result

def comparar(a1,b1,a2,b2):
    if a1 == a2:
        if b1 == b2:
            print('As retas são sobrepostas!')
            return None
        else:
            print('As retas são paralelas!')
            return None
    else:
        x = (b2 - b1)/(a1 - a2)
        y = a1 * x + b1
        print(f'Elas se encontram no ponto ({x}, {y})')
        return x, y

def plano(x0,x1,lista,lista1,ponto=None):
    y0 = lista[0]
    y1 = lista[-1]
    y2 = lista1[0]
    y3 = lista1[-1]

    plt.plot([x0,x1],[y0,y1], label='Reta 1')
    plt.plot([x0,x1],[y2,y3], label='Reta 2')

    plt.plot(ponto[0], ponto[1], color='red', marker='o', label='Interseção')

    plt.axhline(0,color='pink', linewidth = 2)
    plt.axvline(0,color='pink', linewidth = 2)
    plt.legend()
    plt.show()

x0, x1 = -2, 5
r = grafico(5,-11,x0,x1)

x2, x3 = -2, 7
r1 = grafico(5,-19,x2,x3)

ponto = comparar(2,-1,-1,5)

plano(x0,x1,r,r1,ponto)
