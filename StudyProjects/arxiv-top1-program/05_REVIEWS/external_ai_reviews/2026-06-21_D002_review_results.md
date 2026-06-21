# External AI Review Results - 2026-06-21 - MATH math.PR D002

Project: arxiv-top1-program
Session: MATH / math.PR Probability / 第2/30天
Packet: `05_REVIEWS/external_ai_reviews/2026-06-21_D002_review_packet.md`

## Reviewer Attempts

| Reviewer | Type | Status | Adopted |
|---|---|---|---|
| Godel | Codex reviewer | completed | yes |
| Mencius | Codex reviewer | completed | yes |
| Carver | Codex reviewer | completed | yes |
| ChatGPT | named external connector | blocked_unavailable | no |
| Claude | named external connector | blocked_unavailable | no |
| Perplexity | named external connector | blocked_unavailable | no |

Status: completed_with_blockers. Six traceable attempts are logged; three completed configured reviewers and three blocked named connectors. Do not describe this as six completed reviews.

## Consolidated Findings

| Finding | Severity | Decision |
|---|---|---|
| D002 is sufficient to proceed to D003; no standalone remediation day is needed. | low | adopted |
| D003 must start with a Bayes/base-rate gate testing `P(E|A)` vs `P(A|E)`, false positives, posterior vs action permission. | medium | adopted |
| The D002 teaching chain was too engineering-like if read as a formula. Add precise Bayes form: `P(A|E) proportional to P(E|A) * P(A)`; evidence quality belongs to reliability/calibration, not the formula core. | medium | adopted |
| D003 should prioritize distribution shape, tail risk / drawdown, then variance and calibration. | medium | adopted |
| Balanced catch-up remains MATH D003 before PHYS/Q-FIN D004; Q-FIN D004 still requires LOB walk gate. | low | adopted |

## Required D003 Opening Gate

Before teaching D003, ask:

```text
P(A)=1%, P(E|A)=90%, P(E|not A)=9%.
After alarm E, what is P(A|E) approximately?
Why is it not 90%?
Even if posterior rises, can the agent execute automatically?
```

Expected direction:

```text
P(A|E) = P(E|A)P(A) / [P(E|A)P(A) + P(E|not A)P(not A)]
       = 0.90*0.01 / (0.90*0.01 + 0.09*0.99)
       ~= 9.2%
```

Action permission still requires EV, tail loss, cost, authorization, rollback, and audit.

## Required D003 Teaching Focus

1. Agent confidence: test Bayes reverse-condition error and calibration.
2. Trading signal: teach payoff distribution, EV, variance, drawdown, and left-tail loss.
3. Industrial alarm: teach low base rate, false positives, low-probability high-loss tail risk.

## Rejected / Deferred

- Reject pure variance-only D003. Variance is a summary; it cannot replace distribution shape and survival risk.
- Reject PHYS/Q-FIN D004 before MATH D003 unless user explicitly chooses focus mode.
- Defer advanced continuous distributions until the user can reason from discrete payoff distribution first.
