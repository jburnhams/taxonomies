# Taxonomies taxonomy: facets

**In one line**: three sorting questions for every rule, step, file field and decision
of the method: what part of a taxonomy it is about, in which stage of the work it
applies, and what settles whether it is met.

**In plain words**: an agent about to apply the method asks three things of a rule. Is it
about names, meanings, structure or something else? Does it apply now, while framing,
building, testing or governing? And will a script tell me if I break it, or does it take
someone's judgement, or is it Jonathan's call? Each question has a short list of answers,
and every item gets one answer to each.

**Status**: in use, 2026-11-26. Set A chosen by Jonathan; adopted after three rounds
(agreement on each facet below). Every value has an `approved` glossary entry.

## How these were found

- **Reused what exists** (step 0): the spec already groups its rules by what they
  govern (§8 Structure, Names, Definitions, Contexts; §9 Governance) and its tests by
  who or what runs them (§10 Mechanical, Judgement, In use); the process groups its
  steps by stage and names who does each. The three facets are those three groupings,
  made explicit and made to fit fields and decisions too.
- **Compared unlike items** (step 4, constant comparison) from the build sample: how is
  `b05` (step 8, agreement test) like `b42` (J6, who the raters are)? Both are about the
  evidence that a facet works, both apply in testing, but one is settled by a computed
  kappa and the other was Jonathan's decision. That pair split `part` from `check`.
- **Checked against general categories** (OBO Foundry Table 1; Colon Classification's
  PMEST): `part` is Matter (what it is about), `stage` is Time, and `check` is Energy
  (the action that settles it). No Space facet: every rule applies in every domain.
- **Independence** (S3): each pair of facets varies apart in the build sample. Naming
  rules apply in building (N2), testing (T9) and governing (N6 review); script-checked
  rules occur in every part (T1 structure, T3 naming, T4 meaning, T8 evidence);
  owner decisions occur in framing (step 0), building (step 4) and governing (G1 veto).
- **Three dimensions** (S2): fewer would make a grid. This is why the first draft's two
  facets (`kind`, `stage`) were dropped: they sorted the glossary's concepts, not the
  method's rules, and `kind` already exists as a glossary field (S4).

### Sets put to Jonathan

| Set | Facets | Why not chosen (if not) |
|---|---|---|
| **A** (chosen by Jonathan, 2026-11-26) | `part`, `stage`, `check` | |
| B | `part`, `stage`, `kind` | `kind` asks what sort of thing a rule is about; most rules are about several, and the field already sorts concepts |
| C | the draft `kind`, `stage` | two facets (a grid, S2); sorts terms, not rules |

## Bare-facet test (step 5)

The ten items `t01`-`t10` ([`samples.md`](./samples.md#bare-facet-test-10)) were sorted
by Claude with the facet names and one line per value, before any glossary entry for
them existed, 2026-11-26.

| Item | part | stage | check | Hesitation |
|---|---|---|---|---|
| `t01` spec T5 Kinds | structure | testing | script | |
| `t02` Principle field | structure | building | judgement | |
| `t03` spec C3 mappings | boundary | governing | judgement | C3 applies when `map.md` is first written, which the process puts in step 12 |
| `t04` spec N6 stable IDs | naming | building | judgement | N6 is also applied at each review (governing): first stage wins |
| `t05` step 4 Find the facets | structure | building | owner-decision | the step's text is judgement, its Who says Jonathan decides |
| `t06` Warrant field | naming | building | script | warrant is evidence for a label: naming or evidence? |
| `t07` J18 name for the system | naming | framing | owner-decision | the system's name is no domain's stage; nearest is framing |
| `t08` spec G2 anyone proposes | change | governing | judgement | |
| `t09` Readers field | purpose | framing | judgement | |
| `t10` spec N7 reticence | naming | building | judgement | T3 flags N7 from a short list: script or judgement? |

What it changed, before the glossary was written:

1. **Warrant and harvest are `naming`**, not `evidence`: they exist to choose labels
   (N2). `evidence` keeps the items, samples, rounds, raters and kappa.
2. **A partial script is `judgement`**: `script` only when a script can decide pass or
   fail without a person (T3's word list only flags N7, so N7 is `judgement`).
3. **Who decides comes from the item's own text**: a step's Who counts; "can veto" or
   "checked by Jonathan" is not `owner-decision` (an agent still settles it).
4. **First stage wins**, and a test takes the stage the spec runs it in (T1-T11
   `testing`, T12-T14 `governing`).
5. **A decision is sorted by what it settles**, not by the fact that Jonathan made it:
   every decision in `decisions.md` was his, so sorting by maker would put all of them
   in one value.

No facet was added, dropped or split.

## Chosen: part, stage, check

### Part (`part`)

- **Question**: What part of a taxonomy is it about?
- **Principle**: the part of a domain's files that would change if the item were changed or broken.
- **Kind**: property
- **Values**: `purpose`, `boundary`, `structure`, `naming`, `meaning`, `evidence`, `change`
- **Order**: as a reader meets them: why the taxonomy exists, where it ends, how it is
  arranged, what things are called, what they mean, how that is shown to work, and how it
  changes.
- **Unsorted**: none yet.
- **Agreement**: 0.94 Fleiss, 0.97 non-Claude pair; round 2, 2026-11-26, 43 fresh items, own ids removed (round 1: 1.00, 1.00).

### Stage (`stage`)

- **Question**: In which stage of the work does it first apply?
- **Principle**: the first group of process steps in which the item is applied or checked.
- **Kind**: happening
- **Values**: `framing`, `building`, `testing`, `governing`
- **Order**: the order of the process steps (0-1, 2-6, 7-9, 10-12).
- **Unsorted**: none yet.
- **Agreement**: 0.84 Fleiss, 0.90 non-Claude pair; round 2, 2026-11-26, 43 fresh items (round 1: 1.00, 1.00).

### Check (`check`)

- **Question**: What settles whether it is met?
- **Principle**: who or what has the final word on whether the item holds: a script, a person's or model's reading, or the owner.
- **Kind**: role
- **Values**: `script`, `judgement`, `owner-decision`
- **Order**: from the cheapest to the most expensive to get.
- **Unsorted**: none yet.
- **Agreement**: 0.73 Fleiss, 0.75 non-Claude pair; round 3, 2026-11-26, 73 used items, indicative (round 2: 0.55, 0.45 on 43 fresh; round 1: 0.78, 0.74 on 30 fresh).

## Retired

- **`kind`** (draft facet, 2026-11-26): the values `thing`, `property`, `role`,
  `happening` stay as glossary concepts (the Kind field's values, S4), not as a facet.
