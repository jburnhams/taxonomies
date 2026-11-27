# Changelog

All notable changes, grouped by day, newest first. See [`CLAUDE.md`](./CLAUDE.md).

## 2026-11-27

**Ran prompts stage 3 round 1 (control area) and its name test** (kit `9d2b864`, 30 items,
same three raters). On the 24 in-area items: Fleiss' κ target 0.83, response 0.80;
openai-gemini 0.75, 0.70. Both pass.

- `domains/prompts/stage-3/rounds/round-1/answers/`: **new**. Each rater's CSV and raw
  reply with run details. `results.md`: **new**, the three kappa.py runs.
- `domains/prompts/stage-3/rounds/round-1/name-test/guesses-openai.md`, `guesses-gemini.md`: **new**.

**Started stage 3 of the prompts taxonomy, the control area, with a term backlog and a revision pass (branch `claude/project-thread-oneclm`)**. Jonathan said yes to stage 3 and asked that each stage add the new terms a decided concept opens, and clarify or break earlier entries where needed. That became proposal M8, and stage 3 is the first to follow it.

- `design/method-v1.1.md`: new M8 (term backlog, revision pass by G4 operations, retest of changed entries), with Z39.19 §11.3.1 and Denton §2.3 step 7 as warrant.
- `design/decisions.md`: J27 (proposed).
- `domains/taxonomies/glossary.md`, `changelog.md`: `term-backlog` and `revision-pass` as `candidate` terms.
- `domains/prompts/backlog.md`: **new**, 16 rows taken by stage 3 and 8 open.
- `domains/prompts/stage-3/`: **new**. `sample3.py`, `items.csv`, `samples.md` (104 items from 35 files at prompts `e7d4fb2`), `count3.py`, `harvest.md`, `revision.md` (seven earlier entries changed, R1-R7), and the round-1 kit with a name test for 33 labels in `rounds/round-1/`.
- `domains/prompts/facets.md`: proposed stage-3 sets A (`target`, `response`), B and C (adds `enforcement`), and a bare test on ten items.
- `domains/prompts/glossary.md`: 10 value entries and 16 terms for the control area, all `candidate`. `compaction`, `approval`, `permission-mode`, `sandbox` clarified; `steer` split (new `system-reminder`); `handoff` and `precedence` lose the homonym aliases "escalation" and "authority" to new entries. All seven are `candidate` again until the name test. The stage-2 `precedence` alias "authority" clash was found by T2 when `authority` was drafted.
- `domains/prompts/scope.md`: stage 3 row, competency questions 21-27, T9 now covers entries changed by a revision pass.
- `domains/prompts/changelog.md`: the operations above.

## 2026-11-26

**Adopted stage 2 of the prompts taxonomy, the context area (branch `claude/project-thread-oneclm`, PR #15)**. Jonathan chose facet set A (operation, content, reach). With that, every ending condition holds on round 2.

- `domains/prompts/facets.md`, `scope.md`: stage 2 is `in use`, set A is marked chosen.
- `domains/prompts/glossary.md`: the stage-2 values and terms, and the changed `memory` and `context-file`, are `approved`. `work-note` stays `candidate`.
- `domains/prompts/changelog.md`: the decide and adopt operations.

**Scored the prompts stage-2 name test and reviewed stage 2 (branch `claude/project-thread-oneclm`, PR #15)**. Both fresh readers passed (94% and 97%). All seven competency questions are answered, and the heuristic review found nothing. Stage 2 waits only on Jonathan's choice of facet set.

- `domains/prompts/stage-2/rounds/round-2/name-test/results.md`, `review.md`: **new**.
- `domains/prompts/glossary.md`: `note` relabelled "work note"; a near miss added to `framing`.
- `domains/prompts/changelog.md`: the operations above.

**Ran the prompts stage 2 name test (T9)** with the two non-Claude readers (GPT-6.2-Astra
via `codex exec`, Gemini 4 Carbon High via `agy -p`), same isolation as the rounds.

- `domains/prompts/stage-2/rounds/round-2/name-test/guesses-openai.md`, `guesses-gemini.md`:
  **new**. Each reply verbatim, with run details at the top.

**Prompts stage-2 round 2 passes; context terms drafted; name-test prompt (branch `claude/project-thread-oneclm`, PR #15)**. On the 28 in-area items, Fleiss' κ is operation 0.89, content 1.00 and reach 0.84, and the non-Claude pair scores 0.83, 1.00 and 0.83. Every facet passes. Jonathan's choice of facet set is still open.

- `domains/prompts/facets.md`: round-2 agreement lines and status.
- `domains/prompts/glossary.md`: 16 new context-area `candidate` terms; `memory` and `context-file` changed (see the domain changelog).
- `domains/prompts/stage-2/rounds/round-2/name-test/prompt.md`: **new**.
- `domains/prompts/changelog.md`: the operations above.

**Ran prompts stage 2 round 2 with three raters** (kit `a73ecfd`, 30 items). Every facet
passes on the 28 in-area items: Fleiss' κ operation 0.89, content 1.00, reach 0.84;
openai-gemini 0.83, 1.00, 0.83.

- `domains/prompts/stage-2/rounds/round-2/answers/`: **new**. Each rater's CSV and raw
  reply with run details. `results.md`: **new**, the three kappa.py runs.

**Scored prompts stage-2 round 1 and prepared round 2 (branch `claude/project-thread-oneclm`, PR #15)**. On the 27 in-area items, `operation` and `content` pass both conditions. `reach` passes Fleiss' κ (0.68) but fails the non-Claude pair (0.53), because built-in prompts had no value and raters guessed how widely an unstated store is shared.

- `domains/prompts/facets.md`, `glossary.md`: new `reach` value `built-in-scope`, two rules in the `reach` principle, agreement lines.
- `domains/prompts/stage-2/rounds/round-1/results.md`: fixes table.
- `domains/prompts/stage-2/rounds/round-2/`: **new**. Round-2 kit with items `ch01`-`ch30`.
- `tools/kappa.py`: an empty sample after `--where` is reported instead of raising (Codex review on PR #15).

**Ran prompts stage 2 round 1 (context area) with three raters** (kit `258f560`, 30 items,
same models as stage 1). On the 27 in-area items: Fleiss' κ operation 0.82, content 0.88,
reach 0.68; openai-gemini 0.84, 0.82, 0.53 (reach misses).

- `domains/prompts/stage-2/rounds/round-1/answers/`: **new**. Each rater's CSV and raw
  reply with run details. `results.md`: **new**, the three kappa.py runs.

**Started stage 2 of the prompts taxonomy: the context area (branch `claude/project-thread-oneclm`)**. Jonathan said go on stage 2. I chose the context area over control, because it has the most words in the repo and its own classification to start from (memory levels). This adds the samples, the term harvest, three proposed facet sets for him to choose from, candidate entries for the recommended set, and the round-1 rater kit.

- `domains/prompts/stage-2/`: **new**. `sample2.py`, `samples.md`, `items.csv` (130 items), `harvest.md`, and `rounds/round-1/` (README, items, `make_prompts.py`, three prompts).
- `domains/prompts/facets.md`: "Stage 2" section with sets A-C and the bare-facet test.
- `domains/prompts/glossary.md`: 12 `candidate` entries for set A's values (`supply`, `framing`, `reduction`, `recording`; `instruction-text`, `kept-knowledge`, `run-history`; five `reach` values).
- `domains/prompts/scope.md`: stage table and competency questions 14-20.
- `tools/kappa.py`: `--where col=value` (with `--ref` voters) scores only the items a majority puts in the area. The stage-1 round-3 figures reproduce unchanged.
- `domains/prompts/changelog.md`: the operations above.

**Moved stored source copies to the private `taxonomies-sources` repo (branch `claude/project-thread-plf8yz`)**.
This repo is now public, and the 93 stored files (24 PDFs, saved pages, figures, OCR and
extracted text in 32 source folders) were only allowed here while it was private. Jonathan
asked for them to go into the new private repo `jburnhams/taxonomies-sources`. They are
still in this repo's git history; no history rewrite was done.

- `sources/*/`: every file except `README.md` removed; the same paths now sit at the root
  of `taxonomies-sources` (`<slug>/<file>`).
- **new** `sources/stored-files.txt`: the list of those paths, so tools and the site can
  count stored copies without the private repo.
- `sources/*/README.md`: **Stored here** renamed **Stored**; folders with copies link to
  their folder in `taxonomies-sources`; "stored here" and "Drop a PDF here" now point there.
- `design/spec.md`, `design/process.md`, `design/method-v1.1.md`,
  `domains/prompts/samples.md`: 54 links to stored files now go to
  `https://github.com/jburnhams/taxonomies-sources/blob/main/...`.
- `tools/check_citations.py`: links into `taxonomies-sources` are checked against
  `stored-files.txt`, and against the files on disk when that repo is checked out beside
  this one (or at `$TAXONOMIES_SOURCES`).
- `site/generate.py`, `site/src/pages/docs.tsx`, `site/README.md`: the "Stored copy"
  count reads `stored-files.txt`; the page text says the copies are private.
- `CLAUDE.md`, `README.md`, `sources.md`, `to-fetch.md`: stored copies go in the private
  repo, never here.

**Adopted the taxonomies taxonomy after round 3 (branch `claude/project-thread-yet87g`, PR #12)**.
Round 3 (`check` only, 73 used items, indicative) passed: Fleiss' κ 0.73, non-Claude pair
0.75. Jonathan had chosen to adopt on this retest, so the domain is adopted (process step
10) and linked from this repo's `CLAUDE.md` (step 11).

- `domains/taxonomies/rounds/round-3/`: answers and `results.md` from the run on omarchy;
  this commit adds the reading.
- `domains/taxonomies/glossary.md`: all 57 terms `approved`, with a history line each.
- `domains/taxonomies/scope.md`: status `in use`; the ending conditions' results at adoption.
- `domains/taxonomies/facets.md`, `changelog.md`: agreement and the adopt operation.
- `CLAUDE.md`: new **Vocabulary** rule linking the glossary. `README.md`: domain listed.

**Ran taxonomies round 3 (check only) with three raters** (kit `cac7f1f`, 73 items, same
models). Check passes: Fleiss' κ 0.73, openai-gemini 0.75.

- `domains/taxonomies/rounds/round-3/answers/`: **new**. Each rater's CSV and raw reply.
  `results.md`: **new**, both kappa tables and the disagreement lists.

**Recorded Jonathan's choice of facets for the taxonomies taxonomy (branch `claude/project-thread-yet87g`)**.
He chose set A (`part`, `stage`, `check`), and to adopt `check` if the indicative round 3 reaches κ 0.6.

- `domains/taxonomies/facets.md`, `changelog.md`: the choice recorded.

**Taxonomies T10 and T11 review after rounds 1 and 2 (branch `claude/project-thread-yet87g`, PR #10)**.
Jonathan chose to adopt `check` if round 3 reaches κ 0.6; the review was done meanwhile.
The changelog lines were left out of the review's own commit (`bb6baaf`) and added here.

- `domains/taxonomies/rounds/round-2/review.md`: **new**. All twelve competency questions
  answered; one near-synonym linked; `owner-decision` empty in the round items, kept.
- `domains/taxonomies/glossary.md`: `script` gets Related `mechanical-check`.

**Scored taxonomies round 2 and the name test; redefined `check`'s `script`; built an indicative round 3 (branch `claude/project-thread-yet87g`, PR #10)**.
Round 2 (43 fresh items, ids removed) passed part (Fleiss' κ 0.94) and stage (0.84) but
failed check (0.55; non-Claude pair 0.45): raters split on whether "a program could check
it" means one does. Every fresh item is now used, so check is retested on used items.

- `domains/taxonomies/rounds/round-2/results.md`: the reading, fixes and name-test result added.
- `domains/taxonomies/glossary.md`: `script` and `judgement` redefined; `boundary` relabelled
  "neighbours" (ID kept) after all three fresh readers misread it; label choice 6 added.
- `domains/taxonomies/facets.md`, `scope.md`, `changelog.md`: agreement and status.
- `domains/taxonomies/rounds/round-3/`: **new**. `check` only, 73 used items, recorded as indicative.

**Ran taxonomies round 2 and the name test with three raters** (kit `7004a36`, 43 items,
same models as round 1). Fleiss' κ part 0.94, stage 0.84, check 0.55 (misses);
openai-gemini 0.97, 0.90, 0.45 (check misses). The name test ran in separate fresh sessions.

- `domains/taxonomies/rounds/round-2/answers/`: **new**. Each rater's CSV and raw reply.
  `results.md`: **new**, both kappa tables and the disagreement lists.
- `domains/taxonomies/rounds/round-2/name-test/guesses-{claude,openai,gemini}.md`: **new**.

**Scored taxonomies round 1, fixed `check`, built round 2 and the name test (branch `claude/project-thread-yet87g`, PR #10)**.
The three raters (Claude Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High) passed every facet:
Fleiss' κ part 1.00, stage 1.00, check 0.78; non-Claude pair 1.00, 1.00, 0.74. Part and
stage were probably easy because each item gave its own id, and 30 items is below M3's 35,
so round 2 removes the ids and uses 43 items.

- `domains/taxonomies/rounds/round-1/results.md`: the reading and the fixes table added.
- `domains/taxonomies/glossary.md`: `script`, `judgement`, `owner-decision` redefined.
- `domains/taxonomies/facets.md`, `scope.md`: agreement recorded; T8 target now 35 items (J22).
- `domains/taxonomies/sample.py`, `items-all.csv`, `samples.md`: `--top-up` draws 25 new items
  (M1-M7, J20-J26, spec §1's file table, the light version's steps) as set `s`.
- `domains/taxonomies/rounds/round-2/`: **new**. 43 items without their own ids, three
  prompts, the name test prompt (T9), README.
- `domains/taxonomies/changelog.md`: the operations above.

**Ran taxonomies round 1 with three raters** (kit `0db889f`, 30 items; Claude Opus 5.5,
GPT-6.2-Astra, Gemini 4 Carbon High, as in the prompts rounds). Every facet passes:
Fleiss' κ part 1.00, stage 1.00, check 0.78; openai-gemini 1.00, 1.00, 0.74.

- `domains/taxonomies/rounds/round-1/answers/`: **new**. Each rater's CSV and raw reply
  with run details. `results.md`: **new**, both kappa tables and the disagreement lists.

**Put the taxonomies taxonomy through the full process, to the round-1 kit (branch `claude/project-thread-yet87g`, PR #10)**.
Jonathan asked to "put the taxonomies taxonomy through full process". The draft sorted the
method's concepts; the full process needs items to sort, so the items became the method's
own rules, steps, file fields and decisions, and the facets were rebuilt for them. The
facet choice is put to Jonathan; work went ahead on the recommended set.

- `domains/taxonomies/scope.md`: rewritten (process step 1): items, purpose, twelve
  competency questions, ending conditions with three rater families.
- `domains/taxonomies/sample.py`, `items-all.csv`, `samples.md`: **new** (step 2). 106 items
  (48 build, 10 bare-facet test, 30 round 1, 18 held), seed 20261126, each kind spread
  evenly through the sets; steps carry their "Who" from the process's step table.
- `domains/taxonomies/harvest.md`: **new** (step 3). Counts over `design/` and `domains/ux/`,
  six synonym sets, nine homonyms (scope, round, kind, context, test, status, domain,
  review, check).
- `domains/taxonomies/facets.md`: rewritten (steps 4 and 5). Facets `part`, `stage`, `check`
  (set A of three); the draft facet `kind` retired. Bare-facet test on ten items, with five
  rules it produced.
- `domains/taxonomies/glossary.md`: ten new `candidate` values, stage scope notes
  rewritten, the four term kinds moved out of the facets, two more label choices. One
  correction: the alias entry cited N7 where it meant N1.
- `domains/taxonomies/rounds/round-1/`: **new**. 30 items, `make_prompts.py`, three
  shuffled prompts, README with the run and scoring steps. Raters not yet run.

**Added the explorer site, generated from the domain files, and drafted the method's own words as a domain (branch `claude/project-thread-yet87g`)**.
Jonathan asked for a GitHub Pages site with an overview and a way to explore each taxonomy
down to the raw data behind each term, generated from the structured files, built on
strata-react, and starting with "taxonomies itself" as the first taxonomy. No domain held
the method's vocabulary, so one was drafted (proposal, not adopted).

- `site/`: **new**. `generate.py` reads every `domains/*/` (glossary, facets, samples,
  rounds, answer CSVs, changelog) and the docs and sources, recomputes kappa from the
  answers, and writes JSON; a Vite + strata-react app renders overview, domain, facet,
  term, round, item, doc, CSV and source pages. `site/README.md` lists what the generator
  relies on and what is published (no stored source copies). The repo was made public
  the same day, which let Actions and Pages run.
- `.github/workflows/pages.yml`: **new**. Builds on every pull request, deploys on push to
  `main` once Pages is set to GitHub Actions.
- `domains/taxonomies/`: **new**, `draft`. `scope.md`, `facets.md` (`kind`, `stage`),
  `glossary.md` (39 method concepts and 8 facet values, all `candidate`, warrant counted over
  `design/` and `domains/ux/`), `changelog.md`. `check_domain.py`: one T3 flag, "alias" as a
  possible plural, listed as a label choice.
- `README.md`: links the site and its folder.
**Adopted stage 1 of the prompts taxonomy after the name test (branch `claude/project-thread-oneclm`, PR #11)**.
Both fresh readers passed T9 (openai 94%, gemini 93%), so every stage-1 ending condition
holds on round 3. The four missed labels were changed and are `candidate` again.

- `domains/prompts/rounds/round-3/name-test/results.md`: **new**. Scores and the four misses.
- `domains/prompts/glossary.md`: `rule` labelled "fixed logic" and `model` labelled "model
  calling" (old labels kept as aliases); `context-window` redefined as a token limit;
  `steer` gains a near miss; statuses set (50 approved, 4 candidate).
- `domains/prompts/facets.md`, `scope.md`: status `in use`, round-3 agreement figures.
- `domains/prompts/changelog.md`: the operations above.

**Ran the prompts name test (T9)** with the two non-Claude raters (GPT-6.2-Astra via
`codex exec`, Gemini 4 Carbon High via `agy -p`), same isolation as the rounds.

- `domains/prompts/rounds/round-3/name-test/guesses-openai.md`, `guesses-gemini.md`:
  **new**. Each reply verbatim, with CLI, model and run details at the top.

**Prompts round 3 passes; competency and heuristic review; name-test prompt (branch `claude/project-thread-oneclm`, PR #11)**.
Round 3 passed J23 on every facet. The remaining ending conditions are T9 (name test,
waiting on two fresh readers) and adoption.

- `domains/prompts/rounds/round-3/review.md`: **new**. T10 and T11.
- `domains/prompts/rounds/round-3/name-test/prompt.md`: **new**. 54 labels.
- `domains/prompts/changelog.md`: the operations above.

**Ran prompts round 3 with the same three raters** (kit `5d0ad9e`, 60 items). Every facet
passes: Fleiss' κ area 0.80, decider 0.77, moment 0.86; openai-gemini 0.76, 0.76, 0.83.

- `domains/prompts/rounds/round-3/answers/`: **new**. Each rater's CSV and raw reply with
  run details. `results.md`: **new**, both kappa tables and the disagreement lists.

**Recorded J23 (branch `claude/project-thread-oneclm`)**. Jonathan chose the three-rater pass rule: Fleiss' κ ≥ 0.6 per facet and the non-Claude pair κ ≥ 0.6.

- `design/decisions.md`: J23 moved to the decided table.
- `design/method-v1.1.md`: M4 marked adopted; the other six stay proposed.

**Scored prompts round 2, fixed decider again, drew 80 more items for round 3 (branch `claude/project-thread-oneclm`)**.
Round 2 passed Fleiss' κ ≥ 0.6 on every facet (0.87, 0.66, 0.72) but the two non-Claude
raters agreed only 0.54 on decider, so the M4 rule (proposed, J23) fails. The held set
was used up, so `sample.py` drew 80 more from the same seeded order.

- `domains/prompts/glossary.md`: `second-model`, `person`, `rule` redefined.
- `domains/prompts/rounds/round-2/results.md`: the reading and the fixes table added.
- `domains/prompts/samples.md`, `items-all.csv`, `sample.py`: **new** set `g01`-`g80`.
- `domains/prompts/rounds/round-3/`: **new** kit, 60 items.
- `domains/prompts/facets.md`, `changelog.md`: agreement and operations.

**Ran prompts round 2 with the same three raters** (kit `6145895`, 56 items). Fleiss' κ:
area 0.87, decider 0.66, moment 0.72, all passing; openai-gemini: 0.87, 0.54, 0.67, so
decider still misses for the non-Claude pair.

- `domains/prompts/rounds/round-2/answers/`: **new**. Each rater's CSV and raw reply with
  run details. `results.md`: **new**, both kappa tables and the disagreement lists.

**Scored prompts round 1, fixed the decider and moment scope notes, built round 2 (branch `claude/project-thread-oneclm`)**.
The three raters (Claude Opus 5.5, GPT-6.2-Astra via `codex exec`, Gemini 4 Carbon High via
`agy -p`) were run on omarchy. Area and moment passed; decider missed at Fleiss' κ 0.58.

- `domains/prompts/rounds/round-1/results.md`: written by the run; this commit adds the
  reading of the numbers (decider's low kappa with 83% unanimity) and the fixes table.
- `domains/prompts/glossary.md`: `working-model`, `rule`, `second-model`, `setup` redefined.
- `domains/prompts/facets.md`: agreement recorded per facet; status line.
- `domains/prompts/rounds/round-2/`: **new**. 56 items, three prompts, README.
- `domains/prompts/changelog.md`: the operations above.

**Ran prompts round 1 with three raters**. Each rater ran on omarchy from an empty
directory with only its own prompt (kit `e923f21`); decider misses κ 0.6, so its
definitions need fixing before round 2.

- `domains/prompts/rounds/round-1/answers/`: **new**. Round 1 answers from three raters
  (Claude Opus 5.5, GPT-6.2-Astra, Gemini 4 Carbon High), each with its raw reply and run
  details; `results.md`: **new**, the scores. Fleiss' κ: area 0.93, decider 0.58 (misses
  0.6), moment 0.72; openai-gemini: 0.92, 0.57, 0.69.

**Started the prompts taxonomy and proposed method v1.1 for large domains (branch `claude/project-thread-oneclm`)**.
Jonathan asked for a taxonomy for `jburnhams/prompts` ("agents, mcps, llm, harnesses,
evals, everything really"), to refine the process as it goes, and for better raters
(OpenAI, and a stronger Gemini than Flash through `agy`). The repo is about 815,000 words
in 281 files, so the plan changed from one pass to stages: the kernel words and an area
facet first, then one area at a time.

- `design/method-v1.1.md`: **new**. Seven proposed changes (M1-M7): stages inside one
  context, a written population and seeded draw, test samples of at least 5 per value,
  three raters from three families scored with Fleiss' and pairwise kappa, majority
  labels, rules for raters run through agent CLIs, and items as heading plus text. Not
  adopted; `process.md` and `spec.md` are unchanged.
- `design/decisions.md`: J20-J26 for those proposals; J14 ("agent") flagged as needed now.
- `tools/kappa.py`: takes three or more answer files and prints Fleiss' kappa, Cohen's
  kappa per pair, and the majority value or SPLIT for each disagreement. Two files work as
  before (checked on ux round 1: same table). Fleiss checked against the textbook
  14-rater example (0.210).
- `domains/prompts/`: **new**. `scope.md`, `harvest.md`, `samples.md`, `sample.py`,
  `items-all.csv`, `facets.md`, `changelog.md`.
- `domains/prompts/glossary.md`: **new**. Draft `candidate` entries for set A's 18 values,
  written before Jonathan's choice so the kit could be built; the decider value `model`
  became `working-model` so it does not share a label with the area `model`.
  `tools/check_domain.py domains/prompts`: one heuristic flag (`operations`, a mass noun,
  kept).
- `domains/prompts/rounds/round-1/`: **new**. Three-rater kit: `items.csv` (60 items),
  `prompt-{claude,openai,gemini}.md` with values shuffled per rater, `make_prompts.py`,
  and a `README.md` for running all three through their CLIs on omarchy (M6).
- Jonathan decided J14 on 2026-11-26: "agent" is a model configured to act (prompt and tools in a loop); products are harnesses. Moved to the decided table in `design/decisions.md`.
- Jonathan chose facet set A on 2026-11-26; `facets.md`, the domain changelog and the kit README say so.
- `domains/prompts/glossary.md`: 36 kernel terms drafted after J14; area values `model` and `tool` relabelled "model access" and "tool use" (IDs kept) so the plain words are kernel terms. T1-T6 clean apart from one heuristic flag.
- `domains/prompts/samples.md`, `rounds/round-1/`: four round-1 items (`r06`, `r36`, `r48`, `r58`) had been used in the facet comparison or as glossary examples, so they moved to the build sample and four held items (`h01`-`h04`) replaced them; prompts regenerated. Found by the Codex review on PR #9.
- `.gitignore`: **new**, ignores `__pycache__/` (one `.pyc` was committed by mistake and removed).
- Looked for and found: `agent-design/keel/taxonomy.md` in prompts is an existing
  glossary (Keel's own words) and is the seed; *Inside the Scaffold* (stored in
  prompts' `papers/`) has a three-layer taxonomy not yet read in full for this.

**Fixed the duplicate-ID check in `tools/check_domain.py` (branch `claude/project-thread-l3cp9e`)**.
A review on PR #7 found that T1's duplicate-ID flag was lost when the second record replaced
the first, so a glossary with a repeated ID passed. The fix was committed after PR #7 merged.

- `tools/check_domain.py`: the replacing record keeps the duplicate flag; tested by appending
  a second `brief` entry to the ux glossary (now reports `T1 brief: duplicate id`).

**Fixed what round 1 showed and adopted the ux taxonomy (branch `claude/project-thread-l3cp9e`, built on PR #6)**.
Round 1 passed κ ≥ 0.6 on every facet. The six disagreements were fixed in scope notes,
the name test and the remaining checks were run, and the domain was adopted under G1,
with Jonathan able to veto.

- `domains/ux/glossary.md`: nine scope notes widened; "one question" and "one finding"
  renamed to "screen question" and "screen finding" after the name test; two definitions
  reworded for T4; alias "fingerprint" moved; 40 terms `approved`, 13 `candidate`.
- `domains/ux/facets.md`: kappa per facet recorded; `r20` in Unsorted under `aspect`.
- `domains/ux/scope.md`: status `in use`, 2026-11-26.
- `domains/ux/rounds/round-1/results.md`: fixes and the ending-conditions table.
- `domains/ux/rounds/round-1/review.md`: **new**. Competency questions (T10) and the
  Z39.19 review (T11).
- `domains/ux/rounds/round-1/name-test/`: **new**. Prompt, a fresh reader's guesses and
  the results (T9): 41 of 53 right, 4 wrong; WordNet sense counts.
- `domains/ux/changelog.md`: the operations above.
- `tools/check_domain.py`: **new**. Mechanical checks T1-T6 for a domain (J19's
  recommendation, built for this round).

**Scored ux round 1 with Gemini as the second rater (branch `claude/ux-round-1-gemini`)**.
Gemini 3.8 Flash sorted the 30 round-1 items from `prompt-second.md` alone, run through
strata-models on omarchy. Every facet clears κ ≥ 0.6: aspect 0.92, brief_override 0.92,
detection 0.78, mode 1.00, with six disagreements listed for the fix-up.

- `domains/ux/rounds/round-1/answers/gemini.csv`: **new**. Rater B's 30 answers.
- `domains/ux/rounds/round-1/answers/gemini-raw.md`: **new**. Rater B's whole reply.
- `domains/ux/rounds/round-1/results.md`: rater B's run details, the kappa table and
  the disagreement list.

## 2026-11-25

**Started the ux-research domain (branch `claude/project-thread-l3cp9e`)**. Jonathan
asked to start applying the adopted method (v1) to ux-research. Files go in
`domains/ux/` (J2). The thirteen open decisions follow their recommendations
(J3, J4, J9-J19), as `design/decisions.md` says; the facets are proposed and wait for
Jonathan's choice (process step 4).

- `domains/ux/scope.md`: **new**. Purpose, readers, owner, twelve competency questions,
  out of scope, neighbours, ending conditions (T1-T6, T7 with at most 2 unsorted, T8
  κ ≥ 0.6 by two model families, T10, T11).
- `domains/ux/samples.md`: **new**. 53 build items, 10 bare-facet test items, 30 round-1
  test items, 16 held for round 2, from ux-research at `c742019` (five items moved into the build sample after review, because the draft had drawn on them).
- `domains/ux/harvest.md`: **new**. Term counts over the repo's own 28 docs, synonym sets,
  and seven homonyms (surface, layer, mode, signature, finding, role, source).
- `domains/ux/facets.md`: **new, proposal**. Recommended set A (aspect, brief override,
  detection, mode), three other sets, the build-sample classification and the
  bare-facet test with the changes it caused.
- `domains/ux/changelog.md`: **new**.
- Jonathan chose facet set A on 2026-11-25; `facets.md` now says so, and `glossary.md`
  has 12 more candidates for the facet values (53 in all).
- `domains/ux/rounds/round-1/`: **new**. The 30-item agreement-test kit: `items.csv`, two
  prompts (`prompt-claude.md`, `prompt-second.md`, values in different orders) and a
  README on running the second model family, which Jonathan is setting up on omarchy.
- `tools/rater_kit.py`: **new**. Builds the items file and rater prompts from a domain's
  samples, facets and glossary.
- `tools/kappa.py`: **new**. Cohen's kappa per facet between two raters' CSVs, with the list
  of disagreements.
- `domains/ux/glossary.md`: **new**. 41 candidate entries for the general terms and the
  four modes; facet values wait for the facet choice. Seven label choices are listed at
  the top for Jonathan's veto, the main one being that `surface` means the tonal layer
  (as in strata-react's token names) and `screen` the page being built.

**Recorded Jonathan's six "before the first domain" decisions (branch `claude/project-thread-cfqw9w`)**.
Jonathan asked to be interviewed on the open decisions; he answered one card per
decision in the project thread. Three answers differ from the recommendations, so the
spec and process were edited to match.

- `design/decisions.md`: new "Decided 2026-11-25" table replacing "Needed before the
  first domain". J1 adopt as version 1; J2 files live **centrally** in this repo under
  `domains/<name>/` (recommended: in each repo); J5 κ ≥ 0.6; J6 raters are **two model
  families** (recommended: Jonathan plus a model); J7 build 30-60, test 30 fresh; J8
  **agents approve, Jonathan can veto** (recommended: Jonathan approves everything).
- `design/spec.md`: status now version 1; §1 paths moved from `taxonomy/` in each repo to
  `domains/<name>/` here, with the trade-off against Evans's code-base boundary written
  down; T8 rater rule; G1 and G2 rewritten for agent approval with a veto, noting that
  this departs from Z39.19 §11.3.1.1; `scope.md` Owner field.
- `design/process.md`: status; steps 1, 3, 6, 8, 10, 11, 12, the light version and both
  tables updated for J2, J6 and J8. Step 4 (choosing facets) still names Jonathan, since
  J8 asked about names and changes, not structure.

**Wrote the definitive process and spec (branch `claude/project-thread-cfqw9w`, built on PR #2)**.
Jonathan asked for a process and spec for the taxonomies to be built in other repos,
with a citation backing every decision. Every rule and step now cites a stored file in
`sources/` with a page or section; where the best source is not stored, it says so (⚠).
The branch starts from PR #2's branch because the citations point at the files PR #2
stores, so PR #2 should be merged first.

- `design/spec.md`: **new**. File set and field grammar for `taxonomy/` in each domain
  repo (`scope.md`, `facets.md`, `glossary.md`, `map.md`, `changelog.md`, `patterns/`),
  mapped to SKOS and to the Z39.19 term record; structure rules S1-S6, naming N1-N8,
  definitions D1-D5, contexts C1-C3, governance G1-G7, and tests T1-T14 (mechanical,
  judgement, in use).
- `design/process.md`: **new**. Steps 0-12, from deciding to start to maintenance, with a
  light version and a table of what models and people each do.
- `design/decisions.md`: **new**. Nineteen decisions for Jonathan (six needed before the
  first domain), with recommendations. It absorbs the five open questions in
  `design/README.md` and the nine proposals in `design/source-check-2026-11-25.md`.
- `tools/check_citations.py`: **new**. Checks that every rule and step in the spec and
  process cites an existing stored file (or carries ⚠), and that all links resolve.
- `design/README.md`, `design/templates.md`: marked as superseded in detail by the new
  files; kept for the overview and history.
- `README.md`: links the new files.
- `sources/wan-2024-tnt-llm/README.md`: notes on TnT-LLM's agreement results, read for the
  spec.
- **Changes to earlier claims and proposals**:
  - Kappa target lowered from 0.7 to **0.6** (proposed). TnT-LLM's expert annotators
    reached 0.553 and above 0.6 on its two taxonomies (§5.3.2, Table 2).
  - The **depth cap** ("at most three levels") is dropped: it rested on Berlin 1992, which
    is not stored. Noy and McGuinness's sibling and new-level rules (§§4.2, 4.4) replace it.
  - **Confidence levels** (Alexander's asterisks, not stored) are replaced by a status
    (`candidate`, `approved`, `deprecated`) from Z39.19 §11.1.6.
  - TnT-LLM's authors did "a lightweight human calibration" after generation (§5.3); the
    earlier note said only that the loop has no human in it, which stays true.
- Review fixes (PR #3, Codex): G5 kept a deprecated term's labels on its record *and*
  copied them to the replacement, which T2 would reject; now they stay on the deprecated
  record, which gains a **Replaced by** field. The light version used the whole domain to
  build and then had nothing fresh to test on, and its 20-item agreement test clashed
  with T8's 30; it now holds back a third first, and small samples give an indicative
  kappa only.
- Read for the first time: Z39.19 §11 (construction, testing, maintenance, management
  systems, pp. 90-102), which supplies most of the governance and the error checks.
- Not reachable again: Kundisch et al. 2022 (Augsburg resets the connection, Springer
  serves a JS page, EconStor a bot check). Nickerson 2013, Cohen 1960, Berlin 1992 and
  *A Pattern Language* remain unstored, so the points resting on them are marked ⚠.

**Checked the notes and topic docs against the stored sources (branch `claude/project-thread-sn5nqu`, PR #2)**.
Jonathan asked to use the downloaded sources to inform the research. Each of the 32
stored sources' notes was checked against its text (two scans read by eye), its
**Read** line and the `sources.md` Read column updated, and the topic docs corrected or
extended where the text said more or something different. Design changes are written
as proposals, not applied.

- `sources/*/README.md` (32 folders): notes rewritten from the text with page or section
  references; quotes that were from memory are now checked. Corrections to earlier
  claims:
  - Rosch et al. 1976 did **not** test expertise ("the degree of expertise of subjects
    did not vary systematically"). "Experts name at a finer level" was stated as a
    finding; it is a hypothesis in the paper, with one anecdote.
  - Kwasnik's paradigm is strictly two dimensions, not "two or three".
  - Z39.19 allows singular count nouns where a field's usage is singular (§6.5.1.1), so
    there is no real clash with OBO's singular rule.
  - Hofmeister et al.: the figure is 19%, and abbreviations were no better than single
    letters. Lawrie et al. (2007 version) found abbreviations often as good as words and
    easier to remember; the earlier note gave only half of that.
  - TnT-LLM has no human review in its loop; the review step is an LLM prompt.
  - Medin and Ortony: the painted-raccoon example is Keil's, not theirs.
  - Gruber's design criteria (clarity, coherence, etc.) are from his 1995 paper, not 1993.
  - PMEST is in *Colon Classification* (6th ed., rule 05501) and absent from the 1937
    *Prolegomena*; the three planes are in neither stored edition.
  - Feitelson et al.'s 334 vs 234 subjects: both right (all experiments vs main survey).
  - Denton's page shows no licence; "reportedly CC BY 4.0" is unconfirmed.
- New findings worked into the topic docs:
  - `01-structures.md`: Kwasnik's "premature hierarchy" test (a "miscellaneous" box),
    and her warning that facets are hard to add later.
  - `02-how-minds-categorise.md`: the basic-level correction above, and Medin and
    Ortony's "essence placeholder" that defers to experts.
  - `03-naming.md`: Z39.19 abbreviation and plural rules, the Hofmeister and Lawrie
    figures, Meszaros and Doble's guess-the-name test, and Ranganathan's 1937 Canons of
    Terminology (Currency, Reticence, Enumeration, Context).
  - `04-vocabularies-and-ontologies.md`: OntoClean's other two pitfalls (constitution
    and "can be" taken for is-a). Its own worked example treats *Agent* as a role. Also
    the OBO Foundry's orthogonality and term composition, and the fact that
    `exactMatch` is transitive.
  - `05-building-and-testing.md`: what TnT-LLM and Clio actually do, and constant
    comparison from grounded theory.
  - `07-limits-and-politics.md`: Star and Griesemer's definition and four types of
    boundary object, and Hjørland's four approaches.
  - `08-pattern-languages.md`: Meszaros and Doble's mandatory elements and naming
    patterns. Alexander's 1971 rejection of his own method. Gabriel's "The Failure of
    Pattern Languages": Alexander judged the language did not change what got built,
    and turned to the process.
- `design/source-check-2026-11-25.md`: **new**. It lists what this pass confirms in the
  design and nine proposed additions, none adopted. Examples: test the facet list early;
  a Reticence rule for names; abbreviations as aliases; an owner per glossary; define
  "agent" first; prefer `closeMatch`; keep the procedure light. It is linked from
  `design/README.md` and `README.md`.
- `sources/*/`: the IEKO pages' `.md` text was re-extracted, because the first
  extraction ran each table-laid page onto a few lines.
- `sources.md`: the Read column was updated for the 32 checked sources. 28 rows remain
  "not read", all for sources with no stored copy.

**Downloaded copies of the sources (branch `claude/project-thread-sn5nqu`)**.
The coordinator asked for full copies of every source from the first pass, now that the
project has a cloud environment that can reach publisher and preprint hosts; Jonathan had
said storing papers and books is fine as the repo is private. 32 of 65 sources now have a
stored copy, most with extracted text. Only legitimately free copies were taken (open
access, author or repository copies, course reading lists, public-domain and Digital
Library of India scans); Internet Archive loans and anonymous uploads of in-copyright
books were left alone.

- `sources/*/`: 38 files (plus 24 figure images) added across 32 folders (PDFs or saved HTML pages, plus OCR text
  for the Wilkins 1668 and Ranganathan scans). Beside each PDF or page, a `.md` holds its
  extracted text for searching; the original file is the authority. Medin and Ortony 1989
  and Star and Griesemer 1989 are image scans with no text layer, so they have no `.md`.
- `sources/*/README.md`: the **Stored here** and **To fetch** lines of those 32 folders
  now name the files and where each came from. The notes themselves were written before
  the copies were stored and have **not** been re-checked against them yet.
- Corrections: the Lawrie copy is the 2007 journal extension, not the ICPC 2006 paper;
  the Ranganathan copy is the 1937 first edition, not the 1967 third; the Hofmeister
  copy is the SANER 2017 paper (a longer EMSE 2019 version exists); `hjorland-2017-
  classification/`'s URL pointed to the IEKO *knowledge organization* article, and the
  stored copy is the IEKO *classification* article.
- Review fixes (PR #2, Codex): the *Colon Classification* OCR is the 6th edition (1960,
  1969 reprint), not 1933 as the Internet Archive catalogues it; renamed to
  `ranganathan-1960-colon-classification-6th-ed.ocr.txt`. The saved pages for Alexander
  1965, Noy and McGuinness, and IEKO "Classification" now carry their figures in an
  `img/` folder beside them, with references rewritten to point there.
- `sources.md`: new **Stored** column (yes / part / blank).
- `to-fetch.md`: rewritten. 9 items obtained and removed; 24 remain. Free copies found
  for Nickerson et al. 2013 (Augsburg postprint) and Usman et al. 2017 (ScienceDirect)
  but those servers refused this container, so they are listed with links to open in a
  browser.
- Not reachable from this container (site-level bot blocks or resets, not the network
  policy): opus.bibliothek.uni-augsburg.de, link.springer.com PDFs, dl.acm.org and
  cacm.acm.org, sciencedirect.com, aisel.aisnet.org, econstor.eu, philarchive.org,
  ideals.illinois.edu item pages (bitstreams worked), wordnet.princeton.edu,
  researchgate.net, tandfonline.com, web.archive.org. The Rosch 1978 course copy used in
  the first pass now returns 404.

**First pass: literature review and a candidate system (branch `claude/project-thread-jyv2l9`)**.
Jonathan asked for the best research on taxonomy and naming, starting from an ELI5 and
going deep, laid out like `prompts` (sources, then topic docs, then our own design), with
a list of paywalled works to fetch, and a look at Alexander's *A Pattern Language*. The
container's network policy blocked downloads from every publisher and preprint host, so
no raw copies are stored yet; open sources were read through a web reader instead.

- `README.md`, `eli5.md`: **new**. Map of the repo; taxonomy from zero in six levels.
- `01-structures.md` to `08-pattern-languages.md`: **new** topic docs.
- `design/README.md`, `design/templates.md`, `design/first-look.md`: **new**. The candidate
  system (facets, SKOS-style glossary, bounded contexts, tested build method, pattern
  layer), its templates, and observations on the prompts and ux-research repos.
- `sources/` (65 folders), `sources.md`, `to-fetch.md`: **new**.
- Read online: Rosch 1978 (to p.15), Alexander 1965, Kundisch et al. 2022, Feitelson et al.
  2020 and the 2024 replication, Schober et al. 2009, Seppälä et al. 2017, Guarino and
  Welty (OntoClean), Noy and McGuinness, SKOS Reference, Evans's DDD Reference, Denton
  2003, ISKO "Facet analysis" (most in part).
- Not reached: Nickerson et al. 2013 (paywalled; its ending conditions are given from
  prior knowledge and marked), Furnas et al. 1987 full text (only the abstract, which is
  cut before its figure), Kwasnik 1999 (the IDEALS item has no fetchable PDF link),
  Meszaros and Doble (hillside.net refuses automated fetches). Everything else is in
  `to-fetch.md`.
