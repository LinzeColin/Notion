# External AI Review Results - 2026-06-14

Project: arxiv-top1-program  
Calendar Global Day: D002  
Reviewer: Codex multi-agent reviewer (`multi_agent_v1`, nickname Gibbs)  
Status: completed

## Reviewer Summary

| Area | Reviewer suggestion | Decision | Reason |
|---|---|---|---|
| Market order wording | Replace “market what price” with “current immediately executable counterparty price”; market order has high fill certainty but price uncertainty. | Adopt | This directly improves trading judgment and prevents screen-price illusion. |
| Limit order wording | Limit order guarantees price condition, not fill; add queue/time priority. | Adopt | High ROI for understanding real execution and future price formation. |
| State wording | State is a computable description inside a theoretical framework, not reality itself. | Adopt | Fits user’s PHYS/AI transfer goal and avoids naive realism. |
| Stop order teaching | Stop price is a trigger, not guaranteed fill price; after trigger it becomes market or limit execution. | Adopt | Directly answers user’s question and links to risk control. |
| D003 prerequisite | Add 10 minutes on bid/ask spread + order book depth before price formation. | Adopt | Price formation is not learnable well without spread/depth mechanics. |
| ROI risk | User may memorize definitions without converting them into trading judgment questions. | Adopt | Add daily question: “今天这个概念让我避免哪一种亏钱错觉？” |

## Adopted Plan Change

D003 will start with a compact order book example before price formation:

1. bid = 当前最高买价。
2. ask = 当前最低卖价。
3. spread = 立即买卖要付出的价差。
4. depth = 每个价格层有多少可成交数量。
5. price moves when market orders consume available liquidity.

Then proceed to:

- Q-FIN: Price Formation - how order flow forms price.
- PHYS: Amplitude vs Probability - why quantum probability is not ordinary probability.

## New Daily Judgment Question

每次日课都加入：

> 如果我是交易系统，今天这个概念会让我避免哪一种亏钱错觉？

## Stop Order Explanation To Retain

Stop order 管的是“什么时候启动退出/进入动作”，不是“保证以什么价格成交”。如果市场跳空或 order book 缺少对手方，stop 被触发后仍可能在更差价格成交；stop-limit 可能控制价格但完全不成交。

## External Availability

- Codex multi-agent reviewer: completed.
- ChatGPT separate connector/session: blocked_unavailable.
- Claude connector/API/browser session: blocked_unavailable.
- Perplexity connector/API/browser session: blocked_unavailable.

External feedback is advisory. The adopted items were selected because they improve ROI, match the user’s learning style, and strengthen Top 1% practical judgment.

## PHYS quant-ph D003 Review - Nash

Reviewer: Codex multi-agent reviewer (`multi_agent_v1`, nickname Nash)
Status: completed
Scope: PHYS / `quant-ph` D003 amplitude vs probability teaching quality and next-step route.

| Area | Reviewer suggestion | Decision | Reason |
|---|---|---|---|
| Amplitude-like vs probability-like analogy | Adopt with guardrails: amplitude is an unobservable intermediate representation; probability is computed from amplitude and validated through repeated measurement distribution. | Adopt | This keeps the AI/trading analogy useful without incorrectly implying quantum probability is just ML prediction confidence. |
| User score | Keep 4/5, but correct the wording “真实行为验证” for physics. | Adopt | User caught intermediate vs result correctly; the missing piece is that `quant-ph` validation is about repeated-shot distribution, not a single real-world outcome. |
| Next validation example | Use single-qubit repeated measurement: `|psi> = sqrt(0.7)|0> + sqrt(0.3)|1>` gives approximate 70/30 outcomes over many shots. | Adopt | This is the cleanest bridge from amplitude to probability while preserving physics rigor. |
| Next queue | Continue PHYS D004 before returning to Q-FIN. | Adopt conditionally | It forms the minimal `quant-ph` loop: amplitude -> Born rule -> measurement -> repeated shots. Q-FIN D003 and MATH D001 remain pending, not skipped. |
| Stable decision rule | “先判断一个量能不能被直接观测；不能观测的是中间表示，能被重复实验统计验证的才进入概率/结果层。” | Adopt | This is precise enough for `quant-ph` and still useful for AI/RAG/trading score judgment. |

## User Scheduler Correction

After this review, the user corrected the routing logic: the arXiv rolling program should keep active archives synchronized by validated archive day. Therefore, the reviewer suggestion to continue PHYS D004 is downgraded from default route to optional focus-mode route.

Final routing decision:

| Priority | Archive | Reason |
|---:|---|---|
| 1 | Q-FIN / `q-fin.TR` D003 | Q-FIN is behind PHYS and should catch up. |
| 2 | MATH / `math.PR` D001 | MATH has not started and should be brought into the active-slot schedule. |
| 3 | PHYS / `quant-ph` D004 | Concept closure remains valuable but waits unless user explicitly chooses PHYS focus mode. |

## Q-FIN q-fin.TR D003 Review - Kierkegaard

Reviewer: Codex multi-agent reviewer (`multi_agent_v1`, nickname Kierkegaard)
Status: completed
Scope: Q-FIN / `q-fin.TR` D003 price formation teaching quality and next gate.

| Area | Reviewer suggestion | Decision | Reason |
|---|---|---|---|
| D003 mastery | Adopt with condition: 4/5 conceptual validation is fair, but usable mastery needs one concrete execution calculation. | Adopt | User understands order book formation qualitatively; before Q-FIN D004, user should calculate fill levels, last price, VWAP, and slippage on a small book. |
| Next example | Use LOB walk: `ask 100.00 x100`, `100.01 x200`, `100.03 x300`; market buy `250` fills `100@100.00 + 150@100.01`. | Adopt | This turns price formation from vocabulary into executable trading-agent judgment. |
| Stable agent rule | “先估可成交价格和执行成本；只有 expected edge > spread + fee + slippage + market impact + safety buffer 时才允许下单。” | Adopt | Prevents direction prediction from being treated as sufficient trade authorization. |
| Defer list | Defer adverse selection, toxic flow, maker inventory risk, queue-position modeling, optimal execution, HFT mechanics, and alpha/backtest discussion. | Adopt | Keeps D003 focused on executable order flow before advanced microstructure. |

## Adopted Q-FIN Guardrail

Q-FIN / `q-fin.TR` D003 remains validated at conceptual level, but Q-FIN D004 must not start until the user completes a concrete order-book walk calculation:

```text
ask 100.00 x100
ask 100.01 x200
ask 100.03 x300
market buy 250
```

Required outputs: fill levels, last price, VWAP, and slippage/cost reference.

## Adopted Guardrail

When teaching `quant-ph`, do not say “real-world validation” as if one observed result proves the model. Use:

> 真实验证看重复测量形成的分布，而不是单次结果。

For AI/trading transfer, it remains valid to say model confidence / signal / score must be externally calibrated and validated before becoming an action basis.
