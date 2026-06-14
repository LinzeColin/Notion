# Local AI Infrastructure

Project slug: `local-ai-infrastructure`  
Timezone: Australia/Sydney  
Planned start date: 2026-07-19  
Planned end date: 2026-08-15  
Duration: 28 days  
Status: scheduled parallel from 2026-07-19

## Schedule Decision

This project was moved forward on 2026-06-14 so every non-arXiv Study Project can finish no later than 2026-08-15.

It runs in controlled parallel with `ai-workflow-operating-system` because the two projects reinforce each other: AI Workflow OS teaches orchestration, Codex, Notion, prompt/loop, and software workflow; Local AI Infrastructure teaches the local runtime, RAG, deployment, NPU/CNN, and simulator infrastructure underneath that workflow.

## 2026-06-14 Scope Integration Decision

User authorized integrating the new AI infrastructure topics into existing Study Projects rather than creating a new project.

Current budget mode: local/current hardware plus limited remote GPU experiments. New computer expected on 2026-06-30 with substantially larger GPU memory, CPU, and storage; hardware-sensitive lessons should preserve local-vs-remote comparison rather than assume one fixed machine.

Training-large-models choice: option C. Distributed training / from-scratch pretraining is not forced into this 28-day project. This project only covers training decision literacy, fine-tuning/LoRA boundaries, hardware cost awareness, and when to open a future dedicated `GPU ML Systems & Model Training` project.

## Goal

Build practical local and remote AI infrastructure judgment: local LLM deployment, remote GPU access, 32B/70B quantized model serving, local RAG and knowledge-base infrastructure, multimodal/vision inference, NPU/CNN concepts, and a local big-data strategy simulator.

## Included Scope

| Area | Role |
|---|---|
| Local LLM Deployment | Run and evaluate local models through Ollama, llama.cpp, vLLM-compatible servers, or equivalent serving stacks. |
| Remote GPU | Understand when renting GPU is higher ROI than local hardware; compare cost, latency, reproducibility, security, and setup friction. |
| 32B / 70B quantized models | Learn memory, quantization, context, throughput, quality, and serving tradeoffs for local/remote inference. |
| Local RAG | Build local document retrieval and grounded generation pipelines. |
| Large document knowledge base | Understand ingestion, chunking, embedding, vector DB, hybrid search, reranking, eval, and update governance for many documents. |
| Multimodal / vision models | Learn image generation, visual understanding, document/image QA, and industrial/commercial use-case boundaries. |
| NPU applications | Understand when NPU matters, what can run on it, and how OpenVINO-style deployment fits. |
| CNN | Learn the core visual-model concept needed to understand NPU/vision inference. |
| Local big-data strategy simulator | Build the mental model for local data pipelines, strategy simulation, backtesting, event loops, and reporting. |
| Training decision literacy | Learn when LoRA/fine-tuning is appropriate and when distributed training/pretraining requires a separate 60-90 day project. |

## Excluded / Future Conditional Scope

| Topic | Treatment |
|---|---|
| From-scratch pretraining | Future conditional project only. Do not fit into the 28-day Local AI Infrastructure plan. |
| Distributed training systems | Future `GPU ML Systems & Model Training` project if user explicitly chooses this as the main target. |
| Deep CUDA/NCCL/DeepSpeed internals | Mention as system boundary; do not treat as required current mastery. |
| Heavy production MLOps platform | Defer until a real product or research workload needs it. |

## Success Criteria

- Can choose between API model, cloud LLM, remote GPU, local LLM, RAG, classic software, and simulator approaches.
- Can explain deployment tradeoffs: privacy, latency, cost, model quality, hardware, storage, maintenance, and reproducibility.
- Can judge whether 32B/70B local or remote inference is worth the memory/cost/latency tradeoff.
- Can design a local or remote RAG/knowledge-base stack with evals rather than just embeddings.
- Can explain when multimodal/vision belongs in a workflow and when it is a distraction.
- Can design a local simulator that produces testable strategy metrics rather than vague claims.
- Can connect local infrastructure back to Industrial AI SaaS, AI workflow systems, and finance/arbitrage systems.
