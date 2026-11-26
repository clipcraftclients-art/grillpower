# GrillPower

**Ask five better questions. Build the right thing.**

A universal AI skill that challenges your ideas, recommends answers, and helps you build an approved design without wasting usage on endless improvement loops.

[![Release](https://img.shields.io/github/v/release/clipcraftclients-art/grillpower)](https://github.com/clipcraftclients-art/grillpower/releases)
[![Stars](https://img.shields.io/github/stars/clipcraftclients-art/grillpower?style=flat)](https://github.com/clipcraftclients-art/grillpower/stargazers)

## Install

```bash
npx skills add clipcraftclients-art/grillpower --skill grillpower
```

Or copy [PROMPT.md](PROMPT.md) into any AI chat. The optional installer requires Node.js and network access; the skill itself has no runtime dependencies. [Manual installation and compatibility](COMPATIBILITY.md).

## Use it

> Use GrillPower. Grill me in rounds of five questions. Recommend an answer to each question, challenge my assumptions, and wait for design approval before building.

Give the agent a project or idea. It inspects available evidence first.

## What you get

Example: "Build a report export feature."

| Question | Recommended answer |
|---|---|
| Q1. Which records should be exported? | Only authorized records matching the current filter. |
| Q2. Which format should we support first? | CSV, for broad compatibility. |
| Q3. How large can exports be? | Set a measured limit; avoid unbounded requests. |
| Q4. How should permissions be enforced? | Recheck authorization on the server. |
| Q5. How do we verify success? | Test filters, unauthorized access and size boundaries. |

Reply by question number, or say **accept all**. The agent records the answers and asks the next five meaningful questions if necessary. This is an illustrative example, not a recorded benchmark.

## The workflow

**Inspect → 5 questions per round → Design approval → Build → Verify → Stop**

- Deep questioning, with a recommendation for every question.
- No repeated questions or filler; the final round can be shorter.
- Explicit approval before implementation.
- One focused implementation pass, consolidated review and essential tests.
- No mandatory improvement cycles or speculative polishing.

## Works with your AI

Native skill routes are documented for Codex, Claude Code, Antigravity, Cursor, Gemini CLI, Copilot and OpenCode. Chat-only assistants and local models can use the universal prompt. Actual capabilities depend on the host.

[Compatibility](COMPATIBILITY.md) · [More examples](examples/README.md) · [Evaluation](references/evaluation.md) · [Changelog](CHANGELOG.md)

GrillPower is inspired by [Grill Me](https://github.com/mattpocock/skills) and [Superpowers](https://github.com/obra/superpowers). It is independent and not affiliated with either project.

Run `python3 validate.py` for offline structural checks. Live model behavior, installer execution and token savings remain unmeasured. Report reproducible problems via [Issues](https://github.com/clipcraftclients-art/grillpower/issues). [Contributing](CONTRIBUTING.md).
