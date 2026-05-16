# Character Design

Use this reference to create or update `novel/characters/CHARACTER_BIBLE.md`. It preserves the original repo's character-bible intent while fitting the scene-first workflow.

## Contents

- Inputs
- Modes
- Extraction
- Character Bible Schema
- New Character Stub
- Update Rules
- Summary Report

## Inputs

Prefer:

- `CREATIVE_BLUEPRINT.md`
- `OUTLINE.md`
- `CHAPTER_OUTLINE.md` or `SCENE_PLAN.md`
- pasted character notes or user instructions
- PDF/visual source material if the user provides it

For PDF or image-heavy source material, extract character and world clues from text plus visible details. Do not create deep backstory from an image alone; use visual details for appearance anchors and world notes.

## Modes

- Fresh design: no bible exists; build from blueprint and outline.
- Add/update: bible exists and a new character appears during scene drafting.
- Rebuild: user explicitly requests refresh/rebuild; archive the old bible first.
- Retcon: user explicitly changes canon; preserve old information with a note rather than silently erasing it.

## Extraction

Read the source and identify:

- all named characters and aliases
- first appearance, role, and story function
- want, need, fear, secret, contradiction
- relationships, emotional debts, and power imbalance
- visual anchors and signature items
- speech patterns implied by culture, age, class, personality, and role
- knowledge boundaries: what they know, do not know, and when they learn it

Classify:

- Major: protagonist, deuteragonist, primary antagonist, or core relationship character
- Supporting: recurring character with dialogue, pressure, or plot influence
- Minor: one-scene or low-impact character; keep to table entry unless they return

## Character Bible Schema

```markdown
# Character Bible

## Major Characters

### [Name]

**Role**:
**First appears**:
**Status**:

#### Identity
- Age:
- Background:
- Social position:
- Names / aliases:

#### Appearance
- Stable visual anchors:
- Clothing / bearing:
- Signature object or gesture:

#### Desire and Pressure
- Surface want:
- Deep need:
- Fear:
- Will not admit:
- External pressure:

#### Personality Core
- Public mask:
- Private truth:
- Decision pattern:
- Contradiction:

#### Speech Fingerprint
- Vocabulary:
- Sentence rhythm:
- Directness / evasions:
- Pet phrases:
- Avoids saying:
- Emotional leakage:
- Sample line:

#### Relationships
| Character | Dynamic | Current tension | Direction |
|---|---|---|---|

#### Knowledge State
- Knows:
- Does not know:
- Learns in:

#### Arc
- Start:
- Pressure tests:
- Breakpoint:
- End direction:
```

Supporting characters may use a shorter version, but still need visual anchor, personality anchor, and speech fingerprint before important dialogue.

Minor characters:

```markdown
## Minor Characters
| Name | First appears | Function | One-line description |
|---|---|---|---|
```

## New Character Stub

Before a new major/supporting character speaks in prose:

```markdown
### [Name] (stub - added VolNN ChNN SceneNN)
**Role**:
**First appears**:
**Status**:
- Visual anchor:
- Personality anchor:
- Speech fingerprint:
- Relationship to scene cast:
- Notes to expand:
```

## Update Rules

- The bible is the consistency source of truth.
- If a scene contradicts the bible, fix the scene unless the user approves a canon update.
- Never write a major/supporting character's first important dialogue without a speech fingerprint.
- Track knowledge changes after each scene with major reveals.
- Keep relationship states current; scene writing depends on them.
- Do not invent major backstory unless the outline supports it or the user requested expansion.
- Preserve suspected secrets and future reveals; do not expose them in the bible summary shown to readers.

## Summary Report

After creating or updating the bible, report:

- major/supporting/minor counts
- newly added stubs
- relationship pressure points
- consistency risks
- next file that should be updated, if any
