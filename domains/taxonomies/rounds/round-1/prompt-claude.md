# Rater prompt: taxonomies taxonomy, round 1

You are classifying 30 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one unit of a written method for agreeing a taxonomy (a controlled vocabulary with facets) for one area of work: a rule, a process step, a file field or a recorded decision. The repo's owner is Jonathan.

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify what the item itself says. An item is a rule of the method's spec (ids S, N, D, C, G, T), a step of its process (with who does it), a field of one of a domain's files (`scope.md`, `facets.md`, `glossary.md`), or a decision the owner recorded (ids J). The `from` column is part of the item.
- part: the part of a domain's files that would change if the item were changed or broken. Words and their counts (harvest, warrant) are `naming`; items, samples, rounds, raters and kappa are `evidence`; how contexts meet is `boundary`; what the domain is for and when it is finished is `purpose`.
- stage: the first group of process steps in which the item is applied or checked: `framing` steps 0-1, `building` steps 2-6, `testing` steps 7-9, `governing` steps 10-12. A validation test T1 to T11 is `testing`; T12 to T14 are `governing`. A field takes the stage of the step that first fills it. If an item applies in several stages, the first wins.
- check: who or what has the final word on whether the item holds. `script` only when a program can decide pass or fail on its own (a count, a format, a computed kappa); a script that only flags for a person is `judgement`. `owner-decision` only when the item's own text gives the final word to Jonathan or the owner; "can veto" or "checked by Jonathan" leaves it to whoever approves, so `judgement`.
- A decision (J) is sorted by what it settles, on all three questions, not by the fact that the owner made it.
- If an item names several things, classify the first; if no value fits, pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,part,stage,check,note
```

## The questions and their values

- **part**: What part of a taxonomy is it about? Values: `boundary`, `purpose`, `structure`, `evidence`, `change`, `meaning`, `naming`
- **stage**: In which stage of the work does it first apply? Values: `framing`, `governing`, `testing`, `building`
- **check**: What settles whether it is met? Values: `judgement`, `script`, `owner-decision`

## Definitions of the values

### naming (`naming`)

- **Definition**: Naming is a part of a taxonomy that covers the words for its concepts: labels, aliases, hidden labels and identifiers.
- **Scope**: Includes the rules N1-N8, the label test (T2), name form (T3), the name test (T9), and the harvest and warrant that choose a label (N2). Excludes what the word means (`meaning`).
- **Aliases**: names
- **Near miss**: Warrant: it is counted evidence, but it exists to choose a label, so `naming`, not `evidence`.
- **Kind**: property
- **Facet**: `part`

### script (`script`)

- **Definition**: A script is a check in which a program decides from the files whether an item holds.
- **Scope**: Includes counts, uniqueness, presence of fields, formats and computed figures: the mechanical tests T1-T6, kappa against its target (T8's pass), sample sizes, and the in-use counts (T12, T13). A program must be able to decide pass or fail without anyone reading for sense. Excludes a script that only flags candidates for a person to decide (`judgement`).
- **Near miss**: N7, no evaluative words: T3 flags words from a short list, but a person decides, so `judgement`.
- **Kind**: role
- **Facet**: `check`

### building (`building`)

- **Definition**: Building is a stage of the method that collects samples and words and drafts the facets and glossary.
- **Scope**: Process steps 2 to 6: samples, harvest, facets, the bare-facet test, names and definitions. Includes the rules applied while drafting (S, N and D rules) and the `facets.md` and `glossary.md` fields, which step 4 or 6 first fills.
- **Near miss**: Testing: building may read the build sample; testing may not.
- **Kind**: happening
- **Facet**: `stage`

### testing (`testing`)

- **Definition**: Testing is a stage of the method that sorts fresh items, scores agreement and tries the names on fresh readers.
- **Scope**: Process steps 7 to 9, repeated by round. Includes every validation test from T1 to T11 (the spec runs the mechanical ones after each round, step 7), the Agreement and Unsorted fields, and rater rules.
- **Near miss**: A rule a test checks, such as N7 checked by T3: the rule first applies when a label is chosen, so `building`; the test is `testing`.
- **Kind**: happening
- **Facet**: `stage`

### meaning (`meaning`)

- **Definition**: Meaning is a part of a taxonomy that covers what each term is: its definition, scope note, example and near miss.
- **Scope**: Includes the rules D1-D5 and the definition form test (T4). Excludes the term's label (`naming`) and its place among other terms (`structure`).
- **Aliases**: definitions
- **Near miss**: The Kind field: D5 asks for it, but it places the term among kinds (S4), so `structure`.
- **Kind**: property
- **Facet**: `part`

### evidence (`evidence`)

- **Definition**: Evidence is a part of a taxonomy that covers the items it is tried on and the results of trying it.
- **Scope**: Includes samples, build and test items, rounds, raters and their answers, kappa and the agreement test (T8), the Agreement field, and sample sizes (J7). Excludes counts of words (`naming`).
- **Near miss**: A competency question: it is asked of the finished taxonomy, but it states what the taxonomy is for, so `purpose`.
- **Kind**: property
- **Facet**: `part`

### judgement (`judgement`)

- **Definition**: A judgement is a check in which a person or a model reads for sense and decides whether an item holds.
- **Scope**: Includes writing and reviewing definitions, choosing facets and labels, rating items, the name test, the heuristic review and agent approval under G1, where Jonathan can veto but an agent settles it. Excludes a computed pass (`script`) and a call the text reserves for the owner (`owner-decision`).
- **Near miss**: A step "checked by Jonathan": he looks, but the step's work is settled by whoever does it, so `judgement`.
- **Kind**: role
- **Facet**: `check`

### boundary (`boundary`)

- **Definition**: A boundary is a part of a taxonomy that covers how its context meets other contexts.
- **Scope**: Includes one context per domain, `map.md` and its mappings (closeMatch and the rest), the shared kernel, and the `scope.md` fields Context and Neighbours (spec §8 Contexts, C1-C3, G7). Excludes what the domain itself covers (`purpose`).
- **Aliases**: contexts
- **Near miss**: A shared kernel change: it needs every owner's agreement, but it is about two contexts meeting, so `boundary`, with check `owner-decision`.
- **Kind**: property
- **Facet**: `part`

### governing (`governing`)

- **Definition**: Governing is a stage of the method that adopts a taxonomy and then changes it only by named operations.
- **Scope**: Process steps 10 to 12: adoption, putting into use, and maintenance. Includes the G rules, reviews, the in-use tests T12 to T14, and `map.md` (written in step 12).
- **Aliases**: governance, maintenance
- **Near miss**: Building: a change after adoption is an operation, never a redraft.
- **Kind**: happening
- **Facet**: `stage`

### owner decision (`owner-decision`)

- **Definition**: An owner decision is a check in which the item's own text gives the final word to Jonathan or a domain's owner.
- **Scope**: Includes deciding to start a domain, choosing the facets (process step 4, "Jonathan decides"), a veto, design changes, open questions left for him, and shared-kernel changes needing every owner. A decision record is sorted by what it settles, not by the fact that Jonathan made it. Excludes "can veto" and "checked by Jonathan", where an agent still settles it (`judgement`).
- **Aliases**: Jonathan's decision
- **Near miss**: G1, agents approve and Jonathan can veto: the veto is his, but what settles a change day to day is an agent's approval, so `judgement`.
- **Kind**: role
- **Facet**: `check`

### structure (`structure`)

- **Definition**: A structure is a part of a taxonomy that covers how its terms and facets are arranged.
- **Scope**: Includes facets and their values, the `facets.md` fields, broader and related links, term kinds, levels, the Unsorted list, the record grammar and integrity (spec §8 Structure, S1-S6, T1, T5-T7). Excludes the words chosen for them (`naming`).
- **Near miss**: A facet value's label: the value is structure, the word for it is `naming`.
- **Kind**: property
- **Facet**: `part`

### change (`change`)

- **Definition**: A change is a part of a taxonomy that covers how it is approved, adopted, used and altered over time.
- **Scope**: Includes the rules G1-G6, the operations, status, history, the changelog, adoption, veto, reviews, putting a glossary into use, and the in-use tests (T12-T14). Excludes changes to how contexts meet (`boundary`).
- **Near miss**: A rule about when a label should be updated (N6): a change happens, but the rule is about the label, so `naming`.
- **Kind**: property
- **Facet**: `part`

### framing (`framing`)

- **Definition**: Framing is a stage of the method that decides a domain's purpose, readers and ending conditions before any word is collected.
- **Scope**: Process steps 0 and 1; produces `scope.md`. Includes every `scope.md` field and the decisions they settle.
- **Near miss**: Building: it starts once the frame is written.
- **Kind**: happening
- **Facet**: `stage`

### purpose (`purpose`)

- **Definition**: A purpose is a part of a taxonomy that says what it is for, who reads it, what it must answer and when it is finished.
- **Scope**: Includes the `scope.md` fields Purpose, Readers, Owner, Competency questions, Out of scope and Ending conditions, process steps 0 and 1, and the competency-question test (T10). Excludes the edges between this context and others (`boundary`).
- **Near miss**: Out of scope: it marks the edge of the domain's own subject, so `purpose`; a link to a neighbouring context is `boundary`.
- **Kind**: property
- **Facet**: `part`

## Items

```csv
id,item,from
r01,"decision J17. Rules whose best source is not stored: Keep them marked and in force; check each when the source is fetched (Nickerson 2013, Kundisch 2022, Cohen 1960, Berlin 1992, biology codes, *A Pattern Language*)",design/decisions.md (J17)
r02,"glossary.md field. Near miss: something it looks like but is not, and why (D4)",design/spec.md (glossary.md)
r03,"spec T6. Facets. Every facet value has a glossary entry; no value is empty in the latest classification (an empty cell asks whether a concept or an axis is wrong, Kwasnik pp.",design/spec.md (T6)
r04,"process step 7. Classify fresh items, fix, repeat (who: model). Classify a fresh test sample using only `facets.md` and `glossary.md`. Note every hesitation; put items that fit no value in the facet's Unsorted list (S6).",design/process.md (step 7)
r05,"spec T8. Agreement. Two raters classify the same fresh items independently, using only `facets.md` and `glossary.md`. Compute Cohen's kappa per facet. Target: κ ≥ 0.6 on every facet (J5). Disagreements show where the vocabulary is unclear (Z39.19 §11.2.2, pp.",design/spec.md (T8)
r06,"scope.md field. Neighbours: other contexts it touches, and the map file",design/spec.md (scope.md)
r07,"decision J7. Sample sizes: Build from 30-60 items, test on 30 fresh items per round; light version under ~30 items",design/decisions.md (J7)
r08,"spec T1. Integrity. Every ID unique; every record has all required fields; every referenced ID exists (""no cross-references ...",design/spec.md (T1)
r09,"glossary.md field. Scope: what it includes and excludes, especially at the edges (D2)",design/spec.md (glossary.md)
r10,"spec S5. Add a level only when it says something new. A narrower term is added ""only when there is something that we can say about this class that we cannot say about the superclass"" (Noy and McGuinness §4.4).",design/spec.md (S5)
r11,"process step 5. Test the bare facet list (who: model). Before writing any glossary entries, classify about 10 test items with the facet names and a one-line description of each value, and add, drop or split facets now.",design/process.md (step 5)
r12,decision J11. No evaluative words in names: Adopt as N7 (proposal 3),design/decisions.md (J11)
r13,"scope.md field. Purpose: one sentence: what the taxonomy is for, and the one question every facet must help answer",design/spec.md (scope.md)
r14,"spec G4. Named operations only. Every change is one of: add, rename (label changes, ID stays), split, merge, move (change broader or facet), redefine, deprecate. Each is logged in `changelog.md` and in the term's History with date and reason (Z39.19 §§11.3.1.2, 11.3.2.2, pp. 96-97).",design/spec.md (G4)
r15,"spec D4. Near miss. One thing it is easily confused with, and why it is not it: the edge of the concept, where raters disagree. TnT-LLM's raters disagreed mostly at the boundaries between neighbouring labels (Wan et al. App.",design/spec.md (D4)
r16,glossary.md field. Broader: the ID of the nearest is-a parent (S5),design/spec.md (glossary.md)
r17,"spec N2. Harvest, then choose. Collect the words already in use, with counts, before choosing. Choose the preferred label by warrant: the words in the content (literary warrant), the words of the readers (user warrant), and the owner's needs (organizational warrant) (Z39.19 §5.3.5).",design/spec.md (N2)
r18,"decision J13. Find facets by comparison, and test the bare facet list early: Adopt both as process steps 4 and 5 (proposals 1 and 2)",design/decisions.md (J13)
r19,glossary.md field. Example: a link to the clearest real case in the repo (D3),design/spec.md (glossary.md)
r20,"process step 3. Harvest the words (who: model). List every term used for the things in the build sample, and in Jonathan's own words about the domain. Count each term's uses across the repo.",design/process.md (step 3)
r21,"spec G1. Agents approve, Jonathan can veto. (J8, decided by Jonathan 2026-11-25). An agent may approve a change, or a term's move from `candidate` to `approved`, when every mechanical test (T1-T6) passes and the change is logged with its reason.",design/spec.md (G1)
r22,"spec G5. Deprecate, never delete. A deprecated term keeps its record, ID, labels and history, and its Replaced by field names the term(s) to use instead; looking up an old label finds the deprecated record, which points on.",design/spec.md (G5)
r23,"glossary.md field. Hidden: misspellings and old forms, kept for search, never shown as advice",design/spec.md (glossary.md)
r24,"decision J16. Replace ""confidence"" with a status: `candidate` / `approved` / `deprecated`",design/decisions.md (J16)
r25,"spec N1. One concept, one preferred name; one name, one concept. inside a context. Names must map to concepts one-to-one, with no homonyms and no synonyms (Deissenboeck and Pizka pp.",design/spec.md (N1)
r26,scope.md field. Competency questions: 5 to 15 questions the taxonomy must let you answer,design/spec.md (scope.md)
r27,"spec T9. Guess the name. Show someone who has not seen the glossary a preferred label and ask what it means. A wrong guess means the name or the concept needs work (Meszaros and Doble, ""Evocative Pattern Name"").",design/spec.md (T9)
r28,process step 11. Put into use (who: model). Link `domains/<name>/glossary.md` in this repo from the domain repo's `CLAUDE.md` / `AGENTS.md` (by its GitHub URL) so agents there load it and use preferred labels (J2).,design/process.md (step 11)
r29,"decision J8. Who has the final say: Agents approve, Jonathan can veto: an agent approves changes that pass T1-T6 with a logged reason; Jonathan is the named owner, reviews the changelog, can reverse anything and settles disputes",design/decisions.md (J8)
r30,"facets.md field. Agreement: the latest kappa, the date, the sample size, and who rated",design/spec.md (facets.md)
```
