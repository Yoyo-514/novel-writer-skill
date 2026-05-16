# Character Design

Use this reference to create, update, or rebuild `novel/characters/CHARACTER_BIBLE.md`. The character bible is the consistency source for prose writing: appearance, voice, motive, relationships, knowledge state, and character-relevant world notes should be kept here.

This workflow keeps the useful detail from the original character-design command, but removes platform-specific slash-command behavior.

## Contents

- Inputs
- Modes
- Source Handling
- Extraction Pass
- Setting and Register Pass
- Character Classification
- Character Bible Schema
- Supporting and Minor Characters
- New Character Stub
- Relationship Map
- World Notes
- Update and Retcon Rules
- Consistency Rules
- Summary Report

## Inputs

Prefer:

- `CREATIVE_BLUEPRINT.md`
- `OUTLINE.md`
- `CHAPTER_OUTLINE.md` or `SCENE_PLAN.md`
- existing `CHARACTER_BIBLE.md`
- pasted character notes, scene notes, or user instructions
- PDF/visual source material if the user provides it

If no usable outline or character source exists, ask for a story outline, character list, scene context, or pasted notes before building anything substantial.

## Modes

- Fresh design: no bible exists; build from blueprint, outline, and provided notes.
- Add/update: bible exists and a new character appears during scene drafting.
- Enrich: bible exists but profiles are too thin for prose; deepen selected characters without changing canon.
- Rebuild: user explicitly requests refresh/rebuild; archive the old bible first.
- Retcon: user explicitly changes canon; preserve the old entry with a dated note rather than silently erasing it.

Before overwriting `CHARACTER_BIBLE.md`, create a timestamped backup when a previous file exists.

## Source Handling

For text outlines:

- extract names, aliases, roles, scenes, relationships, and implied motives
- separate explicit canon from inference
- mark vague or inferred traits clearly

For PDFs:

- read text first
- if the PDF is long, process by page ranges or logical sections
- treat embedded illustrations, maps, tables, and diagrams as supporting evidence, not as permission to invent hidden backstory

For visual material:

- character illustration: use for visual anchors, clothing, body language, signature items
- map or location diagram: add character-relevant location and culture notes to World Notes
- table, timeline, or chart: extract named entities, factions, dates, ranks, and relationship clues
- image-heavy page: record what was extracted and which profile it affects

Never create deep personal history from a picture alone.

## Extraction Pass

Create an extraction table before writing full profiles:

```markdown
| Character | First mention | Role signal | Known traits | Relationships | Evidence |
|---|---|---|---|---|---|
| [Name] | Vol/Ch/Scene or source line | protagonist/support/etc. | ... | ... | explicit / inferred |
```

Extract:

- all named characters and aliases
- first appearance or first mention
- story function and role
- visible traits and recurring symbols
- surface want, deep need, fear, secret, contradiction
- major choices at turning points
- relationships, emotional debts, promises, rivalries, and power imbalance
- knowledge boundaries: what they know, do not know, reveal, conceal, or misunderstand
- speech clues: register, vocabulary, rhythm, directness, evasions, pet phrases, forbidden phrasing
- setting clues that affect names, clothing, hierarchy, dialect, honorifics, taboo, education, and etiquette

If a trait is inferred, write it as inferred:

```markdown
- Inferred trait: avoids direct confrontation, based on [scene/source].
```

## Setting and Register Pass

Before finalizing major/supporting profiles, consider the story's cultural and genre context:

- Contemporary: current speech, social media habits, school/workplace norms, realistic fashion and class markers.
- Historical: period vocabulary, etiquette, hierarchy, taboo, naming customs, and anachronism risks.
- Fantasy or science fiction: invented register should fit the world's institutions, technology, magic, class, species, or region.
- Chinese light novel: keep voice readable, distinct, and interaction-friendly; character charm should emerge through behavior, contrast, inner commentary, and relationship dynamics.
- Cinematic / literary hybrid: mark visual anchors, silence, gesture, subtext, and what the character avoids saying.

Add global naming, dialect, honorific, faction, or culture notes under World Notes when they affect multiple characters.

## Character Classification

- Major: protagonist, deuteragonist, primary antagonist, core relationship character, or character carrying a major arc.
- Supporting: recurring character with dialogue, plot pressure, emotional influence, or setting function.
- Minor: one-scene or low-impact character; keep as table entry unless they return or affect the plot.

Do not overbuild minor characters. If a character appears once, has no meaningful dialogue, and causes no lasting state change, give only a one-line entry.

## Character Bible Schema

```markdown
# Character Bible

> Source:
> Novel:
> Last updated:
> Current drafting point:

## Major Characters

### [Name]

**Role**:
**First appears**:
**Status**:

#### Identity
- Full name:
- Aliases / titles:
- Age:
- Pronouns:
- Background:
- Social position:
- Faction / family / group:

#### Appearance
- Height / build:
- Stable visual anchors:
- Distinctive features:
- Clothing / bearing:
- Signature object:
- Gesture or body-language tell:

#### Personality Core
Three traits that should remain stable unless a major arc changes them:

1. [Trait plus behavioral proof]
2. [Trait plus behavioral proof]
3. [Trait plus behavioral proof]

#### Desire and Pressure
- Surface want:
- Deep need:
- Fear:
- Secret:
- Will not admit:
- External pressure:
- Internal contradiction:

#### Speech Fingerprint
- Vocabulary:
- Sentence rhythm:
- Directness / evasions:
- Pet phrases:
- Would never say:
- Emotional leakage:
- Register shifts under stress:
- Sample line:

#### Backstory
Only include story-relevant backstory.

- Known past:
- Wound / formative pressure:
- What the reader can know now:
- What should remain hidden:

#### Relationships
| Character | Dynamic | Current tension | Debt / promise / secret | Direction |
|---|---|---|---|---|

#### Knowledge State
- Knows at story start:
- Does not know:
- Hides:
- Learns in:
- Reveals in:

#### Story Arc
- Start state:
- Surface goal:
- Internal conflict:
- Key turning points:
  - Vol/Ch/Scene:
- Breakpoint:
- End direction:

#### Consistency Watch
- Must preserve:
- Risk of acting out of character:
- Similar-name or similar-role confusion:
- Notes for future scenes:
```

## Supporting and Minor Characters

Supporting characters may use a shorter profile, but still need:

- role and first appearance
- visual anchor
- personality anchor
- speech fingerprint before important dialogue
- relationship to major characters
- knowledge state if they hold or reveal information
- plot function

Minor characters:

```markdown
## Minor Characters
| Name | First appears | Function | One-line description | Return risk |
|---|---|---|---|---|
```

## New Character Stub

Before a new major/supporting character speaks in prose, add at least:

```markdown
### [Name] (stub - added VolNN ChNN SceneNN)
**Role**:
**First appears**:
**Status**:
- Visual anchor:
- Personality anchor:
- Speech fingerprint:
- Relationship to scene cast:
- Scene function:
- Knowledge boundary:
- Notes to expand:
```

Present the stub to the user when the new character is important, surprising, or likely to recur.

## Relationship Map

Include a table or text diagram after the character sections:

```markdown
## Relationship Map

| Pair / Group | Current dynamic | Pressure | Expected movement |
|---|---|---|---|
| A - B | childhood friends | unspoken promise | trust -> rupture -> repair |
```

Use relationship entries to track:

- romance / friendship / family / rivalry
- hierarchy and dependence
- emotional debt
- secrets and one-sided knowledge
- relationship stage changes after scenes

For relationship-driven stories, update this section after every major scene that changes trust, intimacy, resentment, fear, or obligation.

## World Notes

Add only character-relevant world notes:

- naming conventions
- honorifics and forms of address
- dialect, class register, education markers
- faction ranks and social hierarchy
- clothing norms and taboo
- culture-specific gestures or etiquette
- locations that shape a character's behavior
- shared history that affects relationships

Keep worldbuilding here practical. Broader setting lore belongs in outline or setting files unless it directly affects character behavior or voice.

## Update and Retcon Rules

- The bible is the consistency source of truth.
- If a scene contradicts the bible, fix the scene unless the user approves a canon update.
- Track knowledge changes after scenes with major reveals.
- Keep relationship states current.
- Never delete old canon silently. For retcons, mark the replaced detail and add a dated note.
- Do not invent major backstory unless the outline supports it or the user requested expansion.
- Preserve suspected secrets and future reveals; do not expose them in reader-facing summaries.
- If rebuilding, archive the old bible before writing the new one.

Retcon note format:

```markdown
> Retcon [YYYY-MM-DD]: [old detail] replaced by [new detail]. Reason: [user request / outline revision].
```

## Consistency Rules

- Never write a major/supporting character's first important dialogue without a speech fingerprint.
- Important actions must follow desire, fear, pressure, relationship, or knowledge state.
- Character charm should be shown through specific behavior, not just labels.
- Avoid making different characters speak with the same rhythm.
- Do not let a character know information they have not learned yet.
- Do not resolve a relationship shift without a scene-level cause.
- If a profile is thin, mark what is missing instead of pretending it is complete.

## Summary Report

After creating or updating the bible, report:

- major/supporting/minor counts
- newly added or enriched profiles
- inferred traits that need user confirmation
- relationship pressure points
- world notes added
- consistency risks
- next file that should be updated, if any
