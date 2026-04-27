"""
=== OBJETIVO DO CÓDIGO ===

Construir um algoritmo que trace a região de solução de um sistema de inequações
lineares, restringindo a visualização ao PRIMEIRO QUADRANTE (x >= 0 e y >= 0).

O software solicita inequações no formato: a1*X + a2*Y [SINAL] valorDireito.
A região destacada no gráfico representa a intersecção de todas as áreas das 
inequações fornecidas, respeitando inclusive restrições verticais.

=== EXEMPLO DE USO ===

Para o sistema:
1) 1x + 1y <= 12
2) 1x + 0y <= 5
O algoritmo desenhará a reta diagonal e a reta vertical, sombreando apenas
a área comum a ambas dentro do primeiro quadrante.
"""

import matplotlib.pyplot as plt
import numpy as np


def plotar_sistema_inequacoes_1q(inequacoes: list) -> None:
    """
    Desenha as retas e a área de intersecção resultante no 1º Quadrante.
    
    Parâmetros:
      inequacoes (list): Lista de tuplas contendo (a1, a2, operador, valor_direito).
    """
    plt.figure(figsize=(10, 7))
    
    # Configurações Iniciais e Restrições do 1º Quadrante
    x_min, x_max = 0.0, 1e10  # x_max -> 1e10 Significa 1 x 10^10 (10 Bilhões), inicia para ser reduzido por restrições
    intercepts_x = [10.0]     
    intercepts_y = [10.0]
    
    # Identificar limites de X (retas verticais) e coletar interceptos para escala
    for a1, a2, op, vd in inequacoes:
        if a1 != 0:
            ponto_x = vd / a1
            intercepts_x.append(abs(ponto_x))
            if a2 == 0:  # Restrição puramente vertical (a1*X [SINAL] vd)
                if (a1 > 0 and '<' in op) or (a1 < 0 and '>' in op):
                    x_max = min(x_max, ponto_x)
                else:
                    x_min = max(x_min, ponto_x)
        if a2 != 0:
            intercepts_y.append(abs(vd / a2))

    # Verifica se o domínio de X é impossível
    if x_min > x_max:
        print("\n[ERRO] O sistema não possui solução viável (conflito de limites em X).")
        return

    # Define o limite do gráfico baseado nos interceptos encontrados
    limite_visual_x = max(intercepts_x) * 1.2
    valores_x = np.linspace(0, limite_visual_x, 1000)
    
    # Inicializa os limites de Y para o sombreamento
    limite_inferior_y = np.zeros_like(valores_x)
    limite_superior_y = np.full_like(valores_x, max(intercepts_y) * 2.0)

    # Processamento das inequações e plotagem das linhas
    for a1, a2, op, vd in inequacoes:
        estilo_linha = '-' if '=' in op else '--'
        rotulo = f'{a1}x + {a2}y {op} {vd}'
        
        if a2 != 0:
            # Reta inclinada ou horizontal
            valores_y_reta = (-a1 * valores_x + vd) / a2
            plt.plot(valores_x, valores_y_reta, linestyle=estilo_linha, linewidth=2, label=rotulo)
            
            # Determina se a reta limita a área por cima ou por baixo
            e_limite_inferior = (a2 > 0 and '>' in op) or (a2 < 0 and '<' in op)
            
            if e_limite_inferior:
                limite_inferior_y = np.maximum(limite_inferior_y, valores_y_reta)
            else:
                limite_superior_y = np.minimum(limite_superior_y, valores_y_reta)
        else:
            # Reta vertical (a2 = 0)
            plt.axvline(x=vd/a1, linestyle=estilo_linha, color='gray', alpha=0.7, label=rotulo)

    # Preenchimento da área de intersecção
    plt.fill_between(
        valores_x, 
        limite_inferior_y, 
        limite_superior_y, 
        where=(limite_superior_y >= limite_inferior_y) & (valores_x <= x_max) & (valores_x >= x_min),
        color='skyblue', 
        alpha=0.4, 
        label='Área de Intersecção'
    )

    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    
    plt.xlim(-5, limite_visual_x)
    plt.ylim(-5, max(intercepts_y) * 1.2)
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title('Solução do Sistema de Inequações no 1º Quadrante')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    
    plt.show()


if __name__ == '__main__':
    print("--- Gerador de Região de Solução (Sistemas Lineares) ---")
    print("Formato: a1*X + a2*Y [SINAL] valorDireito\n")
    
    sistema = []
    
    while True:
        try:
            print(f"Inequação #{len(sistema) + 1}:")
            val_a1 = float(input("  Coeficiente a1 (X): "))
            val_a2 = float(input("  Coeficiente a2 (Y): "))
            sinal = input("  Sinal (>, >=, <, <=): ").strip()
            val_vd = float(input("  Valor à direita: "))
            
            if sinal not in ['>', '>=', '<', '<=']:
                print("[!] Sinal inválido. Use apenas >, >=, < ou <=.\n")
                continue
                
            sistema.append((val_a1, val_a2, sinal, val_vd))
            
            cont = input("\nDeseja adicionar outra inequação? (s/n): ").lower()
            if cont != 's':
                break
            print("-" * 30)
            
        except ValueError:
            print("[!] Erro: Digite apenas valores numéricos.\n")

    if sistema:
        plotar_sistema_inequacoes_1q(sistema)
    else:
        print("Nenhuma inequação foi inserida.")