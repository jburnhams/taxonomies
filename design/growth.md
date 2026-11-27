# Growth: how domain repos ask for terms (proposed)

**In one line**: a domain repo looks up the term for a concept before it writes a word,
uses its own word as a request when nothing fits, and asks for clarification or a
breaking change the same way; the taxonomies repo collects those requests, answers each
with a named operation, and the domain repo picks the answers up on its next pass.

**In plain words**: the glossaries only grow if the people and agents writing in the
domain repos (a prompts research pass, a ux-research doc) can ask two questions cheaply:
"which word do we use for this?" and "there is no word for this, can we have one?". Today
they would have to read an 1,100-line glossary, and the weekly prompts pass cannot even
write to this repo. So: one command answers the first question; a short file in the
domain repo's own tree holds the second; and this repo reads that file, decides, and
writes the answer where the same command will show it. The same path carries "this term
is unclear" and "this term is wrong", because research that settles one concept usually
opens up more and shows where older ones need a sharper edge (Jonathan, 2026-11-27).

**Status**: proposed 2026-11-27, not adopted (◆ J27-J32 in [`decisions.md`](./decisions.md)).
The tool [`tools/term.py`](../tools/term.py) and the empty request logs work today
without any decision; the rules below are what an intake follows until Jonathan decides,
as earlier proposals were. When adopted, they fold into spec §§1, 9 and 10 and process
steps 11-12 as listed at the end. Citations follow the spec's rules; "reasoning" marks a
point with no source claimed.

## Why v1 needs this

v1 already says that anyone may propose a term (spec G2), that an agent missing a word
adds a `candidate` entry rather than inventing one, and that new words in use are counted
(T13). Three things stop that working outside this repo:

1. **No way in.** The domain repos' agents are told to add a `candidate` entry here
   (prompts and ux-research `CLAUDE.md`), but the weekly prompts research pass runs in a
   session that can push only to `jburnhams/prompts`. Its new concepts have nowhere to go,
   so they become unrecorded words: exactly what T13 counts.
2. **No cheap lookup.** The prompts glossary is 83 entries over 1,137 lines. Checking it
   for each new word costs more than inventing one, so the choice leans to inventing
   (reasoning). Feitelson et al. found two developers name the same thing the same way
   with median probability 6.9% ([§III][fe]); a lookup that is cheaper than guessing is
   what makes agreement likely.
3. **No path for changes to terms in use.** Spec G6 asks that a rename change "every use
   in the repo in the same commit" ([Evans pp. 3-4][ev]). With the glossary here and the
   uses in other repos (J2), that cannot be one commit, so a rename here silently leaves
   the domain repos on the old word.

## The loop

| # | Who | Does | With |
|---|---|---|---|
| 1 | domain repo | looks up the concept before writing a new word | `term.py lookup <domain> <words>` |
| 2 | domain repo | uses the term found; if none fits, uses its own word at once (a usable `candidate`, G3) | |
| 3 | domain repo | writes a request record for each miss, unclear term or wrong term | `term-requests.md` in its own root |
| 4 | this repo | collects new requests into the domain's log | `term.py intake --write` |
| 5 | this repo | answers each with an outcome (table below) and the operations it needs | `domains/<name>/requests.md`, glossary, changelog |
| 6 | domain repo | on its next pass, reads what changed since its last pass, switches words, removes answered requests | `term.py changes <domain> --since <date>` |

The tool reads the files in this repo; from a domain repo, with no checkout, it fetches
them from GitHub:

```bash
T=https://raw.githubusercontent.com/jburnhams/taxonomies/main/tools/term.py
curl -fsSL $T | python3 - lookup prompts "approval timeout"
curl -fsSL $T | python3 - changes prompts --since 2026-11-26
```

`lookup` folds case and hyphens, so an alias or old label finds its term and says to
write the preferred label; a deprecated label says what replaced it (G5). With no exact
match it lists the closest terms with their scope notes and near misses, and any request
already made for the words.

## The request record

One record per request in the domain repo's `term-requests.md`, in the spec's field
grammar (spec §1) so `term.py` can read it. The ID is the date asked and a slug, unique
in that file. The record holds what the intake needs to decide without a second
conversation: the draft definition (D1), what lookup showed and why it did not fit (D4's
near miss, from the asker's side), and the asker's warrant (N2).

```markdown
### approval timeout (`2026-11-30-approval-timeout`)

- **Ask**: new
- **Term**: (for `clarify` or `change`: the ID it is about)
- **Concept**: An approval timeout is a limit on how long a harness waits for an approval before it acts.
- **Looked at**: `approval` (the happening, not its limit), `permission-mode` (which actions need one)
- **Example**: [agent-permissions-approval.md §4](agent-permissions-approval.md)
- **Warrant**: "approval timeout" 6 in *.md, 2026-11-30
- **Asked**: 2026-11-30, weekly research pass, PR #52
```

**Ask** is one of:

- **`new`**: a concept no term covers.
- **`clarify`**: a term whose definition, scope note or near miss left the asker unsure
  which term to use, or which a new case falls outside. **Concept** says the case.
- **`change`**: a term whose label or boundary the asker thinks is wrong (a rename, a
  split, a merge, a deprecation). **Concept** says what should change and why.

## Rules for an intake

- **R1. Every request gets an outcome and a date.** The intake copies each new request
  into `domains/<name>/requests.md` as `open`, then records one outcome: `use` (an
  existing term fits; give its ID), `alias` (an existing term fits and the asker's word
  becomes its alias), `candidate` (a new term was added), `clarified` (a field was
  rewritten), `changed` (a breaking operation, below), or `declined` (with the reason,
  for example out of scope) (◆ J27). **Answered** gives the date and who answered. This is
  Z39.19's candidate-term record, kept for every proposal whether or not it is accepted
  ([Z39.19 §§11.3.1.1-11.3.1.2, pp. 96-97][z39]), and the log is what `lookup` and
  `changes` show back to the asker. A request is not deleted after it is answered (G5's
  reasoning applies: the log is how an old question finds its answer).
- **R2. Check the request against the glossary first.** Many misses are a word the asker
  did not find: an alias the glossary lacks, or a term whose label is not the asker's
  basic-level word ([Rosch et al. pp. 392-393][ro]). Then the outcome is `use` or `alias`,
  not a new term: readers should be "led from their own words to your chosen
  terminology" ([Denton §2.3 step 4][den]). Adding an alias is logged as a **redefine**
  of the term it joins (G4), and must keep T2 (one label, one term).
- **R3. A new term enters as `candidate` with the asker's warrant.** The asker's draft
  is the starting definition, rewritten to D1-D4 and N1-N8; the asker's use is its user
  warrant ([Z39.19 §5.3.5][z39]). If it is a facet value, or an item needing a value no
  facet has, it also goes on the facet's **Unsorted** list (S6) and waits for the next
  round, because a new value changes what the facet's kappa measured. In a staged
  domain (method v1.1 M1), a request in an area not yet built goes into that stage's
  harvest instead. Recommended approval: an agent may move a non-facet candidate to
  `approved` (G1) at the next review once T1-T6 pass, one fresh reader from another
  model family guesses its meaning (T9), and it is used in at least two docs
  (◆ J28; reasoning: the bar a round sets for facet values, scaled to one term).
- **R4. Clarify without moving the edge.** A `clarified` outcome rewrites the
  definition, scope note, near miss or example so the asker's case is decided. It is
  non-breaking only if every item raters already sorted under the term still fits it
  (judgement, checked against the term's round items on the explorer site); otherwise
  it is a boundary change and follows R5. Scope notes exist to "distinguish between
  terms that have overlapping meanings" ([Z39.19 §6.2.2][z39]); the boundary is where
  raters disagree ([Wan et al. App. B.2.1][wan]).
- **R5. Breaking operations keep the old word findable, and some need a re-test.** A
  breaking operation is a **rename**, **split**, **merge**, **move** or **deprecate**
  that touches a term, or a **redefine** that moves its boundary (R4). Every one keeps
  the old label as an alias or on a deprecated record, so `lookup` on the old word names
  the new one ([Z39.19 §11.3.2.1a, p. 97][z39]; G5); IDs never change (N6;
  [OBO Foundry, "A collaborative experiment"][obo]). Recommended approval (◆ J29): an
  agent approves a rename, merge or deprecate under G1, as now. A split, a move, or a
  boundary change of an `approved` facet value needs a round on that facet first, with
  fresh items that include the value, since the facet's last kappa no longer describes
  it; for any other term the G1 rule holds. Every breaking operation in an `in use`
  domain is named in the PR for Jonathan's veto.
- **R6. Mark breaking changes in the changelog, and version by date.** A breaking line in
  `domains/<name>/changelog.md` ends `Breaking: <what a domain repo must do>`, for example
  `Breaking: write "fixed logic" for "rule"`. `term.py changes` flags those lines and
  any rename, split, merge, move or deprecate that names a term. The version of a
  glossary is the changelog's date: a domain repo's own changelog says which date it
  checked against ("glossary checked to 2026-11-30"), and its next pass asks for changes
  since then (◆ J30; reasoning: one owner, so dates are enough and nothing else has to be
  kept in step). This amends G6 across repos: in this repo, the rename and every use
  change in one commit as before; in a domain repo, at its next pass, in the docs it
  touches, with T12 (alias drift) counting what is left ([Evans pp. 3-4][ev]).
- **R7. Intake runs when the domain is worked on, and at each review.** Recommended
  (◆ J31): at every G7 review, at the start of any thread that works on a domain, and on
  a weekly scheduled task in this project the day after the prompts research pass, so
  that pass's requests are answered before the next one ([Z39.19 §11.3.1, p. 96][z39]:
  review at intervals set by how fast terms change). The scheduled task is not created
  until Jonathan says so.

## What a domain repo's instructions say

The domain repo's `CLAUDE.md` (or `AGENTS.md`) already links its glossary (process step
11). It gains four lines (◆ J32): look up before writing a new concept word; when nothing
fits, use your own word and add a request; for a term that is unclear or wrong, add a
`clarify` or `change` request rather than working round it; at the start of a pass, run
`changes --since` the date in your last changelog entry, switch the words it lists in
the docs you touch, and say in the new changelog entry which date you checked to and
which requests you made. Agents that can write to this repo may still add a `candidate`
directly (G2), but the request record is the one path that works from every session.

Encouragement is the point, not policing: each request is evidence that the domain
needs a word, and the count of requests answered `candidate` is how the glossary's growth
shows up in T13 rather than as unrecorded new words. A pass that requests nothing over
several weeks while writing new docs is worth a look (reasoning).

## Where this lands when adopted

| Proposal | Changes |
|---|---|
| request log | spec §1 file table: `domains/<name>/requests.md` (one record per request, R1); spec §4 History may cite a request ID |
| R1-R3 | spec G2 (the request record is how a proposal arrives), G3 (a candidate from a request) |
| R4-R5 | spec G4 (which operations are breaking), G6 (across repos, at the next pass) |
| R6 | spec §6 changelog line form (`Breaking:`); T12 counts against the checked date |
| R7 | spec G7, process step 12 (intake is part of maintaining) |
| J32 | process step 11 (the four lines in each domain repo) |

## Not in this proposal

- **A search box on the explorer site.** The site already has every term's data;
  a find-a-term page would serve people browsing. Left for later because the asker in
  Jonathan's example is an agent, for which the command is the better fit.
- **GitHub issues as the inbox.** An issue form would let a person ask from a phone, but
  the weekly pass cannot open issues here either, and a second inbox means two places to
  read. A person can add a record to `term-requests.md` in the same way.

## Sources cited

Keys match [`spec.md`](./spec.md#sources-cited). Stored copies are in the private
`jburnhams/taxonomies-sources` repo.

[den]: https://github.com/jburnhams/taxonomies-sources/blob/main/denton-2003-faceted-howto/denton-2003-faceted-howto.html
[ev]: https://github.com/jburnhams/taxonomies-sources/blob/main/evans-2003-domain-driven-design/evans-2015-ddd-reference.pdf
[fe]: https://github.com/jburnhams/taxonomies-sources/blob/main/feitelson-2021-how-developers-choose-names/feitelson-2021-how-developers-choose-names.pdf
[obo]: https://github.com/jburnhams/taxonomies-sources/blob/main/arp-smith-spear-2015-bfo/smith-2007-obo-foundry.html
[ro]: https://github.com/jburnhams/taxonomies-sources/blob/main/rosch-1976-basic-objects/rosch-1976-basic-objects.pdf
[wan]: https://github.com/jburnhams/taxonomies-sources/blob/main/wan-2024-tnt-llm/wan-2024-tnt-llm.pdf
[z39]: https://github.com/jburnhams/taxonomies-sources/blob/main/niso-z39-19-2005/ansi-niso-z39-19-2005-r2010.pdf
