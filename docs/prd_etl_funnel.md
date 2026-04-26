# PRD – ETL Pipeline & Data Warehouse for Sales Funnel Analysis

---

## 1. Overview
**Purpose**: Build an automated Extract‑Transform‑Load (ETL) pipeline that ingests raw marketing and sales data from `gen/data/` into a structured data warehouse, enabling reliable analysis of the sales funnel and key performance indicators (KPIs) such as Click‑Through Rate (CTR), Customer Acquisition Cost (CAC), Return on Investment (ROI) and Return on Ad Spend (ROAS).

**Business Value**:
- Centralized, trustworthy data for the growth team.
- Faster, data‑driven decision‑making on campaign performance.
- Scalable foundation for future analytics (e.g., LTV, churn, cohort analysis).

---

## 2. Scope
| In‑Scope | Out‑Of‑Scope |
|----------|--------------|
| • Ingestion of CSV/JSONL files located in `gen/data/` (ads, crm, orders, subscriptions, engagement logs, support tickets, reviews).<br>• Transformation into a star‑schema data warehouse (DuckDB file).<br>• Calculation of CTR, CAC, ROI, ROAS at campaign and funnel level.<br>• Automated daily run with basic monitoring & alerting. | • Real‑time streaming ingestion (beyond daily batch).<br>• Advanced ML models (churn prediction, LTV forecasting).<br>• Integration with external BI tools beyond the built‑in Streamlit dashboard. |

---

## 3. Stakeholders
- **Product / Growth Team** – Primary consumers of the funnel dashboards.
- **Data Engineering Team** – Maintains pipeline code and warehouse.
- **Executive Leadership** – Reviews high‑level ROI/ROAS metrics.
- **Compliance / Security** – Ensures data handling follows policy.

---

## 4. Functional Requirements
| ID | Requirement |
|----|-------------|
| FR‑001 | Ingest all files in `gen/data/` (CSV or JSONL) into a **staging layer** on each run. |
| FR‑002 | Validate required columns; reject rows with missing critical fields (e.g., `ad_id`, `campaign_id`, `lead_id`). |
| FR‑003 | Transform staging tables into a **star schema** (`fact_funnel`, `dim_campaign`, `dim_lead`, `dim_order`, …). |
| FR‑004 | Compute derived metrics:  CTR = clicks / impressions, CAC = ad_spend / new_customers, ROI = (revenue‑total_cost) / total_cost, ROAS = revenue / ad_spend. |
| FR‑005 | Store the final model in a DuckDB file (`warehouse.db`) located under `gen/warehouse/`. |
| FR‑006 | Provide a **read‑only** connection string for downstream analytics. |
| FR‑007 | Emit a concise **run‑summary** (rows loaded, rows rejected, duration, success/failure). |
| FR‑008 | Fail fast and send an alert (email/Slack) on any validation or runtime error. |

---

## 5. Non‑Functional Requirements
| ID | Requirement |
|----|-------------|
| NFR‑001 | **Performance** – Full daily run must complete within 10 minutes on a typical developer laptop. |
| NFR‑002 | **Reliability** – 99.5 % success rate over a month; automatic retry on transient failures. |
| NFR‑003 | **Maintainability** – Pipeline code versioned in Git, linted with `ruff`, test‑covered ≥ 80 %. |
| NFR‑004 | **Security** – Data files stored locally; no external network calls. |
| NFR‑005 | **Scalability** – Architecture should allow migration to a hosted DB (PostgreSQL) with minimal code change. |

---

## 6. Data Sources
| Source | File | Format | Core Columns |
|--------|------|--------|--------------|
| Ads | `ads.csv` | CSV | `ad_id`, `campaign_id`, `impressions`, `clicks`, `spend` |
| CRM | `crm.csv` | CSV | `lead_id`, `source`, `created_at`, `status` |
| Orders | `erp_orders.csv` | CSV | `order_id`, `lead_id`, `revenue`, `cost_of_goods` |
| Subscriptions | `subscriptions.csv` | CSV | `sub_id`, `order_id`, `start_date`, `end_date`, `plan` |
| Engagement | `engagement.log` | JSONL | `user_id`, `event_type`, `timestamp` |
| Support | `support_tickets.csv` | CSV | `ticket_id`, `lead_id`, `issue_type`, `resolution_time` |
| Reviews | `reviews.csv` | CSV | `review_id`, `order_id`, `rating`, `comment` |

*If additional files exist, they should be added to this table.*

---

## 7. Architecture Overview
```mermaid
flowchart TD
    subgraph Raw[Raw Data (gen/data/)]
        A[ads.csv]
        B[crm.csv]
        C[erp_orders.csv]
        D[subscriptions.csv]
        E[engagement.log]
        F[support_tickets.csv]
        G[reviews.csv]
    end
    
    subgraph ETL[ETL Process]
        ingest[Ingest & Staging]
        validate[Validate & Clean]
        transform[Transform to Star Schema]
        metrics[Calculate Metrics]
        load[Load into DuckDB]
    end
    
    subgraph DW[Data Warehouse (DuckDB)]
        dimC[dim_campaign]
        dimL[dim_lead]
        dimO[dim_order]
        fact[fact_funnel]
    end
    
    subgraph UI[Analytics Layer]
        dash[Streamlit Dashboard]
    end
    
    Raw --> ingest --> validate --> transform --> metrics --> load --> DW --> UI
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef highlight fill:#e0f7fa,stroke:#006064,stroke-width:2px;
    class ETL highlight;
```

---

## 8. Data Model (Star Schema)
### Fact Table – `fact_funnel`
| Column | Type | Description |
|--------|------|-------------|
| funnel_id | INTEGER (PK) | Synthetic surrogate key |
| date | DATE | Transaction date |
| campaign_id | INTEGER (FK → dim_campaign) |
| lead_id | INTEGER (FK → dim_lead) |
| order_id | INTEGER (FK → dim_order) |
| impressions | BIGINT |
| clicks | BIGINT |
| spend | DECIMAL(12,2) |
| revenue | DECIMAL(12,2) |
| cost_of_goods | DECIMAL(12,2) |
| ctr | DOUBLE | clicks / impressions |
| cac | DOUBLE | spend / new_customers |
| roi | DOUBLE | (revenue‑total_cost) / total_cost |
| roas | DOUBLE | revenue / spend |

### Dimension Tables (examples)
- **dim_campaign** – `campaign_id`, `name`, `budget`, `start_date`, `end_date`.
- **dim_lead** – `lead_id`, `source`, `created_at`, `status`.
- **dim_order** – `order_id`, `order_date`, `revenue`, `cost_of_goods`.

---

## 9. Data Quality & Validation
| Check | Implementation |
|-------|----------------|
| Not‑null key fields | `NOT NULL` constraints on staging tables. |
| Duplicate primary keys | `SELECT … GROUP BY pk HAVING COUNT(*)>1`. |
| Logical ranges | `impressions >= clicks`, `spend >= 0`, `revenue >= 0`. |
| Referential integrity | DBT `relationships` tests between fact and dimensions. |
| Row‑level rejection logging | Write rejected rows to `gen/warehouse/rejections.log` with reason. |

---

## 10. Operational Considerations
- **Run Frequency**: Daily (mid‑night) with optional manual trigger.
- **Orchestration**: Simple Python script invoked via Windows Task Scheduler *or* Prefect flow (if Prefect is already in the repo).
- **Monitoring**: Write a JSON run‑summary to `gen/warehouse/run_log.json`. Slack webhook alert on failure.
- **Backup**: Copy `warehouse.db` to `gen/warehouse/backups/` with a timestamp after each successful run.
- **Permissions**: Restrict write access to the `gen/warehouse/` folder to the `data-eng` group.

---

## 11. Deliverables
| Artifact | Format |
|----------|--------|
| PRD (this document) | Markdown (`docs/prd_etl_funnel.md`) |
| Architecture diagram | Mermaid in MD (above) |
| ETL code skeleton | Python package under `src/etl/` (to be created) |
| Data model definition | DBT models or raw SQL scripts |
| Test suite | PyTest + DBT test files |
| Deployment guide | `README.md` in `src/etl/` |
| Dashboard prototype | Streamlit app (`app/dashboard.py`) |

---

## 12. Timeline (high‑level)
| Sprint | Milestone |
|--------|-----------|
| 1 (1 wk) | Finalize requirements, data source inventory, and PRD sign‑off. |
| 2 (2 wks) | Implement ingestion & staging, basic validation. |
| 3 (2 wks) | Build star‑schema transformations, metric calculations. |
| 4 (1 wk) | Create monitoring, alerts, and backup routine. |
| 5 (1 wk) | Develop Streamlit dashboard mock‑up. |
| 6 (1 wk) | End‑to‑end testing, documentation, hand‑over. |

---

## 13. Acceptance Criteria
- All source files are successfully loaded into the staging layer on the first run.
- No validation errors for a clean data set; rejected rows are logged with clear reasons.
- The warehouse contains the star schema with accurate metric columns.
- The dashboard displays funnel progression and KPI cards for each campaign.
- Automated run produces a JSON summary and sends a Slack alert on failure.

---

*Prepared by the Antigravity AI assistant on 2026‑04‑23.*
