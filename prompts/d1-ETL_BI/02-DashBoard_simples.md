Prompt Adaptado para o Radar Estratégico (Class 2)
Persona: Você é um Analytics Engineer e Especialista em Business Intelligence, focado em Decision Intelligence. Sua especialidade é criar dashboards executivos que transformam dados de Star Schema (DuckDB) em alavancas de crescimento.

CONTEXTO:
Estamos na aula de Inteligência de Decisão do curso Radar Estratégico. O aluno já realizou o ETL e construiu um Data Warehouse com as tabelas Fact_Marketing_Top_Funnel, Fact_Assinaturas, Dim_Clientes e Dim_Produtos.

OBJETIVO:
Criar um dashboard interativo em um único arquivo HTML (com CSS e JS via CDN) que exponha a saúde do negócio e identifique por que o crescimento acelerado de junho/julho está mascarando um problema de retenção.

ANÁLISES OBRIGATÓRIAS (DASHBOARD DE DECISÃO):

KPIs de Saúde (Top Cards):

MRR Atual: (Monthly Recurring Revenue).

CAC Médio: (Custo de Aquisição por Cliente).

LTV Estimado: (Lifetime Value).

Churn Rate Mensal: (Taxa de cancelamento).

NPS/CSAT Médio: (Sentimento do cliente).

Funil de Aquisição (Funnel Chart):

Exibir a jornada: Cliques -> Leads -> Oportunidades -> Clientes Won.

Calcular a taxa de conversão entre cada etapa.

Matriz de Cohort de Retenção (UAU Moment - Heatmap):

Uma matriz visual mostrando a retenção (%) de cada cohort de novos clientes (Eixo Y: Mês de Início | Eixo X: Mês 0, 1, 2, 3, 4, 5). 
Usar cores quentes para baixa retenção e frias para alta retenção.  

Distribuição de Receita por Canal (Donut):

Google vs Meta Ads vs Orgânico.

Análise de Sentimento (Suporte):

Distribuição de categorias de tickets (Bug, Cancelamento, Dúvida) cruzada com o canal de origem.

DIRETRIZES DE DESIGN (ESTÉTICA RADAR ESTRATÉGICO):

Tema: Dark Mode Premium.

Background: #030616 (Deep Navy).

Cards: #1a1a24 com bordas sutis.

Acentos: #FF9900 (Electric Orange) para alertas e #3859ff (Electric Blue) para dados positivos.

Insights Contextuais: Abaixo de cada gráfico, deve haver uma pequena caixa de "Insight Estratégico" que mude conforme os filtros.

Interatividade:

Filtro por Canal: O usuário deve poder filtrar o dashboard por "Google" ou "Meta Ads".

O Reveal: Ao filtrar por "Meta Ads", a Matriz de Cohort deve mostrar visualmente a queda drástica na retenção a partir do Mês 1, e o card de Insight deve alertar sobre a baixa qualidade dos leads.

TECNOLOGIA:

Use Chart.js para os gráficos e D3.js para a matriz de cohort (heatmap).

Código limpo, formatado para padrões brasileiros (R$).

Tudo em um único arquivo HTML.

DADOS:
Use a estrutura do Star Schema gerada no DuckDB. Agregue os dados para mostrar o volume real de junho/julho e a falha de retenção subsequente.