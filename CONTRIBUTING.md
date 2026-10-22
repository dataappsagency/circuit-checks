# Contributing to circuit-checks

Thank you for helping. Every pair here becomes a public claim — "these two tools ran together,
on this date, at these versions" — and circuit shows it as **verified**. So the bar is
simple and strict: **the check must make one real call through the integration.**

## What counts as a real check

A check passes only if the integration between the two tools actually worked.

**Do**

- Install both tools from their real packages, at their current versions (no pins unless a
  pair can't install without one — say why in `pairs.json`).
- Make **one real call through the integration**: the call a user of both tools would make.
  LiteLLM routing a completion to Ollama. LangChain writing a vector to Qdrant *and reading
  it back*.
- Assert on the result, so a silent no-op fails: the reply isn't empty, the vector you wrote
  is the one you found.
- Return a short note on success (it's shown with the result), and let anything else raise.

**Don't**

- **No mocks, stubs or fakes of either tool in the pair**, and nothing that patches, skips
  or catches the call under test. If the integration is broken, the check must fail.
- No test of one tool alone — that proves the tool, not the connection.
- No accounts, API keys or paid services. Checks run on a free GitHub runner with no
  secrets. Pairs that need a key or a GPU wait until circuit can run them with its own
  capped keys.
- No network calls beyond installing packages and the local services the runner provides.

**Allowed:** deterministic stand-ins for things *outside* the pair. When the pair is a
framework and a vector store, the embeddings can come from `pairs/_fake.py` — the
integration being proved is the framework talking to the store, not the embedding model.

## Adding a pair

1. **Pick the pair.** Two tools with a documented integration that runs on a CPU runner.
2. **Find circuit's ids for both tools** (`a` and `b`). They look like `t-gh-berriai-litellm`.
   Look them up with circuit's API (`GET https://www.usecircuit.app/v1/search?q=litellm`,
   free key), or leave your best guess and say so in the pull request — we'll fill them in.
3. **Add an entry to `pairs.json`:**

   ```json
   {
     "id": "litellm-ollama",
     "a": "t-gh-berriai-litellm",
     "b": "t-gh-ollama-ollama",
     "type": "rest-api",
     "packages": ["litellm"],
     "needs": ["ollama"],
     "what": "LiteLLM routes a chat completion to a local Ollama model"
   }
   ```

   | Field | What it is |
   |---|---|
   | `id` | `<a>-<b>`, lowercase, the same as the file name |
   | `a`, `b` | circuit's tool ids, the caller first |
   | `type` | how they connect: `sdk`, `rest-api`, `native-connector`, `mcp-server`, `plugin`… |
   | `packages` | what `pip install` needs |
   | `needs` | local services: `ollama`, `ollama-embed`, `postgres`, `qdrant`, `redis`, `weaviate` |
   | `what` | one sentence: the real call the check makes |
   | `pre` *(optional)* | installs that must come first, e.g. CPU-only PyTorch |
   | `env` *(optional)* | environment variables the check needs |

4. **Write `pairs/<id>.py`** with a `check()` function:

   ```python
   import litellm
   from _ollama import MODEL, BASE

   def check():
       r = litellm.completion(model=f"ollama/{MODEL}", api_base=BASE,
                              messages=[{"role": "user", "content": "Reply with the word ready."}], max_tokens=10)
       text = r.choices[0].message.content
       assert text and text.strip(), "empty reply"
       return f"replied: {text.strip()[:60]}"
   ```

   Shared helpers are in `pairs/_*.py` (`_ollama.py` for the local model, `_fake.py` for
   deterministic embeddings). Keep the check short — one call, one assertion that matters.

5. **Run it locally** with the services it needs (Docker is easiest), then:

   ```sh
   python run.py litellm-ollama
   ```

   It writes `results/runs/<id>.json` and prints it. `"ok": true` is what you want.

6. **Open a pull request.** Don't edit `results/` — the workflow writes it after your pair
   is merged and run.

## How a pull request is reviewed

A maintainer reads every check before it's merged, because merging it lets it publish a
verified claim. We look for:

- one real call through the integration, and an assertion that would catch it failing;
- no mocks of either tool, nothing swallowing the error;
- packages from their official names on PyPI;
- no network use beyond the runner's local services.

Checks run only after merge, on `main`. Pull requests from forks don't run the workflow.

## When a check breaks

A failing pair isn't a red build — it's the finding. If a tool's API changed and the check
is out of date, fix the check (and say what changed in the pull request). If the integration
itself broke, leave the check as it is: the failure is the fact circuit records.

## Licence

By contributing, you agree that your contribution is licensed under the Apache License 2.0
(see `LICENSE`). Results the workflow publishes are under CC BY 4.0 (see `results/LICENSE`).
