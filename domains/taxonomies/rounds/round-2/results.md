# Round 2: results

**In one line**: all three raters answered all 43 items; part (Fleiss' κ 0.94) and stage (0.84) pass, but check misses (0.55), and the non-Claude pair misses on check too (0.45). Gemini leaned to `judgement` where the other two said `script`.

- **Files tested**: `facets.md` and `glossary.md` at commit `7004a36` (2026-11-26), the kit commit too.
- **Rater claude**: Claude Opus 5.5 (`claude-opus-5-5`), Claude Code `claude -p`, effort high, no tools. [`answers/claude.csv`](./answers/claude.csv), [raw](./answers/claude-raw.md). 11 notes marked `unsure`.
- **Rater openai**: GPT-6.2-Astra (`gpt-6.2-astra`), `codex exec`, read-only sandbox, reasoning effort high, web search off; no tool calls. [`answers/openai.csv`](./answers/openai.csv), [raw](./answers/openai-raw.md). 1 note marked `unsure`.
- **Rater gemini**: Gemini 4 Carbon High (`gemini-4-carbon-high`), Antigravity `agy -p`, sandboxed. [`answers/gemini.csv`](./answers/gemini.csv), [raw](./answers/gemini-raw.md). No notes marked `unsure`.
- All three ran on omarchy on 2026-11-26 from fresh empty directories holding only their own prompt file, on Jonathan's plans (no API keys, no proxy), same models and flags as round 1. Every answer has 43 rows with the ids in `items.csv`, and only listed values.
- The name test ran in three other fresh sessions (one per CLI, own empty directories), never in a rating session: [`name-test/`](./name-test/).

Target (J5, J23): Fleiss' κ ≥ 0.6 on each facet, and the non-Claude pair κ ≥ 0.6.

| Facet | Fleiss' κ (3 raters) | openai-gemini κ | Pass? |
|---|---|---|---|
| part | 0.94 | 0.97 | yes |
| stage | 0.84 | 0.90 | yes |
| check | 0.55 | 0.45 | **no** |

## All three raters

`python3 tools/kappa.py domains/taxonomies/rounds/round-2/answers/{claude,openai,gemini}.csv`

```
raters: claude, openai, gemini; items compared: 43

| Facet | Unanimous | Fleiss' kappa | claude-openai | claude-gemini | openai-gemini |
|---|---|---|---|---|---|
| part | 93% | 0.94 | 0.91 | 0.94 | 0.97 |
| stage | 84% | 0.84 | 0.76 | 0.86 | 0.90 |
| check | 70% | 0.55 | 0.76 | 0.45 | 0.45 |

Not unanimous (claude / openai / gemini); majority value, or SPLIT when none (M5):
- `h09` part: naming / change / naming -> naming
- `h11` part: change / purpose / purpose -> purpose
- `s13` part: meaning / structure / structure -> structure
- `h08` stage: testing / building / building -> building
- `h09` stage: building / testing / testing -> testing
- `h11` stage: governing / framing / framing -> framing
- `h17` stage: governing / building / governing -> governing
- `h18` stage: building / testing / testing -> testing
- `s12` stage: testing / building / testing -> testing
- `s22` stage: testing / building / testing -> testing
- `h10` check: judgement / script / script -> script
- `h17` check: script / script / judgement -> script
- `s07` check: judgement / owner-decision / judgement -> judgement
- `s09` check: script / script / judgement -> script
- `s13` check: script / script / judgement -> script
- `s15` check: script / script / judgement -> script
- `s17` check: judgement / script / judgement -> judgement
- `s18` check: script / script / judgement -> script
- `s19` check: judgement / script / judgement -> judgement
- `s21` check: script / script / judgement -> script
- `s23` check: script / script / judgement -> script
- `s24` check: script / judgement / judgement -> judgement
- `s25` check: script / script / judgement -> script
```

## The non-Claude pair

`python3 tools/kappa.py domains/taxonomies/rounds/round-2/answers/{openai,gemini}.csv`

```
raters: openai, gemini; items compared: 43

| Facet | Agreement | Cohen's kappa |
|---|---|---|
| part | 98% | 0.97 |
| stage | 93% | 0.90 |
| check | 74% | 0.45 |

Disagreements (openai / gemini):
- `h09` part: change / naming
- `h17` stage: building / governing
- `s12` stage: building / testing
- `s22` stage: building / testing
- `h17` check: script / judgement
- `s07` check: owner-decision / judgement
- `s09` check: script / judgement
- `s13` check: script / judgement
- `s15` check: script / judgement
- `s17` check: script / judgement
- `s18` check: script / judgement
- `s19` check: script / judgement
- `s21` check: script / judgement
- `s23` check: script / judgement
- `s25` check: script / judgement
```

## Reading the numbers

`part` and `stage` pass with the items' own ids removed, so round 1's unanimity was not
only the id lookup. `check` fails, and the failure has one main cause: eight of the
eleven splits are Gemini saying `judgement` where Claude and GPT said `script`, on items
whose conditions a program *could* test but no script in the repo does (a file present,
a seed stated, a majority label). The round-1 fix ("every condition must be one a program
can test") was read as "could", and Gemini read the question as "does". The other
splits: `h10` (Kind field: a value list a script checks, a choice that needs reading),
`s24` (changelog.md), `s17` and `s19` (the CLI rater rules), and `s07` (light version
steps 0 and 1, which GPT took as Jonathan's).

## Fixes after scoring (2026-11-26)

| Items | Split | Fix |
|---|---|---|
| `s09` `s13` `s15` `s18` `s21` `s23` `s25` `h17` `s24` `s17` `s19` | script / judgement | `script` redefined as a closed list: what `tools/check_domain.py`, `tools/kappa.py` and a domain's `sample.py` check today, each listed. Anything else is `judgement`, even where a program could check it. This is also the question an agent asks: "will a script catch me?" |
| `h10` | judgement / script | covered: T1 and T5 check the Kind value, so `script` |
| `s07` | owner-decision | none: the light step names no decider; the majority stands |

Every fresh item is now used. `check` is retested on the 73 round items as an
indicative round 3 ([`../round-3/`](../round-3/README.md)); `part` and `stage` stand.

## Name test (T9)

[`name-test/`](./name-test/): three fresh sessions (Claude, GPT, Gemini) guessed each of
the 14 value labels with no definitions. 13 of 14 were guessed right by all three.
`boundary` was guessed wrong by all three, as the domain's own scope ("which items are
in or out"), which is `purpose`. Renamed to **neighbours** (ID unchanged, N6), after the
`scope.md` field it covers.
