# Benchmark — anti-ai-design-style, iteration 2

Register 2026.10 · rules `6b7abae241e662e5` · 3 evals x 2 configurations · graded 2026-09-11. Regraded the same day after the CSS twins landed.

**n = 1 per cell.** Each number below is one run. No repeat runs were done, so
no variance claim is made. Treat every delta as directional.

## Pass rate

| Configuration | Assertions passed | Pass rate |
|---|---|---|
| with_skill | 24 / 24 | **100%** |
| without_skill (baseline) | 16 / 24 | 67% |

Iteration 1 used 18 assertions and with_skill scored 18/18. That was a
ceiling: the set could not tell a good run from a better one. This iteration
adds two assertions per eval, `a7` brand distance and `a8` library misuse,
taking the set to 24. `a7` is the one that moved.

## Per eval

| Eval | with_skill | baseline | AI-look (with / base) | Craft flags (with / base) | Brand (with / base) |
|---|---|---|---|---|---|
| clinic-landing-page | 8/8 | 6/8 | 0 / 2 | none / CR5, CR6 | COMPLIANT / **NON-COMPLIANT (8)** |
| student-budget-app-screen | 8/8 | 6/8 | 0 / 4 | none / CR2, CR5 | COMPLIANT / **NON-COMPLIANT (7)** |
| deslop-lovable-page | 8/8 | 4/8 | 0 / 20 | none / CR2, CR6 | COMPLIANT / **NON-COMPLIANT (4)** |

The deslop input scored 52 with craft flags CR1, CR2, CR5 and brand
NON-COMPLIANT before either run touched it.

**Regraded once.** After the audit, ten rules gained a plain-CSS form
(`research/17-tailwind-vs-css.md`). Three baseline pages moved. Clinic went 0 to 2, budget 0 to 4, deslop 18 to
20. The deslop baseline now fails `a1`. No
with_skill page moved. The grader and benchmark were re-run, not edited.

## The finding: the two guards are close to orthogonal

Every baseline passed the AI-look guard. Every baseline failed the brand
guard. Three for three.

This is the same shape as the result that motivated the skill, where four of
four pages passed one guard and failed the other. It now has a mechanism.
Here is the evidence from the student-budget baseline, tool-printed:

```
FAIL #EFE4CE  fails as neutral (C1 5.37 Delta-E from brand value #E8E6DC, needs >= 12)
FAIL #F1E7D2  fails as neutral (C1 4.91 Delta-E from brand value #E8E6DC, needs >= 12)
FAIL #EADFC6  fails as neutral (C1 6.29 Delta-E from brand value #E8E6DC, needs >= 12)
```

Every one of those is a warm cream. Asked to avoid looking generic, the
baseline reached for the warm-paper editorial palette. That palette is the
current convergence wave, which this register already tracks as the
cream-editorial escape era. It also sits inside Delta-E 12 of the brand
neutrals. So the popular escape route from the AI look walks into the
brand-distance violation zone.

The two guards are not redundant. A page can satisfy one by means of failing
the other. Only the with_skill runs cleared both, and they did it by
generating the palette with `generate_palette.py` rather than choosing colours
by eye.

## Every baseline failure, with evidence

| Eval | Assertion | Why it failed |
|---|---|---|
| clinic-landing-page | a4 copy_check | grade 4.9 with findings outstanding |
| clinic-landing-page | a7 brand | 8 violations, all colours inside Delta-E 12 of brand neutrals |
| student-budget-app-screen | a2 craft | CR2 present: no `prefers-reduced-motion` handling |
| student-budget-app-screen | a7 brand | 7 violations, same warm-cream cause |
| deslop-lovable-page | a1 AI-look under 20 | 20 after the CSS twins (was 18): TY5 now sees its plain-CSS eyebrows |
| deslop-lovable-page | a2 placeholder people | `John Doe` and `Jane Smith` still in `fixed.html` |
| deslop-lovable-page | a3 fake stats | `Trusted by 10,000+` and `99.9%` still in `fixed.html` |
| deslop-lovable-page | a7 brand | 4 violations |

The deslop baseline is worth reading rather than scoring. It **reported** the
placeholders and fake stats honestly in its reply, then left them in the file.
That is a real distinction: it was transparent about the problem and did not
fix it. The assertion is about the artifact, so it fails. The with_skill run
removed all four patterns.

## Cost

| Configuration | Mean tokens | Mean duration |
|---|---|---|
| with_skill | 156,843 | 607s |
| without_skill | 127,463 | 342s |

The skill costs about 23% more tokens and 77% more time. That buys the brief
step, the generated palette, the scanner runs and the fix rounds. Iteration 1
measured 45% more tokens, so the token gap narrowed while the time gap grew.
With n = 1 per cell, do not over-read either number.

## What the assertions still cannot see

`a8` library misuse was 0 in all six runs, with_skill and baseline alike. It
never discriminated. None of these three tasks pulls in an animation or map
library, so the rule had nothing to score. It is not a bad assertion, it is
an assertion aimed at a case these evals do not contain. A fourth eval that
asks for scroll animation or a map would give it something to do.

The `side-tab` gap in `cross-tool-findings.md` is the other blind spot. An
unrelated detector flagged accent stripes on two with_skill outputs, and this
register has no rule for it, so both scored 0 on that axis.
