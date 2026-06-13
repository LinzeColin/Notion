# Top 1% Strategy

## Definition

Top 1% practical capability in this project means the ability to turn AI from a chat interface into a reliable work system:

- Clear task framing.
- High-signal context selection.
- Explicit output contracts.
- Tool and schema design.
- Traceable validation.
- Eval-driven iteration.
- Low-context, high-ROI handoff.

It does not mean becoming a full-time researcher in three days.

## Ability Tree

| Capability | What good looks like | Failure mode |
|---|---|---|
| Task framing | Goal, scope, input, output, constraints, verification are explicit | Vague prompt produces vague output |
| Context engineering | Only relevant state enters the model context | Context overload and hidden conflicts |
| Output contracts | Tables, JSON, Markdown, code, or artifacts match downstream use | Nice text but unusable structure |
| Loop design | Workflow has observe/act/validate/retry boundaries | Endless prompting without state or checks |
| Tool engineering | Tool names, schemas, errors, and permissions are model-legible | Tool misuse or unsafe action |
| Evals | Improvements are measured against real cases | Prompt changes judged by feeling |
| Handoff | Future agent can continue without chat history | Progress disappears after context loss |

## Defer List

Do not spend Phase B time on:

- Large agent frameworks unless needed for a concrete loop.
- Fine-tuning.
- Multi-agent complexity before single-loop reliability.
- Tool setup that does not teach the underlying concept.
- Generic prompt hack lists.

## Core Rule

Every concept must produce one artifact that can be reused in real Codex or AI workflow work.

