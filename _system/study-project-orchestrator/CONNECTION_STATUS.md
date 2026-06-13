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

## Repository Structure Rule

System files live under:

```text
LinzeColin/Notion/_system/
```

Study Project folders live under:

```text
LinzeColin/Notion/StudyProjects/<project-slug>/
```

Notion backups live under:

```text
LinzeColin/Notion/NotionBackup/YYYYMMDD/
```

Examples:

```text
LinzeColin/Notion/StudyProjects/ai/
LinzeColin/Notion/StudyProjects/macro-investing/
LinzeColin/Notion/StudyProjects/python-backend/
LinzeColin/Notion/NotionBackup/20260613/
```

## Notion Workspace Rule

The user's Notion structure is:

```text
Linz Dashboard
├── 个人价值增长
├── 制造业
├── Re:0
└── arXiv
```

For every new Study Project:

1. Create the new Study Project database/page under `Linz Dashboard` as a peer to the existing workspaces.
2. Do not modify `个人价值增长`, `制造业`, `Re:0`, `arXiv`, or other existing workspaces unless explicitly requested.
3. Existing workspaces are read-only by default.
4. Before creating/importing a new Notion Study Project workspace/database, back up currently accessible relevant Notion content to `NotionBackup/YYYYMMDD/`.

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

For broad fields, the agent must propose high-ROI adjacent subdomains, industry boards, practical use cases, automation opportunities, and frontier areas before locking the scope.

The agent should use numbered choices, multi-select matrices, and a default recommendation. The agent should not create a new project folder until these are locked or explicit defaults are accepted.

## Reminder Objective

Reminder systems such as NitroSend, Calendar, GitHub Issues, or local automation exist to make the user return to Codex daily. Long lesson content should not live in reminders by default.
