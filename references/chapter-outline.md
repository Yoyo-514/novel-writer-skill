# Chapter Outline

Use this reference when turning a module/volume outline into executable scene cards and chapter groups. This is the bridge between outline and drafting, but its working direction is small-to-large: scene -> chapter -> volume.

Chapter outlines are strong references for prose drafting. They should guide scene order, scene function, information reveals, and chapter endings. They can change during writing, but only after the user clearly asks to change the plan or approves a proposed adjustment.

## Contents

- Core Unit
- Chapter Planning Workflow
- Chapter Outline Template
- Scene Card Template
- Scene -> Chapter -> Volume Checks
- Completion Standard
- Revision and Drift
- Output Behavior

## Core Unit

Use scenes as the basic unit. A chapter is a small chain of functional scenes. A volume is a chain of chapters with a larger emotional and structural payoff.

Each scene needs:

- viewpoint
- location/time
- immediate goal
- obstacle or pressure
- result / state change
- information movement
- emotional movement
- transition to the next scene

## Chapter Planning Workflow

1. Read the creative blueprint, selected topic/style guidance if any, outline, relevant module outline, character bible, style settings, and current timeline.
2. Identify the needed scenes first: what each scene changes and why it exists.
3. Group scenes into chapters only after the scene chain has a readable rise, turn, and ending interface.
4. Group chapters into the active volume only after each chapter has a clear function and cumulative payoff.
5. For each scene, clarify goal, obstacle, result, information, emotion, and connection.
6. Design chapter endings as interfaces: suspense, unresolved choice, danger, promise, emotional suspension, reveal, or reward.
7. Check consistency with the module outline and neighboring chapters.
8. Save scene cards to `novel/settings/SCENE_PLAN.md` and chapter grouping to `novel/CHAPTER_OUTLINE.md`.

## Chapter Outline Template

```markdown
## Volume NN - [Name]

### Volume Role
- Core promise:
- Opening state:
- Final state:
- Main payoff:

## ChNN - [Title]

### Chapter Position
- Function in module:
- Main reader appeal:
- Starting state:
- Ending state:

### Key Information
- New information:
- Withheld information:
- Reader knows / character knows:

### Scene Chain

#### Scene 01 - [Scene name]
- Function:
- POV:
- Location/time:
- Goal:
- Obstacle:
- Core event:
- Result / state change:
- Emotional movement:
- Information movement:
- Transition:

#### Scene 02 - [Scene name]
...

### Key Dialogue Planning
- Participants:
- Topic:
- Conflict or turn:
- Function:
- Hidden subtext:

Do not write exact dialogue during planning unless the user asks for draft prose.

### Ending Interface
- Ending beat:
- Suspense or question:
- Link to next chapter:

### Consistency Notes
- Character logic:
- Setting logic:
- Timeline:
- Risks:
```

## Micro Planning Tools

Use these internally and explain them plainly:

- Scene effectiveness: a scene should change a situation, relationship, knowledge state, or emotional state.
- Emotional variation: avoid one-note chapters; add contrast or a small turn when a chapter feels flat.
- Pacing: vary event density and information release speed.
- Dialogue function: plan what dialogue must accomplish, not exact lines.
- Information control: choose what the reader knows, what the POV character knows, and what remains hidden.
- Conflict expression: decide whether conflict appears through action, conversation, competition, rule pressure, environment, or relationship strain.
- Viewpoint: choose the POV that best controls emotion and information.
- Topic profile fit: check that the scene delivers the reader rewards promised by the selected topic/style profile.

## Option Giving

When the user is stuck, provide 1-2 concrete scene-chain options:

```markdown
[2.1] More external pressure
- Scene idea:
- Why it works:
- Risk:

[2.2] More emotional pressure
- Scene idea:
- Why it works:
- Risk:

These can be merged: for example, use [2.1]'s event pressure but keep [2.2]'s relationship turn.
```

Only treat an option as fixed after user confirmation or explicit modification.

## Revision and Ripple Check

When a chapter plan changes, check effects on:

- prior setup
- next chapter opening
- character arc
- module climax
- information reveal timing
- setting rules
- timeline

If the change affects the module core, say so and ask whether to adjust the module outline as well.

During prose drafting, do not silently alter a chapter outline to match a draft that drifted. Either bring the draft back to the plan, or enter explicit plan-revision mode with the user's approval.
