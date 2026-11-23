# 0001. Publish BSG standards as Agent Skills

- **Status:** Proposed
- **Date:** 2026-11-23
- **Deciders:** BSG admins

## Context

BSG members increasingly write backend code with AI coding agents. Our standards need to be in a form those agents load and follow, while staying readable for people.

## Options considered

### Option A: Agent Skills (SKILL.md folders)
- Pros: an open format supported by many coding agents; agents load a skill only when its description matches the task; plain Markdown that people can read and review.
- Cons: some agent-specific features aren't portable; descriptions must be written carefully or skills won't trigger.

### Option B: one large standards document (for example AGENTS.md)
- Pros: simple, one file.
- Cons: the whole document fills the agent's context on every task; hard to maintain as it grows.

## Decision

We will publish our standards as Agent Skills in this repository, one skill per area, with ADRs in `decisions/` for any change to a rule.

## Consequences

- Good: members can plug in only the skills they need; changes are reviewed like code.
- Bad, and accepted: contributors need to learn the skill format (the template helps).
- Follow-ups: validate skills in CI; write the "Wanted" skills listed in the README.
