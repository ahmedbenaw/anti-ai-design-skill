# anti-ai-design-style

A measured guard against the "AI-generated look" in web and mobile design.

Everything AI makes looks fine at a glance. That is the problem. This skill
does not ask whether a page looks fine; it measures it. A scanner scores the
known tells of AI-made design from a sourced, dated register. It checks the
accessibility craft. It measures how close the colours sit to one brand's
palette. Then it prints one line. Work is not done until that line starts
with `PASS`.

```
PASS: AI-look 0/100 (distinct), craft flags 0, library misuse 0, copy grade 4.6, brand distance COMPLIANT, rendered SKIPPED | register 2026.10, rules b591c533d917bdd4, brand rules 5697117fa1b27195 (native)
```

That line is quoted, never composed. The two fingerprints name the exact
rules that produced it, so any number in any report can be checked.

## Install in one line

Mac or Linux:

```
curl -fsSL https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.sh | sh
```

Windows, in PowerShell:

```
irm https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.ps1 -OutFile install.ps1; .\install.ps1
```

Both find Claude Code, Claude Cowork and Codex, and install to each. Each run
ends by checking the skill's own example with the skill's own scanner. A
printed `PASS:` line is the proof; copied files are not. `--dry-run` shows
the plan and touches nothing; `--uninstall` removes it all. When piping,
flags go after `sh -s --`, for example `| sh -s -- --dry-run`.

**It installs this skill and nothing else.** No Node, no npm packages, no
system package-manager calls, no third-party installer. Every path it writes
belongs to this skill and is listed before it is written. The scanners are
plain Python with no third-party imports. Python is needed only by the two
hooks. If it is missing, the installer says so and prints the one command
that fixes it, rather than installing software you did not ask for.

For Cursor, VS Code and other editors, the installer prints a one-line
command instead of running it. That command needs Node and downloads a
third-party tool, so it is yours to run knowingly. A browser check is
optional and needs Playwright; without it the line says `rendered SKIPPED`,
which means that check did not run.

Status, stated plainly: `install.sh` was run end to end on macOS, from a
clone and from the downloaded archive. `install.ps1` was written to the same
spec but has not yet been executed on Windows. Its `-DryRun` changes nothing.

## What you get

| Piece | What it does |
|---|---|
| The skill | Loads whenever Claude builds or edits visual output. Brief first, build, scan, fix until PASS, quote the line. |
| `/design-check <file>` | Scans a file and explains the findings in plain words, worst first. |
| `/design-fix <file>` | Fixes every finding, then proves it with a rescan. |
| `/design-brief` | Writes the two-minute brief that stops generic output before it starts. |
| Two hooks | Scan each UI file as it is written; re-check the session before it ends. Silent on anything that is not a UI file. |

The two hooks register themselves through the skill's own `hooks/hooks.json`.
Do not also add them to `settings.json`: a second entry runs the same hook
twice on every stop.

One thing the installer cannot do: five hookify warning rules load only from
the folder you work in. Inside any project, run
`python3 ~/.claude/skills/anti-ai-design-style/scripts/install.py .` once.

## How it decides

Two guards, nearly independent of each other. Every baseline page in the
evaluations passed the first and failed the second.

1. **AI-look distance.** Thirty-odd code and copy tells, each with a source,
   an era tag, a weight and a test fixture. Score under 20 and no near-proof
   finding passes. Craft problems (contrast, targets, reduced motion, tiny
   text) are reported alongside but never added to the score.
2. **Brand distance.** Colours and typefaces measured against one published
   brand palette in CIE Lab with Delta-E 2000. Implemented in
   `scripts/brand_distance.py`; verified verdict-for-verdict against the
   original implementation on 42 pages with zero differences.

Judgment stays out of both. A separate checklist covers what no scanner can
see, labelled as judgment, never mixed into a number.

## What the evaluations say

Four tasks, each run with the skill and without, one run per cell. Grades
are recorded in `anti-ai-design-style-workspace/` and never edited to look
tidier.

| Set | With skill | Without |
|---|---|---|
| Iteration 2, three pages | 25/27 | 19/27 |
| Iteration 3, a page using GSAP and Leaflet | 9/9 | 7/9 |

A single run per cell is a measurement, not a pass rate. The workspace says
so on every benchmark.

## Prove it works yourself

From `anti-ai-design-style/`:

```bash
python3 scripts/ai_tell_scan.py --selftest
python3 scripts/brand_distance.py --selftest
python3 scripts/verify_all.py examples/fixed-example.html
python3 scripts/verify_all.py examples/slop-example.html
```

Expected: two `SELFTEST: PASS` lines, then a `PASS:` line for the fixed
example and a `FAIL:` line scoring 50 for the slop example.

The Windows installer is the one part of this repo the Python selftests
cannot reach. PowerShell runs on macOS and Linux too, so check it anywhere:

```bash
pwsh -NoProfile -File installer/check-install-ps1.ps1
```

Expected: `PARSE: OK - 0 errors`, then `CHECKS: PASS`. It exits non-zero on
a parse error, so it can gate a release.

## Turn on the browser check

Contrast, tap-target size and focus rings are measured by rendering the page
in a real browser. That check needs a Python with Playwright in it. Without
one the proof line reads `rendered SKIPPED`, and a skipped check is not a
passed one. Set it up once:

```bash
python3 -m venv ~/.claude/skills/.venv-render
~/.claude/skills/.venv-render/bin/python3 -m pip install playwright Pillow
~/.claude/skills/.venv-render/bin/python3 -m playwright install chromium
```

On Windows, in PowerShell:

```powershell
py -m venv "$HOME\.claude\skills\.venv-render"
& "$HOME\.claude\skills\.venv-render\Scripts\python.exe" -m pip install playwright Pillow
& "$HOME\.claude\skills\.venv-render\Scripts\python.exe" -m playwright install chromium
```

Three things about that path and those packages:

- The folder sits **beside** the skill, not inside it. The installer replaces
  the skill folder outright, so a virtual environment kept inside it is
  deleted on every install.
- **Pillow is required, not optional.** Without it the check cannot sample
  what is actually painted behind the text. It falls back to the colours in
  the stylesheet and then reports a contrast failure on text that is fine.
  Measured on 2026-10-27: the sibling-paint case in
  `render_check.py --selftest` fails without Pillow.
- `verify_all.py` looks for `$RENDER_PYTHON` first, then `.venv-render`
  inside the skill, then `.venv-render` beside it. It checks both venv
  layouts in each place, `bin/` and `Scripts/`, so either platform is found.

Check it, from `anti-ai-design-style/`:

```bash
~/.claude/skills/.venv-render/bin/python3 scripts/render_check.py --selftest
python3 scripts/verify_all.py --render examples/fixed-example.html
```

On Windows, swap the first path for
`$HOME\.claude\skills\.venv-render\Scripts\python.exe` and `python3` for
`py`.

Expected: a `SELFTEST: PASS` line, then a `PASS:` line ending in
`rendered PASS`.

A browser that is installed but cannot start, as happens in a sandbox or a
container, gives `rendered ERROR` instead. The stop hook prints that and lets
you stop anyway, because no edit to the page can fix it.

## Repository map

| Path | What it is |
|---|---|
| `anti-ai-design-style/` | The skill. Scanners, rules, register, sources, examples, templates. Canonical. |
| `install.sh`, `install.ps1`, `installer/` | The universal installer, its contract, and a parser check for the PowerShell half. |
| `anti-ai-design-style-workspace/` | Evaluation runs, the adversarial review, measurements. History; not edited after the fact. |
| `HANDOVER-claude-code.md` | What was built, what was found, what is still open. |
| `CHANGELOG.md` | Versions and what changed. |
| `archive/` | Older drafts, kept because earlier notes cite them. Not current. |
| `proposals/` | Suggested changes to the sibling skill this one cross-checks against. |

## Known limits

- No pixel-based AI detector exists, and this skill never claims one. It
  measures code, copy and colour.
- The library-misuse check never fired in the evaluations, and the reason is
  sampling, not the check. Only one evaluation cell loaded an animation
  library at all, and both pages in it used GSAP carefully, so nothing was
  there to catch. It is now held to a pair of real pages. Both load GSAP and
  ScrollTrigger. `examples/library-misuse-example.html` raises five rules, and
  `examples/library-careful-example.html` raises none. The careful one is real
  generated output, copied byte for byte out of the evaluation run. Presence
  of the library is therefore not what separates them. One thing stays true.
  No page in an evaluation has ever been caught by this check. It is a working
  guard with no field catch to its name.
- Near-grey gradients such as `#f4f4f5` still count as colour washes; a
  regex cannot judge colour distance.
- The hooks run the browser check without network access. A page whose
  styling comes from a CDN therefore reports `rendered INCONCLUSIVE`, and
  contrast, tap targets and focus go unmeasured for that page. This is
  deliberate: a hook that fetches from the network on every stop is worse.
  Run `verify_all.py --render --allow-network <page>` by hand to measure one.
- `install.ps1` has been run end to end under PowerShell 7.6.9 on macOS.
  Dry run, install, its own self-check and uninstall, all clean. No hook
  entries were written to `settings.json`. It has never been run on Windows.
  Windows-specific behaviour is therefore unproven: `USERPROFILE`, native
  backslash paths, and Windows PowerShell 5.1. The script parses with no
  errors and holds no PowerShell 7-only syntax, so the 5.1 claim is
  plausible rather than tested.

## Refresh the register by March 2028

The tells register is stamped `2026.10`. It describes how AI-made design
looked when it was written, so it ages. Two kinds of row age fastest. Rows
marked `[STALE-RISK]` name a literal from some tool's starter project, and
they die the day that project is rewritten. Era-tagged rows are tied to one
generation of models. A stale rule is quiet, not loud: it keeps passing its
own fixture while matching nothing real.

March 2028 is about eighteen months out, which is roughly how long the
previous register held up. Nothing breaks on that date. It is the point to
re-read the rows rather than trust them.

You do not have to remember it. `scripts/check_citations.py` reads the stamp
and prints one line once the register passes eighteen months. It still exits
0, because a stale register works; it just stops being evidence. The steps are at the end of
`anti-ai-design-style/reference/tells-register.md`, under "Keeping this
register alive".

## Licence

No licence file has been chosen yet, which means all rights reserved by
default. Until one is added, you may read the code but not reuse it.
