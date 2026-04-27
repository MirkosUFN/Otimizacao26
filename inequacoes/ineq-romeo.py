import numpy as np
import matplotlib.pyplot as plt

def obter_inequacoes():
    """
    Solicita ao usuário as inequações na forma a1X + a2Y SINAL valorDireito.
    Retorna uma lista de dicionários com as inequações.
    """
    inequacoes = []
    operadores_validos = ['<', '<=', '>', '>=']
    
    try:
        n = int(input("Quantas inequações você deseja inserir? "))
        if n <= 0:
            raise ValueError("Número de inequações deve ser positivo.")
        
        for i in range(n):
            print(f"\nInequação {i+1}:")
            a1 = float(input("Coeficiente de X (a1): "))
            a2 = float(input("Coeficiente de Y (a2): "))
            operador = input("Operador (<, <=, >, >=): ").strip()
            if operador not in operadores_validos:
                raise ValueError(f"Operador inválido! Use um dos seguintes: {operadores_validos}")
            valor = float(input("Valor direito: "))
            
            inequacoes.append({
                'a1': a1,
                'a2': a2,
                'operador': operador,
                'valor': valor
            })
    except ValueError as e:
        print(f"Erro na entrada: {e}")
        return []
    
    return inequacoes

def plotar_sistema_inequacoes(inequacoes):
    """
    Plota o sistema de inequações no primeiro quadrante, destacando a intersecção das regiões de solução.
    
    Parâmetros:
    inequacoes (list): Lista de dicionários com as inequações.
    """
    if not inequacoes:
        print("Nenhuma inequação válida fornecida.")
        return
    
    # Definir o domínio no primeiro quadrante
    x_vals = np.linspace(0, 10, 200)
    y_vals = np.linspace(0, 10, 200)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    # Inicializar máscara de solução com True
    mascara_solucao = np.ones_like(X, dtype=bool)
    
    # Lista para armazenar as linhas das inequações
    linhas = []
    
    # Processar cada inequação
    for idx, ineq in enumerate(inequacoes):
        a1, a2, op, val = ineq['a1'], ineq['a2'], ineq['operador'], ineq['valor']
        
        # Calcular a expressão para cada ponto da grade
        expr = a1 * X + a2 * Y
        
        # Aplicar o operador para obter a máscara
        if op == '<':
            mascara = expr < val
        elif op == '<=':
            mascara = expr <= val
        elif op == '>':
            mascara = expr > val
        elif op == '>=':
            mascara = expr >= val
        
        # Intersecção com a máscara atual
        mascara_solucao = np.logical_and(mascara_solucao, mascara)
        
        # Preparar a linha da inequação para plotar
        # Resolver para y = (val - a1*x) / a2 se a2 != 0, senão para x
        if a2 != 0:
            # y = (val - a1*x) / a2
            y_line = (val - a1 * x_vals) / a2
            # Limitar ao primeiro quadrante
            valid = (y_line >= 0) & (y_line <= 10)
            x_plot = x_vals[valid]
            y_plot = y_line[valid]
            label = f'{a1}X + {a2}Y {op} {val}'
        elif a1 != 0:
            # x = val / a1 se a2 == 0
            x_line = val / a1
            if 0 <= x_line <= 10:
                y_plot = y_vals[(y_vals >= 0) & (y_vals <= 10)]
                x_plot = np.full_like(y_plot, x_line)
                label = f'{a1}X + {a2}Y {op} {val}'
            else:
                x_plot, y_plot = [], []
                label = f'{a1}X + {a2}Y {op} {val} (fora do domínio)'
        else:
            # Caso degenerado, ignorar
            continue
        
        linhas.append((x_plot, y_plot, label, op))
    
    # Inicializar o gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Desenhar os eixos
    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Plotar as linhas das inequações
    cores = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    for idx, (x_plot, y_plot, label, op) in enumerate(linhas):
        if len(x_plot) > 0:
            estilo = '--' if op in ['<', '>'] else '-'
            cor = cores[idx % len(cores)]
            ax.plot(x_plot, y_plot, linestyle=estilo, color=cor, linewidth=2, label=label)
    
    # Preencher a região de intersecção
    if np.any(mascara_solucao):
        ax.contourf(X, Y, mascara_solucao, levels=[0.5, 1], colors=['lightblue'], alpha=0.4)
        ax.contour(X, Y, mascara_solucao, levels=[0.5], colors=['blue'], linewidths=1)
    
    # Ajustes finais
    ax.set_xlim(-3, 10)
    ax.set_ylim(-3, 10)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Sistema de Inequações - Região de Solução (Primeiro Quadrante)', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.show()

# Programa principal
if __name__ == "__main__":
    inequacoes = obter_inequacoes()
    plotar_sistema_inequacoes(inequacoes)
