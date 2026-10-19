# LangGraph Practical: Beginner → Expert

Hands-on Jupyter notebooks that teach LangGraph step by step, using Claude (Anthropic) as the LLM.

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
