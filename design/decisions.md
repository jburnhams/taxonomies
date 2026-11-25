# Decisions for Jonathan

**In one line**: nineteen choices that the process and spec depend on and that only
Jonathan can make; six are needed before the first domain is built, the rest can wait.

**Status**: open, 2026-11-25. [`process.md`](./process.md) and [`spec.md`](./spec.md)
are written as if every recommendation below were accepted, so they read as a whole.
Rejecting one means editing the rule or step named in its row. These include the five
open questions in [`README.md`](./README.md#open-questions) and the nine proposals in
[`source-check-2026-11-25.md`](./source-check-2026-11-25.md); this page supersedes both
lists.

Each row gives the recommendation, the stored source it rests on (paths are in
[`spec.md`](./spec.md#sources-cited)), and where it lands.

## Needed before the first domain

| # | Decision | Recommended | Rests on | Lands in |
|---|---|---|---|---|
| J1 | Adopt this process and spec as the method | Yes, as version 1, to be revised after the first domain | the whole of `spec.md` and `process.md` | everything |
| J2 | Where a domain's taxonomy files live | In each domain repo, `taxonomy/` (was open question 1) | Evans p. 2: a bounded context's boundary includes "code bases"; agents read files in their own repo | spec §1 |
| J5 | Agreement target | κ ≥ 0.6 on every facet (was 0.7, open question 3) | Wan et al. §5.3.2 and Table 2: expert annotators reached 0.553 and >0.6; their scale calls >0.6 substantial. ⚠ Cohen 1960 and Landis and Koch not stored | spec T8, process step 8 |
| J6 | Who the two raters are | Jonathan plus a model, or two different model families; not two sessions of one model | Z39.19 §11.2.2 (several indexers); Wan et al. §5.3.2 (GPT-4 as a reliable single-label rater). Same-model blind spots: reasoning, no stored source | spec T8 |
| J7 | Sample sizes | Build: 30-60 items or the whole domain; test: at least 30 fresh items per round; light version under ~30 items | Denton §2.3 step 1 gives the principle ("enough to cover all foreseen possibilities"); the numbers have **no stored source** (Tullis and Wood 2004 is in `to-fetch.md`) | process steps 2, 8 |
| J8 | Owner of each glossary | Jonathan, for every context, until he names someone else (proposal 5) | Z39.19 §11.3 ("identify the individual responsible"); OBO Foundry Table 2 (custodians); Medin and Ortony pp. 184-185 | spec G1 |

## Can wait until it comes up

| # | Decision | Recommended | Rests on | Lands in |
|---|---|---|---|---|
| J3 | File format | Strict markdown fields, SKOS names; generate SKOS/YAML only if a tool needs it (was open question 5) | Gruber §1 (names plus prose first); SKOS §§5, 7, 10 (field names); Z39.19 §11.1.2 (fix the format before collecting terms) | spec §1 |
| J4 | Singular or plural labels | Singular; close open question 2 | Schober Table 1, 2.3; Z39.19 §6.5.1.1 allows it; Noy and McGuinness §6.2: pick one and keep it | spec N4 |
| J9 | Whose needs win | Jonathan's first, then the agents' (proposal 8) | Hjørland §4.2c: "can never be neutral" | spec §2, process step 1 |
| J10 | When to run the process | Only when a domain is being worked in, inside that work; review monthly while active (proposal 9) | Gabriel 2023 App. E.2 (Alexander's 1971 preface); Gabriel 1996 pp. 57-60 | process steps 0, 12; spec G7 |
| J11 | No evaluative words in names | Adopt as N7 (proposal 3) | Ranganathan 1937 pp. 62-72, Canon of Reticence; Seppälä 9.4 | spec N7, T3 |
| J12 | Abbreviations | Full form preferred, abbreviation as alias unless the full form is rarely used (proposal 4) | Z39.19 §6.6.3; Schober 3.4; Hofmeister abstract; Lawrie abstract | spec N8 |
| J13 | Find facets by comparison, and test the bare facet list early | Adopt both as process steps 4 and 5 (proposals 1 and 2) | Star 1998 pp. 218-224; Kwasnik p. 41 | process steps 4, 5 |
| J14 | What "agent" means in the prompts glossary | Decide first; treat "agent" as a kind (a configured model program) and "sub-agent", "reviewer" as roles (proposal 6) | OntoClean §8.3: *Agent* as a role, and the error of putting it above kinds | process step 1; spec D5 |
| J15 | Default mapping between contexts | `closeMatch`; `exactMatch` only for real identity (proposal 7) | SKOS §10.4 S45 (`exactMatch` is transitive), §10.1 | spec C3 |
| J16 | Replace "confidence" with a status | `candidate` / `approved` / `deprecated` | Z39.19 §11.1.6 (candidate terms), §11.3.2.1a (retained terms). Alexander's asterisks are not stored | spec G3 |
| J17 | Rules whose best source is not stored | Keep them marked ⚠ and in force; check each when the source is fetched (Nickerson 2013, Kundisch 2022, Cohen 1960, Berlin 1992, biology codes, *A Pattern Language*) | `to-fetch.md`; the ⚠ lines in `spec.md` and `process.md` | both |
| J18 | A name for the system | None proposed yet (was open question 4). It should follow N4 to N8 | spec N rules | — |
| J19 | Build the checker script | Yes, after J1 and J3: a small script for T1 to T6 and T12, run in each domain repo | Z39.19 §11.4.6 (error checking a system "should" do) | spec §10, process step 11 |

## What changed from the first draft

- **Kappa target 0.7 → 0.6** (J5). Reading TnT-LLM's agreement tables showed expert
  human annotators below 0.7 on one of two taxonomies.
- **Depth cap dropped** (spec S5). "At most three levels" rested on Berlin 1992, which is
  not stored; it is replaced by Noy and McGuinness's sibling and new-level rules.
- **Confidence levels → status** (J16). Alexander's asterisks are not stored; Z39.19's
  candidate terms are, and they do the same job.
- **Governance and tests are now written out** (spec §§9-10). Z39.19 §11 (construction,
  testing, maintenance), not read in the first pass, supplies most of them: candidate
  terms, history notes, merge and split, deprecation, and the error checks.
