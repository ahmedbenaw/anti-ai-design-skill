# Audit report: the anti-ai-design-style skill, end to end

Date: 2026-09-11. Subject: the whole skill, treated as the product. Method:
every check was re-run by a tool. Five pages were rendered and looked at.
Every script was read for anything that could hurt you. The official plugin
validator was run.
Nothing in this report is from memory.

## The short version

The skill works. Every automated check passes. It is also not finished, and
four things would surprise you if you used it today. They are listed first,
in plain words, with what I will do about each.

## Four things you would notice

### 1. A finished page shipped with "[ CLINIC NAME ]" still in it

In the evaluation, the skill was asked for a clinic website. It produced a
clean page and passed all 24 checks. The headline reads `[ CLINIC NAME ]`,
and three therapists are `[ Therapist name ]`. Nobody would upload that.

Why it happened: the skill has a rule against inventing facts, so it left
gaps rather than make up a clinic. That is honest. But no check looks for
bracketed placeholders in the finished page, so it passed anyway.

Fix: when a person is present, the skill will ask for the missing names
before it builds. When nobody is present, it will invent a clearly marked
stand-in and say so at the top of its reply. And a new check will fail any
page that ships with `[ ... ]` placeholders in visible text.

### 2. The scanner goes quiet on plain CSS

Ten of the thirty code rules only recognise Tailwind class names. A page
written in ordinary CSS, or exported from Framer or Webflow, can carry the
exact same tell and score zero.

I proved it with a test page. Three uppercase, letter-spaced eyebrow labels
written in plain CSS scored 0. The same labels written as Tailwind classes
scored 2. Same tell, same look, different spelling.

Why it happened: the rules were built from a corpus that is mostly Tailwind
(Lovable, Bolt, v0). Nobody wrote the CSS twin.

Fix: add the CSS form to each of the ten rules, test first so each one is
seen to fail before it passes. The fingerprint will change.

### 3. `/design-fix page.html` ignores the file name

The command advertises that it takes a file. The instructions inside never
read it. So the file name you type is silently dropped.

Fix: one line. Confirmed by the plugin validator as well.

### 4. The page that passed every check looks plainer than the one that failed

This is one comparison, judged by my eye, so treat it as a lead. The clinic
page the skill produced passes every gate and sits in a narrow column with a
lot of empty screen. The page produced without the skill fails the brand
check. It also looks like a designer made it.

Why it happened: the four gates measure AI-look, craft, copy and brand
distance. None of them measures "does this look composed". A page can pass
all four and still be flat.

Fix: this is the strongest honest reason to add the design-system checklist
you asked for, as a fifth axis that is judged rather than scored. It will
never be mixed into the score, and the skill will never claim to "check
governance" by machine.

## Everything else found

| # | Finding | Severity | Why | Fix |
|---|---|---|---|---|
| 5 | ~~Installing as a plugin does not ship the skill itself~~ **Withdrawn.** The sub-validator said `SKILL.md` must sit under `skills/`. The official docs say a single-skill plugin may place it at the root, and `claude plugin validate` prints `Validation passed`. No change. | withdrawn | The sub-validator applied a rule the docs do not have | None |
| 6 | `hookify_check.py` hardcodes one marketplace path | should-fix | Written on this machine | Honour a `HOOKIFY_PATH` variable, the way the brand guard honours `ANTI_ANTROPIK_PATH` |
| 7 | Scripts carry `#!/usr/bin/env python3` but are not executable | nit | Never invoked directly | `chmod +x` |
| 8 | `.serena/` (a tool's own files) is tracked in git | tidy | Committed by accident | Untrack and ignore |
| 9 | `SKILL.md` is 332 lines against a 300 target | tidy | Two blocks added in T6 | Move the long "what v2 got wrong" bodies to `reference/lessons.md`, keep one-liners |
| 10 | The description-tuning loop measured nothing (every score 0.0) | open | The harness never saw a tool call to detect | Harness bug; recorded, not fixable here |
| 11 | Check `a8` (library misuse) never separated skill from baseline | open | No evaluation task uses a library | Add a fourth evaluation that does |
| 12 | Pages that load fonts or Tailwind from the internet render as INCONCLUSIVE | by design | The renderer blocks the internet so results are repeatable | Correct for local files. A live-site audit needs a separate mode |
| 13 | The newest lessons (the cream palette, the stale-risk miss, side-tab) are not in `SKILL.md` yet | gap | Found after the last SKILL.md edit | Fold in via `reference/lessons.md` |
| 14 | Graph dangling edges | resolved | Earlier count used the wrong key | 930 nodes, 2,246 links, 0 dangling |

## Safety review, for a non-technical owner

I read every script for anything that deletes, phones home, or handles a
password. Findings:

- Two delete calls exist. Both delete only a temporary folder the script
  created seconds earlier for its own test, and nothing else.
- No script contacts the internet at run time. The web addresses in the
  code are inside test fixtures, as text, and are never fetched.
- No script reads or stores a password, key or token.
- `install.py` has `--dry-run` (shows what it would do) and `--uninstall`.
- The renderer blocks all network access on purpose.

Nothing here can damage your files or leak anything. That statement is
based on reading the code, not on trust.

## What passed, tool-printed

- Six self-tests: PASS.
- Example pages: slop 52 FAIL, fixed 0 PASS, fingerprint `b7cd873aa4831ab9`.
- Full gate on the clean example: `PASS ... brand distance COMPLIANT, rendered PASS`.
- Fail-closed with the brand guard hidden: `brand distance NOT RUN`, exit 1.
- 150 citations resolve, 0 broken; 368 sources; 16 research files.
- All five hookify rules load in hookify's own loader.
- Plugin validator: PASS, no blockers.
- Plain-language check: PASS on all six user-facing documents.
- Evaluation: with_skill 24/24, baseline 17/24, n = 1 per cell, with the.
  caveat in finding 1

## Where the skill can be installed, honestly

- **Claude Code**: works today, as a skill or as a plugin (finding 5 applies).
- **Cowork**: uses the same plugin format. Should work once finding 5 is
  fixed; will be verified, not assumed.
- **Codex**: reads the same `SKILL.md` format from `.agents/skills/`. It has
  no slash commands and no hooks, so only the skill body ports. The
  `$SKILL` path line added in T6 is what makes it portable.
- **Claude Design**: there is no separate install. It is the `/design`
  canvas inside the same session. "Installed in Claude Design" means the
  skill tells the model to run its checks on canvas artboards. I will not
  describe this as a fourth install, because it is not one.

## What happened next (status 2026-09-11)

| Step | Status |
|---|---|
| 1. Routine fixes, test first | **Done** in `9c36fd3`. Ten CSS twins, `/design-fix` argument, `HOOKIFY_PATH`, exec bits, `.serena/`, SKILL.md at 300 lines, `lessons.md`. |
| 2. Vendor `anti-antropik-design` | **Done** in `9c36fd3`, as-is. The installed copy wins; the proof line says `(installed)` or `(vendored)`; a selftest pins the vendored fingerprint. No licence file exists in the source, stated in `vendor/README.md`. |
| 3. Design-system standard, three tiers | **Done** in `f5caa5b`. CR7, CR8, CR9 measured; `reference/design-system-checklist.md` for the rest, judged by a person, never scored. |
| 4. Packaging | **Done** in `f5caa5b`. Codex via `install.py --codex`; Cowork is the plugin format that `claude plugin validate` passes; Claude Design is the same session. |
| 5. Live-site audit mode | **Done** in `f5caa5b`. `--allow-network` plus `reference/live-audit.md`. |
| 6. Placeholder check and fourth eval | Check **done**; the fourth eval is **running**. |
| 7. Re-run, repackage, handover | After the fourth eval reports. |

Finding 1 is now caught by the copy checker and by eval assertion `a9`.
Finding 2 is closed with a red-then-green fixture per rule. Finding 3 is a
one-line fix. Finding 4 is what the checklist in step 3 is for.

## Update 2026-09-11, after the adversarial review

Three read-only reviewers went over every scanner change made for this
report. They found 17 problems; every one was reproduced by hand and 13 fixes
went in, test first. The one that mattered most concerns a double install.
If this skill is installed twice, once as a plugin, the plugin copy's frozen
brand guard could beat your real one. The proof line would still say
"(installed)". That is fixed and tested. The others were spellings the scanner missed or wrongly caught. Examples:
upper-case hex, `rgba()` gradients, `[PDF]` badges, a logo inverted for dark
mode. One more: a Codex install that could not be undone. Verdict and evidence:
`interrogate/VERDICT.md`, `interrogate/reproduction-log.md`. New rules
fingerprint `b591c533d917bdd4`. Evals re-measured: same grades.
