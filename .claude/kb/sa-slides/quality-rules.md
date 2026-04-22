# Quality Rules — Sprint Analítica™ (SA)
> Baseado no sa Slide System, adaptado para a marca de Lucas Pontes, PhD — Fluência Analítica.

---

## 1. Regras de Preenchimento de Tela (Screen Filling)
1. Cada slide DEVE preencher **90%+ do viewport** — evitar buracos vazios.
2. Use `justify-content: center` por padrão.
3. Todo slide de conteúdo DEVE ter um **painel de explicação inferior** usando `margin-top: auto`.
4. Este painel deve conectar o conteúdo técnico ao **Contexto de Negócio** (é o lado "Lucas Pontes" fundamentando o "Lucas Pontes").

## 2. Paleta e Cores (SA Brand)
1. **Fundo:** Sempre `#030616` (Dark Navy).
2. **Ações/Resultados/Ganhos:** Sempre `#FF9900` (Electric Orange).
3. **Dados/IA/Tecnologia:** Sempre `#0AABEC` (Electric Cyan).
4. **Resumo Visual:**
   - `--brand`: Ação, Dinheiro, Impacto, Medo (Lucas Pontes).
   - `--accent`: IA, Método, Estrutura (Lucas Pontes).
   - `--text`: Off-white `#f3f4f6`.

## 3. Tipografia "Lucas Pontes"
1. **Títulos de Impacto (Lucas Pontes):** Montserrat 800 (Bold). Use para headlines que desafiam o status quo.
2. **Narração/Fundamentação (Lucas Pontes):** Newsreader Italic. Use para aspas de autoridade, explicações PhD e conexão com o argumento McKinsey/MIT.
3. **Corpo:** Inter Regular/Medium. Legível e moderno.
4. **Dados/Prompts:** Fira Code. Para o lado "técnico democratizado".

## 4. Branding Bar (SA Config)
1. **Topo:** Fixa, 54px de altura.
2. **Esquerda:** "SPRINT ANALÍTICA™" em Electric Orange.
3. **Centro:** "Lucas Pontes, PhD — Fluência Analítica" em Newsreader Italic.
4. **Direita:** Referência ao Documento Master e Data.
5. **Rodapé (Slide Final):** "FLUÊNCIA ANALÍTICA · SPRINT ANALÍTICA™ · LUCAS PONTES, PhD · 2026"

## 5. Regras de Linguagem (Português de Alta Qualidade)
1. **ACENTUAÇÃO OBRIGATÓRIA:** Jamais entregue palavras como "nao", "voce", "estagio", "decisao".
2. **Checklist de Auditoria:**
   - [ ] Não -> não
   - [ ] Você -> você
   - [ ] Está -> está (verbo)
   - [ ] Codigo -> código
   - [ ] Formacao -> formação
   - [ ] Analítica -> analítica (sempre com acento na marca)
3. **Tom de Voz:** Direto, provocativo, técnico mas sem "economês" ou "academicismo" excessivo. 
   - *O Lucas Pontes garante o método; o Lucas Pontes garante a velocidade.*

## 6. Diagramas e SVG
1. **ViewBox:** Sempre 900+ de largura para diagramas de fluxo.
2. **Stroke:** Use `#0AABEC` para fluxos de dados e `#FF9900` para fluxos de valor/dinheiro.
3. **Textos em SVG:** Use fontes inline (CSS vars não funcionam em atributos SVG):
   - `font-family="'Montserrat',sans-serif"`
   - `font-family="'Newsreader',serif"`
   - `font-family="'Fira Code',monospace"`

## 7. Componentes de Interação (Hover Cards)
1. **JS Inline:** Use `onmouseenter`/`onmouseleave` para elevação de cards.
2. **Shadows:** Use `rgba(10, 171, 236, 0.2)` no hover para dar um aspecto de "brilho tecnológico" ao card.

## 8. Estrutura de Slide (Padrão SA)
1. **Slide 01 (Capa):** Avatar de Lucas Pontes, PhD + Título do Curso + Tagline de Medo/Sobrevivência do V6.
2. **Dividers:** Sempre com número fantasma gigante (opacity 0.05) atrás do título.
3. **Slides de "Roma":** Foco em Ambição (Amarelo/Ouro).
4. **Slides de "Operacional":** Foco em Sair do Buraco (Ciano/IA).

---
*Estes Quality Rules garantem que cada apresentação pareça uma consultoria de alto nível entregue via IA.*
