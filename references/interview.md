# Decision interview playbook

Read only for difficult or ambiguous decisions. The five-question round and one-recommendation rules in the core skill remain authoritative.

## Prioritize decisions, not question count

- Upstream: outcome, existing system, non-goals, target users and hard constraints.
- High-impact: decisions that change architecture, interfaces, privacy, resource costs, or difficult migrations.
- Downstream: implementation choices, edge cases and acceptance criteria once prerequisites are known.
- Low-impact: delegate reversible details with clear assumptions; don't interrupt the user unnecessarily.

A question is useful when its answer would materially change the approved design or acceptance evidence. If the answer is already supported by project evidence, record it instead of asking.

## Select the best option

Filter infeasible options first. Compare feasible options on the same criteria: goal fit, risk, quality, resource cost, complexity, reversibility and long-term maintenance. State the deciding criterion rather than inventing numeric scores. For close alternatives, prefer the one that preserves working behavior and requires less irreversible work.

Example: the user needs offline animation on a CPU-only host. A GPU-only renderer is not a valid choice. If the current renderer can satisfy the agreed style and performance targets, optimizing it may be better than migration. If a representative render fails a non-negotiable visual requirement, the recommendation may change. Do not recommend a specific renderer merely because it is familiar.

## Batch safety

Ask five independent or conditionally answerable questions. If a choice changes the meaning of a downstream option, defer that question. Keep original IDs and option mappings when answers are partial. Accept letters, custom choices and delegated decisions. If the user changes a previous choice, identify affected decisions only and preserve unaffected answers.

## Close the interview

Review the goal, non-goals, constraints, high-impact choices, risks, success evidence and recovery. Explicitly defer optional details. Ask for design approval separately. Do not keep asking questions just to appear thorough.
