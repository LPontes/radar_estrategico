Chame a função /openspec-explore para criar o PRD deste projeto de ETL, utilizando como base as informações abaixo:

Atue como um Engenheiro de Dados Sênior e Especialista em DuckDB. Sua missão é construir o pipeline de ETL e a camada Gold (Star Schema) de um Data Warehouse a partir de arquivos CSV brutos (raw data).

## CONTEXTO DO NEGÓCIO:
Temos dados de marketing, CRM e ERP. Os dados brutos contêm inconsistências de digitação que quebram os relacionamentos entre os sistemas. Precisamos limpar esses dados e estruturá-los para análises de Funil e Cohort de Retenção.

## ARQUIVOS DE ENTRADA DISPONÍVEIS:
- crm_leads.csv
- crm_oportunidades.csv
- erp_clientes.csv
- erp_pedidos.csv
- erp_itens_pedido.csv
- erp_produtos.csv
- erp_assinaturas.csv
- google_campanhas.csv
- meta_campanhas.csv

## REGRAS DE ETL OBRIGATÓRIAS (TRATAMENTO DE DADOS):
1. O campo "email" na tabela crm_leads possui inconsistências (maiúsculas/minúsculas). Você deve aplicar LOWER() e TRIM() antes de fazer qualquer JOIN com erp_clientes.
2. O campo "utm_source" possui variações de caixa (ex: 'facebook' e 'FACEBOOK'). Aplique LOWER() e TRIM() para padronizar os canais de aquisição.

## MODELAGEM DIMENSIONAL EXIGIDA (STAR SCHEMA):
Escreva o código SQL em DuckDB para criar as seguintes Views ou Tabelas na Camada Gold:

1. Dim_Clientes:
- Faça o JOIN de crm_leads (limpo) com crm_oportunidades (LEFT JOIN) e erp_clientes (LEFT JOIN no email limpo).
- Colunas necessárias: id_cliente (se existir), id_lead, email_padronizado, canal_aquisicao (o utm_source limpo), campanha_aquisicao, data_criacao_lead, status_funil.

2. Dim_Tempo:
- Uma tabela calendário simples extraída a partir das datas mínimas e máximas dos eventos.
- Colunas: data_completa, ano, mes, ano_mes (YYYY-MM).

3. Dim_Produtos:
- Seleção direta de erp_produtos.
- Colunas: id_produto, nome_produto, plano, recorrente.

4. Fact_Marketing_Top_Funnel:
- Faça um UNION ALL ou agregue os dados diários de google_campanhas e meta_campanhas.
- Colunas necessárias: data, canal (google ou facebook), id_campanha, impressoes, cliques, gasto.

5. Fact_Assinaturas:
- Seleção direta de erp_assinaturas mapeando a retenção.
- Colunas: id_evento, id_cliente, id_produto, data_evento, tipo_evento, mrr_novo.

## ENTREGA ESPERADA:
Crie o PRD utilizando a função /openspec-explore, com as seguintes informações:
- Use o prompt acima como base para a criação do PRD.
- O PRD deve conter o código SQL executável do DuckDB para criar essas estruturas. Não utilize dados de exemplo genéricos, baseie-se estritamente na estrutura descrita. Separe o script em etapas lógicas: 1. Ingestão/Leitura dos CSVs, 2. Transformação/Limpeza (CTEs) e 3. Criação das Tabelas Finais.