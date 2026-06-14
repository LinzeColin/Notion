# GPU ML Systems & Model Training

Project slug: `gpu-ml-systems-model-training`  
Timezone: Australia/Sydney  
Planned start date: 2026-06-30  
Planned end date: 2026-09-27  
Duration: 90 days  
Status: scheduled  
Notion Timeline: `37fb1a98-6ba6-81f1-929a-fd4290f4be04`

## Goal

Build practical Top1% judgment and operating capability for GPU ML systems and model training: hardware profiling, CUDA/PyTorch mental models, single-GPU training, distributed training, FSDP/ZeRO/NCCL, model/data scaling, fine-tuning versus pretraining, experiment reliability, cost control, and failure diagnosis.

The target is not to claim the user can train frontier-scale models cheaply. The target is to make the user able to judge, design, run, debug, and cost a training system without being fooled by model hype, vendor demos, or vague agent claims.

## Why This Project Exists

The user explicitly authorized opening the previously conditional `GPU ML Systems & Model Training` project. It starts on 2026-06-30, the expected arrival date of the new computer with larger GPU memory, CPU, and storage.

Hardware assumptions must stay provisional until D01 verifies the actual machine.

## Scope

| Area | Included |
|---|---|
| Hardware | GPU/VRAM/CPU/RAM/storage profile, PCIe/IO bottlenecks, local vs remote GPU tradeoffs |
| CUDA fundamentals | CUDA execution model, memory hierarchy, kernels at conceptual/operator level |
| PyTorch training | training loop, autograd, optimizer, dataloader, precision, checkpointing |
| Performance | profiling, throughput, memory, batch size, gradient accumulation, bottleneck diagnosis |
| Distributed training | DDP, FSDP, ZeRO, tensor parallel, pipeline parallel, sequence parallel, NCCL |
| LLM training systems | tokenizer, data pipeline, model config, loss, scaling, evaluation, checkpoint strategy |
| Fine-tuning | LoRA, PEFT, full fine-tuning, eval, overfitting, dataset quality |
| Operations | reproducibility, logging, run metadata, fault recovery, cost and budget governance |

## Explicit Non-Goals

- No fake promise of training frontier models from scratch without budget and cluster.
- No blind multi-GPU experiment before hardware, driver, and cost profile are known.
- No “tool installed = learned” accounting.
- No live high-cost cloud run without a written run contract, budget cap, and stop condition.

## Success Criteria

| Capability | Pass Standard |
|---|---|
| Hardware judgment | Can estimate whether a model/training run fits VRAM and what tradeoffs exist |
| Training loop | Can explain forward, loss, backward, optimizer step, precision, and checkpointing |
| Bottleneck diagnosis | Can identify whether a run is compute-bound, memory-bound, IO-bound, or communication-bound |
| Distributed strategy | Can choose DDP/FSDP/ZeRO/TP/PP based on model size, hardware, and failure risk |
| Cost control | Can estimate GPU hours, storage, checkpoint cost, and stop conditions |
| Experiment quality | Can define eval, logging, reproducibility, and rollback before running |
| System design | Can produce a training runbook and architecture memo that another agent can execute safely |

## Relationship To Other Study Projects

- `local-ai-infrastructure` handles local inference, RAG, multimodal runtime, and local data infrastructure.
- `ai-workflow-operating-system` handles agent tool contracts and workflow orchestration.
- `industrial-ai-saas-builder` handles business/ROI/product judgment.
- This project owns distributed training, training systems, GPU ML performance, and model-training operations.
