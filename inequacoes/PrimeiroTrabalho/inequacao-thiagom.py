import numpy as np
import matplotlib.pyplot as plt


def plot_inequacao_linear(a, b, simbolo):
    """
    Desenha a área de solução para a inequação y [simbolo] ax + b.
    """
    # Primeiro,temos que garantir que o símbolo recebido realmente faz sentido.
    simbolos_validos = {">", ">=", "<", "<="}
    if simbolo not in simbolos_validos:
        raise ValueError("Símbolo inválido. Use: >, >=, < ou <=")

    # Criamos vários valores de x para desenhar a reta de forma suave.
    x = np.linspace(-10, 10, 400)
    # Aqui aplicamos a fórmula y = ax + b para cada ponto de x para desenhar a reta.
    y_linha = a * x + b

    # Montamos a janela do gráfico e os eixos.
    plt.figure(figsize=(8, 6))
    plt.axhline(0, color='black', linewidth=1)  # Eixo X
    plt.axvline(0, color='black', linewidth=1)  # Eixo Y

    # Linha tracejada para desigualdade estrita (< ou >),
    # e linha contínua quando a borda faz parte da solução (<= ou >=).
    estilo_linha = '--' if simbolo in ['>', '<'] else '-'
    label_linha = f'y = {a}x + {b}'

    # Essa reta é a fronteira entre "região que vale" e "região que não vale".
    plt.plot(x, y_linha, linestyle=estilo_linha, color='red', label=label_linha)

    # Definimos uma margem para o gráfico não ficar "colado" na reta.
    margem = max(5, 0.1 * (np.max(y_linha) - np.min(y_linha) + 1))
    y_min_plot = np.min(y_linha) - margem
    y_max_plot = np.max(y_linha) + margem

    # Se a inequação for y > ax+b (ou >=), pintamos acima da reta.
    # Caso contrário, pintamos abaixo.
    if simbolo in ['>', '>=']:
        plt.fill_between(x, y_linha, y_max_plot, color='skyblue', alpha=0.4, label='Área de Solução')
    else:
        plt.fill_between(x, y_linha, y_min_plot, color='skyblue', alpha=0.4, label='Área de Solução')

    # Ajustes visuais finais para deixar o gráfico legível.
    plt.title(f'Solução da Inequação: $y {simbolo} {a}x + {b}$')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(y_min_plot, y_max_plot)

    plt.show()

def ler_float(mensagem):
    # Continua pedindo até o usuário digitar um número válido.
    while True:
        try:
            # Aceita vírgula decimal (ex.: 2,5), comum em PT-BR.
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 2, -1.5, 0).")


def ler_simbolo():
    # Também repetimos até vir um operador válido.
    simbolos_validos = {">", ">=", "<", "<="}
    while True:
        simbolo = input("Digite o símbolo da inequação (>, >=, <, <=): ").strip()
        if simbolo in simbolos_validos:
            return simbolo
        print("Símbolo inválido. Use apenas: >, >=, <, <=")


if __name__ == "__main__":
    # Ponto de entrada do programa quando ele é executado diretamente.
    print("Inequação linear da forma: y [símbolo] ax + b")
    a = ler_float("Digite o valor de a: ")
    b = ler_float("Digite o valor de b: ")
    simbolo = ler_simbolo()

    plot_inequacao_linear(a, b, simbolo)