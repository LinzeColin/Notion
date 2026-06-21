# Teaching Adjustments

Updated: 2026-06-14
Timezone: Australia/Sydney

## Daily arXiv Session Header And Single-Archive Teaching Rule

每次 arXiv 日课开头必须先明确显示当前学习位置，避免用户不知道今天到底在学哪个 archive。不要只说 group，必须说 group 里的哪一个 archive。

固定格式：

| Field | Value |
|---|---|
| Global Day | Dxxx |
| Current Archive | Group / archive_code archive_name / Archive day out of 30 |
| Today focus | 本 archive 的一个核心概念 |
| Queue | 其他 active archive 只列为下一步排队，不展开讲解 |

示例：

| Field | Value |
|---|---|
| Global Day | D003 |
| Current Archive | PHYS / quant-ph Quantum Physics / 第3/30天 |
| Today focus | Amplitude vs Probability |
| Queue | Q-FIN q-fin.TR D003、MATH math.PR D001 排队，不在本次正文展开 |

强制规则：

- 一次输出只讲一个 archive。
- 本文教学、例子、主动回忆、练习任务必须围绕同一个 archive。
- 其他 archive 只能出现在 `Next Queue` / `Upcoming Lessons` 表格里。
- 讲解必须详细、专业、全面、深度，不能只给一句定义或让用户自己猜模板。

## Notion Sync Rule

- 每次 arXiv 日课结束后，不能只同步 GitHub；如果 `state.json` 中存在对应 Notion page，必须先 fetch 页面格式，再把简洁中文学习笔记同步到对应 Notion 页面。
- Notion 是笔记本，不是数据库污染区；只追加 `学习笔记` 或同页面同格式内容，不新建乱页、不改其他 workspace。
- 同步后必须在 GitHub `07_NOTION/notion_sync_log.csv` 或等价文件记录：日期、session、page、sync scope、结果。
- 如果 Notion connector 不可用，必须在 GitHub daily log 或 sync log 里显式记录 blocker，不能沉默跳过。

## External AI Review Handshake Rule

- 每次 arXiv 日课完成 GitHub 和 Notion 记录后，必须生成一个外部 AI 评审 packet，路径默认：`05_REVIEWS/external_ai_reviews/YYYY-MM-DD_review_packet.md`。
- Packet 必须包含：当天 GitHub log、Notion 笔记链接或摘要、用户学习要求、当前弱点、下一步计划、Top 1%/ROI 目标、需要外部 reviewer 检查的问题。
- 如果 ChatGPT、Claude、Perplexity 或其他 AI agent connector/API/browser session 可用，才实际发起握手评审；必须记录 reviewer、输入范围、建议、采纳/拒绝理由。
- 如果外部 reviewer 不可用，必须在 `05_REVIEWS/external_ai_reviews/external_review_log.csv` 记录 `blocked_unavailable`，不能假装完成。
- 外部 AI 建议只作为二级评审输入。不能覆盖用户明确要求、项目锁定范围、安全边界和 GitHub/Notion 的事实记录。
- 采纳建议前，Codex 必须判断其是否高 ROI、是否符合用户学习风格、是否有助于 Top 1% 判断力，并在需要时用权威来源验证。

## Teaching Fit

- 当用户说“模板不知道怎么填”时，不继续要求用户填模板；先给标准答案、反例、类比和可复制表达，再让用户用自己的话复述。
- 对金融市场概念，优先用真实交易流程讲解：报价、下单、撮合、成交、滑点、费用、风控、仓位、退出。
- 每个概念都必须回答“这个概念我应该怎么用”，不能只给定义。
- 2026-06-21 MATH / `math.PR` D001：用户能抓住长期频率、Expected Value、Payoff 的主线，但 `random variable` 容易说成“观测对象”。后续数学课必须固定使用“现实对象 -> 可计算数字 -> distribution -> decision”的链条，并把有限样本波动、variance、tail risk 加进交易/agent 例子。
- 2026-06-21 MATH / `math.PR` D002：用户对 `P(A|B)` vs `P(B|A)` 和 posterior/action gate 理解较快。后续应继续用 agent confidence、trading signal、industrial alarm 三类例子，避免纯数学抽象；D003 必须压实 distribution、variance、tail risk，防止只看 posterior mean 或 win rate。
- D002 reviewer correction：Bayes 公式要先给数学精确形式 `P(A|E) proportional to P(E|A) * P(A)`；evidence quality 放在 reliability/calibration/source audit 层。D003 开头必须测试 base rate 和 false positive，防止用户把 `P(E|A)` 误当 `P(A|E)`。
