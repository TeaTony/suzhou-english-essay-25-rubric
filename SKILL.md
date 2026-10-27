---
name: suzhou-english-essay-25-rubric
description: 苏州中考英语作文 25 分制评分标准的单一来源。用于作文评分、阅卷尺度校准、评分提示词生成，以及点墨等本地批改平台读取默认 rubric；不负责云痕网页操作或题目要点库维护。
metadata:
  version: 1.0.0
  author: 王智迪
  rubric_version: "2026-10-27"
---

# 苏州英语作文 25 分制评分标准

本 skill 是评分标准的 canonical source。评分、提示词和系统集成都以本目录文件为准，不在其他项目复制后单独修改。

## Core Invariants

- 总分固定为 **25 分**：内容 10＋语言 10＋结构 3＋书写 2。
- 四维只取整数，`score` 必须等于四维之和，并落在对应五档区间。
- 内容先看要点和论证链，再看细节；语言好不能抵消漏要点、偏题或无论证。
- “言之有理”必须形成：**标题主张 → 原因 → 与主张一致的具体事例 → 自身联系**。
- 只有关键词、个人偏好、情绪结果或重复标题，判内容空洞；事例证明了另一个对象，判论证错位。
- 题目允许自由选材时，不按关键词或题材类别自动判偏题。题材能否成立，取决于正文是否把因果关系说清。
- 书写默认 1 分；全篇零涂改且工整才给 2 分，出现涂改记 1 分。

## Workflow

1. 批改具体题目时，先读取 `zhongkao-essay-task-points` 的对应任务记录。
2. 完整读取 [references/rubric-25.md](references/rubric-25.md)，按四维和五档先定档、后给分。
3. 输出时必须给出四维整数、档位、内容和语言的主要依据，并自检四维和等于总分。
4. 修改评分标准时，同时更新 `references/rubric-25.md`、`references/prompt-25.md`、`rubric.json` 和版本日期。
5. 运行 `python3 scripts/check_rubric.py .` 验证总分、档位连续性、提示词版本和论证链规则。

## Canonical Prompt

应用或模型需要 system prompt 时，直接读取：

`references/prompt-25.md`

不要从应用源码、缓存或历史对话中复制评分规则。应用应通过文件读取或固定 release 获取该文件。

## Reference Routing

| 文件 | 用途 |
|---|---|
| [references/rubric-25.md](references/rubric-25.md) | 完整四维、五档、扣分和边界样例 |
| [references/prompt-25.md](references/prompt-25.md) | 可直接注入应用的完整 system prompt |
| [references/calibration-cases.md](references/calibration-cases.md) | 容易分歧的论证质量锚点 |
| `rubric.json` | 给程序读取的结构化维度、档位和版本 |

## Boundaries

- 本 skill 不执行云痕网页点击或提交分数。
- 本 skill 不维护具体试卷的题目原文和必写要点。
- 评分台账、学生信息和成绩不得写入本仓库。
