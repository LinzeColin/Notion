# GPU ML Systems & Model Training - 90-Day Plan

Start: 2026-06-30  
End: 2026-09-27  
Timezone: Australia/Sydney  
Mode: concept-first, experiment-second, evidence-logged

## Operating Rule

Every day must produce one reusable artifact: profile table, concept card, benchmark result, failure diagnosis, decision matrix, run contract, diagram, or training memo. Notes alone are insufficient.

## Phase Route

| Phase | Dates | Focus | Required output |
|---|---|---|---|
| Phase 1 | 2026-06-30 to 2026-07-13 | Hardware, CUDA, PyTorch training loop, memory math | Hardware profile + single-GPU baseline |
| Phase 2 | 2026-07-14 to 2026-07-27 | Data pipeline, precision, optimizer, checkpointing, profiling | Training bottleneck report |
| Phase 3 | 2026-07-28 to 2026-08-10 | DDP, FSDP, ZeRO, NCCL, communication bottlenecks | Distributed strategy decision matrix |
| Phase 4 | 2026-08-11 to 2026-08-24 | LLM architecture, tokenizer, model/data scaling, Megatron/DeepSpeed | Mini LLM training design spec |
| Phase 5 | 2026-08-25 to 2026-09-07 | Fine-tuning, LoRA, full FT, eval, experiment tracking | Training experiment protocol |
| Phase 6 | 2026-09-08 to 2026-09-21 | Multi-GPU/remote GPU operations, fault recovery, cost governance | GPU training operations runbook |
| Final | 2026-09-22 to 2026-09-27 | Capstone and review | GPU ML Systems playbook v1 |

## First 14 Days

| Day | Date | Theme | Required output |
|---:|---|---|---|
| D01 | 2026-06-30 | Hardware and environment profile | GPU/CPU/RAM/storage/CUDA/PyTorch profile table |
| D02 | 2026-07-01 | What happens in a training step | Forward-loss-backward-step diagram |
| D03 | 2026-07-02 | GPU memory math | Parameters/gradients/optimizer/activations memory calculator |
| D04 | 2026-07-03 | Batch size, sequence length, gradient accumulation | Throughput vs memory decision table |
| D05 | 2026-07-04 | Precision: FP32/TF32/FP16/BF16 | Precision risk and speed card |
| D06 | 2026-07-05 | DataLoader and IO bottlenecks | Data pipeline checklist |
| D07 | 2026-07-06 | W1 review | Single-GPU baseline run contract |
| D08 | 2026-07-07 | CUDA mental model | CUDA execution and memory hierarchy card |
| D09 | 2026-07-08 | Autograd and optimizer states | Autograd/optimizer state diagram |
| D10 | 2026-07-09 | Checkpointing and resume | Checkpoint/resume failure-mode table |
| D11 | 2026-07-10 | Profiling basics | Profiling checklist: CPU/GPU/utilization/memory/IO |
| D12 | 2026-07-11 | Small benchmark design | Benchmark protocol v0.1 |
| D13 | 2026-07-12 | Failure diagnosis | Training failure taxonomy |
| D14 | 2026-07-13 | W2 review | Training bottleneck report v0.1 |

## Weeks 3-13

| Week | Dates | Theme | Output |
|---:|---|---|---|
| W03 | 2026-07-14 to 2026-07-20 | DDP and basic distributed launch | DDP run contract + failure checklist |
| W04 | 2026-07-21 to 2026-07-27 | FSDP and ZeRO memory sharding | FSDP vs ZeRO decision matrix |
| W05 | 2026-07-28 to 2026-08-03 | NCCL and communication bottlenecks | Communication bottleneck diagnosis card |
| W06 | 2026-08-04 to 2026-08-10 | Tensor/pipeline/sequence parallel | Parallelism architecture diagram |
| W07 | 2026-08-11 to 2026-08-17 | LLM data and tokenizer pipeline | Mini corpus/data pipeline spec |
| W08 | 2026-08-18 to 2026-08-24 | Model config, scaling, eval | Mini LLM training design spec |
| W09 | 2026-08-25 to 2026-08-31 | LoRA/PEFT/full fine-tuning | Fine-tuning decision matrix |
| W10 | 2026-09-01 to 2026-09-07 | Eval and experiment tracking | Experiment protocol + eval rubric |
| W11 | 2026-09-08 to 2026-09-14 | Remote GPU and multi-node operations | Remote GPU runbook |
| W12 | 2026-09-15 to 2026-09-21 | Reliability, checkpoints, cost caps | Training operations runbook |
| W13 | 2026-09-22 to 2026-09-27 | Capstone | GPU ML Systems playbook v1 |

## D01 Hard Gate

D01 cannot be marked complete until actual hardware is recorded:

| Required field | Status |
|---|---|
| GPU model and VRAM | pending |
| CPU model and cores | pending |
| RAM | pending |
| Storage type and free space | pending |
| OS and driver | pending |
| CUDA toolkit / runtime | pending |
| PyTorch version and CUDA availability | pending |
| Remote GPU option and budget cap | pending |

## Top1 Compression Standard

The project compresses learning by focusing on bottleneck judgment:

1. What limits the run: memory, compute, IO, communication, or data quality?
2. Which training strategy changes the bottleneck?
3. What is the cheapest experiment that proves or falsifies the assumption?
4. What failure mode would make the result unusable?
5. What should an agent be allowed to execute automatically, and what must be budget-gated?
