# Scene and Chapter Writing

Use this reference for drafting, continuing, revising, and assembling prose after scene cards exist. For detailed prose generation, read `chapter-prose-execution.md`. For critique and rewrite, read `chapter-revision.md`. For planning scenes before prose drafting, read `chapter-outline.md`.

## Contents

- Scene First
- Scene Plan
- Chapter Assembly
- Volume Assembly
- Writing Workflow
- Context Management
- Plan Drift
- Quality Checks
- Output Behavior

## Scene First

Treat scenes as the atomic unit. Draft upward:

```text
scene -> chapter -> volume -> full novel
```

Top-down documents still matter: blueprint, outline, and volume plan define intent and boundaries. They guide what each scene must accomplish, but production and revision happen bottom-up.

Each scene needs:

- location and time
- POV holder
- scene goal
- active conflict or uncertainty
- information change
- emotional change
- exit hook or transition

## Scene Plan

Store scene plans in `novel/settings/SCENE_PLAN.md`:

```markdown
## Vol01 / Ch03

### Scene 01
- Purpose:
- POV:
- Location/time:
- Conflict:
- Turn:
- Must include:
- Must avoid:

### Scene 02
...
```

## Drafting Order

1. Load the creative blueprint, selected topic/style guidance if any, relevant outline section, chapter outline, scene plan, character bible, style settings, timeline, and previous scene ending.
2. Confirm the scene's dramatic job against the current outline and chapter outline.
3. If generating user-facing prose, follow `chapter-prose-execution.md`: structure analysis, writing strategy, prose, creation notes.
4. Draft the scene in Chinese unless configured otherwise.
5. Run consistency checks:
   - character voice
   - known facts
   - timeline
   - scene goal fulfilled
   - no unsupported plot invention
   - no silent deviation from the current outline or chapter outline
   - scene delivers the reader reward promised by the selected topic/style profile
6. Save to `novel/draft/zh/volNN/chNN/sceneMM.md` when the project uses volumes. For small projects, `novel/draft/zh/chNN/sceneMM.md` is acceptable.
7. Update timeline and state.
8. Assemble the chapter after all intended scenes are coherent. Assemble the volume after all intended chapters are coherent.

## Chapter Assembly

When assembling `chNN_zh.md`:

- preserve scene order
- remove duplicate headings or planning notes
- smooth transitions between scenes
- keep `---` only for real scene breaks
- end with a chapter-level turn, not a random stop

## Volume Assembly

When assembling `volNN_zh.md`:

- preserve chapter order
- keep chapter headings
- check the volume has a readable opening state, escalation, climax or major payoff, and aftertaste
- ensure each chapter contributes to the volume promise
- do not let assembled chapters contradict the current outline, timeline, or character states

## Continue Mode

When the user says continue:

- read `NOVEL_STATE.json`
- identify the next unfinished scene first
- if the current chapter lacks a scene plan, create or infer one from `CHAPTER_OUTLINE.md` or `OUTLINE.md`, then confirm before long drafting
- continue from the last 300-600 Chinese characters of the previous scene/chapter

## Revision Mode

For scene or chapter revision:

- preserve canon and required events
- preserve the current outline and chapter outline unless the user explicitly instructs a plan change
- state the intended edit target briefly
- make the smallest rewrite that solves the issue
- back up existing completed chapter files before broad rewrites
- do not pad just to hit a word count

## Plan Drift Handling

If drafting reveals that the planned scene no longer works:

1. Stop and identify the mismatch.
2. Prefer a prose-level fix when possible.
3. If the better fix requires changing `OUTLINE.md`, `CHAPTER_OUTLINE.md`, or `SCENE_PLAN.md`, ask for or rely on explicit user instruction before editing the plan.
4. Summarize ripple effects on later scenes, chapter endings, character arcs, information reveals, and timeline entries.
5. After approval, update the affected plan files before continuing prose.

## Batch Mode

Write sequentially, not in parallel. Later scenes depend on earlier scene exits. Give concise progress reports after each scene or chapter.
