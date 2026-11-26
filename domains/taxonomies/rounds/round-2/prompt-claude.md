# Rater prompt: taxonomies taxonomy, round 2

You are classifying 43 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one unit of a written method for agreeing a taxonomy (a controlled vocabulary with facets) for one area of work: a rule, a process step, a file field or a recorded decision. The repo's owner is Jonathan.

For every item, answer all three questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify what the item itself says. The `kind` column says what it is: a rule of the method, a process step (some with who does it; "light version" steps are the short form of the process for small domains), a file field, a file of a domain folder, or a decision the owner recorded. The item's own id has been removed, so read its text; ids inside the text are references to other rules. The `from` column is part of the item.
- part: the part of a domain's files that would change if the item were changed or broken. Words and their counts (harvest, warrant) are `naming`; items, samples, rounds, raters and kappa are `evidence`; how contexts meet is `boundary`; what the domain is for and when it is finished is `purpose`.
- stage: the first group of process steps in which the item is applied or checked: `framing` steps 0-1, `building` steps 2-6, `testing` steps 7-9, `governing` steps 10-12. A validation test T1 to T11 is `testing`; T12 to T14 are `governing`. A field or a file takes the stage of the step that first fills or writes it; a light-version step takes the stage of the steps it runs. If an item applies in several stages, the first wins.
- check: who or what has the final word on whether the item holds. `script` only when a program can decide pass or fail on its own (a count, a format, a computed kappa); a script that only flags for a person is `judgement`. `owner-decision` only when the item's own text gives the final word to Jonathan or the owner; "can veto" or "checked by Jonathan" leaves it to whoever approves, so `judgement`.
- A decision is sorted by what it settles, on all three questions, not by the fact that the owner made it.
- If an item names several things, classify the first; if no value fits, pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,part,stage,check,note
```

## The questions and their values

- **part**: What part of a taxonomy is it about? Values: `meaning`, `purpose`, `change`, `structure`, `evidence`, `naming`, `boundary`
- **stage**: In which stage of the work does it first apply? Values: `building`, `framing`, `testing`, `governing`
- **check**: What settles whether it is met? Values: `judgement`, `script`, `owner-decision`

## Definitions of the values

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

### evidence (`evidence`)

- **Definition**: Evidence is a part of a taxonomy that covers the items it is tried on and the results of trying it.
- **Scope**: Includes samples, build and test items, rounds, raters and their answers, kappa and the agreement test (T8), the Agreement field, and sample sizes (J7). Excludes counts of words (`naming`).
- **Near miss**: A competency question: it is asked of the finished taxonomy, but it states what the taxonomy is for, so `purpose`.
- **Kind**: property
- **Facet**: `part`

### judgement (`judgement`)

- **Definition**: A judgement is a check in which a person or a model reads for sense and decides whether an item holds.
- **Scope**: Includes writing and reviewing definitions, choosing facets and labels, rating items, the name test, the heuristic review and agent approval under G1, where Jonathan can veto but an agent settles it. Includes any item with at least one condition that needs reading for sense, such as naming which operation a change is (G4). Excludes an item whose every condition a program can test (`script`) and a call the text reserves for the owner (`owner-decision`).
- **Near miss**: A step "checked by Jonathan": he looks, but the step's work is settled by whoever does it, so `judgement`.
- **Kind**: role
- **Facet**: `check`

### governing (`governing`)

- **Definition**: Governing is a stage of the method that adopts a taxonomy and then changes it only by named operations.
- **Scope**: Process steps 10 to 12: adoption, putting into use, and maintenance. Includes the G rules, reviews, the in-use tests T12 to T14, and `map.md` (written in step 12).
- **Aliases**: governance, maintenance
- **Near miss**: Building: a change after adoption is an operation, never a redraft.
- **Kind**: happening
- **Facet**: `stage`

### framing (`framing`)

- **Definition**: Framing is a stage of the method that decides a domain's purpose, readers and ending conditions before any word is collected.
- **Scope**: Process steps 0 and 1; produces `scope.md`. Includes every `scope.md` field and the decisions they settle.
- **Near miss**: Building: it starts once the frame is written.
- **Kind**: happening
- **Facet**: `stage`

### building (`building`)

- **Definition**: Building is a stage of the method that collects samples and words and drafts the facets and glossary.
- **Scope**: Process steps 2 to 6: samples, harvest, facets, the bare-facet test, names and definitions. Includes the rules applied while drafting (S, N and D rules) and the `facets.md` and `glossary.md` fields, which step 4 or 6 first fills.
- **Near miss**: Testing: building may read the build sample; testing may not.
- **Kind**: happening
- **Facet**: `stage`

### purpose (`purpose`)

- **Definition**: A purpose is a part of a taxonomy that says what it is for, who reads it, what it must answer and when it is finished.
- **Scope**: Includes the `scope.md` fields Purpose, Readers, Owner, Competency questions, Out of scope and Ending conditions, process steps 0 and 1, and the competency-question test (T10). Excludes the edges between this context and others (`boundary`).
- **Near miss**: Out of scope: it marks the edge of the domain's own subject, so `purpose`; a link to a neighbouring context is `boundary`.
- **Kind**: property
- **Facet**: `part`

### boundary (`boundary`)

- **Definition**: A boundary is a part of a taxonomy that covers how its context meets other contexts.
- **Scope**: Includes one context per domain, `map.md` and its mappings (closeMatch and the rest), the shared kernel, and the `scope.md` fields Context and Neighbours (spec §8 Contexts, C1-C3, G7). Excludes what the domain itself covers (`purpose`).
- **Aliases**: contexts
- **Near miss**: A shared kernel change: it needs every owner's agreement, but it is about two contexts meeting, so `boundary`, with check `owner-decision`.
- **Kind**: property
- **Facet**: `part`

### testing (`testing`)

- **Definition**: Testing is a stage of the method that sorts fresh items, scores agreement and tries the names on fresh readers.
- **Scope**: Process steps 7 to 9, repeated by round. Includes every validation test from T1 to T11 (the spec runs the mechanical ones after each round, step 7), the Agreement and Unsorted fields, and rater rules.
- **Near miss**: A rule a test checks, such as N7 checked by T3: the rule first applies when a label is chosen, so `building`; the test is `testing`.
- **Kind**: happening
- **Facet**: `stage`

### naming (`naming`)

- **Definition**: Naming is a part of a taxonomy that covers the words for its concepts: labels, aliases, hidden labels and identifiers.
- **Scope**: Includes the rules N1-N8, the label test (T2), name form (T3), the name test (T9), and the harvest and warrant that choose a label (N2). Excludes what the word means (`meaning`).
- **Aliases**: names
- **Near miss**: Warrant: it is counted evidence, but it exists to choose a label, so `naming`, not `evidence`.
- **Kind**: property
- **Facet**: `part`

### owner decision (`owner-decision`)

- **Definition**: An owner decision is a check in which the item's own text gives the final word to Jonathan or a domain's owner.
- **Scope**: Includes deciding to start a domain, choosing the facets (process step 4, "Jonathan decides"), a veto, design changes, open questions left for him, and shared-kernel changes needing every owner. A decision record is sorted by what it settles, not by the fact that Jonathan made it. Excludes "can veto" and "checked by Jonathan", where an agent still settles it (`judgement`).
- **Aliases**: Jonathan's decision
- **Near miss**: G1, agents approve and Jonathan can veto: the veto is his, but what settles a change day to day is an agent's approval, so `judgement`. A decision that adds a step in which Jonathan decides (J13 adds step 4): the decision settles how the step is done, so it takes that work's check, not the step's Who.
- **Kind**: role
- **Facet**: `check`

### meaning (`meaning`)

- **Definition**: Meaning is a part of a taxonomy that covers what each term is: its definition, scope note, example and near miss.
- **Scope**: Includes the rules D1-D5 and the definition form test (T4). Excludes the term's label (`naming`) and its place among other terms (`structure`).
- **Aliases**: definitions
- **Near miss**: The Kind field: D5 asks for it, but it places the term among kinds (S4), so `structure`.
- **Kind**: property
- **Facet**: `part`

### script (`script`)

- **Definition**: A script is a check in which a program decides from the files whether an item holds.
- **Scope**: Includes counts, uniqueness, presence of fields, formats and computed figures: the mechanical tests T1-T6, kappa against its target (T8's pass), sample sizes, and the in-use counts (T12, T13). A program must be able to decide pass or fail without anyone reading for sense: every condition the item sets must be one a program can test (a record kept, a field present, a link in place). A clause saying what the item is for ("so agents use it") is not a condition. Excludes a script that only flags candidates for a person to decide (`judgement`).
- **Near miss**: N7, no evaluative words: T3 flags words from a short list, but a person decides, so `judgement`. G4, named operations only: the list of operations looks checkable, but saying which operation a change is takes reading, so `judgement`.
- **Kind**: role
- **Facet**: `check`

## Items

```csv
id,item,kind,from
h01,"Genus-differentia. ""A <term> is a <genus> that <differentia>."" One genus, the nearest one; no categorizer words; no ""and"" or ""or"" in the genus; no circularity; no ""usually"" or ""generally""; no examples or lists inside the definition; no evaluative or indexical words (Seppälä et al.",a rule,design/spec.md
h02,"Small shared kernel. Terms that are truly the same across contexts go in a shared kernel: ""Keep this kernel small"", and it ""shouldn't be changed without consultation"" (Evans p. 31). A kernel term is a boundary object: ""plastic enough to adapt to local needs ...",a rule,design/spec.md
h03,"scope.md: Context: the repo or area this vocabulary governs, and its short context name",a file field,design/spec.md
h04,"Build the checker script: Yes, after J1 and J3: a small script for T1 to T6 and T12, run in each domain repo",a recorded decision,design/decisions.md
h05,"Kind and rigidity. Each term states its Kind. A role (sub-agent, reviewer) or a phase (draft, released) is never the broader term of a kind, and ""can be a"" is not ""is a"": OntoClean's own example wrongly puts *Agent* above *Animal*; ""animals can be agents"" (OntoClean §8.3).",a rule,design/spec.md
h06,"Maintain (who: owner). Changes follow spec §9: anyone proposes a `candidate`, an agent approves it under spec G1 with Jonathan able to veto, every change is a named operation in `changelog.md` and the term's history, and nothing is deleted (Z39.19 §§11.3-11.3.2, pp. 96-97).",a process step,design/process.md
h07,"glossary.md: Definition: one sentence, genus-differentia (D1)",a file field,design/spec.md
h08,"No permanent ""other"". Each facet has an Unsorted list, reviewed every round. A growing one means the structure is wrong: ""The sure sign of a 'premature' hierarchical structure is the need for a 'miscellaneous' or 'other' category"" (Kwasnik pp.",a rule,design/spec.md
h09,"Heuristic review. At the end of a build round, check the evaluation questions of Z39.19 §11.2.2: unmarked synonyms, missing facets, out-of-date terms, consistent term form, quality of definitions and scope notes.",a rule,design/spec.md
h10,"glossary.md: Kind: `thing`, `property`, `role`, or `happening` (S4)",a file field,design/spec.md
h11,"When to run the process: Only when a domain is being worked in, inside that work; review monthly while active (proposal 9)",a recorded decision,design/decisions.md
h12,"One principle per facet. Each facet uses a single characteristic of division, and its values are mutually exclusive and jointly exhaustive for the items in scope.",a rule,design/spec.md
h13,"facets.md: Order: the order used for the values (by sequence, size, simple to complex, ...)",a file field,design/spec.md
h14,"Collect the samples (who: model, checked by Jonathan). Collect ""a representative sample of the entities. In a large domain, get enough to cover all foreseen possibilities. In a small domain, use the entire domain"" (Denton §2.3 step 1). Items are files, sections or rules, whatever the competency questions are about.",a process step,design/process.md
h15,"Review. Review the unsorted lists and candidates at intervals set by how fast terms change (Z39.19 §11.3.1, p. 96), and at least whenever the domain is being actively worked on (J10). Shared-kernel changes need every affected context's owner (Evans p. 31).",a rule,design/spec.md
h16,"Whose needs win: Jonathan's first, then the agents' (proposal 8)",a recorded decision,design/decisions.md
h17,glossary.md: Matches: see `map.md` (C3),a file field,design/spec.md
h18,"Labels. No label (preferred, alias or hidden) used twice in the context, after folding case and hyphens, counting deprecated records too (G5 keeps an old label on its deprecated record only); every deprecated record has a Replaced by that exists (SKOS S13-S14; potential duplicates, Z39.19 §11.4.6).",a rule,design/spec.md
s01,"(Light version for small domains) One round of step 7 and the agreement test of step 8 on the held-back items, with two model families as raters (J6). With fewer than 30 items, kappa is recorded as indicative: it guides fixes but is not an ending condition (spec T8).",a process step,design/process.md
s02,An item is a heading plus its opening text; raters sort the mechanism: Yes (M7),a recorded decision,design/decisions.md
s03,(Light version for small domains) Steps 3 to 6 in one sitting on the remaining items.,a process step,design/process.md
s04,"An item is a section's heading and its opening text, and raters sort the mechanism. where items are sections of prose rather than catalogue rows, each item is the heading plus the first lines under it (up to about 300 characters), and the rater prompt says to classify the mechanism the section describes, not the doc it is in.",a rule,design/method-v1.1.md
s05,"Three raters from three families, scored with Fleiss' and pairwise kappa. T8 uses three raters, each from a different model family, each the strongest model that family offers on Jonathan's plans at the time (for 2026-11: Claude, an OpenAI model through `codex exec`, and a Gemini Pro model through Antigravity's `agy -p`; not a Flash model).",a rule,design/method-v1.1.md
s06,"scope.md: holds purpose, readers, owner, competency questions, out of scope, neighbours, ending conditions; required: yes",a file of a domain folder,design/spec.md
s07,(Light version for small domains) Steps 0 and 1 as usual.,a process step,design/process.md
s08,"Three raters from three families, strongest model each; pass on Fleiss' κ ≥ 0.6 and the non-author pair's Cohen's κ ≥ 0.6: Yes (M4); Jonathan asked for OpenAI and a better Gemini on 2026-11-26",a recorded decision,design/decisions.md
s09,"With three raters, the majority answer is the round's label. an item where two of three raters agree takes that value for T7; an item where all three differ goes to the facet's Unsorted list and is the first thing the next round's fixes address. Fixes still use the disagreements, not the majority.",a rule,design/method-v1.1.md
s10,"Build a large domain in stages (kernel and areas, then one area at a time) inside one context: Yes (M1)",a recorded decision,design/decisions.md
s11,facets.md: holds the facets and their values; required: yes,a file of a domain folder,design/spec.md
s12,Test sample at least 30 and at least 5 per value of the largest facet: Yes (M3); 60 for prompts stage 1,a recorded decision,design/decisions.md
s13,glossary.md: holds one entry per concept; required: yes,a file of a domain folder,design/spec.md
s14,"(Light version for small domains) Adopt when T1 to T7, T10 and T11 pass. Alexander's warning applies most here: keep it piecemeal and inside real work (Gabriel 2023, App. E.2).",a process step,design/process.md
s15,patterns/<id>.md: holds one pattern per file (design domains only); required: no,a file of a domain folder,design/spec.md
s16,"Build a large domain in stages, inside one context. when a domain has more than about 300 candidate items or more than about six distinct areas, build it in stages. Stage 1 covers the kernel (the words every area uses) and one facet that sorts every item into an area.",a rule,design/method-v1.1.md
s17,"A rater run through an agent CLI is kept to the prompt. when a rater is called through a vendor's agent CLI rather than an API (Jonathan's ChatGPT and Google AI plans have no API credit), run it in a new, empty directory, read-only, with tools and web access off where the CLI allows, the whole rater prompt as the only user input, and record the CLI name and version, the model, the reasoning effort and the date.",a rule,design/method-v1.1.md
s18,"(Light version for small domains) Before building, hold back a third of the items (at least 10; if the domain has fewer than about 15 items, skip the held-out set and the kappa test altogether and rely on T7, T10 and T11).",a process step,design/process.md
s19,"Rules for a rater run through an agent CLI (empty folder, read-only, record CLI and model): Yes (M6)",a recorded decision,design/decisions.md
s20,"With three raters, two-of-three is the round's label; three-way splits go to Unsorted: Yes (M5)",a recorded decision,design/decisions.md
s21,map.md: holds links to other contexts' terms and the shared kernel; required: once a second context exists,a file of a domain folder,design/spec.md
s22,"Test sample: at least 30, and at least 5 per value of the largest facet. each round's fresh sample is at least 30 items and at least five times the number of values in the largest facet. For prompts stage 1 (`area` has 8 values) that is 40; the domain uses 60, the round size J7 allowed for building.",a rule,design/method-v1.1.md
s23,"Write the item unit and population down, and draw by a seeded rule. before drawing, `samples.md` states what one item is, which files the population comes from, the filters, and the seed.",a rule,design/method-v1.1.md
s24,changelog.md: holds every change as a named operation; required: yes,a file of a domain folder,design/spec.md
s25,"Write down the item unit and population, and draw by a stored, seeded script: Yes (M2)",a recorded decision,design/decisions.md
```
