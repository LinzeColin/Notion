# arXiv Mathematics

## 路线规则

- 规则：`1 archive = 30 天`
- archive 数量：`32`
- 路线窗口：`2026-06-15 -> 2029-01-29`
- 当前 active archive：`math.PR` Probability，第 1/30 天
- GitHub 真相源：`LinzeColin/Notion/StudyProjects/arxiv-top1-program/10_PROGRAM_STATE/group_routes/MATH.csv`

## 前 10 个学习顺序

1. `math.PR` - Probability：先把不确定性压缩成可计算分布，服务 Q-FIN、PHYS、AI agent 和风险判断。
2. `math.ST` - Statistics Theory：学习统计推断、证据质量、估计和检验。
3. `math.OC` - Optimization and Control：连接控制、运筹、动态决策和系统优化。
4. `math.IT` - Information Theory：理解信息、编码、压缩和不确定性边界。
5. `math.NA` - Numerical Analysis：理解数值算法、误差和科学计算可靠性。
6. `math.DS` - Dynamical Systems：理解动态系统、稳定性、复杂演化和长期预测边界。
7. `math.FA` - Functional Analysis：理解函数空间、算子和现代分析语言。
8. `math.AP` - Analysis of PDEs：理解偏微分方程、连续系统和稳定性。
9. `math.CO` - Combinatorics：理解离散结构、图和组合优化。
10. `math.LO` - Logic：理解形式系统、证明、可判定性和严谨推理边界。

完整 32 个 archive 顺序在 GitHub route file 中维护。

## 学习笔记

### 2026-06-21 · D001 · `math.PR` Probability

#### 当前进度

- Calendar Day：D009
- Archive Day：1/30
- 状态：D001 validated with correction
- GitHub log：`StudyProjects/arxiv-top1-program/04_DAILY_LOGS/2026-06-21_MATH_math.PR_D001.md`

#### D001 核心：Probability as uncertainty compression

- 概率不是“下一次一定发生”，而是把一类不确定情况压缩成可计算的分布结构。
- `70% probability` 不是单次保证，也不是有限样本必然精确 70%；有限样本会波动，长期频率或模型分布才提供约束。
- 数学链条是：现实不确定性 -> sample space -> event -> random variable -> distribution -> expected value / variance / tail risk -> decision。

#### 用户复述评分

- Q1：用户已理解 70% 是长期/分布意义，不是单次保证。评分 4/5。
- Q2：用户把 random variable 说成“观测对象”。方向接近，但需要修正为“把现实不确定结果映射成可计算数字的规则/函数”。评分 3/5。
- Q3：用户指出 Expected Value、Payoff。方向正确，但还要补充 loss distribution、交易成本、样本量、out-of-sample、最大回撤和 tail risk。评分 3/5。

#### ROI 用法

以后看到任何 trading signal、agent confidence、模型胜率、RAG similarity、工业报警预测，都不要只问“准不准”。先问：

1. Event 是什么？
2. Random variable 把现实结果映射成了什么数字？
3. Distribution 来源是什么？
4. Expected Value 是否扣除了成本和损失？
5. Tail risk 是否能承受？

#### 下次进入

下一课按 balanced catch-up 进入 `MATH / math.PR` D002：Conditional Probability and Bayesian Update，新信息如何改变概率判断。

### 2026-06-21 · 外部复审采纳

- 复审状态：completed_with_blockers。3 个 Codex reviewer completed；ChatGPT、Claude、Perplexity connector 不可用，已记录 blocked_unavailable。
- D001 可以进入 D002，但只能带纠偏进入，不能视为稳固掌握。
- D002 开头必须做 5 分钟补测：finite-sample fluctuation、random variable 映射规则、EV/payoff/tail risk、agent confidence 校准。
- D002 例子顺序：agent confidence -> trading signal -> industrial alarm。
- 路线保持：`MATH D002 -> MATH D003 -> PHYS/Q-FIN D004`，除非用户明确要求 focus mode。

### 2026-06-21 · D002 · `math.PR` Conditional Probability and Bayesian Update

#### 当前进度

- Calendar Day：D009
- Archive Day：2/30
- 状态：D002 validated
- GitHub log：`StudyProjects/arxiv-top1-program/04_DAILY_LOGS/2026-06-21_MATH_math.PR_D002.md`

#### D002 核心

- `P(A|B)` 是在 B 条件过滤后的世界里，A 占多少比例。
- `P(B|A)` 是在 A 条件过滤后的世界里，B 占多少比例。
- Bayesian Update 更新的是“在新证据条件下，对目标事件概率分布/信念强度的估计”，不是直接更新执行权限。

#### 用户复述评分

- `P(A|B)` vs `P(B|A)`：5/5。用户准确区分了两个条件过滤世界。
- posterior vs action gate：5/5。用户能列出 prior、evidence、evidence reliability、`P(A|Evidence)`、EV、tail risk、posterior 只够提醒还是执行。
- Bayesian Update 标准句：4/5。用户掌握组件，但后续需要继续强化“更新概率分布/信念强度，不更新执行许可”。

#### ROI 用法

当 agent 把成功概率从 70% 更新到 85%，不能直接自动执行。必须继续检查：prior、evidence quality、likelihood、posterior、EV、tail risk、成本、权限边界、回滚和审计。

#### 下次进入

下一课按 balanced catch-up 进入 `MATH / math.PR` D003：Distribution, variance, tail risk。目标是防止只看平均值、胜率或 posterior，忽略大亏损和极端风险。

### 2026-06-21 · D002 外部复审采纳

- 复审状态：completed_with_blockers。3 个 Codex reviewer completed；ChatGPT、Claude、Perplexity connector 不可用，已记录 blocked_unavailable。
- D002 可以进入 D003，不需要单独返工。
- 纠偏：Bayes 数学核心应写成 `P(A|E) ∝ P(E|A) * P(A)`；evidence quality 属于 reliability / calibration / source audit 层，不是公式本体。
- D003 开头必须先测 base rate / false positive：`P(A)=1%`，`P(E|A)=90%`，`P(E|not A)=9%` 时，`P(A|E)` 约为 9.2%，不是 90%。
- D003 重点顺序：distribution shape -> tail risk / drawdown -> variance -> calibration。
- 路线保持：MATH D003 先于 PHYS/Q-FIN D004；Q-FIN D004 仍需 LOB walk gate。
