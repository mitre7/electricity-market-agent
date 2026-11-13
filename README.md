# ⚡ Electricity Market Morning-Briefing Agent

Hands-on notebook for the lecture **Agentic AI in Energy**. You build an LLM agent that analyses German (DE-LU) day-ahead electricity prices, renewable generation, demand and forecast errors using data from the [ENTSO-E Transparency Platform](https://transparency.entsoe.eu). It then writes a market briefing in which every claim cites its evidence.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-GITHUB-USER/electricity-market-agent/blob/main/electricity_market_agent.ipynb)

## For participants

1. Click **Open in Colab** above, then **File → Save a copy in Drive** so your changes are kept.
2. Add your keys as **Colab Secrets** (🔑 icon in the left sidebar), and switch on *Notebook access* for each:
   - `ENTSOE_API_KEY`: optional. Without it the notebook uses the bundled cached data.
   - One LLM key: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `XAI_API_KEY` or `NVIDIA_API_KEY`.
3. Run the cells from top to bottom.

Your keys stay in your own Google account and are never saved in the notebook.

**ENTSO-E API access:** register at transparency.entsoe.eu, then email `transparency@entsoe.eu` with the subject *"Restful API access"*. Approval can take a few days. Your token then appears under *My Account Settings → Web API Security Token*.

## Data resolution

The notebook uses the native **15-minute** day-ahead resolution (96 intervals per day; 92 / 100 on DST days) and nothing is averaged. Only delivery days from **2025-10-01** onwards are supported, because earlier days were hourly. The bundled cache holds 7 such days.

## Supported LLM providers

All are called through their OpenAI-compatible endpoints with the `openai` Python package. Set `PROVIDER` / `MODEL` in section 2 of the notebook.

| `PROVIDER` | Default model | Secret name |
|---|---|---|
| `openai` | `gpt-6.1-sol` | `OPENAI_API_KEY` |
| `anthropic` | `claude-opus-5-5` | `ANTHROPIC_API_KEY` |
| `gemini` | `gemini-3.8-flash` | `GEMINI_API_KEY` |
| `xai` | `grok-4.7` | `XAI_API_KEY` |
| `nvidia` | `nvidia/nvidia/nemotron-3-ultra` | `NVIDIA_API_KEY` (free at build.nvidia.com) |

## Repository layout

```
electricity_market_agent.ipynb   the lecture notebook
knowledge/                       Markdown knowledge base the agent searches (BM25)
data/cache/                      Parquet snapshots of ENTSO-E data (offline fallback)
scripts/build_cache.py           rebuild / extend the cache (15-minute data)
```

## For the instructor

- Push this folder to a **public** GitHub repo. Replace `YOUR-GITHUB-USER` in this README and in `REPO_URL` (section 0 of the notebook).
- Add cached dates: `ENTSOE_API_KEY=... python scripts/build_cache.py 2026-11-12`. Each date takes about 1-2 minutes.
- Run locally: `pip install -r requirements.txt jupyter`, put keys in a `.env` file (git-ignored), then `jupyter lab`.
