from pathlib import Path
import re
root = Path(__file__).resolve().parent
s = (root/'SKILL.md').read_text(encoding='utf-8')
checks = {
 'frontmatter': bool(re.match(r'^---\nname: grillpower\ndescription: Use when .+\n---\n', s)),
 'directory name': root.name == 'grillpower',
 'deep only': 'One workflow only: deep' in s and 'Ask one substantive question per turn' in s,
 'recommended answer': 'My recommended answer' in s,
 'approval gate': 'No implementation before the user approves' in s,
 'evidence gate': 'Run fresh, applicable tests' in s,
 'no automatic improvement cycles': 'No automatic improvement cycles' in s and not re.search(r'up to\s+15', s, re.I),
 'required failure repairs retained': 'Repair only concrete defects' in s and 'targeted retest' in s,
 'no fabricated delegation': 'Do not invent agent calls' in s,
 'reference exists': (root/'references/deep-review.md').is_file(),
 'pressure scenarios exist': (root/'references/pressure-tests.md').is_file(),
 'readme exists': (root/'README.md').is_file(),
}
for k,v in checks.items(): print(('PASS' if v else 'FAIL')+' '+k)
print(f'{sum(checks.values())}/{len(checks)} static checks passed')
raise SystemExit(0 if all(checks.values()) else 1)
