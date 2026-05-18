from fractions import Fraction

def formatar_fracao(f):
    if f.denominator == 1:
        return f"{f.numerator}"
    return f"{f}"

pt1_x = Fraction(input("Digite a coordenada X do ponto 1: "))
pt1_y = Fraction(input("Digite a coordenada Y do ponto 1: "))
pt2_x = Fraction(input("Digite a coordenada X do ponto 2: "))
pt2_y = Fraction(input("Digite a coordenada Y do ponto 2: "))

if pt1_x == pt2_x:
    print("Aviso: A reta é vertical (não possui intercepto no eixo Y).")
elif pt1_y == pt2_y:
    print("Aviso: A reta é horizontal (não possui intercepto no eixo X).")
else:
    coef_a = (pt2_y - pt1_y) / (pt2_x - pt1_x)
    coef_b = pt1_y - coef_a * pt1_x
    raiz_x = -coef_b / coef_a
    
    if coef_a == 1:
        str_a = ""
    elif coef_a == -1:
        str_a = "-"
    else:
        str_a = formatar_fracao(coef_a)
        
    if coef_b > 0:
        str_b = f" + {formatar_fracao(coef_b)}"
    elif coef_b < 0:
        str_b = f" - {formatar_fracao(abs(coef_b))}"
    else:
        str_b = ""

    print("\n--- RESULTADOS ---")
    print(f"Equação reduzida: y = {str_a}x{str_b}")
    print(f"Ponto de corte em Y: (0, {formatar_fracao(coef_b)})")
    print(f"Ponto de corte em X: ({formatar_fracao(raiz_x)}, 0)")
