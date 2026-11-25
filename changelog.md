# Changelog

All notable changes, grouped by day, newest first. See [`CLAUDE.md`](./CLAUDE.md).

## 2026-11-25

**Started the ux-research domain (branch `claude/project-thread-l3cp9e`)**. Jonathan
asked to start applying the adopted method (v1) to ux-research. Files go in
`domains/ux/` (J2). The thirteen open decisions follow their recommendations
(J3, J4, J9-J19), as `design/decisions.md` says; the facets are proposed and wait for
Jonathan's choice (process step 4).

- `domains/ux/scope.md`: **new**. Purpose, readers, owner, twelve competency questions,
  out of scope, neighbours, ending conditions (T1-T6, T7 with at most 2 unsorted, T8
  κ ≥ 0.6 by two model families, T10, T11).
- `domains/ux/samples.md`: **new**. 48 build items, 10 bare-facet test items, 30 round-1
  test items, 21 held for round 2, from ux-research at `c742019`.
- `domains/ux/harvest.md`: **new**. Term counts over the repo's own 28 docs, synonym sets,
  and seven homonyms (surface, layer, mode, signature, finding, role, source).
- `domains/ux/facets.md`: **new, proposal**. Recommended set A (aspect, brief override,
  detection, mode), three other sets, the build-sample classification and the
  bare-facet test with the changes it caused.
- `domains/ux/changelog.md`: **new**.
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
