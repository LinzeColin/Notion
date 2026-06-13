# Reminder Plan

Purpose: bring the user back to Codex. Reminders do not replace the learning surface.

## Default Return Prompt

```text
Continue prompt-engineering-loop-engineering W01D01. Start with active recall, then build Prompt Contract v1 and sync Notion notes.
```

## Missed Study Rule

If no actual minutes are recorded by 18:00 Sydney on a study day, mark `missed_study_today: true` in `state.json` and use:

```text
未完成今天学习打卡。请优先返回并同步今日学习：Continue prompt-engineering-loop-engineering W01Dxx and sync my Notion notes.
```

