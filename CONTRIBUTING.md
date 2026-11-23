# Contributing

Thanks for helping. Every skill here should make an AI agent behave like a careful senior backend engineer from BSG.

## Add a skill

1. Pick a "Wanted" skill from the README, or open an issue to propose a new one. Comment on the issue so two people don't write the same skill.
2. Copy `templates/SKILL.md` to `skills/<skill-name>/SKILL.md`.
3. Fill it in. Long material (full examples, checklists, comparisons) goes in `skills/<skill-name>/references/` and is linked from `SKILL.md`.
4. Run `python3 scripts/validate.py`.
5. Open a pull request. Two maintainers approve before it merges.

## Rules for a good skill

- **Name:** lowercase letters, numbers and hyphens, up to 64 characters, the same as its folder.
- **Description** (up to 1024 characters): say what it does *and when to use it*. The agent decides from this line alone whether to load the skill.
- **Keep `SKILL.md` short:** under about 500 lines. Put depth in `references/`, one level deep.
- **Be specific:** rules an agent can follow and a reviewer can check. "Return 409 on a duplicate" beats "handle conflicts well".
- **Say why:** one line of reasoning per rule, so people can disagree with the reason, not just the rule.
- **Language-neutral first:** examples in at least two languages when code matters (for example TypeScript and Go).
- **Cite sources** for anything taken from a standard (RFCs, vendor docs).
- **Changing a rule?** Add a decision record in `decisions/`, copied from `templates/decision.md`, explaining the change.
