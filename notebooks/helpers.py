"""Shared helpers for the LangGraph practical notebooks.

Every notebook starts with `from helpers import get_llm, show_graph, print_messages`.
Notebook 00 walks through exactly what these helpers do, step by step.
"""
import os

from dotenv import find_dotenv, load_dotenv
from IPython.display import Image, display

# Find the .env file in the project root (searching upward from the notebook's folder).
load_dotenv(find_dotenv(usecwd=True))

# Default model. Override without editing code by adding CLAUDE_MODEL=... to .env,
# e.g. CLAUDE_MODEL=claude-haiku-5-5 for cheaper / faster demo runs.
MODEL = os.getenv("CLAUDE_MODEL", "claude-opus-5-5")


def get_llm(model: str | None = None, effort: str | None = None, max_tokens: int = 4096, **kwargs):
    """Return a LangChain `ChatAnthropic` chat model authenticated with CLAUDE_KEY from .env.

    effort: "low" | "medium" | "high" | "xhigh" | "max" - how hard Claude thinks.
            None uses the model default (medium on Claude Opus 5.5).
    """
    from langchain_anthropic import ChatAnthropic

    api_key = os.getenv("CLAUDE_KEY")
    if not api_key:
        raise RuntimeError("CLAUDE_KEY not found. Add CLAUDE_KEY=sk-ant-... to the .env file in the project root.")

    if effort:
        kwargs["output_config"] = {"effort": effort}

    # Claude's thinking blocks are bound to the exact conversation that produced them.
    # LangGraph apps often reshape history (trimming, summaries, dynamic system prompts,
    # several agents sharing one message list). "drop_block" tells the API to quietly drop
    # any thinking block whose context changed, instead of rejecting the request.
    kwargs.setdefault("thinking", {"type": "adaptive", "block_binding": {"prefix_mismatch_behavior": "drop_block"}})
    kwargs.setdefault("betas", ["thinking-binding-controls-2026-08-01"])

    return ChatAnthropic(model=model or MODEL, api_key=api_key, max_tokens=max_tokens, **kwargs)


def show_graph(graph, xray: bool = False):
    """Draw a compiled LangGraph graph inline (falls back to Mermaid text when offline)."""
    g = graph.get_graph(xray=xray)
    try:
        display(Image(g.draw_mermaid_png()))
    except Exception:
        print(g.draw_mermaid())  # paste into https://mermaid.live to view


def print_messages(messages):
    """Readable dump of a message list: who said what, and which tools were called."""
    for m in messages:
        header = m.type.upper() + (f" [{m.name}]" if getattr(m, "name", None) else "")
        print(f"===== {header} =====")
        if m.text:
            print(m.text)
        for call in getattr(m, "tool_calls", None) or []:
            print(f"  -> calls tool {call['name']}({call['args']})")
