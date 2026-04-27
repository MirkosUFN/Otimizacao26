import numpy as np
import matplotlib.pyplot as plt


# Comparação de acordo com o símbolo da inequação
def comparar(lhs, simbolo, rhs):
    if simbolo == "<":
        return lhs < rhs
    if simbolo == "<=":
        return lhs <= rhs
    if simbolo == ">":
        return lhs > rhs
    return lhs >= rhs

# Leitura de inequação digitada pelo usuário
def ler_inequacao_basica(indice):
    """
    Leitura simples no formato: a1 a2 sinal b
    Exemplo: 2 3 <= 10
    """
    texto = input(f"Inequação {indice} (a1 a2 sinal b) ex.: 2 3 <= 10: ")
    texto = texto.upper().replace(",", ".")
    partes = texto.split()

    a1 = float(partes[0])
    a2 = float(partes[1])
    simbolo = partes[2]
    rhs = float(partes[3])
    return a1, a2, simbolo, rhs


# Define o tamanho dos eixos do gráfico automaticamente.
#Analisa os coeficientes e o termo independente de cada inequação para estimar um limite razoável de visualização.
#Retorna um único valor limite, usado tanto para X quanto para Y.
def calcular_limite(inequacoes):
    limites = [10.0]
    for a1, a2, _, b in inequacoes:
        limites.append(abs(b))
        if a1 != 0:
            limites.append(abs(b / a1))
        if a2 != 0:
            limites.append(abs(b / a2))
    return min(max(limites) * 1.2, 100.0)

# Plotagem do sistema de inequações / desenho do sistema
def plot_sistema(inequacoes):
    limite = calcular_limite(inequacoes)
    x = np.linspace(0, limite, 400)
    y = np.linspace(0, limite, 400)
    X, Y = np.meshgrid(x, y)

    regiao = np.ones_like(X, dtype=bool)
    for a1, a2, simbolo, b in inequacoes:
        regiao &= comparar(a1 * X + a2 * Y, simbolo, b)

    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, regiao.astype(int), levels=[0.5, 1.5], colors=['skyblue'], alpha=0.5)

    x_linha = np.linspace(0, limite, 500)
    for i, (a1, a2, simbolo, b) in enumerate(inequacoes, start=1):
        estilo = '--' if simbolo in ['<', '>'] else '-'
        rotulo = f"I{i}: {a1}X + {a2}Y {simbolo} {b}"

        if a2 != 0:
            y_linha = (b - a1 * x_linha) / a2
            validos = (y_linha >= 0) & np.isfinite(y_linha)
            plt.plot(x_linha[validos], y_linha[validos], estilo, linewidth=2, label=rotulo)
        elif a1 != 0:
            x0 = b / a1
            if x0 >= 0:
                plt.plot([x0, x0], [0, limite], estilo, linewidth=2, label=rotulo)

    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlim(0, limite)
    plt.ylim(0, limite)
    plt.title('Região solução no primeiro quadrante')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend() 
    plt.tight_layout() # Ajusta o layout para evitar sobreposição de elementos
    plt.show()


if __name__ == "__main__":
    print("Sistema de inequações no formato: a1 a2 SINAL valor")
    print("Exemplo: 2 3 <= 10")
    print("Observação: use a2 negativo se quiser termo -Y, por exemplo: 2 -3 <= 10")

    quantidade = int(input("Quantas inequações deseja inserir? "))
    sistema = []

    for i in range(1, quantidade + 1):
        sistema.append(ler_inequacao_basica(i))

    plot_sistema(sistema)