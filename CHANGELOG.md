# Changelog

Versions follow the skill's own `plugin.json`. Every scanner verdict prints a
rules fingerprint, so a number quoted in one version can be checked against
the rules that produced it.

## 3.1.0 — 2026-09-12, first public release

Rules fingerprint `b591c533d917bdd4`, register 2026.10.

**Added**
- `scripts/brand_distance.py`: brand distance measured by the skill's own
  code. Verified verdict-for-verdict against the original implementation on
  42 pages (0 differences) with an identical exclusion fingerprint
  `5697117fa1b27195`. An installed `anti-antropik-design` is now an optional
  cross-check; a disagreement fails the verdict.
- `--suggest`: replacement colours that clear the brand standard.
- Universal installer: `install.sh` (Mac, Linux), `install.ps1` (Windows),
  `installer/manifest.json`, `installer/INSTALL-SPEC.md`. One line installs
  to Claude Code, Cowork, Codex and detected editors, and ends by running the
  skill's own scanner on its own example.
- Ten CSS twins for rules that only matched Tailwind spellings, plus rule
  fixes from a three-reviewer adversarial pass (17 findings, all reproduced,
  13 fixed test-first).
- Craft rules CR7 (tokens bypassed), CR8 (dark mode by inversion), CR9
  (focus outline removed with nothing put back).
- Shipped-placeholder check in `copy_check.py`.
- Live-site audit mode (`--render --allow-network`), with the proof line
  marking a networked run.
- Design-system checklist as a labelled judgment axis, never mixed into the
  score.
- Fourth eval using GSAP and Leaflet.

**Changed**
- The vendored copy of `anti-antropik-design` is removed; nothing in the
  skill depends on it.
- The stop hook skips recorded evidence and the skill's own fixtures, and
  names what it skipped.
- `copy_check.py` counts dashes in visible text only, not in script payloads.
- LA8 (side-stripe borders) down-weighted 3 to 1 after measuring 2 of 12.

**Known limits, stated rather than hidden**
- `install.ps1` has not been executed on Windows yet.
- The library-misuse assertion has never discriminated in four evals.
- Near-grey gradients such as `#f4f4f5` still count as colour washes.
- No pixel-based AI detection exists, and this skill never claims one.

## 3.0.0 — 2026-09-11, internal

Rebuilt from the v2 bundle on Python 3.14. Added the proof line, the
brand-guard locator, the rendered craft check, hooks and commands. Register
bumped to 2026.10 with the new tells. Evals iteration 2 run.

## 2.x — 2026-09, bundle only

The `anti-ai-design-review-bundle.zip` era. Never run outside its author's
machine. Superseded.
