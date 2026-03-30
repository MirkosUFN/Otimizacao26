from fractions import Fraction

def main():
    print("=== Gerador de Equação da Reta (y = ax + b) ===")
    
    while True:
        try:
            x1 = float(input("Digite o valor de x1 para o P1 (obrigatório ser 0): "))
            if x1 != 0:
                print("Erro: o x1 precisa ser 0. Tente novamente.\n")
                continue
                
            y1 = float(input("Digite o valor de y1 para o P1: "))
            break
        except ValueError:
            print("Erro: Digite apenas números.\n")

    print("-" * 30)

    while True:
        try:
            x2 = float(input("Digite o valor de x2 para o P2: "))
            if x2 == 0:
                print("Erro: Se x2 também for 0, não teremos uma inclinação válida.\n")
                continue
            break
        except ValueError:
            print("Erro: Digite apenas números.\n")

    while True:
        try:
            y2 = float(input("Digite o valor de y2 para o P2 (obrigatório ser 0): "))
            if y2 != 0:
                print("Erro: o y2 precisa ser 0. Tente novamente.\n")
                continue
            break
        except ValueError:
            print("Erro: Digite apenas números.\n")
            
    a_float = (y2 - y1) / (x2 - x1)

    a = Fraction(a_float).limit_denominator() 
    b = Fraction(y1).limit_denominator()
    
    sinal_b = "+" if b >= 0 else "-"
    
    print("\n" + "="*30)
    print("RESULTADO:")
    print(f"Pontos registrados: P1(0, {y1}) e P2({x2}, 0)")
    print(f"A equação reduzida da reta é: y = {a}x {sinal_b} {abs(b)}")
    print("="*30)

if __name__ == "__main__":
    main()