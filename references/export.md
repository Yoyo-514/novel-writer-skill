# TXT-First Export

Use this reference when assembling and exporting a novel.

## Defaults

- Export TXT first.
- Also create full markdown as an intermediate.
- Generate DOCX, EPUB, or PDF only when requested.
- Images are optional. TXT strips markdown image references by default.
- Generated markdown and TXT outputs are overwritten by export assembly only after timestamped backups are created when content differs.

## Supported Formats

| Format | Tool | Notes |
|---|---|---|
| TXT | `assemble_novel.py` | Default, strips markdown syntax and images |
| Markdown | `assemble_novel.py` | Intermediate full novel file |
| DOCX | pandoc | Optional, can embed markdown images |
| EPUB | pandoc | Optional, can use cover image if available |
| PDF | pandoc + xelatex or compatible engine | Optional; CJK setup required |

## Assembly Command

Run from the project root:

```bash
python path/to/skill/scripts/assemble_novel.py --project novel --lang zh --txt
```

The script assembles upward:

- `novel/draft/zh/volNN/chNN_zh.md` when volume directories exist
- `novel/draft/zh/volNN_zh.md` when volume directories exist
- `novel/draft/FULL_NOVEL_zh.md`
- `novel/output/novel_zh.txt`

It supports both:

- volume path: `draft/zh/vol01/ch01/scene01.md`
- flat path: `draft/zh/ch01/scene01.md`

## Format Parsing

- empty request: TXT
- `txt`, `text`, `纯文本`: TXT
- `docx`, `word`: DOCX
- `epub`, `电子书`: EPUB
- `pdf`: PDF
- `all`: TXT + DOCX + EPUB + PDF, with graceful degradation
- chapter/volume preview: assemble requested scope when the user names one

## Optional Pandoc Formats

When requested and `pandoc` is available:

```bash
pandoc novel/draft/FULL_NOVEL_zh.md -o novel/output/novel_zh.docx
pandoc novel/draft/FULL_NOVEL_zh.md -o novel/output/novel_zh.epub --metadata lang=zh
```

For PDF, require a working CJK-capable engine such as xelatex. If unavailable, export TXT and other requested formats first, then report the missing dependency.

## Image Handling

- Do not auto-trigger image mapping just because `novel/assets/` exists.
- If the user requests illustrated DOCX/EPUB/PDF and images are unplaced, read `asset-map.md`.
- Verify referenced image paths before optional pandoc export.
- Missing images should warn and degrade gracefully, not abort TXT export.
- If `novel/assets/cover.jpg` or `.png` exists and EPUB is requested, use it as cover when possible.

## Bilingual Handling

For bilingual projects:

- assemble primary and secondary language separately
- use `LANGUAGE_SETTING.json` output filenames
- if post-writing translation is configured and secondary chapters are missing, ask before starting a translation pass unless the user already requested export-with-translation
- always consult `TRANSLATION_GLOSSARY.md`

## Verification

Check:

- output files exist
- TXT is not suspiciously small
- scene, chapter, and volume order are correct
- planning notes did not leak into final prose
- markdown image references are absent from TXT unless requested
- optional DOCX/EPUB/PDF files are non-empty

## Output Report

Report:

- title and language
- assembled volumes/chapters/scenes count when known
- output files and sizes
- skipped formats and why
- next suggested action if export was partial
