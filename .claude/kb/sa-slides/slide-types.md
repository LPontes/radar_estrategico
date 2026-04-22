# Slide Types — sa Slides

> Cada slide no deck deve seguir um destes tipos. Escolha o tipo certo para cada item de conteúdo do roteiro.

---

## 1. Title Slide (`slide--title`)

**Propósito:** Abertura da aula. Define o tom e autoridade.
**Layout:** Centralizado, imagem do instrutor, badges de módulo/aula.
**Elementos:** Label do Módulo, Pill da Aula (RA-X), pill de duração, título Montserrat 800 (Lucas Pontes), subtítulo Newsreader Italic (Lucas Pontes), avatar Lucas Pontes + Nome em Montserrat, row de tags.

## 2. Hook Quote (`slide--quote`)

**Propósito:** Citação dramática para capturar a atenção.
**Layout:** Centralizado, marca de aspas gigante, bloco editorial.
**Elementos:** Aspas (opacity 0.05), blockquote com frase principal em destaque, fonte/autor em destaque.

## 3. Context Slide (Bio/Explicação)

**Propósito:** Explicar um conceito fundamental ou background.
**Layout:** Grid de 2 colunas, bio à esquerda + cards à direita.
**Elementos:** Texto editorial (0.95rem+), 4-5 cards de contribuição com bordas coloridas, painel inferior de aspas.

## 4. Timeline Grid

**Propósito:** Mostrar progressão histórica de dados ou tecnologia.
**Layout:** Grid de 7 colunas (ou flex adaptável).
**Elementos por node:** Ano (display 1.5rem), título (display 1.05rem), tagline (editorial italic), parágrafo de detalhe, pill de estatística (mono).

## 5. Stat Cards

**Propósito:** Exibir 3-4 métricas chave ou "factoids" de impacto.
**Layout:** Grid de 3 colunas.
**Elementos:** Valor estatístico gigante (Montserrat 800), label mono, descrição, painel inferior conectando o dado ao negócio.

## 6. Divider (`slide--divider`)

**Propósito:** Quebra visual entre blocos de conteúdo.
**Layout:** Centralizado, número fantasma gigante ao fundo.
**Elementos:** Número gigante (opacity 0.04, gradient text), label da seção, título Montserrat em destaque.

## 7. Flow Architecture

**Propósito:** Mostrar fluxo de dados ou processos da "Ponte".
**Layout:** Row flexível com setas SVG e diagramas 360.
**Elementos:** Caixas de entrada → Processamento → Saída, passos numerados, exemplos práticos em cada card, painel de insight inferior.

## 8. Pipeline (Passos Horizontais)

**Propósito:** Mostrar passos sequenciais numerados.
**Layout:** Row flexível com badges numerados + setas.

## 9. Phase Flow (Progresso de Projeto)

**Propósito:** Mostrar progressão de 3 fases com detalhes técnicos e de valor.
**Layout:** `.phase-flow` com `.phase-card` + setas SVG.

## 10. Bar Chart

**Propósito:** Mostrar dados comparativos com barras animadas.
**Layout:** `.bar-chart` com linhas empilhadas.

## 11. Method Grid (Comparação 2-Painéis)

**Propósito:** Comparar duas abordagens/arquiteturas (ex: OLTP vs OLAP).
**Layout:** `.method-grid` de 2 colunas.

## 12. Tier Cards (Comparação 3-Planos/Modos)

**Propósito:** Comparar 3 opções ou versões (ex: Data Warehouse, Data Lake, Lakehouse).
**Layout:** Grid de 3 colunas, um card destacado com brilho/pulse.

## 13. Table Slide

**Propósito:** Exibir dados estruturados (ex: mapeamento de ferramentas).
**Layout:** `.authors-table` (tabela estilizada).

## 14. Closing Quote

**Propósito:** Fechamento épico + teaser da próxima aula.
**Layout:** `slide--quote` centralizado.
**Elementos:** Aspas douradas/laranja, blockquote, parágrafo editorial, pill "Próximo: RA-X", rodapé Sprint Analítica.

---

## Convenção de Ordem dos Slides

1. **Title** (Capa sempre em primeiro)
2. **Context** (Contextualização do instrutor/tema)
3. **Hook Quote** (A dor central ou provocação)
4. **Timeline/Stats** (Contexto histórico ou numérico)
5. **Divider** → Conteúdo técnico/estratégico (Pipeline, Architecture, Dives)
6. **Closing Quote** (Fechamento e teaser)
