from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parent
def read(path):
    try:
        return (root / path).read_text(encoding="utf-8")
    except OSError:
        return ""

s = read("SKILL.md")
p = read("PROMPT.md")
r = read("README.md")
m = re.match(r"^---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: ([^\n]+)\n---\n", s)
body = s[m.end():] if m else ""
required = (
    "README.md", "COMPATIBILITY.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "examples/README.md", "templates/decision-ledger.md",
    "references/deep-review.md", "references/pressure-tests.md", "references/evaluation.md",
)
checks = {
    "valid frontmatter": bool(m and m[1] == "grillpower" and 1 <= len(m[2]) <= 1024),
    "skill and prompt identical": bool(body and p == body),
    "deep interview": "Ask one substantive question per turn" in s and "My recommended answer" in s,
    "actual approval gate": "No implementation before the user approves" in s and "Wait." in s,
    "capability fallback": all(x in s for x in ("Conversation only", "Read-only", "Editing without execution", "Editing plus execution")),
    "noninteractive safety": "If interactive replies are unavailable" in s and "do not simulate user answers" in s,
    "decision recovery": "On resumption" in s and "decision ledger" in s,
    "no automatic loops": "No automatic improvement cycles" in s and not re.search(r"up to\s+15", s, re.I),
    "bounded repairs": "two unsuccessful attempts" in s and "Repair only concrete defects" in s,
    "evidence traceability": "acceptance IDs" in s and "mark it unrun" in s,
    "required files": all(read(x) for x in required),
    "install visibility": "npx skills add clipcraftclients-art/grillpower --skill grillpower" in r,
    "benchmark honesty": "remain unmeasured" in r and "not a completed benchmark" in read("references/evaluation.md"),
    "no mandatory extra tools": "no mandatory extra tools" in s,
}

# Check relative Markdown links in all package documents; skip URLs and anchors.
missing = []
for doc in sorted(root.rglob("*.md")):
    if ".git" in doc.relative_to(root).parts:
        continue
    for target in re.findall(r"\[[^\]\n]+\]\(([^()\s]+)\)", doc.read_text(encoding="utf-8")):
        path = target.split("#", 1)[0]
        if not path or "://" in path or path.startswith(("mailto:", "data:")):
            continue
        if not (doc.parent / path).exists():
            missing.append(f"{doc.relative_to(root)}: {target}")
checks["relative links resolve"] = not missing

for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + " " + name)
for item in missing:
    print("MISSING " + item)
print(f"{sum(checks.values())}/{len(checks)} static checks passed")
sys.exit(0 if all(checks.values()) else 1)
