# Taxonomies taxonomy: term harvest

**In one line**: the words the method's own documents use for its concepts, with counts,
the synonym sets and homonyms they form, and the vocabularies reused.

**In plain words**: before choosing names, we count what the spec, process and the
first domain already say. Where several words mean one thing (alias, alternative label)
we pick one and keep the rest as aliases. Where one word means several things ("scope",
"round") we say which sense the glossary uses and give the others another word.

Process step 3 ([`design/process.md`](../../design/process.md#step-3-harvest-the-words)).
Counted 2026-11-26 at commit `d6900f1` over `design/*.md` and every `.md` file under
`domains/ux/` (22 files, about 33,700 words): the method and the one domain that has
been through it. Counts are whole-word, case-folded matches of the word and its plural
(`grep -o -i -w -E`), so they include quotes, field names and code; treat them as order
of magnitude.

## Vocabularies reused (step 0)

- **The spec's own field names** (`design/spec.md` §§2-4): every field of `scope.md`,
  `facets.md` and `glossary.md` already has a name, and most of them are the method's
  concepts (definition, scope note, near miss, warrant). Kept as they are.
- **SKOS** (cited in spec §1 and T1-T2): preferred label, alternative label, hidden
  label, broader, related, closeMatch. The glossary keeps SKOS's concepts and the spec's
  shorter words for them (alias, not "alternative label": below).
- **Z39.19 §11** and **Denton 2003** (stored, cited throughout the spec): candidate,
  warrant, scope note, facet, test classification.
- **OntoClean / OBO** (spec S4): thing, property, role, happening, the term kinds.
- **The spec's own groups** (§8 rules: Structure, Names, Definitions, Contexts; §9
  Governance; §10 Validation tests) and the process's step table ("The steps at a
  glance", with its Who column). These are the seeds of the three facets
  ([`facets.md`](./facets.md)).

## Counts for the concepts

| Concept (draft) | Words used, with counts |
|---|---|
| one area of work with its own vocabulary | domain 76, context 38, bounded context 9 |
| the whole vocabulary | taxonomy 38, glossary (field and file), controlled vocabulary 2 |
| a sorting question | facet 232, dimension, axis (in sources and quotes) |
| one entry | term 116, concept 42, entry, record |
| the name of a term | label 90, name; preferred label |
| other names | alias 115, alternative label 0, hidden label, synonym |
| the fixed key | identifier/ID 66 |
| what the term means | definition 131, scope 167, scope note 28, near miss 99 |
| what is sorted | item 13 as "fresh items", sample 47, held-out 4 |
| counting words in use | harvest 57, warrant 72 |
| a test pass | round 191, agreement test, test classification |
| who sorts in a test | rater 57, judge 15 |
| agreement figure | kappa/κ 38 |
| term status | candidate 40, approved 136, deprecated |
| a change | operation 14, change 41, review 35, veto 64 |
| who decides | owner 13, Jonathan 110 |
| what must hold to finish | ending condition 58, competency question 18 |
| items that fit nowhere | Unsorted 31 |
| a check | check 87, test 113, mechanical 5, judgement 50, script 6 |
| a phase of the method | step 100, stage 1; framing 3, building 10, testing 1, governance 8, governing 0 |
| what a rule is about | structure 22, naming 8, meaning 10, evidence 12, purpose 25, boundary 12 |

## Synonym sets (one preferred, the rest aliases)

1. **alias**, alternative label (SKOS), synonym. *alias*: 115 uses against 0; the
   glossary field is already called Aliases.
2. **rater**, judge, annotator. *rater*: 57 against 15. "judge" stays an alias here; in
   the prompts domain it names a model that grades output, a different concept there.
3. **term**, entry, record, concept. Not one concept: a *concept* is the meaning, a
   *term* its entry with a label (N3, spec §4). Kept apart; "entry" and "record" are
   file words and need no glossary entry.
4. **facet**, dimension, axis, sorting question. *facet* (232).
5. **governing**, governance, maintenance. The stage word; see label choice 3 in the
   glossary.
6. **owner-decision**, Jonathan's decision, the owner decides. A check value; "owner"
   rather than "Jonathan" because a domain may have another owner (spec §2 Owner).

## Homonyms (one word, several senses)

| Word | Senses found | What the glossary does |
|---|---|---|
| scope | the file `scope.md`; the glossary field Scope (the scope note); the extent of a domain | `scope note` is the field's concept; the file is named by its path; extent stays plain English |
| round | a test round (rounds/round-1/); "round 1 harvest" in ux; "build round" in T11 | `round` is a test round; the others are written out ("build pass", "harvest") |
| kind | the glossary field Kind (S4); plain "sort of" | `kind` is the field only; the old facet `kind` is retired (see facets.md) |
| context | bounded context; the context of a pattern (§7); plain "surroundings" | `bounded-context` is the term, with alias "context" kept only for the full sense |
| test | the tests T1-T14; the test sample; a round | each has its own term (`agreement-test`, `name-test`, `test-sample`, `round`) |
| status | a term's status (candidate ...); a domain's status (draft, in use) | `status` is a term's; a domain's status is its near miss |
| domain | a folder under `domains/`; Jonathan's area of work; the domain repo | `domain` is the area of work; the folder is its home |
| review | the monthly review (step 12); a heuristic review (T11); a PR review | `review` not given an entry: the step and test names say which |
| check | the third facet; a mechanical check; any test | `mechanical-check` is T1-T6; the facet is `check`, with question "What settles whether it is met?" |

## Gaps

- No word in use for "what part of a taxonomy a rule governs". The spec's section names
  (Structure, Names, Definitions, Contexts, Governance) are the warrant for the `part`
  values; "naming" and "meaning" are the gerund and noun forms that read as parts.
- "stage" has one use; the process says "step". Kept because a stage groups several
  steps, and the step table already groups them that way. Checked by the name test (T9).
