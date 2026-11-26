from pathlib import Path
import re
root = Path(__file__).resolve().parent
s = (root / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"^---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\n---\n", s)
body = s[match.end():] if match else ""
def present(path):
    return (root / path).is_file()
def contains_all(*terms):
    return all(term in s for term in terms)
checks = {
    "frontmatter": bool(match and match[1] == "grillpower" and len(match[2]) <= 1024),
    "deep only": contains_all("one portable workflow", "One workflow only: deep"),
    "one question": contains_all("Ask one substantive question per turn", "My recommended answer"),
    "approval": contains_all("No implementation before the user approves", "Wait."),
    "capability routing": contains_all("Conversation only", "Read-only files or web", "File editing without execution", "Editing plus execution"),
    "no fabricated tools": contains_all("Never invent file access", "Do not invent agent calls"),
    "noninteractive fallback": contains_all("If interactive replies are unavailable"),
    "context recovery": contains_all("On resumption", "observed / inferred / unknown"),
    "no cycles": contains_all("No automatic improvement cycles", "Repair only concrete defects") and not re.search(r"up to\s+15", s, re.I),
    "verification": contains_all("Run fresh, applicable tests", "mark it unrun"),
    "prompt parity": present("PROMPT.md") and (root / "PROMPT.md").read_text(encoding="utf-8") == body,
    "references": all(present(p) for p in ("references/deep-review.md", "references/pressure-tests.md", "COMPATIBILITY.md", "README.md")),
}
for k, v in checks.items():
    print(("PASS" if v else "FAIL") + " " + k)
print(f"{sum(checks.values())}/{len(checks)} static checks passed")
raise SystemExit(0 if all(checks.values()) else 1)
