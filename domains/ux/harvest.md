# UX taxonomy: term harvest (round 1)

**In one line**: the words ux-research already uses for its concepts, with counts, grouped
into synonym sets and flagged homonyms, before any label is chosen (process step 3, spec N2).

**In plain words**: before picking one word per idea, we count how often each word is
used and notice where two words mean the same thing (synonyms) or one word means two
things (homonyms). The counts are the evidence ("warrant") for the label we choose.

**How counted**: case-insensitive whole-word matches with `grep -oiw` (or `grep -oiE` for
phrases) over the repo's **own** docs, not the stored sources: `README.md`, the ten
`ux-*.md` synthesis docs, and every `.md` under `ux-design/` and `ui-library/` except
fixtures (28 files), at `jburnhams/ux-research` commit `c742019`, 2026-11-25. Counts in
the stored source folders are left out because those keep their authors' words (scope:
out of scope). Phrase counts overlap their single words.

## Concepts and the words used for them

| Concept | Words and counts | Notes |
|---|---|---|
| a default that appears whatever the subject | "tell"/"tells" 154, "default(s)" 123 (mostly other senses), "fingerprint(s)" 3 | "tell" is the repo's own term (`tells.md`: "A tell is a default that appears regardless of the subject") |
| the generic look as a whole | "slop" 194, "AI slop" 8, "generic" 23, "median" 25, "AI-made" 5 | "slop" is also used as a lint category (`slop` vs `quality`) |
| a fault that makes the interface fail, which the brief cannot waive | "defect(s)" 4, "quality" (lint category), "the floor"/"quality floor" 9 + 9, "craft floor" 4 | "defect" has low warrant but is the word `audit.md` uses ("These are defects, not taste") |
| the minimum every interface must meet | "quality floor" 9, "craft floor" 4 (Impeccable's word), "the floor" 9 | synonym set; "craft floor" is a source's word |
| the kind of screen, which decides the rules | "mode" 73 (also "dark mode" 11), "the mode" 20 | homonym with "dark mode" |
| the four modes | "Persuade" 33, "Operate" 97, "Read" 105 (mostly the verb), "Experience" 11 | "Read surfaces" 7 |
| how much decoration a screen gets | "treatment" 9, "utilitarian" 10, "editorial" 15 | |
| the screen or page being built | "screen(s)" 215, "page(s)" 196, "surface(s)" 90, "view(s)" 61 | "surface" mostly in "Operate/Persuade surface(s)" (31) |
| a fill or layer of colour that content sits on | "surface" (6, e.g. `--surface-card`, "its actual surface"), "ground" 49, "background" 33, "page ground" 6 | homonym with the line above |
| what the brief starts from: what the product is | "subject" 121, "subject inventory" 6, "inventory" 26 | |
| what the person asked for | "brief" 56 | |
| the chosen visual idea | "direction" 42, "mood" 38, "vibe" 9, "aesthetic(s)" 12, "look" 65 (general) | not all synonyms: `direction.md` treats mood and vibe as **inputs** and the direction as the **output** |
| the sentence that fixes a direction | "reference sentence(s)" 12, "reference" 72 (wider) | |
| named design values in CSS variables | "token(s)" 123, "token contract" 14, "theme" 100, "DESIGN.md" 88 | "theme" is the generated set of tokens; "token contract" the agreement not to bypass them |
| a colour's job in the theme | "role(s)" 43 (palette role 17; ARIA role 10) | homonym |
| one memorable device on an Operate screen | "signature move" 12, "the signature" 7 | homonym with a model's or generator's signature (3) |
| the generations of tells | "wave(s)" 31 | |
| the dated list of tells | "registry" 24, "tell registry" | |
| the source linter | "slop-lint" 49, "linter" 13, "lint" 76 | proper name |
| how a tell is found | "src" 98 (mostly code paths), "lint" 76, "render" 64, "judge" 40, "judgement" 5 | the catalogue writes `src` / `render` / `judge`; `tells.md` writes a rule id / `render` / `judge` |
| what a review reports | "finding(s)" 14 (lint findings) | homonym with "the one finding" 11 |
| the one thing an Operate screen must answer | "one question" 12; "one finding" 11 | |
| part of the look / part of the code | "layer(s)" 49 | homonym: the catalogue is "by layer" (colour, type, ...); `ux-react-tailwind.md` §1 has five layers of the stack (brief, tokens, variants, composition, call site) |
| personality added on purpose | "character" 125, "personality" 17, "voice" 37, "playful" 40, "delight" 30, "whimsy" 16 | |
| a rare, earned flourish | "moment" 52 | general word; the repo's sense is "the moment" in `character.md` |
| checks named as tests | "swap test" 12, "competitor test" 8, "silhouette test" 3 | |
| generic playfulness | "stock whimsy" 8, "playful slop" 3 | synonym set |
| pages of one product diverging | "drift" 15 | |

## Homonyms to resolve (spec N1)

1. **surface**: (a) the screen or page being built, classified by mode ("Operate
   surfaces"); (b) a fill that content sits on ("against its actual surface",
   `--surface-card`). Sense (a) has the warrant (31 of the counted phrase uses against 6).
2. **layer**: (a) the part of the interface a tell is about (the catalogue's "by layer");
   (b) the five layers of the stack in `ux-react-tailwind.md`. Neither should be the
   facet's label.
3. **mode**: Persuade/Operate/Read/Experience against dark mode. Low risk, since "dark
   mode" is always the phrase; record "dark mode" as its own entry.
4. **signature**: an Operate screen's one device ("signature move") against a model's or
   generator's identifying habits (§3g "Signatures and drift").
5. **finding**: a linter or review result against "the one finding" of an Operate screen.
6. **role**: a colour's job (palette role) against an ARIA role.
7. **source**: a research source (a folder) against source code (the `src` detection
   value). The detection value should not be labelled "source".

## Words from Jonathan

None yet for this domain. The project chat's brief says only "start ux-research".
