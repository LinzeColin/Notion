# Reminder Plan

Purpose: bring the user back to Codex and keep the daily sync fail-closed.

## Active Automations

| Automation | ID | Kind | Schedule | Role | Status |
|---|---|---|---|---|---|
| Study Project Daily Sync | `study-project-daily-sync` | cron | daily 18:10 Sydney | Reads active Study Projects from index, checks missed study, sync gaps | ACTIVE |

## Default Return Prompt

```text
Continue quant-agent-workspace W01D01. Start with active recall: why good backtests are not enough, what permission is most dangerous for a trading agent, and what paper trading cannot prove.
```
