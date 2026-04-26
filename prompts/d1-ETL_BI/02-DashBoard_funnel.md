Atue como um Engenheiro de Front-end Sênior e Especialista em UI/UX Design. Sua tarefa é criar um Dashboard Executivo de "Inteligência de Decisão" em um único arquivo HTML (usando Tailwind CSS via CDN e Chart.js).

CONTEXTO DO NEGÓCIO (DADOS):
O dashboard deve mostrar a armadilha de retenção (Cohort) escondida por trás de um pico de vendas (Funil) causado por uma campanha ruim de Meta Ads nos meses de Junho e Julho.
- KPIs: MRR (R$ 45.200), CAC (R$ 120), LTV Estimado (R$ 950), Churn Rate (12%).
- Gráfico Principal 1 (Esquerda): Funil de Vendas (Cliques -> Leads -> Clientes) mostrando alto volume.
- Gráfico Principal 2 (Direita): Matriz de Cohort (Heatmap) mostrando retenção despencando no Mês 2 para os cohorts recentes.

IDENTIDADE VISUAL E STYLING (ESTRITAMENTE OBRIGATÓRIO):
Você deve replicar uma estética "Dark Neon Analytics", seguindo exatamente estas diretrizes de CSS/Tailwind:

1. Cores de Fundo:
- Background geral da página: Azul muito escuro/Night sky (ex: #0B0F19 ou `bg-slate-950`).
- Background dos Cards/Painéis: Azul escuro levemente mais claro (ex: #131826 ou `bg-slate-900`).

2. Cores de Acento (Neon/Glow):
- Primária: Ciano Neon (ex: #00F0FF ou `text-cyan-400`).
- Secundária: Roxo/Violeta Vibrante (ex: #B026FF ou `text-purple-500`).
- Use um gradiente dessas duas cores (cyan-to-purple) em elementos de destaque.

3. Tipografia:
- Fonte: 'Inter' ou 'Plus Jakarta Sans' (importe via Google Fonts).
- Números de KPIs: Brancos, fonte bold, tamanho grande.
- Textos de apoio/labels: Cinza azulado (ex: `text-slate-400`), tamanho pequeno.

4. Estilização dos Cards (Glassmorphism sutil):
- Bordas arredondadas generosas (`rounded-2xl` ou 16px).
- Borda interna extremamente sutil (`border border-slate-800`).
- Adicione uma fina linha de gradiente brilhante no topo dos cards de KPI principais (border-top accent).
- Sombra sutil para destacar os cards do fundo (`shadow-lg shadow-black/50`).

5. Estilização dos Gráficos (Chart.js):
- Remova todas as linhas de grade (grid lines) sólidas. Deixe apenas marcações muito sutis (`rgba(255,255,255,0.05)`).
- Os gráficos de linha ou área devem ter a propriedade `tension: 0.4` para curvas suaves.
- Preenchimento (Fill): Use gradientes lineares semi-transparentes sob as linhas (fading de ciano para transparente).
- Heatmap de Cohort: As células com retenção alta devem ser em tons de ciano/roxo vibrante, e as de retenção baixa quase pretas ou vermelhas escuras para indicar o alerta de churn.

LAYOUT ESPERADO:
- Header superior: Título "Radar Estratégico", Data, e um seletor de "Canal de Origem" (Todos / Meta Ads).
- Linha 1: 4 Cards de KPI. Cada card deve ter o número grande e um mini-gráfico (sparkline) brilhante ao fundo.
- Linha 2: O container principal dividido em dois (Funil à esquerda, Heatmap de Cohort à direita).
- Adicione um card flutuante ou seção de "Insight Estratégico" com um alerta vermelho/laranja destacando a queda de retenção no Meta Ads.

ENTREGA:
Gere o código HTML completo, responsivo, com os scripts integrados. O visual deve parecer um software financeiro premium de ponta.