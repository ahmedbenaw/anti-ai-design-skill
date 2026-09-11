# Cross-tool findings, iteration 2

**Corrected 2026-09-11.** The first version of this file was written from
design-hook messages and claimed the iteration-2 outputs carried tells our
scanner misses. That claim was not checked and does not hold. What follows is
the checked version.

## The correction first

The hook reported `side-tab`, `flat-type-hierarchy`, `overused-font` and
`nested-cards` on eval outputs while the runs were in progress. I wrote those
up as findings about the delivered pages. They are not.

Running the other tool's own detector over all six final artifacts returns
**zero findings on every one**. A mid-run snapshot recovered from git is clean
too. The hook fires on each write, so it was reporting on drafts that the
agents then fixed. On every artifact I can actually inspect, the two tools
agree.

The detector was confirmed working before trusting that result. A page built
to trip it reports 2 anti-patterns and exits 2; the six artifacts report none
and exit 0. An earlier run of mine returned nothing on that same positive
control. The fragment had no `<!doctype>`. So the first "all clean" reading
was itself unsafe until the control passed.

## The gap is real, but this is what shows it

A constructed page, not an eval output:

```html
<!doctype html><html><head><style>
body{font-family:Inter,sans-serif}
.card{border-left:5px solid #c2410c;border-radius:8px;padding:20px;width:360px}
</style></head><body><div class="card">...</div></body></html>
```

| Tool | Result |
|---|---|
| Impeccable | 2 anti-patterns: `side-tab`, `overused-font` |
| `ai_tell_scan.py` | **AI-look 0/100, PASS, no tells, no craft flags** |

That is a reproducible disagreement on a page either tool can read. It is
worth more than the four hook messages, because it can be re-run.

## 1. `side-tab` — a real gap, and harder to close than it looks

No rule covers it. `grep` for `side.tab`, `border-left` and
`border-inline-start` across `rules.json` and `tells-register.md` finds
nothing.

The definition is not "a page contains `border-left`". Reading the detector's source, it fires on four conditions at once. The
left or right border is at least 2px. Its colour is not neutral. It is at
least twice the other three sides, or they are 1px or less. And the tag is
not one of roughly thirty safe tags, `blockquote` among them. With a border radius it fires at 2px; without one it
needs 3px.

A regex over CSS text would get partial recall. It could not apply any of the
other conditions, because each needs the other sides, the radius and the
colour resolved together. So this is not a cheap `rules.json` addition.

- **Sources:** the other tool's registry, plus the reproducible case above.
  Still one measurement short of the register's bar.
- **What would settle it:** count it across the K corpus of verified-generated
  repos and a human-built control, the way MB3 was done. The control is the
  hard part. The FlutterFlow control is Dart, and this is web CSS, so a
  pre-2022 human web corpus would have to be assembled first.
- **Status:** candidate. No rule, no weight, nothing changed.

## 2. `overused-font` — not a gap, a calibration difference

Our TY2 is a **pairing** rule. It needs Space Grotesk, Instrument Serif or
Bricolage, and only then counts Inter as the second half. Bare Inter scores 0
here by design.

The other tool flags Inter on its own. Both positions are defensible. Inter is genuinely everywhere, including on work no model
touched. A single-face rule buys recall with false positives. Recording it as a deliberate difference
to revisit at the next sweep, not as a hole.

## 3. `flat-type-hierarchy` — belongs in the rendered layer

Our nearest rule is TY4, "Hero type sandwich", and it is not the same thing.
TY4 looks at the hero. This is the ratio between type roles across the page.

It needs the computed font size of each role after the cascade, which means a
browser. That puts it in `render_check.py` with the contrast and target-size
checks, on the **craft axis**, not in `rules.json` on the AI-look axis.

- **Status:** candidate for the rendered layer. Nothing changed.

## What I should have done

I wrote in this session that I would let the measurement script record
these properly, rather than treat a hook message as a result. Then I wrote
them up from hook messages anyway. The detector was one command away the whole time.

A tool's warning is a lead, not a finding. It becomes a finding once you
run the tool yourself. Run it on the artifact you are claiming something
about. And prove the tool was switched on with a positive control.
