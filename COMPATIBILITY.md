# Universal compatibility

GrillPower uses the vendor-neutral [Agent Skills specification](https://agentskills.io/specification). There is one canonical SKILL.md and one generated plain-text equivalent, PROMPT.md. Model brand does not determine capabilities: the host, permission settings, installed version and available tools do.

## Installation routes

| Host | Suggested route | Documentation |
|---|---|---|
| Codex | Native skill under project .agents/skills/grillpower or a supported personal skill directory | [OpenAI skills](https://developers.openai.com/plugins/concepts/skills) |
| Claude Code | Native skill under .claude/skills/grillpower or personal ~/.claude/skills/grillpower | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Google Antigravity | .agents/skills/grillpower in workspace; global ~/.gemini/config/skills/grillpower | [Antigravity skills](https://antigravity.google/docs/skills) |
| Gemini CLI | Native Agent Skills, e.g. .agents/skills/grillpower | [Gemini CLI skills](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md) |
| Cursor | .cursor/skills/grillpower | [Cursor skills](https://cursor.com/docs/skills) |
| GitHub Copilot / VS Code | .github/skills/grillpower in the workspace | [Copilot skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| OpenCode | .opencode/skills/grillpower | [OpenCode skills](https://opencode.ai/docs/skills/) |
| Cline, Roo Code, Amp, OpenHands, OpenClaw, other agents | Use the native skill directory documented for the installed version, or paste PROMPT.md | [Agent Skills specification](https://agentskills.io/specification) |
| ChatGPT, Claude, Gemini, Grok, DeepSeek, Qwen, local models, custom agents | Paste PROMPT.md or attach it and ask the assistant to follow it; use native skill support only where actually available | Universal prompt fallback |

The listed native routes are documentation-based, not live installation certifications. Support varies with versions, configuration and permissions. A chat-only assistant cannot execute a shell command just because the prompt describes one.

## No package manager required

Download a release or clone the repository. Copy SKILL.md and references/ into a folder named grillpower within the host's skill directory. Keep the exact folder name for native discovery, including when extracting a tagged source ZIP. Avoid overwriting existing custom files. Restart or reload discovery if necessary.

An optional third-party installer is [Vercel skills](https://github.com/vercel-labs/skills):

```sh
npx skills add clipcraftclients-art/grillpower --skill grillpower
```

This requires Node.js and network access; review the installer and its destination/permissions before accepting. The skill itself has no runtime dependencies. If this installer cannot discover the root skill, use the manual route. No auto-executed installation scripts are included.

## Universal prompt route

Open [PROMPT.md](PROMPT.md), copy all its contents into an instruction field or chat, then give the project goal. On hosts with small context windows, retain the compact ledger and reattach the same prompt on resumption. A one-shot noninteractive API can return a decision handoff; it cannot simulate real user approval. No particular slash command or agent tool is required. A model with a short context or weak instruction-following may miss rules: retain the decision ledger and evaluate on a small task before relying on it.

## Verify activation

Ask the assistant to use GrillPower on an ambiguous project. It should inspect available evidence, ask five material questions together with recommended answers, and wait. This is a smoke test, not a comprehensive benchmark. See [pressure tests](references/pressure-tests.md) for the full behavioral evaluation.
