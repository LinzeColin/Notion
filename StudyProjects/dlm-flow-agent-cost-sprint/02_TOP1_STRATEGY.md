# Top1 Strategy

## Top1 Definition

在这个 7 天 sprint 中，Top1% 不是数学推导最强，而是技术判断、成本判断、应用判断和工作流迁移能力足够强。

| Dimension | Top1% Behavior |
|---|---|
| 技术判断 | 不被“DLM 替代 GPT”“token 计费崩塌”等标题带偏，能拆成本、架构和应用场景。 |
| 成本判断 | 看到任何模型/agent 任务，都能先拆 Prefill、Decode、KV cache、steps、tool calls、retries。 |
| 应用判断 | 知道 DLM 的机会更可能先出现在 infill、局部编辑、并行候选、本地低延迟，而不是立刻替代通用聊天。 |
| 论文判断 | 能用一页纸解释 ELF 和 Cola DLM 的贡献、局限和下一步实验。 |
| ROI 判断 | 每个概念都能转成 Codex/Agent/本地模型的路由规则。 |

## High-Leverage Concepts

| Concept | Why It Matters |
|---|---|
| AR LM | 当前主流 LLM 成本和推理形态的基线。 |
| KV cache | AR 推理速度和显存成本的核心。 |
| Diffusion model | 理解 iterative refinement 和 block generation 的基础。 |
| Flow Matching | 理解连续生成路径和 vector field。 |
| Discrete DLM | 理解 mask/token state 上的文本扩散。 |
| Latent representation | 区分 token、embedding、hidden state、latent。 |
| VAE | 理解 text latent 如何被训练和重构。 |
| Latent prior | 理解 Cola DLM 的语义生成规律。 |
| ELF | continuous embedding flow 的代表路线。 |
| Cola DLM | continuous latent diffusion language model 的代表路线。 |
| Code infill | DLM 最有可能形成 ROI 的应用场景之一。 |
| Agent cost governance | 把模型能力变成可控工作流的关键。 |

## Defer List

| Defer | Reason |
|---|---|
| 完整推导 SDE/ODE 数学 | 7 天内 ROI 低，先掌握机制和成本。 |
| 从零训练 DLM | 需要 GPU、数据、工程资源，不适合本 sprint。 |
| 大规模 benchmark | 先做最小实验设计，不盲目跑。 |
| 宣称 DLM 替代 AR | 当前证据不足，必须场景化判断。 |
