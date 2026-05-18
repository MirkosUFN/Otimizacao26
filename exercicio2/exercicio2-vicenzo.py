def calcular_equacao_reta():
    print("--- Calculadora de Equação da Reta (y = ax + b) ---")
    print("\nInsira as coordenadas do Ponto 1:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    print("\nInsira as coordenadas do Ponto 2:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    
    if x1 == x2:
        print(f"\nOs pontos formam uma reta vertical.")
        print(f"A equação da reta é: x = {x1}")
        return

    a = (y2 - y1) / (x2 - x1)
    
    b = y1 - (a * x1)
    
    sinal_b = "+" if b >= 0 else "-"
    
    print(f"\nA equação da reta é: y = {a:.2f}x {sinal_b} {abs(b):.2f}")

if __name__ == "__main__":
    calcular_equacao_reta()