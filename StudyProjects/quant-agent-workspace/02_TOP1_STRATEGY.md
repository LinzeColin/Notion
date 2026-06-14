# Top 1% Strategy

## Definition

Top 1% practical capability for this project means the ability to design a quant-agent workspace that is:

- evidence-backed;
- falsifiable;
- resistant to backtest overfitting;
- aware of cost and market impact;
- controlled by portfolio-level risk rules;
- auditable;
- paper-forward validated;
- unable to bypass human approval for real-money execution.

## Ability Tree

| Capability | What good looks like | Failure mode |
|---|---|---|
| Evidence mining | Every market claim has source, timestamp, and confidence | Signal built on weak rumors |
| Strategy generation | Strategy hypothesis is explicit and testable | Parameter hacking |
| Backtest integrity | Costs, slippage, liquidity, survivorship, and look-ahead are handled | Beautiful but fake equity curve |
| Anti-overfitting | PBO / DSR / walk-forward checks gate promotion | Best backtest selected from many trials |
| Risk control | Position, drawdown, exposure, liquidity, and correlation limits exist | Strategy-level win destroys portfolio |
| Agent workflow | Each agent role has permissions and tool contract | Agent improvises unsafe actions |
| Paper execution | Paper run logs match the execution contract | Backtest cannot survive forward simulation |
| Approval gateway | Real broker action requires human confirmation | Autonomous trade escapes controls |

## Core Rule

The agent can be autonomous only inside bounded research and paper-validation loops. Real-money execution stays behind a hard approval boundary.

