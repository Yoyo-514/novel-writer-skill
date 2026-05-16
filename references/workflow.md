# End-to-End Novel Workflow

## Contents

- Phase 0: Intake and Project Initialization
- Outline Authority
- State Model
- Phase Order
- Confirmation Gates
- Gate Output Format
- Chapter Drafting Gate
- Manifest

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
5. Character review gate: summarize characters, relationship map, inferred traits, missing information, and consistency risks; wait for user confirmation before automatic prose drafting.
6. Language setup: create `LANGUAGE_SETTING.json` with Chinese monolingual defaults unless the user requested otherwise.
7. Language confirmation gate: summarize primary language, bilingual/translation status, glossary rules, and output names; wait for user confirmation.
8. Style setup: create `STYLE_SETTING.json` and `CHAPTER_TEMPLATE.md`.
9. Style confirmation gate: summarize POV, tense, genre/topic profile, prose density, dialogue density, scene/chapter length, and custom style file; wait for user confirmation.
10. Draft scenes: write scene files sequentially.
11. Assemble chapters: combine approved scenes into `chNN_zh.md`.
12. Assemble volumes: combine approved chapters into `volNN_zh.md`.
13. Export: assemble volumes into the full novel and write TXT first.

## Confirmation Gates

Default to gated mode for full projects and any autonomous/batch writing. Pause before:

- accepting or changing the creative blueprint
- accepting or changing the whole-story outline, module outline, chapter outline, or scene plan
- committing to a full outline restructure
- changing `OUTLINE.md`, `CHAPTER_OUTLINE.md`, or `SCENE_PLAN.md` during prose drafting
- moving from module outline to chapter outline
- finishing character design and starting prose drafting
- finishing language setup and starting prose drafting
- finishing style setup and starting prose drafting
- starting a new chapter in autonomous mode, unless the user explicitly approved uninterrupted batch drafting
- starting long autonomous drafting
- rewriting existing chapters
- adding a recurring major/supporting character during drafting
- making a plan drift official
- inserting image references into prose
- exporting over existing output files

Continue without a gate for small local edits, state updates, or TXT preview assembly unless the user asked for strict review.

For single-scene drafting, use a light gate: confirm the scene card if it is missing or inferred, then proceed.

## Gate Output Format

Use short confirmation packets:

```markdown
## Gate: [Name]

- Confirmed facts:
- Inferred items needing approval:
- Risks:
- Files to be written or updated:
- Next action after approval:
```

Do not bury the approval request in a long explanation. Ask clearly whether to proceed.

## Chapter Drafting Gate

Before each chapter in autonomous mode, show:

- chapter number and volume position
- scene chain and what each scene changes
- reader reward and chapter-ending interface
- characters used and any new character stubs needed
- continuity risks from timeline, relationship, knowledge state, or outline
- files to be created or overwritten

After each chapter, pause unless the user explicitly allowed continuing:

- report written scenes and assembled chapter
- summarize state changes
- list character/timeline/glossary updates
- confirm whether the next chapter plan still fits

## Manifest

Append important created files to `novel/MANIFEST.md`:

```markdown
| Timestamp | Operation | File | Description |
|-----------|-----------|------|-------------|
| ... | outline | novel/OUTLINE.md | 12-chapter revised outline |
```
