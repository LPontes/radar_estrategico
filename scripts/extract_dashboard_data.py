import duckdb
import json
import os

# Use an in-memory database to avoid locks
con = duckdb.connect(':memory:')

def extract_data():
    # 1. Setup Staging Tables (similar to ETL)
    con.execute("CREATE TABLE raw_crm_leads AS SELECT * FROM read_csv_auto('gen/data/bi_class/crm_leads.csv')")
    con.execute("CREATE TABLE raw_crm_oportunidades AS SELECT * FROM read_csv_auto('gen/data/bi_class/crm_oportunidades.csv')")
    con.execute("CREATE TABLE raw_erp_clientes AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_clientes.csv')")
    con.execute("CREATE TABLE raw_erp_produtos AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_produtos.csv')")
    con.execute("CREATE TABLE raw_erp_assinaturas AS SELECT * FROM read_csv_auto('gen/data/bi_class/erp_assinaturas.csv')")
    con.execute("CREATE TABLE raw_google_campanhas AS SELECT * FROM read_csv_auto('gen/data/bi_class/google_campanhas.csv')")
    con.execute("CREATE TABLE raw_meta_campanhas AS SELECT * FROM read_csv_auto('gen/data/bi_class/meta_campanhas.csv')")
    con.execute("CREATE TABLE raw_suporte AS SELECT * FROM read_csv_auto('gen/data/bi_class/suporte_tickets.csv')")

    # 2. Build Mini-DW in memory
    con.execute("CREATE SCHEMA DW")
    
    # stg_leads helper
    con.execute("""
        CREATE VIEW stg_leads AS 
        SELECT 
            id_lead,
            data_criacao AS data_criacao_lead,
            LOWER(TRIM(email)) AS email_padronizado,
            LOWER(TRIM(utm_source)) AS canal_aquisicao,
            utm_campaign AS campanha_aquisicao,
            status AS status_funil
        FROM raw_crm_leads
    """)

    con.execute("""
        CREATE VIEW stg_erp_clientes AS 
        SELECT 
            id_cliente,
            LOWER(TRIM(email)) AS email_padronizado
        FROM raw_erp_clientes
    """)

    con.execute("""
        CREATE TABLE DW.dim_clientes AS
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
        LEFT JOIN stg_erp_clientes ec ON sl.email_padronizado = ec.email_padronizado
    """)

    con.execute("""
        CREATE TABLE DW.fact_marketing_top_funnel AS
        SELECT data, 'google' AS canal, id_campanha, impressoes, cliques, gasto FROM raw_google_campanhas
        UNION ALL
        SELECT data, 'facebook' AS canal, id_campanha, impressoes, cliques, gasto FROM raw_meta_campanhas
    """)

    con.execute("""
        CREATE TABLE DW.fact_assinaturas AS
        SELECT id_evento, id_cliente, id_produto, data_evento, tipo_evento, mrr_novo FROM raw_erp_assinaturas
    """)

    # 3. Extract Data for Dashboard
    # Funnel and Channel Data
    marketing = con.execute("""
        SELECT canal, SUM(cliques) as cliques, SUM(gasto) as gasto
        FROM DW.fact_marketing_top_funnel
        GROUP BY 1
    """).df().to_dict(orient='records')
    
    crm = con.execute("""
        SELECT canal_aquisicao as canal, COUNT(id_lead) as leads, COUNT(id_cliente) as conversions
        FROM DW.dim_clientes
        GROUP BY 1
    """).df().to_dict(orient='records')
    
    # 2. Cohort Data (Pre-calculated in DuckDB)
    cohort_data = con.execute("""
        WITH Cohort_Inicial AS (
            SELECT 
                a.id_cliente, 
                MIN(date_trunc('month', a.data_evento::DATE)) as mes_cohort,
                c.canal_aquisicao as canal
            FROM DW.fact_assinaturas a
            JOIN DW.dim_clientes c ON a.id_cliente = c.id_cliente
            WHERE a.tipo_evento = 'Criação'
            GROUP BY 1, 3
        ),
        Tamanho_Cohort AS (
            SELECT 
                mes_cohort, 
                canal,
                COUNT(DISTINCT id_cliente) as total_clientes_cohort
            FROM Cohort_Inicial
            GROUP BY 1, 2
        ),
        Atividade_Mensal AS (
            SELECT 
                ci.id_cliente,
                ci.mes_cohort,
                ci.canal,
                date_diff('month', ci.mes_cohort, date_trunc('month', a.data_evento::DATE)) as month_index
            FROM DW.fact_assinaturas a
            JOIN Cohort_Inicial ci ON a.id_cliente = ci.id_cliente
        ),
        Retencao_Absoluta AS (
            SELECT 
                mes_cohort,
                canal,
                month_index,
                COUNT(DISTINCT id_cliente) as clientes_retidos
            FROM Atividade_Mensal
            WHERE month_index >= 0
            GROUP BY 1, 2, 3
        )
        SELECT 
            strftime(ra.mes_cohort, '%Y-%m') as cohort_month,
            ra.canal,
            ra.month_index,
            ra.clientes_retidos,
            tc.total_clientes_cohort,
            (ra.clientes_retidos * 100.0) / tc.total_clientes_cohort as retention_pct
        FROM Retencao_Absoluta ra
        JOIN Tamanho_Cohort tc ON ra.mes_cohort = tc.mes_cohort AND ra.canal = tc.canal
        ORDER BY cohort_month, ra.canal, ra.month_index
    """).df().to_dict(orient='records')

    # Tickets and Sentiment
    tickets = con.execute("""
        SELECT 
            c.canal_aquisicao as canal,
            t.categoria,
            AVG(t.satisfacao_csat) as avg_csat,
            COUNT(t.id_ticket) as ticket_count
        FROM raw_suporte t
        JOIN DW.dim_clientes c ON t.id_cliente = c.id_cliente
        GROUP BY 1, 2
    """).df().to_dict(orient='records')
    
    # KPIs
    kpis = con.execute("""
        SELECT 
            (SELECT SUM(mrr_novo) FROM DW.fact_assinaturas WHERE tipo_evento != 'Cancelamento' AND data_evento >= '2025-07-01') as total_mrr,
            (SELECT COUNT(*) FROM DW.fact_assinaturas WHERE tipo_evento = 'Cancelamento') as total_churns,
            (SELECT COUNT(DISTINCT id_cliente) FROM DW.fact_assinaturas) as total_customers,
            (SELECT SUM(gasto) FROM DW.fact_marketing_top_funnel) as total_spend
    """).df().to_dict(orient='records')[0]

    # Time Series for Sparklines
    mrr_series = con.execute("""
        SELECT strftime(date_trunc('month', data_evento::DATE), '%Y-%m') as mes, 
               SUM(CASE WHEN tipo_evento != 'Cancelamento' THEN mrr_novo ELSE -mrr_novo END) as value
        FROM DW.fact_assinaturas
        GROUP BY 1 ORDER BY 1
    """).df().to_dict(orient='records')

    cac_series = con.execute("""
        WITH MonthlySpend AS (
            SELECT date_trunc('month', data::DATE) as mes, SUM(gasto) as gasto
            FROM DW.fact_marketing_top_funnel
            GROUP BY 1
        ),
        MonthlyConversions AS (
            SELECT date_trunc('month', data_evento::DATE) as mes, COUNT(DISTINCT id_cliente) as new_customers
            FROM DW.fact_assinaturas
            WHERE tipo_evento = 'Criação'
            GROUP BY 1
        )
        SELECT strftime(s.mes, '%Y-%m') as mes, s.gasto / c.new_customers as value
        FROM MonthlySpend s
        JOIN MonthlyConversions c ON s.mes = c.mes
        ORDER BY 1
    """).df().to_dict(orient='records')
    
    churn_series = con.execute("""
        SELECT strftime(date_trunc('month', data_evento::DATE), '%Y-%m') as mes,
               (COUNT(CASE WHEN tipo_evento = 'Cancelamento' THEN 1 END) * 1.0 / COUNT(DISTINCT id_cliente)) as value
        FROM DW.fact_assinaturas
        GROUP BY 1 ORDER BY 1
    """).df().to_dict(orient='records')
    
    data = {
        "marketing": marketing,
        "crm": crm,
        "cohort": cohort_data,
        "tickets": tickets,
        "kpis": kpis,
        "series": {
            "mrr": mrr_series,
            "cac": cac_series,
            "churn": churn_series
        }
    }
    
    with open('dashboard_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Data extracted to dashboard_data.json using in-memory DuckDB")

if __name__ == "__main__":
    extract_data()
