# Benchmark — anti-ai-design-style, iteration 1

Register 2026.08 · 3 evals × 2 configurations · graded 2026-09-04

## Pass rate

| Configuration | Assertions passed | Pass rate |
|---|---|---|
| with_skill | 18 / 18 | **100%** |
| without_skill (baseline) | 15 / 18 | 83% |

## Per eval

| Eval | with_skill | baseline | AI-look score (with / baseline) | Craft flags (with / baseline) |
|---|---|---|---|---|
| clinic-landing-page | 6/6 | 5/6 | 0 / 0 | 0 / 4 |
| student-budget-app-screen | 6/6 | 6/6 | 0 / 0 | 0 / 1 |
| deslop-lovable-page | 6/6 | 4/6 | 0 / 18 | 0 / 2 |

## Cost

| Configuration | Mean tokens | Mean duration |
|---|---|---|
| with_skill | 136,581 | 444s |
| without_skill | 94,098 | 312s |

The skill costs roughly 45% more tokens and 40% more time per task. That buys
the brief step, two scanner runs, and up to three fix rounds.

## What the baseline actually failed

1. **clinic (baseline):** four craft flags — animations with no
   `prefers-reduced-motion` path, focus outlines removed, tiny text, uppercase
   runs. The page looked fine; it was just less accessible.
2. **de-slop (baseline):** kept "John Doe", "Sarah Chen" and "Jane Smith" as
   testimonials, and kept "10K+", "99.9%", "Trusted by 10,000" — because the
   user said "don't remove real information" and the baseline treated
   placeholders as real. Final AI-look score 18 versus 0 with the skill.

## Measured after grading: the brand-distance guard (v2)

The three with_skill outputs were re-scanned with
`anti-antropik-design/scripts/audit_file.py` after Ben flagged that the fixed
example looked like Claude's own design system.

| Eval | with_skill brand distance | Violations |
|---|---|---|
| clinic-landing-page | NON-COMPLIANT | `#F3F5F2` |
| student-budget-app-screen | NON-COMPLIANT | `#B9B6AC` `#F1F1EA` `#FBFBF7` |
| deslop-lovable-page | NON-COMPLIANT | `#FBFBF9`, georgia, source serif |

With `examples/fixed-example.html` v1 that is 4 of 4 skill-generated pages
failing a guard the skill did not run. The 18/18 above is therefore an
AI-look and craft result only. v2 makes the brand guard a gate (brief,
commands, stop hook). **These evals have not been re-run against v2**; that is
the first open item in the handover.

## What this does NOT prove

- n = 1 per cell. No variance data; a rerun could move any single number.
- The with_skill runs were graded partly against the skill's own scanner, so
  that axis is not independent. The judgment assertions (product-specific
  elements, preserved information, plain-language summary) are the independent
  part, and two of the three baseline failures were judgment failures.
- Both configurations produced good-looking pages. The measured difference is
  in accessibility craft and in honesty about placeholder content, not in
  whether the page "looks nice".
