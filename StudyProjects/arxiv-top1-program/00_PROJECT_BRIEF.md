# arXiv Top1 Program

Project slug: `arxiv-top1-program`  
Start date: `2026-06-13`  
Timezone: `Australia/Sydney`  
Status: `active`  
Mode: rolling multi-group Study Project

## 已锁定范围

| 字段 | 决策 |
|---|---|
| 目标 | 深度学习 arXiv archives，建立 Top 1% 判断力、论文阅读能力、研究品味和现实迁移能力。 |
| Group 顺序 | Q-FIN, PHYS, MATH, STAT, CS, ECON, EE/EESS, Q-BIO。 |
| 同时 active groups | 2 个。 |
| Archive 周期 | 每个 archive/category 固定 30 天。 |
| Group 总时长 | `archive_count * 30 天`；group 不是一个月单位。 |
| Day 1 | 2026-06-13。 |
| 真相源 | GitHub project folder。 |
| Notion 角色 | `Codex Study Timeline` 只存简洁 timeline 和笔记；原始 Notion workspace 未授权不修改。 |
| 学习笔记语言 | 默认中文；保留必要专业术语、archive code、API 名、论文名和工具名。 |

## 当前 active tracks

| Track | Group | 当前 archive | 原因 |
|---|---|---|---|
| 1 | Q-FIN | Trading and Market Microstructure `q-fin.TR` | 对 alpha、执行质量、市场结构、risk control、交易 Agent 判断的近期 ROI 最高。 |
| 2 | PHYS | Quantum Physics `quant-ph` | 对不确定性、测量、信息、前沿技术阅读和跨领域系统思维很关键。 |

## 当前 group 真实计划窗口

| Group | Archive 数量 | 计划开始 | 计划结束 | 状态 |
|---|---:|---|---|---|
| Q-FIN | 9 | 2026-06-13 | 2027-03-09 | active |
| PHYS | 51 | 2026-06-13 | 2030-08-20 | active |
| MATH | 32 | 2027-03-10 | 2029-10-24 | queued |
| STAT | 6 | 2029-10-25 | 2030-04-22 | queued |
| CS | 40 | 2030-04-23 | 2033-08-04 | queued |
| ECON | 3 | 2030-08-21 | 2030-11-18 | queued |
| EE/EESS | 4 | 2030-11-19 | 2031-03-18 | queued |
| Q-BIO | 10 | 2031-03-19 | 2032-01-12 | queued |

完整计划见 `01_STUDY_PLAN.md` 和 `10_PROGRAM_STATE/archive_catalog.csv`。

## 推进规则

| 规则 | 触发条件 | 动作 |
|---|---|---|
| Archive 完成 | 30 天 archive cycle 完成，且 mastery evidence 通过复盘 | 同一 group 推进到下一个 archive。 |
| Group 完成 | group 内所有 archives 完成 | 下一个 queued group 进入空出来的 active slot。 |
| 每日同步 | 每日学习/同步完成 | 更新 daily log、metrics、state、active tracks、progression log。 |

## 不可违反流程

- 修改 Notion 前先读取现有 Notion 格式。
- 未明确授权，不创建新 Notion 页面或 database。
- 学习先于搭建；没有吃透概念，不把项目搭建当进度。
- 每日学习必须说明当前进度，例如：`D001 / Q-FIN q-fin.TR 第1/30天；PHYS quant-ph 第1/30天`。
- 每个重要概念必须讲到能用：含义、机制、失败模式、真实例子、决策规则、ROI 最大化行动。
