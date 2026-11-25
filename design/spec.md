# Taxonomy spec

**In one line**: what a domain's taxonomy files contain, the rules their names, definitions
and structure must follow, how they change, and the tests they must pass.

**Status**: proposal, 2026-11-25. Not adopted. Where a choice is Jonathan's, it is marked
◆ and listed in [`decisions.md`](./decisions.md); the text below follows the recommended
option so the spec reads as a whole. The order of work that produces these files is in
[`process.md`](./process.md).

## How to read this

Imagine a shared notebook for one project, where every important word gets one entry:
the word to use, the other words people say for it, a one-sentence definition, a real
example, and something it could be confused with. A few short "sorting questions"
(facets) let you describe any item in the project by picking one answer to each. This
spec says what goes in that notebook, how it is written, and how to check it.

- Every rule has an ID (S1, N1, ...) and cites a **stored** source in this repo: a file
  under [`sources/`](../sources) with a page or section. Paths for each short citation
  are listed in [Sources cited](#sources-cited) at the end.
- ⚠ marks a point whose best source is **not stored yet**. It says which one and stays
  a proposal until the source is read (all are in [`to-fetch.md`](../to-fetch.md)).
- "Prior knowledge" means the claim is not in a stored source and needs checking.
- Rule IDs carry on from [`README.md`](./README.md) where the rule is the same, so the
  history is easy to follow. A table at the end maps old IDs to new.

## 1. Files and where they live

Each domain is one **bounded context** and keeps its files in a `taxonomy/` folder at the
root of its own repo (◆ J2). A bounded context is the boundary inside which one model,
and so one meaning per word, applies, and Evans names "code bases" as one such boundary
([Evans p. 2][ev]; definition [p. vi][ev]).

| File | Holds | Required |
|---|---|---|
| `taxonomy/scope.md` | purpose, readers, owner, competency questions, out of scope, neighbours, ending conditions | yes |
| `taxonomy/facets.md` | the facets and their values | yes |
| `taxonomy/glossary.md` | one entry per concept | yes |
| `taxonomy/map.md` | links to other contexts' terms and the shared kernel | once a second context exists |
| `taxonomy/changelog.md` | every change as a named operation | yes |
| `taxonomy/patterns/<id>.md` | one pattern per file (design domains only) | no |

The structure and format are fixed here, before any terms are collected, because the
format decides which relationships get recorded ([Z39.19 §11.1.2, p. 91][z39]).

**Format** (◆ J3): plain markdown with the fixed field grammar below, so people and
agents read it without tools and a script can parse it. Field names follow SKOS so the
files can be converted to RDF later if ever needed ([SKOS §§5, 7, 8, 10][skos]). Prose
definitions are the core and formal axioms are optional: even Gruber's ontologies are
names plus "human-readable text" first ([Gruber §1][gru]).

### Field grammar (all files)

- A record starts with a level-3 heading: `### <preferred label> (`<id>`)`.
- Each field is one bullet: `- **<Field>**: <value>`. Field names are exactly as in the
  tables below. Lists are comma-separated. IDs are always in backticks.
- **IDs**: lower-case ASCII words joined by hyphens (`sub-agent`); unique within the
  context; never changed, even when the label is; never reused after deprecation. A
  shared, stable identifier space is what lets old references survive change
  ([OBO Foundry, "A collaborative experiment"][obo]; [Z39.19 §11.3.2.1, p. 97][z39]).
- A term in another context is written `<context>:<id>` (for example `ux:surface`).

## 2. `scope.md`

| Field | Content | Source |
|---|---|---|
| **Context** | the repo or area this vocabulary governs, and its short context name | [Evans p. 29][ev]: "Name each bounded context" |
| **Purpose** | one sentence: what the taxonomy is for, and the one question every facet must help answer | [Denton §1][den]: "The design of the classification must follow its purpose"; [Hjørland §1][hj] |
| **Readers** | who uses the names, in priority order, and whose needs win when they conflict | [Hjørland §4.2c][hj]: a classification "can never be neutral" |
| **Owner** | the person who decides disputes and approves changes | [Z39.19 §11.3, p. 96][z39]; [OBO Foundry Table 2][obo] (named custodians) |
| **Competency questions** | 5 to 15 questions the taxonomy must let you answer | [Noy and McGuinness, Step 1][noy] |
| **Out of scope** | what this context does not cover | [OBO Foundry, "A collaborative experiment"][obo] (orthogonality) |
| **Neighbours** | other contexts it touches, and the map file | [Evans p. 29][ev] |
| **Ending conditions** | the tests in §9 with their target values | [Denton §2.3 step 7][den]; ⚠ Nickerson et al. 2013 not stored |
| **Status** | `draft`, `in use`, or `retired`, with date | [Z39.19 §11.1.6, p. 93][z39] |

## 3. `facets.md`

One record per facet:

| Field | Content |
|---|---|
| **Question** | the question this facet answers about an item ("Who starts it?") |
| **Principle** | the single characteristic of division used |
| **Kind** | `thing`, `property`, `role`, or `happening` (rule S4) |
| **Values** | the IDs of its values, in a stated order; each value has a glossary entry |
| **Order** | the order used for the values (by sequence, size, simple to complex, ...) |
| **Unsorted** | items waiting for a value, with links, and the date each arrived |
| **Agreement** | the latest kappa, the date, the sample size, and who rated |

Values are controlled vocabulary: each is a glossary term, so people are "led from their
own words to your chosen terminology" ([Denton §2.3 step 4][den]). The order field
follows Spiteri's principle of Relevant Succession ([Denton §2.2][den]).

## 4. `glossary.md`

One record per concept. Facet values, everyday domain terms and proper names (Keel,
Forge) all get entries; a proper name needs only a definition that points at the thing
it names.

| Field | Req. | SKOS property | Content and rule |
|---|---|---|---|
| heading | yes | `prefLabel` | the preferred label (rules N1-N7) and the ID |
| **Definition** | yes | `definition` | one sentence, genus-differentia (D1) |
| **Scope** | yes | `scopeNote` | what it includes and excludes, especially at the edges (D2) |
| **Aliases** | if any | `altLabel` | other names people use; each points here only (N2, N7) |
| **Hidden** | if any | `hiddenLabel` | misspellings and old forms, kept for search, never shown as advice |
| **Example** | yes | `example` | a link to the clearest real case in the repo (D3) |
| **Near miss** | yes | `scopeNote` | something it looks like but is not, and why (D4) |
| **Kind** | yes | — | `thing`, `property`, `role`, or `happening` (S4) |
| **Broader** | if any | `broader` | the ID of the nearest is-a parent (S5) |
| **Related** | if any | `related` | IDs of associated terms, never also broader (T1) |
| **Facet** | if a value | `inScheme` | the facet it is a value of |
| **Matches** | if any | mapping properties | see `map.md` (C3) |
| **Status** | yes | — | `candidate`, `approved`, or `deprecated` (G3) |
| **Warrant** | yes | — | where the term is used: files, counts, or "Jonathan's words" (N2) |
| **History** | yes | `historyNote` | dated lines: added, renamed, split, ... with the reason (G4) |

The record follows the term record of [Z39.19 §11.1.4, p. 93][z39] (term, sources
consulted, scope note, used-for references, non-displayable variants, broader, narrower,
related, history note) with the SKOS names from [SKOS §5][skos] (labels) and
[§7][skos] (notes). Narrower links are not written by hand: a tool derives them from
**Broader**, which avoids the missing-reciprocal errors Z39.19 warns about
([Z39.19 §11.4.3, pp. 100-101][z39]).

Example record (illustrative, not a decision):

```markdown
### sub-agent (`sub-agent`)

- **Definition**: A sub-agent is an agent that another agent starts to do part of its task.
- **Scope**: Includes helpers started through a tool call. Excludes agents a person
  starts directly (use `agent`).
- **Aliases**: subagent, helper agent
- **Hidden**: sub agent
- **Example**: [agent-orchestration.md](../agent-orchestration.md)
- **Near miss**: a tool call, because a tool runs no model loop of its own.
- **Kind**: role
- **Broader**: `agent`
- **Status**: candidate
- **Warrant**: "sub-agent" 873, "subagent" 821, "sub agent" 2 (all `*.md`, 2026-11-25)
- **History**: 2026-11-25 added (round 1 harvest)
```

## 5. `map.md`

One line per link: `` `<this-id>` <relation> `<context>:<id>` ``, with a reason. The
relations are SKOS's mapping properties: `exactMatch`, `closeMatch`, `broadMatch`,
`narrowMatch`, `relatedMatch` ([SKOS §10][skos]). Rule C3 limits `exactMatch`.

## 6. `changelog.md`

Grouped by day under `## YYYY-MM-DD`, newest first. Each line is one operation from G4,
the IDs it touched, and the reason:

```markdown
## 2026-11-25
- **split** `tool-surface` into `tool-set` and `tool-schema`: six round-2 items fitted neither
- **deprecate** `playbook`, use `skill`: same concept, lower warrant (12 vs 140 uses)
```

## 7. `patterns/` (design domains only)

One file per pattern, with the five mandatory elements **name, context, problem, forces,
solution**, plus related patterns and examples when helpful ([Meszaros and Doble,
"Mandatory Elements Present" and "Optional Elements When Helpful"][md]). The name is a
noun phrase naming the result ([Meszaros and Doble, "Noun Phrase Name"][md]), follows N1
to N7, and every domain word in the pattern is a glossary term. A pattern that links to
no larger or smaller pattern is a catalogue entry, not yet part of the language
([Beck and Cunningham 1987][bc]: patterns "connect to other patterns"). Patterns carry
the same **Status** field as terms; Alexander's asterisk ratings are ⚠ not stored
(*A Pattern Language* is in [`to-fetch.md`](../to-fetch.md)).

## 8. Rules

### Structure

- **S1. Purpose first.** No facet or term without a written purpose and competency
  questions to test it against. A classification is built "according to some
  principles or conception, purpose or interest" ([Hjørland §1][hj]); a
  conceptualization is a view of the world "for some purpose" ([Gruber §1][gru]);
  competency questions are the "litmus test" of scope ([Noy and McGuinness, Step 1][noy]).
  The scope file also says whose purpose wins ([Hjørland §4.2c][hj]; ◆ J9).
- **S2. Pick the structure your knowledge supports.** One dimension: a flat list. Two:
  a paradigm (grid). Three or more independent dimensions: facets
  ([Denton §§1.1-1.2][den]; [Kwasnik pp. 33-42][kw]). A hierarchy is allowed inside a
  facet only where is-a holds strictly and the domain is known well enough: a hierarchy
  needs "relatively complete knowledge of the domain in advance" ([Kwasnik pp. 25-29][kw]).
  Real units overlap; forcing them into one tree loses the overlaps
  ([Alexander 1965][al65]).
- **S3. One principle per facet.** Each facet uses a single characteristic of division,
  and its values are mutually exclusive and jointly exhaustive for the items in scope.
  Each facet passes Spiteri's principles for the choice of facets: differentiation,
  relevance, ascertainability, permanence, homogeneity, mutual exclusivity
  ([Denton §2.2][den], quoting Spiteri 1998; the originals are Ranganathan's canons,
  [Ranganathan 1937 pp. 30-92][ran37]).
- **S4. One kind of term per facet; roles never parent kinds.** Things, properties, roles
  and happenings go in separate facets. The split follows the continuant / dependent
  continuant / occurrent grid of the OBO Foundry ([OBO Foundry Table 1][obo]). A role
  (anti-rigid: an instance can stop having it) may not be the broader term of a kind
  (rigid): "antirigid properties cannot subsume rigid properties"
  ([OntoClean §8.2][oc]).
- **S5. Add a level only when it says something new.** A narrower term is added "only
  when there is something that we can say about this class that we cannot say about the
  superclass" ([Noy and McGuinness §4.4][noy]). Siblings: between two and about a
  dozen; one child suggests a modelling problem, more than a dozen suggests a missing
  level ([Noy and McGuinness §4.2][noy]). No fixed depth limit: the first draft's "three
  levels" rested on Berlin 1992, ⚠ not stored.
- **S6. No permanent "other".** Each facet has an **Unsorted** list, reviewed every round.
  A growing one means the structure is wrong: "The sure sign of a 'premature'
  hierarchical structure is the need for a 'miscellaneous' or 'other' category"
  ([Kwasnik pp. 28-29][kw]); "If too many things are filed under 'Other,' ...
  re-examine the classification and see if it needs rearrangement or a new facet"
  ([Denton §2.5][den]). Catch-all values ("other", "misc", "unknown") are not allowed
  ([Schober Table 1, 2.5][sch]).

### Names

- **N1. One concept, one preferred name; one name, one concept** inside a context.
  Names must map to concepts one-to-one, with no homonyms and no synonyms
  ([Deissenboeck and Pizka pp. 267-268][dp]); one `prefLabel` per concept
  ([SKOS §5.4, S14][skos]); the three label types are pairwise disjoint
  ([SKOS §5.4, S13][skos]); one meaning per name ([Schober Table 1, 2.1][sch]).
- **N2. Harvest, then choose.** Collect the words already in use, with counts, before
  choosing. Choose the preferred label by warrant: the words in the content (literary
  warrant), the words of the readers (user warrant), and the owner's needs
  (organizational warrant) ([Z39.19 §5.3.5][z39]). Every other word becomes an alias,
  so readers are led from their words to the chosen one ([Denton §2.3 step 4][den]).
  Agreement does not happen by itself: two developers pick the same name for the same
  thing with median probability 6.9% ([Feitelson et al. §III][fe]).
- **N3. Concepts before words.** First decide what the name must carry, then the words,
  then the name ([Feitelson et al. §§IV-V][fe]: names built this way were judged better
  two-to-one). Keep the three planes apart: what the categories are, what they are
  called, how they are numbered ([Denton §2.2][den], quoting Spiteri on Ranganathan).
  A name can only be judged concise against an agreed concept list
  ([Deissenboeck and Pizka pp. 268-269][dp]), so the definition is written with the name.
- **N4. Form.** A noun or noun phrase ([Z39.19 §6.4][z39]); singular ([Schober Table 1,
  2.3][sch]; allowed by [Z39.19 §6.5.1.1][z39]; one choice used consistently,
  [Noy and McGuinness §6.2][noy]; ◆ J4); lower-case unless a proper noun or acronym
  ([Schober Table 1, 4.1][sch]); spaces between words ([Schober 3.3][sch]); full words
  ([Schober 3.4][sch]; full words gave 19% faster comprehension than abbreviations or
  letters, [Hofmeister et al., abstract][hof]); no articles ([Schober 1.1][sch]); no
  "and" or "or" ([Schober 2.2][sch]); no negation ([Schober 2.4][sch]); no "type",
  "class", "kind" or similar claims ([Schober 1.3][sch]); no status, version or date
  ([Schober 1.4][sch]); no level or position encoded in the name.
- **N5. Basic level for the readers.** Prefer the word the readers reach for first.
  Basic-level categories are "the most codable, most coded, and most necessary in
  language" ([Rosch et al. 1976, abstract and Part II][ro]); which level is basic
  depends on the readers ([Rosch et al. pp. 392-393][ro]). Experts may want a finer
  level, but this is Rosch's hypothesis, not a finding ([p. 393][ro]).
- **N6. Stable IDs, current labels.** The ID never changes. The label follows current
  usage ([Ranganathan 1937 pp. 62-72][ran37], Canon of Currency: "some arrangement by
  which the terms can be changed over to current ones"; Spiteri's Currency,
  [Denton §2.2][den]). When a label changes, the old one becomes an alias and the
  change is logged ([Z39.19 §11.3.1.2, pp. 96-97][z39]). A rename needs a reason
  stronger than taste (G4).
- **N7. Reticence.** No evaluative words in names ("legacy", "hacky", "minor", "bad",
  "proper"): terms should be "purely descriptive and not opinionative"
  ([Ranganathan 1937 pp. 62-72][ran37], Canon of Reticence). Definitions follow the same
  rule ([Seppälä et al. guideline 9.4][sep]). (Source-check proposal 3; ◆ J11.)
- **N8. Abbreviations are aliases.** The full form is preferred and each well-known
  abbreviation is an alias, unless the abbreviation is "so well established that the
  full form ... is rarely used" ([Z39.19 §6.6.3][z39]; [Schober 3.4][sch]: DNA,
  LASER). Abbreviations can be as good as words for comprehension and easier to recall
  ([Lawrie et al. 2007, abstract][law]), so they are kept as aliases rather than
  banned. (Source-check proposal 4; ◆ J12.)

### Definitions

- **D1. Genus-differentia.** "A <term> is a <genus> that <differentia>." One genus, the
  nearest one; no categorizer words; no "and" or "or" in the genus; no circularity; no
  "usually" or "generally"; no examples or lists inside the definition; no evaluative or
  indexical words ([Seppälä et al. guidelines 3, 3.1.1, 3.1.3, 3.1.4, 5.3, 7, 9.1, 9.2,
  9.3, 9.4][sep]). The genus is the **Broader** term where there is one ([OBO Foundry,
  "Models of good practice"][obo]: "where B is the 'is_a' parent of A"; the same form in
  WordNet, [Miller p. 40][wn]). Definitions in one glossary share one structure
  ([Seppälä 1.1][sep]).
- **D2. Scope note.** Say what is included and excluded and how the term differs from
  near neighbours; a scope note should "state the chosen meaning of a term" and can name
  meanings deliberately excluded ([Z39.19 §6.2.2][z39]).
- **D3. Example.** A link to the clearest real case in the repo, kept out of the
  definition and in its own field ([Seppälä 9.2][sep]; `skos:example`,
  [SKOS §7][skos]). Using the example as the term's fixed anchor when a definition is
  revised (biology's type specimens) is ⚠ not stored (the nomenclature codes are in
  [`to-fetch.md`](../to-fetch.md)).
- **D4. Near miss.** One thing it is easily confused with, and why it is not it: the
  edge of the concept, where raters disagree. TnT-LLM's raters disagreed mostly at the
  boundaries between neighbouring labels ([Wan et al. App. B.2.1][wan]); scope notes
  exist to "distinguish between terms that have overlapping meanings"
  ([Z39.19 §6.2.2][z39]).
- **D5. Kind and rigidity.** Each term states its **Kind**. A role (sub-agent, reviewer)
  or a phase (draft, released) is never the broader term of a kind, and "can be a" is
  not "is a": OntoClean's own example wrongly puts *Agent* above *Animal*; "animals can
  be agents" ([OntoClean §8.3][oc]). Material something is made of is not its
  genus (constitution, [OntoClean §8.3][oc]).

### Contexts

- **C1. One glossary per bounded context.** Inside a context, one meaning per word;
  across contexts the same word may mean different things if the map says so
  ([Evans pp. 2-4][ev]). No term appears as a preferred label in two contexts unless
  mapped ([OBO Foundry, "A collaborative experiment"][obo]: "orthogonal").
- **C2. Small shared kernel.** Terms that are truly the same across contexts go in a
  shared kernel: "Keep this kernel small", and it "shouldn't be changed without
  consultation" ([Evans p. 31][ev]). A kernel term is a boundary object: "plastic enough
  to adapt to local needs ... yet robust enough to maintain a common identity"
  ([Star and Griesemer p. 393][sg]).
- **C3. Mappings, with `closeMatch` as the default.** Links between contexts use SKOS
  mapping properties ([SKOS §10][skos]). `exactMatch` is transitive ([SKOS §10.4, S45][skos])
  and means the concepts "can be used interchangeably" ([SKOS §10.1][skos]), so a chain
  across three repos would equate the ends. Use `exactMatch` only for real identity and
  `closeMatch` otherwise. `exactMatch` may not coexist with `broadMatch` or
  `relatedMatch` on the same pair ([SKOS S46][skos]). (Source-check proposal 7; ◆ J15.)

## 9. Governance: how a taxonomy changes

- **G1. Owner.** Each context names one owner in `scope.md`, who approves every change
  and settles disputes (◆ J8: Jonathan for now). Change records note "the individual
  responsible" ([Z39.19 §11.3, p. 96][z39]); each OBO Foundry ontology has named
  custodians ([OBO Foundry Table 2][obo]). People defer to someone who "really knows
  what makes the thing the thing that it is" ([Medin and Ortony pp. 184-185][mo]), so
  give that deference a name. (Source-check proposal 5.)
- **G2. Anyone proposes, the owner decides.** Any person or agent may propose a term or a
  change, with its reason and evidence. The proposal is recorded as a `candidate`
  ([Z39.19 §§11.1.6, 11.3.1.1-11.3.1.2, pp. 93-97][z39]). An agent writing docs that
  needs a term not in the glossary adds a candidate entry rather than inventing a word.
- **G3. Status.** `candidate` (proposed, usable, not yet agreed), `approved`, or
  `deprecated` (kept for lookup, points to its replacement). Candidates are marked so
  they cannot be mistaken for agreed terms ([Z39.19 §11.1.6][z39]). This replaces the
  first draft's confidence levels (◆ J16).
- **G4. Named operations only.** Every change is one of: **add**, **rename** (label
  changes, ID stays), **split**, **merge**, **move** (change broader or facet),
  **redefine**, **deprecate**. Each is logged in `changelog.md` and in the term's
  **History** with date and reason ([Z39.19 §§11.3.1.2, 11.3.2.2, pp. 96-97][z39]).
  Merge: the kept term takes the other's relations and notes and the other becomes an
  alias ([Z39.19 §11.4.5][z39]). Split: an overused term is replaced by narrower,
  more specific terms ([Z39.19 §11.3.1.3][z39]). ⚠ The operation set in Kundisch et
  al. 2022 (read online in the first pass) is not stored; check it when fetched.
- **G5. Deprecate, never delete.** A deprecated term keeps its record, ID and history,
  says what replaces it, and its labels become hidden labels of the replacement
  ([Z39.19 §11.3.2.1a, p. 97][z39]). Delete only a term added in error and never used
  ([same][z39]).
- **G6. A rename is a model change.** Update the glossary, the aliases and every use in
  the repo in the same commit: "a change in the language is a change to the model"
  ([Evans pp. 3-4][ev]).
- **G7. Review.** Review the unsorted lists and candidates at intervals set by how fast
  terms change ([Z39.19 §11.3.1, p. 96][z39]), and at least whenever the domain is being
  actively worked on (◆ J10). Shared-kernel changes need every affected context's owner
  ([Evans p. 31][ev]).

## 10. Validation tests

Three groups: mechanical checks a script can run on every commit; judgement tests run
during building and at review; and in-use checks after adoption. The ending conditions
in `scope.md` name which tests must pass and at what level.

### Mechanical (every commit)

These are the error checks a vocabulary system "should" run ([Z39.19 §11.4.6, p. 101][z39];
cross-reference rules [§11.4.3, pp. 100-101][z39]) plus SKOS's integrity conditions.

- **T1. Integrity.** Every ID unique; every record has all required fields; every
  referenced ID exists ("no cross-references ... to unused 'dead-end' terms");
  no term related to itself; no pair both broader and related ([SKOS S27][skos];
  [Z39.19 §11.4.3][z39]); no cycles in broader, which SKOS allows but does not want
  ([SKOS §8.6.8][skos]); no `exactMatch` together with `broadMatch` or `relatedMatch`
  ([SKOS S46][skos]); aliases and deprecated terms have no relations of their own
  ([Z39.19 §11.4.3][z39], note).
- **T2. Labels.** No label (preferred, alias or hidden) used twice in the context, after
  folding case and hyphens ([SKOS S13-S14][skos]; potential duplicates,
  [Z39.19 §11.4.6][z39]).
- **T3. Name form.** Flags N4 and N7 breaches: "and"/"or", "non-"/"not", catch-alls,
  claim words ("type", "class"), plural endings, dates or status words, evaluative words
  from a short list ([Schober Table 1][sch]; [Ranganathan 1937 pp. 62-72][ran37]).
- **T4. Definition form.** Starts "A/An <label> is a"; names its genus; does not contain
  its own label after "is a" (circularity); no "usually", "generally", "e.g."
  ([Seppälä et al. guidelines 3, 7, 9.1, 9.2][sep]). The genus matches the **Broader**
  term where one is given ([OBO Foundry][obo]).
- **T5. Kinds.** No `role` or `happening` term is the broader term of a `thing` term
  ([OntoClean §§8.2-8.3][oc]).
- **T6. Facets.** Every facet value has a glossary entry; no value is empty in the
  latest classification (an empty cell asks whether a concept or an axis is wrong,
  [Kwasnik pp. 33-39][kw]); no value has a single child or more than about a dozen
  ([Noy and McGuinness §4.2][noy]); **Unsorted** has no item older than the last review
  (S6).

### Judgement (while building, and at each review)

- **T7. Fresh-sample classification.** Classify items that were not used to build the
  taxonomy. Every item gets a value in every facet, or goes to **Unsorted** with a note
  ([Denton §2.3 steps 4, 6-7][den]: "Go back through the steps until you are able to
  classify everything").
- **T8. Agreement.** Two raters classify the same fresh items independently, using only
  `facets.md` and `glossary.md`. Compute Cohen's kappa per facet. Target: **κ ≥ 0.6 on
  every facet** (◆ J5). Disagreements show where the vocabulary is unclear
  ([Z39.19 §11.2.2, pp. 95-96][z39]: "Indexing experiments where several people index
  the same items can be very useful; disagreements can point out problems"). Evidence
  for the target: TnT-LLM reports Cohen's and Fleiss' kappa and treats (0.4, 0.6] as
  moderate and above 0.6 as substantial; expert human annotators reached above 0.6 on a
  25-label domain taxonomy and 0.553 on a 10-label intent taxonomy ([Wan et al. §5.3.2,
  Table 2][wan]). The first draft's 0.7 is above what these experts reached; 0.6 is
  "substantial" on that scale. ⚠ Cohen 1960 and the Landis and Koch bands are not
  stored; the formula κ = (p_o − p_e) / (1 − p_e) is prior knowledge.
  Rater rules:
  - One value per facet per item. GPT-4 agreed with the human majority better than the
    humans agreed with each other on single labels, but was "more liberal than humans"
    when allowed several labels ([Wan et al. §§5.2.3, 5.3.2][wan]).
  - Shuffle the order of the values for a model rater; LLM raters showed position bias
    ([Wan et al. §5.2.2][wan]).
  - At least one rater is Jonathan or a different model family (◆ J6). Two sessions of
    the same model may share blind spots; this is reasoning, not a stored finding.
  - Sample: at least 30 items per test, with every value used at least once
    (◆ J7; prior knowledge: kappa on few items has a wide margin of error).
- **T9. Guess the name.** Show someone who has not seen the glossary a preferred label
  and ask what it means. A wrong guess means the name or the concept needs work
  ([Meszaros and Doble, "Evocative Pattern Name"][md]). Look up candidate labels in
  WordNet: many senses in plain English is a homonym risk ([Miller p. 39][wn]: about
  17% of WordNet's words are polysemous).
- **T10. Competency questions.** Each question in `scope.md` can be answered using the
  facets and glossary ([Noy and McGuinness, Step 1 and §4][noy]).
- **T11. Heuristic review.** At the end of a build round, check the evaluation questions
  of [Z39.19 §11.2.2][z39]: unmarked synonyms, missing facets, out-of-date terms,
  consistent term form, quality of definitions and scope notes.

### In use (after adoption)

- **T12. Alias drift.** Count aliases and deprecated labels used in new docs in place of
  the preferred label; agents and people should use one language "in diagrams, writing,
  and especially speech" ([Evans pp. 3-4][ev]). A rising count means the preferred name
  is losing: review it under N6.
- **T13. New words.** Count new terms that appear in the repo without a glossary entry,
  and items that went to **Unsorted**. Machine-assisted candidate finding and frequency
  counts are standard ([Z39.19 §11.1.3.4][z39]).
- **T14. Does it change the work?** After a month of use, ask whether the names are used
  and whether the repo reads more consistently. A catalogue alone did not change what got
  built for Alexander; the process did ([Gabriel pp. 57-60][gab96]). ⚠ Kundisch et al.'s
  ex post evaluation is not stored.

## Old rule IDs

| Old ([`README.md`](./README.md)) | New |
|---|---|
| S1-S4, S6 | same |
| S5 (shallow, at most three levels) | S5 rewritten: Noy's sibling and new-level rules; no depth cap |
| N1-N6 | same; N4 now singular (J4); N6 now "stable IDs, current labels" |
| — | N7 Reticence, N8 abbreviations (source-check proposals 3, 4) |
| D1-D4 | same; D4 now cites boundary disagreements |
| D5 Confidence | replaced by G3 Status (Z39.19 candidate terms) |
| — | D5 Kind and rigidity (OntoClean; was part of S4) |
| C1-C3 | same; C3 defaults to `closeMatch` (proposal 7) |
| M1, M2 | G4, G6 |
| — | G1-G3, G5, G7 governance; T1-T14 tests |

## Sources cited

Every path is relative to this file. Page numbers are the printed pages of the stored
copy; section numbers are the source's own.

| Key | Source | Stored file |
|---|---|---|
| al65 | Alexander 1965, "A City is Not a Tree" | [`alexander-1965-city-is-not-a-tree.html`][al65] |
| bc | Beck and Cunningham 1987 | [`beck-cunningham-1987-oopsla.html`][bc] |
| den | Denton 2003, faceted how-to | [`denton-2003-faceted-howto.html`][den] |
| dp | Deissenboeck and Pizka 2006 | [`deissenboeck-pizka-2006-sqj.pdf`][dp] |
| ev | Evans 2015, *DDD Reference* | [`evans-2015-ddd-reference.pdf`][ev] |
| fe | Feitelson et al. 2021 | [`feitelson-2021-how-developers-choose-names.pdf`][fe] |
| gab96 | Gabriel 1996, *Patterns of Software* | [`gabriel-1996-patterns-of-software.pdf`][gab96] |
| gru | Gruber 1993 | [`gruber-1993-ksl-92-71.pdf`][gru] |
| hj | Hjørland, IEKO "Classification" | [`ieko-classification.html`][hj] |
| hof | Hofmeister et al. 2017 | [`hofmeister-2017-shorter-names.pdf`][hof] |
| kw | Kwasnik 1999 | [`kwasnik-1999-classification-structures.pdf`][kw] |
| law | Lawrie et al. 2007 | [`lawrie-2007-effective-identifier-names.pdf`][law] |
| md | Meszaros and Doble 1997 | [`meszaros-doble-1997-pattern-writing.pdf`][md] |
| mo | Medin and Ortony 1989 | [`medin-ortony-1989-psychological-essentialism.pdf`][mo] |
| noy | Noy and McGuinness 2001 | [`noy-mcguinness-2001-ontology-101.html`][noy] |
| obo | Smith et al. 2007, OBO Foundry | [`smith-2007-obo-foundry.html`][obo] |
| oc | Guarino and Welty 2004, OntoClean | [`guarino-welty-2004-overview-of-ontoclean.pdf`][oc] |
| ran37 | Ranganathan 1937, *Prolegomena* | [`ranganathan-1937-prolegomena.pdf`][ran37] |
| ro | Rosch et al. 1976 | [`rosch-1976-basic-objects.pdf`][ro] |
| sch | Schober et al. 2009 | [`schober-2009-obo-naming-conventions.html`][sch] |
| sep | Seppälä et al. 2017 | [`seppala-2017-definitions.pdf`][sep] |
| sg | Star and Griesemer 1989 | [`star-griesemer-1989-boundary-objects.pdf`][sg] |
| skos | SKOS Reference 2009 | [`skos-reference-2009.html`][skos] |
| wan | Wan et al. 2024, TnT-LLM | [`wan-2024-tnt-llm.pdf`][wan] |
| wn | Miller 1995, WordNet | [`miller-1995-wordnet.pdf`][wn] |
| z39 | ANSI/NISO Z39.19-2005 (R2010) | [`ansi-niso-z39-19-2005-r2010.pdf`][z39] |

[al65]: ../sources/alexander-1965-city-is-not-a-tree/alexander-1965-city-is-not-a-tree.html
[bc]: ../sources/gamma-1994-design-patterns/beck-cunningham-1987-oopsla.html
[den]: ../sources/denton-2003-faceted-howto/denton-2003-faceted-howto.html
[dp]: ../sources/deissenboeck-pizka-2006-concise-consistent-naming/deissenboeck-pizka-2006-sqj.pdf
[ev]: ../sources/evans-2003-domain-driven-design/evans-2015-ddd-reference.pdf
[fe]: ../sources/feitelson-2021-how-developers-choose-names/feitelson-2021-how-developers-choose-names.pdf
[gab96]: ../sources/gabriel-1996-patterns-of-software/gabriel-1996-patterns-of-software.pdf
[gru]: ../sources/gruber-1993-ontology-definition/gruber-1993-ksl-92-71.pdf
[hj]: ../sources/hjorland-2017-classification/ieko-classification.html
[hof]: ../sources/hofmeister-2017-shorter-names/hofmeister-2017-shorter-names.pdf
[kw]: ../sources/kwasnik-1999-classification-structures/kwasnik-1999-classification-structures.pdf
[law]: ../sources/lawrie-2006-whats-in-a-name/lawrie-2007-effective-identifier-names.pdf
[md]: ../sources/meszaros-doble-1997-pattern-writing/meszaros-doble-1997-pattern-writing.pdf
[mo]: ../sources/medin-ortony-1989-psychological-essentialism/medin-ortony-1989-psychological-essentialism.pdf
[noy]: ../sources/noy-mcguinness-2001-ontology-101/noy-mcguinness-2001-ontology-101.html
[obo]: ../sources/arp-smith-spear-2015-bfo/smith-2007-obo-foundry.html
[oc]: ../sources/guarino-welty-ontoclean/guarino-welty-2004-overview-of-ontoclean.pdf
[ran37]: ../sources/ranganathan-prolegomena/ranganathan-1937-prolegomena.pdf
[ro]: ../sources/rosch-1976-basic-objects/rosch-1976-basic-objects.pdf
[sch]: ../sources/schober-2009-obo-naming-conventions/schober-2009-obo-naming-conventions.html
[sep]: ../sources/seppala-2017-definitions/seppala-2017-definitions.pdf
[sg]: ../sources/star-griesemer-1989-boundary-objects/star-griesemer-1989-boundary-objects.pdf
[skos]: ../sources/skos-2009/skos-reference-2009.html
[wan]: ../sources/wan-2024-tnt-llm/wan-2024-tnt-llm.pdf
[wn]: ../sources/wordnet-1995/miller-1995-wordnet.pdf
[z39]: ../sources/niso-z39-19-2005/ansi-niso-z39-19-2005-r2010.pdf
