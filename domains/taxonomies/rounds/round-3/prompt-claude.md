# Rater prompt: taxonomies taxonomy, round 3 (one question)

You are classifying 73 items for a taxonomy agreement test. Use only the definitions below; do not look anything up, do not read any files, and do not use other knowledge of the repo they come from.

Each item is one unit of a written method for agreeing a taxonomy (a controlled vocabulary with facets) for one area of work: a rule, a process step, a file field or a recorded decision. The repo's owner is Jonathan.

For every item, answer the question with exactly one value, chosen from its list. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Classify what the item itself says. The `kind` column says what it is: a rule of the method, a process step (some with who does it; "light version" steps are the short form of the process for small domains), a file field, a file of a domain folder, or a decision the owner recorded. The item's own id has been removed, so read its text; ids inside the text are references to other rules. The `from` column is part of the item.
- check: who or what has the final word on whether the item holds. `script` only for what a script stored in the repo checks today; the definition of `script` lists them all. Anything else is `judgement`, even when a program could check it, unless the item's own text gives the final word to Jonathan or the owner (`owner-decision`); "can veto" or "checked by Jonathan" leaves it to whoever approves, so `judgement`.
- A decision is sorted by what it settles, not by the fact that the owner made it.
- If an item names several things, classify the first; if no value fits, pick the closest and mark `unsure`.

Answer as CSV only, with this header and one row per item, in the items' order. Quote any note that contains a comma.

```
id,check,note
```

## The questions and their values

- **check**: What settles whether it is met? Values: `owner-decision`, `judgement`, `script`

## Definitions of the values

### script (`script`)

- **Definition**: A script is a check in which a program stored in this repo decides whether an item holds.
- **Scope**: Only what these scripts check today: `tools/check_domain.py` (the mechanical tests T1-T6: IDs unique, required fields present, references exist, no cycles in broader, no label used twice, name form, definition form, kinds, every facet value has an entry and a facet has 2 to 12 values), which reads `glossary.md` and `facets.md`; `tools/kappa.py` (kappa per facet against the 0.6 target, the majority label and splits: T8's pass, J23, J24); and a domain's `sample.py` (the seeded draw, J21). Excludes anything no script checks yet, even where a program could (a file present, a link in place, a count of aliases in use, T12, T13), and the rules the mechanical tests only flag for a person (N4, N7): those are `judgement`.
- **Near miss**: `scope.md` must exist (spec §1): a program could check it, but none does, so `judgement` until a script is added.
- **Kind**: role
- **Facet**: `check`

### judgement (`judgement`)

- **Definition**: A judgement is a check in which a person or a model reads for sense and decides whether an item holds.
- **Scope**: Includes writing and reviewing definitions, choosing facets and labels, rating items, the name test, the heuristic review and agent approval under G1, where Jonathan can veto but an agent settles it. Includes any item that no stored script checks: one with a condition that needs reading for sense, such as naming which operation a change is (G4), and one a program could check but none yet does (a file present, a link in place). Excludes what a stored script checks (`script`) and a call the text reserves for the owner (`owner-decision`).
- **Near miss**: A step "checked by Jonathan": he looks, but the step's work is settled by whoever does it, so `judgement`.
- **Kind**: role
- **Facet**: `check`

### owner decision (`owner-decision`)

- **Definition**: An owner decision is a check in which the item's own text gives the final word to Jonathan or a domain's owner.
- **Scope**: Includes deciding to start a domain, choosing the facets (process step 4, "Jonathan decides"), a veto, design changes, open questions left for him, and shared-kernel changes needing every owner. A decision record is sorted by what it settles, not by the fact that Jonathan made it. Excludes "can veto" and "checked by Jonathan", where an agent still settles it (`judgement`).
- **Aliases**: Jonathan's decision
- **Near miss**: G1, agents approve and Jonathan can veto: the veto is his, but what settles a change day to day is an agent's approval, so `judgement`. A decision that adds a step in which Jonathan decides (J13 adds step 4): the decision settles how the step is done, so it takes that work's check, not the step's Who.
- **Kind**: role
- **Facet**: `check`

## Items

```csv
id,item,kind,from
r01,"Rules whose best source is not stored: Keep them marked and in force; check each when the source is fetched (Nickerson 2013, Kundisch 2022, Cohen 1960, Berlin 1992, biology codes, *A Pattern Language*)",a recorded decision,design/decisions.md
r02,"glossary.md: Near miss: something it looks like but is not, and why (D4)",a file field,design/spec.md
r03,"Facets. Every facet value has a glossary entry; no value is empty in the latest classification (an empty cell asks whether a concept or an axis is wrong, Kwasnik pp.",a rule,design/spec.md
r04,"Classify fresh items, fix, repeat (who: model). Classify a fresh test sample using only `facets.md` and `glossary.md`. Note every hesitation; put items that fit no value in the facet's Unsorted list (S6).",a process step,design/process.md
r05,"Agreement. Two raters classify the same fresh items independently, using only `facets.md` and `glossary.md`. Compute Cohen's kappa per facet. Target: κ ≥ 0.6 on every facet (J5). Disagreements show where the vocabulary is unclear (Z39.19 §11.2.2, pp.",a rule,design/spec.md
r06,"scope.md: Neighbours: other contexts it touches, and the map file",a file field,design/spec.md
r07,"Sample sizes: Build from 30-60 items, test on 30 fresh items per round; light version under ~30 items",a recorded decision,design/decisions.md
r08,"Integrity. Every ID unique; every record has all required fields; every referenced ID exists (""no cross-references ...",a rule,design/spec.md
r09,"glossary.md: Scope: what it includes and excludes, especially at the edges (D2)",a file field,design/spec.md
r10,"Add a level only when it says something new. A narrower term is added ""only when there is something that we can say about this class that we cannot say about the superclass"" (Noy and McGuinness §4.4).",a rule,design/spec.md
r11,"Test the bare facet list (who: model). Before writing any glossary entries, classify about 10 test items with the facet names and a one-line description of each value, and add, drop or split facets now.",a process step,design/process.md
r12,No evaluative words in names: Adopt as N7 (proposal 3),a recorded decision,design/decisions.md
r13,"scope.md: Purpose: one sentence: what the taxonomy is for, and the one question every facet must help answer",a file field,design/spec.md
r14,"Named operations only. Every change is one of: add, rename (label changes, ID stays), split, merge, move (change broader or facet), redefine, deprecate. Each is logged in `changelog.md` and in the term's History with date and reason (Z39.19 §§11.3.1.2, 11.3.2.2, pp. 96-97).",a rule,design/spec.md
r15,"Near miss. One thing it is easily confused with, and why it is not it: the edge of the concept, where raters disagree. TnT-LLM's raters disagreed mostly at the boundaries between neighbouring labels (Wan et al. App.",a rule,design/spec.md
r16,glossary.md: Broader: the ID of the nearest is-a parent (S5),a file field,design/spec.md
r17,"Harvest, then choose. Collect the words already in use, with counts, before choosing. Choose the preferred label by warrant: the words in the content (literary warrant), the words of the readers (user warrant), and the owner's needs (organizational warrant) (Z39.19 §5.3.5).",a rule,design/spec.md
r18,"Find facets by comparison, and test the bare facet list early: Adopt both as process steps 4 and 5 (proposals 1 and 2)",a recorded decision,design/decisions.md
r19,glossary.md: Example: a link to the clearest real case in the repo (D3),a file field,design/spec.md
r20,"Harvest the words (who: model). List every term used for the things in the build sample, and in Jonathan's own words about the domain. Count each term's uses across the repo.",a process step,design/process.md
r21,"Agents approve, Jonathan can veto. (J8, decided by Jonathan 2026-11-25). An agent may approve a change, or a term's move from `candidate` to `approved`, when every mechanical test (T1-T6) passes and the change is logged with its reason.",a rule,design/spec.md
r22,"Deprecate, never delete. A deprecated term keeps its record, ID, labels and history, and its Replaced by field names the term(s) to use instead; looking up an old label finds the deprecated record, which points on.",a rule,design/spec.md
r23,"glossary.md: Hidden: misspellings and old forms, kept for search, never shown as advice",a file field,design/spec.md
r24,"Replace ""confidence"" with a status: `candidate` / `approved` / `deprecated`",a recorded decision,design/decisions.md
r25,"One concept, one preferred name; one name, one concept. inside a context. Names must map to concepts one-to-one, with no homonyms and no synonyms (Deissenboeck and Pizka pp.",a rule,design/spec.md
r26,scope.md: Competency questions: 5 to 15 questions the taxonomy must let you answer,a file field,design/spec.md
r27,"Guess the name. Show someone who has not seen the glossary a preferred label and ask what it means. A wrong guess means the name or the concept needs work (Meszaros and Doble, ""Evocative Pattern Name"").",a rule,design/spec.md
r28,Put into use (who: model). Link `domains/<name>/glossary.md` in this repo from the domain repo's `CLAUDE.md` / `AGENTS.md` (by its GitHub URL) so agents there load it and use preferred labels (J2).,a process step,design/process.md
r29,"Who has the final say: Agents approve, Jonathan can veto: an agent approves changes that pass T1-T6 with a logged reason; Jonathan is the named owner, reviews the changelog, can reverse anything and settles disputes",a recorded decision,design/decisions.md
r30,"facets.md: Agreement: the latest kappa, the date, the sample size, and who rated",a file field,design/spec.md
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
