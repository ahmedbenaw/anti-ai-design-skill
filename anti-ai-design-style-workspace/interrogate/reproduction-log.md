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
