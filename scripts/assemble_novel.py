#!/usr/bin/env python3
"""Assemble scene markdown upward into chapters, volumes, full markdown, and TXT."""

from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime
from pathlib import Path


CHAPTER_RE = re.compile(r"ch(\d+)", re.IGNORECASE)
SCENE_RE = re.compile(r"scene(\d+)", re.IGNORECASE)
VOLUME_RE = re.compile(r"vol(\d+)", re.IGNORECASE)
IMAGE_RE = re.compile(r"!\[[^\]]*]\([^)]+\)")


def natural_key(path: Path) -> tuple[int, int, int, str]:
    volume_match = VOLUME_RE.search(path.as_posix())
    chapter_match = CHAPTER_RE.search(path.as_posix())
    scene_match = SCENE_RE.search(path.stem)
    volume = int(volume_match.group(1)) if volume_match else 10**9
    chapter = int(chapter_match.group(1)) if chapter_match else 10**9
    scene = int(scene_match.group(1)) if scene_match else 0
    return volume, chapter, scene, path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def write_text_with_backup(path: Path, text: str) -> None:
    if path.exists() and path.read_text(encoding="utf-8") != text:
        stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = path.with_suffix(path.suffix + f".bak-{stamp}")
        shutil.copy2(path, backup_path)
    path.write_text(text, encoding="utf-8")


def chapter_id(path: Path) -> str:
    match = CHAPTER_RE.search(path.name)
    return f"ch{int(match.group(1)):02d}" if match else path.stem.lower()


def volume_id(path: Path) -> str:
    match = VOLUME_RE.search(path.name)
    return f"vol{int(match.group(1)):02d}" if match else path.stem.lower()


def assemble_chapter_dir(chapter_dir: Path) -> str:
    scene_files = sorted(chapter_dir.glob("scene*.md"), key=natural_key)
    parts = []
    for scene_file in scene_files:
        text = read_text(scene_file)
        if text:
            parts.append(text)
    return "\n\n---\n\n".join(parts).strip()


def collect_chapters_from_dir(parent_dir: Path) -> list[tuple[str, str]]:
    assembled: list[tuple[str, str]] = []
    seen_chapters: set[str] = set()

    chapter_dirs = sorted(
        [p for p in parent_dir.iterdir() if p.is_dir() and CHAPTER_RE.fullmatch(p.name)],
        key=natural_key,
    )
    for chapter_dir in chapter_dirs:
        text = assemble_chapter_dir(chapter_dir)
        if text:
            chap_id = chapter_id(chapter_dir)
            assembled.append((chap_id, text))
            seen_chapters.add(chap_id)

    chapter_files = sorted(parent_dir.glob("ch*.md"), key=natural_key)
    for chapter_file in chapter_files:
        chap_id = chapter_id(chapter_file)
        if chap_id in seen_chapters:
            continue
        text = read_text(chapter_file)
        if text:
            assembled.append((chap_id, text))

    return sorted(assembled, key=lambda item: natural_key(Path(item[0])))


def write_chapter_outputs(parent_dir: Path, lang: str, chapters: list[tuple[str, str]]) -> None:
    for chap_id, text in chapters:
        out_path = parent_dir / f"{chap_id}_{lang}.md"
        write_text_with_backup(out_path, text.strip() + "\n")


def collect_full_markdown(draft_dir: Path, lang: str) -> list[tuple[str, str]]:
    lang_dir = draft_dir / lang
    if not lang_dir.exists():
        raise SystemExit(f"Missing draft language directory: {lang_dir}")

    full_units: list[tuple[str, str]] = []
    volume_dirs = sorted(
        [p for p in lang_dir.iterdir() if p.is_dir() and VOLUME_RE.fullmatch(p.name)],
        key=natural_key,
    )

    for vol_dir in volume_dirs:
        chapters = collect_chapters_from_dir(vol_dir)
        if not chapters:
            continue
        write_chapter_outputs(vol_dir, lang, chapters)
        volume_text = "\n\n".join(text for _, text in chapters).strip()
        if volume_text:
            vol_id = volume_id(vol_dir)
            vol_path = lang_dir / f"{vol_id}_{lang}.md"
            write_text_with_backup(vol_path, volume_text + "\n")
            full_units.append((vol_id, volume_text))

    flat_chapters = collect_chapters_from_dir(lang_dir)
    if flat_chapters:
        write_chapter_outputs(lang_dir, lang, flat_chapters)
        full_units.extend(flat_chapters)

    volume_files = sorted(lang_dir.glob("vol*.md"), key=natural_key)
    existing_ids = {unit_id for unit_id, _ in full_units}
    for volume_file in volume_files:
        vol_id = volume_id(volume_file)
        if vol_id in existing_ids:
            continue
        text = read_text(volume_file)
        if text:
            full_units.append((vol_id, text))

    return sorted(full_units, key=lambda item: natural_key(Path(item[0])))


def markdown_to_txt(markdown: str, keep_images: bool) -> str:
    text = markdown if keep_images else IMAGE_RE.sub("", markdown)
    text = re.sub(r"^#{1,6}\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default="novel", help="Novel project directory")
    parser.add_argument("--lang", default="zh", help="Language code under draft/")
    parser.add_argument("--txt", action="store_true", help="Write TXT output")
    parser.add_argument("--keep-images", action="store_true", help="Keep image markdown in TXT")
    args = parser.parse_args()

    project = Path(args.project)
    draft_dir = project / "draft"
    output_dir = project / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    draft_dir.mkdir(parents=True, exist_ok=True)

    units = collect_full_markdown(draft_dir, args.lang)
    if not units:
        raise SystemExit(f"No chapters or scenes found under {draft_dir / args.lang}")

    full_markdown = "\n\n".join(text for _, text in units).strip() + "\n"
    full_path = draft_dir / f"FULL_NOVEL_{args.lang}.md"
    write_text_with_backup(full_path, full_markdown)

    print(f"Wrote {full_path} ({len(units)} assembled units)")

    if args.txt:
        txt_path = output_dir / f"novel_{args.lang}.txt"
        write_text_with_backup(txt_path, markdown_to_txt(full_markdown, args.keep_images))
        print(f"Wrote {txt_path}")


if __name__ == "__main__":
    main()
