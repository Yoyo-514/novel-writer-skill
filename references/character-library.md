# Character Library

Use this reference for medium and long projects where one `CHARACTER_BIBLE.md` would become too large. It extends `character-design.md` with an indexed, split-file character library.

For short works, a single `CHARACTER_BIBLE.md` is acceptable. For medium/long works, prefer `CHARACTER_INDEX.md` plus per-character files.

## Contents

- When to Split
- Recommended Layout
- Character Index
- Major Character File
- Supporting Character File
- Minor Character Table
- Relationship Files
- Loading Strategy
- Update Rules
- Migration from Single Bible

## When to Split

Use the split library when:

- the cast has more than roughly 8 important recurring characters
- multiple volumes introduce new groups
- relationships are a major engine
- characters carry long arcs, secrets, aliases, or shifting loyalties
- prose drafting frequently loads irrelevant character information

Keep a single bible when the project is short, the cast is small, or the user wants a lightweight setup.

## Recommended Layout

```text
novel/characters/
  CHARACTER_INDEX.md
  major/
    [character-name].md
  supporting/
    [character-name].md
  minor/
    MINOR_CHARACTERS.md
  relationships/
    RELATIONSHIP_MAP.md
    [relationship-thread].md
```

Use filename slugs that are stable and readable. Chinese filenames are allowed when they are convenient for the user.

## Character Index

`CHARACTER_INDEX.md` is navigation, not the full bible:

```markdown
# Character Index

## Major
| Name | Role | First Appears | File | Current Status | Load When |
|---|---|---|---|---|---|

## Supporting
| Name | Role | First Appears | File | Current Status | Load When |
|---|---|---|---|---|---|

## Minor
See `minor/MINOR_CHARACTERS.md`.

## Relationship Files
| Thread | File | Characters | Status |
|---|---|---|---|
```

Keep the index current after new characters, deaths, faction changes, major relationship changes, or new relationship-thread files.

## Major Character File

```markdown
# [Character Name]

## Metadata
- Role:
- First appears:
- Current status:
- Last updated:

## Identity
- Full name:
- Aliases / titles:
- Age:
- Background:
- Social position:
- Faction / family / group:

## Appearance
- Stable visual anchors:
- Clothing / bearing:
- Signature item or gesture:

## Personality Core
- Stable traits:
- Contradiction:
- Public mask:
- Private truth:

## Desire and Pressure
- Surface want:
- Deep need:
- Fear:
- Secret:
- External pressure:

## Speech Fingerprint
- Vocabulary:
- Sentence rhythm:
- Pet phrases:
- Would never say:
- Register shifts:
- Sample line:

## Story-Relevant Backstory
- Known:
- Hidden:
- Reveal plan:

## Relationships
- See:
- Current key tensions:

## Knowledge State
- Knows:
- Does not know:
- Hides:
- Learns in:

## Arc
- Start:
- Turning points:
- Current state:
- End direction:

## Ability / Equipment Links
- Ability profile:
- Items:
- Weapons:

## Consistency Watch
- Must preserve:
- Risks:
- Open questions:
```

## Supporting Character File

Supporting files can be shorter, but must include:

- role and first appearance
- visual anchor
- personality anchor
- speech fingerprint before important dialogue
- relationship to major cast
- plot function
- knowledge state if they carry information
- promotion condition: what would make them major

## Minor Character Table

Use `minor/MINOR_CHARACTERS.md`:

```markdown
# Minor Characters

| Name | First Appears | Function | One-line Description | Return Risk |
|---|---|---|---|---|
```

Promote a minor character to supporting when they recur, speak meaningfully, alter a relationship, hold information, or gain a future function.

## Relationship Files

Use `RELATIONSHIP_MAP.md` for the overview and optional thread files for complex dynamics:

```markdown
# [Relationship Thread]

## Characters

## Starting Dynamic

## Pressure Points

## Stage Changes
| Vol/Ch/Scene | Change | Cause | Consequence |
|---|---|---|---|

## Secrets / One-Sided Knowledge

## Future Payoff
```

Relationship files are especially useful for romance, rivalry, family debt, mentor-student dynamics, factions, and multi-volume betrayals.

## Loading Strategy

Before writing a scene, load:

- `CHARACTER_INDEX.md`
- files for POV character and active scene cast
- relevant relationship thread files
- minor table only when a minor character appears or returns

Do not load the entire character library by default for long projects.

## Update Rules

After each scene or chapter, update:

- relationship state changes
- knowledge changes
- status changes
- new aliases, injuries, equipment, abilities, or faction ties
- promotion from minor to supporting
- index rows and relationship files

Never modify a character's canon to justify a drifting scene unless the user approved the change.

## Migration from Single Bible

When migrating from `CHARACTER_BIBLE.md`:

1. Archive the original file.
2. Create `CHARACTER_INDEX.md`.
3. Split major characters first.
4. Move supporting characters next.
5. Leave true minor characters in `MINOR_CHARACTERS.md`.
6. Create relationship map from existing relationship tables.
7. Update workflow references to load the index and relevant files.
