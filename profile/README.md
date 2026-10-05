# Maida.AI

**Don't let broken agent changes merge.**

Your coding agent returns a plausible answer and the tests pass, but it now loops, skips verification, or rewrites a test to hide a bug. **Maida checks an agent change before merge.** It checks how the agent worked alongside your tests of the result.

## Try Maida on your coding agent

Use Python 3.12–3.14 and an existing Git repository with Claude Code:

```bash
uv tool install "maida-ai==0.6.1"

cd my-repo
maida init

# Run one normal Claude Code task and exit the session.

maida check
# Then run the exact "View:" command printed by Maida.
```

Approve init's setup preview, then start a new agent session. **A successful first report says `3 active checks passed`**, identifies your task, and prints the viewer command. Open it to see the task's execution timeline. You need no tutorial clone or agent-code changes. If Maida is already in the project's uv environment, prefix its commands with `uv run`; plain `claude` still works.

For example: `maida view 83aa19e3`. Use the command from your own report.

**Runs on your machine or CI runner. No Maida cloud account required.** Task evidence is not uploaded to Maida; your coding agent still uses its normal provider.

## Protect the next agent change

The first report checks completion, recorded loops, and guardrail events. Next, [review the observed behavior and keep a baseline and policy](https://maida.ai/docs/getting-started/#protect-the-next-agent-change) so you can compare the next change. Instructions, skills, tools, model configuration, harness code, and application code can all change behavior. Maida gates the resulting change whether a human or the agent authored it.

Keep ordinary tests and evals: a Maida result covers observed behavior, not answer correctness. Once a local pass → safe failure → repair works, [add the PR gate and repository protection](https://github.com/maida-ai/maida-assert#add-the-merge-boundary).

Comparisons report **PASS, FAIL, or INCONCLUSIVE**. Exit `0` includes INCONCLUSIVE; read the verdict rather than treating process success as approval.

## See why green tests are not enough

In the [canonical storefront demo](https://github.com/maida-ai/maida-tutorials/tree/main/demos/pr-gate), a coding agent simplifies shipping, then changes the VIP test to approve **$15 shipping instead of $0**. All four application tests pass. **Maida fails the agent change** because the agent rewrote the protected regression test. The deterministic rehearsal uses released Maida v0.6.1 and runs offline after installation.

For a smaller canned example without a clone, run `maida demo --regression`: expect a FAIL verdict and PR-comment preview. The rehearsal exits `0` when that expected failure is reproduced.

## Core product

- [Maida](https://github.com/maida-ai/maida): the engine, CLI, and public contracts. Start here to check your own agent change.
- [Maida tutorials](https://github.com/maida-ai/maida-tutorials): the canonical runnable coding-agent project, walkthroughs, and examples.
- [Maida Action](https://github.com/maida-ai/maida-assert): the GitHub PR boundary around the same engine and CLI.

## Supported extensions

- [Product skills](https://github.com/maida-ai/skills): instrument an agent, add the gate, and debug regressions.
- [OpenCode plugin](https://github.com/maida-ai/opencode-plugin): record local OpenCode traces for Maida.
- [TypeScript trace writer](https://github.com/maida-ai/maida-ts): a limited write-side mirror for TS/JS integrations; Python owns behavior and schema.

## Find what you need next

- [Check your own task](https://maida.ai/docs/getting-started/): setup, first report, and protection for the next change.
- [Investigate a regression](https://maida.ai/docs/viewer/): see what the agent did.
- [Add the PR gate](https://github.com/maida-ai/maida-assert): CI and repository protection requirements.
- [Integrate another agent/framework](https://maida.ai/docs/integrations/): supported capture integrations; [Python agent walkthrough](https://github.com/maida-ai/maida-tutorials/blob/main/guides/python-agent.md).
- [Product skills](https://github.com/maida-ai/skills/tree/main/product): help with setup, adding a gate, or debugging it.
- [CLI and technical reference](https://maida.ai/docs/cli/): commands, coverage, configuration, and data formats.

[Website](https://maida.ai) · [Documentation](https://maida.ai/docs/) · [PyPI](https://pypi.org/project/maida-ai/)

The website source, this organization-profile repository, and the Action smoke fixture are public infrastructure maintained for Maida. They are outside the product and extension hierarchy.
