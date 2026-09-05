# Vendored skill files

**TL;DR:** two official agent-skill repos are copied here, SKILL.md files
only. They are reference. When they disagree with this skill's own library
notes, this skill's notes win.

## What is here

| Folder | From | Commit | Date | Licence | Files |
|---|---|---|---|---|---|
| `gsap-skills/` | github.com/greensock/gsap-skills | `aed9cfd` | 2026-04-21 | MIT | 8 SKILL.md |
| `pixijs-skills/` | github.com/pixijs/pixijs-skills | `6aae70d` | 2026-06-04 | MIT | 26 SKILL.md |

Only `skills/**/SKILL.md` and each repo's `LICENSE` are copied. Examples,
assets and agent config files are not, to keep the bundle small. Fetched
2026-09-05 with a shallow clone.

## The override rule

These files describe how to use GSAP and PixiJS well. They do not know what
this skill knows: that fade-up-on-scroll, infinite pulse and particle fields
are the most common AI-look tells on the web. So:

1. For **how to call the API**, trust the vendored file.
2. For **whether to call it at all**, trust `../motion.md` and
   `../scroll-canvas-ui.md`. Those carry the ADOPT and AVOID rules and the
   scanner signatures.
3. If the two conflict, the AVOID rule wins. A vendored file will happily show
   you `repeat: -1`. The scanner will flag it. The scanner is right.

## Why vendor at all

The upstream repos move. A `SKILL.md` read from the live repo next year may
describe an API that the pinned version here does not have. The copy is a
snapshot tied to the versions in `../README.md`, so the two cannot drift
apart without someone noticing.

## Refreshing

1. Clone each repo shallow and copy the `SKILL.md` files.
2. Update the table above with the new commit and date.
3. Run `python3 ../../../scripts/ai_tell_scan.py --selftest`. It must still
   report all twelve library-misuse rules caught.
