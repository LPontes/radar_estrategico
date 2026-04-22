import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configurações
n_rows = 1000
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)

# Categorias e Produtos
categories = {
    "Eletrônicos": ["Smartphone X", "Laptop Pro", "Tablet Z", "Fone Bluetooth"],
    "Moda": ["Camiseta Algodão", "Calça Jeans", "Tênis Runner", "Casaco Inverno"],
    "Casa": ["Cafeteira", "Jogo de Lençol", "Vaso Decorativo", "Lâmpada Smart"]
}

regions = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
channels = ["loja física", "e-commerce", "marketplace"]
statuses = ["entregue", "cancelado", "devolvido"]
status_weights = [0.85, 0.10, 0.05]

data = []

for i in range(n_rows):
    order_id = 10000 + i
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    
    # Simular queda de vendas no Q3 (Julho, Agosto, Setembro)
    if 7 <= date.month <= 9:
        if random.random() > 0.4: # 60% menos chances de venda
            continue
            
    client_id = random.randint(100, 500)
    client_name = f"Cliente {client_id}"
    region = random.choice(regions)
    channel = random.choice(channels)
    
    # Marketplace tem mais cancelamentos (Sinal 2 do PRD)
    if channel == "marketplace":
        status = random.choices(statuses, weights=[0.60, 0.35, 0.05])[0]
    else:
        status = random.choices(statuses, weights=status_weights)[0]
        
    cat = random.choice(list(categories.keys()))
    
    # Problema intencional: Categorias inconsistentes (Seção 6.1 do PRD)
    if cat == "Eletrônicos":
        cat_variation = random.choice(["Eletrônico", "Eletrônicos", "eletronicos"])
    else:
        cat_variation = cat
        
    product = random.choice(categories[cat])
    qty = random.randint(1, 5)
    unit_price = random.uniform(50, 2000)
    total = qty * unit_price
    
    # Frete
    freight = random.uniform(10, 100)
    # Problema intencional: Outlier de frete (Seção 6.1 do PRD)
    if i == 500:
        freight = 5000.0
        
    # Entrega e NPS
    days_to_deliver = random.randint(1, 15)
    # Correlação intencional: entrega lenta -> NPS baixo (Seção 6.2 do PRD)
    if days_to_deliver > 10:
        nps = random.randint(1, 5)
    else:
        nps = random.randint(7, 10)
        
    # Problema intencional: 8% nulos em NPS (Seção 6.1 do PRD)
    if random.random() < 0.08:
        nps = np.nan
        
    cancel_reason = None
    if status == "cancelado":
        cancel_reason = random.choice(["Arrependimento", "Preço Alto", "Atraso na Entrega", "Erro no Endereço"])
        
    data.append([
        order_id, date.strftime("%Y-%m-%d"), client_id, client_name, region, channel,
        cat_variation, product, qty, round(unit_price, 2), round(total, 2), round(freight, 2),
        status, days_to_deliver, nps, cancel_reason
    ])

df = pd.DataFrame(data, columns=[
    "id_pedido", "data_pedido", "id_cliente", "nome_cliente", "regiao", "canal_venda",
    "categoria_produto", "produto", "quantidade", "valor_unitario", "valor_total", "custo_frete",
    "status_pedido", "dias_entrega", "nota_nps", "motivo_cancelamento"
])

# Problema intencional: Duplicatas (Seção 6.1 do PRD)
df = pd.concat([df, df.iloc[:3]], ignore_index=True)

import os
os.makedirs("data", exist_ok=True)
df.to_csv("data/pedidos_consolidado.csv", index=False, encoding="utf-8-sig")

print(f"Dataset gerado com {len(df)} linhas em data/pedidos_consolidado.csv")
