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

> Use GrillPower. Grill me in rounds of five questions. Mark only the best option for my project as Recommended in each question, challenge my assumptions, and wait for design approval before building.

Give the agent a project or idea. It inspects available evidence first.

## What you get

Example: "Improve my animation engine on a limited CPU budget."

**Q1 — Which renderer should we use?**
- A. Optimize the existing renderer (Recommended)
- B. Replace the renderer
- C. Support two renderers

Why: If the existing renderer meets the visual requirements, keeping it avoids migration overhead.

**Q2 — What animation approach should we use?**
- A. Manual keyframes
- B. Reusable rigs with editable keyframes (Recommended)
- C. Fully procedural motion

Why: Reusable rigs balance production speed and creative control.

The agent asks Q1–Q5 together, with one project-specific recommendation for each question. The other options remain neutral. Reply like **1A, 2B, 3C, 4A, 5B**, or say **accept all**. Subsequent rounds adapt to your choices. Examples are illustrative, not recorded benchmarks.

## The workflow

**Inspect → 5 questions per round → Design approval → Build → Verify → Stop**

- Deep questioning, with exactly one recommended option per question.
- No repeated questions or filler; the final round can be shorter.
- Explicit approval before implementation.
- One focused implementation pass, consolidated review and essential tests.
- No mandatory improvement cycles or speculative polishing.

## Works with your AI

Native skill routes are documented for Codex, Claude Code, Antigravity, Cursor, Gemini CLI, Copilot and OpenCode. Chat-only assistants and local models can use the universal prompt. Actual capabilities depend on the host.

[Compatibility](COMPATIBILITY.md) · [More examples](examples/README.md) · [Evaluation](references/evaluation.md) · [Changelog](CHANGELOG.md)

GrillPower is inspired by [Grill Me](https://github.com/mattpocock/skills) and [Superpowers](https://github.com/obra/superpowers). It is independent and not affiliated with either project.

Run `python3 validate.py` for offline structural checks. Live model behavior, installer execution and token savings remain unmeasured. Report reproducible problems via [Issues](https://github.com/clipcraftclients-art/grillpower/issues). [Contributing](CONTRIBUTING.md).
