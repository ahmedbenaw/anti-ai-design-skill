# Reproduction log for the reviewers' findings

Every claim below was re-run by the lead (not taken on trust) with probe pages
under the session scratchpad, against fingerprint `ee9ee6320a9a639b`.
Date: 2026-09-11.

| # | Reviewer | Claim | Reproduced? | Evidence |
|---|---|---|---|---|
| B1 | opus | CO3 CSS twin is hex-only; `rgba()`/`hsl()`/named gradients never count | yes | five non-hex purple/pink gradients + one hex: CO3 did not fire (only CO1 on the hex one, 1 pt) |
| B2 | opus | CO3 CSS twin counts grey-to-grey gradients | yes | six neutral panel gradients: `[CO3] +4` |
| B3 | opus | CO4 / LA9 hex lists are lowercase-only | yes | `#E5E7EB` + big shadow: LA9 silent; `#e5e7eb`: fires |
| B4 | opus | placeholder regex flags `[DHL]`, `[VISA]`, `[PDF MENU]` | yes (same as C2) | `[NOTE]`, `[IMPORTANT]`, `[DRAFT]` all match |
| B5 | opus | CR8 `requires` is page-wide, so a logo `invert(1)` plus any dark-mode block fires | yes | token dark block + `.logo-mark{filter:invert(1)}`: `[CR8]` |
| B6 | opus | `--uninstall` ignores the Codex tree; `--codex --dry-run` prints "Also added" | yes | 121 files left; "Nothing to remove"; dry run says "added" |
| B7 | opus | vendored-fingerprint selftest check is appended after the print loop | yes | six `ok` lines printed, no fingerprint line |
| B8 | opus | `--allow-network` leaves no trace in the proof line; no-op without `--render` | yes | proof line reads `rendered SKIPPED`, no warning |
| B9 | opus | TY4 font-size arm stops at 99px | yes | `140px` sandwich: silent; `96px`: fires |
| C1 | sonnet | docstring still says "fails closed" though the vendored copy makes NOT RUN unreachable in normal use | yes (wording) | `find_brand_guard.py:10-12` |
| C2 | sonnet | placeholder regex flags `[NOTE]` etc. | yes | see B4 |
| C3 | sonnet | CO4 rgba arm misses `0.20` / `.25` | yes | `0.20` no match, `0.2` match |


## Where the points went (old rules `ee9ee6320a9a639b` vs new `b591c533d917bdd4`)

Checked before writing the report, because thirteen regexes changed at once
and "never weaken to pass" has to be shown, not assumed.

| Page | Old score | New score | Tells that changed |
|---|---|---|---|
| examples/slop-example.html | 50 | 50 | none |
| examples/fixed-example.html | 0 | 0 | none |
| iteration-2, six pages (`scan.txt` diffed at `1805e4c` vs re-capture) | as before | same | none; only the fingerprint header line differs |
| iteration-3, two pages | 2 / 0 | 2 / 0 | none |

The docs had quoted 52 for the slop example and the deslop input. Both score
50, and did before this review: LA8 went from 3 points to 1 in T10 after the
side-tab measurement (2 of 12). The stale number was in `examples/README.md`,
the handover and the grader label, all corrected 2026-09-11.
