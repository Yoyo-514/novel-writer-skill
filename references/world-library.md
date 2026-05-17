# World Library

Use this reference to manage worldbuilding that is not primarily character psychology: core rules, history, culture, locations, factions, items, weapons, and other setting objects.

For short works, `WORLD_BIBLE.md` can be a single file. For medium/long works, use an indexed library.

## Contents

- When to Use
- Recommended Layout
- World Index
- Core Rule Files
- Location Files
- Faction Files
- Item Files
- Weapon Files
- State Changes
- Loading Strategy
- World Review Gate

## When to Use

Create or update the world library when the story includes:

- recurring locations
- factions, institutions, guilds, schools, sects, companies, states, families, or religions
- important items, relics, documents, keys, tools, vehicles, artifacts, or evidence
- weapons with narrative function
- setting rules that constrain action
- historical events or cultural rules that shape choices

Do not overbuild background lore that does not affect scenes, character choices, conflict, or reader expectation.

## Recommended Layout

```text
novel/world/
  WORLD_INDEX.md
  rules/
    CORE_RULES.md
    HISTORY.md
    CALENDAR_AND_TIME.md
    CULTURE_AND_SOCIAL_ORDER.md
  locations/
    [location-name].md
  factions/
    [faction-name].md
  items/
    [item-name].md
  weapons/
    [weapon-name].md
```

Use a single `WORLD_BIBLE.md` only for small projects.

## World Index

`WORLD_INDEX.md` is a navigation and status file:

```markdown
# World Index

## Core Rules
| Area | File | Status | Notes |
|---|---|---|---|

## Locations
| Name | Type | First Appears | File | Current State |
|---|---|---|---|---|

## Factions
| Name | Type | First Appears | File | Current State |
|---|---|---|---|---|

## Items
| Name | Type | Owner / Custody | File | Current State |
|---|---|---|---|---|

## Weapons
| Name | User / Owner | File | Current State |
|---|---|---|---|
```

## Core Rule Files

Use core files for rules that affect many scenes:

- `CORE_RULES.md`: what the world allows, forbids, costs, hides, or normalizes
- `HISTORY.md`: only history that affects current conflict or identity
- `CALENDAR_AND_TIME.md`: dates, seasons, festivals, travel time, timekeeping
- `CULTURE_AND_SOCIAL_ORDER.md`: hierarchy, etiquette, taboo, law, class, education, religion, norms

Each core rule should include:

- practical effect on scenes
- who knows it
- whether the reader knows it
- exceptions
- contradiction risks

## Location Files

```markdown
# [Location Name]

## Metadata
- Type:
- First appears:
- Current state:
- Related characters:
- Related factions:

## Visual / Sensory Anchors

## Function
- What scenes this location enables:
- What pressures or limits it creates:

## Rules and Constraints

## History / Reputation

## Information Revealed Here

## State Changes
| Vol/Ch/Scene | Change | Cause | Consequence |
|---|---|---|---|

## Consistency Watch
```

## Faction Files

```markdown
# [Faction Name]

## Identity
- Type:
- Public goal:
- Hidden goal:
- Resources:
- Territory / influence:

## Structure
- Leadership:
- Ranks:
- Internal factions:

## Methods and Values

## Relationships
| Faction / Character | Dynamic | Pressure |
|---|---|---|

## Current State

## Secrets and Reveals

## Consistency Watch
```

## Item Files

```markdown
# [Item Name]

## Metadata
- Type:
- First appears:
- Owner / custody:
- Current state:

## Physical Anchor

## Function
- What it can do:
- What it cannot do:
- Why it matters:

## Limitation / Cost

## History / Source

## Reveal / Payoff Plan

## State Changes
| Vol/Ch/Scene | Owner / state | Cause | Consequence |
|---|---|---|---|
```

## Weapon Files

```markdown
# [Weapon Name]

## User / Owner

## Physical Anchor

## Combat Function

## Strengths

## Weaknesses

## Cost / Maintenance / Damage

## Symbolic Meaning

## State Changes
```

Weapons that are also magical, technological, or ability-linked should cross-link to `ability-system.md` files.

## State Changes

Track setting changes after scenes:

- location damage, access, control, public reputation
- faction alliances, betrayals, losses, exposure, leadership changes
- item ownership, damage, activation, disappearance, reveal
- weapon damage, upgrades, stolen status, symbolic meaning shifts

## Loading Strategy

Before writing a scene, load:

- `WORLD_INDEX.md`
- active location file
- relevant faction files
- relevant item/weapon files
- core rule files only when they constrain the scene

Avoid loading broad history unless the scene uses it.

## World Review Gate

Before autonomous drafting in a setting-heavy project, summarize:

- world library structure being used: single file or split library
- core rules that affect immediate chapters
- locations/factions/items/weapons needed in the first writing range
- inferred world details needing user confirmation
- contradictions or missing limits that could break future scenes

Wait for user confirmation before long drafting.
