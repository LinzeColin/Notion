# Study Project Orchestrator Connection Status

Generated: 2026-06-13
Timezone: Australia/Sydney
Status: connected

## Verified Connections

| System | Status | Evidence |
|---|---|---|
| GitHub | Connected with push access | Repository `LinzeColin/Notion`, default branch `main`, push permission verified |
| Notion | Connected with search/read access | Search found study-related pages and fetch verified `Codex Study Project 4周` |
| Codex Skill | Installed locally | `/Users/linzezhang/.codex/skills/study-project-orchestrator/` validated with `Skill is valid!` |

## Default Repository Rule

Each Study Project uses a top-level project folder:

```text
LinzeColin/Notion/<project-slug>/
```

Examples:

```text
LinzeColin/Notion/ai-agent/
LinzeColin/Notion/macro-investing/
LinzeColin/Notion/python-backend/
```

## Default Daily Sync Rule

Sync mode:

```text
after_user_returns_to_codex
```

Default sync content:

- Summary.
- Structured learning behavior.
- Key links.

Allowed when useful:

- Full Notion note body.

Excluded:

- Secrets.
- Tokens.
- Cookies.
- API keys.
- Private credentials.
- Unrelated private content.

## Notion Boundary

Notion is treated as a clean notebook. Codex may read relevant notes, propose layout improvements, build companion structure, and create indexes or visualization suggestions. Codex should not overwrite or pollute original notes unless explicitly requested.

## Multi-Project Rule

Multiple Study Projects may run at the same time. Before any read/write operation, the agent must identify the active `project-slug` using one or more of:

- Explicit project slug.
- Notion page URL or title.
- Domain or industry name.
- Current week/day code.
- `_system/study-project-orchestrator/PROJECT_INDEX.md`.

If multiple projects match, ask the user to choose from a numbered list.

## New Project Intake Rule

When a Study Project is triggered, the agent must first lock:

1. Learning goal.
2. Domain or industry.
3. Subdomain or concrete content focus.
4. Duration and daily time.
5. Weekly output type.

The agent should use numbered choices, multi-select matrices, and a default recommendation. The agent should not create a new project folder until these are locked or explicit defaults are accepted.

## Reminder Objective

Reminder systems such as NitroSend, Calendar, GitHub Issues, or local automation exist to make the user return to Codex daily. Long lesson content should not live in reminders by default.
