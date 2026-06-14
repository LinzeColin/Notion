# 7-Day Study Plan

## Zero-Base Patch Integration

Source: `/Users/linzezhang/Downloads/dlm_zero_base_patch_zh.zip`

This patch does not widen the sprint. It adds a zero-base ramp before the existing advanced route, so every day starts from an explainable mental model before moving into papers, cost models, or agent workflow decisions.

Core cognitive chain:

```text
文字 -> token -> embedding -> AR -> KV cache -> diffusion -> latent -> Flow Matching -> ELF / Cola DLM -> infill / local interaction / cost governance
```

## 8 Mini-Lessons Compressed Into 7 Days

| Mini Lesson | Merged Into | Purpose |
|---|---|---|
| token 和语言模型 | D01 | Build the base unit of text generation and cost. |
| AR 模型 | D01 | Understand the current LLM inference baseline. |
| KV Cache | D01 | Connect speed, long context, memory, and cost. |
| 扩散模型 | D02 | Build the draft-to-refinement intuition. |
| embedding 与 latent | D03-D05 | Separate surface tokens from internal semantic space. |
| Flow Matching | D02 | Understand generation as learned movement from noise to data. |
| ELF 与 Cola DLM | D04-D05 | Compare embedding-space flow and latent-space diffusion. |
| code infill / local interaction / cost governance | D06-D07 | Convert model mechanisms into Codex, agent, and local workflow ROI. |

## Daily Structure

| Module | Minutes | Requirement |
|---|---:|---|
| 零基础 gate | 10 | 先用白话解释当天底层概念，不允许直接跳论文术语。 |
| 主动回忆 | 10 | 回答昨天 3 个核心问题。 |
| 深度讲解 | 35 | 概念、机制、误区、使用方式。 |
| 资料阅读 | 20 | 读学习包或关键论文段落，不全文乱读。 |
| 应用转化 | 20 | 转成 Codex / agent / 本地模型工作流判断。 |
| 输出物 | 20 | 每天必须生成表、图、memo 或实验设计。 |

## Day Map

| Day | Date | Topic | Zero-Base Gate | Core Question | Practice | Output |
|---:|---|---|---|---|---|---|
| D01 | 2026-06-14 | AR vs Diffusion LM + KV cache | token、语言模型、AR、KV cache | 为什么 AR 逐 token 串行？为什么 KV cache 快但贵？ | 用一段自己的话拆 token，并画 prefill/decode/KV cache 成本链。 | AR 成本模型图 |
| D02 | 2026-06-15 | 扩散模型 + Flow Matching | diffusion 是“草稿多轮变清楚”，Flow Matching 是“学移动方向” | 生成为什么可以理解为从噪声流向数据？ | 把写文章拆成粗稿、补全、润色三轮，对应 diffusion/refinement。 | diffusion / flow 对比图 |
| D03 | 2026-06-16 | 离散扩散语言模型 | embedding 是文字坐标，latent 是语义草图 | 文本为什么比图像难扩散？ | 区分 token、embedding、hidden state、latent，并解释离散文本的难点。 | AR vs DLM 机制对照表 |
| D04 | 2026-06-17 | ELF | ELF 在 embedding space 做 flow，最后回到 token | 为什么在 continuous embedding space 做 language flow？ | 用“先在语义坐标里移动，最后翻译回文字”解释 ELF。 | ELF 一页拆解 |
| D05 | 2026-06-18 | VAE + latent representation + Cola DLM | VAE 是压缩器 + 解压器，latent prior 是合理语义草图的分布 | 为什么先压缩成 latent 再生成？ | 画 text -> encoder -> latent -> diffusion -> decoder -> text。 | Cola DLM 架构图 |
| D06 | 2026-06-19 | 推理成本模型 + Agent 成本治理 | 成本不只 token，还有工具调用、文件读取、测试、重试、上下文恢复 | 真正烧钱的是 token，还是循环、工具、上下文和重试？ | 把一次 Codex/agent 任务拆成预算表和停止条件。 | Agent 成本治理模板 |
| D07 | 2026-06-20 | Code infill + 本地高速交互 | infill 是补中间，local interaction 是低延迟、低成本、可撤销的小任务流 | DLM 最可能先在哪里产生 ROI？ | 写一份 Codex infill 任务包，并判断本地快模型 vs 云端强模型分工。 | 终局 memo |

## Daily Zero-Base Check Questions

| Day | Must Answer Before Advanced Teaching |
|---:|---|
| D01 | token 为什么影响成本？AR 为什么天然串行？KV cache 缓存什么？ |
| D02 | diffusion 和普通续写的直觉差异是什么？Flow Matching 学终点还是路线？ |
| D03 | embedding 和 latent 的区别是什么？为什么文本不像图像一样天然连续？ |
| D04 | ELF 为什么不直接在 token 上做 flow？continuous embedding space 的好处和风险是什么？ |
| D05 | VAE 为什么是 Cola DLM 的关键？latent prior 管的是什么？ |
| D06 | agent 成本为什么会被循环、工具和上下文放大？哪些成本必须硬限制？ |
| D07 | infill 和续写有什么不同？为什么本地高速交互不追求最聪明模型？ |

## Scoring

| Score | Standard |
|---:|---|
| 1 | 只记住名词。 |
| 2 | 能复述定义。 |
| 3 | 能解释机制。 |
| 4 | 能判断适用场景和局限。 |
| 5 | 能把概念转成 agent / Codex / 本地模型工作流决策。 |
