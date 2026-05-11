import matplotlib.pyplot as plt

def plotar_pontos(pontos_x, pontos_y):
    plt.figure(figsize=(6, 6))
    
    plt.scatter(pontos_x, pontos_y, color='red', s=100, label='Pontos')
    
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title("Visualização de Coordenadas")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.legend()
    
    plt.show()

def main():
    x_coords = []
    y_coords = []
    
    print("--- Plotter de Pontos ---")
    print("Digite as coordenadas ou 'sair' para ver o gráfico.")
    
    while True:
        entrada = input("\nDigite o valor de X (ou 'sair'): ").strip().lower()
        if entrada == 'sair':
            break
            
        try:
            x = float(entrada)
            y = float(input("Digite o valor de Y: "))
            
            x_coords.append(x)
            y_coords.append(y)
        except ValueError:
            print("Ops! Digite apenas números válidos.")

    if x_coords:
        plotar_pontos(x_coords, y_coords)
    else:
        print("Nenhum ponto foi inserido.")

if __name__ == "__main__":
    main()
