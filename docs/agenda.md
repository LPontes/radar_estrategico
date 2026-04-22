# Radar Estratégico™

Radar Estratégico | Fluência Analítica | Lucas Pontes

---

## Visão Geral

Em **4 noites práticas + 1 podcast**, os participantes constroem do zero o **EDA**: um sistema multi-agente de IA para e-commerce que consulta dados estruturados (SQL) e semânticos (vetores), com interface conversacional e frontend profissional.

**Pergunta Central:** *O que eu consigo fazer agora que não conseguia antes?*

**Filosofia Docker-First:** Dias 1–3 rodam 100% local. Dia 4 migra para cloud — mesma arquitetura, só muda o endpoint.

> Este evento é o **Radar Estratégico™**: o Framework EDA aplicado ao vivo em casos reais. O aluno sai sabendo exatamente onde olhar e como apresentar — usando os dados que já tem, sem programar.

---

## Posicionamento do Evento

| Etapa no Funil | Driver | Promessa |
|---|---|---|
| **Sprint Analítica™** (front-end, R$37–67) | Sobrevivência | Você tem os dados. Falta o método para não ficar para trás. |
| **→ Radar Estratégico™** (upsell, R$197) | Transição — sobrevivência + primeiros sinais de ambição | Veja o Framework EDA funcionando ao vivo no seu tipo de desafio — e traga o seu caso. |
| **Radar Estratégico™ Pro** *(futuro, R$800–1.500)* | Ambição | Torne-se a referência na sua área e escolha o cargo que deseja. |

---

## Stack Completa

```
+------------------+     +------------------+     +------------------+
|  DADOS           |     |   IA / LLM       |     |   INTERFACE      |
|  ShadowTraffic   |     |   Claude         |     |   Chainlit       |
+--------+---------+     |   LlamaIndex     |     |   Frontend Pro   |
         |               |   LangChain      |     +--------+---------+
         v               |   CrewAI         |              |
+------------------+     +--------+---------+              v
|  ARMAZENAMENTO   |              |               +------------------+
|  Postgres        |              v               |   QUALIDADE      |
|  (The Ledger)    |     +------------------+     |   DeepEval       |
|  Qdrant          |<--->|   MCP Protocol   |     |   LangFuse       |
|  (The Memory)    |     |   AgentSpec      |     +------------------+
+------------------+     +------------------+
```

---

## Arco Narrativo — Progressão de Fluência Analítica

| Dia | Tema | Emoção | O Participante Sai Com... |
|-----|------|--------|--------------------------|
| 1 Seg | **INGERIR** | Curiosidade | Dados fluindo + primeiro contacto com Agentic Commerce |
| 2 Ter | **CONTEXTUALIZAR** | Confiança | IA pesquisando nos SEUS dados — Ledger + RAG |
| 3 Qua | **AGENTE** | Empolgação | Agente autônomo tomando decisões sozinho |
| 4 Qui | **MULTI-AGENTE** | Orgulho | Time de agentes + Frontend profissional + Cloud |
| 5 Sex | **REFLETIR** | Inspiração | Clareza sobre carreira e próximo passo |

### Progressão de Autonomia — Do Executor ao Estrategista

```
Dia 1:  EU FAÇO, IA AJUDA           → Executor que usa IA pontualmente
Dia 2:  IA BUSCA, EU PERGUNTO       → Framework EDA + dados próprios (RAG + Ledger)
Dia 3:  IA PROJETA, EU VALIDO       → Analista que usa o método com consistência
Dia 4:  IA CONSTRÓI, IA EXECUTA     → Referência estratégica que a empresa consulta antes de decidir
```

> **Conexão com o One Belief:** "Usar IA para analisar dados é a chave para não ficar para trás — e a melhor forma de fazer isso é com o Framework EDA."

---

## Agentic Commerce — O Fio Condutor

> *O shopper do futuro não é humano. É um agente de IA que decide e executa.*

O EDA não é só um exercício técnico — é um exemplo real do que o mercado está adotando. Ele conecta diretamente à **ruminação do ICP**: *"Tenho os dados. Sei que tem valor ali. Mas não sei como transformar isso em algo que a liderança ouça."*

| Antes | Agora (Agentic Commerce) |
|-------|--------------------------|
| Humano navega, compara, decide | Agente pesquisa, compara, executa |
| SEO para olhos humanos | AEO (Agent Engine Optimization) para máquinas |
| Funil de 7 etapas | Conversa única |
| Dados para dashboards — cemitérios de dados | Dados para agentes — Fluência Analítica |

- **McKinsey (Jan 2026):** AI agents podem intermediar **$3–5 trilhões** em comércio global até 2030
- **Google Cloud (Jan 2026):** Lançou "Gemini Enterprise for CX" — agentes autônomos discovery-to-purchase
- **60%+ das buscas** de produto já começam em interfaces de IA, não em search engines

| Dia | Conexão com Agentic Commerce |
|-----|------------------------------|
| 1 | "O mercado está mudando: $3–5 tri intermediados por agentes. Vamos construir um." |
| 2 | "Pra um agente funcionar, precisa de dados exatos E compreensão. Isso é Ledger + RAG." |
| 3 | "Um agente de verdade decide sozinho. AgentSpec projeta, o agente executa." |
| 4 | "Na prática: um time de agentes com frontend profissional. Isso é o produto." |

---

# DIA 1 — Segunda-feira

## INGERIR: Dados + Fundamentos + Agentic Commerce

> *De "o que é isso?" para "tenho dados fluindo e entendo para onde o mercado vai"*

**Driver do Dia:** Sobrevivência — *"Estou ficando para trás e preciso agir."*
**Persona ativa:** Ana Beatriz, 29 anos, analista que abre o Excel todo dia e fecha sem chegar a lugar nenhum.

### Agenda Detalhada

#### Bloco 1: AI Data Engineering + AI Coding Agents (20h00 – 20h25)

| Horário | Atividade | Detalhes |
|---------|-----------|----------|
| 20h00 | **AI Data Engineering** | O que é, números do mercado, como a IA muda o papel do analista |
| 20h10 | **AI Coding Agents** | O que são e os 4 tipos — ferramenta, não destino |
| 20h18 | **Panorama de Ferramentas** | Cursor (IDE), Claude Code (Terminal), Codex (Cloud) — contexto, não tutorial |

> **Gancho:** *"Funções de pura manipulação de dados vão desaparecer. O que o FEM e a McKinsey já disseram — e o que isso significa para você agora."*

#### Bloco 2: Claude Code Deep Dive (20h25 – 21h00)

| Horário | Atividade | Detalhes |
|---------|-----------|----------|
| 20h25 | **Por que Terminal, não IDE** | Autonomia real vs. assistência — a diferença que o ICP ainda não viu |
| 20h35 | **Demonstração ao vivo** | Claude Code ingerindo dados — EU FAÇO, IA AJUDA |
| 20h50 | **Estrutura do projeto** | Ledger (Postgres) + Memory (Qdrant) — o mapa do que vem a seguir |

#### Bloco 3: Agentic Commerce & EDA (21h00 – 21h25)

| Horário | Atividade | Detalhes |
|---------|-----------|----------|
| 21h00 | **O Momento Disruptivo** | "Até 2030, agentes de IA vão intermediar mais comércio do que todos os marketplaces juntos." |
| 21h10 | **Apresentação do EDA** | O que vamos construir esta semana — e por que importa para a carreira |
| 21h18 | **Conexão Framework EDA** | O EDA é o Framework EDA em escala: pergunta certa → IA executa → sinal → decisão |

> **Gancho interno para upsell:** *"No Radar Estratégico™, eu aplico o Framework EDA ao vivo e você traz o seu caso — não o caso do EDA, o seu."*

#### Bloco 4: ShadowTraffic — Geração de Dados (21h25 – 22h10)

| Horário | Atividade | Detalhes |
|---------|-----------|----------|
| 21h25 | **O problema real** | Dados caóticos travam qualquer análise — e ninguém ensina a resolver isso |
| 21h35 | **ShadowTraffic ao vivo** | Gerando datasets realistas de e-commerce: pedidos, clientes, reviews, estoque |
| 22h00 | **Ingestão no Ledger** | ETL rodando — dados fluindo para o Postgres |

> **Conexão com OB2 — Base Pronta™:** *"Se sua base está bagunçada, existe um jeito de resolver em minutos antes de analisar — 12 prompts que fazem isso sem código."*

#### Bloco 5: Pydantic & Structured Outputs (22h10 – 22h45)

| Horário | Atividade | Detalhes |
|---------|-----------|----------|
| 22h10 | **Por que estrutura importa** | A IA sem estrutura gera genérico — com contexto de negócio, encontra o sinal |
| 22h20 | **Pydantic na prática** | Modelando dados de e-commerce com tipagem forte |
| 22h35 | **Outputs estruturados** | A base para o Decision Briefing que a liderança recebe |

> **Provocação:** *"Você não está sendo pago para cruzar planilhas. Está sendo pago para o que vem depois. Hoje você deu o primeiro passo."*

#### Bloco 6: Encerramento (22h45 – 23h00)

- **Recap:** "Você tem dados reais fluindo e entende para onde o mercado vai."
- **Conexão com o ICP:** A Ana Beatriz não fecha o Excel sem chegar a lugar nenhum — ela tem método agora.
- **Desafio:** Explorar o Ledger com uma pergunta estratégica antes de amanhã.
- **Preview Dia 2:** "Amanhã a IA vai pesquisar nos SEUS dados — RAG + Ledger."

**Entregas do Dia:**
- [x] ETL pronto
- [x] Data Warehouse em SQLite / Postgres (The Ledger)
- [x] Primeiro contato com Fluência Analítica na prática

---

## Ganchos de Funil Interno — Dia 1

| Momento | Gancho | Produto |
|---------|--------|---------|
| **Bloco 3 — final** | *"30 frameworks prontos te dizem qual pergunta fazer em qualquer desafio — com o prompt de IA pronto para executar."* | OB1 — 30 Frameworks de Análise |
| **Bloco 4 — abertura** | *"Se sua base está bagunçada, existe um jeito de resolver em minutos."* | OB2 — Base Pronta™ |
| **Bloco 6 — encerramento** | *"No Radar Estratégico™ eu aplico o Framework EDA ao vivo e você traz o seu caso."* | Radar Estratégico™ |

---

## Conexão Semana ↔ Formação

| Dia | Semana (Introdução — 20%) | Formação (Domínio — 100%) |
|-----|--------------------------|--------------------------|
| 1 | ShadowTraffic + Pydantic + Claude Code | Foundation: 16 módulos + 4 AI Coding Agents |
| 2 | RAG + Ledger via MCP | Framework EDA aplicado — perguntas estratégicas nos dados próprios |
| 3 | AgentSpec + Agente autônomo | Fluência Analítica consistente — do sinal ao Decision Briefing |
| 4 | Multi-agente + Frontend + Cloud | Referência estratégica — o profissional que a empresa consulta antes de decidir |

---

## Framework EDA — Referência Rápida

| Etapa | Nome | O que acontece | Por que importa |
|---|---|---|---|
| **1** | Foco no Negócio | Define a pergunta estratégica antes de abrir qualquer dado | Sem a pergunta certa, a análise vira exploração sem destino |
| **2** | IA como Motor | A IA executa — limpeza, cruzamento, padrões. O profissional dirige com contexto | Contexto de negócio direciona a IA. Sem ele, ela gera genérico |
| **3** | Sinal nos Dados | Identifica o detalhe que explica o desafio atual | O momento do "foi eu" — a velocidade de encontrar o sinal é o superpoder |
| **4** | Entrega de Valor | Transforma o sinal em Decision Briefing: linguagem executiva, uma página | Fluência Analítica sem comunicação é trabalho invisível |

---

## Métricas de Sucesso

| Métrica | Meta | Como Medir |
|---------|------|------------|
| Audiência Dia 1 (ao vivo) | 1.000+ | Plataforma de live |
| Taxa de conversão → Radar Estratégico™ | ≥ 15% dos compradores da Sprint Analítica™ | Painel de vendas |
| Entregável Dia 1 completo | 100% dos participantes com Ledger rodando | Check ao vivo |
| Prova social gerada | ≥ 1 momento de "foi eu" capturável para anúncio | Gravação da sessão |

---

## As Três Ruminações que Guiam a Comunicação

**1 — Tão Perto Tão Longe (Manifestação A — tráfego frio):**
> *"Você abre os dados todo dia. Sabe que tem algo ali. E fecha sem chegar a lugar nenhum. De novo."*

**2 — Mostrar Serviço com IA (Manifestação B — remarketing):**
> *"Todo mundo fala que usa IA. Poucos sabem mostrar resultado real com ela."*

**3 — O Destino (Roma — upsell e back-end):**
> *"O profissional que chega na reunião com o insight que ninguém tinha visto — amparado nos dados, com clareza total, mal conseguindo dormir esperando apresentar."*

---

*Radar Estratégico™ · Sprint Analítica™ · Lucas Pontes, PhD — Fluência Analítica · 2026*
