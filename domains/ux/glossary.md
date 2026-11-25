# UX taxonomy: glossary

**In one line**: one entry per concept in ux-research, with the word to use, the other
words people use for it, a definition, an example and a near miss.

**In plain words**: when you write about ux-research, use the heading word of the entry.
If you reach for one of its aliases, it points you here. Every entry is a `candidate`
until the agreement test passes (spec G3).

**Status**: round 1 draft, 2026-11-25. General terms only; the facet values are added
once Jonathan has chosen the facets (process step 4). Mode values are here already
because the modes are domain terms whichever facets are chosen.

Field rules: [`design/spec.md` §4](../../design/spec.md#4-glossarymd). Counts:
[`harvest.md`](./harvest.md). Examples link to ux-research at commit `c742019`.

## Label choices for Jonathan's veto (J8)

Where warrant did not settle a label, the approving agent chose one (process step 6):

1. **`surface` now means a tonal layer** (the theme's `--surface-*`), and the screen
   being built is a **`screen`**. The screen sense of "surface" has more uses in the docs
   (31 phrase uses), but the tonal sense is baked into strata-react's token names
   (`--surface-sunken`, `--radius-surface`), which are code and out of scope, and
   "screen" (215) is the commoner word for the other sense anyway. "Operate surface"
   and the like become aliases of the mode entries. Using it means rewording about 31
   phrases in ux-research (G6), which is left for the adopting round.
2. **"Layer" goes to `stack layer`** (the five levels of `ux-react-tailwind.md`). The
   catalogue's "by layer" becomes the facet `aspect` if set A is chosen.
3. **`defect`** for what the repo also calls "quality" findings, because "quality" is
   already in "quality floor" and in everyday use.
4. **`mood word`** rather than "mood" or "vibe", so the entry names the input (an
   adjective in a brief) and not the feeling.
5. **"Signature" goes to `signature move`**; a model's identifying habits are
   **`model signature`**.
6. **`one question` and `one finding`** without the article "the" (N4), with "the one
   question" as an alias.
7. **Definition form for mass nouns and names.** D1 and T4 expect "A <label> is a ...".
   Mass nouns and mode names cannot take "a", so those entries read "<Label> is a ..."
   ("Slop is a property ...", "Operate is a mode ..."). The T4 check should accept both.

## Entries

### brief (`brief`)

- **Definition**: A brief is a request that states what an interface must do and for whom.
- **Scope**: Includes the user's words and the project's written constraints. The brief wins over the skill's defaults, so a tell the brief asks for is built well, not removed.
- **Example**: [SKILL.md, Precedence](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: The subject: the brief is what was asked; the subject is what the product is.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "brief" 56
- **History**: 2026-11-25 added (round 1 harvest)

### character (`character`)

- **Definition**: Character is a property of an interface that gives it a personality taken from its subject.
- **Scope**: Placed by how often a person meets the thing: none on what is used constantly, most at rest (voice, how data is drawn), the delight budget on rare moments.
- **Aliases**: personality, playfulness
- **Example**: [character.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/character.md)
- **Near miss**: Stock whimsy: playfulness that fits any product.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "character" 125, "personality" 17, "playful" 40, "delight" 30
- **History**: 2026-11-25 added (round 1 harvest)

### competitor test (`competitor-test`)

- **Definition**: A competitor test is a check that puts the nearest competitor into a reference sentence to see whether it still works.
- **Scope**: If it still works, the idea belongs to the category and is discarded.
- **Example**: [direction.md §2](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/direction.md)
- **Near miss**: The swap test: the same idea applied to a finished character touch, not to a reference.
- **Kind**: happening
- **Related**: `swap-test`
- **Status**: candidate
- **Warrant**: "competitor test" 8
- **History**: 2026-11-25 added (round 1 harvest)

### dark mode (`dark-mode`)

- **Definition**: Dark mode is a theme variant that sets light content on a dark ground.
- **Scope**: Designed as its own set of token values, not inverted. Excludes `mode`.
- **Example**: [audit.md, Robust](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md)
- **Near miss**: A near-black Persuade page with one neon accent: a tell (wave 2), not a dark-mode theme.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "dark mode" 11
- **History**: 2026-11-25 added (round 1 harvest)

### defect (`defect`)

- **Definition**: A defect is a fault that makes an interface fail some user whatever the brief says.
- **Scope**: Includes accessibility, robustness and input faults: low contrast, no visible focus, blocked paste, a blank render, content left invisible, an error that does not say what failed. Excludes tells, which the brief may ask for.
- **Aliases**: quality issue, quality error
- **Example**: [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md)
- **Near miss**: A font declared but never loaded: listed in the catalogue as a tell, but it is a defect, because no brief asks for a font that does not load.
- **Kind**: thing
- **Related**: `quality-floor`
- **Status**: candidate
- **Warrant**: "defect(s)" 4; `audit.md`: "These are defects, not taste"; `slop-lint` category `quality`
- **History**: 2026-11-25 added (round 1 harvest)

### direction (`direction`)

- **Definition**: A direction is a visual idea chosen for a screen from the subject before any code is written.
- **Scope**: Fixed by one reference sentence and recorded in DESIGN.md. On Operate screens it lends only type, palette, density and one signature move.
- **Aliases**: aesthetic, visual direction
- **Example**: [direction.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/direction.md)
- **Near miss**: A mood word: an input to choosing the direction, not the direction.
- **Kind**: thing
- **Related**: `reference-sentence`, `mood-word`
- **Status**: candidate
- **Warrant**: "direction" 42, "aesthetic(s)" 12
- **History**: 2026-11-25 added (round 1 harvest)

### drift (`drift`)

- **Definition**: Drift is a property of a product whose screens diverge from its own token contract.
- **Scope**: Includes different fonts, palette or radius between pages, invented token names, and a component's old API. Visible only side by side.
- **Aliases**: design drift, cross-page drift
- **Example**: [ui-library/agents.md](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/agents.md)
- **Near miss**: Slop: slop is convergence on the corpus; drift is divergence from one's own system.
- **Kind**: property
- **Related**: `token-contract`
- **Status**: candidate
- **Warrant**: "drift" 15
- **History**: 2026-11-25 added (round 1 harvest)

### editorial (`editorial`)

- **Definition**: Editorial is a treatment that gives a screen a composed, publication-like design meant to be kept or shared.
- **Scope**: Only on Persuade or Experience screens.
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: Broadsheet cosplay (hairlines and dense columns on something that is not a publication): a wave 3 tell.
- **Kind**: property
- **Broader**: `treatment`
- **Status**: candidate
- **Warrant**: "editorial" 15
- **History**: 2026-11-25 added (round 1 harvest)

### Experience (`experience`)

- **Definition**: Experience is a mode in which the person on the screen is inside the work it shows.
- **Scope**: Includes portfolios, galleries and showcases. The work leads and the interface recedes.
- **Aliases**: Experience surface, Experience mode
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: Persuade: a showcase that exists to sell is Persuade.
- **Kind**: property
- **Broader**: `mode`
- **Status**: candidate
- **Warrant**: "Experience" 11
- **History**: 2026-11-25 added (round 1 harvest)

### ground (`ground`)

- **Definition**: A ground is a surface that fills the page behind all other content.
- **Scope**: Includes `--background` and its dark-mode value.
- **Aliases**: page ground, background
- **Example**: [ui-library/tokens.md](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/tokens.md)
- **Near miss**: The background image of a hero: an image on the ground, not the ground.
- **Kind**: thing
- **Broader**: `surface`
- **Status**: candidate
- **Warrant**: "ground" 49, "background" 33, "page ground" 6
- **History**: 2026-11-25 added (round 1 harvest)

### mode (`mode`)

- **Definition**: A mode is a property of a screen that names what the person on it is there to do.
- **Scope**: Has four values: Persuade, Operate, Read and Experience. Decided first, because most rules depend on it. Excludes dark mode (use `dark-mode`).
- **Aliases**: screen mode, surface mode
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: Treatment: the mode says what the screen is for; the treatment says how much decoration it gets.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "mode" 73 (11 of them "dark mode")
- **History**: 2026-11-25 added (round 1 harvest)

### model signature (`model-signature`)

- **Definition**: A model signature is a set of tells that identifies the model or generator that made an interface.
- **Scope**: Includes generator fingerprints left in the code (`lovable-tagger`) and model-family tells (Impeccable's `<codex>` block).
- **Aliases**: generator fingerprint, model-family tell
- **Example**: [ux-slop-taxonomy.md §3g](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3g-signatures-and-drift)
- **Near miss**: A signature move, which is chosen on purpose from the subject.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "model-family" and "generator fingerprint" 3
- **History**: 2026-11-25 added (round 1 harvest)

### moment (`moment`)

- **Definition**: A moment is a rare, earned response in which an interface spends its delight budget.
- **Scope**: One per flow, from the subject, proportional to the stakes, shown once: first use, finishing hard work, recovery.
- **Aliases**: the moment, earned moment
- **Example**: [character.md §4](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/character.md)
- **Near miss**: A celebration on a routine action (confetti on save): stock whimsy.
- **Kind**: happening
- **Status**: candidate
- **Warrant**: "moment" 52 (general word; the repo's sense is "the moment")
- **History**: 2026-11-25 added (round 1 harvest)

### mood word (`mood-word`)

- **Definition**: A mood word is an adjective in a brief that describes the feel wanted for an interface.
- **Scope**: Includes vibes and keywords ("calm", "premium", "fun"). Translated into axes and used to choose a reference, never mapped straight to colours.
- **Aliases**: mood, vibe, keyword
- **Example**: [direction.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/direction.md)
- **Near miss**: A reference sentence: a mood word names a region, a reference names a point.
- **Kind**: thing
- **Related**: `direction`
- **Status**: candidate
- **Warrant**: "mood" 38, "vibe" 9
- **History**: 2026-11-25 added (round 1 harvest)

### one finding (`one-finding`)

- **Definition**: The one finding is a fact in the current data that most needs the attention of a person on an Operate screen.
- **Scope**: Placed where it is read first, next to the action it drives. Excludes linter or review results (lint findings).
- **Aliases**: the one finding
- **Example**: [ui-library/patterns.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/patterns.md#1-before-any-component-mode-question-finding)
- **Near miss**: A KPI: a KPI is always shown; the finding is the one fact that matters today.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "one finding" 11; "finding(s)" in the lint sense 14
- **History**: 2026-11-25 added (round 1 harvest)

### one question (`one-question`)

- **Definition**: The one question is a question that an Operate screen exists to answer.
- **Scope**: Decides what is biggest on the screen. Any block that answers no question is deleted.
- **Aliases**: the one question
- **Example**: [ui-library/patterns.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/patterns.md#1-before-any-component-mode-question-finding)
- **Near miss**: A heading: the question is decided first and may not appear as text.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "one question" 12
- **History**: 2026-11-25 added (round 1 harvest)

### Operate (`operate`)

- **Definition**: Operate is a mode in which the person on the screen completes a task.
- **Scope**: Includes app screens, dashboards, tables, settings, editors and admin. Familiar patterns are a feature here; most character is at rest.
- **Aliases**: Operate surface, Operate mode, product UI
- **Example**: [product-ui.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/product-ui.md)
- **Near miss**: A dashboard on a landing page as decoration (a fake dashboard hero): that screen is Persuade.
- **Kind**: property
- **Broader**: `mode`
- **Status**: candidate
- **Warrant**: "Operate" 97
- **History**: 2026-11-25 added (round 1 harvest)

### palette role (`palette-role`)

- **Definition**: A palette role is a token that names the job a colour does in the theme.
- **Scope**: Includes ground, ink, primary, accent, muted, border, ring and status roles. Excludes ARIA roles.
- **Aliases**: colour role, role
- **Example**: [ux-react-tailwind.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-react-tailwind.md#1-the-layers)
- **Near miss**: A ramp step (`--primary-9`): a step is a position on a scale; a role is a job.
- **Kind**: thing
- **Broader**: `token`
- **Status**: candidate
- **Warrant**: "role(s)" 43, of which palette or colour role 17, ARIA role 10
- **History**: 2026-11-25 added (round 1 harvest)

### Persuade (`persuade`)

- **Definition**: Persuade is a mode in which the person on the screen decides and acts.
- **Scope**: Includes landing, marketing, pricing and launch pages. Ambition shows as one committed visual idea.
- **Aliases**: Persuade surface, Persuade mode, marketing page
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: A tool's own settings page, which is Operate even though the product also has Persuade pages.
- **Kind**: property
- **Broader**: `mode`
- **Status**: candidate
- **Warrant**: "Persuade" 33
- **History**: 2026-11-25 added (round 1 harvest)

### quality floor (`quality-floor`)

- **Definition**: A quality floor is a set of checks that every interface must pass before any taste applies.
- **Scope**: Includes contrast, focus, states, reduced motion, real content and responsive layout, as listed in `audit.md`. Checked after the build, never written into the design prompt.
- **Aliases**: floor, craft floor, audit floor
- **Example**: [ux-slop-taxonomy.md §4](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#4-the-quality-floor-is-a-different-axis)
- **Near miss**: The token contract: also not overridable, but it says how values are expressed, not what must work.
- **Kind**: thing
- **Related**: `defect`
- **Status**: candidate
- **Warrant**: "quality floor" 9, "the floor" 9, "craft floor" 4 (Impeccable's word)
- **History**: 2026-11-25 added (round 1 harvest)

### Read (`read`)

- **Definition**: Read is a mode in which the person on the screen is there to understand something.
- **Scope**: Includes docs, articles, changelogs and help. Ambition shows as measure, hierarchy and navigation.
- **Aliases**: Read surface, Read mode
- **Example**: [ui-library/patterns.md §8](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/patterns.md#8-read-surfaces)
- **Near miss**: An Operate screen with long help text: the task decides the mode, not the amount of text.
- **Kind**: property
- **Broader**: `mode`
- **Status**: candidate
- **Warrant**: "Read surfaces" 7 ("Read" 105, mostly the verb)
- **History**: 2026-11-25 added (round 1 harvest)

### reference sentence (`reference-sentence`)

- **Definition**: A reference sentence is a sentence that names something from the subject's world and the design device it becomes.
- **Scope**: Written in the form "On this screen, [something that belongs to the subject] becomes [the device]". Three are written; one is chosen.
- **Aliases**: reference
- **Example**: [direction.md §2](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/direction.md)
- **Near miss**: A style name ("brutalist", "editorial"): a style fits any subject, so it fails the competitor test.
- **Kind**: thing
- **Related**: `direction`, `competitor-test`
- **Status**: candidate
- **Warrant**: "reference sentence(s)" 12
- **History**: 2026-11-25 added (round 1 harvest)

### screen (`screen`)

- **Definition**: A screen is a page or view of an interface that is designed as one unit.
- **Scope**: Includes landing pages, app screens, dashboards, settings pages and documents. The mode is set per screen, not per product. Previously written "surface" in this sense ("Operate surfaces"); see `surface`.
- **Aliases**: page, view, app screen
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: A component: a screen is made of components and has one job.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "screen(s)" 215, "page(s)" 196, "view(s)" 61, "surface(s)" in "Operate/Persuade surfaces" 31
- **History**: 2026-11-25 added (round 1 harvest)

### signature move (`signature-move`)

- **Definition**: A signature move is a design device taken from the subject that a direction lends to an Operate screen.
- **Scope**: One per screen; usually how the main data is drawn (a timetable's column rhythm, a transit-map status view).
- **Aliases**: signature
- **Example**: [SKILL.md §3](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: A model signature: the habits that identify the model that made a page.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "signature move" 12, "the signature" 7
- **History**: 2026-11-25 added (round 1 harvest)

### silhouette test (`silhouette-test`)

- **Definition**: A silhouette test is a check that compares a page's section order with five competitors' pages.
- **Scope**: Finds the stock section waterfall.
- **Example**: [tells.md, Structure](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md)
- **Near miss**: The competitor test, which checks one idea, not the page outline.
- **Kind**: happening
- **Status**: candidate
- **Warrant**: "silhouette test" 3
- **History**: 2026-11-25 added (round 1 harvest)

### slop (`slop`)

- **Definition**: Slop is a property of an interface whose look comes from defaults nobody chose for its subject.
- **Scope**: Includes the generated look as a whole and any part of it. Excludes faults that stop an interface working (use `defect`); a page can be free of slop and still broken.
- **Aliases**: AI slop, generated median
- **Example**: [ux-slop-taxonomy.md opening](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md)
- **Near miss**: Generic but deliberate design, such as a house style a team chose and wrote down: it is chosen, so it is not slop.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "slop" 194, "AI slop" 8, "generic" 23, "median" 25 (own docs)
- **History**: 2026-11-25 added (round 1 harvest)

### slop-lint (`slop-lint`)

- **Definition**: slop-lint is the source linter of the ux-design skill.
- **Scope**: A proper name. Reports `slop` rules (overridable, P0-P2) and `quality` rules (defects), aware of mode.
- **Aliases**: linter, the linter
- **Example**: [slop-lint.mjs](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/scripts/slop-lint.mjs)
- **Near miss**: A render check, which needs the running page; slop-lint reads only the code.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "slop-lint" 49, "linter" 13
- **History**: 2026-11-25 added (round 1 harvest)

### stack layer (`stack-layer`)

- **Definition**: A stack layer is one of the five levels of a React and Tailwind project where a design decision can live.
- **Scope**: The five: brief and DESIGN.md, theme tokens, primitive variants, composition, call-site className. Excludes the part of the interface a tell is about (the catalogue's "by layer").
- **Aliases**: layer
- **Example**: [ux-react-tailwind.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-react-tailwind.md#1-the-layers)
- **Near miss**: The catalogue's "layer" (colour, typography, ...): a part of the look, not of the code.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "layer(s)" 49, split between this sense and the catalogue's
- **History**: 2026-11-25 added (round 1 harvest)

### stock whimsy (`stock-whimsy`)

- **Definition**: Stock whimsy is slop that comes from a brief asking for fun, made from playful defaults any product could ship.
- **Scope**: Includes confetti, "Oops!", kit illustrations, emoji, bounce and a talking mascot.
- **Aliases**: playful slop
- **Example**: [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md)
- **Near miss**: A moment, which comes from the subject and passes the swap test.
- **Kind**: property
- **Broader**: `slop`
- **Status**: candidate
- **Warrant**: "stock whimsy" 8, "playful slop" 3, "whimsy" 16
- **History**: 2026-11-25 added (round 1 harvest)

### subject (`subject`)

- **Definition**: A subject is the product, place or activity that an interface is for.
- **Scope**: Includes its name, audience, numbers, materials and rituals. Distinctive choices are taken from the subject, not from the product category.
- **Example**: [SKILL.md §2](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: The category (a "SaaS dashboard"): many subjects share a category, and choices taken from it are tells.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "subject" 121
- **History**: 2026-11-25 added (round 1 harvest)

### subject inventory (`subject-inventory`)

- **Definition**: A subject inventory is a list of facts that only one subject has, written before any design choice.
- **Scope**: Includes 8-12 facts, plus 3-5 behaviours when character is added. The source of reference sentences.
- **Aliases**: inventory
- **Example**: [SKILL.md §2](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: A mood board: it collects looks, while the inventory collects facts.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "subject inventory" 6, "inventory" 26
- **History**: 2026-11-25 added (round 1 harvest)

### surface (`surface`)

- **Definition**: A surface is a tonal layer of the theme that content sits on.
- **Scope**: Includes the page ground and the sunken, raised and overlay layers, and the `--surface-*` tokens. Excludes the screen being built, which older text also calls a surface (use `screen`).
- **Aliases**: surface layer, tonal layer
- **Example**: [ui-library/tokens.md §5](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/tokens.md#5-surfaces)
- **Near miss**: A component such as a card: a card sits on a surface and may have one, but is not one.
- **Kind**: thing
- **Related**: `ground`
- **Status**: candidate
- **Warrant**: "surface" 90, of which 31 are the screen sense and the rest this sense or unclear; strata-react token names `--surface-sunken`, `--radius-surface`
- **History**: 2026-11-25 added (round 1 harvest)

### swap test (`swap-test`)

- **Definition**: A swap test is a check that asks whether a neighbouring product could ship a design touch unchanged.
- **Scope**: If it could, the touch is stock whimsy and is replaced from the subject or removed.
- **Example**: [character.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/character.md)
- **Near miss**: The competitor test (see there).
- **Kind**: happening
- **Related**: `stock-whimsy`
- **Status**: candidate
- **Warrant**: "swap test" 12
- **History**: 2026-11-25 added (round 1 harvest)

### tell (`tell`)

- **Definition**: A tell is a design pattern that appears in generated interfaces regardless of their subject.
- **Scope**: Includes patterns in colour, typography, layout, components, imagery, motion and copy. A tell is slop by default and becomes a choice when the brief asks for it with a reason. Excludes defects.
- **Aliases**: AI tell, slop tell, fingerprint
- **Example**: [tells.md, Wave 1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md)
- **Near miss**: A pattern that is common because it works (a top bar with side navigation on an Operate screen): it is expected there, so it is not a tell.
- **Kind**: thing
- **Related**: `slop`, `tell-registry`
- **Status**: candidate
- **Warrant**: "tell(s)" 154 (own docs); `tells.md` defines it
- **History**: 2026-11-25 added (round 1 harvest)

### tell registry (`tell-registry`)

- **Definition**: A tell registry is a dated list of tells grouped by wave, with how each is detected.
- **Scope**: Names what to avoid and never what to use instead. Reviewed each quarter.
- **Aliases**: registry, dated registry
- **Example**: [tells.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md)
- **Near miss**: The tell catalogue in `ux-slop-taxonomy.md` §3: the research behind the registry, with sources and severity.
- **Kind**: thing
- **Related**: `wave`, `tell`
- **Status**: candidate
- **Warrant**: "registry" 24
- **History**: 2026-11-25 added (round 1 harvest)

### theme (`theme`)

- **Definition**: A theme is a set of token values generated for one product from its subject.
- **Scope**: Includes light and dark values. strata-react ships no theme; each product makes its own.
- **Example**: [ui-library/README.md](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/README.md)
- **Near miss**: A direction: the direction is the idea; the theme is its values.
- **Kind**: thing
- **Related**: `token`
- **Status**: candidate
- **Warrant**: "theme" 100
- **History**: 2026-11-25 added (round 1 harvest)

### token (`token`)

- **Definition**: A token is a named design value that components read instead of a literal value.
- **Scope**: Includes colour roles, type steps, radius, elevation, motion and density, as CSS variables in `@theme` and `:root`.
- **Aliases**: design token, CSS variable
- **Example**: [ui-library/tokens.md](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/tokens.md)
- **Near miss**: A Tailwind utility class such as `bg-primary`: the class uses the token; it is not the token.
- **Kind**: thing
- **Status**: candidate
- **Warrant**: "token(s)" 123
- **History**: 2026-11-25 added (round 1 harvest)

### token contract (`token-contract`)

- **Definition**: A token contract is an agreement that every colour, type, radius, shadow and motion value in a project comes from its tokens.
- **Scope**: Written once in DESIGN.md and the theme; agents read it and never regenerate it. A literal value at a call site breaks it.
- **Example**: [ui-library/tokens.md](https://github.com/jburnhams/ux-research/blob/c742019/ui-library/tokens.md)
- **Near miss**: The theme: the theme is the set of values; the contract is the rule that only those values are used.
- **Kind**: thing
- **Related**: `token`, `theme`, `drift`
- **Status**: candidate
- **Warrant**: "token contract" 14
- **History**: 2026-11-25 added (round 1 harvest)

### treatment (`treatment`)

- **Definition**: A treatment is a property of a screen that sets how much decoration it carries.
- **Scope**: Has two values: utilitarian and editorial. Most screens are utilitarian.
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: Mode: see the near miss on `mode`.
- **Kind**: property
- **Status**: candidate
- **Warrant**: "treatment" 9 (from Claude `artifact-design`)
- **History**: 2026-11-25 added (round 1 harvest)

### utilitarian (`utilitarian`)

- **Definition**: Utilitarian is a treatment that gives a screen considered hierarchy, spacing and palette and no flourishes.
- **Scope**: The default treatment.
- **Example**: [SKILL.md §1](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/SKILL.md)
- **Near miss**: Plain or unstyled: utilitarian screens still have a real palette and type scale.
- **Kind**: property
- **Broader**: `treatment`
- **Status**: candidate
- **Warrant**: "utilitarian" 10
- **History**: 2026-11-25 added (round 1 harvest)

### wave (`wave`)

- **Definition**: A wave is a period in which one set of tells spread, often from the published fix for the set before.
- **Scope**: Four so far: the median (2023-24), the decorated median (2025), the tasteful escape (2025-26) and one forming in late 2026. A property of the registry, not of every item.
- **Example**: [ux-slop-taxonomy.md §2](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#2-the-waves-why-every-list-goes-stale)
- **Near miss**: Drift: a wave is across products over time; drift is within one product.
- **Kind**: happening
- **Related**: `tell-registry`
- **Status**: candidate
- **Warrant**: "wave(s)" 31
- **History**: 2026-11-25 added (round 1 harvest)
