def calcular_equacao_reta():
    print("--- Gerador de Equação da Reta (y = ax + b) ---")
    
    try:
        x1 = float(input("P1 - Digite x1: "))
        y1 = float(input("P1 - Digite y1: "))
        x2 = float(input("P2 - Digite x2: "))
        y2 = float(input("P2 - Digite y2: "))
      
        if x1 == x2:
            print(f"\nA reta é vertical: x = {x1}")
            print("Não pode ser escrita na forma y = ax + b (a é infinito).")
        else:
            a = (y2 - y1) / (x2 - x1)
            b = y1 - a * x1
            
            sinal = "+" if b >= 0 else "-"
            print(f"\nEquação calculada:")
            print(f"y = {a:.2f}x {sinal} {abs(b):.2f}")
            
    except ValueError:
        print("Erro: Por favor, digite apenas números.")

if __name__ == "__main__":
    calcular_equacao_reta()
