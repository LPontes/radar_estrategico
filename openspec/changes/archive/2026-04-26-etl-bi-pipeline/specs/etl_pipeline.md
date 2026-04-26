# Spec: ETL BI Pipeline

## ADDED Requirements

### Requirement: Esquema DW Separado
Toda a modelagem dimensional deve residir no schema `DW` para isolamento de dados.

#### Scenario: Criação das tabelas Gold
- **WHEN** O script de ETL for executado
- **THEN** As tabelas `dim_clientes`, `dim_tempo`, `dim_produtos`, `fact_marketing_top_funnel` e `fact_assinaturas` devem ser criadas dentro do schema `DW`.

### Requirement: Padronização de Dados
Os campos de e-mail e fontes de tráfego devem ser normalizados.

#### Scenario: Limpeza de E-mail
- **WHEN** Um lead for ingerido com e-mail ' User@Exemplo.com '
- **THEN** O valor na `dim_clientes` deve ser 'user@exemplo.com'.

#### Scenario: Padronização de UTM Source
- **WHEN** Um registro tiver `utm_source` como 'FACEBOOK' ou 'facebook '
- **THEN** O valor na `fact_marketing_top_funnel` e `dim_clientes` deve ser 'facebook'.
