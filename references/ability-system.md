# Ability System

Use this reference for magic systems, supernatural powers, cultivation, martial arts, technology powers, game systems, skills, blessings, curses, transformations, or any repeatable capability that can solve or create plot problems.

Ability systems should not be buried in the general world bible. They need separate rules, limits, costs, counters, growth paths, and per-user profiles.

## Contents

- When to Use
- Missing / Empty Ability Proposal Gate
- Recommended Layout
- Ability System File
- Ability School File
- Single Ability File
- Character Ability Profile
- Power Scale
- Balance and Plot-Break Checks
- Reveal Management
- Ability Gate
- Scene and Chapter Updates

## When to Use

Create ability files when the story includes:

- magic, spells, spiritual arts, cultivation, martial techniques, psychic powers, systems, game skills, superpowers, blessings, curses, or advanced technology powers
- combat where abilities decide outcomes
- non-combat problem solving through special powers
- progression, training, awakening, mutation, unlocking, leveling, or mastery
- ability secrets, hidden costs, counters, or school/faction techniques

## Missing / Empty Ability Proposal Gate

If the ability, magic, cultivation, system, or power rules are absent or empty, do not write a complete ability system immediately. First offer 2-3 system models and wait for user confirmation.

Each option should include:

- source of power
- trigger and growth method
- cost, limit, and counterplay
- user-facing reader appeal
- reveal strategy
- plot-break risk
- recommended file layout

After the user chooses, merges, or revises an option, create `ABILITY_SYSTEM.md` and any needed school, ability, or user-profile files.

## Recommended Layout

```text
novel/world/abilities/
  ABILITY_SYSTEM.md
  schools/
    [school-or-category].md
  abilities/
    [ability-name].md
  users/
    [character-name]-ability-profile.md
```

Keep ability rules separate from character psychology:

- ability file: what the ability can theoretically do
- user ability profile: what this character can currently do, misunderstand, misuse, or hide

## Ability System File

```markdown
# Ability System

## Core Premise
- Source:
- Categories:
- Trigger method:
- Growth method:
- Upper limit:
- Cost:
- Taboo:
- Counter logic:

## Public Knowledge
- What ordinary people know:
- What institutions teach:
- What myths or misinformation exist:

## Hidden Truth
- True origin:
- Hidden cost:
- Future reveal timing:

## Power Scale
| Tier | Description | Typical User | Cost | Narrative Risk |
|---|---|---|---|---|

## Conflict Rules
- What abilities can solve:
- What abilities cannot solve:
- What problems abilities create:
- Counterplay:
- Failure modes:

## Consistency Watch
- Rules that cannot be broken:
- Rules that can be misunderstood:
- Exceptions requiring user approval:
```

## Ability School File

Use school/category files for branches of power:

```markdown
# [School / Category Name]

## Role in System

## Common Techniques

## Training / Access

## Strengths

## Weaknesses

## Cultural / Faction Ties

## Known Users

## Reveal Notes
```

## Single Ability File

```markdown
# [Ability Name]

## Basic Effect

## Type / School

## User(s)

## First Appears

## Trigger Condition

## Cost / Limitation

## Counterplay

## Growth Path

## Visual / Sensory Signature

## Non-Combat Use

## Known By
- User knows:
- Other characters know:
- Reader knows:

## Reveal Plan

## Consistency Watch
- Could break plot if:
- Must not do:
- Needs setup before:
```

## Character Ability Profile

```markdown
# [Character Name] Ability Profile

## Current Abilities
| Ability | Mastery | Limit | First Used | Public? |
|---|---|---|---|---|

## Growth Plan

## Misuse / Failure Cases

## Combat Style

## Non-Combat Use

## Concealed Abilities

## Risk of Breaking Plot

## Update Log
| Vol/Ch/Scene | Change | Cause | Consequence |
|---|---|---|---|
```

Cross-link this file from the character's profile.

## Power Scale

Power scale should express story function, not just numbers:

- what a tier can affect
- what it costs
- what it cannot bypass
- how lower-tier users can survive or counter it
- what social consequence comes with the tier

Avoid unlimited abilities unless the story is explicitly about the cost, isolation, corruption, or narrative burden of that power.

## Balance and Plot-Break Checks

Before accepting an ability, ask:

- What problem does this ability solve?
- What problem does it create?
- What can it not solve?
- What is the cost or limit?
- Who can counter it?
- Why has it not already broken the world?
- Why can the character not use it every time?
- What information about it should be hidden from the reader?

## Reveal Management

Track three layers:

- user knowledge: what the character understands about their ability
- world knowledge: what factions, teachers, enemies, or witnesses know
- reader knowledge: what the prose has revealed

Do not reveal the full system too early unless system transparency is the selling point.

## Ability Gate

Before autonomous drafting if abilities are central, pause and confirm:

- core system premise
- categories and power scale
- costs and limits
- counterplay
- hidden truth and reveal boundaries
- first chapters' ability files and user profiles
- unresolved risks

If this gate is skipped, fight scenes, training, upgrades, and ability-driven problem solving are likely to drift.

## Scene and Chapter Updates

After scenes, update:

- new ability discovered or used
- mastery change
- cost paid
- injury or side effect
- public exposure
- counter discovered
- item/weapon interaction
- hidden rule revealed
- new risk to future outline
