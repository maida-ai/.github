# Maida.AI

**Don't let broken agent changes merge.**

Your agent still returns the right answer — but now it calls 3× the tools. A
retry loop that wasn't there last week. A new tool the baseline has never seen.
Output evals pass. Review sees a green diff. It ships.

Maida is the pre-merge behavioral regression gate for AI agents. It compares
agent execution traces against checked-in baselines and blocks PRs when
structural behavior regresses.

Maida sits earlier than production tools and complements output evals. Output
evals ask whether the answer was good. Maida asks whether this PR changed how
the agent behaves.

No cloud account required. No telemetry by default. Runs stay in your
environment unless you explicitly export them.

---

## Try it in 60 seconds

No repo clone, no config file, no API key, no sign-up:

```bash
pip install maida-ai
maida demo               # traced run of a bundled simulated agent
maida view               # open the timeline at 127.0.0.1:8712
maida demo --regression  # watch the gate catch a bad refactor
```

📚 Full documentation: **[maida.ai/docs](https://maida.ai/docs/)**

---

## The workflow

Instrument one agent entrypoint:

```python
from maida import trace

@trace
def run_agent(user_input: str):
    # Your existing agent code
    ...
```

Capture a reviewed baseline from known-good trials, then gate every change
against it:

```bash
# 1. Sample known-good behavior
maida run my_agent.py --trials 25 --no-fail-fast --json-out baseline-report.json

# 2. Check in the reviewed baseline
maida baseline --from-report baseline-report.json --out baselines/my_agent.json

# 3. Gate the candidate after your next change
maida run my_agent.py \
  --baseline baselines/my_agent.json \
  --policy .maida/policy.yaml \
  --format markdown
```

Exit code `0` means pass or inconclusive; `1` means the gate failed.
`maida init --github` scaffolds the policy and the workflow for you.

---

## GitHub Action

[`maida-ai/maida-assert@v5`](https://github.com/maida-ai/maida-assert) runs the
same gate on every pull request and posts a sticky verdict comment.

```yaml
name: Agent Regression Check

on: [pull_request]

jobs:
  agent-check:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      checks: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v7
      - uses: maida-ai/maida-assert@v5
        with:
          agent-script: my_agent.py
          baseline: baselines/my_agent.json
          policy: .maida/policy.yaml
          python-version: '3.12'
```

Your `agent-script` must use `@trace` or `traced_run()` so Maida can record a
run.

---

## What Maida flags

- Step-count regressions
- Tool-call count regressions
- Unexpected tool paths
- Loop and cycle risk
- Guardrail events
- Latency envelope changes
- Cost envelope changes
- Missing stop conditions

These are behavioral regression signals. They do not prove output quality. They
tell you when an agent's execution behavior changed relative to a baseline.

---

## Repositories

| Repo | What it is |
|------|------------|
| [maida](https://github.com/maida-ai/maida) | Python package, `maida` CLI, SDK, local run storage, and timeline viewer |
| [maida-assert](https://github.com/maida-ai/maida-assert) | GitHub Action that runs the gate on pull requests |
| [maida-tutorials](https://github.com/maida-ai/maida-tutorials) | Runnable notebooks for trying Maida on agent code |
| [maida-workflows](https://github.com/maida-ai/maida-workflows) | Verify runtime-generated agent plans before they run |
| [maida-ts](https://github.com/maida-ai/maida-ts) | TypeScript mirror of the trace contract |
| [opencode-plugin](https://github.com/maida-ai/opencode-plugin) | Record OpenCode sessions as Maida traces |
| [Demos](https://github.com/maida-ai/Demos) | Self-contained demos of the gate |

---

Website: [maida.ai](https://maida.ai) ·
Docs: [maida.ai/docs](https://maida.ai/docs/) ·
PyPI: [`maida-ai`](https://pypi.org/project/maida-ai/) ·
Contact: [contact@maida.ai](mailto:contact@maida.ai)
