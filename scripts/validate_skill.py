#!/usr/bin/env python3
"""Lightweight repository validation for the novel-writer skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = [
    "SKILL.md",
    "README.md",
    "references/workflow.md",
    "references/conception-blueprint.md",
    "references/outline-planning.md",
    "references/chapter-outline.md",
    "references/scene-chapter-writing.md",
    "references/chapter-prose-execution.md",
    "references/chapter-revision.md",
    "references/character-design.md",
    "references/character-library.md",
    "references/world-library.md",
    "references/ability-system.md",
    "references/terminology.md",
    "references/novel-style.md",
    "references/style-language.md",
    "references/topic-guidance.md",
    "references/asset-map.md",
    "references/export.md",
    "scripts/assemble_novel.py",
    "scripts/extract_pdf_images.py",
]
BANNED_PATTERNS = [
    r"allowed-tools",
    r"argument-hint",
    r"(?m)^\s*/novel-[a-z]",
    r"Bash\(",
    r"Read\(",
    r"Write\(",
    r"Edit\(",
    r"MultiEdit\(",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_skill_md() -> None:
    skill_path = ROOT / "SKILL.md"
    text = read(skill_path)
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")

    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md frontmatter is not closed")

    frontmatter = match.group(1)
    keys = []
    for line in frontmatter.splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            keys.append(line.split(":", 1)[0].strip())

    if keys != ["name", "description"]:
        fail("SKILL.md frontmatter should contain only name and description")
    if "name: novel-writer" not in frontmatter:
        fail("SKILL.md name must be novel-writer")


def validate_required_paths() -> None:
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            fail(f"Missing required path: {relative}")


def validate_reference_contents() -> None:
    for path in (ROOT / "references").glob("*.md"):
        text = read(path)
        if len(text.splitlines()) > 100 and "## Contents" not in text:
            fail(f"Reference over 100 lines needs ## Contents: {path.name}")


def validate_no_command_residue() -> None:
    combined = []
    for path in [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md")]:
        combined.append((path, read(path)))

    for path, text in combined:
        for pattern in BANNED_PATTERNS:
            if re.search(pattern, text):
                fail(f"Found command-specific residue in {path.relative_to(ROOT)}: {pattern}")


def main() -> None:
    validate_skill_md()
    validate_required_paths()
    validate_reference_contents()
    validate_no_command_residue()
    print("novel-writer skill repository looks publish-ready.")


if __name__ == "__main__":
    main()
