# Decisions for Jonathan

**In one line**: nineteen choices that the process and spec depend on and that only
Jonathan can make; the six needed before the first domain were decided on 2026-11-25,
and thirteen can wait.

**Status**: six decided (J1, J2, J5-J8), thirteen open, 2026-11-25.
[`process.md`](./process.md) and [`spec.md`](./spec.md) follow the decisions, and follow
the recommendation for each open row so they read as a whole. Rejecting an open
recommendation means editing the rule or step named in its row. These include the five
open questions in [`README.md`](./README.md#open-questions) and the nine proposals in
[`source-check-2026-11-25.md`](./source-check-2026-11-25.md); this page supersedes both
lists.

Each row gives the recommendation, the stored source it rests on (paths are in
[`spec.md`](./spec.md#sources-cited)), and where it lands.

## Decided 2026-11-25 (interview in the project thread)

| # | Decision | Jonathan's answer | Was recommended | What changed |
|---|---|---|---|---|
| J1 | Adopt this process and spec as the method | **Adopt as version 1**, revise after the first domain | same | spec and process status now "version 1, adopted" |
| J2 | Where a domain's taxonomy files live | **Centrally, in this repo**, `domains/<name>/`; each domain repo links to it | in each repo's `taxonomy/` (Evans p. 2) | spec §1 and process step 11. Trade-off recorded in spec §1: the vocabulary sits one link from the work, so T12 (alias drift) is the check that agents use it |
| J5 | Agreement target | **κ ≥ 0.6 on every facet** | same (Wan et al. §5.3.2, Table 2) | none; already in spec T8 |
| J6 | Who the two raters are | **Two model families** (for example Claude and another vendor's model) | Jonathan plus a model | spec T8 and process steps 8 and the light version. With no human rater, T9 (fresh reader) and Jonathan's veto are the human checks |
| J7 | Sample sizes | **Build from 30-60 items, test on 30 fresh items per round**; light version under ~30 items | same; still no stored source (Tullis and Wood 2004 in `to-fetch.md`) | none |
| J8 | Who has the final say | **Agents approve, Jonathan can veto**: an agent approves changes that pass T1-T6 with a logged reason; Jonathan is the named owner, reviews the changelog, can reverse anything and settles disputes | Jonathan approves every change | spec G1, G2 and the `scope.md` Owner field; process steps 1, 3, 6, 10, 12 and the tables. Departs from Z39.19 §11.3.1.1 (editor reviews each term); the veto and logged reasons keep it checkable |

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
