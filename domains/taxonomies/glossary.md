# Taxonomies taxonomy: glossary

**In one line**: one entry per concept the method uses, with the word to use, the other
words for it, a definition, an example and a near miss.

**In plain words**: when you write the spec, the process or a domain's files, use the
heading word of the entry. Everything here is `approved` (2026-11-26, after three rounds); new
terms come in as `candidate` (spec G3).

**Status**: in use, 2026-11-26, all `approved`. 39 concepts of the method, the 4 term
kinds, and the 14 values of facets `part`, `stage` and `check` ([`facets.md`](./facets.md)). Field rules:
[`design/spec.md` §4](../../design/spec.md#4-glossarymd). Warrant counts are whole-word,
case-insensitive matches (plurals included) over `design/*.md` and `domains/ux/` on
2026-11-26.

## Label choices for Jonathan's veto (J8)

1. **`alias`** rather than "alternative label" (SKOS's word): alias has 115 uses, the
   SKOS word none, and the glossary field is already called Aliases. T3 flags "alias" as
   a possible plural; it is singular.
2. **`owner-decision`** rather than "Jonathan's decision" (his name has 110 uses): a
   domain may have another owner (spec §2), and the value must hold for all of them.
3. **`governing`** for steps 10 to 12, to match framing, building and testing, although
   "governance" (the spec's §9 heading) has more uses; governance is an alias.
4. **`definition`**, **`scope note`** and **`near miss`** are entries even though they
   are also field names, because the method's rules (D1-D4) are about them.
5. **`naming`**, **`meaning`** and **`change`** for the parts the spec heads Names,
   Definitions and Governance: the heading words name the rules, these name the part of a
   taxonomy the rules govern, and "definitions" reads as the `definition` entry's plural.
   "names" and "definitions" are aliases; "governance" stays an alias of `governing`
   only (T2), so `change` has none.
6. **`neighbours`** (ID `boundary`) for how a context meets others, after the name test:
   all three fresh readers took "boundary" to mean the domain's own scope. "Neighbours"
   is the `scope.md` field it covers. T3 flags it as a possible plural; it is a mass
   noun here, like "contents".

## Entries

### taxonomy (`taxonomy`)

- **Definition**: A taxonomy is a vocabulary of agreed terms and facets for one bounded context.
- **Scope**: Here, the files in one `domains/<name>/` folder: scope, facets, glossary, changelog and rounds. Includes the terms and the sorting questions; excludes the pattern layer, which is optional.
- **Aliases**: classification scheme, controlled vocabulary
- **Example**: [spec §1](../../design/spec.md#1-files-and-where-they-live)
- **Near miss**: An ontology: it adds formal rules a machine can reason with, which none of these domains has needed.
- **Kind**: thing
- **Related**: `glossary`, `facet`, `bounded-context`
- **Status**: approved
- **Warrant**: "taxonomy" 38, "controlled vocabulary" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### bounded context (`bounded-context`)

- **Definition**: A bounded context is a boundary inside which each word has one meaning.
- **Scope**: One per domain folder (J2). A word may mean something else in another context; `map.md` links the two.
- **Aliases**: context
- **Example**: [spec §1](../../design/spec.md#1-files-and-where-they-live)
- **Near miss**: A repository: one repository can hold several contexts, and here a context's files live outside the repository its words govern.
- **Kind**: thing
- **Related**: `domain`, `shared-kernel`
- **Status**: approved
- **Warrant**: "bounded context" 9, "context" 55 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### domain (`domain`)

- **Definition**: A domain is an area of Jonathan's work that gets its own taxonomy.
- **Scope**: Named by its folder under `domains/` (`ux`, `prompts`, `taxonomies`). Each domain is one bounded context.
- **Example**: [the ux domain](../ux/scope.md)
- **Near miss**: The domain's repository (`jburnhams/ux-research`): it links to the domain folder but does not hold it.
- **Kind**: thing
- **Related**: `bounded-context`
- **Status**: approved
- **Warrant**: "domain" 73 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### owner (`owner`)

- **Definition**: An owner is a role of the person who settles disputes about a taxonomy and can veto any change to it.
- **Scope**: Named in `scope.md`; Jonathan for every domain so far (G1). Agents approve changes that pass T1-T6; the owner reviews the changelog.
- **Example**: [spec §9, G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: An approving agent: it approves a change under G1 but cannot overrule the owner.
- **Kind**: role
- **Related**: `veto`
- **Status**: approved
- **Warrant**: "owner" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### competency question (`competency-question`)

- **Definition**: A competency question is a question that a finished taxonomy must let a reader answer from its facets and glossary alone.
- **Scope**: Five to fifteen, listed in `scope.md`; T10 checks them at the end of a round.
- **Example**: [spec §2](../../design/spec.md#2-scopemd)
- **Near miss**: A facet's question: asked of each item, where a competency question is asked of the whole taxonomy.
- **Kind**: thing
- **Related**: `ending-condition`
- **Status**: approved
- **Warrant**: "competency question" 18 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### ending condition (`ending-condition`)

- **Definition**: An ending condition is a test result that must hold before a taxonomy is adopted.
- **Scope**: Listed in `scope.md` with target values: T1-T7, κ ≥ 0.6 per facet (T8), T10, T11, and no facet changed in the last round.
- **Example**: [ux round 1, ending conditions](../ux/rounds/round-1/results.md#ending-conditions-scopemd)
- **Near miss**: A mechanical check: one input to the ending conditions, run on every commit.
- **Kind**: thing
- **Related**: `adoption`, `competency-question`
- **Status**: approved
- **Warrant**: "ending condition" 58 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### item (`item`)

- **Definition**: An item is a piece of a domain's own material that the facets must sort.
- **Scope**: A row of a catalogue, a section of a doc, a rule. Items keep their IDs (`b01`, `r13`) when they move between samples.
- **Example**: [ux samples](../ux/samples.md)
- **Near miss**: A term: a term names a concept; an item is a case the terms are used to sort.
- **Kind**: thing
- **Related**: `sample`
- **Status**: approved
- **Warrant**: "item" 166 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### sample (`sample`)

- **Definition**: A sample is a set of items drawn from a domain before any of them is classified.
- **Scope**: Fixed in `samples.md` (process step 2) so that test items stay fresh. Sizes follow J7: 30 to 60 to build, 30 fresh per round.
- **Example**: [process step 2](../../design/process.md#step-2-collect-the-samples)
- **Near miss**: The domain's whole material: a sample is chosen from it, for variety.
- **Kind**: thing
- **Related**: `item`
- **Status**: approved
- **Warrant**: "sample" 46 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### build sample (`build-sample`)

- **Definition**: A build sample is a sample that the facets and glossary are built from.
- **Scope**: Used in process steps 3 to 6. Its items may be read as often as needed.
- **Example**: [ux build sample](../ux/samples.md#build-sample-53)
- **Near miss**: A test sample: never read while building.
- **Kind**: thing
- **Broader**: `sample`
- **Status**: approved
- **Warrant**: "build sample" 14 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### test sample (`test-sample`)

- **Definition**: A test sample is a sample held back from building and used only to test the taxonomy.
- **Scope**: Given to raters in a round. Once used, its items count as seen, so the next round needs new ones.
- **Aliases**: held-out sample, fresh items
- **Example**: [ux round-1 items](../ux/rounds/round-1/items.csv)
- **Near miss**: The bare-facet items of process step 5: they test the facet list before any definition exists, and are then spent.
- **Kind**: thing
- **Broader**: `sample`
- **Related**: `round`
- **Status**: approved
- **Warrant**: "test sample" 4, "fresh items" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### harvest (`harvest`)

- **Definition**: A harvest is a count of the words a domain already uses for each concept, made before any label is chosen.
- **Scope**: Groups the words into synonym sets and flags homonyms (process step 3). Counts the domain's own docs, not its stored sources.
- **Aliases**: term harvest
- **Example**: [ux harvest](../ux/harvest.md)
- **Near miss**: Warrant: the evidence a harvest yields for one term.
- **Kind**: happening
- **Related**: `warrant`
- **Status**: approved
- **Warrant**: "harvest" 57, "term harvest" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### warrant (`warrant`)

- **Definition**: A warrant is a record of where and how often a label is used, kept as the term's evidence.
- **Scope**: Counts from the harvest, file names, or Jonathan's own words (N2). The label with the most warrant wins unless it clashes with another sense.
- **Aliases**: literary warrant
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An example: one clear case of the concept, not a count of the word.
- **Kind**: property
- **Related**: `harvest`
- **Status**: approved
- **Warrant**: "warrant" 72 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### facet (`facet`)

- **Definition**: A facet is a question that every item in a domain answers with exactly one value.
- **Scope**: Recorded in `facets.md` with its principle, values, order, unsorted list and agreement. Facets are independent: one answer does not fix another (S2).
- **Aliases**: sorting question, dimension
- **Example**: [ux facets](../ux/facets.md)
- **Near miss**: A level of a tree: a tree asks one question at each level, so an item's place depends on every question above it.
- **Kind**: thing
- **Related**: `facet-value`, `taxonomy`
- **Status**: approved
- **Warrant**: "facet" 222, "sorting question" 3, "dimension" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### facet value (`facet-value`)

- **Definition**: A facet value is a term that answers one facet's question.
- **Scope**: Every value has a glossary entry whose Facet field names its facet (T6); two to about a dozen per facet.
- **Aliases**: value
- **Example**: [spec §3](../../design/spec.md#3-facetsmd)
- **Near miss**: An alias of a value: another word for the same answer, not another answer.
- **Kind**: thing
- **Broader**: `term`
- **Related**: `facet`
- **Status**: approved
- **Warrant**: "facet value" 10, "value" 112 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### term (`term`)

- **Definition**: A term is a concept with one entry in a domain's glossary.
- **Scope**: Identified by an identifier that never changes and named by its preferred label. Includes facet values, everyday domain words and proper names.
- **Aliases**: concept, entry
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A label: one of the words for a term; a term can have several.
- **Kind**: thing
- **Related**: `label`, `glossary`
- **Status**: approved
- **Warrant**: "term" 109, "concept" 42, "entry" 23 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### glossary (`glossary`)

- **Definition**: A glossary is a file that holds one entry per term of a domain.
- **Scope**: `glossary.md`, with the fields of spec §4, named after SKOS so it could become RDF.
- **Example**: [ux glossary](../ux/glossary.md)
- **Near miss**: A dictionary of the field: a glossary records only the words this context agrees on.
- **Kind**: thing
- **Related**: `term`, `taxonomy`
- **Status**: approved
- **Warrant**: "glossary" 62 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### label (`label`)

- **Definition**: A label is a word or phrase that names a term.
- **Scope**: No label is used twice in a context, after folding case and hyphens (T2).
- **Aliases**: name
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An identifier: it never changes, while a label can be renamed.
- **Kind**: thing
- **Related**: `identifier`
- **Status**: approved
- **Warrant**: "label" 84, "name" 156 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### preferred label (`preferred-label`)

- **Definition**: A preferred label is a label that a context agrees to use for a term.
- **Scope**: The heading word of the glossary entry; chosen by warrant and the name rules N1-N7.
- **Aliases**: heading word, prefLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An alias: in use, but not the one to write.
- **Kind**: thing
- **Broader**: `label`
- **Status**: approved
- **Warrant**: "preferred label" 14, "heading word" 1, "prefLabel" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### alias (`alias`)

- **Definition**: An alias is a label that people also use for a term and that points to its preferred label.
- **Scope**: Listed in the Aliases field; each points to one term only (N1).
- **Aliases**: alternative label, altLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A hidden label: kept for search, never offered as a word to use.
- **Kind**: thing
- **Broader**: `label`
- **Status**: approved
- **Warrant**: "alias" 113, "altLabel" 1 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### hidden label (`hidden-label`)

- **Definition**: A hidden label is a label kept for search but never shown as advice.
- **Scope**: Misspellings and old forms.
- **Aliases**: hiddenLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A deprecated term: a whole record kept for lookup, where a hidden label is one string on a live record.
- **Kind**: thing
- **Broader**: `label`
- **Status**: approved
- **Warrant**: "hidden label" 1, "hiddenLabel" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### identifier (`identifier`)

- **Definition**: An identifier is a code that names a term and never changes.
- **Scope**: Lower-case words joined by hyphens, in backticks; never reused after deprecation. A term in another context is written `<context>:<id>`.
- **Aliases**: ID
- **Example**: [spec §1, field grammar](../../design/spec.md#field-grammar-all-files)
- **Near miss**: A label: what people read, and what a rename changes.
- **Kind**: thing
- **Related**: `label`
- **Status**: approved
- **Warrant**: "identifier" 3, "ID" 49 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### definition (`definition`)

- **Definition**: A definition is a sentence that says what a term is by naming its genus and what sets it apart.
- **Scope**: One sentence that starts "A <label> is a" (T4), with no hedge or example in it.
- **Aliases**: genus-differentia
- **Example**: [spec §8, Definitions](../../design/spec.md#definitions)
- **Near miss**: A scope note: it says where the edges are, not what the thing is.
- **Kind**: thing
- **Related**: `scope-note`
- **Status**: approved
- **Warrant**: "definition" 126, "genus-differentia" 9 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### scope note (`scope-note`)

- **Definition**: A scope note is a note that says what a term includes and excludes at its edges.
- **Scope**: The Scope field. Widened after a round wherever raters split on an item.
- **Aliases**: scopeNote
- **Example**: [ux round 1, fixes](../ux/rounds/round-1/results.md#fixes-after-scoring-2026-11-26)
- **Near miss**: A near miss: one named case it is not, where a scope note draws the line.
- **Kind**: thing
- **Related**: `definition`, `near-miss`
- **Status**: approved
- **Warrant**: "scope note" 28, "scopeNote" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### near miss (`near-miss`)

- **Definition**: A near miss is a note that names something a term looks like but is not, and why.
- **Scope**: One per entry (D4).
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An alias: the same concept under another word, where a near miss is a different concept.
- **Kind**: thing
- **Related**: `scope-note`
- **Status**: approved
- **Warrant**: "near miss" 99 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### operation (`operation`)

- **Definition**: An operation is a named change to a taxonomy, logged with its date and reason.
- **Scope**: One of add, rename, split, merge, move, redefine, deprecate (G4), plus adopt for a whole domain.
- **Aliases**: named operation
- **Example**: [spec §9, G4](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: An edit with no name: not allowed, because the changelog could not say what happened.
- **Kind**: happening
- **Related**: `changelog`
- **Status**: approved
- **Warrant**: "operation" 14, "named operation" 8 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### term backlog (`term-backlog`)

- **Definition**: A term backlog is a list of concepts that settled terms have opened and that no stage has defined yet.
- **Scope**: One row per concept, with the term that opened it, its warrant and the stage expected to take it (method v1.1 M8). Kept in `domains/<name>/backlog.md`.
- **Aliases**: backlog
- **Example**: [prompts backlog](../prompts/backlog.md)
- **Near miss**: Candidate terms: already drafted entries; a backlog row has no entry yet.
- **Kind**: thing
- **Related**: `harvest`
- **Status**: candidate
- **Warrant**: Jonathan, 2026-11-27 ("one decided concept opens up far more"); Z39.19 §11.3.1.1 (nominating candidate terms)
- **History**: 2026-11-27 added with method v1.1 M8 (proposed).

### revision pass (`revision-pass`)

- **Definition**: A revision pass is a happening in which a stage re-reads the earlier entries its harvest touches and records each change as an operation.
- **Scope**: Clarifications are redefinitions or new near misses; breaking changes are splits, merges, moves or deprecations (G4, G5). Changed entries go back to `candidate` and are retested in that stage (method v1.1 M8).
- **Aliases**: revision, review of earlier terms
- **Example**: [prompts stage 3 revision pass](../prompts/stage-3/revision.md)
- **Near miss**: A round's fixes: they change the entries that round tested, not earlier stages' entries.
- **Kind**: happening
- **Related**: `operation`, `term-backlog`
- **Status**: candidate
- **Warrant**: Z39.19 §11.3.1 ("periodic review of terminology"); Denton §2.3 step 7
- **History**: 2026-11-27 added with method v1.1 M8 (proposed).

### changelog (`changelog`)

- **Definition**: A changelog is a file that records every operation on a taxonomy, newest day first.
- **Scope**: `changelog.md` in the domain folder; each line names the approving agent (G1).
- **Example**: [ux changelog](../ux/changelog.md)
- **Near miss**: A term's History field: the same events, kept on each term.
- **Kind**: thing
- **Related**: `operation`
- **Status**: approved
- **Warrant**: "changelog" 25 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### status (`status`)

- **Definition**: A status is a property of a term that says whether it is proposed, agreed or replaced.
- **Scope**: `candidate` (usable, not yet agreed), `approved`, or `deprecated` with a Replaced by field (G3, G5).
- **Example**: [spec §9, G3](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: The status of a domain in `scope.md` (`draft`, `in use`, `retired`), which covers the whole taxonomy.
- **Kind**: property
- **Status**: approved
- **Warrant**: "status" 83 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### round (`round`)

- **Definition**: A round is a pass in which raters sort a fresh test sample and the files are fixed from their disagreements.
- **Scope**: Kept in `rounds/round-N/`: the items, the prompts, each rater's answers, the results and review. Steps 7 to 9 repeat by round.
- **Example**: [ux round 1](../ux/rounds/round-1/README.md)
- **Near miss**: A build pass: it reads the build sample, which a round never does.
- **Kind**: happening
- **Related**: `rater`, `agreement-test`, `test-sample`
- **Status**: approved
- **Warrant**: "round" 166 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### rater (`rater`)

- **Definition**: A rater is a role of a model or person that sorts items using only the facets and glossary.
- **Scope**: At least two model families (J6); each answers alone, with the values shuffled.
- **Aliases**: judge
- **Example**: [ux round-1 answers](../ux/rounds/round-1/answers/claude.csv)
- **Near miss**: An approving agent: it decides whether a change is accepted, not where an item goes.
- **Kind**: role
- **Related**: `round`, `kappa`
- **Status**: approved
- **Warrant**: "rater" 57, "judge" 15 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### agreement test (`agreement-test`)

- **Definition**: An agreement test is a test in which raters sort the same items independently and their answers are compared per facet.
- **Scope**: T8. Disagreements show which definitions to fix.
- **Aliases**: T8
- **Example**: [process step 8](../../design/process.md#step-8-agreement-test)
- **Near miss**: A name test: it asks what a label means, not where an item goes.
- **Kind**: happening
- **Related**: `kappa`, `round`
- **Status**: approved
- **Warrant**: "agreement test" 8, "T8" 11 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### kappa (`kappa`)

- **Definition**: Kappa is a measure of how often raters agree beyond what chance alone would give.
- **Scope**: Cohen's for two raters, Fleiss' for three or more; the target is at least 0.6 per facet (J5).
- **Aliases**: Cohen's kappa, Fleiss' kappa, κ
- **Example**: [ux round-1 results](../ux/rounds/round-1/results.md#kappa-per-facet)
- **Near miss**: Raw agreement: the share of items answered the same, which chance alone can make high.
- **Kind**: property
- **Related**: `agreement-test`
- **Status**: approved
- **Warrant**: "kappa" 23, "Cohen's kappa" 3, "Fleiss' kappa" 2, "κ" 15 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### name test (`name-test`)

- **Definition**: A name test is a test in which a fresh reader guesses what a label means before seeing its definition.
- **Scope**: T9. A wrong guess means the name or the concept needs work; WordNet senses flag homonyms.
- **Aliases**: T9, guess the name
- **Example**: [ux name test](../ux/rounds/round-1/name-test/results.md)
- **Near miss**: An agreement test: it sorts items with the definitions in hand.
- **Kind**: happening
- **Status**: approved
- **Warrant**: "name test" 9, "T9" 13, "guess the name" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### unsorted list (`unsorted-list`)

- **Definition**: An unsorted list is a list in a facet's record of items that no value fits yet.
- **Scope**: The Unsorted field, with the date each item arrived; it should be empty at each review (S6).
- **Aliases**: Unsorted
- **Example**: [ux facets, aspect](../ux/facets.md#aspect-aspect)
- **Near miss**: A disagreement: there the raters chose different values; an unsorted item has none that fits.
- **Kind**: thing
- **Related**: `facet`
- **Status**: approved
- **Warrant**: "unsorted list" 1, "Unsorted" 31 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### mechanical check (`mechanical-check`)

- **Definition**: A mechanical check is a check that a script runs on every commit.
- **Scope**: T1 to T6, in `tools/check_domain.py`.
- **Example**: [spec §10](../../design/spec.md#mechanical-every-commit)
- **Near miss**: A judgement test (T7-T11): it needs a rater or reviewer.
- **Kind**: happening
- **Status**: approved
- **Warrant**: "mechanical check" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### adoption (`adoption`)

- **Definition**: An adoption is a change that puts a whole taxonomy into use once its ending conditions hold.
- **Scope**: Terms move to `approved` and `scope.md` to `in use` (process step 10); an agent approves, Jonathan can veto.
- **Example**: [process step 10](../../design/process.md#step-10-adopt)
- **Near miss**: Approving one term: an operation on one entry, where adoption covers the domain.
- **Kind**: happening
- **Related**: `ending-condition`
- **Status**: approved
- **Warrant**: "adoption" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### veto (`veto`)

- **Definition**: A veto is a decision by the owner that reverses a change.
- **Scope**: Logged as its own operation in the changelog (G1).
- **Example**: [spec §9, G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: A deprecation: a named operation any approver may make under G1.
- **Kind**: happening
- **Related**: `owner`
- **Status**: approved
- **Warrant**: "veto" 64 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### alias drift (`alias-drift`)

- **Definition**: Alias drift is a property of a domain's writing in which aliases are used where the preferred label belongs.
- **Scope**: T12, counted in new docs after adoption. A rising count means the preferred label is losing.
- **Example**: [spec §10, in use](../../design/spec.md#in-use-after-adoption)
- **Near miss**: A new word with no entry (T13): drift is a known word used in place of the agreed one.
- **Kind**: property
- **Status**: approved
- **Warrant**: "alias drift" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### shared kernel (`shared-kernel`)

- **Definition**: A shared kernel is a set of terms that two or more contexts agree to share.
- **Scope**: Changes need every affected owner (G7).
- **Example**: [spec §9, G7](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: A map entry: it links two contexts' terms without making them one.
- **Kind**: thing
- **Related**: `bounded-context`
- **Status**: approved
- **Warrant**: "shared kernel" 8 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### pattern (`pattern`)

- **Definition**: A pattern is a record of a recurring problem in a design domain and the solution that resolves its forces.
- **Scope**: One file per pattern in `patterns/`, with name, context, problem, forces and solution (spec §7).
- **Example**: [spec §7](../../design/spec.md#7-patterns-design-domains-only)
- **Near miss**: A term: a term names a concept; a pattern names a solution and links to other patterns.
- **Kind**: thing
- **Status**: approved
- **Warrant**: "pattern" 54 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

## Term kinds

The values of every entry's Kind field (spec S4). They were the draft facet `kind`.

### thing (`thing`)

- **Definition**: A thing is a term kind for something that exists in its own right and keeps its identity over time.
- **Scope**: Files, items, samples, labels: OntoClean's rigid kinds (S4). No thing sits under a role or a happening (T5).
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A role: a part a thing plays for a while (a model is a thing; rater is one of its roles).
- **Kind**: property
- **Status**: approved
- **Warrant**: "thing" 95 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 moved (no longer a facet value: facet `kind` retired in step 4; kept as a value of the Kind field); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### property (`property`)

- **Definition**: A property is a term kind for a quality that something has.
- **Scope**: Status, kappa, warrant: each is had by a term, a round or a label.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing: it exists on its own; a property exists only in what has it.
- **Kind**: property
- **Status**: approved
- **Warrant**: "property" 50 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 moved (no longer a facet value: facet `kind` retired in step 4; kept as a value of the Kind field); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### role (`role`)

- **Definition**: A role is a term kind for a part that something plays in a relation and can stop playing.
- **Scope**: Owner, rater.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing: a model stays a model when it stops rating.
- **Kind**: property
- **Status**: approved
- **Warrant**: "role" 38 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 moved (no longer a facet value: facet `kind` retired in step 4; kept as a value of the Kind field); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### happening (`happening`)

- **Definition**: A happening is a term kind for something that takes place over time.
- **Scope**: Rounds, tests, operations, harvests.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing that records a happening: the changelog is a thing; the operation it records is a happening.
- **Kind**: property
- **Status**: approved
- **Warrant**: "happening" 12 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 moved (no longer a facet value: facet `kind` retired in step 4; kept as a value of the Kind field); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

## Facet values

Values of facets `part`, `stage` and `check` ([`facets.md`](./facets.md)).

### purpose (`purpose`)

- **Definition**: A purpose is a part of a taxonomy that says what it is for, who reads it, what it must answer and when it is finished.
- **Scope**: Includes the `scope.md` fields Purpose, Readers, Owner, Competency questions, Out of scope and Ending conditions, process steps 0 and 1, and the competency-question test (T10). Excludes the edges between this context and others (`boundary`).
- **Example**: [spec §2](../../design/spec.md#2-scopemd)
- **Near miss**: Out of scope: it marks the edge of the domain's own subject, so `purpose`; a link to a neighbouring context is `boundary`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "purpose" 25 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### neighbours (`boundary`)

- **Definition**: Neighbours is a part of a taxonomy that covers how its context meets other contexts.
- **Scope**: Includes one context per domain, `map.md` and its mappings (closeMatch and the rest), the shared kernel, and the `scope.md` fields Context and Neighbours (spec §8 Contexts, C1-C3, G7). Excludes what the domain itself covers (`purpose`).
- **Aliases**: boundary, contexts
- **Example**: [spec §8, Contexts](../../design/spec.md#contexts)
- **Near miss**: A shared kernel change: it needs every owner's agreement, but it is about two contexts meeting, so `boundary` (neighbours), with check `owner-decision`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "boundary" 12, "context" 38 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 renamed from "boundary" (name test: all three fresh readers read "boundary" as the domain's own scope, in or out); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### structure (`structure`)

- **Definition**: A structure is a part of a taxonomy that covers how its terms and facets are arranged.
- **Scope**: Includes facets and their values, the `facets.md` fields, broader and related links, term kinds, levels, the Unsorted list, the record grammar and integrity (spec §8 Structure, S1-S6, T1, T5-T7). Excludes the words chosen for them (`naming`).
- **Example**: [spec §8, Structure](../../design/spec.md#structure)
- **Near miss**: A facet value's label: the value is structure, the word for it is `naming`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "structure" 22 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### naming (`naming`)

- **Definition**: Naming is a part of a taxonomy that covers the words for its concepts: labels, aliases, hidden labels and identifiers.
- **Scope**: Includes the rules N1-N8, the label test (T2), name form (T3), the name test (T9), and the harvest and warrant that choose a label (N2). Excludes what the word means (`meaning`).
- **Aliases**: names
- **Example**: [spec §8, Names](../../design/spec.md#names)
- **Near miss**: Warrant: it is counted evidence, but it exists to choose a label, so `naming`, not `evidence`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "naming" 8, "names" (spec §8 heading) (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### meaning (`meaning`)

- **Definition**: Meaning is a part of a taxonomy that covers what each term is: its definition, scope note, example and near miss.
- **Scope**: Includes the rules D1-D5 and the definition form test (T4). Excludes the term's label (`naming`) and its place among other terms (`structure`).
- **Aliases**: definitions
- **Example**: [spec §8, Definitions](../../design/spec.md#definitions)
- **Near miss**: The Kind field: D5 asks for it, but it places the term among kinds (S4), so `structure`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "meaning" 10, "definitions" 131 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### evidence (`evidence`)

- **Definition**: Evidence is a part of a taxonomy that covers the items it is tried on and the results of trying it.
- **Scope**: Includes samples, build and test items, rounds, raters and their answers, kappa and the agreement test (T8), the Agreement field, and sample sizes (J7). Excludes counts of words (`naming`).
- **Example**: [spec T8](../../design/spec.md#judgement-while-building-and-at-each-review)
- **Near miss**: A competency question: it is asked of the finished taxonomy, but it states what the taxonomy is for, so `purpose`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "evidence" 12, "round" 191, "sample" 47 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### change (`change`)

- **Definition**: A change is a part of a taxonomy that covers how it is approved, adopted, used and altered over time.
- **Scope**: Includes the rules G1-G6, the operations, status, history, the changelog, adoption, veto, reviews, putting a glossary into use, and the in-use tests (T12-T14). Excludes changes to how contexts meet (`boundary`).
- **Example**: [spec §9](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: A rule about when a label should be updated (N6): a change happens, but the rule is about the label, so `naming`.
- **Kind**: property
- **Facet**: `part`
- **Status**: approved
- **Warrant**: "change" 41, "governance" 8 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `part`; not yet tested); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### script (`script`)

- **Definition**: A script is a check in which a program stored in this repo decides whether an item holds.
- **Scope**: Only what these scripts check today: `tools/check_domain.py` (the mechanical tests T1-T6: IDs unique, required fields present, references exist, no cycles in broader, no label used twice, name form, definition form, kinds, every facet value has an entry and a facet has 2 to 12 values), which reads `glossary.md` and `facets.md`; `tools/kappa.py` (kappa per facet against the 0.6 target, the majority label and splits: T8's pass, J23, J24); and a domain's `sample.py` (the seeded draw, J21). Excludes anything no script checks yet, even where a program could (a file present, a link in place, a count of aliases in use, T12, T13), and the rules the mechanical tests only flag for a person (N4, N7): those are `judgement`.
- **Example**: [`tools/check_domain.py`](../../tools/check_domain.py)
- **Near miss**: `scope.md` must exist (spec §1): a program could check it, but none does, so `judgement` until a script is added.
- **Kind**: role
- **Related**: `mechanical-check`
- **Facet**: `check`
- **Status**: approved
- **Warrant**: "script" 6, "mechanical" 5 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `check`; not yet tested); 2026-11-26 redefined (round 1 splits r14, r18, r22, r28); 2026-11-26 redefined (round 2: `script` is what a stored script checks today, a closed list, not what a program could check); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### judgement (`judgement`)

- **Definition**: A judgement is a check in which a person or a model reads for sense and decides whether an item holds.
- **Scope**: Includes writing and reviewing definitions, choosing facets and labels, rating items, the name test, the heuristic review and agent approval under G1, where Jonathan can veto but an agent settles it. Includes any item that no stored script checks: one with a condition that needs reading for sense, such as naming which operation a change is (G4), and one a program could check but none yet does (a file present, a link in place). Excludes what a stored script checks (`script`) and a call the text reserves for the owner (`owner-decision`).
- **Example**: [spec §10, Judgement](../../design/spec.md#judgement-while-building-and-at-each-review)
- **Near miss**: A step "checked by Jonathan": he looks, but the step's work is settled by whoever does it, so `judgement`.
- **Kind**: role
- **Facet**: `check`
- **Status**: approved
- **Warrant**: "judgement" 50 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `check`; not yet tested); 2026-11-26 redefined (round 1 splits r14, r18, r22, r28); 2026-11-26 redefined (round 2: includes what no stored script checks); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### owner decision (`owner-decision`)

- **Definition**: An owner decision is a check in which the item's own text gives the final word to Jonathan or a domain's owner.
- **Scope**: Includes deciding to start a domain, choosing the facets (process step 4, "Jonathan decides"), a veto, design changes, open questions left for him, and shared-kernel changes needing every owner. A decision record is sorted by what it settles, not by the fact that Jonathan made it. Excludes "can veto" and "checked by Jonathan", where an agent still settles it (`judgement`).
- **Aliases**: Jonathan's decision
- **Example**: [spec G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: G1, agents approve and Jonathan can veto: the veto is his, but what settles a change day to day is an agent's approval, so `judgement`. A decision that adds a step in which Jonathan decides (J13 adds step 4): the decision settles how the step is done, so it takes that work's check, not the step's Who.
- **Kind**: role
- **Facet**: `check`
- **Status**: approved
- **Warrant**: "owner" 13, "Jonathan decides" (process step table) (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (step 6, for facet `check`; not yet tested); 2026-11-26 redefined (round 1 splits r14, r18, r22, r28); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### framing (`framing`)

- **Definition**: Framing is a stage of the method that decides a domain's purpose, readers and ending conditions before any word is collected.
- **Scope**: Process steps 0 and 1; produces `scope.md`. Includes every `scope.md` field and the decisions they settle.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Building: it starts once the frame is written.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: approved
- **Warrant**: "framing" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 redefined (scope note: which items take this stage, after the bare-facet test); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### building (`building`)

- **Definition**: Building is a stage of the method that collects samples and words and drafts the facets and glossary.
- **Scope**: Process steps 2 to 6: samples, harvest, facets, the bare-facet test, names and definitions. Includes the rules applied while drafting (S, N and D rules) and the `facets.md` and `glossary.md` fields, which step 4 or 6 first fills.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Testing: building may read the build sample; testing may not.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: approved
- **Warrant**: "building" 10 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 redefined (scope note: which items take this stage, after the bare-facet test); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### testing (`testing`)

- **Definition**: Testing is a stage of the method that sorts fresh items, scores agreement and tries the names on fresh readers.
- **Scope**: Process steps 7 to 9, repeated by round. Includes every validation test from T1 to T11 (the spec runs the mechanical ones after each round, step 7), the Agreement and Unsorted fields, and rater rules.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: A rule a test checks, such as N7 checked by T3: the rule first applies when a label is chosen, so `building`; the test is `testing`.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: approved
- **Warrant**: "testing" 1 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 redefined (scope note: which items take this stage, after the bare-facet test); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)

### governing (`governing`)

- **Definition**: Governing is a stage of the method that adopts a taxonomy and then changes it only by named operations.
- **Scope**: Process steps 10 to 12: adoption, putting into use, and maintenance. Includes the G rules, reviews, the in-use tests T12 to T14, and `map.md` (written in step 12).
- **Aliases**: governance, maintenance
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Building: a change after adoption is an operation, never a redraft.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: approved
- **Warrant**: "governing" 0, "governance" 4, "maintenance" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested); 2026-11-26 redefined (scope note: which items take this stage, after the bare-facet test); 2026-11-26 approved (ending conditions met after round 3; approved by Claude, Jonathan can veto)
