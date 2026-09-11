# 16 — Does the side-tab accent border replicate in generated code?

**Route:** GitHub API plus shallow clone, then a text measure written here.
Exa was not used; it is not needed to count classes in cloned repos.
**Date:** 2026-09-11.
**Short answer: no. 2 of 12 verified-generated repos. No rule was added.**

## Why this was asked

Another design tool flags "side-tab accent border" and its registry calls it
"the most recognizable tell of AI-generated UIs". This register has no such
rule, so a page can carry one and still score 0 here. That is worth checking
rather than assuming either way.

## The measure, written before the corpus was touched

Tailwind's atomic classes encode what plain CSS hides. `border-l-4` is
exactly `border-left-width: 4px`, and the absence of a `border-t/r/b` sibling
means the other sides are 0. That satisfies the "at least twice the other
sides" condition structurally, which is why this can be a text measure at all.
The plain-CSS form cannot be measured this way. It is **not** covered here.

An element qualifies when the geometry holds. That means a left or right
border of 2, 4 or 8, at least twice the other sides. A width of 2 counts only
when a `rounded-*` class is present. Two tiers are then reported:

- **strict**: a resolvable non-neutral colour on the element
- **loose**: geometry only

Two tiers are necessary, not decorative. Generated shadcn code names colours
as semantic tokens, like `border-l-primary`. It also passes them through
variables, like `` className={`border-l-4 ${stat.borderColor}`} ``. Neither
resolves from text. A strict-only measure would under-report on exactly the corpus that
matters. A loose-only measure cannot tell a coloured accent from a grey one.

Known-answer checks before use: a constructed positive page scores 3 and a
constructed negative page scores 0 strict, with the grey accent correctly
appearing in loose and not in strict. Recall against a raw `grep` over the
corpus is 11 of 12 instances.

## Corpus

12 repos with verified provenance, reused from the K sweep: K16–K23 Bolt.new
(`.bolt/config.json`), K39–K42 Lovable (`lovable-tagger` in `vite.config.ts`).
Nine carry Tailwind; three do not and are kept in the denominator with zeros,
since a project that cannot express the pattern is still a project that did
not produce it.

## Result

| Measure | Count |
|---|---|
| Repos with at least one strict side-tab | **1 of 12** |
| Repos with at least one loose side-tab | **2 of 12** |
| Total instances across the whole corpus | **12** |
| Instances in the single heaviest repo | **9 of 12** (`artesanal-fio-alma`) |

Nine of the twelve instances are `<Card className="border-l-4 border-l-*">`
in one admin dashboard, in one project. Two more are in a second project. The
other ten repos have none.

That is concentration, not prevalence. One project's house style does not
make a tell.

## The part that changed my mind about the source

The page that started this is `deslop-lovable-page/inputs/input.html`, which
carries three side-tabs and is described in the eval prompt as Lovable output.
It has **zero** Lovable provenance markers. It is a hand-authored fixture
standing in for generated output.

So the three side-tabs in it record what someone believed AI output looks
like. The twelve verified-generated repos record what it actually looks like,
and they disagree. This is the straight-down-shadow lesson in a new costume:
the stereotype was measured, and the stereotype lost.

## Why no human control group was assembled

The plan was a pre-2022 human Tailwind control. It was not needed. A control
matters when the generated rate is high and the question is whether humans do
it too. At 2 of 12 the generated side already fails the bar that MB3 cleared
at 5 of 12 positives against 0 of 413 in the control. A control could only
lower the number.

## Gaps

- **The plain-CSS form is unmeasured.** `border-left: 4px solid <colour>`
  needs the four side widths, the radius and the colour resolved together.
  That needs a browser. It belongs in `render_check.py` on the craft axis,
  not in `rules.json`. Nothing here says anything about it.
- **Corpus skew.** Bolt output here is Vue and Nuxt; Lovable is React. No
  Cursor, Copilot or v0 projects were included. A different generator mix
  could give a different answer.
- **Recall is 11 of 12**, not perfect. The miss is a geometry edge case, not
  a colour one.
- **n = 12.** Small, and one repo dominates the instance count.

## Decision

No rule. Recorded as counter-evidence in the register, with the numbers, so
that the next person who reads another tool's registry does not spend this day
again.
