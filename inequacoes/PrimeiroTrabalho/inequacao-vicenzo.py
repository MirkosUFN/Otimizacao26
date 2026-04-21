import numpy as np
import matplotlib.pyplot as plt

def exibirDesigualdade(coefAngular, coefLinear, sinal):
    pontosX = np.linspace(-10, 10, 200)
    pontosY = coefAngular * pontosX + coefLinear

    plt.figure(figsize=(8, 6))

    traco = '--' if sinal in ['>', '<'] else '-'

    plt.plot(pontosX, pontosY, color='purple', linestyle=traco, linewidth=2, label=f'Fronteira: y = {coefAngular}x + {coefLinear}')

    if sinal in ['>', '>=']:
        plt.fill_between(pontosX, pontosY, 20, color='lightgreen', alpha=0.5, label=f'Região Válida: y {sinal} {coefAngular}x + {coefLinear}')
    elif sinal in ['<', '<=']:
        plt.fill_between(pontosX, pontosY, -20, color='salmon', alpha=0.5, label=f'Região Válida: y {sinal} {coefAngular}x + {coefLinear}')
    else:
        print("Sinal não reconhecido. Opções aceitas: '>', '>=', '<' ou '<='.")
        return

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(-10, 10)
    plt.ylim(-15, 15)
    plt.xlabel('Valores de X')
    plt.ylabel('Valores de Y')
    plt.title(f'Visualização Gráfica: y {sinal} {coefAngular}x + {coefLinear}')
    plt.grid(color='gray', linestyle=':', linewidth=0.5)
    plt.legend()
    
    plt.show()

try:
    inclinacao = float(input("Informe o coeficiente angular: "))
    intersecao = float(input("Informe o coeficiente linear: "))
    comparador = input("Informe o sinal matemático (>, >=, <, <=): ").strip()
    
    exibirDesigualdade(inclinacao, intersecao, comparador)
except ValueError:
    print("Aviso: É necessário fornecer valores numéricos para os coeficientes.")