# Example conversations

These are synthetic illustrations of expected behavior, not actual model test runs.

## 1. Software — exports

**User:** Add report exports.

**Agent, Q1 — Data scope:** Should the export represent the user's current filtered view or all authorized records? A full export changes privacy, file size and performance requirements. **Recommendation:** filtered and authorized rows by default; explicit full export only if required. Alternative: full authorized dataset with quotas. Which scope should we use?

**User:** Filtered only.

**Agent, Q2 — Export workload:** Should the export be synchronous for small files or a background job? Large jobs could time out. **Recommendation:** use a synchronous export under an agreed row limit, then return a clear error or queue if larger exports are required. Alternative: always use a queue, with extra complexity. What is your expected maximum row count?

The agent records the answer and continues until the relevant acceptance criteria and risks are resolved. It requests full design approval before code changes.

## 2. Creative — animated short

**User:** Create a stylized animated short with the supplied references.

**Agent, Q1 — Fidelity:** Which matters most: matching character silhouette and motion style, or making environments more realistic? Both can conflict visually. **Recommendation:** prioritize silhouette and motion fidelity; preserve simplified environments unless the references support greater realism. Alternative: more realistic lighting, but with a higher render cost and possible style drift. Which is more important?

If reference media is not accessible, the agent marks fidelity observations unknown instead of inventing them. Before rendering, it agrees on duration, aspect ratio, story, motion, budget and representative visual acceptance checks.

## 3. Research — choose a tool

**User:** Decide which database we should use.

**Agent, Q1 — Workload:** Is the critical path transactional writes with consistency guarantees, or analytics over large historical datasets? The answer affects data layout and trade-offs. **Recommendation:** choose based on measured access patterns rather than popularity; collect the workload before selecting a database. Alternative: choose a familiar general-purpose database provisionally. Which workload dominates?

A chat-only agent can still interview, compare supplied evidence and produce a design; it cannot claim to have run performance benchmarks.

## 4. Completion handoff (illustrative)

- A1: export respects authorized filters — pass, evidence: focused integration test.
- A2: large export returns an actionable error — pass, evidence: boundary test.
- A3: UI accessibility — unrun, no browser available.
- Status: PARTIAL. Manual verification instructions included.

The agent stops when approved criteria pass or a real blocker prevents completion. It does not launch optional improvement loops.
