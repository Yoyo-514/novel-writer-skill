# Language Setting

Use this reference for `LANGUAGE_SETTING.json`, bilingual translation behavior, and translation glossary management. For prose style, chapter/scene length, POV, and custom style guides, read `novel-style.md`.

## Contents

- Defaults
- Supported Languages
- Language Setting Shape
- Translation Modes
- Translation Style
- Directory Layout
- Translation Glossary
- Glossary Rules
- Chinese-First Prose Rules
- Output Rules

## Defaults

Default to Chinese monolingual writing:

```json
{
  "mode": "monolingual",
  "primary_language": "zh",
  "primary_language_name": "Simplified Chinese",
  "translation_style": null,
  "translation_timing": null,
  "output_filenames": {
    "primary": "novel_zh"
  }
}
```

Only create bilingual settings when the user explicitly requests another language or translation.

## Supported Languages

Common codes:

| Code | Language |
|---|---|
| `zh` | Simplified Chinese |
| `zh-tw` | Traditional Chinese |
| `en` | English |
| `ja` | Japanese |
| `ko` | Korean |
| `fr` | French |
| `de` | German |
| `es` | Spanish |

Any valid pandoc language metadata code can be used when exporting.

## Parsing

Detect:

- primary language: default `zh`
- bilingual mode: signals such as bilingual, dual-language, translate to, `zh->en`, `ja->zh`, or explicit user request
- secondary language: default `en` when primary is `zh`; default `zh` when primary is non-Chinese and user does not specify
- translation style:
  - `literary`: natural literary translation, emotional equivalence first
  - `literal`: close to wording and structure when readable
  - `faithful`: precise meaning and cultural context with natural target prose
- translation timing:
  - `per-chapter`: translate after each chapter or scene group
  - `post-writing`: translate after primary-language drafting is complete

Confirm bilingual settings before writing files. For monolingual Chinese, proceed with defaults unless the user asks to review them.

## Bilingual Setting Shape

```json
{
  "mode": "bilingual",
  "primary_language": "ja",
  "primary_language_name": "Japanese",
  "secondary_language": "zh",
  "secondary_language_name": "Simplified Chinese",
  "translation_style": "literary",
  "translation_timing": "per-chapter",
  "output_filenames": {
    "primary": "novel_ja",
    "secondary": "novel_zh"
  },
  "configured_at": "ISO-8601 timestamp"
}
```

## Translation Glossary

For bilingual projects, create `novel/settings/TRANSLATION_GLOSSARY.md` before translation begins.

Recommended sections:

```markdown
# Translation Glossary

## Character Names
| Primary | Secondary | Romanization | Notes |
|---|---|---|---|

## Places and Factions
| Primary | Secondary | Notes |
|---|---|---|

## Terms
| Primary | Secondary | Meaning |
|---|---|---|

## Registers and Verbal Tics
| Primary | Target Rendering | Character | Notes |
|---|---|---|---|

## Pending
| Source | Auto Suggestion | Type | First Seen | Status |
|---|---|---|---|---|
```

Rules:

- Pre-fill names from `CHARACTER_BIBLE.md`, or from `CHARACTER_INDEX.md` and relevant per-character files in split libraries, when possible.
- Confirmed glossary entries are binding. Do not vary them for style.
- New unconfirmed terms go to `Pending`; do not silently invent stable terminology.
- Translation must preserve character speech fingerprints across languages.
- In post-writing mode, export may trigger missing secondary-language translation, but it must still use this glossary.

## Chinese-First Prose Rules

- Prefer natural Simplified Chinese prose over translation-like phrasing.
- Keep names, terms, and titles consistent.
- Avoid meta commentary in story prose.
- Keep exposition inside conflict, dialogue, action, or perception.
- Match register to genre and character background.
