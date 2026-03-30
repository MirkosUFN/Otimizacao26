import matplotlib.pyplot as plt

def main():
    print("=== Gerador de Gráfico de Pontos ===")
    print("Digite 'sair' a qualquer momento no eixo X para finalizar e ver o gráfico.\n")
    
    x_coords = []
    y_coords = []
    
    while True:
        entrada_x = input("Digite a coordenada X (ou 'sair' para terminar): ")
        
        if entrada_x.lower() == 'sair':
            break
            
        entrada_y = input("Digite a coordenada Y: ")
        
        try:
            x = float(entrada_x)
            y = float(entrada_y)
            
            x_coords.append(x)
            y_coords.append(y)
            print(f"Ponto ({x}, {y}) adicionado com sucesso!\n")
            
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.\n")

    if len(x_coords) > 0:
        print("\nGerando o gráfico...")
        plt.figure(figsize=(8, 6))
        plt.scatter(x_coords, y_coords, color='red', s=100, zorder=5)
        
        for i in range(len(x_coords)):
            plt.text(x_coords[i] + 0.1, y_coords[i] + 0.1, f'({x_coords[i]}, {y_coords[i]})', fontsize=9)

        plt.title('Meus Pontos Traçados', fontsize=14)
        plt.xlabel('Eixo X', fontsize=12)
        plt.ylabel('Eixo Y', fontsize=12)
        
        plt.axhline(0, color='black', linewidth=1)
        plt.axvline(0, color='black', linewidth=1)
        
        plt.grid(True, linestyle='--', alpha=0.7) 
        
        plt.show()
    else:
        print("\nNenhum ponto foi inserido. O programa foi encerrado.")

# Executa o programa
if __name__ == "__main__":
    main()