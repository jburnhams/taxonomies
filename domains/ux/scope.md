# UX taxonomy: scope

**In one line**: the vocabulary for `jburnhams/ux-research` and the libraries built from it,
and three or four sorting questions for its tells and quality checks.

**In plain words**: ux-research catalogues the habits that make a generated interface look
generic ("tells") and the faults that make one fail ("defects"), and writes rules for
avoiding both. The same words are used loosely: "surface" means a screen in one sentence
and a coloured fill in the next; "layer" means a part of the look in one doc and a part of
the code in another. This folder fixes one word per idea and a few questions that sort
every tell and check, so the agents that write the research, the skill and strata-react
say the same thing the same way.

Built with the method in [`design/process.md`](../../design/process.md) (version 1) and the
file rules in [`design/spec.md`](../../design/spec.md).

- **Context**: [`jburnhams/ux-research`](https://github.com/jburnhams/ux-research) (the
  research, the `ux-design` skill and `slop-lint`, the `ui-library` design), and the
  vocabulary [strata-react](https://github.com/jburnhams/strata-react) inherits from it.
  Short context name: `ux`.
- **Purpose**: to name the concepts of generated-interface quality once, and sort every
  tell and quality check by the questions an agent asks when it designs, lints or
  reviews a React + Tailwind interface: what part of the interface it is about, whether
  the brief can allow it, how it is found, and on which surfaces it counts.
- **Readers**, in priority order (◆ J9, recommendation followed): Jonathan first; then
  the agents that read and write ux-research, the `ux-design` skill and strata-react.
  Where they conflict, Jonathan's reading wins.
- **Owner**: Jonathan. Agents approve changes that pass T1-T6 with a logged reason;
  Jonathan reviews [`changelog.md`](./changelog.md) and can veto any change (J8,
  [spec G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)).
- **Status**: `in use`, 2026-11-26, after round 1 met the ending conditions below
  ([results](./rounds/round-1/results.md)). Approved by Claude under G1; Jonathan can veto.

## Competency questions

The finished taxonomy must answer these from `facets.md` and `glossary.md` alone (T10).

1. Which tells can `slop-lint` find in the code, and which need the rendered page or the brief?
2. Which tells and checks count only on Operate surfaces, and which only on Persuade surfaces?
3. Is a given entry slop (the brief may allow it, with a reason) or a defect (never allowed)?
4. Which part of the interface (colour, type, layout, a component, motion, copy, imagery,
   interaction) does a tell or check concern?
5. What does "surface" mean in a given sentence, and which word should be used for the other sense?
6. What is the difference between a tell, slop and a defect?
7. What is the difference between mood, vibe, direction and a reference sentence?
8. What do "mode" and "treatment" each decide about a screen?
9. Which wave does a tell belong to, and what does "wave" mean?
10. What is a token contract, and where does it live in a project?
11. What do "the one question" and "the one finding" refer to on an Operate screen?
12. What is a signature move, and how does it differ from a model's signature?

## Out of scope

- The research sources themselves: each source folder in ux-research keeps its own
  words (Impeccable's rule ids, avoid-ai-design's codes). The glossary records them as
  aliases where they name one of our concepts, and does not rename them.
- strata-react's component and prop names (`Button`, `variant="quiet"`): they are code
  identifiers, governed by the library. Concepts they share with this context are
  mapped, not copied.
- Agent and prompt design vocabulary ("agent", "skill", "harness"): the prompts context.
  "Skill" here means only the `ux-design` skill as a named thing.
- General colour science terms (OKLCH, APCA, ΔE): defined by their standards; listed
  only where ux-research gives them a local meaning.

## Neighbours

- **prompts** (`jburnhams/prompts`), not built yet. Known overlap: "surface" ("tool
  surface" there), "skill", "agent". `map.md` is written when that context exists
  (spec C3, `closeMatch` by default).

## Ending conditions

Adopt (process step 10) when all of these hold on the same round:

- T1-T6 clean.
- T7: every item in a fresh sample of 30 gets a value in every facet, or goes to
  **Unsorted** with a note, and **Unsorted** holds at most 2 items (about 7%).
- T8: κ ≥ 0.6 on every facet, two raters from two model families (J5, J6), 30 fresh items.
- T10: every competency question above is answered, with the answer written in
  [`changelog.md`](./changelog.md) on the adopting round.
- T11: the Z39.19 §11.2.2 review finds no unmarked synonym and no missing facet.
- No facet added, split or merged in the last round.

## Samples

[`samples.md`](./samples.md): build sample (53), bare-facet test (10), round-1 test (30),
held for round 2 (16). Term harvest: [`harvest.md`](./harvest.md).
