# GPU ML Systems & Model Training - Top1 Strategy

## Top1 Definition

Top1% for this project means practical training-systems judgment, not pretending to be a frontier lab after 90 days.

| Dimension | Top1 practical standard |
|---|---|
| Hardware judgment | Can estimate VRAM, throughput, bottlenecks, and local vs remote GPU ROI before running |
| Training mechanics | Can explain and inspect training loop, autograd, optimizer state, precision, checkpointing |
| Distributed strategy | Can choose DDP/FSDP/ZeRO/tensor/pipeline parallelism based on model and hardware constraints |
| Failure diagnosis | Can debug OOM, low utilization, dataloader stalls, NCCL errors, divergence, bad checkpoints |
| Cost control | Can turn training ideas into run contracts with budgets, stop conditions, and rollback |
| Agent safety | Can define what a training agent may run automatically and what must be budget-gated |

## High-Leverage Concepts

| Concept | Why it matters |
|---|---|
| VRAM decomposition | Prevents naive “model size fits GPU” mistakes |
| Activations and checkpointing | Often dominates training memory |
| Mixed precision | Major speed/memory lever with numerical risk |
| Gradient accumulation | Trades memory for time and optimization behavior |
| Data pipeline throughput | Many GPU runs are CPU/IO starved |
| DDP | Baseline distributed strategy when model fits per GPU |
| FSDP/ZeRO | Shards model states to fit larger models |
| Tensor parallelism | Splits large layers across GPUs |
| Pipeline parallelism | Splits model layers with bubble/utilization tradeoffs |
| NCCL collectives | Communication layer that often controls scaling |
| Checkpoint strategy | Determines recoverability and storage cost |
| Eval before scale | Prevents expensive useless training |
| Run contract | Converts vague ambition into budgeted executable experiment |

## Defer List

Do not prioritize these before the core gates are passed:

- Custom CUDA kernel authoring beyond conceptual/kernel-level profiling.
- Frontier-scale pretraining without explicit budget and cluster access.
- Exotic MoE/distributed optimizer details before FSDP/ZeRO/DDP are understood.
- Production MLOps platform buildout before experiment design and failure diagnosis are solid.
- Long cloud runs without stop conditions.

## Ability Tree

| Layer | Capabilities |
|---|---|
| Foundation | GPU/CPU/RAM/storage, CUDA model, PyTorch loop, memory math |
| Training | dataloading, precision, optimizer, checkpoint, profiling |
| Distributed | DDP, FSDP, ZeRO, NCCL, tensor/pipeline parallel |
| LLM systems | tokenizer, corpus, architecture config, scaling, eval |
| Operations | reproducibility, logging, remote GPU, cost caps, failure recovery |
| Expert judgment | choose strategy, reject bad runs, design agent-safe training workflows |

## Counterintuitive Rules

1. Bigger GPU does not automatically mean faster training if IO or communication is the bottleneck.
2. A model fitting in VRAM for inference does not mean it fits for training.
3. Distributed training can make a run slower if communication dominates.
4. Fine-tuning can be lower ROI than RAG or prompting if the problem is missing evidence, not model behavior.
5. A successful loss curve is not enough; eval, data leakage, reproducibility, and cost matter.
6. Agent automation is useful only after the run contract has hard budget and stop conditions.
