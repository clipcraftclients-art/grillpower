# Implementation and verification playbook

Use only for complex approved implementation. No extra mandatory reviews or cycles.

## Plan from acceptance

For each task, record the affected file/artifact, intended behavior, acceptance ID, verification method and rollback if relevant. Group tightly coupled changes. Avoid building speculative abstractions, unrelated features or new dependencies.

## Evidence-first work

For defects: capture an observed failure, reproduce it, isolate the cause, fix the cause, rerun the failed check and relevant regressions. For new code: use a failing behavior test first where practical, then implement and verify. For design/media: compare actual output to the agreed examples or measurable criteria. Never claim an unavailable test passed.

## One review, two lenses

1. Requirements: every approved criterion has a corresponding implementation and evidence. Check omissions, unintended scope and contradictory decisions.
2. Engineering quality: check regressions, failure paths, security, unnecessary complexity and maintainability. An independent reviewer can be useful for high-risk work when supported, but is not compulsory.

Fix only actual defects or unmet agreed criteria. Re-run affected checks, not unrelated expensive suites unless required by risk. Respect the same-root-cause attempt limit and agreed budget.

## Completion

Record evidence, limitations and status. If a check is inaccessible, provide a command or procedure and mark it unrun. If the user has not authorized publication or deployment, stop before that action. Preserve a resumable handoff rather than promising background progress.
