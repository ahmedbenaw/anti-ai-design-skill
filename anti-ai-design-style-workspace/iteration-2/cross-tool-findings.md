# Cross-tool findings, iteration 2

Recorded, not acted on. Adding a rule needs the register's evidence bar: two
independent sources or one measurement, plus a fixture, a register row and a
compendium ID. Each item below has one source so far.

## 1. `side-tab` — a tell we score 0 and another tool calls the most recognizable

The Impeccable design hook flagged "side-tab accent border" on the with_skill
output of both `clinic-landing-page` (3 instances) and
`student-budget-app-screen` (1). Its own detector registry files it under
`category: 'slop'`, the group it describes as "tells that something was
AI-generated", and its description calls it "the most recognizable tell of
AI-generated UIs".

Our scanner has no such rule. `grep` for `side.tab`, `border-left` and
`border-inline-start` across `rules.json` and `tells-register.md` returns
nothing. So a page can score 0 on our AI-look axis while carrying what an
unrelated tool considers the single clearest tell.

This is the more useful half of a cross-tool disagreement. We do not
disagree on a judgment call. We are simply silent where another tool is loud.

- **Source so far:** Impeccable's detector registry (1 source, a tool, not a
  measurement of generated output).
- **What it would take:** count `border-left` accent stripes across the K
  methodology's verified-generated corpus and a human control, the way MB3
  was done. If it replicates, it is a real rule; if the human control also
  hits, it is another straight-down-shadow.
- **Status:** candidate. No rule, no weight, nothing changed.

## 2. `flat-type-hierarchy` — belongs in the rendered layer, not in a regex

Flagged on the with_skill output of `student-budget-app-screen`: dominant
heading and body roles separated by less than 1.25x at every step.

Our nearest rule is TY4, "Hero type sandwich", and it is not the same thing.
TY4 looks at the hero. This is a whole-page property: the ratio between type
roles wherever they appear.

The important part is where it would have to live. `side-tab` could plausibly
be a regex, because a thick one-sided coloured border is visible in the CSS
text. A flat type scale is not. It needs the computed font size of each role
after the cascade, which means a browser. That puts it in `render_check.py`
with the contrast and target-size checks, on the **craft axis**, not in
`rules.json` on the AI-look axis.

That distinction matters more than the rule itself. Two tells can look
alike in a report and still need completely different machinery. Filing this
one as a regex candidate would have wasted the next sweep's time.

- **Source so far:** Impeccable's detector registry. One source.
- **Status:** candidate for the rendered layer. Nothing changed.

## 3. `overused-font` overlaps our typography rules but names different faces

Impeccable names Inter, Roboto, Fraunces, Geist, Plus Jakarta Sans and Space
Grotesk. Worth diffing against our own font lists when the next sweep runs.
Not checked yet.
