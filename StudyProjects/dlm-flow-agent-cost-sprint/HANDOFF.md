# Handoff - DLM Flow Agent Cost Sprint

## Restore Summary

This is a 7-day sprint about AR vs Diffusion LM, Flow Matching, latent representation, VAE, latent prior, KV cache, ELF, Cola DLM, code infill, local high-speed interaction, inference cost model, and AI agent cost governance.

## Current State

| Field | Value |
|---|---|
| Slug | `dlm-flow-agent-cost-sprint` |
| Status | setup_created |
| Window | 2026-06-14 to 2026-06-20 |
| Current day | D01 / 第1/7天 |
| Next lesson | zero-base gate + AR vs Diffusion LM + KV cache |
| Source pack | `/Users/linzezhang/Downloads/dlm_learning_pack_zh.zip` |
| Supplemental patch | `/Users/linzezhang/Downloads/dlm_zero_base_patch_zh.zip` |
| Notion page | `https://app.notion.com/p/37fb1a986ba681f8b100c0e2aa67a3f2` |

## Next Teaching Action

Start D01 with zero-base gate first:

1. token 是什么，为什么影响成本？
2. 语言模型为什么可以理解为预测/生成 token 的函数？
3. AR 为什么像从左到右打字？
4. KV cache 缓存了什么，为什么它加速但增加显存成本？

Then continue with active recall:

1. token、embedding、hidden state、latent 有什么区别？
2. 为什么 AR 推理是逐 token 串行？
3. KV cache 缓存了什么，为什么它加速但增加显存成本？

Then teach AR vs Diffusion LM and produce `AR 成本模型图`.

## Zero-Base Patch Rule

The advanced route must not skip the plain Chinese concept gate. If the learner cannot explain the gate, teach the zero-base concept first and delay paper-level details.
