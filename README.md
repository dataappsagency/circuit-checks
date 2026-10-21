# circuit-checks

**Does it actually run?** Each check here installs two tools at their current versions on a
fresh GitHub runner and makes one real call through the integration between them — LiteLLM
routing a completion to Ollama, LangChain writing vectors to Qdrant and finding them again.

- `pairs.json` — the pairs, which circuit tools they are, and what each check does
- `pairs/<id>.py` — the check: it raises if the integration doesn't work
- `results/latest.json` — the last run of every pair: pass or fail, the exact versions, the
  error if it failed, and a link to the run's full log
- `results/history/` — every run, dated

[circuit](https://www.usecircuit.app) reads `results/latest.json` daily. A pair that ran is
**verified** for that connection, with the run as its evidence; a pair that failed is shown as a
dated fact — "didn't run on 21 Oct 2026 with these versions" — and alerts anyone watching a stack
that has both tools.

Runs weekly (Mondays, 05:00 UTC), on demand, and whenever a check changes. Everything here is
public on purpose: anyone can read the code and the logs behind a claim.

Not runnable yet: pairs that need a GPU (vLLM) or a paid account (OpenAI, Pinecone, Anthropic).
Those come later with circuit-owned keys that have hard spend caps.

To add a pair: an entry in `pairs.json` and a `pairs/<id>.py` with a `check()` that raises on
failure. Keep it to one real call — this proves the connection, not the tool.
