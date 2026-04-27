import matplotlib.pyplot as plt
import numpy as np

def resolver_sistema_inequacoes():
    print("--- Sistema de Inequações ---")
    
    # --- VERIFICAÇÃO DE ENTRADA ---
    while True:
        try:
            quantidade_inequacoes = int(input("Quantas inequações no sistema? "))
            if quantidade_inequacoes > 0:
                break
            print("Por favor, digite um número positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    # Configuração do plano
    limite_plano = 20
    eixo_x = np.linspace(-limite_plano, limite_plano, 1000)
    eixo_y = np.linspace(-limite_plano, limite_plano, 1000)
    grade_X, grade_Y = np.meshgrid(eixo_x, eixo_y)
    
    # Começa restrito ao primeiro quadrante
    regiao_intersecao = (grade_X >= 0) & (grade_Y >= 0)
    
    plt.figure(figsize=(10, 8))
    
    for indice in range(quantidade_inequacoes):
        print(f"\n--- Inequação {indice+1} ---")
        try:
            coef_x = float(input("Digite o coeficiente de X: "))
            coef_y = float(input("Digite o coeficiente de Y: "))
            operador = input("Sinal (<, <=, >, >=): ").strip()
            valor_direita = float(input("Digite o valor do lado direito: "))
            
            resultado_expressao = coef_x * grade_X + coef_y * grade_Y
            
            # Atualiza a região de interseção
            if operador == '<':
                regiao_intersecao &= (resultado_expressao < valor_direita)
            elif operador == '<=':
                regiao_intersecao &= (resultado_expressao <= valor_direita)
            elif operador == '>':
                regiao_intersecao &= (resultado_expressao > valor_direita)
            elif operador == '>=':
                regiao_intersecao &= (resultado_expressao >= valor_direita)
            
            # Desenha a linha
            if coef_y != 0:
                linha_fronteira = (valor_direita - coef_x * eixo_x) / coef_y
                estilo_linha = '--' if operador in ['<', '>'] else '-'
                plt.plot(eixo_x, linha_fronteira,
                         label=f'{coef_x}x + {coef_y}y {operador} {valor_direita}',
                         linestyle=estilo_linha)
            else:
                plt.axvline(valor_direita / coef_x,
                            label=f'{coef_x}x {operador} {valor_direita}',
                            linestyle='--' if operador in ['<', '>'] else '-')
                
        except (ValueError, ZeroDivisionError):
            print("Erro nos valores. Pulando esta inequação.")

    # Pinta a região
    plt.imshow(regiao_intersecao,
               extent=(eixo_x.min(), eixo_x.max(), eixo_y.min(), eixo_y.max()),
               origin='lower', cmap='YlGn', alpha=0.4, aspect='auto')

    # Eixos
    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    
    plt.xlim(-limite_plano, limite_plano)
    plt.ylim(-limite_plano, limite_plano)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title("Intersecção das Inequações")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    resolver_sistema_inequacoes()
