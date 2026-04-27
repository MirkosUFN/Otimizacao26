import numpy as np
import matplotlib.pyplot as plt

def exibirSistema(inequacoes):
    """Gera o gráfico com a interseção de múltiplas inequações no 1º quadrante."""
    if not inequacoes:
        print("Nenhuma inequação foi fornecida.")
        return

    limite_grafico = 20
    pontosX = np.linspace(0, limite_grafico, 400)
    
    y_min_val = np.zeros_like(pontosX)
    y_max_val = np.full_like(pontosX, limite_grafico)
    x_valido = np.ones_like(pontosX, dtype=bool)

    plt.figure(figsize=(10, 8))

    for a1, a2, sinal, b, texto_original in inequacoes:
        traco = '--' if sinal in ['>', '<'] else '-'
        
        if a2 != 0:
            pontosY = (b - a1 * pontosX) / a2
            plt.plot(pontosX, pontosY, linestyle=traco, linewidth=2, label=f'Fronteira: {texto_original}')
            
            if (sinal in ['<', '<='] and a2 > 0) or (sinal in ['>', '>='] and a2 < 0):
                y_max_val = np.minimum(y_max_val, pontosY)
            else:
                y_min_val = np.maximum(y_min_val, pontosY)
                
        else:
            if a1 == 0:
                continue
                
            x_linha = b / a1
            plt.axvline(x_linha, linestyle=traco, linewidth=2, label=f'Fronteira: {texto_original}')
            
            if (sinal in ['<', '<='] and a1 > 0) or (sinal in ['>', '>='] and a1 < 0):
                x_valido &= (pontosX <= x_linha)
            else:
                x_valido &= (pontosX >= x_linha)

    regiao_intersecao = (y_max_val >= y_min_val) & x_valido

    plt.fill_between(pontosX, y_min_val, y_max_val, where=regiao_intersecao, color='lightgreen', alpha=0.5, label='Região Válida (Interseção)')

    plt.axhline(0, color='black', linewidth=1.5)
    plt.axvline(0, color='black', linewidth=1.5)
    plt.xlim(0, limite_grafico)
    plt.ylim(0, limite_grafico)
    plt.xlabel('Valores de X')
    plt.ylabel('Valores de Y')
    plt.title('Solução de Sistema de Inequações (1º Quadrante)')
    plt.grid(color='gray', linestyle=':', linewidth=0.5)
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    
    plt.show()


lista_inequacoes = []

print("A estrutura da inequação é: (a1 * X) + (a2 * Y) [SINAL] valorDireito\n")

contador = 1
while True:
    print(f"\n--- Inserindo a {contador}ª inequação ---")
    try:
        a1 = float(input("1. Informe o coeficiente de X (a1): "))
        a2 = float(input("2. Informe o coeficiente de Y (a2): "))
        
        sinal = input("3. Informe o sinal (<, <=, >, >=): ").strip()
        if sinal not in ['<', '<=', '>', '>=']:
            print("Erro: Sinal inválido. Use apenas <, <=, >, ou >=")
            continue
            
        b = float(input("4. Informe o valor do lado direito da inequação: "))
        
        texto_legenda = f"{a1}X + {a2}Y {sinal} {b}"
        
        lista_inequacoes.append((a1, a2, sinal, b, texto_legenda))
        print(f"-> Inequação [ {texto_legenda} ] adicionada com sucesso!")
        
        while True:
            continuar = input("\nDeseja adicionar mais uma inequação? (S/N): ").strip().upper()
            if continuar in ['S', 'N']:
                break
            else:
                print("Por favor, digite apenas 'S' para Sim ou 'N' para Não.")
        
        if continuar == 'N':
            break
            
        contador += 1
        
    except ValueError:
        print("Erro: Você digitou um texto ou símbolo onde deveria ser um número. Tente novamente.")

print("\nGerando gráfico do sistema...")
exibirSistema(lista_inequacoes)