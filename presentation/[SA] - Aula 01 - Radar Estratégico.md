## Roteiro — Aula 1 do Radar Estratégico™

**Da Bagunça ao Insight: ETL, Data Warehouse e Agentes de IA**

_Duração estimada: 90–120 minutos_

---

### Texto de Abertura — Aula 1 · Radar Estratégico™
_10 minutos_

---

#### Slide 1 — Boas-vindas

**Bem-vindo ao Radar Estratégico™**

Você não está aqui para assistir mais uma aula. Você está aqui para aplicar.
usar figura @capa_radar na parte da direita do slide 

---

#### Slide 2 — O que é o Radar Estratégico

**A proposta é simples:**

O Sprint Analítica te deu o método. O Radar te dá a prática — ao vivo, em casos reais, no seu tipo de desafio.

Cada encontro parte de um problema de negócio real, aplica o Framework EDA do zero ao insight na sua frente, e abre a mesa para você trazer o seu caso.

**Objetivos**
- Expandir Horizontes
- Manter atualizações com o estado da arte
- Ajustar a atitude mental para a era da IA
- Gerar valor com Dados

---

#### Slide 3 — Os 3 Encontros

**O que vem pela frente:**

**Encontro 1 — hoje** Da bagunça ao insight: ETL, Data Warehouse e Agentes de IA Como os dados chegam organizados — e como a IA os interroga em linguagem natural

**Encontro 2** Resultado caindo — onde está o problema? Framework EDA aplicado em análise quantitativa: funil, churn e cohort

**Encontro 3** O cliente está falando — você está ouvindo? Framework EDA aplicado em análise qualitativa: NPS e análise de sentimento

---

#### Slide 4 — O que acontece hoje

**Aula 1 · Construindo a Fundação da Máquina de insights**

Hoje você vai entender o que está por trás de qualquer análise bem-feita — e por que a maioria das empresas nunca chega lá.

Vamos cobrir três blocos:

**Fundamentos** — como a IA realmente funciona, por que seus sistemas de gestão não foram feitos para análise e quais os níveis de uso da IA disponíveis hoje

**Técnica** — o que é ETL, o que é um Lakehouse e por que isso importa para quem não é técnico

**Prática** — um agente de IA interrogando uma base de dados ao vivo, em linguagem natural, do dado bruto ao Decision Briefing

Ao final você vai saber o que pedir, o que é possível e como começar na sua empresa — independente do seu nível técnico.

---

#### Slide 5 — Uma coisa antes de começar

**Sobre o que você vai ver hoje:**

Este conteúdo é mais técnico do que o Sprint Analítica.

Não porque você vai precisar executar tudo isso sozinho — mas porque gestores e profissionais de negócio que entendem o que está por baixo tomam decisões melhores, fazem perguntas mais inteligentes e não dependem de ninguém para validar o que é possível.

Você não precisa construir o motor. Precisa saber como ele funciona para dirigir melhor.

Vamos começar.

> _"A maioria dos relatórios corporativos é construída da forma mais cara e mais frágil possível: um analista junta planilhas toda semana, consolida manualmente, formata, envia. Se ele sair de férias, o relatório some. Se a planilha mudar de formato, quebra tudo. E no final, o dashboard que aparece na reunião já está desatualizado."_

**O que essa aula entrega:** o mapa completo de como dados corporativos deveriam ser organizados — e como a IA permite que você interrogue essa estrutura em linguagem natural, sem depender de ninguém do time técnico.

---

### BLOCO 1 — Fundamentos Teóricos

_35–40 minutos_

#### Parte 1A — Como a IA Realmente Funciona

_15 minutos_

**Objetivo:** desmistificar a IA para que o aluno entenda por que ela precisa de dados bem estruturados para funcionar bem. Sem isso, o restante da aula fica sem fundação.

**1. O que é um LLM — Large Language Model**

- Não é um banco de dados. Não "sabe" as informações da sua empresa.
- É um modelo treinado em texto que aprendeu padrões de linguagem e raciocínio.
- Analogia: um consultor brilhante que leu tudo o que já foi publicado — mas não conhece sua empresa. Para ser útil, você precisa dar a ele contexto.

_Ponto-chave para o gestor:_ o LLM é o cérebro. Os dados da empresa são o mapa. Sem o mapa, o cérebro mais inteligente do mundo não encontra nada relevante para o seu negócio.

**2. Redes Neurais — o suficiente para não ter medo**

- Não é necessário entender a matemática. É necessário entender a metáfora.
- Redes neurais aprendem padrões por exposição repetida — como um funcionário que depois de 6 meses começa a antecipar o que o gestor vai pedir.
- O que importa: elas são muito boas em reconhecer padrões em dados — o que as torna poderosas para análise quando bem direcionadas.

**3. O Conceito de Agente: Autonomia e Resolução de Problemas**
**Subtítulo (Opcional):** Da execução passiva à orquestração inteligente de tarefas.

**Tópicos Principais (Bullets):**

- **Definição Central:** Um sistema computacional capaz de perceber seu ambiente, tomar decisões lógicas e executar ações de forma autônoma para atingir um objetivo específico.
    
- **Arquitetura Cognitiva:** Utiliza Modelos de Linguagem (LLMs) como o "motor de raciocínio" para interpretar entradas complexas e planejar múltiplos passos (_Chain of Thought_).
    
- **Capacidade de Atuação (Tools):** Diferente de um modelo estático, o agente possui acesso a ferramentas externas (APIs, bancos de dados, execução de código) para alterar o ambiente real.
    
- **Gestão de Estado e Memória:** Mantém contexto de curto e longo prazo, permitindo a correção de rotas baseada em falhas (reflexão) e aprendizado contínuo durante a execução da tarefa.
    

**Notas do Palestrante (Speaker Notes):**

> "Para ilustrar: um LLM tradicional é como uma enciclopédia interativa; ele responde ao que você pergunta. Um Agente é como um estagiário sênior; você passa um objetivo complexo (ex: 'pesquise nossos concorrentes e monte uma planilha'), e ele planeja os passos, busca na web, formata os dados e entrega o resultado final, corrigindo os próprios erros no caminho."

---

**4. Evaluation Harness Estruturas de Avaliação Rigorosa **
**Subtítulo (Opcional):** Padronizando a medição de performance em sistemas complexos.

**Tópicos Principais (Bullets):**

- **Definição Central:** Um _Harness_ (ou "arnês/infraestrutura de teste") é um framework de software projetado para encapsular, automatizar e padronizar a execução de testes em modelos ou sistemas.
    
- **Isolamento de Variáveis:** Fornece um ambiente controlado onde os _inputs_ (prompts, dados) e _outputs_ são medidos sistematicamente, isolando a performance do modelo de falhas externas.
    
- **Métricas e Benchmarks:** Permite a execução escalável de _datasets_ de referência (ex: MMLU, HumanEval) para quantificar capacidades como raciocínio lógico, matemática, código ou segurança.
    
- **Reprodutibilidade Científica:** Garante que a avaliação de diferentes arquiteturas ou agentes seja comparável, transparente e livre de viés de amostragem manual.
    

**Notas do Palestrante (Speaker Notes):**

> "No desenvolvimento de IA ou software robusto, não podemos confiar em 'testes de feeling' ou anedóticos. O Harness é a bancada de testes metodológica. Ele injeta milhares de cenários no sistema de forma automatizada e extrai relatórios precisos. Se o agente é o 'piloto', o Harness é o simulador de voo que garante e certifica que as métricas de sucesso são estatisticamente válidas."

**5. Tool Calling — quando a IA deixa de conversar e começa a agir**

- Tool Calling é o mecanismo que permite que um LLM execute ações reais: consultar um banco de dados, rodar uma query, chamar uma API, gerar um gráfico.
- Analogia: a diferença entre perguntar para um assistente "como eu faço uma pesquisa de mercado?" e ele te dizer os passos — versus ele mesmo fazer a pesquisa e trazer o resultado.
- **Por que importa aqui:** é o que torna possível o agent query da Parte Prática. Sem Tool Calling, a IA é só texto. Com Tool Calling, ela consegue interrogar seus dados.

---

#### Parte 1B — A Evolução dos Sistemas de Dados

_10 minutos_

**Objetivo:** explicar por que os sistemas que a empresa já usa não foram feitos para análise — e por que isso não é um problema do analista, é um problema de arquitetura.

**OLTP — Online Transaction Processing**

- É o sistema que registra o que acontece: ERP, CRM, sistema de gestão, PDV.
- Otimizado para velocidade de escrita — registrar uma venda em milissegundos.
- Péssimo para análise: consultas complexas travam o sistema, estrutura normalizada dificulta cruzamentos.
- _Exemplo prático:_ quando você tenta cruzar vendas + clientes + produtos no ERP e o sistema fica lento ou retorna dados difíceis de interpretar.

**OLAP — Online Analytical Processing**

- É a camada feita para análise: Data Warehouse, cubos de dados.
- Otimizado para leitura e cruzamento de grandes volumes.
- Permite perguntas complexas sem travar o sistema transacional.
- _Exemplo prático:_ "quero ver receita por região, por categoria de produto, nos últimos 6 meses, comparando com o mesmo período do ano anterior" — isso é OLAP.

**O gap que existe na maioria das empresas:** A maioria das PMEs tem OLTP (sistema de gestão) mas não tem OLAP (camada analítica). O analista vive exportando do sistema para o Excel e construindo a camada analítica manualmente toda semana. Isso é caro, frágil e não escala.

**A solução moderna:** Lakehouse — que vamos ver a seguir.

---

#### Parte 1C — Níveis de Interação com IA

_10 minutos_

**Objetivo:** mostrar ao aluno o espectro completo de como se pode trabalhar com IA — do mais simples ao mais avançado — para que ele saiba onde está e para onde pode ir.

| Nível                               | O que é                                         | Para quem               | Exemplo                                          |
| ----------------------------------- | ----------------------------------------------- | ----------------------- | ------------------------------------------------ |
| **Chat**                            | Conversa direta com o LLM                       | Qualquer profissional   | ChatGPT, Claude para análises pontuais           |
| **Prompt Engineering**              | Estruturar prompts para resultados consistentes | Profissional de negócio | Framework EDA — o que o Sprint Analítica ensina  |
| **Vibe Coding**                     | Pedir o que quer e deixar a IA gerar            | Profissional técnico    | Lovable                                          |
| **Agentes com Tools**               | LLM com acesso a ferramentas externas           | Profissional avançado   | Agent que consulta banco de dados ao vivo        |
| **SDD — Schema-Driven Development** | Definir estrutura de dados que guia a IA        | Técnico / Engenheiro    | IA que gera código a partir de schemas definidos |

**Mensagem central:** você não precisa ir do nível 1 direto para o nível 5. O Framework EDA vive no nível 2. Esta aula mostra o nível 4 em ação — e explica o nível 5 para que você saiba o que pedir para um time técnico.

---

### BLOCO 2 — Técnica

_25–30 minutos_

#### Parte 2A — ETL: o processo que ninguém vê mas todo mundo precisa

_12 minutos_

**Objetivo:** desmistificar o ETL e mostrar que ele é o pré-requisito para qualquer análise confiável.

**O que é ETL — Extract, Transform, Load**

- **Extract:** extrair dados de fontes diferentes — ERP, CRM, planilhas, APIs
- **Transform:** limpar, padronizar, cruzar — o trabalho que hoje é feito manualmente no Excel
- **Load:** carregar na camada analítica — onde a análise vai acontecer

**Demonstração visual:** mostrar o fluxo de dados da empresa típica:

```
ERP (OLTP) ──┐
CRM (OLTP) ──┼──► ETL ──► Data Warehouse (OLAP) ──► Dashboard / Agente IA
Planilhas ───┘
```

**O problema sem ETL:**

- Cada analista faz o ETL na mão, toda semana, no Excel
- Resultados inconsistentes entre áreas
- Impossível automatizar
- Impossível usar agentes de IA — porque não há uma base consolidada para interrogar

**O que muda com ETL automatizado:**

- Uma única fonte de verdade
- Dados sempre atualizados
- Base pronta para dashboard e para agentes de IA
- Analista para de consolidar e começa a analisar

**Ferramentas modernas que democratizaram ETL:**

- dbt — transformação em SQL declarativo
- Airbyte / Fivetran — conectores prontos para as principais fontes
- Python com Pandas — para quem quer controle total

_Mensagem para o gestor:_ você não precisa construir o ETL. Precisa saber que ele existe, por que é necessário e o que pedir para o time técnico ou para um freelancer de dados.

---

#### Parte 2B — Lakehouse: a arquitetura moderna de dados

_10 minutos_

**Objetivo:** apresentar o conceito de Lakehouse como a evolução natural que torna viável ter dados analíticos sem infraestrutura cara.

**A evolução:**

|Geração|Estrutura|Problema|
|---|---|---|
|**Data Warehouse clássico**|Banco relacional estruturado|Caro, rígido, não aceita dados não estruturados|
|**Data Lake**|Armazenamento bruto de tudo|Barato mas vira um "pântano de dados" sem governança|
|**Lakehouse**|Combina os dois — estrutura + flexibilidade|O melhor dos dois mundos|

**O que é um Lakehouse na prática:**

- Armazenamento em arquivos abertos (Parquet, Delta)
- Camada de metadados que dá estrutura sobre esses arquivos
- Suporta SQL, Python e agentes de IA na mesma base
- Pode rodar em cloud barata (S3, Google Cloud Storage) ou localmente

**Ferramentas acessíveis para PMEs:**

- DuckDB — banco analítico que roda localmente, gratuito, incrivelmente rápido
- MotherDuck — DuckDB na nuvem
- Databricks Community — para quem quer explorar Delta Lake

**Demonstração:** mostrar como uma query analítica complexa que travaria um ERP roda em segundos num Lakehouse com DuckDB.

_Mensagem para o gestor:_ você não precisa de uma infraestrutura de big tech para ter uma arquitetura moderna de dados. Com as ferramentas certas, uma PME consegue ter um Lakehouse funcional com custo próximo de zero.

---

### BLOCO 3 — Prática: Agent Query ao Vivo

_30–35 minutos_

**Objetivo:** mostrar ao vivo como um agente de IA conectado a um banco de dados responde perguntas em linguagem natural — e por que isso só funciona bem com a estrutura correta nos Blocos 1 e 2.

#### Setup da demonstração

**Dataset:** base de dados real de e-commerce ou varejo com pelo menos 3 tabelas — pedidos, clientes, produtos — já carregada em DuckDB ou SQLite.

**Agente:** construído com LangChain ou LlamaIndex conectado ao banco, com Tool Calling habilitado para executar queries SQL.

**Interface:** terminal ou Jupyter Notebook visível para os alunos — bastidores completamente abertos.

---

#### Sequência da demonstração ao vivo

**Pergunta 1 — Simples (5 min)**

> _"Qual foi a receita total do último trimestre?"_

Mostrar: o agente recebe a pergunta, identifica a tool de SQL, gera a query, executa, retorna o resultado em linguagem natural. Explicar cada etapa em tempo real.

**Pergunta 2 — Cruzamento (8 min)**

> _"Quais são os 5 produtos com maior taxa de abandono de carrinho nos últimos 90 dias?"_

Mostrar: agente precisa cruzar tabelas de pedidos + produtos + eventos. Explicar como o Tool Calling orquestra múltiplas queries. Mostrar o SQL gerado — não para o aluno aprender SQL, mas para ele ver que a IA está fazendo o trabalho técnico.

**Pergunta 3 — Análise estratégica (10 min)**

> _"Existe correlação entre o tempo de entrega e a nota de NPS? Onde estão os maiores desvios?"_

Mostrar: agente faz análise estatística básica, identifica padrões, retorna interpretação em linguagem executiva. Conectar com o Framework EDA — essa é exatamente a etapa 3 do método (Sinal nos Dados).

**Pergunta 4 — Decision Briefing (7 min)**

> _"Com base nos dados, qual é a principal alavanca de receita que deveríamos priorizar no próximo trimestre?"_

Mostrar: agente sintetiza os insights anteriores, gera uma recomendação estruturada. Mostrar como transformar esse output em um Decision Briefing de uma página. Fechar o ciclo — do dado bruto ao argumento executivo.

---

#### Fechamento da Aula — O que Levar para Amanhã

_5 minutos_

**Três perguntas para o aluno refletir sobre a própria empresa:**

1. _"Seus dados de vendas, clientes e operações estão numa fonte consolidada — ou espalhados em planilhas?"_
2. _"Quanto tempo seu time gasta consolidando dados manualmente toda semana?"_
3. _"Se você pudesse perguntar para seus dados em português e receber a resposta em 30 segundos, que pergunta você faria?"_

**O que fazer com essas respostas:**

- Se os dados estão espalhados: o próximo passo é mapear as fontes e estruturar um ETL simples
- Se há muito trabalho manual: há um caso de negócio claro para automação
- A terceira pergunta: isso é exatamente o que você vai construir capacidade de fazer nas próximas aulas

---

### Materiais de Apoio

|Material|Formato|Quando usar|
|---|---|---|
|Diagrama do fluxo de dados|PDF|Durante o Bloco 2|
|Notebook Jupyter com o agent query|.ipynb|Para alunos replicarem após a aula|
|Dataset de exemplo|CSV / DuckDB|Para prática própria|
|Checklist de maturidade de dados|PDF|Para avaliar a própria empresa|
|Prompt template para interrogar bases|.md|Para usar imediatamente|

---

### Conexão com as Próximas Aulas

**Encerrar com o gancho:**

> _"Agora você sabe como os dados chegam organizados e como a IA os interroga. Nas próximas aulas vamos usar essa estrutura para resolver os dois tipos de desafio que mais aparecem nas empresas: na Aula 2, problemas quantitativos — funil de vendas, churn, cohort — onde o dinheiro está escorrendo. Na Aula 3, problemas qualitativos — NPS, análise de sentimento — onde a voz do cliente está gritando e ninguém está ouvindo."_