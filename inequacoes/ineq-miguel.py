import matplotlib.pyplot as plt
import numpy as np

def resolver_sistema_inequacoes():
    print("--- Sistema de Inequações ---")
    
    # --- VERIFICAÇÃO DE ENTRADA ---
    while True:
        try:
            n = int(input("Quantas inequações compõem o sistema? "))
            if n > 0:
                break
            print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Configuração do plano (Visão de todos os quadrantes)
    limite = 20
    x = np.linspace(-limite, limite, 1000)
    y = np.linspace(-limite, limite, 1000)
    X, Y = np.meshgrid(x, y)
    
    # CRUCIAL: A área de pintura começa restrita ao primeiro quadrante
    interseccao = (X >= 0) & (Y >= 0)
    
    plt.figure(figsize=(10, 8))
    
    for i in range(n):
        print(f"\n--- Inequação {i+1} ---")
        try:
            a1 = float(input("Digite o coeficiente a1 (de X): "))
            a2 = float(input("Digite o coeficiente a2 (de Y): "))
            sinal = input("Sinal (<, <=, >, >=): ").strip()
            v_dir = float(input("Digite o valorDireito: "))
            
            expressao = a1 * X + a2 * Y
            
            # Atualiza a máscara (interseccionando com o que já existe)
            if sinal == '<': interseccao &= (expressao < v_dir)
            elif sinal == '<=': interseccao &= (expressao <= v_dir)
            elif sinal == '>': interseccao &= (expressao > v_dir)
            elif sinal == '>=': interseccao &= (expressao >= v_dir)
            
            # Desenha a linha da fronteira em todo o plano
            if a2 != 0:
                y_fronteira = (v_dir - a1 * x) / a2
                estilo = '--' if sinal in ['<', '>'] else '-'
                plt.plot(x, y_fronteira, label=f'{a1}x + {a2}y {sinal} {v_dir}', linestyle=estilo)
            else:
                plt.axvline(v_dir/a1, label=f'{a1}x {sinal} {v_dir}', linestyle='--' if sinal in ['<', '>'] else '-')
                
        except (ValueError, ZeroDivisionError):
            print("Erro nos valores. Pulando esta inequação.")

    # Pintar a área resultante (imshow mostrará apenas onde 'interseccao' é True)
    plt.imshow(interseccao, extent=(x.min(), x.max(), y.min(), y.max()), 
               origin='lower', cmap='YlGn', alpha=0.4, aspect='auto')

    # Configuração visual dos eixos
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    
    plt.xlim(-limite, limite)
    plt.ylim(-limite, limite)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title("Intersecção das Inequações")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    resolver_sistema_inequacoes()