"""
BI Class — Synthetic Data Generator
Generates 12 CSV files simulating a full SaaS sales funnel.
Covers: Ads → CRM → ERP → Subscriptions → Engagement → Support → Reviews
Enables KPIs: NPS, Sentiment, Churn, MRR, ROAS, LTV, CAC
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import random
import os
import math

# ─── Seed & Output ────────────────────────────────────────────────────────────
SEED = 42
random.seed(SEED)
np.random.seed(SEED)

START_DATE = datetime(2025, 1, 1)
END_DATE   = datetime(2025, 12, 31)
OUTPUT_DIR = "data/bi_class"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save(df, name):
    path = os.path.join(OUTPUT_DIR, name)
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"  OK {name:40s} {len(df):>6} rows")

def rand_date(start=START_DATE, end=END_DATE):
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, delta))

def fmt_date(d):  return d.strftime("%Y-%m-%d")
def fmt_dt(d):    return d.strftime("%Y-%m-%d %H:%M:%S")

# ─── 1. PRODUCTS (static catalog) ─────────────────────────────────────────────
PRODUCTS = [
    # id, nome, categoria, subcategoria, plano, preco, custo, recorrente, periodo, data_lanc
    ("PROD-001","Plano Mensal Starter","SaaS","Assinatura","Starter",  297.0,  45.0,1,"Mensal","2023-01-15"),
    ("PROD-002","Plano Mensal Pro",    "SaaS","Assinatura","Pro",      697.0,  95.0,1,"Mensal","2023-01-15"),
    ("PROD-003","Plano Mensal Ent.",   "SaaS","Assinatura","Enterprise",1497.0,180.0,1,"Mensal","2023-06-01"),
    ("PROD-004","Plano Anual Starter", "SaaS","Assinatura","Starter", 2970.0, 400.0,1,"Anual", "2023-03-01"),
    ("PROD-005","Plano Anual Pro",     "SaaS","Assinatura","Pro",     6970.0, 850.0,1,"Anual", "2023-03-01"),
    ("PROD-006","Plano Anual Ent.",    "SaaS","Assinatura","Enterprise",14970.0,1600.0,1,"Anual","2023-07-01"),
    ("PROD-007","Consultoria Setup",   "Consultoria","Avulso","Avulso",1500.0, 300.0,0,None,   "2023-01-15"),
    ("PROD-008","Treinamento Online",  "Curso","Avulso","Avulso",      497.0,  50.0,0,None,   "2023-04-01"),
    ("PROD-009","Treinamento InCompany","Curso","Avulso","Avulso",    3500.0, 700.0,0,None,   "2023-09-01"),
    ("PROD-010","Licença Extra Seat",  "SaaS","Add-on","Avulso",       97.0,  10.0,1,"Mensal","2024-01-01"),
    ("PROD-011","Suporte Premium",     "Suporte","Add-on","Avulso",   197.0,  20.0,1,"Mensal","2024-03-01"),
    ("PROD-012","Migração de Dados",   "Consultoria","Avulso","Avulso",2500.0,500.0,0,None,   "2024-06-01"),
]

prod_rows = []
for p in PRODUCTS:
    pid,nome,cat,sub,plano,preco,custo,rec,periodo,lanc = p
    margem = round((preco - custo) / preco, 3)
    prod_rows.append({
        "id_produto":pid,"nome_produto":nome,"categoria":cat,"subcategoria":sub,
        "plano":plano,"preco_venda":preco,"custo_produto":custo,"margem_bruta":margem,
        "recorrente":rec,"periodo_recorrencia":periodo,"ativo":1,"data_lancamento":lanc
    })
df_prod = pd.DataFrame(prod_rows)
save(df_prod, "erp_produtos.csv")
PROD_MAP = {p[0]: p for p in PRODUCTS}

# ─── 2. META ADS (daily × ad set × ad) ────────────────────────────────────────
META_CAMPAIGNS = [
    ("META-CAMP-001","Prospecção_Q1_Empreendedores","Lead Gen",
     datetime(2025,1,1),datetime(2025,3,31),"prospeccao_q1_empreendedores"),
    ("META-CAMP-002","Prospecção_Q2_Gestores","Lead Gen",
     datetime(2025,4,1),datetime(2025,6,30),"prospeccao_q2_gestores"),
    ("META-CAMP-003","Remarketing_Visitantes","Conversions",
     datetime(2025,1,1),datetime(2025,12,31),"remarketing_visitantes"),
    ("META-CAMP-004","Brand_Awareness_Q3","Awareness",
     datetime(2025,7,1),datetime(2025,9,30),"brand_awareness_q3"),
    ("META-CAMP-005","Black_Friday_Promo","Conversions",
     datetime(2025,11,1),datetime(2025,11,30),"black_friday_promo"),
]

META_ADSETS = {
    "META-CAMP-001": [("META-SET-001","Interesse_Empreendedores_SP"),("META-SET-002","Lookalike_2pct_Clientes")],
    "META-CAMP-002": [("META-SET-003","Gestores_RH_Brasil"),("META-SET-004","Interesse_Analytics_Sul")],
    "META-CAMP-003": [("META-SET-005","Remarketing_7d")],
    "META-CAMP-004": [("META-SET-006","Brand_BR_25_55")],
    "META-CAMP-005": [("META-SET-007","BF_LeadNurturing"),("META-SET-008","BF_Aquisicao_Nova")],
}

META_ADS_MAP = {
    "META-SET-001":[("META-AD-001","Video_Depoimento_Ana_30s","Video","Instagram"),
                    ("META-AD-002","Carrossel_3Beneficios","Carousel","Facebook")],
    "META-SET-002":[("META-AD-003","Video_CaseEmpresa_60s","Video","Instagram")],
    "META-SET-003":[("META-AD-004","Image_Desconto20_Stories","Stories","Instagram")],
    "META-SET-004":[("META-AD-005","Video_Brand_15s","Video","Facebook")],
    "META-SET-005":[("META-AD-006","Image_Remarketing_Banner","Image","Facebook")],
    "META-SET-006":[("META-AD-007","Reels_BrandStory_30s","Video","Instagram")],
    "META-SET-007":[("META-AD-008","BF_Video_50off","Video","Instagram")],
    "META-SET-008":[("META-AD-009","BF_Carrossel_Planos","Carousel","Facebook")],
}

meta_rows = []
for camp_id, camp_nome, obj, camp_start, camp_end, utm_camp in META_CAMPAIGNS:
    current = camp_start
    while current <= min(camp_end, END_DATE):
        for set_id, set_nome in META_ADSETS[camp_id]:
            for ad_id, ad_nome, fmt, plat in META_ADS_MAP.get(set_id, []):
                month = current.month
                # Seasonality: Q4 boost, July/Aug Brazil dip
                spend_mult = 1.0
                if month in [11, 12]: spend_mult = 1.6
                elif month in [7, 8]: spend_mult = 0.7
                if camp_id == "META-CAMP-005": spend_mult = 2.2

                base_gasto = random.uniform(120, 400) * spend_mult
                impressoes  = int(base_gasto * random.uniform(90, 130))
                alcance     = int(impressoes * random.uniform(0.78, 0.88))
                cliques     = int(impressoes * random.uniform(0.015, 0.025))
                cliques_link= int(cliques * random.uniform(0.78, 0.88))
                leads_meta  = int(cliques_link * random.uniform(0.04, 0.09)) if obj == "Lead Gen" else 0
                frequencia  = round(impressoes / max(alcance, 1), 2)
                ctr         = round(cliques / max(impressoes, 1) * 100, 2)
                cpc         = round(base_gasto / max(cliques, 1), 2)
                cpl         = round(base_gasto / max(leads_meta, 1), 2) if leads_meta > 0 else None

                meta_rows.append({
                    "data": fmt_date(current),
                    "id_campanha": camp_id, "nome_campanha": camp_nome,
                    "objetivo_campanha": obj,
                    "id_conjunto": set_id, "nome_conjunto": set_nome,
                    "id_anuncio": ad_id, "nome_anuncio": ad_nome,
                    "formato_anuncio": fmt, "plataforma": plat,
                    "impressoes": impressoes, "alcance": alcance,
                    "cliques": cliques, "cliques_link": cliques_link,
                    "leads_meta": leads_meta,
                    "gasto": round(base_gasto, 2),
                    "frequencia": frequencia, "ctr": ctr, "cpc": cpc, "cpl_meta": cpl,
                    "utm_source": "facebook", "utm_campaign": utm_camp,
                })
        current += timedelta(days=1)

df_meta = pd.DataFrame(meta_rows)
save(df_meta, "meta_campanhas.csv")

# ─── 3. GOOGLE ADS (daily × ad group) ─────────────────────────────────────────
GOOGLE_CAMPAIGNS = [
    ("GADS-CAMP-001","Search_Marca_Q1","Search",datetime(2025,1,1),datetime(2025,12,31),"search_marca"),
    ("GADS-CAMP-002","Search_Generico_Dados","Search",datetime(2025,1,1),datetime(2025,12,31),"search_generico_dados"),
    ("GADS-CAMP-003","Display_Remarketing","Display",datetime(2025,3,1),datetime(2025,12,31),"display_remarketing"),
    ("GADS-CAMP-004","YouTube_Prospeccao","YouTube",datetime(2025,6,1),datetime(2025,9,30),"youtube_prospeccao"),
]

GOOGLE_GROUPS = {
    "GADS-CAMP-001":[("GADS-GRP-001","Marca_Exata",["planilha dados empresa","consultoria dados sp","analise dados negocio"]),
                     ("GADS-GRP-002","Marca_Ampla",["dados empresa","consultoria business intelligence"])],
    "GADS-CAMP-002":[("GADS-GRP-003","BI_Ferramentas",["ferramenta bi","software business intelligence","dashboard dados"]),
                     ("GADS-GRP-004","EDA_Analytics",["analise exploratoria dados","relatorio executivo automatico"])],
    "GADS-CAMP-003":[("GADS-GRP-005","Remarketing_All",[""])],
    "GADS-CAMP-004":[("GADS-GRP-006","YouTube_Gestores",[""])],
}

GOOGLE_ADS_MAP = {
    "GADS-GRP-001":[("GADS-AD-001","RSA_Marca_v2","Frase")],
    "GADS-GRP-002":[("GADS-AD-002","RSA_Marca_Ampla","Ampla")],
    "GADS-GRP-003":[("GADS-AD-003","RSA_BI_v1","Frase"),("GADS-AD-004","RSA_BI_v2","Exata")],
    "GADS-GRP-004":[("GADS-AD-005","RSA_EDA_v1","Frase")],
    "GADS-GRP-005":[("GADS-AD-006","Display_Banner_300x250","None")],
    "GADS-GRP-006":[("GADS-AD-007","YouTube_InStream_30s","None")],
}

gads_rows = []
for camp_id, camp_nome, tipo, camp_start, camp_end, utm_camp in GOOGLE_CAMPAIGNS:
    current = camp_start
    while current <= min(camp_end, END_DATE):
        month = current.month
        spend_mult = 1.0
        if month in [11, 12]: spend_mult = 1.5
        elif month in [7, 8]:  spend_mult = 0.75

        for grp_id, grp_nome, keywords in GOOGLE_GROUPS[camp_id]:
            for ad_id, ad_nome, match in GOOGLE_ADS_MAP.get(grp_id, []):
                kw = random.choice(keywords) if keywords and keywords[0] else ""
                base_gasto  = random.uniform(80, 280) * spend_mult
                impressoes  = int(base_gasto * random.uniform(30, 55))
                cliques     = int(impressoes * random.uniform(0.04, 0.08))
                conversoes  = int(cliques * random.uniform(0.03, 0.06))
                posicao     = round(random.uniform(1.2, 3.0), 1)
                ctr         = round(cliques / max(impressoes, 1) * 100, 2)
                cpc         = round(base_gasto / max(cliques, 1), 2)
                cpa         = round(base_gasto / max(conversoes, 1), 2) if conversoes > 0 else None
                roas        = round(random.uniform(1.8, 5.5), 2) if tipo == "Search" else None

                gads_rows.append({
                    "data": fmt_date(current),
                    "id_campanha": camp_id, "nome_campanha": camp_nome,
                    "tipo_campanha": tipo,
                    "id_grupo": grp_id, "nome_grupo": grp_nome,
                    "id_anuncio": ad_id, "nome_anuncio": ad_nome,
                    "palavra_chave": kw, "tipo_correspondencia": match,
                    "posicao_media": posicao, "impressoes": impressoes,
                    "cliques": cliques, "conversoes": conversoes,
                    "gasto": round(base_gasto, 2),
                    "ctr": ctr, "cpc": cpc, "cpa": cpa, "roas": roas,
                    "utm_source": "google", "utm_campaign": utm_camp,
                })
        current += timedelta(days=1)

df_gads = pd.DataFrame(gads_rows)
save(df_gads, "google_campanhas.csv")

# ─── 4. CRM LEADS ─────────────────────────────────────────────────────────────
PRIMEIROS_NOMES = ["Ana","Carlos","Fernanda","Rafael","Mariana","Lucas","Juliana","Pedro","Camila","Thiago",
                   "Patricia","Rodrigo","Beatriz","Felipe","Amanda","Gustavo","Leticia","Bruno","Natalia","Diego"]
SOBRENOMES = ["Silva","Santos","Oliveira","Souza","Lima","Costa","Ferreira","Rodrigues","Alves","Pereira",
              "Gomes","Martins","Carvalho","Rocha","Araújo","Mendes","Barros","Freitas","Nunes","Moreira"]
EMPRESAS_SUFIXO = ["Ltda","S.A.","ME","EIRELI","Consultoria","Soluções","Tecnologia","Serviços","Comércio","Group"]
SETORES  = ["Varejo","Serviços Financeiros","Saúde","Educação","Logística","TI","RH","Marketing","Manufatura","Agro"]
CARGOS   = ["Gerente de Marketing","Coordenador de Operações","Analista de BI","Diretor Comercial",
            "CEO","CFO","Head de Dados","Analista de Marketing","Gerente Comercial","Controller"]
UFS      = ["SP","RJ","MG","RS","PR","SC","BA","PE","GO","DF"]
TAMANHOS = ["MEI","Pequena","Média","Grande"]
CANAIS   = ["Meta","Google","Orgânico","Indicação","Email"]
CANAL_W  = [0.40, 0.28, 0.14, 0.11, 0.07]
PAGINAS  = ["/lp-analise-dados","/lp-bi-executivo","/lp-dashboard-rapido","/home","/pricing"]
MOTIVOS_DISQ = ["Sem orçamento","Sem fit de negócio","Sem urgência","Processo longo de decisão",None]

UTM_MAP = {
    "Meta":   ("facebook","paid_social"),
    "Google": ("google","cpc"),
    "Orgânico":("organic",None),
    "Indicação":("referral",None),
    "Email":  ("email","email"),
}
META_UTM_CAMPS  = ["prospeccao_q1_empreendedores","prospeccao_q2_gestores","remarketing_visitantes","black_friday_promo"]
GOOGLE_UTM_CAMPS= ["search_marca","search_generico_dados","display_remarketing"]

N_LEADS = 1000
leads = []
for i in range(N_LEADS):
    lead_id = f"LEAD-{i+1:05d}"
    nome = f"{random.choice(PRIMEIROS_NOMES)} {random.choice(SOBRENOMES)}"
    empresa_nome = f"{random.choice(SOBRENOMES)} {random.choice(EMPRESAS_SUFIXO)}"
    canal = random.choices(CANAIS, weights=CANAL_W)[0]
    utm_src, utm_med = UTM_MAP[canal]
    if canal == "Meta":    utm_camp = random.choice(META_UTM_CAMPS)
    elif canal == "Google": utm_camp = random.choice(GOOGLE_UTM_CAMPS)
    else:                  utm_camp = None
    # Seasonality: fewer leads in July/Aug
    month_weights = [1.0,1.1,1.3,1.2,1.2,1.0,0.6,0.65,1.1,1.15,1.4,1.8]
    month = random.choices(range(1,13), weights=month_weights)[0]
    day = random.randint(1, 28)
    hour = random.randint(8, 20)
    dt_lead = datetime(2025, month, day, hour, random.randint(0,59), random.randint(0,59))

    # Lead scoring: Google search leads score higher
    base_score = 50
    if canal == "Google" and utm_camp and "marca" in utm_camp: base_score = 72
    elif canal == "Indicação": base_score = 78
    elif canal == "Meta":     base_score = 55
    score = min(100, max(10, base_score + random.randint(-20, 25)))

    status = "Novo"
    qual_date = None
    motivo_disq = None
    opp_id = None

    if score >= 50:
        q_prob = 0.55 if score >= 70 else 0.38
        if random.random() < q_prob:
            status = "Qualificado"
            qual_date = fmt_date(dt_lead + timedelta(days=random.randint(1, 7)))
        else:
            status = "Desqualificado"
            motivo_disq = random.choice(MOTIVOS_DISQ)
    else:
        status = random.choices(["Novo","Em Qualificação","Desqualificado"],weights=[0.3,0.4,0.3])[0]
        if status == "Desqualificado":
            motivo_disq = random.choice(MOTIVOS_DISQ)

    leads.append({
        "id_lead": lead_id,
        "data_criacao": fmt_dt(dt_lead),
        "nome": nome,
        "email": f"lead_{i+1:05d}@empresa-demo.com.br",
        "telefone": f"+55 {random.choice(['11','21','31','41','51'])} 9 {random.randint(8000,9999)}-{random.randint(1000,9999)}",
        "empresa": empresa_nome,
        "cargo": random.choice(CARGOS),
        "segmento": random.choice(SETORES),
        "tamanho_empresa": random.choices(TAMANHOS, weights=[0.15,0.40,0.30,0.15])[0],
        "uf": random.choices(UFS, weights=[0.35,0.18,0.12,0.08,0.07,0.06,0.05,0.04,0.03,0.02])[0],
        "canal_origem": canal,
        "utm_source": utm_src,
        "utm_campaign": utm_camp,
        "utm_medium": utm_med,
        "pagina_conversao": random.choice(PAGINAS),
        "status": status,
        "score_lead": score,
        "data_qualificacao": qual_date,
        "motivo_desqualificacao": motivo_disq,
        "id_oportunidade": None,  # filled later
    })

df_leads = pd.DataFrame(leads)

# ─── 5. CRM OPORTUNIDADES ─────────────────────────────────────────────────────
VENDEDORES  = ["Carlos Mendes","Patricia Rocha","Diego Alves","Juliana Costa","Rodrigo Lima"]
MOTIVOS_PERDA = ["Preço","Concorrência","Sem urgência","Orçamento cortado","Escolheu solução interna"]
PRODS_INTERESSE = ["Plano Mensal Starter","Plano Mensal Pro","Plano Anual Pro","Plano Anual Ent.","Consultoria Setup"]

opps = []
client_counter = 0
qual_leads = [l for l in leads if l["status"] == "Qualificado"]

for lead in qual_leads:
    if random.random() > 0.95:  # ~5% slip through without opportunity
        continue
    opp_id = f"OPP-{len(opps)+1:05d}"
    lead["id_oportunidade"] = opp_id
    lead["status"] = "Convertido" if random.random() < 0.43 else "Qualificado"

    dt_lead = datetime.strptime(lead["data_criacao"], "%Y-%m-%d %H:%M:%S")
    dt_open = dt_lead + timedelta(days=random.randint(1, 5))
    if dt_open > END_DATE: dt_open = END_DATE - timedelta(days=10)

    dias_funil = random.randint(7, 45)
    dt_close = dt_open + timedelta(days=dias_funil)
    if dt_close > END_DATE: dt_close = END_DATE

    estagio_final = "Fechado Ganho" if lead["status"] == "Convertido" else \
        random.choices(["Fechado Perdido","Proposta","Negociação"], weights=[0.6,0.25,0.15])[0]

    prod_int = random.choice(PRODS_INTERESSE)
    valor_est = {"Plano Mensal Starter":3564,"Plano Mensal Pro":8364,"Plano Anual Pro":6970,
                 "Plano Anual Ent.":14970,"Consultoria Setup":1500}.get(prod_int, 2500)
    valor_est += random.randint(-500, 1500)
    valor_fechado = round(valor_est * random.uniform(0.88, 1.05), 2) if estagio_final == "Fechado Ganho" else None

    cli_id = None
    if estagio_final == "Fechado Ganho":
        client_counter += 1
        cli_id = f"CLI-{client_counter:05d}"

    opps.append({
        "id_oportunidade": opp_id,
        "id_lead": lead["id_lead"],
        "data_abertura": fmt_date(dt_open),
        "data_fechamento": fmt_date(dt_close),
        "estagio": estagio_final,
        "valor_estimado": round(valor_est, 2),
        "valor_fechado": valor_fechado,
        "probabilidade": 100 if estagio_final == "Fechado Ganho" else random.randint(10, 70),
        "produto_interesse": prod_int,
        "responsavel": random.choice(VENDEDORES),
        "numero_interacoes": random.randint(2, 10),
        "dias_no_funil": dias_funil,
        "motivo_perda": random.choice(MOTIVOS_PERDA) if estagio_final == "Fechado Perdido" else None,
        "id_cliente": cli_id,
    })

df_leads = pd.DataFrame(leads)
save(df_leads, "crm_leads.csv")
df_opps = pd.DataFrame(opps)
save(df_opps, "crm_oportunidades.csv")

# ─── CLIENT LIST ──────────────────────────────────────────────────────────────
won_opps = [o for o in opps if o["estagio"] == "Fechado Ganho"]
CLIENTES = []  # list of dicts with client data

for opp in won_opps:
    lead = next((l for l in leads if l["id_lead"] == opp["id_lead"]), None)
    if not lead: continue
    churn = random.random() < 0.18
    dt_first = datetime.strptime(opp["data_fechamento"], "%Y-%m-%d")
    dt_churn  = None
    status_cli = "Ativo"
    if churn and (END_DATE - dt_first).days > 60:
        months_before_churn = random.randint(2, min(8, ((END_DATE - dt_first).days // 30)))
        dt_churn = dt_first + timedelta(days=months_before_churn * 30)
        if dt_churn <= END_DATE:
            status_cli = "Churned"
        else:
            dt_churn = None
    n_orders = random.randint(1, 5) if not churn else random.randint(1, 2)
    receita_total = round(opp["valor_fechado"] * n_orders * random.uniform(0.8, 1.2), 2)
    dt_last = dt_first + timedelta(days=random.randint(30, 300))
    if dt_churn: dt_last = min(dt_churn, dt_last)
    if dt_last > END_DATE: dt_last = END_DATE

    CLIENTES.append({
        "id_cliente": opp["id_cliente"],
        "id_lead": lead["id_lead"],
        "nome": lead["empresa"],
        "tipo": "PJ" if "Ltda" in lead["empresa"] or "S.A." in lead["empresa"] else "PF",
        "segmento": lead["segmento"],
        "uf": lead["uf"],
        "canal_aquisicao": lead["canal_origem"],
        "data_primeira_compra": fmt_date(dt_first),
        "data_ultima_compra": fmt_date(dt_last),
        "total_pedidos": n_orders,
        "receita_total": receita_total,
        "status_cliente": status_cli,
        "data_churn": fmt_date(dt_churn) if dt_churn else None,
        # internal helpers
        "_dt_first": dt_first,
        "_dt_churn": dt_churn,
        "_churn": churn,
        "_canal": lead["canal_origem"],
        "_utm": lead["utm_campaign"],
    })

df_clientes_out = pd.DataFrame(CLIENTES).drop(columns=["_dt_first","_dt_churn","_churn","_canal","_utm"])
save(df_clientes_out, "erp_clientes.csv")

# ─── 6. ERP PEDIDOS + ITENS ───────────────────────────────────────────────────
RECURRING_PRODS = [p for p in PRODUCTS if p[8] is not None]  # has recorrencia
ONETIME_PRODS   = [p for p in PRODUCTS if p[8] is None]
CANAIS_VENDA    = ["Site","App","WhatsApp","Inside Sales"]
FORMAS_PAG      = ["Cartão","PIX","Boleto","Transferência"]
CUPONS          = [None,None,None,"PROMO10","PROMO20","BLACKFRIDAY30","PARCEIRO15"]

orders, order_items = [], []
ped_counter, item_counter = 0, 0

for cli in CLIENTES:
    dt_first = cli["_dt_first"]
    dt_churn = cli["_dt_churn"]
    n_orders = cli["total_pedidos"]

    for j in range(n_orders):
        ped_counter += 1
        ped_id = f"PED-{ped_counter:06d}"
        dt_ped = dt_first + timedelta(days=j * random.randint(25, 90) + random.randint(0, 15))
        if dt_churn and dt_ped > dt_churn: break
        if dt_ped > END_DATE: break

        prod = random.choice(RECURRING_PRODS if j == 0 else PRODUCTS)
        pid, _, _, _, _, preco, custo, _, _, _ = prod
        cupom   = random.choice(CUPONS)
        desconto = 0.0
        if cupom:
            pct = {"PROMO10":0.10,"PROMO20":0.20,"BLACKFRIDAY30":0.30,"PARCEIRO15":0.15}.get(cupom, 0)
            desconto = round(preco * pct, 2)
        val_liq = round(preco - desconto, 2)
        margem  = round((val_liq - custo) / max(val_liq, 1), 3)
        status  = random.choices(["Entregue","Entregue","Entregue","Cancelado","Reembolsado"],
                                  weights=[0.88,0.88,0.88,0.07,0.05])[0]

        orders.append({
            "id_pedido": ped_id, "id_cliente": cli["id_cliente"],
            "data_pedido": fmt_dt(dt_ped + timedelta(hours=random.randint(8,20),minutes=random.randint(0,59))),
            "canal_venda": random.choice(CANAIS_VENDA),
            "status_pedido": status,
            "valor_bruto": preco, "desconto": desconto, "valor_liquido": val_liq,
            "custo_total": custo, "margem_pedido": margem,
            "forma_pagamento": random.choice(FORMAS_PAG),
            "parcelas": random.choices([1,2,3,6,12], weights=[0.35,0.2,0.2,0.15,0.1])[0],
            "cupom": cupom, "nf_emitida": 1,
            "_cli_id": cli["id_cliente"], "_dt": dt_ped, "_utm": cli["_utm"],
        })

        item_counter += 1
        order_items.append({
            "id_item": f"ITEM-{item_counter:06d}",
            "id_pedido": ped_id, "id_produto": pid,
            "quantidade": 1, "preco_unitario": preco,
            "custo_unitario": custo, "desconto_item": desconto,
            "valor_item": val_liq,
        })

df_orders = pd.DataFrame(orders).drop(columns=["_cli_id","_dt","_utm"])
save(df_orders, "erp_pedidos.csv")
df_items = pd.DataFrame(order_items)
save(df_items, "erp_itens_pedido.csv")

# ─── 7. ERP ASSINATURAS (subscription events for MRR/Churn) ──────────────────
MRR_MAP = {  # id_produto → monthly MRR value
    "PROD-001": 297.0, "PROD-002": 697.0, "PROD-003": 1497.0,
    "PROD-004": 247.5, "PROD-005": 580.8, "PROD-006": 1247.5,
    "PROD-010":  97.0, "PROD-011": 197.0,
}
PLANO_MAP = {"PROD-001":"Starter","PROD-002":"Pro","PROD-003":"Enterprise",
             "PROD-004":"Starter","PROD-005":"Pro","PROD-006":"Enterprise",
             "PROD-010":"Extra Seat","PROD-011":"Suporte Premium"}

sub_events, sub_counter = [], 0
for cli in CLIENTES:
    dt_first = cli["_dt_first"]
    dt_churn  = cli["_dt_churn"]
    # Pick the first recurring product order
    cli_orders = [o for o in orders if o.get("_cli_id","") == cli["id_cliente"]]  # already dropped
    # rebuild: find orders by id_cliente
    cli_ped_ids = [o["id_pedido"] for o in df_orders.to_dict('records') if o["id_cliente"] == cli["id_cliente"]]
    if not cli_ped_ids: continue
    first_item = next((it for it in order_items if it["id_pedido"] == cli_ped_ids[0]), None)
    if not first_item: continue
    pid = first_item["id_produto"]
    if pid not in MRR_MAP: continue

    plano = PLANO_MAP.get(pid, "Starter")
    mrr   = MRR_MAP[pid]

    # Criação
    sub_counter += 1
    sub_events.append({
        "id_evento": f"SUB-EVT-{sub_counter:05d}",
        "id_cliente": cli["id_cliente"], "id_produto": pid,
        "data_evento": fmt_date(dt_first),
        "tipo_evento": "Criação",
        "plano_anterior": None, "plano_novo": plano,
        "mrr_anterior": 0.0, "mrr_novo": mrr, "delta_mrr": mrr,
        "motivo": None,
        "periodo_contrato": "Anual" if pid in ["PROD-004","PROD-005","PROD-006"] else "Mensal",
        "data_inicio_periodo": fmt_date(dt_first),
        "data_fim_periodo": fmt_date(dt_first + timedelta(days=365 if pid in ["PROD-004","PROD-005","PROD-006"] else 30)),
    })

    # Possible upgrade (20% of non-churned clients)
    if not cli["_churn"] and random.random() < 0.20:
        upgrade_prods = {"PROD-001":"PROD-002","PROD-002":"PROD-003","PROD-004":"PROD-005","PROD-005":"PROD-006"}
        if pid in upgrade_prods:
            new_pid = upgrade_prods[pid]
            new_plano = PLANO_MAP[new_pid]
            new_mrr   = MRR_MAP[new_pid]
            dt_upgrade = dt_first + timedelta(days=random.randint(60, 180))
            if dt_upgrade <= END_DATE:
                sub_counter += 1
                sub_events.append({
                    "id_evento": f"SUB-EVT-{sub_counter:05d}",
                    "id_cliente": cli["id_cliente"], "id_produto": new_pid,
                    "data_evento": fmt_date(dt_upgrade),
                    "tipo_evento": "Upgrade",
                    "plano_anterior": plano, "plano_novo": new_plano,
                    "mrr_anterior": mrr, "mrr_novo": new_mrr, "delta_mrr": round(new_mrr - mrr, 2),
                    "motivo": None,
                    "periodo_contrato": "Mensal",
                    "data_inicio_periodo": fmt_date(dt_upgrade),
                    "data_fim_periodo": fmt_date(dt_upgrade + timedelta(days=30)),
                })

    # Cancellation event
    if cli["_churn"] and dt_churn:
        sub_counter += 1
        sub_events.append({
            "id_evento": f"SUB-EVT-{sub_counter:05d}",
            "id_cliente": cli["id_cliente"], "id_produto": pid,
            "data_evento": fmt_date(dt_churn),
            "tipo_evento": "Cancelamento",
            "plano_anterior": plano, "plano_novo": None,
            "mrr_anterior": mrr, "mrr_novo": 0.0, "delta_mrr": -mrr,
            "motivo": random.choice(["Falta de uso","Preço","Migração para concorrente","Crise financeira"]),
            "periodo_contrato": "Mensal",
            "data_inicio_periodo": fmt_date(dt_churn),
            "data_fim_periodo": fmt_date(dt_churn),
        })

df_subs = pd.DataFrame(sub_events)
save(df_subs, "erp_assinaturas.csv")

# ─── 8. ERP ENGAJAMENTO (monthly product usage — churn predictors) ────────────
eng_rows, eng_counter = [], 0
all_months = [f"2025-{m:02d}" for m in range(1, 13)]

for cli in CLIENTES:
    dt_first = cli["_dt_first"]
    dt_churn  = cli["_dt_churn"]
    is_churn  = cli["_churn"]

    baseline_logins = random.randint(8, 25)

    for ano_mes in all_months:
        yr, mo = int(ano_mes.split("-")[0]), int(ano_mes.split("-")[1])
        snapshot_start = datetime(yr, mo, 1)
        if snapshot_start < dt_first: continue
        if dt_churn and snapshot_start > dt_churn: continue

        # Decline pattern: 2 months before churn, engagement drops sharply
        decay = 1.0
        if is_churn and dt_churn:
            months_to_churn = ((dt_churn - snapshot_start).days) / 30
            if months_to_churn < 2:  decay = 0.25
            elif months_to_churn < 4: decay = 0.55
        
        # Seasonality: July/Aug lower engagement
        season = 0.75 if mo in [7, 8] else 1.0

        logins   = max(0, int(baseline_logins * decay * season + random.gauss(0, 2)))
        sessoes  = max(0, int(logins * random.uniform(1.2, 1.6)))
        horas    = round(max(0, logins * random.uniform(0.5, 0.9) * decay), 1)
        dash     = max(0, int(logins * 0.15 * decay + random.gauss(0, 0.5)))
        relatorios = max(0, int(logins * 0.35 * decay + random.gauss(0, 1)))
        users    = random.choices([1,2,3,4,5], weights=[0.4,0.3,0.15,0.1,0.05])[0]
        features = max(1, int(8 * decay * season + random.gauss(0, 1.5)))

        # Engagement score
        score = min(100, max(0, round(
            (logins/20 * 30) + (horas/15 * 25) + (relatorios/8 * 25) + (features/10 * 20), 1
        )))
        alerta = 1 if score < 30 else 0

        eng_counter += 1
        eng_rows.append({
            "id_engajamento": f"ENG-{eng_counter:06d}",
            "id_cliente": cli["id_cliente"],
            "ano_mes": ano_mes,
            "logins": logins, "sessoes": sessoes, "tempo_uso_horas": horas,
            "dashboards_criados": dash, "relatorios_exportados": relatorios,
            "usuarios_ativos": users, "features_usadas": min(features, 12),
            "score_engajamento": score, "alerta_churn": alerta,
        })

df_eng = pd.DataFrame(eng_rows)
save(df_eng, "erp_engajamento.csv")

# ─── 9. SUPPORT TICKETS ────────────────────────────────────────────────────────
AGENTES = ["Fernanda Lima","Marcos Oliveira","Carla Santos","Pedro Rocha","Aline Costa"]
CATEGORIAS = ["Cobrança","Acesso","Bug","Dúvida","Cancelamento"]
CANAIS_SUP  = ["Email","Chat","WhatsApp","Telefone"]
PRIORIDADES = ["Baixa","Média","Alta","Urgente"]

TICKET_DESCRICOES = {
    "Acesso": {
        "Positivo": ["Não consigo logar mas foi resolvido rápido","Perdi a senha, suporte ajudou em minutos"],
        "Negativo": ["Estou sem acesso há 3 dias e ninguém resolve","Sistema trava toda vez que tento entrar! Inaceitável"],
        "Neutro":   ["Preciso redefinir minha senha","Usuário novo não consegue acessar"],
    },
    "Cobrança": {
        "Positivo": ["Fui cobrado mas o estorno foi rápido e eficiente","Ajuste de fatura feito sem burocracia"],
        "Negativo": ["Fui cobrado duas vezes e ninguém me deu retorno","Reembolso prometido há 30 dias e não veio"],
        "Neutro":   ["Preciso de nota fiscal atualizada","Dúvida sobre próximo vencimento"],
    },
    "Bug": {
        "Positivo": ["Bug no relatório foi corrigido no mesmo dia, ótimo suporte"],
        "Negativo": ["Dashboard não carrega há uma semana, perdi reunião por isso","Sistema com muitos erros, estou pensando em cancelar"],
        "Neutro":   ["Gráfico não está exibindo corretamente","Exportação de PDF com formatação errada"],
    },
    "Dúvida": {
        "Positivo": ["Explicação clara e objetiva, resolvi em 5 minutos","Suporte muito atencioso e paciente"],
        "Negativo": ["Só respostas automáticas, ninguém realmente ajuda","Esperei 2 horas no chat sem resposta"],
        "Neutro":   ["Como faço para criar um dashboard compartilhável?","É possível integrar com Google Sheets?"],
    },
    "Cancelamento": {
        "Negativo": ["Quero cancelar minha assinatura, preço muito alto","O produto não entregou o que promete, quero reembolso"],
        "Neutro":   ["Vou pausar a assinatura temporariamente","Empresa passou por reestruturação, preciso cancelar"],
    },
}

CSAT_COMENTARIOS = {
    "Positivo": ["Excelente atendimento!","Resolvido rapidinho, obrigado","Muito profissional e eficiente",
                 "Melhor suporte que já tive","Atenção e agilidade impecáveis"],
    "Neutro":   ["Ok, resolvido","Demorou um pouco mas ok","Poderia ser mais rápido","Atendimento razoável"],
    "Negativo": ["Demorou demais para resolver","Não fiquei satisfeito","Precisei ligar 3 vezes",
                 "Problema não foi totalmente resolvido","Péssima experiência"],
}

tickets, ticket_counter = [], 0
client_pedidos = {o["id_cliente"]: o["id_pedido"] for o in df_orders.to_dict('records')}

for cli in CLIENTES:
    is_churn = cli["_churn"]
    dt_first = cli["_dt_first"]
    dt_churn  = cli["_dt_churn"]
    n_tickets = random.randint(3, 7) if is_churn else random.randint(1, 4)

    for _ in range(n_tickets):
        ticket_counter += 1
        cat = random.choice(CATEGORIAS)
        if is_churn and dt_churn:
            # Churn clients have more tickets near churn date
            dt_ticket = dt_churn - timedelta(days=random.randint(0, 60))
            if random.random() < 0.5: cat = random.choice(["Cancelamento","Bug","Acesso"])
        else:
            dt_ticket = dt_first + timedelta(days=random.randint(5, 300))
        
        if dt_ticket < dt_first: dt_ticket = dt_first + timedelta(days=3)
        if dt_ticket > END_DATE: dt_ticket = END_DATE

        pri = random.choices(PRIORIDADES, weights=[0.35,0.40,0.18,0.07])[0]
        if cat == "Cancelamento": pri = random.choice(["Alta","Urgente"])

        # Determine sentiment based on churn status and category
        if is_churn and cat in ["Cancelamento","Bug"]:
            sent = "Negativo"
        elif is_churn and random.random() < 0.6:
            sent = "Negativo"
        elif cat == "Dúvida" and random.random() < 0.7:
            sent = random.choice(["Positivo","Neutro"])
        else:
            sent = random.choices(["Positivo","Neutro","Negativo"], weights=[0.45,0.30,0.25])[0]

        cat_texts = TICKET_DESCRICOES.get(cat, TICKET_DESCRICOES["Dúvida"])
        descricao = random.choice(cat_texts.get(sent, cat_texts.get("Neutro", ["Problema reportado."])))

        # Resolution times (negative sentiment → worse service OR vice versa)
        if sent == "Negativo":
            t1_resp = random.randint(60, 480)
            t_resol = round(random.uniform(8, 48), 2)
            fcr = 0
            csat = random.randint(1, 3)
        elif sent == "Positivo":
            t1_resp = random.randint(5, 60)
            t_resol = round(random.uniform(0.5, 6), 2)
            fcr = 1 if random.random() < 0.75 else 0
            csat = random.randint(4, 5)
        else:
            t1_resp = random.randint(30, 120)
            t_resol = round(random.uniform(2, 12), 2)
            fcr = 1 if random.random() < 0.45 else 0
            csat = random.randint(3, 4)

        dt_resp = dt_ticket + timedelta(minutes=t1_resp)
        dt_resol= dt_ticket + timedelta(hours=t_resol)
        ped_id  = client_pedidos.get(cli["id_cliente"])

        tickets.append({
            "id_ticket": f"TKT-{ticket_counter:06d}",
            "id_cliente": cli["id_cliente"],
            "id_pedido": ped_id,
            "data_abertura": fmt_dt(dt_ticket),
            "data_primeira_resposta": fmt_dt(dt_resp),
            "data_resolucao": fmt_dt(dt_resol),
            "canal": random.choice(CANAIS_SUP),
            "categoria": cat, "prioridade": pri,
            "status": "Fechado",
            "agente": random.choice(AGENTES),
            "descricao_ticket": descricao,
            "resolvido_primeiro_contato": fcr,
            "tempo_primeira_resposta_min": t1_resp,
            "tempo_resolucao_horas": t_resol,
            "satisfacao_csat": csat,
            "comentario_csat": random.choice(CSAT_COMENTARIOS[sent]),
            "sentimento_label": sent,
        })

df_tickets = pd.DataFrame(tickets)
save(df_tickets, "suporte_tickets.csv")

# ─── 10. AVALIAÇÕES + NPS ─────────────────────────────────────────────────────
NPS_TEXTS = {
    "Promotor": {
        "titulos":  ["Transformou minha rotina de análise","Vale cada centavo","Recomendo sem hesitar",
                     "Melhor investimento do ano","Dados que contam histórias"],
        "textos": [
            "Consegui fazer meu primeiro dashboard em menos de uma hora. Mostrei para a diretoria e foi aprovado na hora.",
            "Antes eu ficava horas no Excel tentando entender os números. Agora em 20 minutos tenho tudo pronto.",
            "O suporte é excepcional e o produto entrega exatamente o que promete. Renovei por mais um ano sem pensar.",
            "Já recomendei para 3 colegas. A facilidade de uso é impressionante para quem não tem formação técnica.",
            "Finalmente consegui provar para o meu diretor onde estavam as ineficiências do processo. Gerou R$50k de economia.",
        ],
        "sentimento": "Positivo",
    },
    "Neutro": {
        "titulos":  ["Produto bom, falta polimento","Atende o básico","Em evolução","Bom mas pode melhorar"],
        "textos": [
            "Atende bem as necessidades básicas. Alguns recursos que esperava ainda não estão disponíveis.",
            "Interface poderia ser mais intuitiva. Levei um tempo para entender o fluxo. O suporte ajudou bastante.",
            "Produto está evoluindo. Esperando as funcionalidades prometidas para renovar com mais entusiasmo.",
            "Bom custo-benefício para o que oferece. Gostaria de mais templates prontos.",
        ],
        "sentimento": "Neutro",
    },
    "Detrator": {
        "titulos":  ["Não entregou o prometido","Experiência frustrante","Vou cancelar","Decepcionante"],
        "textos": [
            "Promessas na venda que o produto não cumpre. Suporte demora muito para responder.",
            "Tive muitos bugs que atrasaram meu trabalho. Não renovarei a assinatura.",
            "Prefiro voltar para o Excel. A plataforma é confusa e o suporte não resolve os problemas.",
            "Cobrado corretamente mas o produto parou de funcionar por dias sem aviso. Inaceitável.",
        ],
        "sentimento": "Negativo",
    },
}

rev_rows, rev_counter = [], 0

for cli in CLIENTES:
    if random.random() > 0.58: continue  # ~58% response rate
    rev_counter += 1
    is_churn = cli["_churn"]
    dt_first = cli["_dt_first"]

    # NPS biased by churn status
    if is_churn:
        nps = random.choices(list(range(11)), weights=[5,5,6,7,8,9,10,8,6,4,2])[0]
    else:
        nps = random.choices(list(range(11)), weights=[1,1,1,2,2,4,7,10,15,20,17])[0]

    cat_nps = "Promotor" if nps >= 9 else ("Neutro" if nps >= 7 else "Detrator")
    texts   = NPS_TEXTS[cat_nps]
    sentimento = texts["sentimento"]

    dt_rev = dt_first + timedelta(days=random.randint(10, 30))
    if dt_rev > END_DATE: dt_rev = END_DATE

    nota_prod = min(5, max(1, round(nps / 2 + random.gauss(0, 0.5))))
    nota_aten = min(5, max(1, round(nps / 2 + random.gauss(0, 0.8))))
    nota_cb   = min(5, max(1, round(nps / 2 + random.gauss(0, 0.6))))

    # Related order
    cli_peds = [o["id_pedido"] for o in df_orders.to_dict('records') if o["id_cliente"] == cli["id_cliente"]]
    ped_id = cli_peds[0] if cli_peds else None

    rev_rows.append({
        "id_avaliacao": f"REV-{rev_counter:06d}",
        "id_cliente": cli["id_cliente"],
        "id_pedido": ped_id,
        "data_avaliacao": fmt_date(dt_rev),
        "tipo": "NPS",
        "nota_nps": nps,
        "categoria_nps": cat_nps,
        "nota_produto": nota_prod,
        "nota_atendimento": nota_aten,
        "nota_custo_beneficio": nota_cb,
        "titulo_review": random.choice(texts["titulos"]),
        "texto_review": random.choice(texts["textos"]),
        "sentimento_label": sentimento,
        "recomendaria": 1 if nps >= 7 else 0,
        "plataforma": random.choices(["Email pós-compra","NPS In-App","Google Forms"],
                                      weights=[0.55,0.30,0.15])[0],
    })

df_rev = pd.DataFrame(rev_rows)
save(df_rev, "avaliacoes_clientes.csv")

# ─── SUMMARY ──────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  BI CLASS DATA GENERATION COMPLETE")
print("="*60)
total_rows = sum([len(df_prod),len(df_meta),len(df_gads),len(df_leads),len(df_opps),
                  len(df_clientes_out),len(df_orders),len(df_items),
                  len(df_subs),len(df_eng),len(df_tickets),len(df_rev)])
print(f"  Total rows across 12 files: {total_rows:,}")
# Quick sanity KPIs
n_clients  = len(CLIENTES)
n_churned  = sum(1 for c in CLIENTES if c["_churn"])
n_promotor = len([r for r in rev_rows if r["categoria_nps"]=="Promotor"])
n_detrator = len([r for r in rev_rows if r["categoria_nps"]=="Detrator"])
nps_score  = round((n_promotor - n_detrator) / max(len(rev_rows),1) * 100, 1)
print(f"  Clients: {n_clients}  |  Churned: {n_churned} ({round(n_churned/n_clients*100,1)}%)")
print(f"  NPS Score: {nps_score}")
print(f"  Reviews: {len(rev_rows)}  |  Tickets: {len(tickets)}")
print(f"  Output directory: {OUTPUT_DIR}/")
print("="*60)
