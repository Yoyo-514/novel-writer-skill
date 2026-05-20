---
name: novel-writer
description: Create, revise, draft, and export long-form fiction from outlines or rough ideas. Use when Codex is asked to write a novel, expand or repair an outline, design characters, split medium/long cast libraries, build worldbuilding files, design ability or magic systems, manage in-world terminology, configure prose style, draft chapters or scenes, continue a story, revise scenes, manage Chinese-first monolingual novel projects, optionally place images, or export finished drafts with TXT as the default priority format.
---

# Novel Writer

## Defaults

- Write in Simplified Chinese unless the user explicitly asks for another language or bilingual output.
- Treat monolingual writing as the default. Configure bilingual writing only on request.
- Prefer TXT output first. Generate DOCX, EPUB, or PDF only when requested or clearly useful.
- Treat images as optional enhancement. Do not scan, classify, or place images unless the user asks, supplies assets, or export requirements depend on them.
- Organize production bottom-up: scene -> chapter -> volume -> full novel. Blueprints and outlines guide the work, but scenes are the smallest writing and revision unit.
- Treat the outline and chapter outline as strong references during drafting. Follow them by default, but allow mid-writing changes when the user explicitly asks to change the plan.
- Ask for confirmation before long autonomous drafting, large rewrites, image insertion, or overwriting finished output.
- Treat missing or empty source material as proposal-gated. If outline, chapter plan, scene plan, worldbuilding, ability rules, terminology, or style direction is absent or too vague, first present 2-3 concise options with assumptions and tradeoffs; wait for the user to choose, merge, or modify before creating the full artifact or drafting prose.

## Project Layout

Use this layout for persistent novel projects:

```text
novel/
  CREATIVE_BLUEPRINT.md
  OUTLINE.md
  CHAPTER_OUTLINE.md
  NOVEL_STATE.json
  MANIFEST.md
  characters/
    # Small projects:
    CHARACTER_BIBLE.md

    # Medium/long projects:
    CHARACTER_INDEX.md
    major/
    supporting/
    minor/
    relationships/
  world/
    # Small projects:
    WORLD_BIBLE.md
    TERMINOLOGY.md

    # Medium/long projects:
    WORLD_INDEX.md
    rules/
    locations/
    factions/
    items/
    weapons/
    abilities/
      # Small ability projects:
      ABILITY_SYSTEM.md

      # Medium/long ability systems:
      schools/
      abilities/
      users/
    terms/
      # Medium/long terminology library:
      TERM_INDEX.md
  settings/
    LANGUAGE_SETTING.json
    STYLE_SETTING.json
    CHAPTER_TEMPLATE.md
    SCENE_PLAN.md
    TIMELINE.md
    TRANSLATION_GLOSSARY.md
  draft/
    zh/
      vol01/
        ch01/
          scene01.md
          scene02.md
        ch01_zh.md
      vol01_zh.md
    FULL_NOVEL_zh.md
  assets/
    IMAGE_MAP.json
    export/
  output/
    novel_zh.txt
```

For small one-shot tasks, use the same workflow conceptually but avoid creating unnecessary files.

## Workflow

1. Determine the requested operation:
   - Creative blueprint / story vision: read `references/conception-blueprint.md`.
   - Full outline or volume/module outline: read `references/outline-planning.md`.
   - Chapter outline / scene planning: read `references/chapter-outline.md`.
   - Outline repair or lightweight normalization: read `references/outline.md`.
   - Character bible generation or update: read `references/character-design.md`.
   - Medium/long cast library splitting: read `references/character-library.md`.
   - Worldbuilding, locations, factions, items, or weapons: read `references/world-library.md`.
   - Ability, magic, power, cultivation, system, or combat-rule design: read `references/ability-system.md`.
   - In-world terminology, titles, slang, or setting-specific words: read `references/terminology.md`.
   - Language setup: read `references/style-language.md`.
   - Prose style setup: read `references/novel-style.md`.
   - Topic/style profile such as Chinese light novel or cinematic character-worldbuilding: read `references/topic-guidance.md`.
   - Scene and chapter drafting or revision: read `references/scene-chapter-writing.md`.
   - Chapter prose generation from a plan: read `references/chapter-prose-execution.md`.
   - Chapter critique, rewrite, or edit pass: read `references/chapter-revision.md`.
   - Optional image mapping: read `references/asset-map.md`.
   - TXT-first export: read `references/export.md`.
   - End-to-end project: read `references/workflow.md`, then load only the phase references needed.
2. Preserve user-provided creative prompts, outline methods, topic/style profiles, and constraints as project rules. If a later topic-specific guide is supplied, keep it as a separate reference and apply it after the general structure workflow.
3. Use internal theory to reason, but explain recommendations in concrete story terms: reader feeling, conflict, character change, information reveal, pacing, and scene function.
4. Keep state in `NOVEL_STATE.json` after each phase, scene, chapter assembly, or volume assembly. Resume from state instead of restarting when possible.
5. Draft and revise scene files first. Assemble multiple coherent scenes into a chapter, then assemble chapters into a volume, then assemble volumes into the full novel.
6. Maintain blueprint, outline, chapter outline, character bible, timeline, and style settings as consistency anchors. Fix scene prose when it contradicts established facts or the current plan; do not silently mutate canon or outline to excuse the contradiction.
7. For medium/long projects, prefer indexed libraries over single bible files: character library, world library, ability system, and terminology. Load only the files relevant to the active scene.
8. Export TXT by default using `scripts/assemble_novel.py`. Use `scripts/extract_pdf_images.py` only for optional PDF image extraction.

## Quality Gates

- Before autonomous drafting starts, pause at these gates by default:
  1. Character review: summarize `CHARACTER_BIBLE.md` or `CHARACTER_INDEX.md` plus relevant character files, relationship map, inferred traits, and consistency risks; wait for user confirmation.
  2. World / ability / terminology review: summarize `WORLD_BIBLE.md` or indexed world library, ability system, key objects, weapons, locations, factions, in-world terms, inferred rules, and consistency risks; wait for user confirmation when relevant.
  3. Language confirmation: summarize `LANGUAGE_SETTING.json`, primary language, bilingual/translation status, translation glossary rules, and output filenames; wait for user confirmation.
  4. Prose style confirmation: summarize `STYLE_SETTING.json`, POV, tense, genre/topic profile, chapter/scene length, dialogue density, and custom style file; wait for user confirmation.
- Before drafting a batch of scenes: confirm creative blueprint, outline or module outline, chapter/scene plan, character/world/ability/term libraries, language, style, chapter range, and whether autonomous continuation is allowed.
- Before filling an empty plan or library: propose options first. Do not turn inferred setting, ability, terminology, outline, or scene-plan choices into complete canon until the user confirms the direction.
- Before drafting each new chapter in autonomous mode: summarize the chapter's scene chain, reader reward, ending interface, and continuity risks; wait for user approval unless the user explicitly enabled uninterrupted batch drafting.
- Before changing an established outline or chapter outline during drafting: require a clear user instruction, then summarize ripple effects before applying the change.
- After completing each chapter: report scene files, major state changes, new/updated characters, timeline changes, and whether the next chapter plan is still valid.
- Before image placement: summarize selected images and insertion targets, then wait for approval.
- Before overwriting completed chapters or outputs: create timestamped backups or ask for confirmation.

## Resource Map

- `references/workflow.md`: end-to-end lifecycle, state model, and phase gates.
- `references/conception-blueprint.md`: turn a rough origin into a creative blueprint and writer vision.
- `references/outline-planning.md`: turn the blueprint into a whole-story skeleton and module/volume outline.
- `references/chapter-outline.md`: turn a module outline into chapter outlines and scene-level plans.
- `references/outline.md`: lightweight outline repair, diagnosis, and normalization helpers.
- `references/character-design.md`: character bible schema and update rules.
- `references/character-library.md`: indexed character libraries for medium/long projects.
- `references/world-library.md`: world rules, locations, factions, items, weapons, and setting state.
- `references/ability-system.md`: ability, magic, cultivation, system, skill, and power-rule design.
- `references/terminology.md`: in-world terms, titles, slang, and terminology distinct from translation glossaries.
- `references/style-language.md`: Chinese-first language defaults and prose style settings.
- `references/novel-style.md`: detailed genre, POV, prose density, rhythm, chapter/scene length, and custom style configuration.
- `references/topic-guidance.md`: reusable topic/style profiles, including Chinese light novel and cinematic character-worldbuilding fiction.
- `references/scene-chapter-writing.md`: scene-level drafting, chapter assembly, continuation, and revision.
- `references/chapter-prose-execution.md`: scene-first prose generation, then chapter and volume assembly.
- `references/chapter-revision.md`: scene-first critique and rewrite workflow, then chapter and volume consistency checks.
- `references/asset-map.md`: optional image inventory, filtering, placement, and approval gate.
- `references/export.md`: TXT-first assembly and optional pandoc formats.
- `assets/`: reusable example settings and style templates copied into projects when helpful.
- `scripts/assemble_novel.py`: assemble scene/chapter markdown into full novel markdown and TXT.
- `scripts/extract_pdf_images.py`: optional PDF image extraction helper.
