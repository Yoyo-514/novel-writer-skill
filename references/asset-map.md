# Optional Image Mapping

Images are optional. Do not run this workflow unless the user asks for illustrated output, supplies images, or explicitly wants PDF images extracted and placed.

## Contents

- Modes
- Inventory
- Scan
- Filter
- Placement
- Approval Gate
- Reset
- Reporting

## Modes

| Mode | Use |
|---|---|
| `report` | Show current image status without changing prose |
| `scan-only` | Create/update image inventory and classify images |
| `filter-only` | Select useful images from scanned inventory |
| `place` | Insert approved selected images into scene/chapter markdown |
| `all` | Scan, filter, confirm, then place |
| `reset` | Clear generated mapping and inserted export references after confirmation |

## Inventory

Use `novel/assets/IMAGE_MAP.json`:

```json
[
  {
    "file": "novel/assets/source.png",
    "source_page": 3,
    "size_kb": 45.2,
    "type": "character",
    "volume": "vol01",
    "chapter": "ch01",
    "scene": "scene02",
    "position": "after_scene_break",
    "position_detail": "after the first mention of the academy gate",
    "caption": "",
    "status": "scanned",
    "scan_notes": "",
    "detected_text": [],
    "detected_keywords": []
  }
]
```

Status values:

- `unscanned`
- `scanned`
- `rejected`
- `selected`
- `placed`

Type values:

- `character`
- `map`
- `scene`
- `diagram`
- `cover`
- `icon`
- `duplicate`
- `text_only`
- `unknown`

## Workflow

1. Build inventory from files in `novel/assets/` or from `scripts/extract_pdf_images.py`.
2. Pre-filter tiny images: likely icons below 5 KB; visually confirm borderline cases.
3. Classify images by type and content.
4. Cross-reference image source page, detected text, outline context, scene cards, and drafted prose.
5. Reject duplicates, irrelevant images, poor-quality fragments, pure UI icons, and images not covered by the prose.
6. Apply density control. Default is 0-3 images per chapter unless the user wants an illustrated edition.
7. Present a selected/rejected summary and wait for user approval before inserting references.
8. Copy approved images to `novel/assets/export/` with clean names such as `vol01_ch03_img01.png`.
9. Insert markdown image references at scene-level placement points.
10. Update `IMAGE_MAP.json`.

## Placement Rules

- Never delete original images.
- Avoid duplicate insertions.
- Prefer scene-level placement when scene files exist.
- Use `novel/assets/export/...` paths expected by export.
- Keep captions in the active writing language.
- Place maps near first location introduction.
- Place character art at first meaningful appearance, not random chapter start.
- Place diagrams before or after the passage that uses the concept.
- TXT export strips image references unless the user explicitly asks to keep them.

## Approval Summary

Before placement, show:

- selected count and rejected count
- selected images by volume/chapter/scene
- rejection breakdown
- files that will be modified
- exact confirmation request

Do not place images without approval.

## Reset

Reset mode requires confirmation because it removes generated placement work:

- remove placed/export fields from `IMAGE_MAP.json`
- delete generated files in `novel/assets/export/`
- remove markdown references pointing to `novel/assets/export/`
- never delete original source images
