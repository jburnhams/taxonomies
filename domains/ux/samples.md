# UX taxonomy: samples

**In one line**: the items the taxonomy is built from and tested on, fixed before any
classification so the test items stay fresh (process step 2).

**In plain words**: an *item* is one entry the repo already writes down: a row of the tell
catalogue, a row of the dated registry, or one line of the quality audit. We sort the
build items to find the questions, then sort items we have not looked at to see whether
the questions still work.

Taken from `jburnhams/ux-research` at commit `c742019` (2026-11-25). Chosen for variety, not
at random (Denton §2.3 step 1): the build sample takes the first rows of each section of
the catalogue (§3a 8, §3b 6, §3c 7, §3d 8, §3e 4, §3f 5) and the 1st and 3rd of every five audit
lines (10 of 24), so both slop and quality entries are in it. The other sets are taken from sources the build
sample does not use, plus the catalogue rows it left out. An item that bundles several
checks is kept whole, as written in the repo (see the bare-facet test in
[`facets.md`](./facets.md) for why that matters).

Sizes follow J7: build 30-60, test 30 fresh per round.

## Build sample (48)

Used in steps 3-4.

| ID | Item | From |
|---|---|---|
| `b01` | Purple/indigo/violet gradient (135°, hero, CTA, glow) | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b02` | Indigo/violet primary button | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b03` | Gradient text (`bg-clip-text text-transparent`) | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b04` | Coloured glow shadows (`shadow-indigo-500/50`, zero-offset halos) | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b05` | Radial halo or spotlight behind the hero | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b06` | Cream or beige ground by reflex; cream plus terracotta | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b07` | Near-black (#0B0B0B, #111) standing in for black; one acid accent | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b08` | `zinc-950` card with `border-white/10` (the default dark SaaS card) | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b09` | Inter, Roboto or system stack for everything, no second face | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b10` | The "tasteful free font" cluster as the only design gesture (Space Grotesk, Geist, Syne, Sora, Instrument Serif, Fraunces, Bricolage Grotesque, Young Serif, Cal Sans; 15.8% in the first version of the Show HN study, 10.4% in the current detector, which counts a face only when it is the page default) | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b11` | Oversized italic serif hero headline | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b12` | One accented word in the headline (italic, colour, gradient, highlighter) | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b13` | Tracked ALL-CAPS eyebrow or kicker above headings | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b14` | Full-sentence headline at display size, three or more lines | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b15` | Centred hero: pill badge, H1, grey subhead, two buttons, screenshot below | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b16` | Three (or six) identical icon-topped feature cards | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b17` | The stock section waterfall: hero, logos, features, how-it-works, testimonials, stats, pricing, FAQ, CTA, footer | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b18` | Hero-metric template / stat strip of round numbers ("10,000+ teams", "99.9%") | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b19` | Three-tier pricing with a ringed "Most Popular" middle | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b20` | Four-column footer with newsletter box and social row | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b21` | Everything centred (over 72% centred text) | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b22` | Untouched shadcn defaults (base colour, `--radius`, Card, Button) | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b23` | `rounded-2xl shadow-lg` on everything; one radius regardless of hierarchy | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b24` | Hairline border *plus* a wide soft shadow on a whole row of cards (the "ghost card") | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b25` | Coloured left or top stripe on a rounded card; a *different* colour per card ("multicoloured side tabs") | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b26` | Icon in a tinted rounded-square chip, one per feature or KPI | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b27` | Cards inside cards | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b28` | Status-chip soup; decorative pulsing "live" dot; status dots on every element; "New"/"Live" badges on things that are neither | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b29` | Decorative sparklines with no data behind them | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b30` | Identical fade-and-rise on every section | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b31` | Bounce or elastic easing (`animate-bounce`, `easeOutBack`) | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b32` | Hover lift on every card; scattered micro-interactions | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b33` | Count-up numbers on scroll | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b34` | Benefit-speak: elevate, unlock, supercharge, seamless, empower, streamline, leverage, all-in-one, cutting-edge, world-class | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b35` | "Not just X, it's Y"; "X. No Y." aphoristic cadence across sections | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b36` | Tricolon slogans ("Faster, smarter, simpler") | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b37` | `→` stapled to button and link text | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b38` | Generic CTA ("Get started", "Learn more", "Submit") | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `b39` | Body and placeholder text ≥ 4.5:1 against its *actual* surface (incl. on muted fills and in dark mode); large text ≥ 3:1. `palette.mjs` checks the token pairs; check the overrides in the render. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b40` | Status never by colour alone: icon, word or position as well. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b41` | Line length ≤ ~75ch for prose; line-height ≥ 1.4 for body. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b42` | Visible focus on everything focusable (`focus-visible:` ring or outline; never `outline-none` alone). `lint: outline-none` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b43` | Hit targets ≥ 24px (44px on touch); checkbox/radio label and control share one target. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b44` | Motion respects `prefers-reduced-motion`; nothing auto-moves for > 5s without pause. `lint: reduced-motion` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b45` | Paste never blocked; `autocomplete`/`type`/`inputmode` correct. `lint: paste-blocked` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b46` | Dates and numbers via `Intl.*`; units with non-breaking spaces. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b47` | Long, empty and hostile content handled: `min-w-0` on flex children, `truncate`/`line-clamp`, empty and error states. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `b48` | Fonts actually load (check the computed font in the render, not the CSS). | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |

## Bare-facet test (10)

Used once, in step 5, before any glossary entry.

| ID | Item | From |
|---|---|---|
| `t01` | Input borders, focus rings and meaningful icons ≥ 3:1 (WCAG 1.4.11). | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `t02` | Images have `alt` (`alt=""` if decorative) and explicit `width`/`height`. `lint: img-alt, img-dimensions` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `t03` | Text resizes to 200% and reflows at 320px CSS width without loss; no `user-scalable=no`. `lint: zoom-disabled` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `t04` | Every interactive element reachable and usable by keyboard, in a sensible order. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `t05` | Dark navy or tinted sidebar with a coloured active pill and a left bar | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `t06` | Four KPI cards, each with an icon in a tinted circle | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `t07` | A green "+12.5%" pill and a sparkline on every KPI | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `t08` | Confetti, fireworks or a full-screen celebration on a routine action | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `t09` | Stock whimsy copy: "Oops!", "Whoops", "Uh-oh", "Yay!", "Woohoo", "You're all set!", "Houston, we have a problem", "Looks like you're lost", "It's quiet in here", "Hang tight", "working our magic" | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `t10` | "Something went wrong" (vague, not playful, but it travels with the above) | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |

## Round-1 test (30)

For step 7 and the first agreement test (step 8). Not read while building.

| ID | Item | From |
|---|---|---|
| `r01` | KPI figures at 36–48px bold in the brand colour | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r02` | Gradient area chart, smoothed spline, a dot on every point; a hue per bar | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r03` | Zebra table, uppercase tracked headers, checkbox, avatar, chip and kebab on every row | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r04` | Left-aligned proportional digits | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r05` | The accent on every button, tab and link | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r06` | An illustration and "No data yet" in an empty chart | [tells.md, Generated dashboards](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r07` | Stock illustration kits: unDraw, Humaaans, Open Peeps, Storyset, Blush, generic Lottie files | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r08` | Sound with no off switch | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r09` | A mascot that talks on every screen | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r10` | Perpetual loops (pulse, float, shimmer, typewriter) on components at rest | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r11` | Pastel blobs, rounded-everything and "bold colors" because the brief said "fun" | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r12` | Streaks, badges and points on a tool nobody asked to gamify | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r13` | Fake waiting jokes; a delay staged before a flourish | [tells.md, Playful slop](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/tells.md) |
| `r14` | Actions are `<button>`, navigation is `<a>`/`<Link>`; no click handlers on `div`/`span`. `lint: div-onclick` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r15` | Icon-only buttons have an accessible name. `lint: icon-button-label` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r16` | Sticky headers and overlays never cover the focused element; dialogs trap and return focus; `overscroll-behavior: contain` in sheets and drawers. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r17` | No `transition: all`; animate transform/opacity/colour only. `lint: transition-all` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r18` | Labels on every form control; errors inline, specific, with the fix; first error focused on submit. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r19` | Buttons name their action; the same verb carries through the flow. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r20` | No console errors; the page renders (an empty `#root` passes every code check and is still a failure). | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r21` | Loads at the top (`scrollY === 0`); no horizontal overflow at 375px and 1280px (`scrollWidth <= innerWidth`). | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r22` | Dark mode designed, not inverted: `color-scheme: dark`, tokens only, no manual `dark:` colour overrides. `lint: dark-override` | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r23` | Browser surfaces themed: text selection, caret, scrollbars, underline offset, focus ring colour. | [audit.md](https://github.com/jburnhams/ux-research/blob/c742019/ux-design/skill/references/audit.md) |
| `r24` | Dark mode nobody asked for; dark ground with muted grey body text | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r25` | Glass and backdrop blur as decoration | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r26` | Font declared in CSS but never loaded | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r27` | Monotonous spacing; heading closer to the block above than its own content | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r28` | Fake window chrome (macOS traffic lights) as the hero | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r29` | Modal as the first thought | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `r30` | "X theater" framing | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |

## Held for round 2 (21)

Catalogue rows not used yet; round 2 adds 9 more from `ux-product-ui.md` and `ux-character.md`.

| ID | Item | From |
|---|---|---|
| `h01` | Cyan or neon accents on a dark ground; several neon accents with no dominant one | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h02` | Timid, evenly distributed palette; primary and accent within 20° of hue | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h03` | Grey text on a coloured surface; muted text below AA | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h04` | Grid-line or stripe backgrounds with no canvas under them | [ux-slop-taxonomy.md §3a](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h05` | Flat scale (steps under 1.25×), nine near-equal sizes | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h06` | Monospace as a costume for "technical" | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h07` | Crushed tracking (below -0.04em) | [ux-slop-taxonomy.md §3b](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h08` | Numbered 01 / 02 / 03 markers on non-sequences | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h09` | Bento grid as the default composition | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h10` | FAQ accordion of 3+ generic questions near the bottom, often restating the page | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h11` | Everything visible at once: no progressive disclosure on app screens | [ux-slop-taxonomy.md §3c](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h12` | Every button styled as primary | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h13` | Stock effect components (Spotlight, Beams, Meteors, Number Ticker, Marquee) | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h14` | Emoji as icons or bullets; Unicode glyphs as an icon system | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h15` | The worn Lucide set: `Sparkles` for AI, `Zap`, `Rocket`, `Shield`, `ArrowRight` | [ux-slop-taxonomy.md §3d](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h16` | Content left at `opacity: 0` waiting for an observer that never fires | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h17` | Motion that ignores `prefers-reduced-motion` | [ux-slop-taxonomy.md §3e](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h18` | Em-dash saturation (8 or more at about 1 per 500 characters) | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h19` | Performative labels ("Field notes", "Quietly trusted by", "On our desks") | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h20` | Placeholder identities: Acme, John Doe, lorem ipsum, pravatar, DiceBear | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
| `h21` | "Welcome back, Alex 👋" dashboard greeting | [ux-slop-taxonomy.md §3f](https://github.com/jburnhams/ux-research/blob/c742019/ux-slop-taxonomy.md#3-the-catalogue-by-layer) |
