import os
from fractions import Fraction  # Utilizado para garantir resultados exatos (ex: 1/3) e evitar erros de arredondamento

def limpar_tela():
    """Limpa o terminal conforme o sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_matriz(matriz, titulo="Matriz Atual"):
    """Exibe a matriz ampliada com formatação para facilitar o acompanhamento."""
    print(f"\n{titulo}:")
    n = len(matriz)
    for linha in matriz:
        # Separa os coeficientes do termo independente para formatar a barra visual
        elementos = [str(val) for val in linha[:-1]]
        resultado = str(linha[-1])
        corpo = " ".join(f"{val:>8}" for val in elementos)
        print(f"[ {corpo} | {resultado:>8} ]")
    print("-" * (12 * (n + 1))) 

def obter_sistema():
    """Gerencia a entrada de dados e monta a matriz inicial."""
    limpar_tela()
    print("=== Resolvendo Sistemas Lineares (Método de Gauss-Jordan) ===")
    
    try:
        n = int(input("Informe o número de variáveis (e equações): "))
        if n <= 0:
            print("Erro: O número de variáveis deve ser positivo.")
            return None
    except ValueError:
        print("Erro: Digite um número inteiro.")
        return None

    matriz = []
    print(f"\nDigite os coeficientes do sistema {n}x{n}:")
    for i in range(n):
        linha = []
        print(f"\nEquação {i + 1}:")
        for j in range(n):
            val = input(f"  Coeficiente de X{j+1}: ")
            linha.append(Fraction(val))
        res = input(f"  Termo independente: ")
        linha.append(Fraction(res))
        matriz.append(linha)
    
    return matriz

def resolver_gauss_jordan():
    matriz = obter_sistema()
    if not matriz:
        return

    n = len(matriz)
    exibir_matriz(matriz, "Matriz Inicial")

    for i in range(n):
        # Passo 1: Pivotamento Parcial
        # Se o pivô atual for zero, busca uma linha abaixo para trocar
        if matriz[i][i] == 0:
            for k in range(i + 1, n):
                if matriz[k][i] != 0:
                    print(f"\n[Aviso] Troca de linha: L{i+1} <-> L{k+1}")
                    matriz[i], matriz[k] = matriz[k], matriz[i]
                    exibir_matriz(matriz)
                    break
            else:
                print(f"\n[Erro] O sistema não possui solução única (determinante zero).")
                return

        # Passo 2: Normalização da linha pivô
        # Divide a linha pelo pivô para que o elemento da diagonal se torne 1
        pivo = matriz[i][i]
        if pivo != 1:
            print(f"\nOperação: L{i+1} = L{i+1} / {pivo}")
            matriz[i] = [val / pivo for val in matriz[i]]
            exibir_matriz(matriz)

        # Passo 3: Eliminação de Gauss-Jordan
        # Zera todos os outros elementos da coluna atual (acima e abaixo do pivô)
        for j in range(n):
            if i != j:
                fator = matriz[j][i]
                if fator != 0:
                    print(f"\nOperação: L{j+1} = L{j+1} - ({fator} * L{i+1})")
                    matriz[j] = [matriz[j][k] - (fator * matriz[i][k]) for k in range(n + 1)]
                    exibir_matriz(matriz)

    print("\n=== Resultado Final (Sistema Resolvido) ===")
    exibir_matriz(matriz)
    
    print("\nValores encontrados:")
    for i in range(n):
        print(f"X{i+1} = {matriz[i][-1]}")

if __name__ == "__main__":
    try:
        resolver_gauss_jordan()
    except Exception as e:
        print(f"\nErro no processamento: {e}")
    input("\nPressione Enter para sair...")
