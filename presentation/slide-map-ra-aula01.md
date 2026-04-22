# Slide Map: RA-Aula01 — Da Bagunça ao Insight

**Palette:** SA (Navy / Cyan / Orange)
**Total slides:** 22
**Chunks:** 5
**Content source:** `presentation/[SA] - Aula 01 - Radar Estratégico.md`
**Lesson code:** RA-01
**Duration:** 90–120 min

---

## PRE-FLIGHT CHECK

- [x] Every content item from source is mapped to a slide
- [x] Slide count >= 15 for a standard lesson (22 slides)
- [x] Title slide is slide 1 with instructor image
- [x] Closing quote is the last slide
- [x] Every section starts with a divider
- [x] Every content slide has bottom panel = Yes
- [x] SVG-heavy slides have viewBox width specified
- [x] Chunk boundaries at divider slides
- [x] No chunk exceeds 7 slides
- [x] Portuguese accent words listed per slide
- [x] Visual pattern assigned to every slide
- [x] Palette correctly identified (SA)

---

## Chunk 1: Abertura (slides 1–5)

> **Theme:** Boas-vindas, apresentação do programa, agenda da aula e contrato de aprendizado.

---

### Slide 1 — title
- **Type:** title
- **Visual:** title-standard (with `electric-text` on line 2)
- **SVG:** No
- **Content:**
  - Label: `RADAR ESTRATÉGICO™ · ENCONTRO 1`
  - Pill: `RA-01` (accent) · `90–120 min` (gold)
  - Title line 1: `Da Bagunça`
  - Title line 2 (electric-text): `ao Insight`
  - Subtitle (Newsreader italic): *ETL, Data Warehouse e Agentes de IA*
  - Instructor avatar: `../../../images/lucas-pontes.jpg`
  - Tags: `Radar Estratégico™` · `Lucas Pontes` · `Sprint Analítica`
  - Right image: `@capa_radar` (side panel, right column)
- **Bottom panel:** No
- **Accents:** Estratégico, Analítica, Agentes

---

### Slide 2 — context
- **Type:** context (2-col: left editorial + right objective cards)
- **Visual:** glassmorphism-card (4 objective cards on right)
- **SVG:** No
- **Content:**
  - Left col headline: *"Você não está aqui para assistir mais uma aula. Você está aqui para aplicar."*
  - Left col body: "O Sprint Analítica te deu o método. O Radar te dá a prática — ao vivo, em casos reais, no seu tipo de desafio."
  - Right col — 4 cards:
    1. 🔭 Expandir Horizontes
    2. ⚡ Manter-se atualizado com o estado da arte
    3. 🧠 Ajustar a atitude mental para a era da IA
    4. 📊 Gerar valor com Dados
- **Bottom panel:** Yes — *"Cada encontro: um problema real, o Framework EDA do zero ao insight, e sua empresa na mesa."*
- **Accents:** você, está, Analítica

---

### Slide 3 — phase-flow
- **Type:** phase-flow (3 phases — the 3 encounters)
- **Visual:** svg-flow-ribbons (horizontal, 3 phases)
- **SVG:** Yes | **ViewBox:** 960
- **Content:** 3 phase cards:
  1. **Encontro 1 — HOJE** · `RA-01` tag · "Da bagunça ao insight: ETL, Data Warehouse e Agentes de IA"
  2. **Encontro 2** · `RA-02` tag · "Resultado caindo — onde está o problema? Funil, churn e cohort"
  3. **Encontro 3** · `RA-03` tag · "O cliente está falando — você está ouvindo? NPS e análise de sentimento"
- **Highlight:** Phase 1 card highlighted (brand border / pulse)
- **Bottom panel:** Yes — *"Três encontros. Três tipos de problema. Uma metodologia: Framework EDA."*
- **Accents:** Encontro, análise, sentimento, cohort, está

---

### Slide 4 — flow-architecture
- **Type:** flow-architecture (3 macro-blocks of today's agenda)
- **Visual:** icon-badge-row (3 columns with icon + title + bullets)
- **SVG:** No
- **Content:**
  - Heading: "Aula 1 · Construindo a Fundação da Máquina de Insights"
  - Block 1 (accent icon): **Fundamentos** — Como a IA funciona, OLTP vs OLAP, Níveis de uso da IA
  - Block 2 (brand icon): **Técnica** — ETL, Lakehouse, Ferramentas modernas
  - Block 3 (gold icon): **Prática** — Agent query ao vivo, do dado bruto ao Decision Briefing
- **Bottom panel:** Yes — *"Ao final você vai saber o que pedir, o que é possível e como começar — independente do seu nível técnico."*
- **Accents:** Fundamentos, Técnica, Prática, Decisão, análise

---

### Slide 5 — hook-quote
- **Type:** hook-quote
- **Visual:** giant-quote-mark (opacity 0.05 background aspas)
- **SVG:** No
- **Content:**
  - Quote: *"A maioria dos relatórios corporativos é construída da forma mais cara e mais frágil possível: um analista junta planilhas toda semana, consolida manualmente, formata, envia. Se ele sair de férias, o relatório some."*
  - Attribution: — Lucas Pontes, PhD · Fluência Analítica
  - Sub-tag: `Você não precisa construir o motor. Precisa saber como ele funciona.`
- **Bottom panel:** No
- **Accents:** não, está, já, férias, Analítica

---

## Chunk 2: Bloco 1 — Fundamentos da IA (slides 6–11)

> **Theme:** Como a IA realmente funciona. LLM, Redes Neurais, Agentes, Evaluation Harness, Tool Calling.

---

### Slide 6 — divider
- **Type:** divider
- **Visual:** ghost-number (`01`)
- **SVG:** No
- **Content:**
  - Ghost number: `01`
  - Label (mono): `BLOCO 1 · 35–40 MINUTOS`
  - Heading: "Fundamentos Teóricos"
  - Subtitle: "Como a IA Realmente Funciona — sem a magia e sem o medo"
- **Bottom panel:** No
- **Accents:** Fundamentos, Teóricos, Realmente

---

### Slide 7 — method-grid
- **Type:** method-grid (2-panel: O que é / O que NÃO é)
- **Visual:** center-divider
- **SVG:** No
- **Content:**
  - Heading: "O que é um LLM — Large Language Model"
  - Left panel (❌ Mito): "Não é um banco de dados. Não 'sabe' as informações da sua empresa."
  - Right panel (✅ Realidade): "É um modelo treinado em texto que aprendeu padrões de linguagem e raciocínio."
  - Analogy card (gold border): *"Um consultor brilhante que leu tudo — mas não conhece sua empresa. Você precisa dar a ele contexto."*
  - Key insight: "O LLM é o cérebro. Os dados da empresa são o mapa. Sem o mapa, o cérebro mais inteligente do mundo não encontra nada relevante."
- **Bottom panel:** Yes — *"Ponto-chave para o gestor: não culpe a IA quando ela não sabe do seu negócio — você não deu o mapa."*
- **Accents:** não, é, padrões, dados

---

### Slide 8 — context
- **Type:** context (editorial left + 3 bullets right)
- **Visual:** glassmorphism-card
- **SVG:** No
- **Content:**
  - Heading: "Redes Neurais — o suficiente para não ter medo"
  - Editorial left: *"Não é necessário entender a matemática. É necessário entender a metáfora."*
  - Right bullets:
    - "Aprendem padrões por exposição repetida"
    - "Como um funcionário que após 6 meses antecipa o que o gestor vai pedir"
    - "São muito boas em reconhecer padrões em dados — o que as torna poderosas para análise"
- **Bottom panel:** Yes — *"Você não precisa saber construir a rede. Precisa saber o que ela é capaz de fazer pelos seus dados."*
- **Accents:** não, é, necessário, matemática, padrões, análise

---

### Slide 9 — flow-architecture
- **Type:** flow-architecture (4-node definition of an AI Agent)
- **Visual:** svg-architecture-360 (hub-and-spoke circular)
- **SVG:** Yes | **ViewBox:** 1000
- **Content:**
  - Heading: "O Conceito de Agente: Autonomia e Resolução de Problemas"
  - Subtitle (italic): *"Da execução passiva à orquestração inteligente de tarefas"*
  - 4 nodes:
    1. **Perceber** — Input do ambiente (prompt, dados, eventos)
    2. **Raciocinar** — LLM como motor (Chain of Thought)
    3. **Agir** — Tool Calling: APIs, banco de dados, código
    4. **Aprender** — Memória e reflexão para corrigir rotas
  - Speaker note quote (bottom): *"Um Agente é como um estagiário sênior: você passa um objetivo complexo e ele planeja, busca, formata e entrega."*
- **Bottom panel:** Yes — *"Diferença chave: o LLM responde ao que você pergunta. O Agente age sobre o que você quer alcançar."*
- **Accents:** Autônomo, Resolução, Agente, raciocínio, correção, reflexão

---

### Slide 10 — context
- **Type:** context (editorial + 4 bullets)
- **Visual:** glassmorphism-card
- **SVG:** No
- **Content:**
  - Heading: "Evaluation Harness — Estruturas de Avaliação Rigorosa"
  - Subtitle: *"Padronizando a medição de performance em sistemas complexos"*
  - 4 bullets:
    1. Framework de software para encapsular, automatizar e padronizar testes em modelos
    2. Ambiente controlado: inputs e outputs medidos sistematicamente
    3. Permite execução de benchmarks (MMLU, HumanEval) para quantificar capacidades
    4. Garante reprodutibilidade científica e comparação transparente entre arquiteturas
  - Analogy (Newsreader italic): *"Se o agente é o 'piloto', o Harness é o simulador de voo que certifica que as métricas são estatisticamente válidas."*
- **Bottom panel:** Yes — *"Sem Harness, confiamos em 'feeling'. Com Harness, confiamos em evidência — a diferença entre achismo e ciência de dados."*
- **Accents:** Avaliação, Rigorosa, Padronizando, científica, válidas

---

### Slide 11 — method-grid
- **Type:** method-grid (2-panel: Antes vs Depois do Tool Calling)
- **Visual:** center-divider
- **SVG:** No
- **Content:**
  - Heading: "Tool Calling — quando a IA deixa de conversar e começa a agir"
  - Left (sem Tool Calling): "LLM só de texto — responde, explica, sugere. Para aí."
  - Right (com Tool Calling, brand highlight): "LLM + Ferramentas — consulta banco, roda query, chama API, gera gráfico, entrega resultado."
  - Analogy (accent border): *"A diferença entre perguntar 'como fazer uma pesquisa' — e o assistente fazer a pesquisa e trazer o resultado."*
  - Connector to demo: "É o que torna possível o agent query da Parte Prática desta aula."
- **Bottom panel:** Yes — *"Sem Tool Calling, a IA é só texto. Com Tool Calling, ela interroga seus dados."*
- **Accents:** é, está, ação

---

## Chunk 3: Sistemas de Dados & ETL (slides 12–16)

> **Theme:** Evolução dos sistemas. OLTP vs OLAP. Níveis de IA. ETL pipeline.

---

### Slide 12 — divider
- **Type:** divider
- **Visual:** ghost-number (`01C`)
- **SVG:** No
- **Content:**
  - Ghost number: `01C`
  - Label (mono): `PARTE 1B + 1C · SISTEMAS & NÍVEIS DE IA`
  - Heading: "A Evolução dos Sistemas de Dados"
  - Subtitle: "Por que seus sistemas de gestão não foram feitos para análise"
- **Bottom panel:** No
- **Accents:** Evolução, análise, gestão, dados

---

### Slide 13 — method-grid
- **Type:** method-grid (2-panel: OLTP vs OLAP)
- **Visual:** center-divider (accent vs brand columns)
- **SVG:** No
- **Content:**
  - Heading: "OLTP vs OLAP — dois mundos, dois propósitos"
  - Left (OLTP — accent border):
    - Título: "Online Transaction Processing"
    - "ERP, CRM, sistema de gestão, PDV"
    - "Otimizado para velocidade de escrita"
    - "⚠️ Péssimo para análise — consultas complexas travam o sistema"
    - Exemplo: *"Cruzar vendas + clientes + produtos no ERP = sistema lento"*
  - Right (OLAP — brand border):
    - Título: "Online Analytical Processing"
    - "Data Warehouse, cubos de dados"
    - "Otimizado para leitura e cruzamento de grandes volumes"
    - "✅ Permite perguntas complexas sem travar o transacional"
    - Exemplo: *"Receita por região, por categoria, nos últimos 6 meses vs. ano anterior"*
  - Gap insight (gold card): "A maioria das PMEs tem OLTP mas não tem OLAP. O analista constrói a camada analítica manualmente no Excel. Isso é caro, frágil e não escala."
- **Bottom panel:** Yes — *"O gap não é culpa do analista. É um problema de arquitetura — e tem solução."*
- **Accents:** análise, é, não, gestão

---

### Slide 14 — table
- **Type:** table (5 levels of AI interaction)
- **Visual:** authors-table (row highlights for levels 2 and 4)
- **SVG:** No
- **Content:**
  - Heading: "Níveis de Interação com IA — onde você está, para onde pode ir"
  - Table columns: Nível | O que é | Para quem | Exemplo
  - Rows:
    1. Chat | Conversa direta com o LLM | Qualquer profissional | ChatGPT, Claude
    2. **Prompt Engineering** ⭐ | Estruturar prompts para resultados consistentes | Profissional de negócio | **Framework EDA — Sprint Analítica ensina isso** (accent highlight)
    3. Vibe Coding | Pedir e deixar a IA gerar | Profissional técnico | Lovable
    4. **Agentes com Tools** 👁 | LLM com acesso a ferramentas externas | Profissional avançado | **Agent query — vemos hoje** (brand highlight)
    5. SDD | Schema-Driven Development | Técnico / Engenheiro | IA que gera código a partir de schemas
- **Bottom panel:** Yes — *"Você não precisa ir do nível 1 ao 5. O Framework EDA vive no nível 2. Esta aula mostra o nível 4 ao vivo."*
- **Accents:** está, você, não, nível, também

---

### Slide 15 — divider
- **Type:** divider
- **Visual:** ghost-number (`02`)
- **SVG:** No
- **Content:**
  - Ghost number: `02`
  - Label (mono): `BLOCO 2 · 25–30 MINUTOS`
  - Heading: "Técnica"
  - Subtitle: "ETL, Lakehouse e a arquitetura que torna a IA possível"
- **Bottom panel:** No
- **Accents:** Técnica, Lakehouse, arquitetura

---

### Slide 16 — flow-architecture
- **Type:** flow-architecture (ETL pipeline left-to-right)
- **Visual:** svg-pipeline-horizontal
- **SVG:** Yes | **ViewBox:** 1000
- **Content:**
  - Heading: "ETL — Extract, Transform, Load"
  - Subtitle: *"O processo que ninguém vê mas todo mundo precisa"*
  - Pipeline nodes:
    - **Fontes (OLTP):** ERP · CRM · Planilhas · APIs
    - **Extract →** coleta bruta das fontes
    - **Transform →** limpar, padronizar, cruzar (o que hoje é feito no Excel)
    - **Load →** carrega na camada analítica
    - **Destino:** Data Warehouse (OLAP) → Dashboard / Agente IA
  - SVG colors: `#0AABEC` para fluxo de dados, `#FF9900` para seta final ao Agente IA
  - Contrast card (red border): "SEM ETL: analista consolida na mão, toda semana, inconsistente, não escala, agentes de IA impossíveis."
  - Tools badge row (mono): `dbt` · `Airbyte` · `Fivetran` · `Python + Pandas`
- **Bottom panel:** Yes — *"Você não precisa construir o ETL. Precisa saber que ele existe, por que é necessário e o que pedir para um time técnico."*
- **Accents:** análise, Extração, Transformação, Carga, está, não

---

## Chunk 4: Lakehouse (slides 17–18)

> **Theme:** Arquitetura moderna de dados — gerações e ferramentas para PMEs.

---

### Slide 17 — tier-cards
- **Type:** tier-cards (3 generations of data architecture)
- **Visual:** card-grid (3 columns, Lakehouse card highlighted/pulse)
- **SVG:** No
- **Content:**
  - Heading: "A Evolução da Arquitetura de Dados"
  - Card 1 — Data Warehouse Clássico (text-dim border):
    - "Banco relacional estruturado"
    - "✅ Estrutura e governança"
    - "❌ Caro, rígido, não aceita dados não estruturados"
  - Card 2 — Data Lake (text-dim border):
    - "Armazenamento bruto de tudo"
    - "✅ Barato e flexível"
    - "❌ Vira um 'pântano de dados' sem governança"
  - Card 3 — **Lakehouse** ⭐ (brand border + pulse glow):
    - "Combina estrutura + flexibilidade"
    - "✅ Parquet/Delta · SQL + Python + Agentes IA"
    - "✅ Cloud barata ou local — custo próximo de zero"
- **Bottom panel:** Yes — *"Uma PME não precisa de infraestrutura de big tech para ter arquitetura moderna. Com DuckDB, você tem um Lakehouse funcional, gratuito, incrivelmente rápido."*
- **Accents:** Clássico, não, também, também, é

---

### Slide 18 — stat-cards
- **Type:** stat-cards (3 modern tools as impact cards)
- **Visual:** stat-card-4line (icon + tool name + role + why it matters)
- **SVG:** No
- **Content:**
  - Heading: "Ferramentas que democratizaram o Lakehouse"
  - Card 1: **DuckDB** · "Banco analítico local" · Gratuito, incrivelmente rápido · tag: `Para quem quer começar amanhã`
  - Card 2: **MotherDuck** · "DuckDB na nuvem" · Sem infra, sem custo inicial · tag: `Para quem quer escalar`
  - Card 3: **dbt** · "Transformação em SQL declarativo" · Substitui o Excel do analista · tag: `Para quem quer automatizar`
- **Tags:** [`PME-Ready`, `Open Source`, `No-Lock-In`]
- **Bottom panel:** Yes — *"Com DuckDB + dbt + Airbyte, uma PME tem uma stack analítica de nível enterprise — sem o custo de enterprise."*
- **Accents:** também, nível, não, é

---

## Chunk 5: Prática + Fechamento (slides 19–22)

> **Theme:** Agent query ao vivo. Perguntas progressivas. Reflexão final. Closing quote com teaser.

---

### Slide 19 — divider
- **Type:** divider
- **Visual:** ghost-number (`03`)
- **SVG:** No
- **Content:**
  - Ghost number: `03`
  - Label (mono): `BLOCO 3 · 30–35 MINUTOS`
  - Heading: "Prática"
  - Subtitle: "Agent Query ao Vivo — do dado bruto ao Decision Briefing"
- **Bottom panel:** No
- **Accents:** Prática, decisão

---

### Slide 20 — pipeline
- **Type:** pipeline (4 numbered demonstration steps)
- **Visual:** svg-pipeline-horizontal (numbered badges, horizontal flow)
- **SVG:** Yes | **ViewBox:** 960
- **Content:**
  - Heading: "Sequência da Demonstração ao Vivo"
  - Subtitle: *"Bastidores completamente abertos"*
  - Step 1 (5 min): **Pergunta Simples** — *"Qual foi a receita total do último trimestre?"* → recebe, identifica tool SQL, gera query, executa, responde em linguagem natural
  - Step 2 (8 min): **Cruzamento** — *"Quais são os 5 produtos com maior taxa de abandono de carrinho nos últimos 90 dias?"* → cruza pedidos + produtos + eventos, Tool Calling orquestra múltiplas queries
  - Step 3 (10 min): **Análise Estratégica** — *"Existe correlação entre tempo de entrega e NPS?"* → análise estatística, identifica padrões, retorna interpretação executiva
  - Step 4 (7 min): **Decision Briefing** — *"Qual é a principal alavanca de receita para o próximo trimestre?"* → sintetiza insights, gera recomendação estruturada de uma página
  - Setup badge (mono small): `Dataset: DuckDB e-commerce · Agente: LangChain + Tool Calling · Interface: Jupyter Notebook`
- **Bottom panel:** Yes — *"Este é o Framework EDA em ação: do dado bruto (Extract) à análise (Discover) ao argumento executivo (Act)."*
- **Accents:** também, análise, decisão, Correlação, é, está, último

---

### Slide 21 — stat-cards
- **Type:** stat-cards (3 reflection questions)
- **Visual:** stat-card-4line (large number + question + action)
- **SVG:** No
- **Content:**
  - Heading: "O que Levar para a Sua Empresa"
  - Subtitle: "Três perguntas para refletir agora"
  - Card 1: `?1` · *"Seus dados de vendas, clientes e operações estão numa fonte consolidada — ou espalhados em planilhas?"* · Ação: mapear fontes e estruturar um ETL simples
  - Card 2: `?2` · *"Quanto tempo seu time gasta consolidando dados manualmente toda semana?"* · Ação: há um caso de negócio claro para automação
  - Card 3: `?3` · *"Se você pudesse perguntar para seus dados em português e receber a resposta em 30 segundos, que pergunta você faria?"* · Ação: isso é o que você vai construir nas próximas aulas
- **Tags:** [`Diagnóstico`, `Oportunidade`, `Próximo Passo`]
- **Bottom panel:** Yes — *"Essas três perguntas são o começo do seu diagnóstico de maturidade analítica. Guarde as respostas."*
- **Accents:** consolidada, está, você, análise, Diagnóstico, Próximo, também

---

### Slide 22 — closing-quote
- **Type:** closing-quote
- **Visual:** gold-quote (aspas `--brand` orange, blockquote Newsreader italic)
- **SVG:** No
- **Content:**
  - Quote: *"Agora você sabe como os dados chegam organizados e como a IA os interroga. Nas próximas aulas vamos usar essa estrutura para resolver os dois tipos de desafio que mais aparecem nas empresas: problemas quantitativos — onde o dinheiro está escorrendo — e problemas qualitativos — onde a voz do cliente está gritando e ninguém está ouvindo."*
  - Attribution: — Lucas Pontes, PhD · Radar Estratégico™
  - Next lesson pill: `Próximo: RA-02 · Resultado caindo — onde está o problema?`
  - Footer (mono): `RADAR ESTRATÉGICO™ · SPRINT ANALÍTICA · LUCAS PONTES, PhD · 2026`
- **Bottom panel:** No
- **Accents:** está, você, quantitativos, qualitativos, análise, Próximo, Estratégico

---

## Summary Table

| Slide | Type | Visual Pattern | SVG | Chunk |
|-------|------|----------------|-----|-------|
| 1 | title | title-standard + electric-text | No | 1 |
| 2 | context | glassmorphism-card | No | 1 |
| 3 | phase-flow | svg-flow-ribbons | Yes (960) | 1 |
| 4 | flow-architecture | icon-badge-row | No | 1 |
| 5 | hook-quote | giant-quote-mark | No | 1 |
| 6 | divider | ghost-number (01) | No | 2 |
| 7 | method-grid | center-divider | No | 2 |
| 8 | context | glassmorphism-card | No | 2 |
| 9 | flow-architecture | svg-architecture-360 | Yes (1000) | 2 |
| 10 | context | glassmorphism-card | No | 2 |
| 11 | method-grid | center-divider | No | 2 |
| 12 | divider | ghost-number (01C) | No | 3 |
| 13 | method-grid | center-divider | No | 3 |
| 14 | table | authors-table | No | 3 |
| 15 | divider | ghost-number (02) | No | 3 |
| 16 | flow-architecture | svg-pipeline-horizontal | Yes (1000) | 3 |
| 17 | tier-cards | card-grid | No | 4 |
| 18 | stat-cards | stat-card-4line | No | 4 |
| 19 | divider | ghost-number (03) | No | 5 |
| 20 | pipeline | svg-pipeline-horizontal | Yes (960) | 5 |
| 21 | stat-cards | stat-card-4line | No | 5 |
| 22 | closing-quote | gold-quote | No | 5 |

**SVG slides:** 3, 9, 16, 20 (4 total — max 1 per chunk, well within limits)
