import numpy as np
import matplotlib.pyplot as plt

def plotar_interseccao(inequacoes, limite_grafico=15):
    """
    Plota as retas em todos os quadrantes, mas destaca a intersecção 
    das inequações APENAS no primeiro quadrante.
    """
    # 1. Gerar malha de pontos para TODOS os quadrantes (de -limite a +limite)
    x = np.linspace(-limite_grafico, limite_grafico, 400)
    y = np.linspace(-limite_grafico, limite_grafico, 400)
    X, Y = np.meshgrid(x, y)
    
    # 2. Matriz booleana para armazenar a intersecção. 
    # Começa como True APENAS para o primeiro quadrante (X >= 0 e Y >= 0).
    regiao_interseccao = (X >= 0) & (Y >= 0)
    
    plt.figure(figsize=(10, 8))
    cores = ['blue', 'red', 'purple', 'orange', 'brown', 'cyan']

    # 3. Processar cada inequação
    for i, (a1, a2, sinal, vd) in enumerate(inequacoes):
        cor = cores[i % len(cores)]
        estilo_linha = '--' if sinal in ['>', '<'] else '-'
        label_eq = f'{a1:g}X + {a2:g}Y {sinal} {vd:g}'
        
        # Avaliar condição na malha de pontos
        if sinal == '<=':
            condicao = (a1 * X + a2 * Y <= vd)
        elif sinal == '<':
            condicao = (a1 * X + a2 * Y < vd)
        elif sinal == '>=':
            condicao = (a1 * X + a2 * Y >= vd)
        elif sinal == '>':
            condicao = (a1 * X + a2 * Y > vd)
            
        # Acumular a intersecção (AND lógico)
        regiao_interseccao = regiao_interseccao & condicao
        
        # Desenhar a linha base em todos os quadrantes para visualização
        if a2 != 0:
            # Isolando Y: Y = (vd - a1*X) / a2
            y_linha = (vd - a1 * x) / a2
            plt.plot(x, y_linha, color=cor, linestyle=estilo_linha, linewidth=2, label=label_eq)
        else:
            # Caso especial: reta vertical (a2 = 0)
            x_val = vd / a1
            plt.axvline(x=x_val, color=cor, linestyle=estilo_linha, linewidth=2, label=label_eq)

    # 4. Destacar (sombrear) a região de intersecção validada
    plt.contourf(X, Y, regiao_interseccao, levels=[0.5, 1.5], colors=['#90EE90'], alpha=0.6)

    # 5. Configurações visuais do gráfico (mostrando os 4 quadrantes)
    plt.axhline(0, color='black', linewidth=1.5) # Eixo X
    plt.axvline(0, color='black', linewidth=1.5) # Eixo Y
    plt.xlim(-limite_grafico, limite_grafico)
    plt.ylim(-limite_grafico, limite_grafico)
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Intersecção de Inequações (Restrita ao 1º Quadrante)')
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    
    # Adicionar legenda fora do gráfico para não sobrepor as linhas
    plt.legend(loc='upper right', bbox_to_anchor=(1.35, 1))
    plt.tight_layout()
    plt.show()

# --- Execução Principal ---
print("=== Solucionador de Sistemas de Inequações ===")
print("Formato das equações: a1*X + a2*Y SINAL valor_direito")
print("-" * 50)

lista_inequacoes = []

while True:
    try:
        n = int(input("Quantas inequações formam o sistema? (mínimo 2): "))
        if n >= 2:
            break
        print("Por favor, digite um número maior ou igual a 2.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

for i in range(n):
    print(f"\n--- Inserindo a {i+1}ª inequação ---")
    while True:
        try:
            a1 = float(input("Digite o valor de a1 (coeficiente de X): "))
            a2 = float(input("Digite o valor de a2 (coeficiente de Y): "))
            sinal = input("Digite o sinal (<, <=, >, >=): ").strip()
            
            if sinal not in ['<', '<=', '>', '>=']:
                print("Sinal inválido! Use apenas <, <=, > ou >=")
                continue
                
            vd = float(input("Digite o valor direito da inequação: "))
            
            lista_inequacoes.append((a1, a2, sinal, vd))
            break
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos para os coeficientes e valor direito.")

plotar_interseccao(lista_inequacoes)