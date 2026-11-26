# Example conversations

Illustrations of intended behavior, not recorded evaluations.

## Coding

**User:** Build a report export feature.

**Round 1 — five decisions**

1. **Data scope:** Which records should be included? Recommended: authorized records matching current filters, to avoid accidental disclosure.
2. **Format:** Which file format? Recommended: CSV first, because it is widely supported. Alternative: XLSX for formatted reports.
3. **Size:** What should the initial size limit be? Recommended: measure typical workloads and set an explicit limit rather than allow unbounded exports.
4. **Access:** How is authorization enforced? Recommended: server-side checks for each export.
5. **Success:** How do we test it? Recommended: filtered results, unauthorized access and boundary tests.

**User:** Accept all except Q2, use XLSX.

**Agent:** Records Q1–Q5, then asks Q6–Q10 about remaining material decisions, adapted to XLSX. If only two remain, asks two. It does not start coding until the full design is approved.

## Creative project

**User:** Create a stylized animated short from references.

1. **Visual fidelity:** Recommended: match silhouette and motion before increasing realism.
2. **Duration:** Recommended: agree on a duration range suited to the story and platform.
3. **Narration:** Recommended: use a consistent narrator and sync actions to speech.
4. **Rendering:** Recommended: confirm available compute and use a representative preview before full export.
5. **Quality:** Recommended: define visible acceptance criteria for movement, camera, captions and audio.

If references are unavailable, the agent labels fidelity judgments uncertain. The next round uses actual answers.

## Research

**User:** Choose a database for our project.

1. **Workload:** Recommended: identify dominant access patterns before choosing a database.
2. **Consistency:** Recommended: clarify transactional requirements rather than assume eventual consistency is sufficient.
3. **Scale:** Recommended: use measured expected read/write volume and retention.
4. **Operations:** Recommended: prefer a maintainable system within the actual team's resources.
5. **Evaluation:** Recommended: define a representative comparison with actual benchmarks where possible.

A chat-only assistant can design an evaluation; it must not claim to have executed benchmarks.
