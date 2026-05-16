# Scene-First Prose Execution

Use this reference when the user asks Codex to write a scene, continue a scene, assemble a chapter from scenes, or expand a planned beat into prose.

The production order is always:

```text
scene -> chapter -> volume -> full novel
```

Blueprints, outlines, and volume plans are strong references, but they are not the unit of prose execution. Write the smallest meaningful scene first; assemble upward only after the lower layer works.

## Contents

- Inputs to Load
- Preflight Checks
- Scene Execution Passes
- Scene File Format
- Upward Assembly
- Batch Writing
- Handling Plan Drift
- Opening Options
- Ending Requirements
- Output to User
- Completion Report

## Inputs to Load

Load what exists and only what is relevant:

- `CREATIVE_BLUEPRINT.md`
- `OUTLINE.md`
- `CHAPTER_OUTLINE.md`
- `SCENE_PLAN.md`
- `CHARACTER_BIBLE.md`
- `STYLE_SETTING.json` and `CHAPTER_TEMPLATE.md`
- selected profile from `topic-guidance.md`
- current scene or previous scene ending
- `TIMELINE.md`, foreshadowing notes, glossary, or user-provided intent notes

If the requested scene has no plan, create or infer a minimal scene card and confirm before long drafting.

For long projects, manage context like the original chapter drafting workflow:

- load relevant character profiles, not necessarily the full cast bible when it is too large
- load the current scene plan and relevant outline slice, not the whole project by default
- load the previous scene ending or previous chapter final 300-600 Chinese characters for continuity
- re-read the custom style guide every time if `STYLE_SETTING.json` points to one
- consult timeline before writing scenes involving travel, injury, relationship state, knowledge state, or time gaps

## Execution Passes

### 1. Scene Fit Check

Before prose, briefly check:

- where this scene sits: volume, chapter, scene number
- scene job: what changes by the end
- POV and information boundary
- character want, pressure, and visible behavior
- conflict or uncertainty
- reader reward: cute, sweet, funny, satisfying, painful, thrilling, revealing, atmospheric, or action-focused
- rhythm: fast entry, slow emotional beat, action burst, aftermath, or transition
- foreshadowing to protect or plant
- risk: weak motivation, fake conflict, exposition dump, tonal mismatch, rushed emotion, flat ending

Keep this concise. The user needs enough context to understand the craft decision, not a lecture.

### 2. Prose Plan

State the chosen execution path:

- entry: action, suspense, character reaction, emotional contrast, image, or dialogue collision
- scene movement: goal -> obstacle -> turn -> result
- interaction focus: chemistry, rivalry, misunderstanding, care, power imbalance, secrecy, or confession pressure
- dialogue plan: subtext, misdirection, teasing, information gap, evasion, or direct confrontation
- image/sensory anchor: concrete object, gesture, sound, weather, spatial movement, light, wound, prop, or architecture
- exit: hook, reward, decision, reveal, aftertaste, or transition

When several choices are viable, offer options only if the user has not already fixed the direction. Otherwise choose and draft.

### 2.5. New Character Gate

Before a new named character receives meaningful dialogue or action:

- check whether they exist in `CHARACTER_BIBLE.md`
- if they are major/supporting, add a compact stub first
- include role, first appearance, one visual anchor, one personality anchor, provisional speech fingerprint, and relationship to the scene's core cast
- if they are minor and have no continuing function, record a one-line minor entry only

Do not give an unregistered major/supporting character a full voice before their speech fingerprint exists.

### 3. Scene Draft

Write complete usable prose for the requested scene. Follow:

- outline fidelity: dramatize the plan, do not replace it
- character fidelity: no action without believable motive
- POV discipline: no accidental head-hopping
- voice consistency: dialogue must sound character-specific
- scene effectiveness: a scene should change plot, relationship, knowledge, emotion, or state
- type fit: satisfy the selected topic profile
- pacing: slow down for high-value character, reveal, action, or emotional moments; compress low-value transitions
- foreshadowing protection: do not spend or erase planned mysteries accidentally

After drafting, run a consistency audit and fix problems before saving:

- physical details match the character bible
- dialogue matches speech fingerprints
- behavior follows personality, motive, and current pressure
- characters do not know information they have not learned
- scene result matches the planned state change
- timeline, location, injuries, relationship status, and prior scene exit are continuous
- all required outline beats for this scene are addressed

For Chinese light novel:

- include a meaningful reader reward in each chapter and ideally in many scenes
- make inner commentary useful: personality, humor, hidden information, attachment, or contrast
- daily-life details must do a job
- CP chemistry matters when relevant
- light conflict must feel subjectively important

For cinematic character-worldbuilding fiction:

- use visual anchors deliberately
- montage or flashback must change meaning
- action needs objective, readable space, reversal, cost, and aftermath
- worldbuilding appears through consequence, object, institution, ritual, architecture, or character choice

### 4. Upward Assembly

After a scene is drafted:

- save it as the scene unit
- update timeline/state
- log new characters, word count, and important knowledge-state changes
- check whether the chapter now has all required scenes
- assemble the chapter only when the scene chain is coherent
- assemble the volume only after its chapter sequence works

Do not flatten scenes too early. Scene files remain useful for revision and reordering.

## Batch Scene Writing

When writing multiple scenes:

- write sequentially, never in parallel
- run the consistency audit after every scene
- update state after every scene
- if the draft reveals a stronger direction than the plan, use Plan Drift Handling from `scene-chapter-writing.md`
- report progress by scene first, then chapter, then volume
- stop at user-defined gates or after major plan-affecting discoveries

## Scene Paths

Preferred layout:

```text
novel/draft/zh/vol01/ch01/scene01.md
novel/draft/zh/vol01/ch01/scene02.md
novel/draft/zh/vol01/ch01_zh.md
novel/draft/zh/vol01_zh.md
novel/draft/FULL_NOVEL_zh.md
```

Legacy flat layout is allowed for small projects:

```text
novel/draft/zh/ch01/scene01.md
novel/draft/zh/ch01_zh.md
```

## Openings

Choose the scene opening by function:

- action entry: movement or choice is already happening
- suspense hold: an absence, contradiction, or threat is present
- character trigger: a cute, awkward, funny, or revealing behavior appears
- emotional contrast: mood shifts from the prior scene
- atmospheric image: visual tone carries stakes
- dialogue collision: a line immediately exposes conflict or chemistry

Avoid neutral setup unless the atmosphere itself is the attraction.

## Endings

Every scene ending must do one job:

- change the situation
- suspend emotion
- create the next question
- land a reward
- reveal a new meaning
- force a decision
- leave a memorable afterimage

Do not stop because the target length is reached.

## User-Facing Output

For direct prose generation, output:

1. `场景判断`: concise scene function and risk check
2. `写法选择`: the chosen execution path
3. `正文`: complete prose
4. `说明`: 2-4 craft notes and that the draft is adjustable

This is a Codex output format, not a copied role workflow. Keep it brief when the user primarily wants prose.
