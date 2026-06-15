# Side Thread -> Main Thread Handoff: Notion Reauth Blocker

Timestamp: 2026-06-15 22:30 AEST

## User Instruction

User asked the side thread to back up the state for the main thread and handle the Notion connector issue next time.

## Current Truth

| Item | Status |
|---|---|
| Notion connector | blocked_reauth_required |
| Codex Study Timeline URL | `https://www.notion.so/37eb1a986ba680bdb5f9ea2367b08991?v=37eb1a986ba68040b4f4000cc8b21956&source=copy_link` |
| Requested Notion work | create/update Industrial 666 project page and align all Codex Study Timeline child page icons |
| Actual Notion mutation | none |
| Actual Notion backup | none, because fetch/search could not authenticate |
| Local Study Project prep | complete enough to resume |

## Evidence

The Notion app returned this error on both database fetch and `get_users(self)`:

```text
This app connection requires reauthentication before other actions on this app can succeed.
```

Because the connector could not fetch Notion content, the side thread did not create pages, update properties, change icons, or claim any Notion backup.

## Local Files To Restore State

| File | Purpose |
|---|---|
| `StudyProjects/industrial-666-roi-map/HANDOFF.md` | Primary project handoff. |
| `StudyProjects/industrial-666-roi-map/state.json` | Machine-readable project state. |
| `StudyProjects/industrial-666-roi-map/07_NOTION/notion_sync_log.csv` | Notion sync attempts and blockers. |
| `StudyProjects/industrial-666-roi-map/07_NOTION/codex_study_timeline_icon_audit_plan.csv` | Planned icon mapping for Codex Study Timeline pages. |
| `_assets/notion-icons/study-timeline-pages/industrial-666-roi-map-b-tech-v1.svg` | Prepared matching local icon asset. |
| `_system/study-project-orchestrator/CONNECTION_STATUS.md` | System-level connector status. |

## Paste This To Main Thread

```text
Side thread handoff: Notion connector is still blocked by reauthentication. Do not assume Notion backup, page creation, content sync, or Codex Study Timeline icon updates were completed.

Resume from:
- work/Notion/NotionBackup/20260615/side_thread_main_handoff_notion_reauth.md
- work/Notion/StudyProjects/industrial-666-roi-map/HANDOFF.md
- work/Notion/StudyProjects/industrial-666-roi-map/state.json
- work/Notion/StudyProjects/industrial-666-roi-map/07_NOTION/notion_sync_log.csv

After I fix Notion authentication, first fetch Codex Study Timeline database 37eb1a986ba680bdb5f9ea2367b08991, back up accessible Notion content to NotionBackup/YYYYMMDD, then create/update Industrial 666 ROI Map and align page icons using the existing blue/white B-tech icon style. Do not mutate Notion before fetch/schema/style inspection succeeds.
```

## Next Safe Resume Procedure

1. Reauthenticate the Notion connector.
2. Fetch `Codex Study Timeline` by URL or ID.
3. Fetch the data source schema and existing rows/pages.
4. Back up the fetched Notion content under `NotionBackup/YYYYMMDD/`.
5. Create or update `industrial-666-roi-map` in the existing database, preserving schema and style.
6. Set icons only after confirming the database's existing icon format supports the chosen icon source.
7. Update `notion_sync_log.csv`, `HANDOFF.md`, and `CONNECTION_STATUS.md`.

## Boundary

No Git commit or push was performed from this side thread because the worktree has unrelated existing dirty files.
