# Daily Log - 2026-06-14 PHYS quant-ph D003

Project: arxiv-top1-program  
Timezone: Australia/Sydney  
Calendar Global Day: D002  
Archive: PHYS / `quant-ph` Quantum Physics  
Archive Day: 3/30  
Session Type: accelerated single-archive lesson and validation

## Archive Header

| Field | Value |
|---|---|
| Current Archive | PHYS / `quant-ph` Quantum Physics / 第 3/30 天 |
| Today Focus | Amplitude vs Probability；为什么量子概率不是普通随机性；如何迁移到 AI score / RAG similarity / trading signal 判断 |
| Main Rule Applied | 本次只讲一个 archive。Q-FIN 和 MATH 只保留在 next queue，不混入主教学内容。 |
| Next Queue | Q-FIN / `q-fin.TR` D003 Price Formation；MATH / `math.PR` D001 Probability as uncertainty compression |

## User Answer And Scoring

| Question | User Answer | Score 1-5 | Correction |
|---|---|---:|---|
| 如果一个 agent 说“我有 92% confidence，所以可以自动执行交易”，你应该用今天的概念怎么反驳它？ | “这只是中间量，模型预测结果，还不是真实实际结果，没有经过真实行为验证。” | 4 | 方向正确。更高精度表达：confidence / score / signal 是模型内部中间量，类似 amplitude-like computation；只有经过执行成本、滑点、费用、风控、回测外推、paper/live validation 和 calibration 后，才可能变成 probability-like 的行动依据。 |

## Concept Mastery

| Concept | Understanding 1-5 | Usage Clarity 1-5 | Evidence |
|---|---:|---:|---|
| Amplitude | 4 | 4 | 用户理解 amplitude 不是最终概率，而是中间计算量。 |
| Probability | 4 | 4 | 用户理解最终结果需要经过转换和验证，不能直接等同模型输出。 |
| Phase / Interference | 4 | 3 | 用户能说出 amplitude 有 phase，可能先抵消；后续需继续用公式和例子稳定掌握。 |
| AI score analogy | 4 | 4 | 用户已能把模型 confidence 迁移为“未验证中间量”。 |

## Corrected Core Notes

### 1. Amplitude 不是 probability

在 quantum physics 里，state 提供的通常不是直接概率，而是 probability amplitude。

```text
amplitude: α
probability: |α|^2
```

如果有多个不可区分路径通向同一个结果，规则不是先把概率相加，而是：

```text
先加 amplitude，再平方：
P(result) = |Amp(path1) + Amp(path2)|^2
```

这就是量子和普通随机性的关键差异。

### 2. 为什么 phase 重要

普通 probability 只有大小，不能互相抵消。  
Amplitude 有 magnitude 和 phase，因此不同路径的 amplitude 可以增强，也可以抵消。

这不是玄学，而是计算规则不同：

```text
普通随机性：probability 直接相加
量子随机性：amplitude 先相加，再平方成 probability
```

### 3. ROI 迁移：不要把中间量当现实结果

今天最重要的迁移不是量子公式本身，而是判断力：

```text
score 不是 truth
confidence 不是 correctness
similarity 不是 evidence
signal 不是 profit
```

AI / RAG / trading agent 里的很多数字都只是中间计算量：

| Scenario | 中间量 | 不能直接等同 | 必须补上的验证 |
|---|---|---|---|
| LLM | confidence / logprob / self-rating | 真实正确率 | calibration、eval、人工/规则验证 |
| RAG | similarity score | 答案正确率 | source 命中、rerank、引用检查、事实核验 |
| Trading | signal strength | 真实利润 | spread、depth、slippage、fee、latency、market impact |
| Agent | task confidence | 可安全执行 | sandbox、policy gate、hard rules、rollback、audit log |

### 4. 可复制决策规则

以后看到任何模型分数，先问：

```text
这是内部中间计算量，还是已经经过外部验证、校准、审计的行动依据？
```

如果只是内部中间量，只能用于候选排序、提醒、辅助判断。  
如果要进入自动执行、交易、生产系统，必须经过外部硬验证和硬规则边界。

## Today's Standard Answer

如果一个 agent 说“我有 92% confidence，所以可以自动执行交易”，标准反驳是：

> 92% confidence 只是模型内部中间量，不是经过真实执行验证的概率，也不是可交易收益。它还没有经过校准、回测外推、paper/live validation、交易成本、滑点、流动性、延迟、market impact 和风控边界验证。所以它只能作为候选信号，不能直接作为真实下单授权。

## Decision Rule For User's Agent Systems

| Decision Layer | Allowed Use |
|---|---|
| Internal model score | 排序、筛选、提示、候选生成 |
| Calibrated probability | 风险评估、阈值判断、策略比较 |
| Executable action | 必须通过硬规则、日志、权限、回滚、风控、真实验证 |

## Status

PHYS / `quant-ph` D003 validated at usable level. User can explain the core distinction between intermediate score/amplitude-like computation and externally validated result/probability-like decision input.

## Next Lessons

| Queue | Archive | Next Lesson |
|---:|---|---|
| 1 | Q-FIN / `q-fin.TR` | D003 Price Formation：价格如何由 order book、bid/ask、depth、aggressive/passive orders 形成 |
| 2 | MATH / `math.PR` | D001 Probability as uncertainty compression：概率如何把不确定性变成可计算对象 |
| 3 | PHYS / `quant-ph` | D004 Measurement + Born rule + repeated shots + Observable：等低天数 archive catch up 后再补完物理闭环 |

## Sync Requirements

| Item | Status |
|---|---|
| GitHub daily log | created |
| Metrics update | success |
| State update | success |
| Notion PHYS page sync | success |
| External review handshake | partial success: Codex reviewer Nash completed; ChatGPT/Claude/Perplexity unavailable |

## External Review Adoption

| Reviewer Point | Decision |
|---|---|
| Do not overstate AI/trading analogy as literal quantum amplitude. | Adopted. The phrase is only an analogy for “internal intermediate quantity,” not a physics identity. |
| For `quant-ph`, validation means repeated-measurement distribution, not one real-world outcome. | Adopted. Future PHYS lessons will use repeated shots / Born rule language. |
| Continue PHYS D004 next to complete the concept loop. | Superseded by user correction. Balanced catch-up is the default scheduler; Q-FIN D003 comes first, then MATH D001. PHYS D004 waits unless the user explicitly chooses focus mode. |
