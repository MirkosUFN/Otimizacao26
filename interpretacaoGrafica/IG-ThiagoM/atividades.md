# Lista de Exercícios: Programação Linear (Interpretação Geométrica)

## prof. Mirkos O. Martins - mirkos@ufn.edu.br

---

### Exercício 1: Otimização de Infraestrutura em Nuvem (IaaS)

**Contexto:** Uma startup de inteligência artificial precisa alocar instâncias de computação na nuvem para processar um novo pipeline de dados. Ela pode escolher entre dois tipos de instâncias: **Instâncias Standard ($x_1$)** e **Instâncias High-Performance ($x_2$)**.

Cada instância do tipo Standard custa \$20 por hora e possui 4 vCPUs e 8 GB de RAM. Cada instância High-Performance custa \$50 por hora e possui 8 vCPUs e 32 GB de RAM. O pipeline exige, no mínimo, 40 vCPUs e 96 GB de RAM para rodar sem gargalos. Por limitações de cota do provedor, a startup não pode contratar mais do que 12 instâncias no total.

**Formule o problema de PL para minimizar o custo horário e resolva geometricamente:**

1. Identifique a função objetivo e as restrições (técnicas e de não-negatividade).
2. Desenhe a região viável no plano cartesiano.
3. Determine a combinação ideal de instâncias ($x_1, x_2$) e o custo mínimo.

---

### Exercício 2: Alocação de Banda e Roteamento de Tráfego

**Contexto:** Um roteador de borda de um provedor de internet precisa gerenciar o tráfego de dois serviços de streaming: **Stream Básico ($x_1$)** e **Stream Premium ($x_2$)** (valores medidos em milhares de conexões simultâneas). O provedor recebe um benefício de qualidade de serviço (QoS) avaliado em 3 pontos por unidade de Stream Básico e 5 pontos por unidade de Stream Premium.

O processamento desse tráfego consome a capacidade de dois switches de núcleo (A e B). Cada switch possui um limite máximo de pacotes por segundo que consegue processar:

- **Switch A:** Cada unidade de Stream Básico consome 2 Gbps de largura de banda e o Premium consome 4 Gbps. A capacidade máxima do Switch A é de 24 Gbps.
- **Switch B:** Cada unidade de Stream Básico consome 3 Gbps e o Premium consome 2 Gbps. A capacidade máxima do Switch B é de 22 Gbps.

**Formule o problema de PL para maximizar a pontuação de QoS e resolva geometricamente:**

1. Monte o sistema de inequações e a função objetivo.
2. Esboce o polígono que representa a região viável.
3. Encontre o ponto extremo (vértice) que maximiza o QoS.

---

### Exercício 3: Treinamento de Modelos de Deep Learning (Machine Learning)

**Contexto:** Um laboratório de pesquisa em IA possui dois tipos de jobs de treinamento para rodar em seu cluster de GPUs: **Modelos NLP ($x_1$)** e **Modelos de Visão Computacional ($x_2$)**. Cada modelo de NLP treinado gera um valor científico de 4 pontos de impacto, enquanto cada modelo de Visão gera 3 pontos.

O treinamento desses modelos é limitado por dois recursos críticos de hardware: o tempo total de uso das GPUs e o armazenamento no sistema de arquivos distribuído (NVMe Pool).

- **Tempo de GPU:** Um modelo NLP exige 3 horas de computação e um de Visão exige 1 hora. O cluster tem 18 horas disponíveis no total para esse experimento.
- **Armazenamento:** Um modelo NLP consome 1 TB de espaço de checkpoint, enquanto um de Visão consome 2 TB. O limite do storage é de 16 TB.

**Formule o problema de PL para maximizar o impacto científico e resolva geometricamente:**

1. Defina a função objetivo e as restrições.
2. Construa o gráfico, hachurando a região de soluções viáveis.
3. Encontre a quantidade ótima de modelos de NLP e Visão a serem treinados.

---

### Exercício 4: Design de Hardware (Sistemas Embarcados / IoT)

**Contexto:** Uma empresa de hardware está projetando uma placa de circuito impresso (PCB) para um dispositivo IoT de baixo custo. O circuito integrado principal precisa acomodar dois tipos de blocos lógicos estruturais: **Blocos de Memória Cache ($x_1$)** e **Unidades Aritméticas (ALUs) ($x_2$)**. A eficiência energética do chip aumenta em 5 unidades para cada Bloco de Cache e em 4 unidades para cada ALU adicionada.

O design do chip sofre restrições físicas severas de área total de silício e de dissipação térmica (potência):

- **Área de Silício:** Cada bloco de cache ocupa $2\text{ mm}^2$ e cada ALU ocupa $3\text{ mm}^2$. A área máxima disponível no die é de $18\text{ mm}^2$.
- **Dissipação Térmica:** Devido ao superaquecimento, o consumo de energia não pode passar de $12\text{ mW}$. Cada bloco de cache dissipa $2\text{ mW}$ e cada ALU dissipa $1\text{ mW}$.

**Formule o problema de PL para maximizar a eficiência do chip e resolva geometricamente:**

1. Escreva o modelo matemático correspondente.
2. Plote as retas de restrição e identifique os vértices da região viável.
3. Descubra a configuração ideal ($x_1, x_2$) utilizando as retas de nível da função objetivo.

---

### Exercício 5: Planejamento de Sprints (Metodologia Ágil / Engenharia de Software)

**Contexto:** Um Tech Lead de uma fábrica de software precisa planejar a próxima Sprint de duas semanas. A equipe é dividida para focar em duas frentes de trabalho: **Desenvolvimento de Novas Funcionalidades ($x_1$)** e **Refatoração de Código / Correção de Bugs ($x_2$)** (unidades medidas em número de tarefas/User Stories). Cada Funcionalidade entrega 8 pontos de valor de negócio ao cliente, e cada Refatoração entrega 5 pontos.

A equipe enfrenta restrições de tempo de desenvolvimento e tempo de garantia de qualidade (QA/Testes):

- **Desenvolvimento:** Cada funcionalidade exige 4 horas de codificação e cada refatoração exige 4 horas. O time tem um teto de 32 horas dedicadas puramente ao desenvolvimento nesta sprint.
- **Testes (QA):** Funcionalidades exigem testes rigorosos, consumindo 2 horas de QA cada. Já as tarefas de refatoração exigem 1 hora de QA. O analista de testes tem apenas 12 horas disponíveis na sprint.

**Formule o problema de PL para maximizar o valor entregue na Sprint e resolva geometricamente:**

1. Determine as variáveis, restrições e a função a ser maximizada.
2. Construa o gráfico cartesiano e determine a região viável.
3. Encontre a solução ótima e discuta se a solução encontrada possui valores inteiros (e a importância disso no contexto prático de engenharia de software).
