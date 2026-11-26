# Explorer site

A browsable site for this repo, **generated** from its files: an overview, then one
explorer per domain, drillable from a facet to its values, from a term to every round item
a rater sorted under it, and from there to each rater's raw answer. Built on
[strata-react](https://github.com/jburnhams/strata-react) (Jonathan's choice, 2026-11-26).

## How it stays automatic

[`generate.py`](./generate.py) reads the repo on every build; nothing in `site/` names a
domain, term or round. It picks up:

| What | From | Rule it relies on |
|---|---|---|
| A domain | every `domains/<name>/` with a `glossary.md` | spec §1 |
| Terms | `### <label> (`<id>`)` records and `- **Field**: value` bullets in `glossary.md` | spec §1 field grammar, §4 |
| Narrower links | derived from **Broader** | spec §4 |
| Facets | records in `facets.md` with **Question** or **Values**; a facet is "in use" when a glossary entry names it in **Facet** | spec §3, T6 |
| Items | tables in `samples.md` whose first cell is a backticked id (`` `b01` ``), and any CSV with `id` and `item` (or `text`, `heading`) columns | process step 2 |
| Rounds | every `rounds/<round>/`: `items.csv`, `answers/<rater>.csv` (columns `id`, one per facet with `_` for `-`, `note`) | process step 8 |
| Kappa | recomputed from the answer CSVs: Cohen for two raters (as `tools/kappa.py`), Fleiss for three or more, plus Cohen for each pair | spec T8 |
| Changes per term | `changelog.md` bullets under `## YYYY-MM-DD` that name the term's id in backticks | spec §6 |
| Docs | every `*.md` in the repo; for sources, only each folder's `README.md` | |

Anything it cannot read (a missing referenced id, an answer column that is not a facet)
is printed by `python3 site/generate.py --check` and listed at the foot of the overview.
The domain order is: `taxonomies` (the method's own words) first, then by size.

## What is published

The site is public even though the repo is private (GitHub Pages has no private sites on
personal plans). It publishes the docs, domain files and CSVs, and each source's
`README.md` (citation and notes). It does **not** publish stored source copies (PDFs,
saved pages, OCR text); their links go to the repo on GitHub, which only people with
access can open.

## Run it

Needs Node 26 (strata-react's engine; Node 22 works with a warning) and Python 3.

```bash
cd site
npm ci
npm run dev        # generate data, then serve at http://localhost:5173
npm run check      # parse every domain, typecheck
npm run build      # generate data and build into site/dist
```

Routes are after the hash (`#/d/ux/term/code`), so the site works from any path on Pages
with no server rewrites. Deployed by [`.github/workflows/pages.yml`](../.github/workflows/pages.yml)
on every push to `main`.

## Dependencies

strata-react and its required peers (`react`, `react-dom`, `react-router`,
`@tanstack/react-query`, `tailwindcss`), with Vite, `@tailwindcss/vite` and TypeScript to
build. Markdown is rendered by a small renderer in [`src/markdown.ts`](./src/markdown.ts)
rather than a library, so links resolve to the site's own pages and nothing else is added.
