# Method version 1.1: changes for large domains (proposed)

**In one line**: seven changes to process v1 and spec v1 that the prompts domain needs
because it is about thirty times the size of ux: build in stages, draw samples by a
written rule, test on more items, rate with three model families, and say how a rater run
through an agent CLI is kept clean.

**In plain words**: the ux taxonomy was built from about 100 short catalogue rows; one
pass and two raters were enough. The prompts repo has about 1,000 sections over 815,000
words. Doing it in one pass would mean hundreds of words tested on 30 items, which shows
little about any one of them. So we split the work into stages, test on bigger samples,
and use three raters instead of two, one of them not from the family that wrote the
definitions.

**Status**: proposed 2026-11-26, not adopted (◆ J20-J26 in
[`decisions.md`](./decisions.md)). The prompts domain (`domains/prompts/`) follows these
proposals while they are open, as v1 did with its open recommendations; each one says
what it changes. When Jonathan adopts them, they are folded into
[`process.md`](./process.md) and [`spec.md`](./spec.md) and both become version 1.1.
Citations follow the spec's rules: a stored source with page or section, ⚠ where the
best source is not stored, "reasoning" where none is claimed.

## Why v1 needs changing

v1 was written before any domain was built, and its sizes (J7: build 30-60, test 30) were
"prior knowledge" with no stored source ([`process.md` step 2](./process.md#step-2-collect-the-samples)).
ux met them easily: 53 build items, κ 0.78-1.00 on 30 items. The prompts repo differs in
three ways that matter:

1. **Size**: 1,070 sections in the analysis docs alone, 584 left after filtering
   (`domains/prompts/samples.md`), against ux's 109 items in total.
2. **Many areas**: tools, context, control, coordination, output, evals and operations
   each have their own vocabulary (approval modes, risk dimensions, memory types), and
   their own existing classifications inside the docs.
3. **The author is a rater**: Claude drafts the definitions and is rater A, so agreement
   between Claude and one other model partly measures how well the other model reads
   Claude's prose (reasoning; not a stored finding).

## M1. Build a large domain in stages, inside one context (◆ J20)

- **Change**: when a domain has more than about 300 candidate items or more than about
  six distinct areas, build it in stages. **Stage 1** covers the kernel (the words every
  area uses) and one facet that sorts every item into an area. **Each later stage** takes
  one area, adds facets that only make sense there, and adds that area's terms. Every
  stage is a full run of steps 2-10, with its own samples, rounds and adoption. All
  stages share one `domains/<name>/` folder and one glossary, so a word keeps one
  meaning across areas.
- **Why**: Ranganathan's Colon Classification gives each main class its own facet
  formula, so History is sorted by "[Community], [Constituent]: [Problem]. [Period]"
  while other classes have their own ([Colon Classification 6th ed., rules 05112-05114][cc]).
  A domain's areas are main classes in this sense. Splitting into separate bounded
  contexts instead would let one word mean two things in two areas, which a context
  exists to stop ([Evans p. 2][ev]); shared terms across contexts need a shared kernel
  that changes only with every owner's agreement ([Evans p. 31][ev]), which is heavy for
  one owner. Denton's step 1 already says "In a large domain, get enough to cover all
  foreseen possibilities" ([Denton §2.3 step 1][den]); staging is how to do that without
  testing everything at once. Clio does the same thing at scale: base clusters first,
  then "a multi-level hierarchy" over them ([Tamkin et al. §2][tam]).
- **Changes**: process steps 1 and 2 (stages are written in `scope.md`); spec §2 adds a
  **Stages** field to `scope.md`.

## M2. Write the item unit and population down, and draw by a seeded rule (◆ J21)

- **Change**: before drawing, `samples.md` states what one item is, which files the
  population comes from, the filters, and the seed. Items are drawn by a script stored
  with the samples, shuffled within and across sources and taken source by source, so
  every source gives a few items before any gives many. Hand removals are listed by
  position.
- **Why**: Denton asks for a "representative sample" chosen for variety
  ([§2.3 step 1][den]); with 584 candidates nobody can choose that by eye, and a hand
  pick by the author of the definitions would favour items that fit them (reasoning). A
  separate validation sample is how TnT-LLM chooses between taxonomies
  ([Wan et al. §5.2.2][wan]); a written rule keeps the held items honestly unseen. A
  stored script makes the draw checkable (reasoning).
- **Changes**: process step 2; spec §1 lists the sample script beside `samples.md`.

## M3. Test sample: at least 30, and at least 5 per value of the largest facet (◆ J22)

- **Change**: each round's fresh sample is at least 30 items **and** at least five times
  the number of values in the largest facet. For prompts stage 1 (`area` has 8 values)
  that is 40; the domain uses 60, the round size J7 allowed for building.
- **Why**: T8 already asks that "every value [be] used at least once" ([spec T8](./spec.md#judgement-while-building-and-at-each-review)),
  and a value used once cannot show whether raters agree on it. Five per value is prior
  knowledge, not a stored rule: kappa on few items "has a wide margin of error" is the
  reason J7 gave, and its margin shrinks roughly with the square root of the sample.
  ⚠ Tullis and Wood 2004 (card-sort sample size) is in [`to-fetch.md`](../to-fetch.md)
  and may give a sourced figure; check this rule when it is read.
- **Changes**: process step 2 and spec T8 (sample line); J7 stays as the floor.

## M4. Three raters from three families, scored with Fleiss' and pairwise kappa (J23, adopted by Jonathan 2026-11-26)

- **Change**: T8 uses three raters, each from a different model family, each the
  strongest model that family offers on Jonathan's plans at the time (for 2026-11:
  Claude, an OpenAI model through `codex exec`, and a Gemini Pro model through
  Antigravity's `agy -p`; not a Flash model). The ending condition becomes **Fleiss' κ ≥
  0.6 on every facet across all three, and Cohen's κ ≥ 0.6 on every facet between the two
  raters not from the family that drafted the definitions.** Pairwise Cohen's κ for all
  three pairs is reported.
- **Why**: Jonathan asked for "more / better llm judges - openai and agy with a better
  gemini than flash" (2026-11-26). TnT-LLM reports Cohen's kappa "between two raters and
  Fleiss' Kappa among multiple raters" ([Wan et al. §5.2.3][wan]), so the measure for
  three raters is the one it uses, and the 0.6 target (J5) carries over. The non-author
  pair is the reasoning in "Why v1 needs changing", item 3: if two models that did not
  write the prose agree, the prose is clear to readers other than its author. GPT-4
  agreed with the human majority better than humans agreed with each other on single
  labels ([Wan et al. §5.2.3][wan]), which is the evidence that model raters are worth
  using at all; it says nothing about which families, so the strongest-model rule is
  Jonathan's decision, not a sourced one.
- **Changes**: spec T8 rater rules and target; `tools/kappa.py` takes any number of
  raters (done: it prints Fleiss' κ and every pair's Cohen's κ).

## M5. With three raters, the majority answer is the round's label (◆ J24)

- **Change**: an item where two of three raters agree takes that value for T7; an item
  where all three differ goes to the facet's **Unsorted** list and is the first thing the
  next round's fixes address. Fixes still use the disagreements, not the majority.
- **Why**: TnT-LLM resolves "disagreements between human annotations by either voting or
  deliberation" and then treats the consensus as the reference ([Wan et al.
  §4.2][wan]). Disagreements "can point out problems in the controlled vocabulary"
  ([Z39.19 §11.2.2, p. 96][z39]), and a three-way split is the strongest sign of one.
- **Changes**: spec T7 and T8; process step 8.

## M6. A rater run through an agent CLI is kept to the prompt (◆ J25)

- **Change**: when a rater is called through a vendor's agent CLI rather than an API
  (Jonathan's ChatGPT and Google AI plans have no API credit), run it in a new, empty
  directory, read-only, with tools and web access off where the CLI allows, the whole
  rater prompt as the only user input, and record the CLI name and version, the model,
  the reasoning effort and the date. The CLI's own system prompt cannot be removed; say
  so in `results.md`. Never route the CLIs' sign-ins through a proxy.
- **Why**: T8's rule is that raters work "using only `facets.md` and `glossary.md`"
  ([spec T8](./spec.md#judgement-while-building-and-at-each-review)); a CLI in a repo
  checkout could read the repo and the other rater's answers (reasoning). The proxy rule
  is from Jonathan's machine notes (`jburnhams/docs`, `tech/code/strata-models/log.md`:
  Google disables accounts for it).
- **Changes**: process step 8; each round's `README.md`.

## M7. An item is a section's heading and its opening text, and raters sort the mechanism (◆ J26)

- **Change**: where items are sections of prose rather than catalogue rows, each item is
  the heading plus the first lines under it (up to about 300 characters), and the rater
  prompt says to classify the mechanism the section describes, not the doc it is in.
- **Why**: in the prompts bare-facet test, two of twelve headings (`t08`, `t11`) named a
  design change rather than a mechanism, and the heading alone did not say what
  decided or when (`domains/prompts/facets.md`). ux's items were one-line rows that
  already named the thing; Denton's test classification checks that "all the original
  entities can be described" ([§2.3 step 4][den]), which needs enough text to describe.
- **Changes**: process steps 2 and 5.

## Not changed

- **κ ≥ 0.6** (J5) and **two families at least** (J6): M4 adds a third, it does not
  replace the rule.
- **Agents approve, Jonathan can veto** (J8): each stage is adopted the same way.
- **The light version** for small domains: unchanged; M1-M3 apply only above its size.

## Sources cited

[cc]: https://github.com/jburnhams/taxonomies-sources/blob/main/ranganathan-prolegomena/ranganathan-1960-colon-classification-6th-ed.ocr.txt
[den]: https://github.com/jburnhams/taxonomies-sources/blob/main/denton-2003-faceted-howto/denton-2003-faceted-howto.html
[ev]: https://github.com/jburnhams/taxonomies-sources/blob/main/evans-2003-domain-driven-design/evans-2015-ddd-reference.pdf
[tam]: https://github.com/jburnhams/taxonomies-sources/blob/main/tamkin-2024-clio/tamkin-2024-clio.pdf
[wan]: https://github.com/jburnhams/taxonomies-sources/blob/main/wan-2024-tnt-llm/wan-2024-tnt-llm.pdf
[z39]: https://github.com/jburnhams/taxonomies-sources/blob/main/niso-z39-19-2005/ansi-niso-z39-19-2005-r2010.pdf
