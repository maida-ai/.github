# Maida.AI

**Don't let broken agent changes merge.**

Maida is a local-first, pre-merge behavioral regression gate for AI agents. Compare observed executions against a reviewed baseline and checked-in policy, and see what changed before merge.

## Start with one task

```bash
uv tool install "maida-ai==0.6.1"
maida demo --regression
```

Expect a FAIL verdict and a PR-comment preview. The demo exits `0` after successfully showing the failing gate; an actual failed gate exits `1`. This offline rehearsal needs no clone, API key, or account.

**[Protect one coding-agent task →](https://maida.ai/docs/getting-started/)**

Follow the gradual walkthrough: capture one useful task in your own repository, check its observed completion and behavior, review a small baseline and policy, then see a pass, a deliberate regression, and a repair. Add CI when that local loop works. Maida 0.6.0 supports Python 3.12–3.14. For a Python tool-calling agent, use the [secondary walkthrough](https://github.com/maida-ai/maida-tutorials/blob/main/guides/python-agent.md) and install the library in the project environment.

The verdict is PASS, FAIL, or INCONCLUSIVE. Exit `0` includes INCONCLUSIVE, so consumers must read the verdict. Checks cover observed executions under the selected policy; they do not prove answer correctness or behavior outside that evidence. Keep correctness tests alongside Maida. Before relying on CI to block merges, configure the [Action and repository protection](https://github.com/maida-ai/maida-assert#blocking-mode-and-required-repository-settings), pin a reviewed Action SHA, and verify the required check on the actual PR head.

## Find what you need next

- [maida](https://github.com/maida-ai/maida): CLI, tracing, comparison engine and local investigation.
- [maida-tutorials](https://github.com/maida-ai/maida-tutorials): one home for progressive tutorials, examples and demo applications.
- [maida-assert](https://github.com/maida-ai/maida-assert): Action setup and repository protection requirements.
- [Product skills](https://github.com/maida-ai/skills/tree/main/product): help with capture, adding a gate, or interpreting its result.
- [maida-ts](https://github.com/maida-ai/maida-ts): limited TypeScript trace writer.

Traces stay on your machine or CI runner unless you explicitly configure otherwise. Capture may use a local telemetry receiver; it is not telemetry to Maida. No Maida cloud account is required for the local workflow.

[Website](https://maida.ai) · [Documentation](https://maida.ai/docs/) · [PyPI](https://pypi.org/project/maida-ai/)
