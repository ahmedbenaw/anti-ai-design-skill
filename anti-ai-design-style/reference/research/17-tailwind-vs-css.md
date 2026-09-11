# 17 — Ten rules only knew the Tailwind spelling

**Route:** end-to-end audit of the shipped skill, 2026-09-11. No web
research; every number here came from running the scanner.
**Short answer:** 10 of 30 code rules scored 0 on the plain-CSS form of the
tell they exist to catch. All ten now carry a CSS twin, test first.

## How it was found

The baseline clinic page from evaluation iteration 2 has three uppercase,
letter-spaced eyebrow labels, written in plain CSS. It scored 0. The same
labels as Tailwind classes score 2 under TY5. A survey of `rules.json` followed. It sorted every code rule by what its
patterns match: Tailwind class syntax, CSS property syntax, or both.

| Form recognised | Rules |
|---|---|
| Tailwind only | 10: CO3, CO4, TY5, TY4, LA3, LA8, LA9, MO1, MO2, MO3 |
| Both | 2: CO2, MO4 |
| CSS only | 0 |
| Neither (copy, provenance, icons) | 18 |

## Why it happened

The rules were written from the K corpus, which is Lovable, Bolt and v0
output. All three emit Tailwind. Nobody wrote the CSS twin because the
evidence never showed one. A hand-coded page, a Framer or Webflow export, or
a Squarespace theme carries the same tells as CSS properties.

## The fix, in test order

1. `CSS_FORM_FIXTURE`: one page carrying all ten tells in plain CSS.
   Selftest asserts every rule fires. Ran it first: `FAIL` naming all ten.
2. One twin per rule, each holding the rule's own threshold. Same-block
   constraints use `[^}]*`. Two declarations must sit in one CSS rule, the
   way two classes must sit in one class attribute.
3. `CSS_CLEAN_FIXTURE`: a well-made plain-CSS page with every property the
   twins look for in its honest, below-threshold form. One gradient. A
   `blockquote` rule with no radius. A 2px shadow. A subtle hover lift. A
   `.02em` uppercase button. Selftest asserts none of the ten fires.
4. Selftest `PASS`.

One twin was set too loose on the first pass. TY4's tight-tracking check
fired at `-0.01em`; Tailwind's `tracking-tight` is `-0.025em`. The skill's own
clean example page tripped it, at 2 points. The threshold was set to the
Tailwind value. That is matching the definition, not weakening it to pass.

## What changed on real pages

| Page | Before | After | Why |
|---|---|---|---|
| clinic baseline (iteration 2) | 0 | 2 | TY5, the three eyebrows that started this |
| budget baseline | 0 | 4 | TY5 + TY4 |
| deslop baseline | 18 PASS | **20 FAIL** | TY5; the baseline now fails assertion a1 |
| slop-example | 52 | 50 | LA8 down-weighted 3 to 1, see below |
| fixed-example | 0 | 0 | TY4 at the correct threshold |
| every with_skill page | 0 | 0 | unchanged |

The deslop change moves the iteration-2 baseline from 17/24 to 16/24. The
benchmark is regenerated, not edited by hand.

## LA8, a second finding along the way

LA8 "Side-stripe accent borders" already covered the Tailwind side-tab. An
earlier note in this workspace said no rule did; it grepped for "side-tab"
and missed a rule named "side-stripe". Corrected there.

LA8 was verified from practitioner claims at 3 points. `16-side-tab-tailwind`
measured it at 2 of 12 verified-generated repos. The register's own rule is
to down-weight what a sweep contradicts and never delete. LA8 is now 1 point,
era `2024-25`, status contested. It also gains the shadcn spelling
`border-l-4 border-l-primary`, which the corpus uses and the old pattern
missed. And it gains the CSS form, with a radius required in the same block.

## Gaps

- `[^}]*` same-block matching assumes one declaration block per rule. CSS
  written with nested rules or CSS-in-JS objects can slip past.
- The CSS gradient twin cannot tell a saturated two-hue wash from a subtle
  tonal one. CO3's `min_distinct: 5` is what keeps it honest, not the regex.
- LA3's CSS twin keys on 40 or 48px square tiles with a radius and a hex
  background. A rounded-square avatar with a solid colour would match.
- The remaining eighteen rules are copy and provenance tells with no
  spelling split. They were not audited for other splits, such as
  inline-style attributes.
