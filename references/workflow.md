# End-to-End Novel Workflow

## Contents

- Phase 0: Intake and Project Initialization
- Outline Authority
- State Model
- Phase Order
- Proposal Before Completion
- Confirmation Gates
- Gate Output Format
- Chapter Drafting Gate
- Library Strategy
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

Choose a library shape by project scale. Do not require both shapes at once.

For small or lightweight projects, use single files as needed:

- `novel/characters/CHARACTER_BIBLE.md`
- `novel/world/WORLD_BIBLE.md`
- `novel/world/TERMINOLOGY.md` for in-world terms
- `novel/world/abilities/ABILITY_SYSTEM.md` when abilities, magic, systems, cultivation, or special powers exist

For medium/long projects, use indexed libraries as needed:

- `novel/characters/CHARACTER_INDEX.md` and per-character files
- `novel/world/WORLD_INDEX.md`
- `novel/world/abilities/ABILITY_SYSTEM.md`
- `novel/world/terms/TERM_INDEX.md`

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
4. Character design: for small works, create or update `CHARACTER_BIBLE.md`; for medium/long works, create `CHARACTER_INDEX.md` and per-character files.
5. Character library review: verify the chosen character structure and split or merge only if scale requires it.
6. Character review gate: summarize characters, relationship map, inferred traits, missing information, and consistency risks; wait for user confirmation before automatic prose drafting.
7. World library setup: for small works, create `WORLD_BIBLE.md`; for medium/long works, create `WORLD_INDEX.md` plus world rules, location, faction, item, and weapon files when relevant.
8. Ability system setup: when abilities matter, create `ABILITY_SYSTEM.md`; for medium/long works, also create ability category, single ability, and per-user ability profile files.
9. Terminology setup: for small works, create `TERMINOLOGY.md`; for medium/long works, create `TERM_INDEX.md` and term files. Keep both separate from translation glossary.
10. World / ability / terminology review gate: summarize core rules, limits, costs, terms, inferred items, and contradictions; wait for user confirmation.
11. Language setup: create `LANGUAGE_SETTING.json` with Chinese monolingual defaults unless the user requested otherwise.
12. Language confirmation gate: summarize primary language, bilingual/translation status, translation glossary rules, and output names; wait for user confirmation.
13. Style setup: create `STYLE_SETTING.json` and `CHAPTER_TEMPLATE.md`.
14. Style confirmation gate: summarize POV, tense, genre/topic profile, prose density, dialogue density, scene/chapter length, and custom style file; wait for user confirmation.
15. Draft scenes: write scene files sequentially.
16. Assemble chapters: combine approved scenes into `chNN_zh.md`.
17. Assemble volumes: combine approved chapters into `volNN_zh.md`.
18. Export: assemble volumes into the full novel and write TXT first.

## Proposal Before Completion

When a requested artifact is missing, empty, or too vague, do not complete it from assumptions. First provide a compact proposal packet with 2-3 options, then wait for the user to choose, merge, or modify.

This applies to:

- creative blueprint and writer vision
- whole-story outline, module outline, chapter outline, or scene plan
- character, world, ability, item, weapon, and terminology libraries
- language and prose style settings
- prose drafting when no usable scene card exists

Use this shape:

```markdown
## Proposal: [Area]

[1.1] [Option name]
- Core direction:
- What it enables:
- Risk:
- Assumptions:

[1.2] [Option name]
- Core direction:
- What it enables:
- Risk:
- Assumptions:

Options can be merged. After you choose or revise one, I will turn it into the full file/outline/scene plan/prose draft.
```

Only skip this proposal step when the user explicitly asks Codex to decide and proceed.

## Confirmation Gates

Default to gated mode for full projects and any autonomous/batch writing. Pause before:

- accepting or changing the creative blueprint
- accepting or changing the whole-story outline, module outline, chapter outline, or scene plan
- committing to a full outline restructure
- changing `OUTLINE.md`, `CHAPTER_OUTLINE.md`, or `SCENE_PLAN.md` during prose drafting
- moving from module outline to chapter outline
- finishing character design and starting prose drafting
- finishing world, ability, or terminology setup and starting prose drafting
- finishing language setup and starting prose drafting
- finishing style setup and starting prose drafting
- starting a new chapter in autonomous mode, unless the user explicitly approved uninterrupted batch drafting
- starting long autonomous drafting
- rewriting existing chapters
- adding a recurring major/supporting character during drafting
- introducing a major location, faction, item, weapon, ability, magic rule, or in-world term during drafting
- making a plan drift official
- inserting image references into prose
- exporting over existing output files

Continue without a gate for small local edits, state updates, or TXT preview assembly unless the user asked for strict review.

For single-scene drafting, use a light gate. If the scene card is missing or inferred, offer scene-card options first; proceed only after the user confirms or explicitly asks Codex to decide.

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
- world, ability, item, weapon, and term files needed
- continuity risks from timeline, relationship, knowledge state, or outline
- consistency risks from world rules, ability limits, item custody, terminology, or reader/character knowledge
- files to be created or overwritten

After each chapter, pause unless the user explicitly allowed continuing:

- report written scenes and assembled chapter
- summarize state changes
- list character/world/ability/term/timeline/glossary updates
- confirm whether the next chapter plan still fits

## Library Strategy

Use lightweight single files for small works. Use indexed libraries for medium/long works:

- Characters: `CHARACTER_BIBLE.md` for small works, or `CHARACTER_INDEX.md` plus per-character files for medium/long works.
- World: `WORLD_BIBLE.md` for small works, or `WORLD_INDEX.md` plus rules, locations, factions, items, and weapons for medium/long works.
- Abilities: `ABILITY_SYSTEM.md` for any project where abilities matter; medium/long works add ability category, single ability, and user profile files.
- Terminology: `TERMINOLOGY.md` for small works, or `TERM_INDEX.md` plus term files for medium/long works.

Before each scene, load only the relevant files. Do not load the entire cast or world library by default.

Keep `TERMINOLOGY.md` / `TERM_INDEX.md` distinct from `TRANSLATION_GLOSSARY.md`: the former defines in-world meaning, the latter defines bilingual rendering.

## Manifest

Append important created files to `novel/MANIFEST.md`:

```markdown
| Timestamp | Operation | File | Description |
|-----------|-----------|------|-------------|
| ... | outline | novel/OUTLINE.md | 12-chapter revised outline |
```
