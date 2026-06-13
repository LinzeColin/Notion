# Notion Backup Manifest

Generated: 2026-06-13
Timezone: Australia/Sydney
Backup path: `LinzeColin/Notion/NotionBackup/20260613/`
Backup type: connector-level snapshot

## Purpose

This backup was created before creating/importing a new Study Project workspace/database for the `AI` Study Project.

## Scope

The user-stated Notion structure is:

```text
Linz Dashboard
├── 个人价值增长
├── 制造业
├── Re:0
└── arXiv
```

Verified teamspace:

| Name | Type | ID | Role |
|---|---|---|---|
| Linz Dashboard | teamspace | `1aeb1a98-6ba6-813a-8420-0042760f36b1` | owner |

Fetched entities:

| Title | Type | ID | Data source |
|---|---|---|---|
| 个人价值增长 | database | `1b3b1a98-6ba6-804c-b123-d5f76675f163` | `collection://1b3b1a98-6ba6-8015-8857-000b3b9feec4` |
| 制造业 | database | `1b7b1a98-6ba6-808c-8813-eaa05da33645` | `collection://1b7b1a98-6ba6-8034-8616-000b8919db85` |
| Re:0 从零开始的异世界生活 | database | `37cb1a98-6ba6-804b-ace6-df86cd709bde` | `collection://37cb1a98-6ba6-8098-9d7e-000b83bdc0b2` |
| arXiv Taxonomy | database | `37cb1a98-6ba6-8083-8ccd-dc8c0931281b` | `collection://37cb1a98-6ba6-80a3-ae9e-000b6b455c93` |

## Saved Files

| File | Contents |
|---|---|
| `MANIFEST.md` | Backup scope, verified sources, limitations |
| `linz-dashboard-search-results.md` | Search results for Linz Dashboard-related pages/databases |
| `database-schema-snapshots.md` | Connector-fetched schema snapshots and source IDs |
| `backup-limitations.md` | Tool limitations and known gaps |

## Important Limitation

This is not a full official Notion workspace export. The current connector allowed search and fetch, but row-level query/export failed with `notion-query-data-sources not found`. Therefore this backup captures accessible top-level database metadata, schema, source URLs, search results, and known limitations.

Before destructive Notion operations, a full native Notion export should still be preferred. This workflow does not perform destructive Notion operations by default.
