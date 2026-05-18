import numpy as np
import matplotlib.pyplot as plt

def obter_inequacoes():
    inequacoes = []
    operadores_validos = ['<', '<=', '>', '>=']
    
    try:
        n = int(input("Quantas inequações você quer analisar? "))
        if n <= 0:
            raise ValueError("O número precisa ser maior que zero!")
        
        for i in range(n):
            print(f"\n--- Configurando a Inequação {i+1} ---")
            a1 = float(input("Digite o coeficiente de X (a1): "))
            a2 = float(input("Digite o coeficiente de Y (a2): "))
            operador = input("Escolha o operador (<, <=, >, >=): ").strip()
            if operador not in operadores_validos:
                raise ValueError(f"Operador inválido! Escolha apenas entre: {operadores_validos}")
            valor = float(input("Digite o termo independente (valor direito): "))
            
            inequacoes.append({
                'a1': a1,
                'a2': a2,
                'operador': operador,
                'valor': valor
            })
    except ValueError as e:
        print(f"Algo deu errado: {e}")
        return []
    
    return inequacoes

def plotar_sistema_inequacoes(inequacoes):
    if not inequacoes:
        print("Nenhuma inequação válida foi encontrada para gerar o gráfico.")
        return
    
    x_vals = np.linspace(0, 10, 200)
    y_vals = np.linspace(0, 10, 200)
    X, Y = np.meshgrid(x_vals, y_vals)
    
    mascara_solucao = np.ones_like(X, dtype=bool)
    linhas = []
    
    for idx, ineq in enumerate(inequacoes):
        a1, a2, op, val = ineq['a1'], ineq['a2'], ineq['operador'], ineq['valor']
        expr = a1 * X + a2 * Y
        
        if op == '<':
            mascara = expr < val
        elif op == '<=':
            mascara = expr <= val
        elif op == '>':
            mascara = expr > val
        elif op == '>=':
            mascara = expr >= val
        
        mascara_solucao = np.logical_and(mascara_solucao, mascara)
        
        if a2 != 0:
            y_line = (val - a1 * x_vals) / a2
            valid = (y_line >= 0) & (y_line <= 10)
            x_plot = x_vals[valid]
            y_plot = y_line[valid]
            label = f'{a1}X + {a2}Y {op} {val}'
        elif a1 != 0:
            x_line = val / a1
            if 0 <= x_line <= 10:
                y_plot = y_vals[(y_vals >= 0) & (y_vals <= 10)]
                x_plot = np.full_like(y_plot, x_line)
                label = f'{a1}X + {a2}Y {op} {val}'
            else:
                x_plot, y_plot = [], []
                label = f'{a1}X + {a2}Y {op} {val} (Fora do limite)'
        else:
            continue
        
        linhas.append((x_plot, y_plot, label, op))
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)
    ax.grid(True, linestyle='--', alpha=0.5)
    
    cores = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
    for idx, (x_plot, y_plot, label, op) in enumerate(linhas):
        if len(x_plot) > 0:
            estilo = '--' if op in ['<', '>'] else '-'
            cor = cores[idx % len(cores)]
            ax.plot(x_plot, y_plot, linestyle=estilo, color=cor, linewidth=2, label=label)
    
    if np.any(mascara_solucao):
        ax.contourf(X, Y, mascara_solucao, levels=[0.5, 1], colors=['lightblue'], alpha=0.4)
        ax.contour(X, Y, mascara_solucao, levels=[0.5], colors=['blue'], linewidths=1)
    
    ax.set_xlim(-3, 10)
    ax.set_ylim(-3, 10)
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    ax.set_title('Gráfico do Sistema de Inequações (Região Viável)', fontsize=14, fontweight='bold')
    ax.legend()
    
    plt.show()

if __name__ == "__main__":
    print("Inicializando o assistente de inequações lineares...")
    inequacoes = obter_inequacoes()
    plotar_sistema_inequacoes(inequacoes)
