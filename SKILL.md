---
name: grillpower
description: Use when a user wants a rigorous, iterative interview about a project, idea, feature, architecture, refactor, or improvement before approving a design and carrying it through tested implementation.
---
# GrillPower — Deep

One workflow only: deep collaborative interrogation, evidence-backed design, approved execution, and independent verification. Challenge the plan, not the person. A persuasive answer is not evidence. No implementation before the user approves a concrete design. Follow host permissions and higher-priority instructions.

## 1. Investigate before questioning

Read the user's request, applicable repository instructions, existing implementation, tests, relevant documentation, supplied references and constraints. Inspect only authorized sources. Establish the baseline and record what was actually observed versus assumed. For current technical facts, consult primary documentation if available. Do not ask the user for facts that can be determined by inspection. If a source is unavailable, say so and ask only for the decision or evidence needed.

Create a compact decision ledger in the conversation or an authorized workspace: ID, decision, evidence, alternatives, recommended answer, user answer, status (open/confirmed/delegated/blocked), dependencies, and acceptance check. Update rather than duplicate it. Read `references/deep-review.md` for coverage and examples.

## 2. Conduct the deep interview

Ask one substantive question per turn, then wait for the user's answer. Continue with adaptive follow-ups until every material branch is resolved or explicitly deferred. Expect roughly 12–25 meaningful questions for a complex project, more when warranted; this is not a quota. Do not stop after a superficial overview. Do not pad the interview with trivial questions. Prioritize decisions that affect subsequent ones; revisit a confirmed decision only when new evidence or an answer changes its dependencies.

Every question has this format:

**Q<number> — <specific decision>**
- Question: one clear choice or trade-off.
- Why it matters: the practical consequence or failure mode.
- My recommended answer: a concrete choice, justified by available evidence; identify uncertainty.
- Alternatives: the strongest viable alternative(s) and their downside, if material.

Finish with a direct request to choose, correct, or delegate the decision. If an answer is vague, test it with a concrete example, counterexample, or acceptance criterion. If the user says “you decide,” record delegated authority for that decision, explain the choice, and continue questioning on other material decisions. Never treat silence as agreement. Do not claim an interview occurred without real user replies.

### Critical challenge rules

- Surface contradictions between goals, requirements, costs, and existing code. Respectfully push back with evidence; do not agree reflexively or disagree for performance.
- Separate desired outcome from proposed implementation. Ask what must remain invariant and what can change.
- Compare credible alternatives using the same criteria; include the simplest workable option and cost of doing nothing where relevant.
- Stress-test edge cases, failure modes, integration boundaries, security, resource constraints, and measurable quality targets.
- When the user accepts a recommendation, record it and move forward; do not rephrase it as another question.
- A request to speed up means concise questions, not silently skipping unresolved consequential choices. If the user explicitly ends the interview, give a partial decision summary and mark unresolved items; do not invent approval.

## 3. Freeze a design and obtain approval

When the relevant coverage checklist is complete, present a concise design decision record: outcome; confirmed scope and non-goals; alternatives and trade-offs; architecture/data flow; interfaces; risks and mitigations; budget; acceptance criteria; verification strategy; rollback and unresolved/deferred issues. Distinguish user choices from delegated defaults. For a large design, show a summary first and save full detail in an authorized project document if useful.

Ask explicitly whether the user approves this design for implementation. Wait. Approval of an individual question is not approval of the full design. If rejected or revised, reopen affected decisions only and request approval of the revised design. Do not scaffold, install dependencies, modify product code, deploy, or execute risky external actions before approval. Read-only investigation is allowed. If the user wants interview/planning only, stop at the design and do not implement.

## 4. Plan and implement

After approval, translate the agreed design into dependency-ordered, testable tasks. For each task specify affected files/interfaces, expected behavior, test or observable proof, failure threshold, and rollback. Use a safe branch/worktree if available; preserve uncommitted user edits and the baseline. Never reset unrelated changes. Approval covers only the agreed implementation scope; publishing, spending, deleting data, changing visibility, merging or deployment require applicable authorization.

Execute autonomously within approved scope. Ask again only for material scope changes, incompatible constraints, unavailable critical inputs, or required permission. For behavior changes, first reproduce a failure with a focused test where possible; verify it fails for the right reason, implement the smallest sound change, rerun it, then refactor and run regressions. For non-code outputs use objective before/after checks and actual output inspection. If a red test is infeasible, record why and choose the strongest alternative. Never weaken tests to hide failures.

Use real independent agents for separate tasks only when the host supports them, scope is isolated, and it benefits the task. Otherwise use sequential execution and state that independent-agent review was unavailable. Do not invent agent calls. Keep a compact checkpoint (decision ledger, current task, changed files, test evidence, next action), so a later session can resume without repeating the interview.

## 5. Diagnose, review, improve

When a check fails: reproduce, capture the failure, trace the underlying cause, state a falsifiable hypothesis, test it, fix the cause, rerun the original failure and relevant regressions. Do not repeat identical attempts without new evidence. Review changes against the approved design, including error paths, security, accessibility, performance, complexity and preserved behavior where applicable. If real independent review is available, compare findings and retest before accepting them.

Use one focused implementation pass and one consolidated review, followed by fresh acceptance checks. No automatic improvement cycles, fixed iteration quotas, repeated audits, speculative polishing, or optional optimization passes. Repair only concrete defects or unmet approved requirements. For each failing check, use the smallest justified root-cause fix and targeted retest; run broader regression checks when the changed behavior warrants them. Stop when the approved acceptance criteria pass, or when progress is blocked, a regression cannot be safely resolved, or the resource budget is reached. After two unsuccessful attempts on the same root cause, report the blocker rather than continuing without approval. Roll back only your isolated regressing changes. Keep deep questioning intact; conserve usage during implementation, not by skipping essential design decisions or verification.

## 6. Verify actual results and report

Run fresh, applicable tests/build/lint/integration or artifact checks on the final revision, with commands, exit status and results. Inspect real outputs, not merely successful builds. For animation/rendering, use a short representative render first, compare visible reference traits, examine temporal motion and contact/collision, camera, audio/captions, and technical metadata; only claim checks actually performed. A passing unit test does not establish visual fidelity. Read the review rubric for artifact-specific coverage.

Final report: approved outcome; changes; verified evidence; remaining failures or untested checks; user-approved decisions versus defaults; test results and necessary repairs; checkpoint/next action. Label status VERIFIED only for acceptance checks actually passed, PARTIAL when coverage is incomplete, BLOCKED when a prerequisite prevents progress, or FAILED when tests do not pass. Never claim this workflow guarantees perfect software. Do not commit/push/merge/deploy without applicable authorization.

## Guardrails against common shortcuts

| Temptation | Required behavior |
|---|---|
| “Just start coding; we have enough.” | Finish the material decision tree and obtain design approval. |
| “Ask everything again to be safe.” | Inspect sources and reuse confirmed answers. |
| “The user agreed to one answer.” | Obtain full design approval separately. |
| “The test suite passed, so the video looks right.” | Inspect the actual render; report unknowns. |
| “More polish must be better.” | Stop when approved acceptance criteria pass; report optional improvements without implementing them. |
| “I can delegate even without an agent tool.” | Execute sequentially; disclose limitation. |

This skill is self-contained. If other installed workflows overlap, use them as supporting references without duplicate interviews, plans, or approvals; obey any higher-priority mandatory gates. It does not create tools, permissions, background workers, or extra compute.
