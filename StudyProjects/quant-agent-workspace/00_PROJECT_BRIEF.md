# Quant Agent Workspace Study Project

Project slug: `quant-agent-workspace`
Timezone: Australia/Sydney
Start date: 2026-06-14
Planned end date: 2026-07-04
Duration: 21 days

## Goal

Build a Quant Agent Workspace that can independently run the full research and paper-validation loop:

`data -> research -> strategy generation -> anti-overfitting validation -> cost/impact stress testing -> portfolio risk -> paper forward validation -> broker-ready order intent -> human approval gateway`

## Hard Boundary

This project does not implement unattended live trading.

Allowed:

- market and fundamental data ingestion;
- public-source evidence mining;
- strategy hypothesis generation;
- backtesting and parameter scans;
- PBO / DSR / walk-forward / stress validation;
- paper trading or simulated execution;
- portfolio risk checks;
- broker-ready `OrderIntent` export;
- approval queue, kill switch, audit log, replay log.

Not allowed:

- autonomous real-money order submission;
- live broker credentials in code or GitHub;
- bypassing human approval;
- disabling kill switches;
- using private, non-public, or credential-leaked information.

## Success Criteria

By Day 21, the project should have:

- a Workspace Charter;
- a full module map;
- an `OrderIntent` schema;
- a strategy validation contract;
- a paper trading runbook;
- a risk-control matrix;
- a 21-day learning and build log;
- a final package spec for future implementation.

## Source Baseline

The project is grounded in:

- SEC Rule 15c3-5 market access risk controls.
- SEC FAQ on real-time monitoring and control of market access risk controls.
- FINRA algorithmic trading supervision guidance.
- ASIC automated trading / AI market integrity modernization.
- IBKR and Alpaca paper-trading documentation.
- Bailey / Lopez de Prado work on backtest overfitting and Deflated Sharpe Ratio.

