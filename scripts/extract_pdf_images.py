#!/usr/bin/env python3
"""Extract embedded images from a PDF into novel/assets and write IMAGE_MAP.json."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", help="Source PDF path")
    parser.add_argument("--project", default="novel", help="Novel project directory")
    args = parser.parse_args()

    try:
        import fitz  # type: ignore
    except ImportError as exc:
        raise SystemExit("PyMuPDF is required. Install with: pip install pymupdf") from exc

    pdf_path = Path(args.pdf)
    assets_dir = Path(args.project) / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    image_map = []
    doc = fitz.open(pdf_path)
    for page_index in range(len(doc)):
        page = doc[page_index]
        for image_index, image in enumerate(page.get_images(full=True), start=1):
            xref = image[0]
            extracted = doc.extract_image(xref)
            ext = extracted.get("ext", "png")
            filename = f"outline_p{page_index + 1:02d}_img{image_index:02d}.{ext}"
            output_path = assets_dir / filename
            output_path.write_bytes(extracted["image"])
            image_map.append(
                {
                    "file": output_path.as_posix(),
                    "source_page": page_index + 1,
                    "type": "unknown",
                    "chapter": None,
                    "scene": None,
                    "caption": "",
                    "status": "unscanned",
                    "notes": "",
                }
            )

    map_path = assets_dir / "IMAGE_MAP.json"
    map_path.write_text(json.dumps(image_map, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Extracted {len(image_map)} images to {assets_dir}")
    print(f"Wrote {map_path}")


if __name__ == "__main__":
    main()
