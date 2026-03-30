from fractions import Fraction

def formatar_fracao(f):
    # Se o denominador for 1, retorna apenas o número inteiro
    if f.denominator == 1:
        return f"{f.numerator}"
    return f"{f}"

pt1_x = Fraction(input("Digite a coordenada X do ponto 1: "))
pt1_y = Fraction(input("Digite a coordenada Y do ponto 1: "))
pt2_x = Fraction(input("Digite a coordenada X do ponto 2: "))
pt2_y = Fraction(input("Digite a coordenada Y do ponto 2: "))

# Verificação de retas verticais ou horizontais
if pt1_x == pt2_x:
    print("Erro: Reta vertical, não cruza o eixo X.")
elif pt1_y == pt2_y:
    print("Erro: Reta horizontal, não cruza o eixo Y.")
else:
    # Coeficiente angular (a): representa a inclinação da reta
    coef_a = (pt2_y - pt1_y) / (pt2_x - pt1_x)
    
    #  Coeficiente linear (b): ponto onde a reta cruza o eixo Y Fórmula: y = ax + b  →  b = y - ax
    coef_b = pt1_y - coef_a * pt1_x
    
    # Para encontrar onde a reta cruza o eixo X, fazemos y = 0: 0 = ax + b → x = -b / a
    raiz_x = -coef_b / coef_a
    
    # Tratamento especial para deixar a equação mais bonita
    if coef_a == 1:
        equacao_reta = "y = x"
    elif coef_a == -1:
        equacao_reta = "y = -x"
    else:
        equacao_reta = f"y = {formatar_fracao(coef_a)}x"
    
    if coef_a == 1:
        equacao_reta = "y = x"
    elif coef_a == -1:
        equacao_reta = "y = -x"
    else:
        equacao_reta = f"y = {formatar_fracao(coef_a)}x"
        
    print(f"\nA equação da reta é: {equacao_reta}")
    print(f"Intercepto no eixo Y: (0, {formatar_fracao(coef_b)})")
    print(f"Intercepto no eixo X: ({formatar_fracao(raiz_x)}, 0)")


