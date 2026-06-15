# Notion Note Index

| Date | Notion object | Status | Notes |
|---|---|---|---|
| 2026-06-15 | Linz Dashboard / Codex Study Timeline | blocked_reauth_required | Notion connector returned reauthentication requirement during search/fetch. No Notion write performed. |
| 2026-06-15 | Codex Study Timeline child page icons | blocked_reauth_required | User requested all child page icons be completed according to style/rules. Local matching icon asset created, but Notion mutation is blocked until reauthentication. |
| 2026-06-16 | Codex Study Timeline / Industrial 666 ROI Map | partial_chrome_fallback_synced | Chrome fallback created/updated the timeline row and verified Project, Date range, and `industrial taxonomy` tag. Page body and icon are not synced. |

## Icon Asset Prepared

| Asset | Purpose | Status |
|---|---|---|
| `_assets/notion-icons/study-timeline-pages/industrial-666-roi-map-b-tech-v1.svg` | Blue/white B-tech icon for `industrial-666-roi-map` timeline page | ready_local |
| `07_NOTION/codex_study_timeline_icon_audit_plan.csv` | Known Codex Study Timeline page-to-icon mapping for post-reauth bulk sync | ready_local |

## Sync Rule

When Notion access is restored or a safer confirmed Chrome upload flow is used:

1. Fetch `Linz Dashboard` and `Codex Study Timeline` schema/style first.
2. Back up accessible relevant content to `LinzeColin/Notion/NotionBackup/YYYYMMDD/`.
3. Open the existing `Industrial 666 ROI Map` row/page, not a duplicate page.
4. Sync concise Chinese notebook content only.
5. Match existing icon style. Do not use random emoji.
6. Set all child page icons in `Codex Study Timeline` to matching blue/white B-tech assets where pages are missing icons or use mismatched random emoji/generic icons.
