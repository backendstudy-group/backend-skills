# BSG Backend Skills

Backend engineering standards, decisions and processes from the **Backend Study Group (BSG)**, written as [Agent Skills](https://agentskills.io). Plug them into an AI coding agent and it builds, reviews and documents backend code the way BSG agrees it should be done.

Each skill is a folder with a `SKILL.md`: a short description that tells the agent *when* to use it, and instructions that tell it *how*. Agents load only the skills a task needs.

## Skills

| Skill | Use it when | Status |
| --- | --- | --- |
| api-design | Designing, changing or reviewing HTTP APIs | Wanted |
| database-migrations | Changing a schema on a live system | Wanted |
| architecture-decision-records | Making or documenting a technical decision | Wanted |
| project-structure | Laying out a new service or module | Wanted |
| error-handling | Defining errors, retries and failure behaviour | Wanted |
| logging-and-observability | Logs, metrics, traces, alerts | Wanted |
| authentication-and-authorization | Sessions, tokens, roles, permissions | Wanted |
| testing-strategy | What to test, where, and how much | Wanted |
| background-jobs-and-queues | Async work, retries, idempotency | Wanted |
| caching | What to cache, invalidation, TTLs | Wanted |
| configuration-and-secrets | Env vars, secret storage, rotation | Wanted |
| security-checklist | Reviewing a service before launch | Wanted |
| code-review | Reviewing a pull request | Wanted |
| git-workflow-and-commits | Branches, commit messages, releases | Wanted |
| ci-cd | Pipelines, environments, deploys, rollbacks | Wanted |
| data-modeling | Tables, relations, money, time, IDs | Wanted |
| incident-postmortems | Writing up an outage | Wanted |

Every skill is open for contributors. Start from [`templates/SKILL.md`](templates/SKILL.md) and see [CONTRIBUTING.md](CONTRIBUTING.md).

## Use the skills

**Claude Code:** copy or symlink the folders you want into `~/.claude/skills/` (for all your projects) or `.claude/skills/` in a repository (for that project and everyone who clones it).

```bash
git clone https://github.com/backendstudy-group/backend-skills.git
mkdir -p ~/.claude/skills
ln -s "$PWD/backend-skills/skills/"* ~/.claude/skills/
```

**Other agents:** Agent Skills is an open format supported by many coding agents. Point your tool at the `skills/` folder as its docs describe.

You don't call a skill by name. Ask normally ("add an endpoint to cancel an order", "write the migration to rename this column") and the agent picks the right skill from its description.

## How the standards are decided

Standards change through pull requests. Anything that changes a rule, not just its wording, comes with a decision record in [`decisions/`](decisions/), written from [`templates/decision.md`](templates/decision.md), so everyone can see why.

## License

MIT. See [LICENSE](LICENSE).
