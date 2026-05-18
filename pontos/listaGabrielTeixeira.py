import matplotlib.pyplot as plt

def plotar_pontos():
    print("=== PLOTADOR DE PONTOS CARTESIANOS ===")
    print("Digite as coordenadas. Digite 's' na coordenada X para sair e gerar o gráfico.\n")
    
    coordenadas_x = []
    coordenadas_y = []
    
    # Loop para receber vários pontos
    contador = 1
    while True:
        entrada_x = input(f"Ponto {contador} - Digite o valor de X (ou 's' para sair): ")
        
        if entrada_x.lower() == 's':
            break
            
        try:
            x = float(entrada_x)
            y = float(input(f"Ponto {contador} - Digite o valor de Y: "))
            
            coordenadas_x.append(x)
            coordenadas_y.append(y)
            print(f"-> Ponto ({x}, {y}) salvo com sucesso!\n")
            contador += 1
            
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.\n")

    # Verifica se algum ponto foi inserido antes de tentar plotar
    if not coordenadas_x:
        print("\nNenhum ponto foi inserido. O gráfico não será gerado.")
        return

    print("\nGerando gráfico...")

    # Configurações do Gráfico
    plt.figure(figsize=(8, 8))
    
    # Plota os pontos
    plt.scatter(coordenadas_x, coordenadas_y, color='red', s=100, zorder=5, label='Pontos inseridos')

    # Adiciona a anotação (texto) ao lado de cada ponto
    for i in range(len(coordenadas_x)):
        texto = f" P{i+1} ({coordenadas_x[i]:.1f}, {coordenadas_y[i]:.1f})"
        plt.annotate(texto, (coordenadas_x[i], coordenadas_y[i]), textcoords="offset points", xytext=(8,5), ha='left')

    # Desenha os eixos X e Y principais passando pela origem (0,0)
    plt.axhline(y=0, color='black', linewidth=1.5, zorder=4)
    plt.axvline(x=0, color='black', linewidth=1.5, zorder=4)

    # Formatação visual
    plt.grid(True, linestyle='--', alpha=0.6, zorder=0)
    plt.title('Representação Gráfica de Coordenadas')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.legend()
    
    # Garante que os eixos tenham a mesma escala para não distorcer a visualização
    plt.axis('equal') 

    # Exibe o gráfico
    plt.show()

# Executa o programa
if __name__ == "__main__":
    plotar_pontos()