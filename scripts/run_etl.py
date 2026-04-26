import duckdb
import os

DB_PATH = 'bi_analytics.duckdb'

SQL_SCRIPT = """
-- ==========================================
-- 0. PREPARAÇÃO DO AMBIENTE
-- ==========================================
CREATE SCHEMA IF NOT EXISTS DW;

-- ==========================================
-- 1. INGESTÃO / LEITURA DOS CSVs
-- ==========================================

CREATE OR REPLACE TABLE raw_crm_leads AS SELECT * FROM read_csv_auto('gen/data/bi_class/crm_leads.csv');
CREATE OR REPLACE TABLE raw_crm_oportunidades AS SELECT * FROM read_csv_auto('gen/data/bi_class/crm_oportunidades.csv');
CREATE OR REPLACE TABLE raw_erp_clientes AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_clientes.csv');
CREATE OR REPLACE TABLE raw_erp_produtos AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_produtos.csv');
CREATE OR REPLACE TABLE raw_erp_assinaturas AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_assinaturas.csv');
CREATE OR REPLACE TABLE raw_google_campanhas AS SELECT * FROM read_csv_auto('gen/data/bi_class/google_campanhas.csv');
CREATE OR REPLACE TABLE raw_meta_campanhas AS SELECT * FROM read_csv_auto('gen/data/bi_class/meta_campanhas.csv');

-- ==========================================
-- 2. CRIAÇÃO DAS TABELAS FINAIS (DW)
-- ==========================================

-- 2.1 dim_clientes
CREATE OR REPLACE TABLE DW.dim_clientes AS
WITH stg_leads AS (
    SELECT 
        id_lead,
        data_criacao AS data_criacao_lead,
        LOWER(TRIM(email)) AS email_padronizado,
        LOWER(TRIM(utm_source)) AS canal_aquisicao,
        utm_campaign AS campanha_aquisicao,
        status AS status_funil
    FROM raw_crm_leads
),
stg_erp_clientes AS (
    SELECT 
        id_cliente,
        LOWER(TRIM(email)) AS email_padronizado
    FROM raw_erp_clientes
)
SELECT 
    ec.id_cliente,
    sl.id_lead,
    sl.email_padronizado,
    sl.canal_aquisicao,
    sl.campanha_aquisicao,
    sl.data_criacao_lead,
    sl.status_funil
FROM stg_leads sl
LEFT JOIN raw_crm_oportunidades co ON sl.id_lead = co.id_lead
LEFT JOIN stg_erp_clientes ec ON sl.email_padronizado = ec.email_padronizado;

-- 2.2 dim_tempo
CREATE OR REPLACE TABLE DW.dim_tempo AS
WITH stg_leads AS (
    SELECT 
        id_lead,
        data_criacao AS data_criacao_lead,
        LOWER(TRIM(email)) AS email_padronizado,
        LOWER(TRIM(utm_source)) AS canal_aquisicao,
        utm_campaign AS campanha_aquisicao,
        status AS status_funil
    FROM raw_crm_leads
),
date_range AS (
    SELECT 
        MIN(data_criacao_lead)::DATE as start_date, 
        MAX(data_criacao_lead)::DATE as end_date 
    FROM stg_leads
)
SELECT 
    datum AS data_completa,
    year(datum) AS ano,
    month(datum) AS mes,
    strftime(datum, '%Y-%m') AS ano_mes
FROM (
    SELECT CAST(range AS DATE) AS datum
    FROM range(
        (SELECT start_date FROM date_range), 
        (SELECT end_date + INTERVAL 1 DAY FROM date_range), 
        INTERVAL 1 DAY
    )
);

-- 2.3 dim_produtos
CREATE OR REPLACE TABLE DW.dim_produtos AS
SELECT 
    id_produto,
    nome AS nome_produto
FROM raw_erp_produtos;

-- 2.4 fact_marketing_top_funnel
CREATE OR REPLACE TABLE DW.fact_marketing_top_funnel AS
SELECT 
    data,
    'google' AS canal,
    id_campanha,
    impressoes,
    cliques,
    gasto
FROM raw_google_campanhas
UNION ALL
SELECT 
    data,
    'facebook' AS canal,
    id_campanha,
    impressoes,
    cliques,
    gasto
FROM raw_meta_campanhas;

-- 2.5 fact_assinaturas
CREATE OR REPLACE TABLE DW.fact_assinaturas AS
SELECT 
    id_evento,
    id_cliente,
    id_produto,
    data_evento,
    tipo_evento,
    mrr_novo
FROM raw_erp_assinaturas;

"""

def run_etl():
    print(f"Connecting to {DB_PATH}...")
    con = duckdb.connect(DB_PATH)
    
    print("Executing ETL SQL script...")
    con.execute(SQL_SCRIPT)
    
    print("ETL execution complete.")
    
    # Validation
    print("\n--- Validation ---")
    tables = con.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema = 'DW'").fetchall()
    for schema, table in tables:
        count = con.execute(f"SELECT COUNT(*) FROM {schema}.{table}").fetchone()[0]
        print(f"Table {schema}.{table}: {count} records")
    
    con.close()

if __name__ == "__main__":
    run_etl()
