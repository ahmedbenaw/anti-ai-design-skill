# Interrogate verdict: sprint-2 scanner changes (`0053ff8..HEAD`, scripts only)

Three adversarial reviewers (Fable, Opus, Sonnet), read-only, same diff and
rubric. Lead re-ran every claim before judging it; see `reproduction-log.md`.
Reviewer reports: `reviewer-A-fable.md`, `reviewer-B-opus.md`, `reviewer-C-sonnet.md`.

**Diversity caveat.** All three reviewers are Anthropic models. The interrogate
method gets its adversarial signal from model diversity, and there is less of it
here than the method assumes. Consensus below is therefore weaker evidence than
it would be across vendors, which is why every item was reproduced by hand.

## Agreement map

| Issue | A | B | C | Lead reproduced |
|---|---|---|---|---|
| Placeholder regex flags any all-caps bracket (`[NOTE]`, `[PDF]`, `[DHL]`) | 3 | 4 | 2 | yes |
| Codex install is not reversible; dry run says "added" | 8 | 6 | | yes |
| CR8 fires on a logo/icon `invert(1)` | 6 | 5 | | yes |
| Vendored-fingerprint selftest line never printed | 9 | 7 | | yes |
| Vendored guard: wrong label through plugin glob; switch cannot remove it | 1 | | (1: docstring) | yes |
| CO3 CSS twin: hex-only, misses `rgba()`/`hsl()` stops | | 1 | | yes |
| CO3 CSS twin: counts grey-to-grey gradients | | 2 | | yes |
| CO4 / LA9 hex lists lowercase-only | | 3 | | yes |
| CO4 rgba arm misses `0.20`, `.25` | | | 3 | yes |
| TY4 font-size arm stops at 99px | | 9 | | yes |
| `[^}]*` twins span unrelated inline `style=""` attributes | 2 | | | yes |
| TY5 and MO2 CSS twins tighter than their Tailwind form | 4 | | | yes |
| CR7 counts `var(--x, #hex)` fallbacks | 5 | | | yes |
| CR9 fires when a box-shadow focus ring is present | 6 | | | yes |
| MO3 fires at `@keyframes pulse` definition, away from `.skeleton` | 7 | | | yes |
| `--allow-network` leaves no trace; no-op without `--render` | | 8 | | yes |
| Craft loop has three ad-hoc shapes | 10 | | | read |

## Act on (all applied in this sprint, fixture-first)

1. **Vendored guard identity (A1, C1).** "Vendored" becomes structural
   (parent folder named `vendor`), the env switch filters every candidate by
   that test, a selftest plants a vendored copy under a globbed plugin path,
   and the docstring stops claiming a hard fail-closed. Critical: today a
   plugin-cache copy of this skill beats a real install and is labelled
   `(installed)`.
2. **Placeholder regex (A3, B4, C2).** Consensus 3/3. All-caps branch now
   needs a field word or two-plus words; `[PDF]`, `[BETA]`, `[NOTE]`, `[DHL]`
   join the OK fixture.
3. **CO3 CSS twin (B1, B2).** Stops may be hex, `rgb()`/`hsl()` or named;
   exact-grey stops (`#f0f0f0`, `rgb(n,n,n)`) are excluded by backreference.
   Red fixture gets an rgba gradient; clean fixture gets six grey panels.
4. **Case-insensitive hex (B3)** for CO4 and LA9 via scoped `(?i:…)`.
5. **CO4 rgba `.20`–`.29` (C3)**, matching the border arm.
6. **TY4 three-digit px (B9)**, digit-bounded.
7. **Inline-style span (A2).** `[^}]*` becomes `[^}"]*` in the six twins so a
   `style=""` attribute ends the span; clean fixture gets the inline case.
   Trade-off stated: a CSS block with a double-quoted string between the two
   declarations is now missed. Judged rarer than inline styles.
8. **TY5 / MO2 thresholds (A4).** One threshold per tell: the CSS twin takes
   the Tailwind range (`tracking-wide` = .025em; `scale-105`..`scale-129`).
   This widens the CSS side; nothing is weakened.
9. **CR7 `var()` fallback (A5)**, **CR8 selector anchor (A6, B5)**, **CR9
   box-shadow veto (A6)**, **MO3 definition-site (A7)**: each with a clean
   case that failed before the fix.
10. **Codex uninstall (A8, B6)** plus dry-run wording; selftest round-trips
    install and uninstall in a temp dir.
11. **Selftest print order (A9, B7).**
12. **`--allow-network` trace (B8):** proof line reads `rendered PASS (network)`
    and a warning prints when the flag is given without `--render`.
13. **Craft loop (A10):** one path. `requires` gates, `missing` vetoes,
    `patterns` counts (absent = 1). Selftest holds CR2/CR3/CR7–9 behaviour.

## Consider (not done this sprint)

- B2's stronger form: a real hue-distance check needs colour parsing, which
  the regex engine cannot do. The backreference exclusion catches exact greys
  only; near-greys like `#f4f4f5` still count. Recorded as a known gap in the
  register row for CO3.

## Noted

- B's clearance list (CR2 unaffected, fail-closed reachable with the switch
  and no vendored copy, LA8 down-weight documented, `[^}]*` cannot cross `}`)
  matches the lead's reading. A2 shows the same-block assumption fails in the
  other direction (no `}` at all), which is why item 7 exists.

## Dismissed

- None. Every finding reproduced. C1's framing ("fail-closed is defeated")
  overstates a documented design choice (T11: vendored fallback last, tagged),
  but its concrete point, the stale docstring, is real and is fixed under item 1.
