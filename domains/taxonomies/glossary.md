# Taxonomies taxonomy: glossary

**In one line**: one entry per concept the method uses, with the word to use, the other
words for it, a definition, an example and a near miss.

**In plain words**: when you write the spec, the process or a domain's files, use the
heading word of the entry. Everything here is `candidate`: drafted, not yet tested
(spec G3).

**Status**: draft, 2026-11-26, all `candidate`. 39 concepts of the method and the 8
values of facets `kind` and `stage` ([`facets.md`](./facets.md)). Field rules:
[`design/spec.md` §4](../../design/spec.md#4-glossarymd). Warrant counts are whole-word,
case-insensitive matches (plurals included) over `design/*.md` and `domains/ux/` on
2026-11-26.

## Label choices for Jonathan's veto (J8)

1. **`alias`** rather than "alternative label" (SKOS's word): alias has 113 uses, the
   SKOS word none, and the glossary field is already called Aliases. T3 flags "alias" as
   a possible plural; it is singular.
2. **`kind`** is a facet here although N4 bars "kind" as a claim word in labels: the
   facet keeps the spec's field name (S4), and it is not a glossary label.
3. **`governing`** for steps 10 to 12, to match framing, building and testing, although
   "governance" (the spec's §9 heading) has more uses; governance is an alias.
4. **`definition`**, **`scope note`** and **`near miss`** are entries even though they
   are also field names, because the method's rules (D1-D4) are about them.

## Entries

### taxonomy (`taxonomy`)

- **Definition**: A taxonomy is a vocabulary of agreed terms and facets for one bounded context.
- **Scope**: Here, the files in one `domains/<name>/` folder: scope, facets, glossary, changelog and rounds. Includes the terms and the sorting questions; excludes the pattern layer, which is optional.
- **Aliases**: classification scheme, controlled vocabulary
- **Example**: [spec §1](../../design/spec.md#1-files-and-where-they-live)
- **Near miss**: An ontology: it adds formal rules a machine can reason with, which none of these domains has needed.
- **Kind**: thing
- **Related**: `glossary`, `facet`, `bounded-context`
- **Status**: candidate
- **Warrant**: "taxonomy" 38, "controlled vocabulary" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### bounded context (`bounded-context`)

- **Definition**: A bounded context is a boundary inside which each word has one meaning.
- **Scope**: One per domain folder (J2). A word may mean something else in another context; `map.md` links the two.
- **Aliases**: context
- **Example**: [spec §1](../../design/spec.md#1-files-and-where-they-live)
- **Near miss**: A repository: one repository can hold several contexts, and here a context's files live outside the repository its words govern.
- **Kind**: thing
- **Related**: `domain`, `shared-kernel`
- **Status**: candidate
- **Warrant**: "bounded context" 9, "context" 55 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### domain (`domain`)

- **Definition**: A domain is an area of Jonathan's work that gets its own taxonomy.
- **Scope**: Named by its folder under `domains/` (`ux`, `prompts`, `taxonomies`). Each domain is one bounded context.
- **Example**: [the ux domain](../ux/scope.md)
- **Near miss**: The domain's repository (`jburnhams/ux-research`): it links to the domain folder but does not hold it.
- **Kind**: thing
- **Related**: `bounded-context`
- **Status**: candidate
- **Warrant**: "domain" 73 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### owner (`owner`)

- **Definition**: An owner is a role of the person who settles disputes about a taxonomy and can veto any change to it.
- **Scope**: Named in `scope.md`; Jonathan for every domain so far (G1). Agents approve changes that pass T1-T6; the owner reviews the changelog.
- **Example**: [spec §9, G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: An approving agent: it approves a change under G1 but cannot overrule the owner.
- **Kind**: role
- **Related**: `veto`
- **Status**: candidate
- **Warrant**: "owner" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### competency question (`competency-question`)

- **Definition**: A competency question is a question that a finished taxonomy must let a reader answer from its facets and glossary alone.
- **Scope**: Five to fifteen, listed in `scope.md`; T10 checks them at the end of a round.
- **Example**: [spec §2](../../design/spec.md#2-scopemd)
- **Near miss**: A facet's question: asked of each item, where a competency question is asked of the whole taxonomy.
- **Kind**: thing
- **Related**: `ending-condition`
- **Status**: candidate
- **Warrant**: "competency question" 18 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### ending condition (`ending-condition`)

- **Definition**: An ending condition is a test result that must hold before a taxonomy is adopted.
- **Scope**: Listed in `scope.md` with target values: T1-T7, κ ≥ 0.6 per facet (T8), T10, T11, and no facet changed in the last round.
- **Example**: [ux round 1, ending conditions](../ux/rounds/round-1/results.md#ending-conditions-scopemd)
- **Near miss**: A mechanical check: one input to the ending conditions, run on every commit.
- **Kind**: thing
- **Related**: `adoption`, `competency-question`
- **Status**: candidate
- **Warrant**: "ending condition" 58 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### item (`item`)

- **Definition**: An item is a piece of a domain's own material that the facets must sort.
- **Scope**: A row of a catalogue, a section of a doc, a rule. Items keep their IDs (`b01`, `r13`) when they move between samples.
- **Example**: [ux samples](../ux/samples.md)
- **Near miss**: A term: a term names a concept; an item is a case the terms are used to sort.
- **Kind**: thing
- **Related**: `sample`
- **Status**: candidate
- **Warrant**: "item" 166 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### sample (`sample`)

- **Definition**: A sample is a set of items drawn from a domain before any of them is classified.
- **Scope**: Fixed in `samples.md` (process step 2) so that test items stay fresh. Sizes follow J7: 30 to 60 to build, 30 fresh per round.
- **Example**: [process step 2](../../design/process.md#step-2-collect-the-samples)
- **Near miss**: The domain's whole material: a sample is chosen from it, for variety.
- **Kind**: thing
- **Related**: `item`
- **Status**: candidate
- **Warrant**: "sample" 46 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### build sample (`build-sample`)

- **Definition**: A build sample is a sample that the facets and glossary are built from.
- **Scope**: Used in process steps 3 to 6. Its items may be read as often as needed.
- **Example**: [ux build sample](../ux/samples.md#build-sample-53)
- **Near miss**: A test sample: never read while building.
- **Kind**: thing
- **Broader**: `sample`
- **Status**: candidate
- **Warrant**: "build sample" 14 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### test sample (`test-sample`)

- **Definition**: A test sample is a sample held back from building and used only to test the taxonomy.
- **Scope**: Given to raters in a round. Once used, its items count as seen, so the next round needs new ones.
- **Aliases**: held-out sample, fresh items
- **Example**: [ux round-1 items](../ux/rounds/round-1/items.csv)
- **Near miss**: The bare-facet items of process step 5: they test the facet list before any definition exists, and are then spent.
- **Kind**: thing
- **Broader**: `sample`
- **Related**: `round`
- **Status**: candidate
- **Warrant**: "test sample" 4, "fresh items" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### harvest (`harvest`)

- **Definition**: A harvest is a count of the words a domain already uses for each concept, made before any label is chosen.
- **Scope**: Groups the words into synonym sets and flags homonyms (process step 3). Counts the domain's own docs, not its stored sources.
- **Aliases**: term harvest
- **Example**: [ux harvest](../ux/harvest.md)
- **Near miss**: Warrant: the evidence a harvest yields for one term.
- **Kind**: happening
- **Related**: `warrant`
- **Status**: candidate
- **Warrant**: "harvest" 57, "term harvest" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### warrant (`warrant`)

- **Definition**: A warrant is a record of where and how often a label is used, kept as the term's evidence.
- **Scope**: Counts from the harvest, file names, or Jonathan's own words (N2). The label with the most warrant wins unless it clashes with another sense.
- **Aliases**: literary warrant
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An example: one clear case of the concept, not a count of the word.
- **Kind**: property
- **Related**: `harvest`
- **Status**: candidate
- **Warrant**: "warrant" 72 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### facet (`facet`)

- **Definition**: A facet is a question that every item in a domain answers with exactly one value.
- **Scope**: Recorded in `facets.md` with its principle, values, order, unsorted list and agreement. Facets are independent: one answer does not fix another (S2).
- **Aliases**: sorting question, dimension
- **Example**: [ux facets](../ux/facets.md)
- **Near miss**: A level of a tree: a tree asks one question at each level, so an item's place depends on every question above it.
- **Kind**: thing
- **Related**: `facet-value`, `taxonomy`
- **Status**: candidate
- **Warrant**: "facet" 222, "sorting question" 3, "dimension" 13 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### facet value (`facet-value`)

- **Definition**: A facet value is a term that answers one facet's question.
- **Scope**: Every value has a glossary entry whose Facet field names its facet (T6); two to about a dozen per facet.
- **Aliases**: value
- **Example**: [spec §3](../../design/spec.md#3-facetsmd)
- **Near miss**: An alias of a value: another word for the same answer, not another answer.
- **Kind**: thing
- **Broader**: `term`
- **Related**: `facet`
- **Status**: candidate
- **Warrant**: "facet value" 10, "value" 112 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### term (`term`)

- **Definition**: A term is a concept with one entry in a domain's glossary.
- **Scope**: Identified by an identifier that never changes and named by its preferred label. Includes facet values, everyday domain words and proper names.
- **Aliases**: concept, entry
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A label: one of the words for a term; a term can have several.
- **Kind**: thing
- **Related**: `label`, `glossary`
- **Status**: candidate
- **Warrant**: "term" 109, "concept" 42, "entry" 23 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### glossary (`glossary`)

- **Definition**: A glossary is a file that holds one entry per term of a domain.
- **Scope**: `glossary.md`, with the fields of spec §4, named after SKOS so it could become RDF.
- **Example**: [ux glossary](../ux/glossary.md)
- **Near miss**: A dictionary of the field: a glossary records only the words this context agrees on.
- **Kind**: thing
- **Related**: `term`, `taxonomy`
- **Status**: candidate
- **Warrant**: "glossary" 62 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### label (`label`)

- **Definition**: A label is a word or phrase that names a term.
- **Scope**: No label is used twice in a context, after folding case and hyphens (T2).
- **Aliases**: name
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An identifier: it never changes, while a label can be renamed.
- **Kind**: thing
- **Related**: `identifier`
- **Status**: candidate
- **Warrant**: "label" 84, "name" 156 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### preferred label (`preferred-label`)

- **Definition**: A preferred label is a label that a context agrees to use for a term.
- **Scope**: The heading word of the glossary entry; chosen by warrant and the name rules N1-N7.
- **Aliases**: heading word, prefLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An alias: in use, but not the one to write.
- **Kind**: thing
- **Broader**: `label`
- **Status**: candidate
- **Warrant**: "preferred label" 14, "heading word" 1, "prefLabel" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### alias (`alias`)

- **Definition**: An alias is a label that people also use for a term and that points to its preferred label.
- **Scope**: Listed in the Aliases field; each points to one term only (N7).
- **Aliases**: alternative label, altLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A hidden label: kept for search, never offered as a word to use.
- **Kind**: thing
- **Broader**: `label`
- **Status**: candidate
- **Warrant**: "alias" 113, "altLabel" 1 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### hidden label (`hidden-label`)

- **Definition**: A hidden label is a label kept for search but never shown as advice.
- **Scope**: Misspellings and old forms.
- **Aliases**: hiddenLabel
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: A deprecated term: a whole record kept for lookup, where a hidden label is one string on a live record.
- **Kind**: thing
- **Broader**: `label`
- **Status**: candidate
- **Warrant**: "hidden label" 1, "hiddenLabel" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### identifier (`identifier`)

- **Definition**: An identifier is a code that names a term and never changes.
- **Scope**: Lower-case words joined by hyphens, in backticks; never reused after deprecation. A term in another context is written `<context>:<id>`.
- **Aliases**: ID
- **Example**: [spec §1, field grammar](../../design/spec.md#field-grammar-all-files)
- **Near miss**: A label: what people read, and what a rename changes.
- **Kind**: thing
- **Related**: `label`
- **Status**: candidate
- **Warrant**: "identifier" 3, "ID" 49 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### definition (`definition`)

- **Definition**: A definition is a sentence that says what a term is by naming its genus and what sets it apart.
- **Scope**: One sentence that starts "A <label> is a" (T4), with no hedge or example in it.
- **Aliases**: genus-differentia
- **Example**: [spec §8, Definitions](../../design/spec.md#definitions)
- **Near miss**: A scope note: it says where the edges are, not what the thing is.
- **Kind**: thing
- **Related**: `scope-note`
- **Status**: candidate
- **Warrant**: "definition" 126, "genus-differentia" 9 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### scope note (`scope-note`)

- **Definition**: A scope note is a note that says what a term includes and excludes at its edges.
- **Scope**: The Scope field. Widened after a round wherever raters split on an item.
- **Aliases**: scopeNote
- **Example**: [ux round 1, fixes](../ux/rounds/round-1/results.md#fixes-after-scoring-2026-11-26)
- **Near miss**: A near miss: one named case it is not, where a scope note draws the line.
- **Kind**: thing
- **Related**: `definition`, `near-miss`
- **Status**: candidate
- **Warrant**: "scope note" 28, "scopeNote" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### near miss (`near-miss`)

- **Definition**: A near miss is a note that names something a term looks like but is not, and why.
- **Scope**: One per entry (D4).
- **Example**: [spec §4](../../design/spec.md#4-glossarymd)
- **Near miss**: An alias: the same concept under another word, where a near miss is a different concept.
- **Kind**: thing
- **Related**: `scope-note`
- **Status**: candidate
- **Warrant**: "near miss" 99 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### operation (`operation`)

- **Definition**: An operation is a named change to a taxonomy, logged with its date and reason.
- **Scope**: One of add, rename, split, merge, move, redefine, deprecate (G4), plus adopt for a whole domain.
- **Aliases**: named operation
- **Example**: [spec §9, G4](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: An edit with no name: not allowed, because the changelog could not say what happened.
- **Kind**: happening
- **Related**: `changelog`
- **Status**: candidate
- **Warrant**: "operation" 14, "named operation" 8 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### changelog (`changelog`)

- **Definition**: A changelog is a file that records every operation on a taxonomy, newest day first.
- **Scope**: `changelog.md` in the domain folder; each line names the approving agent (G1).
- **Example**: [ux changelog](../ux/changelog.md)
- **Near miss**: A term's History field: the same events, kept on each term.
- **Kind**: thing
- **Related**: `operation`
- **Status**: candidate
- **Warrant**: "changelog" 25 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### status (`status`)

- **Definition**: A status is a property of a term that says whether it is proposed, agreed or replaced.
- **Scope**: `candidate` (usable, not yet agreed), `approved`, or `deprecated` with a Replaced by field (G3, G5).
- **Example**: [spec §9, G3](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: The status of a domain in `scope.md` (`draft`, `in use`, `retired`), which covers the whole taxonomy.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "status" 83 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### round (`round`)

- **Definition**: A round is a pass in which raters sort a fresh test sample and the files are fixed from their disagreements.
- **Scope**: Kept in `rounds/round-N/`: the items, the prompts, each rater's answers, the results and review. Steps 7 to 9 repeat by round.
- **Example**: [ux round 1](../ux/rounds/round-1/README.md)
- **Near miss**: A build pass: it reads the build sample, which a round never does.
- **Kind**: happening
- **Related**: `rater`, `agreement-test`, `test-sample`
- **Status**: candidate
- **Warrant**: "round" 166 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### rater (`rater`)

- **Definition**: A rater is a role of a model or person that sorts items using only the facets and glossary.
- **Scope**: At least two model families (J6); each answers alone, with the values shuffled.
- **Aliases**: judge
- **Example**: [ux round-1 answers](../ux/rounds/round-1/answers/claude.csv)
- **Near miss**: An approving agent: it decides whether a change is accepted, not where an item goes.
- **Kind**: role
- **Related**: `round`, `kappa`
- **Status**: candidate
- **Warrant**: "rater" 57, "judge" 15 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### agreement test (`agreement-test`)

- **Definition**: An agreement test is a test in which raters sort the same items independently and their answers are compared per facet.
- **Scope**: T8. Disagreements show which definitions to fix.
- **Aliases**: T8
- **Example**: [process step 8](../../design/process.md#step-8-agreement-test)
- **Near miss**: A name test: it asks what a label means, not where an item goes.
- **Kind**: happening
- **Related**: `kappa`, `round`
- **Status**: candidate
- **Warrant**: "agreement test" 8, "T8" 11 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### kappa (`kappa`)

- **Definition**: Kappa is a measure of how often raters agree beyond what chance alone would give.
- **Scope**: Cohen's for two raters, Fleiss' for three or more; the target is at least 0.6 per facet (J5).
- **Aliases**: Cohen's kappa, Fleiss' kappa, κ
- **Example**: [ux round-1 results](../ux/rounds/round-1/results.md#kappa-per-facet)
- **Near miss**: Raw agreement: the share of items answered the same, which chance alone can make high.
- **Kind**: property
- **Related**: `agreement-test`
- **Status**: candidate
- **Warrant**: "kappa" 23, "Cohen's kappa" 3, "Fleiss' kappa" 2, "κ" 15 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### name test (`name-test`)

- **Definition**: A name test is a test in which a fresh reader guesses what a label means before seeing its definition.
- **Scope**: T9. A wrong guess means the name or the concept needs work; WordNet senses flag homonyms.
- **Aliases**: T9, guess the name
- **Example**: [ux name test](../ux/rounds/round-1/name-test/results.md)
- **Near miss**: An agreement test: it sorts items with the definitions in hand.
- **Kind**: happening
- **Status**: candidate
- **Warrant**: "name test" 9, "T9" 13, "guess the name" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### unsorted list (`unsorted-list`)

- **Definition**: An unsorted list is a list in a facet's record of items that no value fits yet.
- **Scope**: The Unsorted field, with the date each item arrived; it should be empty at each review (S6).
- **Aliases**: Unsorted
- **Example**: [ux facets, aspect](../ux/facets.md#aspect-aspect)
- **Near miss**: A disagreement: there the raters chose different values; an unsorted item has none that fits.
- **Kind**: thing
- **Related**: `facet`
- **Status**: candidate
- **Warrant**: "unsorted list" 1, "Unsorted" 31 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### mechanical check (`mechanical-check`)

- **Definition**: A mechanical check is a check that a script runs on every commit.
- **Scope**: T1 to T6, in `tools/check_domain.py`.
- **Example**: [spec §10](../../design/spec.md#mechanical-every-commit)
- **Near miss**: A judgement test (T7-T11): it needs a rater or reviewer.
- **Kind**: happening
- **Status**: candidate
- **Warrant**: "mechanical check" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### adoption (`adoption`)

- **Definition**: An adoption is a change that puts a whole taxonomy into use once its ending conditions hold.
- **Scope**: Terms move to `approved` and `scope.md` to `in use` (process step 10); an agent approves, Jonathan can veto.
- **Example**: [process step 10](../../design/process.md#step-10-adopt)
- **Near miss**: Approving one term: an operation on one entry, where adoption covers the domain.
- **Kind**: happening
- **Related**: `ending-condition`
- **Status**: candidate
- **Warrant**: "adoption" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### veto (`veto`)

- **Definition**: A veto is a decision by the owner that reverses a change.
- **Scope**: Logged as its own operation in the changelog (G1).
- **Example**: [spec §9, G1](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: A deprecation: a named operation any approver may make under G1.
- **Kind**: happening
- **Related**: `owner`
- **Status**: candidate
- **Warrant**: "veto" 64 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### alias drift (`alias-drift`)

- **Definition**: Alias drift is a property of a domain's writing in which aliases are used where the preferred label belongs.
- **Scope**: T12, counted in new docs after adoption. A rising count means the preferred label is losing.
- **Example**: [spec §10, in use](../../design/spec.md#in-use-after-adoption)
- **Near miss**: A new word with no entry (T13): drift is a known word used in place of the agreed one.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "alias drift" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### shared kernel (`shared-kernel`)

- **Definition**: A shared kernel is a set of terms that two or more contexts agree to share.
- **Scope**: Changes need every affected owner (G7).
- **Example**: [spec §9, G7](../../design/spec.md#9-governance-how-a-taxonomy-changes)
- **Near miss**: A map entry: it links two contexts' terms without making them one.
- **Kind**: thing
- **Related**: `bounded-context`
- **Status**: candidate
- **Warrant**: "shared kernel" 8 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### pattern (`pattern`)

- **Definition**: A pattern is a record of a recurring problem in a design domain and the solution that resolves its forces.
- **Scope**: One file per pattern in `patterns/`, with name, context, problem, forces and solution (spec §7).
- **Example**: [spec §7](../../design/spec.md#7-patterns-design-domains-only)
- **Near miss**: A term: a term names a concept; a pattern names a solution and links to other patterns.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "pattern" 54 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

## Facet values

### thing (`thing`)

- **Definition**: A thing is a term kind for something that exists in its own right and keeps its identity over time.
- **Scope**: Files, items, samples, labels: OntoClean's rigid kinds (S4). No thing sits under a role or a happening (T5).
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A role: a part a thing plays for a while (a model is a thing; rater is one of its roles).
- **Kind**: property
- **Facet**: `kind`
- **Status**: candidate
- **Warrant**: "thing" 95 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### property (`property`)

- **Definition**: A property is a term kind for a quality that something has.
- **Scope**: Status, kappa, warrant: each is had by a term, a round or a label.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing: it exists on its own; a property exists only in what has it.
- **Kind**: property
- **Facet**: `kind`
- **Status**: candidate
- **Warrant**: "property" 50 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### role (`role`)

- **Definition**: A role is a term kind for a part that something plays in a relation and can stop playing.
- **Scope**: Owner, rater.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing: a model stays a model when it stops rating.
- **Kind**: property
- **Facet**: `kind`
- **Status**: candidate
- **Warrant**: "role" 38 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### happening (`happening`)

- **Definition**: A happening is a term kind for something that takes place over time.
- **Scope**: Rounds, tests, operations, harvests.
- **Example**: [spec S4](../../design/spec.md#structure)
- **Near miss**: A thing that records a happening: the changelog is a thing; the operation it records is a happening.
- **Kind**: property
- **Facet**: `kind`
- **Status**: candidate
- **Warrant**: "happening" 12 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### framing (`framing`)

- **Definition**: Framing is a stage of the method that decides a domain's purpose, readers and ending conditions before any word is collected.
- **Scope**: Process steps 0 and 1; produces `scope.md`.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Building: it starts once the frame is written.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: candidate
- **Warrant**: "framing" 3 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### building (`building`)

- **Definition**: Building is a stage of the method that collects samples and words and drafts the facets and glossary.
- **Scope**: Process steps 2 to 6.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Testing: building may read the build sample; testing may not.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: candidate
- **Warrant**: "building" 10 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### testing (`testing`)

- **Definition**: Testing is a stage of the method that sorts fresh items, scores agreement and tries the names on fresh readers.
- **Scope**: Process steps 7 to 9, repeated by round.
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Mechanical checks: they run in every stage, on every commit.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: candidate
- **Warrant**: "testing" 1 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)

### governing (`governing`)

- **Definition**: Governing is a stage of the method that adopts a taxonomy and then changes it only by named operations.
- **Scope**: Process steps 10 to 12.
- **Aliases**: governance, maintenance
- **Example**: [process, the steps at a glance](../../design/process.md#the-steps-at-a-glance)
- **Near miss**: Building: a change after adoption is an operation, never a redraft.
- **Kind**: happening
- **Facet**: `stage`
- **Status**: candidate
- **Warrant**: "governing" 0, "governance" 4, "maintenance" 2 (design/ and domains/ux/, 2026-11-26)
- **History**: 2026-11-26 added (drafted from the spec and process; not yet tested)
