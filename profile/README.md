# Maida.AI

**Don't let broken agent changes merge.**

Maida is a local-first, pre-merge behavioral regression gate for AI agents. Compare observed executions against a reviewed baseline and checked-in policy, and see what changed before merge.

## Start with one task

```bash
uv tool install "maida-ai==0.5.3"
maida demo --regression
```

Expect FAIL and a PR-comment preview; exit `1` is deliberate. The offline demo needs no clone, API key, or account.

**[Protect one coding-agent task →](https://maida.ai/docs/getting-started/)**

Follow the gradual walkthrough: capture one useful task, review a few checks, see a pass, introduce a deliberate regression, and repair it. Add CI when that local loop works. The guide names the next safe action and what the evidence covers. For a Python tool-calling agent, use the [secondary walkthrough](https://github.com/maida-ai/maida-tutorials/blob/main/guides/python-agent.md).

The verdict is PASS, FAIL, or INCONCLUSIVE. Exit `0` includes INCONCLUSIVE, so consumers must read the verdict. A behavioral check complements correctness tests. Repository protection and a fresh check on the actual PR head need separate verification.

## Find what you need next

- [maida](https://github.com/maida-ai/maida): CLI, tracing, comparison engine and local investigation.
- [maida-tutorials](https://github.com/maida-ai/maida-tutorials): one home for progressive tutorials, examples and demo applications.
- [maida-assert](https://github.com/maida-ai/maida-assert): Action setup and repository protection requirements.
- [Product skills](https://github.com/maida-ai/skills/tree/main/product): help with capture, adding a gate, or interpreting its result.
- [maida-ts](https://github.com/maida-ai/maida-ts): limited TypeScript trace writer.
- [opencode-plugin](https://github.com/maida-ai/opencode-plugin): supported native capture integration.

Traces stay on your machine or CI runner unless you explicitly configure otherwise. Capture may use a local telemetry receiver; it is not telemetry to Maida.

[Website](https://maida.ai) · [Documentation](https://maida.ai/docs/) · [PyPI](https://pypi.org/project/maida-ai/)
