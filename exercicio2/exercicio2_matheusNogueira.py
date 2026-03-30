from fractions import Fraction

def formatar_fracao(f):
    # Se o denominador for 1, oculta ele para exibir como um número inteiro na tela
    if f.denominator == 1:
        return f"{f.numerator}"
    return f"{f}"

# Leitura das coordenadas dos dois pontos
pt1_x = Fraction(input("Digite a coordenada X do ponto 1: "))
pt1_y = Fraction(input("Digite a coordenada Y do ponto 1: "))
pt2_x = Fraction(input("Digite a coordenada X do ponto 2: "))
pt2_y = Fraction(input("Digite a coordenada Y do ponto 2: "))

# Verificação de retas verticais ou horizontais
if pt1_x == pt2_x:
    print("Erro: Reta vertical, não cruza o eixo Y.")
elif pt1_y == pt2_y:
    print("Erro: Reta horizontal, não cruza o eixo X.")
else:
    # Cálculo do coeficiente angular (a) da reta
    coef_a = (pt2_y - pt1_y) / (pt2_x - pt1_x)
    
    # Cálculo do coeficiente linear (b) usando a fórmula: y = ax + b -> b = y - ax
    coef_b = pt1_y - coef_a * pt1_x
    
    # Cálculo da raiz predefinida (intercepto do eixo X: ax + b = 0)
    raiz_x = -coef_b / coef_a
    
    # Formatação visual da string da equação da reta
    equacao_reta = f"y = {formatar_fracao(coef_a)}x"
    
    if coef_b > 0:
        equacao_reta += f" + {formatar_fracao(coef_b)}"
    elif coef_b < 0:
        equacao_reta += f" - {formatar_fracao(-coef_b)}"
        
    # Exibição dos resultados finais
    print(f"\nA equação da reta é: {equacao_reta}")
    print(f"Intercepto no eixo Y: (0, {formatar_fracao(coef_b)})")
    print(f"Intercepto no eixo X: ({formatar_fracao(raiz_x)}, 0)")
