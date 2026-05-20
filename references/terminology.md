# Terminology

Use this reference for world-specific terms: special nouns, titles, slang, faction words, ability terms, ritual names, historical event names, social categories, in-world concepts, and other terms that shape reader understanding.

Do not confuse this with `TRANSLATION_GLOSSARY.md`. Terminology explains what a word means inside the fictional world. Translation glossary decides how that word is rendered in another language.

## Contents

- Boundary with Translation Glossary
- Missing / Empty Term Proposal Gate
- Recommended Layout
- Term Index
- Term File
- Term Types
- Reveal Strategy
- Writing Checks
- Translation Sync
- Update Rules

## Boundary with Translation Glossary

Use `novel/world/terms/` for story meaning:

- what the term means in the world
- who uses it
- who avoids it
- whether it is formal, slang, taboo, insulting, sacred, technical, or secret
- when the reader should understand it

Use `novel/settings/TRANSLATION_GLOSSARY.md` for bilingual rendering:

- source term
- target translation
- capitalization
- romanization
- whether translation is fixed or context-dependent

## Missing / Empty Term Proposal Gate

If no in-world terminology exists yet, do not create a full glossary from assumptions. First offer 2-3 terminology strategies and wait for user confirmation.

Each option should include:

- term categories to track
- tone: formal, slang-heavy, mythic, technical, factional, or mixed
- first-appearance reveal style
- split choice: `TERMINOLOGY.md` or `TERM_INDEX.md` plus term files
- risk of reader confusion

After the user chooses, merges, or revises an option, create the terminology library and keep it separate from `TRANSLATION_GLOSSARY.md`.

Example:

```markdown
World term: 星痕 means a visible trace of a forbidden contract.
Translation glossary: 星痕 -> Star Scar, always capitalized.
```

## Recommended Layout

```text
novel/world/terms/
  TERM_INDEX.md
  core_terms/
    [term].md
  slang_and_titles/
    [term].md
```

For small projects, `novel/world/TERMINOLOGY.md` is acceptable.

## Term Index

```markdown
# Term Index

## Core World Terms
| Term | Type | First Appears | File | Reveal Level |
|---|---|---|---|---|

## Ability Terms
| Term | Related System | File | Public Meaning | Hidden Meaning |
|---|---|---|---|---|

## Slang / Titles
| Term | Used By | Tone | Meaning |
|---|---|---|---|
```

Reveal level can be:

- unexplained: reader sees the word but lacks meaning
- partial: reader understands surface use
- functional: reader knows enough for scene logic
- full: reader understands origin, implication, and hidden meaning

## Term File

```markdown
# [Term]

## Definition
- Internal meaning:
- Type:
- First appears:
- Related files:

## In-World Usage
- Who uses it:
- Who does not use it:
- Formal version:
- Folk version:
- Slang / insult / honorific:
- Taboo or sacred status:

## Reader Reveal
- First appearance handling:
- When partial meaning is clear:
- When full meaning is revealed:
- Hidden information:

## Related Terms
- Parent concept:
- Child concepts:
- Similar terms:
- Easy confusion:

## Writing Notes
- Use frequency:
- Should remain mysterious:
- Avoid over-explaining:
- Example sentence:
```

## Term Types

Common types:

- ability term
- title or rank
- faction term
- profession
- ritual
- law or institution
- historical event
- place nickname
- species/race/class category
- technology term
- slang, insult, honorific, oath, taboo word

## Reveal Strategy

Terms can create atmosphere, but too many unexplained terms cause reader fatigue. Before using a new term, decide:

- should the reader understand it immediately?
- can context explain it?
- should a character misunderstand it?
- does it need a later payoff?
- is it just flavor, or does it affect plot?

For first appearance, prefer context and consequence over dictionary explanation.

## Writing Checks

Before drafting a scene:

- Does this scene introduce a new term?
- Is the term already in `TERM_INDEX.md`?
- Is it world terminology or a translation glossary issue?
- Who in the scene knows the term?
- Does the reader need full meaning now?
- Could this term be confused with another term?

After drafting a chapter:

- add new terms
- update reveal level
- note whether future explanation is needed
- sync translation glossary only for bilingual projects or requested exports

## Translation Sync

For bilingual projects, after a world term becomes stable:

1. keep its meaning in `TERM_INDEX.md` or the term file
2. add translation handling to `TRANSLATION_GLOSSARY.md`
3. do not use translation choices to change in-world meaning

## Update Rules

- Do not rename core terms casually after they appear in prose.
- If a term changes, record the old form and affected chapters.
- Keep ability terms linked to `ability-system.md`.
- Keep faction titles linked to faction files.
- Keep names, titles, and honorifics consistent with character speech fingerprints.
