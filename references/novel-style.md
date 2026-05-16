# Novel Style Configuration

Use this reference to create or revise `novel/settings/STYLE_SETTING.json` and `novel/settings/CHAPTER_TEMPLATE.md`. This is the Codex skill equivalent of the original `novel-style` command, updated for Chinese-first, scene-first drafting.

## Contents

- Defaults
- Argument Parsing
- Custom Style File
- Genre Guidance
- STYLE_SETTING.json Shape
- Chapter Template Requirements
- Mid-Project Changes
- Validation

## Defaults

- Language: Simplified Chinese
- Genre: auto-detect or `general`
- POV: third-person limited
- Tense: past
- Chapter target: 3000 Chinese characters
- Scene target: 700-1500 Chinese characters
- Scenes per chapter: 2-4, default 3
- Prose density: balanced
- Sentence rhythm: mixed
- Dialogue density: balanced

Always confirm genre when it materially affects prose expectations. Do not silently lock a story into a genre if the user's blueprint suggests a hybrid.

## Argument Parsing

### Genre

| Signals | Code | Default tendency |
|---|---|---|
| 都市 / 现代 / contemporary | `contemporary` | conversational, realistic pacing |
| 言情 / romance / 爱情 | `romance` | emotional interiority, subtext |
| 悬疑 / 推理 / thriller / mystery | `thriller` | tension, withheld information |
| 玄幻 / 奇幻 / fantasy / 修仙 | `fantasy` | world texture, elevated register where fitting |
| 科幻 / sci-fi / science fiction | `scifi` | speculative rules, conceptual clarity |
| 历史 / historical | `historical` | period register, slower buildup |
| 武侠 | `wuxia` | code, honor, poetic action |
| 纯文学 / literary fiction / 文学 | `literary` | psychological depth, thematic density |
| 轻小说 / light novel / 轻松 | `light` | fast cuts, lively dialogue |
| none | `general` | neutral, adaptive |

### POV

| Signals | Code |
|---|---|
| 第一人称 / first person / 我 | `first_person` |
| 第三人称限制 / limited third / close third | `third_limited` |
| 第三人称全知 / omniscient / 上帝视角 | `third_omniscient` |
| 第二人称 / second person | `second_person` |

### Other Settings

- Tense: past by default; present only if requested or genre/style strongly favors immediacy.
- Chapter length: parse `每章N字`, `N words`, `chapter_words`.
- Scene count: parse `每章N场`, `N scenes per chapter`.
- Prose density: `tight`, `balanced`, `rich`.
- Sentence rhythm: `staccato`, `mixed`, `flowing`.
- Dialogue density: `low`, `balanced`, `high`.
- Custom style file: any `.md` path or explicit style guide signal.

## Custom Style File

If a custom style guide is provided:

1. Resolve exact path, then `novel/[path]`, then project root.
2. Read the file and treat it as primary prose guidance.
3. Store the resolved path in `STYLE_SETTING.json`.
4. Re-read it before each chapter or scene draft, so edits take effect without rerunning style setup.

The style file governs prose texture. It does not override canon, outline events, blueprint priorities, POV, tense, or user constraints unless the user explicitly says so.

## Genre Guidance

Use these as defaults only; the creative blueprint, topic guidance, and any custom style file outrank them.

### Romance

- Prioritize inner emotional movement over external event density.
- Let dialogue carry subtext.
- Slow down at moments of hesitation, recognition, jealousy, tenderness, or loss.
- Ending turns should often be emotional rather than purely action-based.

### Thriller / Mystery

- Keep the reader slightly hungry for missing information.
- Use short causal chains and frequent state changes.
- Reserve reflection for aftermath, not urgent action.
- Chapter endings should create a sharp question or immediate pressure.

### Fantasy

- Reveal worldbuilding through action, cost, ritual, conflict, and consequence.
- Keep magic or special systems consistent.
- Let register vary by class, culture, education, and occasion.
- Landscape and setting description should reflect the POV character's stakes.

### Sci-Fi

- Clarify speculative rules through problem-solving and constraint.
- Avoid concept lectures unless the scene itself demands explanation.
- Let technology shape social behavior and personal choices.
- Track causal implications of each new rule.

### Historical / Wuxia

- Avoid anachronistic speech and concepts unless intentional.
- Let honor, duty, hierarchy, lineage, reputation, or custom shape action.
- Use restraint: not every feeling needs direct explanation.

### Literary

- Each scene should advance plot and deepen character, relationship, or meaning.
- Prefer implication, contradiction, and charged detail over overt summary.
- Keep thematic pressure embodied in concrete action.

### Light Novel

- Favor quick scene turns and readable momentum.
- Use dialogue and reaction contrast for character charm.
- Keep exposition short and attached to immediate action or comedy.

For 中式轻小说 specifically, read `topic-guidance.md`; it adds stronger requirements around character charm, CP chemistry, light conflict, ACG context, inner commentary, and daily-life scene function.

## STYLE_SETTING.json Shape

```json
{
  "genre": "general",
  "genre_name": "General Fiction",
  "pov": "third_limited",
  "pov_description": "Third-person limited, bound to the POV character's knowledge boundary",
  "tense": "past",
  "chapter_word_count_target": 3000,
  "chapter_word_count_range": [2400, 4200],
  "scene_word_count_target": 1000,
  "scene_word_count_range": [700, 1500],
  "scenes_per_chapter_target": 3,
  "prose_density": "balanced",
  "sentence_rhythm": "mixed",
  "dialogue_density": "balanced",
  "style_notes": "Generated from genre guidance or custom style file.",
  "custom_style_file": null,
  "chapter_ending_rule": "End each chapter with a meaningful turn, unresolved pressure, or emotional question.",
  "configured_at": "ISO-8601 timestamp"
}
```

## Chapter Template Requirements

Generate `CHAPTER_TEMPLATE.md` with:

- chapter target and scene target
- POV and tense
- scene-first drafting rule
- opening hook expectations
- scene development expectations
- midpoint or turn guidance
- closing pressure rule
- transition rules
- emotional expression constraints
- character voice consistency reminder

## Mid-Project Changes

If style changes after drafting started:

- warn that future scenes use the new style
- do not rewrite existing prose unless requested
- for restyle, back up existing chapter/scene files first
- preserve plot events and canon while changing prose texture

## Validation

Before drafting each scene:

- custom style file exists, if configured
- topic/style profile has been checked, if configured
- style does not contradict blueprint
- POV can support planned information control
- target length fits the scene function
- dialogue density matches the chapter's actual needs
