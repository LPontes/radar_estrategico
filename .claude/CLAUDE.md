# Radar Estratégico — 2026

## Project Overview


## Directory Structure

```
.env.example                  # Root env template (canonical — all keys here)
gen/                          # Data generation (ShadowTraffic + Docker)

docs/                         # Event documentation
prompts/                      # Sequenced live-coding prompts per day
src/                          # Python source + requirements per day
presentation/                 # HTML slide decks (Days 1-4)
.claude/
  kb/                         # 18 Knowledge Base domains
  agents/                     # SubAgents (ai-ml/, code-quality/, communication/, domain/, exploration/)
  commands/                   # Custom Claude Code commands
```

## Knowledge Base Domains (18)

| Domain | Path | Purpose | Day |
|--------|------|---------|-----|
| shadowtraffic | kb/shadowtraffic/ | Synthetic data generation | 1 |
| pydantic | kb/pydantic/ | Data validation + structured outputs | 1 |
| python | kb/python/ | Clean code patterns | 1-4 |
| llamaindex | kb/llamaindex/ | RAG ingestion + query | 2 |
| qdrant | kb/qdrant/ | Vector DB (The Memory) | 2-4 |
| prompt-engineering | kb/prompt-engineering/ | Prompting techniques | 2 |
| langchain | kb/langchain/ | Agent framework + tool routing | 3 |
| chainlit | kb/chainlit/ | Chat interface + streaming | 3-4 |
| genai | kb/genai/ | GenAI architecture patterns | 3-4 |
| crewai | kb/crewai/ | Multi-agent orchestration | 4 |
| deepeval | kb/deepeval/ | LLM evaluation + testing | 4 |
| langfuse | kb/langfuse/ | LLMOps observability | 4 |
| testing | kb/testing/ | pytest patterns | 3-4 |
| architecture | kb/architecture/ | System design | 1-4 |
| exploration | kb/exploration/ | Codebase analysis | 1-4 |
| communication | kb/communication/ | Stakeholder communication | 1-4 |
| sa-slides | kb/sa-slides/ | Slide deck design system | 1-4 |

## SubAgents

| Agent | Category | Domain |
|-------|----------|--------|
| genai-architect | ai-ml/ | Multi-agent architecture design |
| ai-data-engineer | ai-ml/ | Pipeline + cloud optimization |
| ai-prompt-specialist | ai-ml/ | Prompt engineering |
| llm-specialist | ai-ml/ | LLM selection + optimization |
| code-reviewer | code-quality/ | Code review specialist |
| code-cleaner | code-quality/ | Python code cleaning |
| code-documenter | code-quality/ | Documentation specialist |
| python-developer | code-quality/ | Python code architect |
| shell-script-specialist | code-quality/ | Shell scripting |
| the-planner | communication/ | Project planning |
| meeting-analyst | communication/ | Meeting notes extraction |
| sa-slide-builder | domain/ | Slide deck builder |
| sa-slide-reviewer | domain/ | Slide deck reviewer |
| sa-slide-fixer | domain/ | Slide deck fixer |
| sa-slide-planner | domain/ | Slide content planner |
| codebase-explorer | exploration/ | Code analysis + discovery |
| kb-architect | exploration/ | Knowledge base design |

## Data Model (4 Entities)

## Local Dev Quickstart

```bash
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY
cd gen && cp license.env.example license.env
# Set your ShadowTraffic license fields in license.env
docker compose up
```

## Conventions

- Python 3.11+ with type hints
- KB files: concepts < 150 lines, patterns < 200 lines
- File naming: kebab-case
- MCP validation required before KB updates
- All code production-ready (real imports, error handling)
- Environment-based URLs (localhost for local, cloud URLs via env vars)
