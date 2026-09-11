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

## 2. `overused-font` overlaps our typography rules but names different faces

Impeccable names Inter, Roboto, Fraunces, Geist, Plus Jakarta Sans and Space
Grotesk. Worth diffing against our own font lists when the next sweep runs.
Not checked yet.
