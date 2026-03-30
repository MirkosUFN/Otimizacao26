from fractions import Fraction

# Recebe as coordenadas dos dois pontos do usuário
x1 = Fraction(input("Digite x1: "))
y1 = Fraction(input("Digite y1: "))
x2 = Fraction(input("Digite x2: "))
y2 = Fraction(input("Digite y2: "))

# Verifica se a reta seria vertical ou horizontal
if x1 == x2:
    print("Erro: reta vertical não cruza o eixo y.")
elif y1 == y2:
    print("Erro: reta horizontal não cruza o eixo x.")
else:
    # Calcula o coeficiente angular (a)
    a = (y2 - y1) / (x2 - x1)
    
    # Calcula o coeficiente linear (b)
    b = y1 - a * x1
    
    # Calcula intercepto no eixo x
    x_intercept = -b / a
    
    # Função para imprimir frações de forma “bonitinha”
    def format_frac(f):
        if f.denominator == 1:
            return f"{f.numerator}"
        else:
            return f"{f}"
    
    # Monta a equação
    equacao = f"y = {format_frac(a)}x"
    if b > 0:
        equacao += f" + {format_frac(b)}"
    elif b < 0:
        equacao += f" - {format_frac(-b)}"
    # se b == 0, não adiciona nada
    
    # Exibe a equação da reta e os interceptos
    print(f"A equação da reta é: {equacao}")
    print(f"Intercepto no eixo y: (0, {format_frac(b)})")
    print(f"Intercepto no eixo x: ({format_frac(x_intercept)}, 0)")