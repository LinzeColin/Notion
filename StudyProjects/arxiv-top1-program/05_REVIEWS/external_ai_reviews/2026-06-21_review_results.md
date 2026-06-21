# External AI Review Results - 2026-06-21 - MATH math.PR D001

Project: arxiv-top1-program  
Session: MATH / math.PR Probability / 第1/30天  
Packet: `05_REVIEWS/external_ai_reviews/2026-06-21_review_packet.md`

## Reviewer Attempts

| Reviewer | Type | Status | Adopted |
|---|---|---|---|
| Pauli | Codex reviewer | completed | yes |
| Chandrasekhar | Codex reviewer | completed | yes |
| Socrates | Codex reviewer | completed | yes |
| ChatGPT | named external connector | blocked_unavailable | no |
| Claude | named external connector | blocked_unavailable | no |
| Perplexity | named external connector | blocked_unavailable | no |

Status: completed_with_blockers. Six traceable attempts are logged; three completed configured reviewers and three blocked named connectors. Do not describe this as six completed reviews.

## Consolidated Findings

| Finding | Severity | Decision |
|---|---|---|
| MATH D001 is sufficient to proceed to D002, but only with a D001 correction gate. | low | adopted |
| `random variable = 观测对象` is still imprecise; must be retested before D002 teaching. | medium | adopted |
| Do not claim remote GitHub sync without commit/push evidence. Current state is local Git working tree sync plus live Notion mutation. | medium | adopted |
| `2026-06-21_review_results.md` and 2026-06-21 review log rows must exist before state can point to review result. | medium | fixed in this file and log update |
| Balanced catch-up route should remain MATH D002 -> MATH D003 -> then PHYS/Q-FIN D004. | low | adopted |

## D002 Required Opening Gate

Before teaching MATH / `math.PR` D002, run this 5-minute gate:

1. Explain why `70% probability` does not guarantee the next event, and explicitly mention finite-sample fluctuation.
2. Split a trading signal into `sample space`, `event`, and `random variable`; random variable must be explained as a mapping/function from real outcome to computable value.
3. Compute whether a strategy with 80% win rate, +1 payoff, -5 loss, and 0.1 cost is worth doing.
4. For an agent claiming 90% confidence, name at least four checks: calibration, sample size, failure cost, tail risk, evidence quality, out-of-sample, or permission boundary.
5. Explain why new evidence changes probability: the condition changes the distribution/judgment basis.

Pass rule: at least 4/5 directionally correct, and item 2 must be correct. Otherwise D002 teaching pauses for D001 remediation.

## Adopted D002 Teaching Focus

MATH / `math.PR` D002 should teach `Conditional Probability and Bayesian Update` through mixed examples:

1. Agent confidence -> posterior probability is not action permission.
2. Trading signal -> posterior must pass EV, cost, slippage, and tail-risk gate.
3. Industrial alarm -> low probability can still dominate decision if loss severity is high.

Core misconception to test:

> 一个 agent 在新证据出现后，把成功概率从 70% 提到 85%，是否可以自动执行？必须追问 base rate、evidence reliability、conditional probability、calibration、payoff/loss、tail risk、执行成本和权限边界。

## Rejected / Deferred

- Reject a separate full D001 remediation day. The correction can be embedded as D002 opening gate.
- Reject moving PHYS/Q-FIN to D004 before MATH reaches D003, unless the user explicitly requests focus mode.
- Defer any claim of remote GitHub persistence until commit/push evidence exists.
