# Anti-AI-design skill — repository map

**TL;DR:** the real skill lives in `anti-ai-design-style/`. The loose `.md`
files at this top level are older review drafts. If two files disagree, the
one inside the skill folder wins.

## Install in one line

Mac or Linux:

```
curl -fsSL https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.sh | sh
```

Windows, in PowerShell:

```
irm https://raw.githubusercontent.com/ahmedbenaw/anti-ai-design-skill/main/install.ps1 -OutFile install.ps1; .\install.ps1
```

Both detect Claude Code, Claude Cowork, Codex and common editors, and install
to each. Each run ends by checking the skill's own example with the skill's
own scanner. A printed `PASS:` line is the proof; copied files are not. `--dry-run` shows the plan and
touches nothing; `--uninstall` removes it all. The shared algorithm both
scripts follow is in `installer/INSTALL-SPEC.md`.

## What is where

| Path | What it is | Trust it? |
|---|---|---|
| `anti-ai-design-style/` | **The skill.** Scanners, rules, register, sources, examples, templates. | Yes — this is canonical |
| `anti-ai-design-style-workspace/` | Eval runs. Measurements taken on a given day. | Yes, as history — do not edit to make numbers tidier |
| `PLAN-anti-ai-design-style.md`, `HANDOVER-claude-code.md`, `REVIEW-MANIFEST.md` | Build plan, handover notes, review manifest. | Yes |
| `tells-register.md` | Stale draft. Says register **2026.08**. | No — read `anti-ai-design-style/reference/tells-register.md` (**2026.09**) |
| `brand-distance.md` | Stale draft, 19 lines behind. | No — read `anti-ai-design-style/reference/brand-distance.md` |
| `sources-compendium.md` | Identical to the skill's copy today, but not the source of truth. | Read the skill's copy |
| `benchmark.md` | Iteration-1 benchmark, register 2026.08. Historical. | As history only |
| `anti-ai-design-review-bundle.zip` | The packaged bundle the skill was extracted from. | Archive |

## Why the duplicates exist

The skill was reviewed by unzipping parts of the bundle to the top level. Those
copies then fell behind while the skill folder kept moving. They are kept
because earlier notes cite them, not because they are current.

## Proving the skill works

Run these from `anti-ai-design-style/`. Each prints its own verdict — a claim
here is worth nothing without the tool's output.

```bash
python3 scripts/ai_tell_scan.py --selftest
python3 scripts/copy_check.py --selftest
python3 scripts/ai_tell_scan.py examples/
```

Expected: two `SELFTEST: PASS` lines, then `slop-example.html` scoring 52 (FAIL)
and `fixed-example.html` scoring 0 (PASS). Every verdict prints a rule
fingerprint, so two runs quoting the same fingerprint used the same rules.
