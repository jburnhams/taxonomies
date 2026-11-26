# UX taxonomy: facets

**In one line**: four proposed sorting questions for every tell and quality check (which
part of the interface, can the brief allow it, how is it found, on which surfaces does it
count), awaiting Jonathan's choice.

**In plain words**: a facet is a question you can ask of any item, with a short list of
answers. Each item gets one answer per question. With four questions you can find, for
example, "every slop tell in the copy that a linter can catch on Operate screens" without
a special list for it.

**Status**: set A chosen by Jonathan, 2026-11-25 (process step 4); in use after round 1,
2026-11-26 (κ 0.78 to 1.00 per facet). Every value has a
glossary entry in [`glossary.md`](./glossary.md), status `candidate`. Sets B to D are kept
below as the record of what was weighed.

## How these were found

- **Compared unlike items** (process step 4, constant comparison): a purple gradient
  (`b01`), a missing focus ring (`b42`), stock whimsy copy (`t09`) and a three-tier pricing
  block (`b19`) share four things worth asking: what part of the interface each is in;
  whether a brief could ask for it (b01 and b19 yes, b42 no); how you would find it
  (b01 by reading the code, b19 only by judging the page against the brief); and whether
  it counts on every screen (b42) or only on a landing page (b19).
- **Checked against general categories** (OBO Foundry Table 1; Vickery's list, ISKO §3):
  *aspect* is a part of the thing (continuant), *brief override* and *mode* are qualities
  of the item, *detection* is about a process (finding it). Nothing about time came up as
  a facet: the **wave** of a tell is a date on the registry and applies to slop only, so it
  stays a field of the registry, not a facet (it fails "jointly exhaustive" on defects).
- **Structure (spec S2)**: four independent dimensions, so facets rather than a list or a
  grid. Independence check on the build sample: colour, typography, layout, motion and
  copy each occur with both slop and defect; detection and mode vary within every aspect
  that has more than three items. Component has no defect and interaction no slop in
  the build sample; round 1 will show whether that is a gap in the sample or a dependency.
- **Reused what exists** (step 0): the catalogue in `ux-slop-taxonomy.md` §3 already has
  aspect ("by layer"), detection (src/render/judge) and severity (P0-P2); §4 names the
  slop/quality split as "a different axis"; `SKILL.md` §1 has the modes.

## Set A (chosen): aspect, brief override, detection, mode

### Aspect (`aspect`)

- **Question**: Which part of the interface is it about?
- **Principle**: the design property or interface part that has to change to remove it.
- **Kind**: thing
- **Values**: `colour`, `typography`, `layout`, `component`, `imagery`, `motion`, `copy`, `interaction`
- **Order**: as the catalogue orders its sections, from the ground up to behaviour
  (colour, typography, layout, component), then imagery and motion, then words, then input.
- **Unsorted**: `r20` (the page renders blank; a whole-page failure, not one part), 2026-11-26. Both raters put it under `component`, neither sure.
- **Agreement**: κ = 0.92 (93% agreement), round 1, 2026-11-25, 30 fresh items, Claude and Gemini 3.8 Flash ([results](./rounds/round-1/results.md)).

This is the catalogue's "layer". It is not labelled "layer" because `ux-react-tailwind.md`
uses "layer" for the five layers of the stack (harvest homonym 2), and not "element"
because a React element is a code object. `typography` replaces the catalogue's "type",
which N4 bars as a claim word and which reads as "kind".

### Brief override (`brief-override`)

- **Question**: Can the brief allow it?
- **Principle**: whether a stated reason in the brief makes it acceptable.
- **Kind**: property
- **Values**: `slop` (yes: a default nobody chose; the brief may ask for it, with a reason),
  `defect` (no: it fails some user whatever the brief says)
- **Order**: slop, defect (the repo's own order: slop axis, then quality axis).
- **Unsorted**: none yet.
- **Agreement**: κ = 0.92 (97%), round 1, 2026-11-25, 30 fresh items, Claude and Gemini 3.8 Flash ([results](./rounds/round-1/results.md)).

The repo already splits these as `slop` and `quality` lint categories and as two axes
(`ux-slop-taxonomy.md` §4: "Brief can override? Yes, always / No"). The facet is named by
that question because both "axis" (also "named axes" of a direction) and "quality" (also
"quality floor", "quality rules") are taken.

### Detection (`detection`)

- **Question**: What is the least you need to find it?
- **Principle**: the evidence needed: the code, the running page, or the brief.
- **Kind**: property
- **Values**: `code` (reading the source finds it, by eye or by a rule such as
  `slop-lint`), `render` (it needs the page running: pixels, computed styles, a keyboard
  pass), `judgement` (it needs the brief or the subject to decide)
- **Order**: from least evidence to most.
- **Unsorted**: none yet.
- **Agreement**: κ = 0.78 (90%), round 1, 2026-11-25, 30 fresh items, Claude and Gemini 3.8 Flash ([results](./rounds/round-1/results.md)).

Rule for raters: take the least evidence that finds the item as written. Whether the
brief allows it is the other facet, so a slop tell that a rule can find is `code`, not
`judgement`. Not labelled "source" because the repo's "sources" are its research
folders (harvest homonym 7); `src` and `lint` become aliases of `code`.

### Mode (`mode`)

- **Question**: On which surfaces does it count?
- **Principle**: the narrowest set of modes the repo says it applies to.
- **Kind**: property
- **Values**: `any-mode`, `persuade`, `operate`
- **Order**: widest first.
- **Unsorted**: none yet.
- **Agreement**: κ = 1.00 (100%), round 1, 2026-11-25, 30 fresh items, Claude and Gemini 3.8 Flash ([results](./rounds/round-1/results.md)).

Read and Experience are modes (and glossary terms) but no item so far applies only to
them, so they are not values yet (T6: no empty value). An item that applies to two modes
but not all goes to **Unsorted**, and the value list is revisited if that happens.

## Other sets considered

| Set | Facets | For | Against |
|---|---|---|---|
| **B** the catalogue's own | aspect ("layer"), severity (P0/P1/P2), detection | no relabelling of the catalogue; severity says who notices | severity has no value for defects (the audit and the registry carry none: 0 of the 10 bare-test items could be rated from the repo), so it fails "jointly exhaustive" (S3); the slop/defect split, the repo's main decision (§4), is missing |
| **C** set A plus fix layer | A + "where the fix goes" (brief, tokens, variants, composition, call site, content: `ux-react-tailwind.md` §1) | the most useful answer for an agent fixing things | follows from aspect most of the time (colour → tokens, copy → content), so it adds little sorting; a rough pass over the build sample (not recorded item by item) gave two plausible layers for about a quarter of the items, so it risks failing κ ≥ 0.6 now |
| **D** two only | aspect × brief override, as a grid (S2) | fewest decisions, highest agreement | loses the questions the skill acts on: what a linter can own, and which rules are mode-dependent (competency questions 1 and 2) |

Severity and wave stay as fields on the catalogue and registry rows; they are not lost.

## Step 4: build sample under set A

The first 48 items of [`samples.md`](./samples.md) (the five moved in later are
classified in round 1). Counts: aspect colour 10, typography 8,
component 8, layout 7, copy 7, motion 5, interaction 3, imagery 0; brief override slop 38,
defect 10; detection code 35, render 9, judgement 4; mode any-mode 33, persuade 14,
operate 1. 22 of 48 items had a hesitation (noted below), mostly on aspect.

| ID | Aspect | Brief override | Detection | Mode | Hesitation |
|---|---|---|---|---|---|
| `b01` | colour | slop | code | any |  |
| `b02` | colour | slop | code | any |  |
| `b03` | colour | slop | code | any | colour or type: the fill is colour, the target is text; colour (the tell is the gradient) |
| `b04` | colour | slop | code | any | colour or component (shadow is elevation); colour, because the tell is the hue |
| `b05` | colour | slop | code | Persuade | "behind the hero" ties it to Persuade |
| `b06` | colour | slop | code | any |  |
| `b07` | colour | slop | code | any | detection: the catalogue says src, tells.md says judge |
| `b08` | colour | slop | code | any | colour or component (a card) |
| `b09` | typography | slop | code | Persuade | tells.md and slop-lint skip it on Operate |
| `b10` | typography | slop | code | Persuade |  |
| `b11` | typography | slop | code | Persuade | detection: catalogue src, tells.md judge |
| `b12` | typography | slop | code | Persuade |  |
| `b13` | typography | slop | code | any | slop-lint allows one on Operate: still "any" |
| `b14` | typography | slop | render | Persuade |  |
| `b15` | layout | slop | code | Persuade | detection: code finds the parts, judgement decides the whole |
| `b16` | layout | slop | code | Persuade | layout or component (cards) |
| `b17` | layout | slop | judgement | Persuade |  |
| `b18` | copy | slop | code | Persuade | layout (a strip) or copy (invented numbers) |
| `b19` | layout | slop | judgement | Persuade | catalogue src, tells.md judge |
| `b20` | layout | slop | judgement | Persuade | catalogue src, tells.md judge |
| `b21` | layout | slop | render | any |  |
| `b22` | component | slop | code | any |  |
| `b23` | component | slop | code | any | component or colour; radius and shadow have no aspect of their own |
| `b24` | component | slop | render | any | catalogue src, tells.md render |
| `b25` | component | slop | code | any |  |
| `b26` | component | slop | code | any | component or imagery (an icon) |
| `b27` | component | slop | render | any |  |
| `b28` | component | slop | code | any |  |
| `b29` | component | slop | code | Operate | component or content (no data behind it) |
| `b30` | motion | slop | code | any |  |
| `b31` | motion | slop | code | any |  |
| `b32` | motion | slop | code | any |  |
| `b33` | motion | slop | code | any |  |
| `b34` | copy | slop | code | any |  |
| `b35` | copy | slop | code | Persuade |  |
| `b36` | copy | slop | code | Persuade |  |
| `b37` | copy | slop | code | any |  |
| `b38` | copy | slop | code | any |  |
| `b39` | colour | defect | render | any |  |
| `b40` | colour | defect | judgement | any | needs to know which colours carry status |
| `b41` | typography | defect | render | any | type or layout (line length) |
| `b42` | interaction | defect | code | any |  |
| `b43` | interaction | defect | render | any | interaction or layout (target size) |
| `b44` | motion | defect | code | any |  |
| `b45` | interaction | defect | code | any |  |
| `b46` | copy | defect | code | any | copy or content (number format) |
| `b47` | layout | defect | render | any | bundles three checks: overflow, truncation, empty and error states |
| `b48` | typography | defect | render | any |  |
What the build sample showed:

- **The catalogue mixes the two axes.** `ux-slop-taxonomy.md` §3 lists "Font declared in
  CSS but never loaded" (P1) and "Content left at `opacity: 0`" (marked **error**) among
  the slop tells. Under brief override both are defects: no brief asks for an invisible
  page. Reported to ux-research, not changed there.
- **The catalogue and the registry disagree on detection** for five items (`b07`, `b11`,
  `b19`, `b20`, `b24`: `src` in one, `judge` or `render` in the other). The rater rule
  above ("least evidence that finds it as written") is the fix; whichever is right, the
  two files should agree.
- **Aspect boundaries**: shadow and radius (b04, b23) have no aspect of their own and split
  between colour and component; icons (b26) between component and imagery. These need
  scope notes and near misses in the glossary (D2, D4).

## Step 5: bare-facet test (10 fresh items)

The facet names and one-line value descriptions only, before any glossary entry, on the
ten items of [`samples.md`](./samples.md#bare-facet-test-10). All ten got a value on every
facet; nothing went to Unsorted. 9 of 10 had a hesitation.

| ID | Aspect | Brief override | Detection | Mode | Hesitation |
|---|---|---|---|---|---|
| `t01` | colour | defect | render | any | bundles three targets |
| `t02` | imagery | defect | code | any | bundles alt text and dimensions |
| `t03` | layout | defect | render | any | bundles reflow (render) and user-scalable (code); layout or type |
| `t04` | interaction | defect | render | any | needs a keyboard pass: "render" has to mean "the running page", not only pixels |
| `t05` | colour | slop | code | Operate | colour or layout (the sidebar); code or render |
| `t06` | component | slop | code | Operate | b26 is the same device and was "any" |
| `t07` | component | slop | code | Operate | component or imagery (sparkline) |
| `t08` | motion | slop | code | any | motion or imagery |
| `t09` | copy | slop | code | any |  |
| `t10` | copy | defect | code | any | tells.md lists it as a tell; audit.md's rule ("errors ... specific") makes it a defect |
Changes made because of it (logged in [`changelog.md`](./changelog.md)):

1. **`render` now means "the running page"**, not "pixels": a keyboard pass (`t04`) needs
   the page running but no screenshot.
2. **`imagery` kept** as an aspect value: the first image check (`t02`) had nowhere else
   to go, and the build sample has illustration and mascot items (`r07`, `r09`, moved there
   from the round-1 test for that reason).
3. **The "least evidence" rule** for detection, written above, after `t03` and `t05`.
4. **Bundled items** (`t01`, `t02`, `t03`, and `b47`) hold two or three checks with
   different answers. Items stay as the repo writes them, so raters take the first check
   named. Suggested for ux-research: one check per audit line.
5. **Mode**: `t06` (four KPI cards with tinted icon circles) is the dashboard form of
   `b26` (icon chip, any mode). Recorded as `operate` because the registry files it under
   Generated dashboards; a near miss for the glossary.
6. **Slop or defect**: `t10` ("Something went wrong") is in the registry as a tell but
   fails `audit.md`'s rule that errors are specific. Scope note for `defect`: an error
   message that does not say what failed is a defect.
