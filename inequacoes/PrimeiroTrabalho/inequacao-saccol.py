import numpy as np
import matplotlib.pyplot as plt

def plot_sistema_inequacoes(inequalities):
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(8, 8))

    # Define the grid for plotting, initially covering a broader range
    # The actual plotting will be restricted to the first quadrant (X>=0, Y>=0)
    x_range = np.linspace(0, 10, 400) # Assuming a typical range for visualization
    y_range = np.linspace(0, 10, 400)
    X, Y = np.meshgrid(x_range, y_range)

    # Initialize the solution region mask for the first quadrant
    solution_mask = (X >= 0) & (Y >= 0)

    line_labels = []

    for i, ineq in enumerate(inequalities):
        coeficiente_x = ineq['coeficiente_x']
        coeficiente_y = ineq['coeficiente_y']
        simbolo = ineq['simbolo']
        valor_direito = ineq['valor_direito']

        # Determine the mask for the current inequality
        current_ineq_mask = np.zeros(X.shape, dtype=bool)
        if simbolo == '<':
            current_ineq_mask = (coeficiente_x * X + coeficiente_y * Y < valor_direito)
        elif simbolo == '<=':
            current_ineq_mask = (coeficiente_x * X + coeficiente_y * Y <= valor_direito)
        elif simbolo == '>':
            current_ineq_mask = (coeficiente_x * X + coeficiente_y * Y > valor_direito)
        elif simbolo == '>=':
            current_ineq_mask = (coeficiente_x * X + coeficiente_y * Y >= valor_direito)

        # Combine with the overall solution mask
        solution_mask &= current_ineq_mask

        # Plot boundary line for the current inequality
        estilo = '--' if simbolo in ['<', '>'] else '-'
        # Cycle through colors for better distinction of lines
        color = plt.cm.get_cmap('Dark2')(i % plt.cm.get_cmap('Dark2').N)

        # Add a small epsilon to avoid division by zero when coeficiente_y is very close to zero
        epsilon = 1e-9

        if abs(coeficiente_y) > epsilon: # Not a vertical line
            # Equation for y: y = (valor_direito - coeficiente_x*x) / coeficiente_y
            y_line = (valor_direito - coeficiente_x * x_range) / coeficiente_y
            # Filter y_line to keep it within the plotting bounds for cosmetic reasons
            y_line_filtered = np.ma.masked_where((y_line < y_range.min()) | (y_line > y_range.max()), y_line)
            ax.plot(x_range, y_line_filtered, linestyle=estilo, color=color, linewidth=2,
                    label=f'{coeficiente_x}X + {coeficiente_y}Y {simbolo} {valor_direito}')
        elif abs(coeficiente_x) > epsilon: # Vertical line (coeficiente_y is 0 or very close to 0, and coeficiente_x is not)
            # Equation for x: x = valor_direito / coeficiente_x
            x_line_val = valor_direito / coeficiente_x
            ax.axvline(x=x_line_val, linestyle=estilo, color=color, linewidth=2,
                       label=f'{coeficiente_x}X {simbolo} {valor_direito}')
        # If both coeficiente_x and coeficiente_y are effectively zero, it's 0 SINAL valor_direito, which doesn't define a line.


    # Highlight the solution region using imshow with the calculated mask
    ax.imshow(solution_mask, extent=[x_range.min(), x_range.max(), y_range.min(), y_range.max()],
              origin='lower', cmap='Blues', alpha=0.3, aspect='auto')

    # --- Adjustments to make it look like a real Cartesian plane --- (First Quadrant focus)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none') # Remove right spine
    ax.spines['top'].set_color('none')   # Remove top spine
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

    # Set arrowheads for positive axes if desired (optional, more complex)
    # For simplicity, we just use thick lines for now.

    ax.set_xlim(-0.1, x_range.max() + 0.5) # Extend slightly beyond 0 to show the axis, up to max
    ax.set_ylim(-0.1, y_range.max() + 0.5) # Extend slightly beyond 0 to show the axis, up to max
    ax.set_aspect('equal', adjustable='box') # Keep real proportion and adjust box

    plt.legend(loc='upper right', frameon=True, shadow=True)
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.title('Solução de um Sistema de Inequações no Primeiro Quadrante')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def main():
    print("=== Plotador de Sistemas de Inequações Lineares (Primeiro Quadrante) ===")
    inequalities = []
    while True:
        try:
            print("\nPara adicionar uma inequação do tipo 'coeficiente_xX + coeficiente_yY SINAL valor_direito', insira os valores a seguir.")
            print("Digite 'plotar' para gerar o gráfico das inequações atuais ou 'sair' para encerrar o programa.")
            
            user_action = input("Sua ação (coeficiente_xX + coeficiente_yY ... / plotar / sair): ").strip().lower()

            if user_action == 'sair':
                break
            if user_action == 'plotar':
                if not inequalities:
                    print("Erro: Nenhuma inequação adicionada para plotar. Por favor, adicione pelo menos uma inequação.")
                    continue
                plot_sistema_inequacoes(inequalities)
                print("\nGráfico gerado. Você pode continuar adicionando mais inequações ou digitar 'sair' para finalizar.")
                continue
            
            # If user_action was not 'plotar' or 'sair', assume they are entering an inequality.
            # We'll re-prompt for components to ensure robust parsing.
            print("\nInsira os componentes para a nova inequação:")
            
            coeficiente_x_str = input("Valor de coeficiente_x (coeficiente de X): ").replace(",", ".")
            coeficiente_x = float(coeficiente_x_str)

            coeficiente_y_str = input("Valor de coeficiente_y (coeficiente de Y): ").replace(",", ".")
            coeficiente_y = float(coeficiente_y_str)

            simbolo = input("Símbolo da inequação (>, >=, <, <=): ").strip()
            if simbolo not in [">", ">=", "<", "<="]:
                print("Erro: Símbolo inválido. Por favor, use '>', '>=', '<' ou '<='.")
                continue

            vd_str = input("Valor Direito (termo constante): ").replace(",", ".")
            valor_direito = float(vd_str)

            inequalities.append({
                'coeficiente_x': coeficiente_x,
                'coeficiente_y': coeficiente_y,
                'simbolo': simbolo,
                'valor_direito': valor_direito
            })
            print(f"Inequação '{coeficiente_x}X + {coeficiente_y}Y {simbolo} {valor_direito}' adicionada com sucesso.")

        except ValueError:
            print("Erro de entrada: Certifique-se de inserir números válidos para coeficiente_x, coeficiente_y e Valor Direito.")
        except KeyboardInterrupt:
            print("\nEncerrando o programa devido a interrupção do usuário.")
            break

if __name__ == "__main__":
    main()
