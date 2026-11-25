# Rater prompt: ux taxonomy, round-1

You are classifying 30 items for a taxonomy agreement test. Use only the definitions below; do not look anything up and do not use other knowledge of the repos they come from.

Each item is one entry from a research repo about generated React + Tailwind interfaces: a tell (a design habit that shows up whatever the product is) or a quality check. The `from` column says which file and section it came from, which is part of the item.

For every item, answer all four questions with exactly one value each, chosen from the list for that question. If no value fits, still pick the closest one and write `unsure` plus a few words in the note column.

Rules:
- Aspect: the part of the interface that has to change to remove the problem.
- Brief override: `slop` if a brief could ask for it with a reason, `defect` if it fails some user whatever the brief says.
- Detection: the least evidence that finds the item as written. `code` if reading the source is enough, `render` if the page has to be running, `judgement` if you need to know the brief or the subject. Whether the brief allows it is the other question.
- Mode: the narrowest set of screens the item applies to, as written. `any-mode` unless the item or its section ties it to Persuade (landing, marketing, pricing) or Operate (app screens, dashboards, tables, settings) screens.
- If an item bundles several checks, classify the first one named.

Answer as CSV only, with this header and one row per item, in the items' order:

```
id,aspect,brief_override,detection,mode,note
```

## The questions and their values

- **aspect**: Which part of the interface is it about? Values: `component`, `copy`, `typography`, `motion`, `interaction`, `colour`, `imagery`, `layout`
- **brief_override**: Can the brief allow it? Values: `slop`, `defect`
- **detection**: What is the least you need to find it? Values: `code`, `render`, `judgement`
- **mode**: On which screens does it count? Values: `persuade`, `operate`, `any-mode`

## Definitions of the values

### layout (`layout`)

- **Definition**: Layout is an aspect of an interface that covers the arrangement, alignment, spacing and order of its blocks and sections.
- **Scope**: Includes section order, centring, widths, grids, spacing rhythm, reflow and overflow.
- **Aliases**: page structure, structure, spacing
- **Near miss**: A row of identical cards: layout when the item names the arrangement (three in a row, a stock order), `component` when it names how the card is styled (stripe, shadow, nesting).
- **Kind**: thing
- **Facet**: `aspect`

### component (`component`)

- **Definition**: A component is an aspect of an interface that covers which UI parts are used and how each is shaped and configured.
- **Scope**: Includes cards, badges, chips, buttons, modals, charts as parts, and their radius, borders and shadows. Excludes the icon or picture inside a part (use `imagery`).
- **Aliases**: components, chrome, UI part
- **Near miss**: An icon in a tinted square chip: the chip is the tell, so it is component; the choice of which icons to draw is imagery.
- **Kind**: thing
- **Facet**: `aspect`

### render (`render`)

- **Definition**: Render is a detection method that needs the page running to find an item.
- **Scope**: Includes pixels, computed styles, layout measurements and a keyboard or screen-reader pass.
- **Aliases**: browser check, running page
- **Near miss**: A font declared but never loaded: the declaration is in the code, but whether it loaded needs the render.
- **Kind**: property
- **Facet**: `detection`

### code (`code`)

- **Definition**: Code is a detection method that finds an item by reading the source.
- **Scope**: Includes rules in `slop-lint` and anything a reader of the source could spot without running it. Take it whenever reading the code is enough, even if the brief may still allow the item.
- **Aliases**: src, lint, source check
- **Near miss**: A contrast check on token pairs done by `palette.mjs`: it reads values, not the page, so it is code; a contrast check on the rendered overrides is render.
- **Kind**: property
- **Facet**: `detection`

### slop (`slop`)

- **Definition**: Slop is a property of an interface whose look comes from defaults nobody chose for its subject.
- **Scope**: Includes the generated look as a whole and any part of it. Excludes faults that stop an interface working (use `defect`); a page can be free of slop and still broken.
- **Aliases**: AI slop, generated median
- **Near miss**: Generic but deliberate design, such as a house style a team chose and wrote down: it is chosen, so it is not slop.
- **Kind**: property
- **Facet**: `brief-override`

### typography (`typography`)

- **Definition**: Typography is an aspect of an interface that covers its typefaces, sizes, weights, tracking, line length and line height.
- **Scope**: Includes font choice and loading, the type scale, casing of headings and display headlines.
- **Aliases**: type, fonts
- **Near miss**: The words of a headline: what it says is `copy`; how it is set is typography.
- **Kind**: thing
- **Facet**: `aspect`

### motion (`motion`)

- **Definition**: Motion is an aspect of an interface that covers animation, transitions, easing and anything that moves on its own.
- **Scope**: Includes entrance animations, hover lifts, loops, count-ups, celebrations and reduced-motion handling.
- **Aliases**: animation
- **Near miss**: A slow response to a click: the wait is `interaction` (what happens when the person acts), not motion.
- **Kind**: thing
- **Facet**: `aspect`

### imagery (`imagery`)

- **Definition**: Imagery is an aspect of an interface that covers its icons, illustrations, images, emoji and mascots.
- **Scope**: Includes icon sets, illustration kits, image alt text and dimensions.
- **Aliases**: icons, illustration, images
- **Near miss**: A decorative sparkline: a chart drawn as decoration is a `component`, not an image.
- **Kind**: thing
- **Facet**: `aspect`

### interaction (`interaction`)

- **Definition**: Interaction is an aspect of an interface that covers how it responds to a person's input.
- **Scope**: Includes keyboard access, focus, hit targets, form behaviour, semantic controls and what happens after an action.
- **Aliases**: behaviour, input
- **Near miss**: A hover lift on every card: it moves, so it is `motion`; it does not change what the input does.
- **Kind**: thing
- **Facet**: `aspect`

### Persuade (`persuade`)

- **Definition**: Persuade is a mode in which the person on the screen decides and acts.
- **Scope**: Includes landing, marketing, pricing and launch pages. Ambition shows as one committed visual idea.
- **Aliases**: Persuade surface, Persuade mode, marketing page
- **Near miss**: A tool's own settings page, which is Operate even though the product also has Persuade pages.
- **Kind**: property
- **Broader**: `mode`
- **Facet**: `mode`

### defect (`defect`)

- **Definition**: A defect is a fault that makes an interface fail some user whatever the brief says.
- **Scope**: Includes accessibility, robustness and input faults: low contrast, no visible focus, blocked paste, a blank render, content left invisible, an error that does not say what failed. Excludes tells, which the brief may ask for.
- **Aliases**: quality issue, quality error
- **Near miss**: A font declared but never loaded: listed in the catalogue as a tell, but it is a defect, because no brief asks for a font that does not load.
- **Kind**: thing
- **Related**: `quality-floor`
- **Facet**: `brief-override`

### judgement (`judgement`)

- **Definition**: Judgement is a detection method that needs the brief or the subject to find an item.
- **Scope**: Includes items that no rule can decide without knowing what the product is or what was asked: a stock section order, a direction borrowed from the category.
- **Aliases**: judge, judgment
- **Near miss**: A tell the brief may allow: whether the brief allows it is the `brief-override` facet; detection only asks how it is found.
- **Kind**: property
- **Facet**: `detection`

### copy (`copy`)

- **Definition**: Copy is an aspect of an interface that covers the words and numbers it shows.
- **Scope**: Includes headlines, labels, button text, error messages, invented proof and number formats.
- **Aliases**: text, wording, microcopy
- **Near miss**: A stat strip of round numbers: the numbers are invented copy, though they sit in a layout block.
- **Kind**: thing
- **Facet**: `aspect`

### any mode (`any-mode`)

- **Definition**: Any mode is a mode scope that covers every mode of screen.
- **Scope**: The value for items the repo applies everywhere. Excludes items it applies only to Persuade or only to Operate screens.
- **Aliases**: all modes, every mode
- **Near miss**: An item the repo relaxes on one mode but still counts there (the eyebrow, one allowed on Operate): still any mode.
- **Kind**: property
- **Facet**: `mode`

### colour (`colour`)

- **Definition**: Colour is an aspect of an interface that covers the hues, lightness and contrast of its fills, text, borders, shadows and glows.
- **Scope**: Includes gradients, including gradient text, coloured glows and halos, palette choice, and contrast between text and its surface. Excludes the shape of a shadow or a radius (use `component`).
- **Aliases**: color, palette, colour and surface
- **Near miss**: Gradient text: it is about colour even though the target is a headline, because removing it means changing the fill, not the type.
- **Kind**: thing
- **Facet**: `aspect`

### Operate (`operate`)

- **Definition**: Operate is a mode in which the person on the screen completes a task.
- **Scope**: Includes app screens, dashboards, tables, settings, editors and admin. Familiar patterns are a feature here; most character is at rest.
- **Aliases**: Operate surface, Operate mode, product UI
- **Near miss**: A dashboard on a landing page as decoration (a fake dashboard hero): that screen is Persuade.
- **Kind**: property
- **Broader**: `mode`
- **Facet**: `mode`

## Items

```csv
id,item,from
r01,KPI figures at 36–48px bold in the brand colour,"tells.md, Generated dashboards"
r02,"Gradient area chart, smoothed spline, a dot on every point; a hue per bar","tells.md, Generated dashboards"
r03,"Zebra table, uppercase tracked headers, checkbox, avatar, chip and kebab on every row","tells.md, Generated dashboards"
r04,Left-aligned proportional digits,"tells.md, Generated dashboards"
r05,"The accent on every button, tab and link","tells.md, Generated dashboards"
r08,Sound with no off switch,"tells.md, Playful slop"
r10,"Perpetual loops (pulse, float, shimmer, typewriter) on components at rest","tells.md, Playful slop"
r11,"Pastel blobs, rounded-everything and ""bold colors"" because the brief said ""fun""","tells.md, Playful slop"
r12,"Streaks, badges and points on a tool nobody asked to gamify","tells.md, Playful slop"
r13,Fake waiting jokes; a delay staged before a flourish,"tells.md, Playful slop"
r14,"Actions are `<button>`, navigation is `<a>`/`<Link>`; no click handlers on `div`/`span`. `lint: div-onclick`",audit.md
r15,Icon-only buttons have an accessible name. `lint: icon-button-label`,audit.md
r16,Sticky headers and overlays never cover the focused element; dialogs trap and return focus; `overscroll-behavior: contain` in sheets and drawers.,audit.md
r17,No `transition: all`; animate transform/opacity/colour only. `lint: transition-all`,audit.md
r18,"Labels on every form control; errors inline, specific, with the fix; first error focused on submit.",audit.md
r19,Buttons name their action; the same verb carries through the flow.,audit.md
r20,No console errors; the page renders (an empty `#root` passes every code check and is still a failure).,audit.md
r21,Loads at the top (`scrollY === 0`); no horizontal overflow at 375px and 1280px (`scrollWidth <= innerWidth`).,audit.md
r22,"Dark mode designed, not inverted: `color-scheme: dark`, tokens only, no manual `dark:` colour overrides. `lint: dark-override`",audit.md
r23,"Browser surfaces themed: text selection, caret, scrollbars, underline offset, focus ring colour.",audit.md
r24,Dark mode nobody asked for; dark ground with muted grey body text,ux-slop-taxonomy.md §3a
r25,Glass and backdrop blur as decoration,ux-slop-taxonomy.md §3a
r27,Monotonous spacing; heading closer to the block above than its own content,ux-slop-taxonomy.md §3c
r28,Fake window chrome (macOS traffic lights) as the hero,ux-slop-taxonomy.md §3d
r29,Modal as the first thought,ux-slop-taxonomy.md §3d
r30,"""X theater"" framing",ux-slop-taxonomy.md §3f
h01,Cyan or neon accents on a dark ground; several neon accents with no dominant one,ux-slop-taxonomy.md §3a
h12,Every button styled as primary,ux-slop-taxonomy.md §3d
h14,Emoji as icons or bullets; Unicode glyphs as an icon system,ux-slop-taxonomy.md §3d
h15,"The worn Lucide set: `Sparkles` for AI, `Zap`, `Rocket`, `Shield`, `ArrowRight`",ux-slop-taxonomy.md §3d
```
