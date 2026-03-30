import matplotlib.pyplot as plt

def main():

    print("--- Desenhador de Traçado de Pontos ---")
    print("Você precisará informar as coordenadas X e Y de 6 pontos.")

    pontos_x = []
    pontos_y = []
    
    for i in range(1, 7):
        print(f"\n--- Ponto {i} ---")
        
        while True:
            try:
                x = float(input("Digite a coordenada X: "))
                y = float(input("Digite a coordenada Y: "))
                pontos_x.append(x)
                pontos_y.append(y)
                
                break 

            except ValueError:
                print("Valor inválido! Por favor, digite apenas números.")
    
    plt.figure(figsize=(8, 6))
    
    plt.plot(pontos_x, pontos_y, marker='o', linestyle='-', color='dodgerblue', linewidth=2, markersize=8)
    
    # Zip(...) une as listas num único objeto para andarmos pelas duas ao mesmo tempo. Enumerate(...) me dá o índice além do valor.
    # Basicamente, é para passarmos sobre cada ponto armazenado e anotarmos perto dele quem ele é.
    for i, (x, y) in enumerate(zip(pontos_x, pontos_y)):
         plt.text(x, y, f' P{i+1} ({x:g}, {y:g})', fontsize=10, verticalalignment='bottom', horizontalalignment='left')


    # Abaixo começo a mexer na "área interna" do gráfico, tecnicamente chamada de Axes.
    # plt.gca() (Get Current Axes) obtém a nossa área de desenho atual para podermos configurar ela.
    ax = plt.gca()
    
    # ax.spines são as 4 bordas (linhas ou "espinhas") que circundam o gráfico originalmente (top, right, left, bottom).
    # Aqui eu mando as bordas de cima e da direita esconderem as próprias linhas passando a cor 'none' (nenhuma).
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    
    # set_position('zero') move as linhas da esquerda e de baixo (os nossos eixos Y e X) 
    # exatamente para a marcação do "zero" da régua matemática. É isso que cria a cruz do Plano Cartesiano!!
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    
    # Estas quatro linhas seguintes garantem o "nível de zoom".
    # get_xlim e get_ylim pegam o tamanho mínimo e máximo do zoom atual que estava sendo calculado usando nossos pontos digitados.
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Usamos set_xlim e set_ylim para dar uma ajeitada pequena: Se os pontos estiverem só do lado positivo (tipo x=10, y=10),
    # o código poderia deixar de fora a parte negativa e aí a cruz do meio não apareceria.
    # Portanto, dizemos para o Zoom mínimo começar no máximo de -1 e o máximo encerrar no mínimo de 1.
    ax.set_xlim(min(xlim[0], -1), max(xlim[1], 1))
    ax.set_ylim(min(ylim[0], -1), max(ylim[1], 1))


    plt.title("Traçado dos 6 Pontos no Plano Cartesiano", fontsize=14, fontweight='bold', pad=20)
    
    plt.grid(True, linestyle='--', alpha=0.6)
    
    print("\nAbrindo a janela com o traçado na tela...")
    plt.show()

if __name__ == "__main__":
    main()
