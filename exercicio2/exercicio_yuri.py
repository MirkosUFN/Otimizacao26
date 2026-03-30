from fractions import Fraction

print(f'Adicione os valores abaixo: ')
x1 = Fraction(input('x1: '))
y1 = Fraction(input('y1: '))
x2 = Fraction(input('x2: '))
y2 = Fraction(input('y2: '))

if x1 == x2:
    print(f'Reta vertical: x = {x1}')
else:
    a = (y2 - y1) / (x2 - x1) # Coefeciente Angular (a)
    b = y1 - a * x1 # Coefeciente Linear (b)

    print(f'Equação: y = {a}x {"+" if b >= 0 else ""} {b}')
    