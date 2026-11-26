# Taxonomies taxonomy: samples

**In one line**: the 106 items the taxonomy is built from and tested on, fixed before any
classification so the test items stay fresh (process step 2).

**In plain words**: an *item* is one rule, step, file field or decision of the method.
We sort the build items to find the questions, then sort items we have not looked at to
see whether the questions still work.

Drawn by [`sample.py`](./sample.py) (seed 20261126) from `design/spec.md`, `design/process.md`
and `design/decisions.md` at commit `c4fa001` (2026-11-26), into
[`items-all.csv`](./items-all.csv). Each kind of item (rule, step, field, decision) is
shuffled and spread evenly through one order, which is cut into the sets, so every set has
the same mix. Item text is the rule's title and first sentences, without citations; a step also
carries its "Who" from the process's table of steps, since a reader sees both.

## Build sample (48)

Used in steps 3 to 6: the harvest, the facets and the glossary were built from these.

| ID | Item | From |
|---|---|---|
| `b01` | spec N5. Basic level for the readers. Prefer the word the readers reach for first. Basic-level categories are "the most codable, most coded, and most necessary in language" (Rosch et al. 1976, abstract and Part II); which level is basic depends on the readers (Rosch et al. pp. 392-393). | [design/spec.md (N5)](../../design/spec.md) |
| `b02` | glossary.md field. Aliases: other names people use; each points here only (N2, N7) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b03` | decision J1. Adopt this process and spec as the method: Adopt as version 1, revise after the first domain | [design/decisions.md (J1)](../../design/decisions.md) |
| `b04` | spec N8. Abbreviations are aliases. The full form is preferred and each well-known abbreviation is an alias, unless the abbreviation is "so well established that the full form ... is rarely used" (Z39.19 §6.6.3; Schober 3.4: DNA, LASER). | [design/spec.md (N8)](../../design/spec.md) |
| `b05` | process step 8. Agreement test (who: two independent raters). Two raters classify the same fresh sample independently, using only the files, and kappa is computed per facet (spec T8, with its rater rules). | [design/process.md (step 8)](../../design/process.md) |
| `b06` | glossary.md field. History: dated lines: added, renamed, split, ... with the reason (G4) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b07` | spec T3. Name form. Flags N4 and N7 breaches: "and"/"or", "non-"/"not", catch-alls, claim words ("type", "class"), plural endings, dates or status words, evaluative words from a short list (Schober Table 1; Ranganathan 1937 pp. 62-72). | [design/spec.md (T3)](../../design/spec.md) |
| `b08` | decision J3. File format: Strict markdown fields, SKOS names; generate SKOS/YAML only if a tool needs it (was open question 5) | [design/decisions.md (J3)](../../design/decisions.md) |
| `b09` | scope.md field. Status: `draft`, `in use`, or `retired`, with date | [design/spec.md (scope.md)](../../design/spec.md) |
| `b10` | spec S2. Pick the structure your knowledge supports. One dimension: a flat list. Two: a paradigm (grid). Three or more independent dimensions: facets (Denton §§1.1-1.2; Kwasnik pp. 33-42). | [design/spec.md (S2)](../../design/spec.md) |
| `b11` | spec D3. Example. A link to the clearest real case in the repo, kept out of the definition and in its own field (Seppälä 9.2; `skos:example`, SKOS §7). | [design/spec.md (D3)](../../design/spec.md) |
| `b12` | glossary.md field. Status: `candidate`, `approved`, or `deprecated` (G3) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b13` | process step 0. Decide to start, and check for reuse (who: Jonathan). Start only when the domain is being worked in, and run the steps inside that work, not as a separate exercise (J10). | [design/process.md (step 0)](../../design/process.md) |
| `b14` | spec T4. Definition form. Starts "A/An <label> is a"; names its genus; does not contain its own label after "is a" (circularity); no "usually", "generally", "e.g." (Seppälä et al. guidelines 3, 7, 9.1, 9.2). The genus matches the Broader term where one is given (OBO Foundry). | [design/spec.md (T4)](../../design/spec.md) |
| `b15` | decision J4. Singular or plural labels: Singular; close open question 2 | [design/decisions.md (J4)](../../design/decisions.md) |
| `b16` | glossary.md field. Facet: the facet it is a value of | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b17` | spec G3. Status. `candidate` (proposed, usable, not yet agreed), `approved`, or `deprecated` (kept for lookup, points to its replacement). Candidates are marked so they cannot be mistaken for agreed terms (Z39.19 §11.1.6). | [design/spec.md (G3)](../../design/spec.md) |
| `b18` | spec S1. Purpose first. No facet or term without a written purpose and competency questions to test it against. | [design/spec.md (S1)](../../design/spec.md) |
| `b19` | scope.md field. Owner: the person who settles disputes and can veto any change; agents approve changes that pass the checks (G1) | [design/spec.md (scope.md)](../../design/spec.md) |
| `b20` | decision J15. Default mapping between contexts: `closeMatch`; `exactMatch` only for real identity (proposal 7) | [design/decisions.md (J15)](../../design/decisions.md) |
| `b21` | process step 1. Frame: write `scope.md` (who: Jonathan, with a model drafting). Write every field of `scope.md` (spec §2) before collecting any terms. The format and structure are settled first because they decide what gets recorded (Z39.19 §11.1.2, p. 91). Purpose: one sentence. | [design/process.md (step 1)](../../design/process.md) |
| `b22` | spec T13. New words. Count new terms that appear in the repo without a glossary entry, and items that went to Unsorted. Machine-assisted candidate finding and frequency counts are standard (Z39.19 §11.1.3.4). | [design/spec.md (T13)](../../design/spec.md) |
| `b23` | scope.md field. Out of scope: what this context does not cover | [design/spec.md (scope.md)](../../design/spec.md) |
| `b24` | spec T7. Fresh-sample classification. Classify items that were not used to build the taxonomy. Every item gets a value in every facet, or goes to Unsorted with a note (Denton §2.3 steps 4, 6-7: "Go back through the steps until you are able to classify everything"). | [design/spec.md (T7)](../../design/spec.md) |
| `b25` | decision J12. Abbreviations: Full form preferred, abbreviation as alias unless the full form is rarely used (proposal 4) | [design/decisions.md (J12)](../../design/decisions.md) |
| `b26` | facets.md field. Unsorted: items waiting for a value, with links, and the date each arrived | [design/spec.md (facets.md)](../../design/spec.md) |
| `b27` | spec N3. Concepts before words. First decide what the name must carry, then the words, then the name (Feitelson et al. §§IV-V: names built this way were judged better two-to-one). | [design/spec.md (N3)](../../design/spec.md) |
| `b28` | spec G6. A rename is a model change. Update the glossary, the aliases and every use in the repo in the same commit: "a change in the language is a change to the model" (Evans pp. 3-4). | [design/spec.md (G6)](../../design/spec.md) |
| `b29` | process step 6. Name and define (who: model drafts and approves, Jonathan can veto). For each concept, in this order (N3: concepts, then words, then the name, Feitelson et al. §§IV-V): Write what the concept is, in a draft definition (D1) and scope note (D2). A name can only be judged against an agreed concept (Deissenboeck and Pizka pp. | [design/process.md (step 6)](../../design/process.md) |
| `b30` | glossary.md field. Replaced by: the ID(s) that replace a deprecated term (G5) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b31` | decision J2. Where a domain's taxonomy files live: Centrally, in this repo, `domains/<name>/`; each domain repo links to it | [design/decisions.md (J2)](../../design/decisions.md) |
| `b32` | spec C1. One glossary per bounded context. Inside a context, one meaning per word; across contexts the same word may mean different things if the map says so (Evans pp. 2-4). No term appears as a preferred label in two contexts unless mapped (OBO Foundry, "A collaborative experiment": "orthogonal"). | [design/spec.md (C1)](../../design/spec.md) |
| `b33` | scope.md field. Ending conditions: the tests in §9 with their target values | [design/spec.md (scope.md)](../../design/spec.md) |
| `b34` | spec N4. Form. A noun or noun phrase (Z39.19 §6.4); singular (Schober Table 1, 2.3; allowed by Z39.19 §6.5.1.1; one choice used consistently, Noy and McGuinness §6.2; J4); lower-case unless a proper noun or acronym (Schober Table 1, 4.1); spaces between words (Schober 3.3); full words (Schober 3.4; full words gave 19% faster comprehension than abbreviations or letters, Hofmeister et al., abstract); no articles (Schober 1.1); no "and" or "or" (Schober 2.2); no negation (Schober 2.4); no "type", "class", "kind" or similar claims (Schober 1.3); no status, version or date (Schober 1.4); no level or position encoded in the name. | [design/spec.md (N4)](../../design/spec.md) |
| `b35` | spec T10. Competency questions. Each question in `scope.md` can be answered using the facets and glossary (Noy and McGuinness, Step 1 and §4). | [design/spec.md (T10)](../../design/spec.md) |
| `b36` | facets.md field. Question: the question this facet answers about an item ("Who starts it?") | [design/spec.md (facets.md)](../../design/spec.md) |
| `b37` | decision J14. What "agent" means in the prompts glossary: Decide first; treat "agent" as a kind (a configured model program) and "sub-agent", "reviewer" as roles (proposal 6) | [design/decisions.md (J14)](../../design/decisions.md) |
| `b38` | process step 9. Name tests (who: a fresh reader, WordNet). Guess the name (spec T9): give each preferred label to a fresh reader (a person or a new model session with no glossary) and ask what it means. Wrong guesses send the label back to step 6 (Meszaros and Doble, "Evocative Pattern Name"). | [design/process.md (step 9)](../../design/process.md) |
| `b39` | spec S4. One kind of term per facet; roles never parent kinds. Things, properties, roles and happenings go in separate facets. The split follows the continuant / dependent continuant / occurrent grid of the OBO Foundry (OBO Foundry Table 1). | [design/spec.md (S4)](../../design/spec.md) |
| `b40` | facets.md field. Kind: `thing`, `property`, `role`, or `happening` (rule S4) | [design/spec.md (facets.md)](../../design/spec.md) |
| `b41` | spec T14. Does it change the work?. After a month of use, ask whether the names are used and whether the repo reads more consistently. A catalogue alone did not change what got built for Alexander; the process did (Gabriel pp. 57-60). Kundisch et al.'s ex post evaluation is not stored. | [design/spec.md (T14)](../../design/spec.md) |
| `b42` | decision J6. Who the two raters are: Two model families (for example Claude and another vendor's model) | [design/decisions.md (J6)](../../design/decisions.md) |
| `b43` | glossary.md field. Related: IDs of associated terms, never also broader (T1) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `b44` | spec T12. Alias drift. Count aliases and deprecated labels used in new docs in place of the preferred label; agents and people should use one language "in diagrams, writing, and especially speech" (Evans pp. 3-4). A rising count means the preferred name is losing: review it under N6. | [design/spec.md (T12)](../../design/spec.md) |
| `b45` | process step 10. Adopt (who: agent approves, Jonathan can veto). When the ending conditions hold (T7, T8, T10, T11 at their targets, T1 to T6 clean), an agent approves under spec G1 and tells Jonathan, who can veto (J8): terms move from `candidate` to `approved` (Z39.19 §11.1.6) and `scope.md` status becomes "in use". | [design/process.md (step 10)](../../design/process.md) |
| `b46` | spec D2. Scope note. Say what is included and excluded and how the term differs from near neighbours; a scope note should "state the chosen meaning of a term" and can name meanings deliberately excluded (Z39.19 §6.2.2). | [design/spec.md (D2)](../../design/spec.md) |
| `b47` | facets.md field. Values: the IDs of its values, in a stated order; each value has a glossary entry | [design/spec.md (facets.md)](../../design/spec.md) |
| `b48` | decision J5. Agreement target: κ ≥ 0.6 on every facet | [design/decisions.md (J5)](../../design/decisions.md) |

## Bare-facet test (10)

Used once in step 5, to test the facet list before any glossary entry existed.

| ID | Item | From |
|---|---|---|
| `t01` | spec T5. Kinds. No `role` or `happening` term is the broader term of a `thing` term (OntoClean §§8.2-8.3). | [design/spec.md (T5)](../../design/spec.md) |
| `t02` | facets.md field. Principle: the single characteristic of division used | [design/spec.md (facets.md)](../../design/spec.md) |
| `t03` | spec C3. Mappings, with `closeMatch` as the default. Links between contexts use SKOS mapping properties (SKOS §10). `exactMatch` is transitive (SKOS §10.4, S45) and means the concepts "can be used interchangeably" (SKOS §10.1), so a chain across three repos would equate the ends. | [design/spec.md (C3)](../../design/spec.md) |
| `t04` | spec N6. Stable IDs, current labels. The ID never changes. The label follows current usage (Ranganathan 1937 pp. 62-72, Canon of Currency: "some arrangement by which the terms can be changed over to current ones"; Spiteri's Currency, Denton §2.2). | [design/spec.md (N6)](../../design/spec.md) |
| `t05` | process step 4. Find the facets (who: model proposes, Jonathan decides). Compare unlike items to find the dimensions they share: constant comparison, from grounded theory, which Star pairs with facet analysis as two ways of representing "vernacular words and processes, empirically discovered" (Star 1998 pp. 218-224). | [design/process.md (step 4)](../../design/process.md) |
| `t06` | glossary.md field. Warrant: where the term is used: files, counts, or "Jonathan's words" (N2) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `t07` | decision J18. A name for the system: None proposed yet (was open question 4). It should follow N4 to N8 | [design/decisions.md (J18)](../../design/decisions.md) |
| `t08` | spec G2. Anyone proposes; an agent approves under G1. Any person or agent may propose a term or a change, with its reason and evidence. The proposal is recorded as a `candidate` (Z39.19 §§11.1.6, 11.3.1.1-11.3.1.2, pp. 93-97). | [design/spec.md (G2)](../../design/spec.md) |
| `t09` | scope.md field. Readers: who uses the names, in priority order, and whose needs win when they conflict | [design/spec.md (scope.md)](../../design/spec.md) |
| `t10` | spec N7. Reticence. No evaluative words in names ("legacy", "hacky", "minor", "bad", "proper"): terms should be "purely descriptive and not opinionative" (Ranganathan 1937 pp. 62-72, Canon of Reticence). Definitions follow the same rule (Seppälä et al. guideline 9.4). | [design/spec.md (N7)](../../design/spec.md) |

## Round-1 test (30)

Fresh items for round 1 (steps 7 and 8). Not read while building.

| ID | Item | From |
|---|---|---|
| `r01` | decision J17. Rules whose best source is not stored: Keep them marked and in force; check each when the source is fetched (Nickerson 2013, Kundisch 2022, Cohen 1960, Berlin 1992, biology codes, *A Pattern Language*) | [design/decisions.md (J17)](../../design/decisions.md) |
| `r02` | glossary.md field. Near miss: something it looks like but is not, and why (D4) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `r03` | spec T6. Facets. Every facet value has a glossary entry; no value is empty in the latest classification (an empty cell asks whether a concept or an axis is wrong, Kwasnik pp. | [design/spec.md (T6)](../../design/spec.md) |
| `r04` | process step 7. Classify fresh items, fix, repeat (who: model). Classify a fresh test sample using only `facets.md` and `glossary.md`. Note every hesitation; put items that fit no value in the facet's Unsorted list (S6). | [design/process.md (step 7)](../../design/process.md) |
| `r05` | spec T8. Agreement. Two raters classify the same fresh items independently, using only `facets.md` and `glossary.md`. Compute Cohen's kappa per facet. Target: κ ≥ 0.6 on every facet (J5). Disagreements show where the vocabulary is unclear (Z39.19 §11.2.2, pp. | [design/spec.md (T8)](../../design/spec.md) |
| `r06` | scope.md field. Neighbours: other contexts it touches, and the map file | [design/spec.md (scope.md)](../../design/spec.md) |
| `r07` | decision J7. Sample sizes: Build from 30-60 items, test on 30 fresh items per round; light version under ~30 items | [design/decisions.md (J7)](../../design/decisions.md) |
| `r08` | spec T1. Integrity. Every ID unique; every record has all required fields; every referenced ID exists ("no cross-references ... | [design/spec.md (T1)](../../design/spec.md) |
| `r09` | glossary.md field. Scope: what it includes and excludes, especially at the edges (D2) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `r10` | spec S5. Add a level only when it says something new. A narrower term is added "only when there is something that we can say about this class that we cannot say about the superclass" (Noy and McGuinness §4.4). | [design/spec.md (S5)](../../design/spec.md) |
| `r11` | process step 5. Test the bare facet list (who: model). Before writing any glossary entries, classify about 10 test items with the facet names and a one-line description of each value, and add, drop or split facets now. | [design/process.md (step 5)](../../design/process.md) |
| `r12` | decision J11. No evaluative words in names: Adopt as N7 (proposal 3) | [design/decisions.md (J11)](../../design/decisions.md) |
| `r13` | scope.md field. Purpose: one sentence: what the taxonomy is for, and the one question every facet must help answer | [design/spec.md (scope.md)](../../design/spec.md) |
| `r14` | spec G4. Named operations only. Every change is one of: add, rename (label changes, ID stays), split, merge, move (change broader or facet), redefine, deprecate. Each is logged in `changelog.md` and in the term's History with date and reason (Z39.19 §§11.3.1.2, 11.3.2.2, pp. 96-97). | [design/spec.md (G4)](../../design/spec.md) |
| `r15` | spec D4. Near miss. One thing it is easily confused with, and why it is not it: the edge of the concept, where raters disagree. TnT-LLM's raters disagreed mostly at the boundaries between neighbouring labels (Wan et al. App. | [design/spec.md (D4)](../../design/spec.md) |
| `r16` | glossary.md field. Broader: the ID of the nearest is-a parent (S5) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `r17` | spec N2. Harvest, then choose. Collect the words already in use, with counts, before choosing. Choose the preferred label by warrant: the words in the content (literary warrant), the words of the readers (user warrant), and the owner's needs (organizational warrant) (Z39.19 §5.3.5). | [design/spec.md (N2)](../../design/spec.md) |
| `r18` | decision J13. Find facets by comparison, and test the bare facet list early: Adopt both as process steps 4 and 5 (proposals 1 and 2) | [design/decisions.md (J13)](../../design/decisions.md) |
| `r19` | glossary.md field. Example: a link to the clearest real case in the repo (D3) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `r20` | process step 3. Harvest the words (who: model). List every term used for the things in the build sample, and in Jonathan's own words about the domain. Count each term's uses across the repo. | [design/process.md (step 3)](../../design/process.md) |
| `r21` | spec G1. Agents approve, Jonathan can veto. (J8, decided by Jonathan 2026-11-25). An agent may approve a change, or a term's move from `candidate` to `approved`, when every mechanical test (T1-T6) passes and the change is logged with its reason. | [design/spec.md (G1)](../../design/spec.md) |
| `r22` | spec G5. Deprecate, never delete. A deprecated term keeps its record, ID, labels and history, and its Replaced by field names the term(s) to use instead; looking up an old label finds the deprecated record, which points on. | [design/spec.md (G5)](../../design/spec.md) |
| `r23` | glossary.md field. Hidden: misspellings and old forms, kept for search, never shown as advice | [design/spec.md (glossary.md)](../../design/spec.md) |
| `r24` | decision J16. Replace "confidence" with a status: `candidate` / `approved` / `deprecated` | [design/decisions.md (J16)](../../design/decisions.md) |
| `r25` | spec N1. One concept, one preferred name; one name, one concept. inside a context. Names must map to concepts one-to-one, with no homonyms and no synonyms (Deissenboeck and Pizka pp. | [design/spec.md (N1)](../../design/spec.md) |
| `r26` | scope.md field. Competency questions: 5 to 15 questions the taxonomy must let you answer | [design/spec.md (scope.md)](../../design/spec.md) |
| `r27` | spec T9. Guess the name. Show someone who has not seen the glossary a preferred label and ask what it means. A wrong guess means the name or the concept needs work (Meszaros and Doble, "Evocative Pattern Name"). | [design/spec.md (T9)](../../design/spec.md) |
| `r28` | process step 11. Put into use (who: model). Link `domains/<name>/glossary.md` in this repo from the domain repo's `CLAUDE.md` / `AGENTS.md` (by its GitHub URL) so agents there load it and use preferred labels (J2). | [design/process.md (step 11)](../../design/process.md) |
| `r29` | decision J8. Who has the final say: Agents approve, Jonathan can veto: an agent approves changes that pass T1-T6 with a logged reason; Jonathan is the named owner, reviews the changelog, can reverse anything and settles disputes | [design/decisions.md (J8)](../../design/decisions.md) |
| `r30` | facets.md field. Agreement: the latest kappa, the date, the sample size, and who rated | [design/spec.md (facets.md)](../../design/spec.md) |

## Held for round 2 (18)

Not read. For round 2, topped up from `design/method-v1.1.md` (rules M1 to M7) and the decisions
added since commit `c4fa001`. Re-running `sample.py` on a later commit draws a different
set: run it at `c4fa001` to reproduce this one.

| ID | Item | From |
|---|---|---|
| `h01` | spec D1. Genus-differentia. "A <term> is a <genus> that <differentia>." One genus, the nearest one; no categorizer words; no "and" or "or" in the genus; no circularity; no "usually" or "generally"; no examples or lists inside the definition; no evaluative or indexical words (Seppälä et al. | [design/spec.md (D1)](../../design/spec.md) |
| `h02` | spec C2. Small shared kernel. Terms that are truly the same across contexts go in a shared kernel: "Keep this kernel small", and it "shouldn't be changed without consultation" (Evans p. 31). A kernel term is a boundary object: "plastic enough to adapt to local needs ... | [design/spec.md (C2)](../../design/spec.md) |
| `h03` | scope.md field. Context: the repo or area this vocabulary governs, and its short context name | [design/spec.md (scope.md)](../../design/spec.md) |
| `h04` | decision J19. Build the checker script: Yes, after J1 and J3: a small script for T1 to T6 and T12, run in each domain repo | [design/decisions.md (J19)](../../design/decisions.md) |
| `h05` | spec D5. Kind and rigidity. Each term states its Kind. A role (sub-agent, reviewer) or a phase (draft, released) is never the broader term of a kind, and "can be a" is not "is a": OntoClean's own example wrongly puts *Agent* above *Animal*; "animals can be agents" (OntoClean §8.3). | [design/spec.md (D5)](../../design/spec.md) |
| `h06` | process step 12. Maintain (who: owner). Changes follow spec §9: anyone proposes a `candidate`, an agent approves it under spec G1 with Jonathan able to veto, every change is a named operation in `changelog.md` and the term's history, and nothing is deleted (Z39.19 §§11.3-11.3.2, pp. 96-97). | [design/process.md (step 12)](../../design/process.md) |
| `h07` | glossary.md field. Definition: one sentence, genus-differentia (D1) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `h08` | spec S6. No permanent "other". Each facet has an Unsorted list, reviewed every round. A growing one means the structure is wrong: "The sure sign of a 'premature' hierarchical structure is the need for a 'miscellaneous' or 'other' category" (Kwasnik pp. | [design/spec.md (S6)](../../design/spec.md) |
| `h09` | spec T11. Heuristic review. At the end of a build round, check the evaluation questions of Z39.19 §11.2.2: unmarked synonyms, missing facets, out-of-date terms, consistent term form, quality of definitions and scope notes. | [design/spec.md (T11)](../../design/spec.md) |
| `h10` | glossary.md field. Kind: `thing`, `property`, `role`, or `happening` (S4) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `h11` | decision J10. When to run the process: Only when a domain is being worked in, inside that work; review monthly while active (proposal 9) | [design/decisions.md (J10)](../../design/decisions.md) |
| `h12` | spec S3. One principle per facet. Each facet uses a single characteristic of division, and its values are mutually exclusive and jointly exhaustive for the items in scope. | [design/spec.md (S3)](../../design/spec.md) |
| `h13` | facets.md field. Order: the order used for the values (by sequence, size, simple to complex, ...) | [design/spec.md (facets.md)](../../design/spec.md) |
| `h14` | process step 2. Collect the samples (who: model, checked by Jonathan). Collect "a representative sample of the entities. In a large domain, get enough to cover all foreseen possibilities. In a small domain, use the entire domain" (Denton §2.3 step 1). Items are files, sections or rules, whatever the competency questions are about. | [design/process.md (step 2)](../../design/process.md) |
| `h15` | spec G7. Review. Review the unsorted lists and candidates at intervals set by how fast terms change (Z39.19 §11.3.1, p. 96), and at least whenever the domain is being actively worked on (J10). Shared-kernel changes need every affected context's owner (Evans p. 31). | [design/spec.md (G7)](../../design/spec.md) |
| `h16` | decision J9. Whose needs win: Jonathan's first, then the agents' (proposal 8) | [design/decisions.md (J9)](../../design/decisions.md) |
| `h17` | glossary.md field. Matches: see `map.md` (C3) | [design/spec.md (glossary.md)](../../design/spec.md) |
| `h18` | spec T2. Labels. No label (preferred, alias or hidden) used twice in the context, after folding case and hyphens, counting deprecated records too (G5 keeps an old label on its deprecated record only); every deprecated record has a Replaced by that exists (SKOS S13-S14; potential duplicates, Z39.19 §11.4.6). | [design/spec.md (T2)](../../design/spec.md) |
