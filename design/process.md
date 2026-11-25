# Taxonomy process: how to build one for a domain

**In one line**: frame the purpose, harvest the words already in use, find a few sorting
questions, name and define each concept, then test on fresh items until two raters agree;
after that, change it only through named, logged operations.

**Status**: proposal, 2026-11-25. Not adopted. Choices marked ◆ are Jonathan's and are
listed in [`decisions.md`](./decisions.md); the steps follow the recommended option. The
files each step produces are defined in [`spec.md`](./spec.md), and rule IDs (S1, N2,
T8, ...) refer to it.

## In plain words

You are making a shared notebook of words for one project. First you write down what
the notebook is for. Then you gather a pile of real things from the project and write
down every word people use for them. You look for a few questions that sort the pile
well ("who starts it?", "what part of the system is it about?"). You pick one name for
each idea, write what it means, and point at a real example. Then you try sorting new
things with only the notebook, and ask someone else to sort the same things. Where you
disagree, the notebook is unclear, so you fix it and try again. When you agree, you
start using it, and from then on every change is written down.

## How to read this

Each step says what to do, what it produces, and why, with a citation to a stored
source (path and page or section; paths are in [Sources cited](#sources-cited)). ⚠ marks
a point whose best source is not stored yet. "Prior knowledge" marks a claim that needs
checking.

## The steps at a glance

| # | Step | Produces | Who |
|---|---|---|---|
| 0 | Decide to start, check for reuse | a go / no-go | Jonathan |
| 1 | Frame | `scope.md` | Jonathan, with a model drafting |
| 2 | Collect the samples | build sample, test sample | model, checked by Jonathan |
| 3 | Harvest the words | term list with counts | model |
| 4 | Find the facets | draft `facets.md` | model proposes, Jonathan decides |
| 5 | Test the bare facets | revised `facets.md` | model |
| 6 | Name and define | `glossary.md` (all `candidate`) | model drafts, Jonathan decides names |
| 7 | Classify fresh items, fix, repeat | revised files, `changelog.md` | model |
| 8 | Agreement test | kappa per facet | two independent raters |
| 9 | Name tests | fixes to labels | a fresh reader, WordNet |
| 10 | Adopt | terms `approved`, `scope.md` status "in use" | Jonathan |
| 11 | Put into use | links from CLAUDE.md / AGENTS.md, lint | model |
| 12 | Maintain | changelog entries, reviews | owner |

Steps 6 to 9 repeat until the ending conditions in `scope.md` hold. A light version for
small domains is at the end.

## Step 0. Decide to start, and check for reuse

- **Start only when the domain is being worked in**, and run the steps inside that work,
  not as a separate exercise (◆ J10). Alexander disowned his own formal design method in
  1971 because readers "made a cult of following" it, and said the diagrams could be
  developed "piecemeal, one at a time ... out of your experience"
  ([Gabriel 2023, App. E.2][gab23]). He later judged that *A Pattern Language* had not
  changed what got built, and turned to the process ([Gabriel 1996 pp. 57-60][gab96]).
  Building a vocabulary is "time-consuming, labor-intensive", justified by the
  consistency it buys ([Z39.19 §11.1, p. 90][z39]).
- **Look for an existing vocabulary first**, in the repo and outside it: an existing one
  "can frequently serve as a useful starting point" ([Z39.19 §11.1.1, p. 91][z39]);
  "consider reusing existing ontologies" is step 2 of [Noy and McGuinness][noy]. For
  ux-research, `ux-slop-taxonomy.md` is already a faceted catalogue
  ([`first-look.md`](./first-look.md)).

## Step 1. Frame: write `scope.md`

Write every field of `scope.md` ([spec §2](./spec.md#2-scopemd)) before collecting any
terms. The format and structure are settled first because they decide what gets
recorded ([Z39.19 §11.1.2, p. 91][z39]).

1. **Purpose**: one sentence. "The design of the classification must follow its purpose"
   ([Denton §1][den]); "Remember the purpose of the classification and the users"
   ([Denton §2.3 step 3][den]). This is the use-case instruction TnT-LLM gives its model
   at every stage ([Wan et al. §3][wan]) and the meta-characteristic in Nickerson's
   method (⚠ Nickerson et al. 2013 not stored).
2. **Readers, and whose needs win** (◆ J9): "a classification can never be neutral, but
   will always tend to support certain goals and interests at the expense of other
   interests" ([Hjørland §4.2c][hj]). Recommended: Jonathan first, then the agents that
   read the repo.
3. **Owner** (◆ J8): who approves changes ([spec G1](./spec.md#9-governance-how-a-taxonomy-changes)).
4. **Competency questions**: 5 to 15 questions the finished taxonomy must answer, used as
   the "litmus test" of scope ([Noy and McGuinness, Step 1][noy]). Example for prompts:
   "Which agent designs run without a person in the loop?"
5. **Out of scope and neighbours**: what belongs to another context, so no term has two
   homes ([Evans p. 29][ev]; orthogonality, [OBO Foundry][obo]).
6. **Ending conditions**: which tests in [spec §10](./spec.md#10-validation-tests) must
   pass and at what level, written now so the stop is not decided by mood. Denton's
   stop is "until you are able to classify everything to your complete satisfaction"
   ([Denton §2.3 step 7][den]); the spec makes that measurable (T7, T8, T10, T11).
   ⚠ Nickerson's objective and subjective ending conditions are not stored; check them
   when the paper is fetched.
7. **For prompts only**: decide which sense of "agent" the context uses before anything
   else (◆ J14). In OntoClean's worked example *Agent* is a role (anything that acts) and
   placing it above kinds is the classic error ([OntoClean §8.3][oc]); the prompts repo
   uses "agent" as a kind of program.

## Step 2. Collect the samples

- Collect "a representative sample of the entities. In a large domain, get enough to
  cover all foreseen possibilities. In a small domain, use the entire domain"
  ([Denton §2.3 step 1][den]). Items are files, sections or rules, whatever the
  competency questions are about. Choose for variety, not at random.
- **Hold back a test sample** of fresh items not used in building, for steps 5, 7 and 8.
  Denton's test classification checks that "all the original entities can be described"
  ([§2.3 step 4][den]), but a taxonomy tested only on the items it was built from will
  look better than it is; TnT-LLM chooses between generated taxonomies on a separate
  validation set ([Wan et al. §5.2.2][wan]).
- Sizes (◆ J7, no stored source; prior knowledge): build sample 30 to 60 items, or the
  whole domain if smaller; test sample at least 30 per round, new each round.

## Step 3. Harvest the words

- List every term used for the things in the build sample, and in Jonathan's own words
  about the domain. Count each term's uses across the repo. This is warrant: the words of
  the content, of the users, and of the organization ([Z39.19 §5.3.5][z39]); "enumerate
  important terms" is step 3 of [Noy and McGuinness][noy]; "Entity listing" breaks
  descriptions "into their basic concepts" ([Denton §2.3 step 2][den]). Collect first,
  control later: that is Z39.19's deductive method ([§11.1.3.2a, pp. 91-92][z39]).
- **A model does this pass.** Candidate-term extraction and frequency counts are standard
  machine assistance ([Z39.19 §11.1.3.4, p. 92][z39]). TnT-LLM first summarises each
  item, then proposes and updates a taxonomy batch by batch ([Wan et al. §3][wan]); Clio
  extracts per-item attributes ("facets") and clusters them ([Tamkin et al. §2][tam]).
  Neither has a person deciding in the loop (TnT-LLM adds "a lightweight human
  calibration" afterwards, [§5.3][wan]), but Z39.19 assumes construction "calls for
  intellectual decisions" ([§11.1.3.4][z39]), so **Jonathan decides** in step 6.
- **Group into synonym sets** (several words, one concept) and flag **homonyms** (one
  word, several concepts). Both break naming consistency, and the mix of the two
  "maximizes confusion" ([Deissenboeck and Pizka pp. 267-268][dp]). Expect a lot of
  both: developers choose the same name for the same thing with median probability 6.9%
  ([Feitelson et al. §III][fe]).

## Step 4. Find the facets

- **Compare unlike items** to find the dimensions they share: constant comparison, from
  grounded theory, which Star pairs with facet analysis as two ways of representing
  "vernacular words and processes, empirically discovered" ([Star 1998 pp. 218-224][star]).
  Ask, for example, "how is a review prompt like a UI tell?" (Source-check proposal 2;
  ◆ J13.)
- **Group the harvested terms** into candidate facets, "mutually exclusive and jointly
  exhaustive ... into which all the terms from the previous step will fit"
  ([Denton §2.3 step 3][den]).
- **Check for missed dimensions** against general category lists: thing (continuant),
  quality or function (dependent continuant), process (occurrent) ([OBO Foundry
  Table 1][obo]); Personality, Matter, Energy, Space, Time ([Colon Classification 6th ed.,
  rule 05501][cc]); Vickery's thirteen categories ([ISKO "Facet analysis" §3][isko]).
  These are prompts, not a required set: "there exist no categories that are fundamental
  to all subjects" (Spiteri's Fundamental Categories, [Denton §2.2][den]).
- **Pick the structure the knowledge supports** (S2): fewer than three independent
  dimensions means a list or a grid, not facets ([Denton §§1.1-1.2][den];
  [Kwasnik pp. 33-42][kw]). For each facet, write its question, principle and kind
  ([spec §3](./spec.md#3-facetsmd)), and check S3 and S4.

## Step 5. Test the bare facet list

Before writing any glossary entries, classify about 10 test items with the facet names
and a one-line description of each value, and add, drop or split facets now. Facets are
cheap to change at this point and expensive later: "it is not a simple matter to add
fundamental facets once the general classification is established"
([Kwasnik p. 41][kw]). Denton puts a test classification at the same point
([§2.3 step 4][den]). (Source-check proposal 1; ◆ J13.)

## Step 6. Name and define

For each concept, in this order (N3: concepts, then words, then the name,
[Feitelson et al. §§IV-V][fe]):

1. **Write what the concept is**, in a draft definition (D1) and scope note (D2). A name
   can only be judged against an agreed concept ([Deissenboeck and Pizka
   pp. 268-269][dp]).
2. **Choose the preferred label** from the harvested words by warrant (N2), then apply
   the form rules N4 to N8. Prefer the readers' everyday word (N5). Keep an established
   word unless it misleads (N6).
3. **Record every other word as an alias** or hidden label (spec §4), so readers are
   "led from their own words to your chosen terminology" ([Denton §2.3 step 4][den]).
4. **Fill the remaining fields**: example (D3), near miss (D4), kind (D5), broader (S5),
   facet, warrant, history.
5. **Mark it `candidate`** until step 10 ([Z39.19 §11.1.6, p. 93][z39]).

A model drafts the entries; Jonathan chooses between candidate labels where warrant does
not settle it ([Z39.19 §11.1.5, p. 93][z39]: "In problematic cases, expert advice should
be sought").

## Step 7. Classify fresh items, fix, repeat

1. Classify a fresh test sample using only `facets.md` and `glossary.md`. Note every
   hesitation; put items that fit no value in the facet's **Unsorted** list (S6).
2. Fix what the hesitations show, using only the named operations of
   [spec G4](./spec.md#9-governance-how-a-taxonomy-changes), and log each in
   `changelog.md`. A growing **Unsorted** list means a missing value or facet
   ([Kwasnik pp. 28-29][kw]; [Denton §2.5][den]).
3. Repeat from step 6. Development "is necessarily an iterative process"
   ([Noy and McGuinness §3][noy]); early decisions "may have to be revised as further
   experience is gained" ([Z39.19 §11.1.3.3, p. 92][z39]); Denton's step 7 is "go back
   as many steps as necessary" ([§2.3][den]). TnT-LLM's update prompt does the same per
   batch: evaluate on new data, find issues, modify ([Wan et al. §3][wan]).
4. Run the mechanical tests T1 to T6 after each round.

## Step 8. Agreement test

Two raters classify the same fresh sample independently, using only the files, and
kappa is computed per facet (spec T8, with its rater rules). Where the raters disagree,
the scope notes and near misses of the values involved are rewritten, and the round goes
back to step 7.

- Why: "Indexing experiments where several people index the same items can be very
  useful; disagreements can point out problems in the controlled vocabulary"
  ([Z39.19 §11.2.2, p. 96][z39]). TnT-LLM measures taxonomies the same way, with Cohen's
  and Fleiss' kappa ([Wan et al. §4 and §5.3.2][wan]); its raters' disagreements fell at
  the boundaries between neighbouring labels ([App. B.2.1][wan]), which is what scope
  notes and near misses are for (D2, D4).
- Target (◆ J5): κ ≥ 0.6 per facet. Expert human annotators in TnT-LLM reached 0.553 to
  above 0.6 ([Wan et al. Table 2][wan]), so the first draft's 0.7 would be strict.
  ⚠ Cohen 1960 and the conventional bands (Landis and Koch 1977) are not stored.
- Raters (◆ J6): Jonathan and a model, or two different model families; one value per
  facet; values shuffled for a model rater ([Wan et al. §§5.2.2, 5.3.2][wan]).

## Step 9. Name tests

- **Guess the name** (spec T9): give each preferred label to a fresh reader (a person or
  a new model session with no glossary) and ask what it means. Wrong guesses send the
  label back to step 6 ([Meszaros and Doble, "Evocative Pattern Name"][md]).
- **Look it up** in WordNet: many plain-English senses is a homonym risk
  ([Miller p. 39][wn]).
- Run T3 (name form) and T4 (definition form).

## Step 10. Adopt

When the ending conditions hold (T7, T8, T10, T11 at their targets, T1 to T6 clean),
Jonathan approves: terms move from `candidate` to `approved` ([Z39.19 §11.1.6][z39]) and
`scope.md` status becomes "in use". The glossary need not be complete to be adopted: "A
commitment to a common ontology is a guarantee of consistency, but not completeness"
([Gruber §2][gru]). New concepts are added later through step 12.

## Step 11. Put into use

- Link `taxonomy/glossary.md` from the repo's `CLAUDE.md` / `AGENTS.md` so agents load it
  and use preferred labels.
- Use the language everywhere: "Within a bounded context, use the same language in
  diagrams, writing, and especially speech" ([Evans pp. 3-4][ev]). Rename existing uses
  in the same commit as the decision (G6).
- Add the mechanical checks (T1 to T6) and the alias-drift count (T12) to the repo's
  checks once a script exists (◆ J19).

## Step 12. Maintain

- **Changes** follow [spec §9](./spec.md#9-governance-how-a-taxonomy-changes): anyone
  proposes a `candidate`, the owner decides, every change is a named operation in
  `changelog.md` and the term's history, and nothing is deleted
  ([Z39.19 §§11.3-11.3.2, pp. 96-97][z39]).
- **Reviews**: when the domain is next worked on, and at least each month it is active
  (◆ J10): clear **Unsorted** and candidates, run T12 to T14, and update labels that
  current usage has overtaken (N6; [Z39.19 §11.3.1][z39]: "periodic review of
  terminology"; Canon of Currency, [Ranganathan 1937 pp. 62-72][ran37]).
- **Judge it by use** (T14): whether the work reads more consistently and fewer
  synonyms creep in, not by the size of the glossary ([Gabriel 1996 pp. 57-60][gab96]).
  ⚠ Kundisch et al.'s ex post evaluation is not stored.
- **Across contexts**: once a second domain exists, write `map.md` with `closeMatch` as
  the default (C3), and move only truly shared terms to the shared kernel, changed only
  with every owner's agreement (C2; [Evans p. 31][ev]).

## Light version (small domains)

For a domain of under about 30 items (◆ J7):

1. Steps 0 and 1 as usual.
2. **Before building, hold back a third of the items** (at least 10; if the domain has
   fewer than about 15 items, skip the held-out set and the kappa test altogether and
   rely on T7, T10 and T11). The same reason as step 2: a taxonomy tested on its own
   build items looks better than it is ([Wan et al. §5.2.2][wan]).
3. Steps 3 to 6 in one sitting on the remaining items.
4. One round of step 7 and the agreement test of step 8 on the held-back items, with
   Jonathan and one model as raters. With fewer than 30 items, kappa is recorded as
   **indicative**: it guides fixes but is not an ending condition (spec T8).
5. Adopt when T1 to T7, T10 and T11 pass. Alexander's warning applies most here: keep it piecemeal and inside real work
([Gabriel 2023, App. E.2][gab23]).

## Where models fit

| Step | Model's job | Person's job |
|---|---|---|
| 1 | draft `scope.md` from the repo and Jonathan's notes | set purpose, readers, owner |
| 3 | extract and count terms, group synonyms ([Z39.19 §11.1.3.4][z39]; [Wan et al. §3][wan]) | check the groups |
| 4-5 | propose facets by comparison; test-classify | choose facets |
| 6 | draft entries | choose labels where warrant is split |
| 7 | classify, log hesitations, propose fixes | approve operations |
| 8 | be one rater | be the other rater, or pick a second model family |
| 9 | be the fresh reader | — |
| 11-12 | use the terms; propose candidates; run checks | approve changes |

## Sources cited

Paths are relative to this file. Keys match [`spec.md`](./spec.md#sources-cited), which
lists the full citations.

[cc]: ../sources/ranganathan-prolegomena/ranganathan-1960-colon-classification-6th-ed.ocr.txt
[den]: ../sources/denton-2003-faceted-howto/denton-2003-faceted-howto.html
[dp]: ../sources/deissenboeck-pizka-2006-concise-consistent-naming/deissenboeck-pizka-2006-sqj.pdf
[ev]: ../sources/evans-2003-domain-driven-design/evans-2015-ddd-reference.pdf
[fe]: ../sources/feitelson-2021-how-developers-choose-names/feitelson-2021-how-developers-choose-names.pdf
[gab23]: ../sources/alexander-1964-synthesis-of-form/gabriel-2023-notes-on-notes-on-the-synthesis-of-form.pdf
[gab96]: ../sources/gabriel-1996-patterns-of-software/gabriel-1996-patterns-of-software.pdf
[gru]: ../sources/gruber-1993-ontology-definition/gruber-1993-ksl-92-71.pdf
[hj]: ../sources/hjorland-2017-classification/ieko-classification.html
[isko]: ../sources/isko-encyclopedia/ieko-facet-analysis.html
[kw]: ../sources/kwasnik-1999-classification-structures/kwasnik-1999-classification-structures.pdf
[md]: ../sources/meszaros-doble-1997-pattern-writing/meszaros-doble-1997-pattern-writing.pdf
[noy]: ../sources/noy-mcguinness-2001-ontology-101/noy-mcguinness-2001-ontology-101.html
[obo]: ../sources/arp-smith-spear-2015-bfo/smith-2007-obo-foundry.html
[oc]: ../sources/guarino-welty-ontoclean/guarino-welty-2004-overview-of-ontoclean.pdf
[ran37]: ../sources/ranganathan-prolegomena/ranganathan-1937-prolegomena.pdf
[star]: ../sources/star-1998-grounded-classification/star-1998-grounded-classification.pdf
[tam]: ../sources/tamkin-2024-clio/tamkin-2024-clio.pdf
[wan]: ../sources/wan-2024-tnt-llm/wan-2024-tnt-llm.pdf
[wn]: ../sources/wordnet-1995/miller-1995-wordnet.pdf
[z39]: ../sources/niso-z39-19-2005/ansi-niso-z39-19-2005-r2010.pdf
