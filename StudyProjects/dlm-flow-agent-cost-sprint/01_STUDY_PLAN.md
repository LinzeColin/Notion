# 7-Day Study Plan

## Daily Structure

| Module | Minutes | Requirement |
|---|---:|---|
| 主动回忆 | 10 | 回答昨天 3 个核心问题。 |
| 深度讲解 | 35 | 概念、机制、误区、使用方式。 |
| 资料阅读 | 25 | 读学习包或关键论文段落，不全文乱读。 |
| 应用转化 | 20 | 转成 Codex / agent / 本地模型工作流判断。 |
| 输出物 | 20 | 每天必须生成表、图、memo 或实验设计。 |

## Day Map

| Day | Date | Topic | Core Question | Output |
|---:|---|---|---|---|
| D01 | 2026-06-14 | AR vs Diffusion LM + KV cache | 为什么 AR 逐 token 串行？为什么 KV cache 快但贵？ | AR 成本模型图 |
| D02 | 2026-06-15 | 扩散模型 + Flow Matching | 生成为什么可以理解为从噪声流向数据？ | diffusion / flow 对比图 |
| D03 | 2026-06-16 | 离散扩散语言模型 | 文本为什么比图像难扩散？ | AR vs DLM 机制对照表 |
| D04 | 2026-06-17 | ELF | 为什么在 continuous embedding space 做 language flow？ | ELF 一页拆解 |
| D05 | 2026-06-18 | VAE + latent representation + Cola DLM | 为什么先压缩成 latent 再生成？ | Cola DLM 架构图 |
| D06 | 2026-06-19 | 推理成本模型 + Agent 成本治理 | 真正烧钱的是 token，还是循环、工具、上下文和重试？ | Agent 成本治理模板 |
| D07 | 2026-06-20 | Code infill + 本地高速交互 | DLM 最可能先在哪里产生 ROI？ | 终局 memo |

## Scoring

| Score | Standard |
|---:|---|
| 1 | 只记住名词。 |
| 2 | 能复述定义。 |
| 3 | 能解释机制。 |
| 4 | 能判断适用场景和局限。 |
| 5 | 能把概念转成 agent / Codex / 本地模型工作流决策。 |
