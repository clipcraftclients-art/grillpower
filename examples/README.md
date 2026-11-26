# Example conversations

Illustrative examples, not recorded evaluations. Recommendations below assume the stated constraints and may change with actual project evidence.

## Coding: report export

Assume a small web app with existing filters and server-side authorization.

**Q1 — Data scope**
- A. Current authorized filtered records (Recommended)
- B. All authorized records
- Why: matches the view without expanding the export scope.

**Q2 — File format**
- A. XLSX
- B. CSV (Recommended)
- C. JSON
- Why: a simple tabular export does not yet need spreadsheet formatting.

**Q3 — Size handling**
- A. Unlimited requests
- B. Asynchronous jobs for every export
- C. Explicit measured size limit (Recommended)
- Why: avoids unbounded work while keeping ordinary exports simple.

**Q4 — Authorization**
- A. Recheck permissions on the server (Recommended)
- B. Reuse a server-issued scoped export token
- Why: fits the existing authorization path without introducing another token mechanism.

**Q5 — Verification**
- A. Manual testing only
- B. Focused integration tests for filters, permissions and limits (Recommended)
- Why: covers the highest-risk behavior repeatably.

User: 1A, 2A, 3C, 4A, 5B.

The agent records these choices (including XLSX instead of CSV), then asks the next batch of unresolved questions. Accepting one or all recommendations never replaces design approval.

## Creative and research

Use the same format for creative decisions (reference fidelity, style, motion, budget and quality) and research decisions (scope, evidence, methods, uncertainty and acceptance). Select one best option for each actual project, not a universal default. A chat-only assistant may draft an evaluation but cannot claim to have executed tests or renders.
