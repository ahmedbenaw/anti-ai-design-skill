# Iteration 3 benchmark: one eval, one pair, n = 1

Register 2026.10, rules fingerprint `ee9ee6320a9a639b` (before the interrogate
fixes; see `../interrogate/VERDICT.md`). This iteration exists for one reason:
no earlier eval used a JavaScript library, so assertion `a8` (library misuse)
had never had a chance to discriminate. This eval asks for GSAP and Leaflet.

**This is a single cell, not a pass rate.** One prompt, one with-skill run, one
baseline. Numbers below say what happened once.

| Configuration | Passed | Failed | Tokens | Time |
|---|---|---|---|---|
| with_skill | 9/9 | none | 166,360 | 13.8 min |
| without_skill | 7/9 | a4 (one 25+-word sentence), a7 (brand NON-COMPLIANT, 4 violations) | 100,601 | 3.6 min |

## What the cell says

- **a8 still did not discriminate.** Both runs used GSAP and Leaflet cleanly:
  no `repeat: -1`, no `stagger` everywhere, tiles attributed, wheel-zoom off.
  The baseline reached that on its own. So `a8` is now 0-for-4 on telling the
  runs apart. It stays because it guards a documented failure mode, not because
  it has ever fired.
- **The two-guard thesis replicated a fourth time.** The baseline passed the
  AI-look guard (2/100) and failed the brand guard. With the skill, 0/100 and
  COMPLIANT. Same shape as iteration 2, with a mechanism recorded there.
- **Copy** is where the skill's plain-words rule shows: grade 3.2 vs 4.5, and
  the baseline's one long sentence is the only mechanical miss besides brand.
- **Rendered check, offline** (CDNs blocked, so repeatable): with_skill fails
  one AA target (a 274x21 px map link, WCAG 2.5.8); baseline fails five text
  nodes at 4.21:1 (section eyebrows, WCAG 1.4.3). No assertion depends on the
  rendered line, so neither cost a point; both are recorded in each run's
  `render_offline.txt`. The with-skill agent reported `rendered SKIPPED` in
  its own proof line because Playwright was not on its path; the lead re-ran
  it with the render venv, which is the FAIL above.
- **Online render** timed out loading the CDN scripts on this session's flaky
  network and is recorded as ERROR, not as a page fault
  (`without_skill/render_online_note.txt`).
- **Both runs invented nothing** (a6) and the with-skill run flagged its two
  stand-ins (map pin, brief) in the first line of its reply, as Step 1 asks.

## Judgment evidence

Each judgment assertion (a3, a5, a6) carries one line of evidence in
`*/grading.json`; the grader refuses to build this table while any judgment
is unrecorded.

## Cost

The with-skill run took 3.8x the time and 1.65x the tokens of the baseline,
most of it running the scanners and the brand guard and reading the two
library notes. That is the price of the proof line.
