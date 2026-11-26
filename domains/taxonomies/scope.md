# Taxonomies taxonomy: scope

**In one line**: the vocabulary of the method itself (facet, rater, round, near miss,
warrant ...), and three sorting questions for every rule, step, file field and decision
of the method.

**In plain words**: the spec and process use about fifty words with a special meaning,
and they hold about a hundred rules, steps, fields and decisions. This domain gives each
word one entry, and sorts every rule by which part of a taxonomy it governs, at which
stage of the work it applies, and what settles whether it is met. So an agent about to
write a definition can find every rule about meaning, or list what only Jonathan can
settle, without reading the whole spec.

Built with the full method in [`design/process.md`](../../design/process.md) (version 1)
and the file rules in [`design/spec.md`](../../design/spec.md), at Jonathan's request
(2026-11-26: "put the taxonomies taxonomy through full process").

- **Context**: this repository's method: [`design/spec.md`](../../design/spec.md),
  [`design/process.md`](../../design/process.md), [`design/decisions.md`](../../design/decisions.md),
  and the files each domain folder holds. Short context name: `taxonomies`.
- **Purpose**: to name the method's concepts once, and to sort each of the method's
  rules, steps, file fields and decisions by the questions an agent asks before it
  applies one: what part of a taxonomy it is about, when in the work it applies, and
  what settles whether it has been met.
- **Readers**, in priority order (◆ J9, recommendation followed): Jonathan first; then
  the agents that build and check domains with the method. Where they conflict,
  Jonathan's reading wins.
- **Owner**: Jonathan. Agents approve changes that pass T1-T6 with a logged reason; he
  can veto any change ([spec G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)).
- **Status**: `draft`, 2026-11-26. Building (steps 0 to 6 done: [`harvest.md`](./harvest.md),
  [`facets.md`](./facets.md) set A, [`glossary.md`](./glossary.md)); round 1 kit ready in
  [`rounds/round-1/`](./rounds/round-1/README.md), raters not yet run.

## Items

An item is one unit of the method that a reader or an agent looks up and applies:

- a rule of `design/spec.md` (S1 to S6, N1 to N8, D1 to D5, C1 to C3, G1 to G7, T1 to T14);
- a step of `design/process.md` (0 to 12);
- a field of a domain file (`scope.md`, `facets.md`, `glossary.md`; spec §§2-4);
- a decision of `design/decisions.md` (J1 to J19).

106 items, drawn by [`sample.py`](./sample.py) into [`samples.md`](./samples.md). The
source-check proposals are left out: each became a decision (J9 to J15).

## Competency questions

The finished taxonomy must answer these from `facets.md` and `glossary.md` alone (T10).

1. Which rules can a script check, and which need a rater's or reviewer's judgement?
2. Which rules and decisions are Jonathan's to settle, not an agent's?
3. Which rules apply while writing a definition, and which while choosing a label?
4. Which rules and steps apply before any word is collected (framing)?
5. Which rules govern changes after a taxonomy is adopted?
6. What does a domain folder hold, and what is each file for?
7. What is the difference between a term, a label and an identifier?
8. What is a facet, and how does a facet value differ from an alias?
9. What is a round, who takes part, and what does it produce?
10. What does kappa measure, and what is the target?
11. When is a taxonomy adopted?
12. What is a near miss, and how does it differ from a scope note?

## Out of scope

The research vocabulary of the topic docs (prototype, basic level, family resemblance,
ontology as a field): words *about* classification, cited from sources, not words the
method uses to run. The rules of a single domain (the ux rater rules, for example) belong
to that domain.

## Neighbours

Every other domain uses this vocabulary in its own files. `method-v1.1.md` (on the
prompts branch, not merged) proposes rules M1 to M7; they join the items when merged.

## Ending conditions

The full version (spec §10):

| Test | Target |
|---|---|
| T1-T6 | `python3 tools/check_domain.py domains/taxonomies` clean, apart from flags listed as label choices |
| T7 | every round item placed or Unsorted; at most 2 Unsorted |
| T8 | κ ≥ 0.6 on every facet, 30 fresh items, raters from at least two model families (three planned: Claude, OpenAI, Gemini) |
| T9 | name test run on every preferred label of the facet values; wrong guesses renamed |
| T10 | the twelve questions above answered |
| T11 | no unmarked synonym, no missing facet |
| Stability | no facet added, split or merged in the last round |
