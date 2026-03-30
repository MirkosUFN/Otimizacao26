print(f'Adicione os valores abaixo: ')
x1 = float(input('x1: '))
y1 = float(input('y1: '))
x2 = float(input('x2: '))
y2 = float(input('y2: '))

if x1 == x2:
    print(f'Reta vertical: x = {x1}')
else:
    a = (y2 - y1) / (x2 - x1) # Coefeciente Angular (a)
    b = y1 - a * x1 # Coefeciente Linear (b)
    
    sinal = (
        '+' if b >= 0 else '-'
    )

    print(f'Equação: y = {a}x {sinal} {b}')