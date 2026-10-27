# Suzhou English Essay 25 Rubric

苏州中考英语作文 25 分制评分标准的单一来源，可同时供 Codex skill、点墨和其他本地批改工具读取。

## Contents

- `SKILL.md`：Codex 使用入口和评分不变量
- `references/rubric-25.md`：完整四维、五档和扣分细则
- `references/prompt-25.md`：可直接注入模型的 canonical system prompt
- `references/calibration-cases.md`：论证质量边界样例
- `rubric.json`：结构化维度、档位和版本
- `scripts/check_rubric.py`：一致性校验脚本

## Install As Skill

```bash
ln -s "/path/to/suzhou-english-essay-25-rubric" \
  "${CODEX_HOME:-$HOME/.codex}/skills/suzhou-english-essay-25-rubric"
```

## PointMo Integration

点墨默认从环境变量 `DIANMO_RUBRIC_PROMPT` 读取本仓库的 `references/prompt-25.md`。未设置时，按以下顺序查找：

1. `~/Documents/点墨数据/rubric-skill/references/prompt-25.md`
2. `~/.codex/skills/suzhou-english-essay-25-rubric/references/prompt-25.md`

应用只负责读取，不再在源码中保存评分标准副本。

## Update Protocol

1. 修改 `rubric.json` 和两份 reference。
2. 同步版本日期。
3. 运行 `python3 scripts/check_rubric.py .`。
4. 提交并打语义化版本 tag。

## Privacy

本仓库不存放学生姓名、学号、答卷图片、成绩单或评分台账。
