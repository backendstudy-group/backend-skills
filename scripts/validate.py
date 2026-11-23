#!/usr/bin/env python3
"""Check every skills/<name>/SKILL.md against the Agent Skills basics."""
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
root = Path(__file__).resolve().parent.parent / "skills"
errors = []

for skill_dir in sorted(p for p in root.iterdir() if p.is_dir()):
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"{skill_dir.name}: missing SKILL.md")
        continue
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"{skill_dir.name}: SKILL.md must start with YAML frontmatter between --- lines")
        continue
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append(f"{skill_dir.name}: frontmatter needs a name")
    elif name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name '{name}' must match the folder name")
    elif len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{skill_dir.name}: name must be lowercase letters, numbers and hyphens, up to 64 characters")
    if not description:
        errors.append(f"{skill_dir.name}: frontmatter needs a description")
    elif len(description) > 1024:
        errors.append(f"{skill_dir.name}: description is {len(description)} characters, the limit is 1024")
    lines = text.count("\n")
    if lines > 500:
        errors.append(f"{skill_dir.name}: SKILL.md is {lines} lines; move detail into references/")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"{len([p for p in root.iterdir() if p.is_dir()])} skills OK")
