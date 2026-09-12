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

## Repository map

| Path | What it is |
|---|---|
| `anti-ai-design-style/` | The skill. Scanners, rules, register, sources, examples, templates. Canonical. |
| `install.sh`, `install.ps1`, `installer/` | The universal installer and its contract. |
| `anti-ai-design-style-workspace/` | Evaluation runs, the adversarial review, measurements. History; not edited after the fact. |
| `HANDOVER-claude-code.md` | What was built, what was found, what is still open. |
| `CHANGELOG.md` | Versions and what changed. |
| `archive/` | Older drafts, kept because earlier notes cite them. Not current. |
| `proposals/` | Suggested changes to the sibling skill this one cross-checks against. |

## Known limits

- No pixel-based AI detector exists, and this skill never claims one. It
  measures code, copy and colour.
- The library-misuse check has never discriminated in four evaluations. It
  stays as a guard, not as evidence.
- Near-grey gradients such as `#f4f4f5` still count as colour washes; a
  regex cannot judge colour distance.
- `install.ps1` is unexecuted on Windows at the time of writing.

## Refresh the register by March 2028

The tells register is stamped `2026.10`. It describes how AI-made design
looked when it was written, so it ages. Two kinds of row age fastest. Rows
marked `[STALE-RISK]` name a literal from some tool's starter project, and
they die the day that project is rewritten. Era-tagged rows are tied to one
generation of models. A stale rule is quiet, not loud: it keeps passing its
own fixture while matching nothing real.

March 2028 is about eighteen months out, which is roughly how long the
previous register held up. Nothing breaks on that date. It is the point to
re-read the rows rather than trust them. The steps are at the end of
`anti-ai-design-style/reference/tells-register.md`, under "Keeping this
register alive".

## Licence

No licence file has been chosen yet, which means all rights reserved by
default. Until one is added, you may read the code but not reuse it.
