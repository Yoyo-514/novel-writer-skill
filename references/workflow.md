# End-to-End Novel Workflow

## Phase 0: Intake and Project Initialization

Parse the user's request for:

- source material: rough idea, existing outline, PDF, notes, or pasted text
- operation: create blueprint, revise blueprint, create outline, revise outline, create chapter outline, draft scenes, continue chapters, export
- language: default `zh` and monolingual
- target length: total chapters, scenes per chapter, words per scene/chapter
- style: genre, POV, tense, density, custom style guide
- output: default `txt`
- image use: default disabled

## Outline Authority

Treat `OUTLINE.md`, `CHAPTER_OUTLINE.md`, and `SCENE_PLAN.md` as strong references. During drafting, follow the current plan unless the user explicitly instructs Codex to change it.

Plans may evolve because writing reveals better choices. When the user clearly asks to change the outline mid-project:

1. Pause drafting.
2. Identify which plan files are affected.
3. Summarize ripple effects on later chapters, character arcs, reveals, timeline, and already drafted prose.
4. Ask for confirmation if the change is broad or affects completed chapters.
5. Apply the outline update and record it in `MANIFEST.md` or state notes.
6. Resume from the revised plan.

Initialize only the directories needed for the requested operation. For a full project, create `novel/characters`, `novel/settings`, `novel/draft/zh`, `novel/output`, and optionally `novel/assets`.

## State Model

Persist progress to `novel/NOVEL_STATE.json`:

```json
{
  "title": "未命名小说",
  "phase": "scene_drafting",
  "language_mode": "monolingual",
  "primary_language": "zh",
  "output_priority": ["txt"],
  "total_chapters": 12,
  "current_chapter": "ch03",
  "current_scene": "scene02",
  "chapters_completed": 2,
  "status": "in_progress",
  "updated_at": "ISO-8601 timestamp"
}
```

When state exists, offer to resume unless the user clearly asks to start fresh.

## Phase Order

1. Creative blueprint: create or revise `CREATIVE_BLUEPRINT.md`.
2. Outline: create a whole-story skeleton and detailed near-term module/volume outline in `OUTLINE.md`.
3. Scene plan: define scene cards that later assemble into chapters and volumes.
4. Character design: create or update `CHARACTER_BIBLE.md` from the blueprint and outline.
5. Style/language: create settings with Chinese monolingual defaults.
6. Draft scenes: write scene files sequentially.
7. Assemble chapters: combine approved scenes into `chNN_zh.md`.
8. Assemble volumes: combine approved chapters into `volNN_zh.md`.
9. Export: assemble volumes into the full novel and write TXT first.

## Confirmation Gates

Pause before:

- committing to a full outline restructure
- confirming or changing the creative blueprint
- changing `OUTLINE.md`, `CHAPTER_OUTLINE.md`, or `SCENE_PLAN.md` during prose drafting
- moving from module outline to chapter outline
- starting long autonomous drafting
- rewriting existing chapters
- inserting image references into prose
- exporting over existing output files

Continue without a gate for small local edits, single-scene drafting, state updates, or TXT preview assembly unless the user asked for strict review.

## Manifest

Append important created files to `novel/MANIFEST.md`:

```markdown
| Timestamp | Operation | File | Description |
|-----------|-----------|------|-------------|
| ... | outline | novel/OUTLINE.md | 12-chapter revised outline |
```
