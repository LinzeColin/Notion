# Reminder Plan - GPU ML Systems & Model Training

Status: no dedicated reminder automation created yet  
Start date: 2026-06-30

## Reminder Purpose

The reminder exists to bring the user back to Codex for the daily Study Project session. The teaching surface remains Codex.

## Default Daily Return Prompt

```text
Continue GPU ML Systems & Model Training D01. 今天是第1/90天，先做硬件 profile。
```

## Automation Rule

If `study-project-daily-sync` cron automation is active, it should read this project state from GitHub and Notion directly. Do not rely on the current chat thread.
