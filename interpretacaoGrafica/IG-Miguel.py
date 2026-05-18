import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')

# =============================================================================
# FUNÇÃO DE PLOTAGEM GEOMÉTRICA
# =============================================================================
def plotar_regiao_viavel(x_val, restricoes, regiao, ponto_otimo, config):
    """
    Função automatizada para plotar os gráficos de Programação Linear.
    
    :param x_val: Array do linspace para o eixo X.
    :param restricoes: Lista de dicionários contendo os arrays das retas e seus labels.
    :param regiao: Dicionário com as coordenadas X e Y para preencher a região viável.
    :param ponto_otimo: Dicionário com a coordenada (X, Y) e o texto do ponto ótimo.
    :param config: Configurações de títulos, eixos e limites do gráfico.
    """
    plt.figure(figsize=(8, 6))
    
    # 1. Plota as linhas de restrição dinamicamente
    for r in restricoes:
        plt.plot(x_val, r['reta'], label=r['label'])
        
    # 2. Preenche a região viável usando os polígonos que você calculou
    plt.fill(regiao['x'], regiao['y'], color='lightgreen', alpha=0.4, label='Região Viável')
    
    # 3. Destaca o ponto da solução ótima
    plt.plot(ponto_otimo['x'], ponto_otimo['y'], 'ro', markersize=10, label=ponto_otimo['label'])
    
    # 4. Configurações estéticas e de limites
    plt.xlim(config['xlim'])
    plt.ylim(config['ylim'])
    plt.xlabel(config['xlabel'])
    plt.ylabel(config['ylabel'])
    plt.title(config['title'])
    
    # 5. Finalização do layout
    plt.legend()
    plt.grid(True)
    plt.show()


# =============================================================================
# EXERCÍCIO 1: Otimização de Infraestrutura em Nuvem (IaaS)
# =============================================================================
x1_ex1 = np.linspace(0, 16, 400)

restricoes_ex1 = [
    {'reta': (40 - 4*x1_ex1) / 8, 'label': '4x1 + 8x2 >= 40 (vCPUs)'},
    {'reta': (96 - 8*x1_ex1) / 32, 'label': '8x1 + 32x2 >= 96 (RAM)'},
    {'reta': 12 - x1_ex1,          'label': 'x1 + x2 <= 12 (Limite)'}
]

plotar_regiao_viavel(
    x_val=x1_ex1,
    restricoes=restricoes_ex1,
    regiao={'x': [0, 8, 12, 0], 'y': [5, 1, 0, 12]},
    ponto_otimo={'x': 8, 'y': 1, 'label': 'Solucao Otima (8, 1)'},
    config={
        'xlim': (0, 14), 'ylim': (0, 14),
        'xlabel': 'x1 (Standard)', 'ylabel': 'x2 (High-Performance)',
        'title': 'Exercicio 1: Regiao Viavel e Solucao Otima'
    }
)


# =============================================================================
# EXERCÍCIO 2: Alocação de Banda e Roteamento de Tráfego
# =============================================================================
x1_ex2 = np.linspace(0, 12, 400)

restricoes_ex2 = [
    {'reta': (24 - 2*x1_ex2) / 4, 'label': '2x1 + 4x2 <= 24 (Switch A)'},
    {'reta': (22 - 3*x1_ex2) / 2, 'label': '3x1 + 2x2 <= 22 (Switch B)'}
]

plotar_regiao_viavel(
    x_val=x1_ex2,
    restricoes=restricoes_ex2,
    regiao={'x': [0, 0, 5, 22/3], 'y': [0, 6, 3.5, 0]},
    ponto_otimo={'x': 5, 'y': 3.5, 'label': 'Solucao Otima (5, 3.5)'},
    config={
        'xlim': (0, 10), 'ylim': (0, 12),
        'xlabel': 'x1 (Stream Basico)', 'ylabel': 'x2 (Stream Premium)',
        'title': 'Exercicio 2: Regiao Viavel e Solucao Otima'
    }
)


# =============================================================================
# EXERCÍCIO 3: Treinamento de Modelos de Deep Learning (Machine Learning)
# =============================================================================
x1_ex3 = np.linspace(0, 10, 400)

restricoes_ex3 = [
    {'reta': 18 - 3*x1_ex3,       'label': '3x1 + x2 <= 18 (GPU)'},
    {'reta': (16 - x1_ex3) / 2,  'label': 'x1 + 2x2 <= 16 (Storage)'}
]

plotar_regiao_viavel(
    x_val=x1_ex3,
    restricoes=restricoes_ex3,
    regiao={'x': [0, 0, 4, 6], 'y': [0, 8, 6, 0]},
    ponto_otimo={'x': 4, 'y': 6, 'label': 'Solucao Otima (4, 6)'},
    config={
        'xlim': (0, 8), 'ylim': (0, 20),
        'xlabel': 'x1 (Modelos NLP)', 'ylabel': 'x2 (Modelos Visao)',
        'title': 'Exercicio 3: Regiao Viavel e Solucao Otima'
    }
)


# =============================================================================
# EXERCÍCIO 4: Design de Hardware (Sistemas Embarcados / IoT)
# =============================================================================
x1_ex4 = np.linspace(0, 8, 400)

restricoes_ex4 = [
    {'reta': (18 - 2*x1_ex4) / 3, 'label': '2x1 + 3x2 <= 18 (Silicio)'},
    {'reta': 12 - 2*x1_ex4,       'label': '2x1 + x2 <= 12 (Termica)'}
]

plotar_regiao_viavel(
    x_val=x1_ex4,
    restricoes=restricoes_ex4,
    regiao={'x': [0, 0, 4.5, 6], 'y': [0, 6, 3, 0]},
    ponto_otimo={'x': 4.5, 'y': 3, 'label': 'Solucao Otima (4.5, 3)'},
    config={
        'xlim': (0, 8), 'ylim': (0, 14),
        'xlabel': 'x1 (Blocos Cache)', 'ylabel': 'x2 (Unidades ALU)',
        'title': 'Exercicio 4: Regiao Viavel e Solucao Otima'
    }
)


# =============================================================================
# EXERCÍCIO 5: Planejamento de Sprints (Metodologia Ágil / Engenharia de Software)
# =============================================================================
x1_ex5 = np.linspace(0, 10, 400)

restricoes_ex5 = [
    {'reta': 8 - x1_ex5,     'label': '4x1 + 4x2 <= 32 (Dev)'},
    {'reta': 12 - 2*x1_ex5,  'label': '2x1 + x2 <= 12 (QA)'}
]

plotar_regiao_viavel(
    x_val=x1_ex5,
    restricoes=restricoes_ex5,
    regiao={'x': [0, 0, 4, 6], 'y': [0, 8, 4, 0]},
    ponto_otimo={'x': 4, 'y': 4, 'label': 'Solucao Otima (4, 4)'},
    config={
        'xlim': (0, 10), 'ylim': (0, 14),
        'xlabel': 'x1 (Funcionalidades)', 'ylabel': 'x2 (Refatoracao)',
        'title': 'Exercicio 5: Regiao Viavel e Solucao Otima'
      }
)