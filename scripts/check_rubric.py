#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    data = json.loads((root / "rubric.json").read_text(encoding="utf-8"))
    prompt = (root / "references/prompt-25.md").read_text(encoding="utf-8")
    rubric = (root / "references/rubric-25.md").read_text(encoding="utf-8")
    skill = (root / "SKILL.md").read_text(encoding="utf-8")

    errors: list[str] = []
    total = sum(item["max"] for item in data["dimensions"].values())
    if total != data["total"] or total != 25:
        errors.append(f"dimension total mismatch: {total}")

    expected_ranges = [(21, 25), (16, 20), (11, 15), (6, 10), (0, 5)]
    actual_ranges = [(tier["min"], tier["max"]) for tier in data["tiers"]]
    if actual_ranges != expected_ranges:
        errors.append(f"tier ranges mismatch: {actual_ranges}")

    version = data["version"]
    for name, text in {
        "prompt-25.md": prompt,
        "rubric-25.md": rubric,
        "SKILL.md": skill,
    }.items():
        if version not in text:
            errors.append(f"{name} missing rubric version {version}")

    for file_name, text in {"prompt-25.md": prompt, "rubric-25.md": rubric}.items():
        for marker in ("言之有理", "标题主张", "具体事例", "自身联系", "内容 4–5"):
            if marker not in text:
                errors.append(f"{file_name} missing marker: {marker}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Rubric valid: version {version}, total {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
