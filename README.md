# LangGraph Practical: Beginner → Expert

[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-ea4aaa?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/hareramray)
[![GitHub stars](https://img.shields.io/github/stars/hareramray/LanggraphPractical?style=flat&logo=github)](https://github.com/hareramray/LanggraphPractical/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/hareramray/LanggraphPractical?style=flat&logo=github)](https://github.com/hareramray/LanggraphPractical/network/members)
[![Last commit](https://img.shields.io/github/last-commit/hareramray/LanggraphPractical)](https://github.com/hareramray/LanggraphPractical/commits/main)
[![Follow](https://img.shields.io/github/followers/hareramray?label=Follow&style=flat&logo=github)](https://github.com/hareramray)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2-1C3C3C?logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![Claude](https://img.shields.io/badge/LLM-Claude%20Opus%205.5-D97757?logo=anthropic&logoColor=white)](https://www.anthropic.com/claude)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Notebooks](https://img.shields.io/badge/notebooks-14-blue)](notebooks/)

Hands-on Jupyter notebooks that teach LangGraph step by step, using Claude (Anthropic) as the LLM.

## About

**LangGraph Practical** is a learn-by-doing course. It goes from your first LLM call to a production-style multi-agent system in 14 small steps. Each notebook explains a concept, shows it in short runnable cells and ends with a recap, so you can learn alone or demo it live.

- 🎯 **Who it's for:** Python developers who are new to agents, and engineers who want production patterns for LangGraph
- 🧪 **What you build:** workflows, tool-using agents, memory, human approval steps, subgraphs, a multi-agent supervisor and a full customer-support agent
- ✅ **Tested:** every notebook was run end to end with LangGraph 1.2 and Claude Opus 5.5

**Author:** [Hareram](https://github.com/hareramray), who works with Vue, Python and AI.

If these notebooks help you, please ⭐ **star the repo** or 💖 **[sponsor the project](https://github.com/sponsors/hareramray)**. It keeps new lessons coming.

## Setup

1. Put your Anthropic key in `.env` in this folder:
   ```
   CLAUDE_KEY=sk-ant-...
   # optional: use a cheaper/faster model for demo runs
   # CLAUDE_MODEL=claude-haiku-5-5
   ```
2. Create the environment (already done if `.venv/` exists):
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Open `notebooks/` in VS Code (or `jupyter lab`), select the `.venv` kernel, and run the notebooks in order.

The default model is Claude Opus 5.5 (`claude-opus-5-5`). `notebooks/helpers.py` reads `CLAUDE_KEY` and creates the model, so every notebook starts with one setup cell.

## Learning path

| # | Level | Notebook | Concepts |
|---|---|---|---|
| 00 | 🟢 Beginner | Setup & first LLM call | `ChatAnthropic`, messages, `.text`, effort, streaming |
| 01 | 🟢 Beginner | Graph basics | State, nodes, edges, reducers, input/output schemas |
| 02 | 🟢 Beginner | Conditional edges & loops | routers, cycles, `recursion_limit`, `Command` |
| 03 | 🟢 Beginner | Chatbot with an LLM | `MessagesState`, `add_messages`, prompt chaining |
| 04 | 🟡 Intermediate | Tools & ReAct agent | `@tool`, `bind_tools`, `ToolNode`, `tools_condition`, `create_agent` |
| 05 | 🟡 Intermediate | Memory & persistence | checkpointers, threads, SQLite, trimming, summarization |
| 06 | 🟡 Intermediate | Human-in-the-loop | `interrupt()`, `Command(resume=...)`, breakpoints, `update_state` |
| 07 | 🟡 Intermediate | Streaming | `values` / `updates` / `messages` / `custom`, async |
| 08 | 🟠 Advanced | Structured output, routing, parallelism | Pydantic outputs, fan-out/fan-in, `Send` map-reduce, evaluator loop |
| 09 | 🟠 Advanced | Subgraphs | shared vs. different schemas, xray, subgraph streaming & interrupts |
| 10 | 🟠 Advanced | Multi-agent supervisor | specialist agents, structured routing, handoffs |
| 11 | 🔴 Expert | Long-term memory | `Store`, namespaces, `context_schema`, `Runtime` |
| 12 | 🔴 Expert | Production patterns | `RetryPolicy`, `CachePolicy`, fallbacks, time travel, durability, testing |
| 13 | 🔴 Expert | Capstone: support agent | everything combined, including secure `ToolRuntime` and refund approval |

## Tips for live demos

- The notebooks are saved with outputs from a real run, so you can rehearse with them. To start fresh, use **Clear All Outputs**, then run cells one by one.
- LLM answers vary between runs. The graph behaviour (routing, interrupts, memory) stays the same.
- To make runs faster or cheaper, set `CLAUDE_MODEL=claude-haiku-5-5`, or pass `get_llm(effort="low")`.
- With Claude, use `with_structured_output(..., method="json_schema")`. Forced tool calling isn't supported on Claude Opus 5.5.

## License

This project is licensed under the [Apache License 2.0](LICENSE). Copyright 2026 Hareram.
