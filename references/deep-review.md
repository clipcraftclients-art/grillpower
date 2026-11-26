# Deep review coverage

Use this as a decision-tree checklist, not a script of questions. Mark each category confirmed, delegated, deferred, blocked, or not applicable. Inspect available sources first. Ask about unresolved, consequential decisions only.

| Domain | Issues to resolve |
|---|---|
| Purpose | Actual problem, intended users, success outcomes, baseline, why now |
| Scope | Must-haves, non-goals, invariants, compatibility, migration |
| Alternatives | Existing solution, incremental change, redesign, trade-offs |
| Architecture | Boundaries, ownership, data flow, dependencies, integration contracts |
| Correctness | Edge cases, error semantics, constraints, input validation, invariants |
| Safety | Authorization, secret handling, privacy, recovery, destructive effects |
| Operations | Deployment environment, resource limits, latency, cost, logging, rollback |
| Experience | User journeys, accessibility, maintainability, configuration and editing |
| Quality | Acceptance thresholds, test fixtures, reproducibility, realistic representative outputs |
| Delivery | Deliverables, versioning, supported environments, scope-change gates |

## Media and animation extension (when relevant)

- Reference evidence: identify files/versions inspected, observed shot and character traits, and uncertain or inaccessible evidence. Do not claim frame-by-frame inspection unless done.
- Art direction: character proportions, silhouettes, line treatment, depth, lighting, palettes, materials and stylistic constraints.
- Movement: rigging, pose readability, contact, collision, anticipation, timing, easing, arcs, camera framing, transitions and continuity.
- Sound/story: hook, script, pacing, narration, caption timing, mix, sound effects and audio continuity.
- Technical: resolution, frame rate, duration, renderer, available CPU/GPU, memory, encoding, portability and editable parameters.
- Verification: choose sample scenes that exercise risks (walking/contact, fast action, close-up, transitions, audio sync); compare against reference evidence; use the same test conditions before and after. Inspect actual frames/playback if possible; metadata alone cannot establish quality. Keep subjective judgments distinct from numeric checks.

## Example interview turn

**Q7 — Character outlines**
- Question: Should outlines be stable in screen space or scale with character distance?
- Why it matters: distance-scaled lines can disappear on wide shots, while fixed-width lines can dominate small characters.
- My recommended answer: use a clamped screen-space width, with a scene-level style override, and test it in near and far shots. This is a proposal until the renderer and reference frames are inspected.
- Alternative: world-space geometry outlines, easier in some renderers but sensitive to distance and mesh intersections.

Choose the recommendation, the alternative, or a different behavior.

## Example acceptance evidence

A rendering change is not complete because compilation succeeds. Require a reproducible render command, an output file that decodes, expected dimensions/duration, sampled frames showing the targeted trait, temporal review for motion/contact where available, and a regression render of unchanged scenes. Note absent playback or reference access explicitly. Set thresholds with the user rather than manufacturing numeric style scores.
