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
| 5 | Installing as a plugin does not ship the skill itself. `SKILL.md` sits at the root, not under `skills/`. The README admits a second manual step. | should-fix | Layout predates the plugin tier | Move it under `skills/anti-ai-design-style/` and repoint paths. Or add a `skills` entry to the manifest. |
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

## What happens next, in order

1. Routine fixes, test first: findings 2, 3, 5, 6, 7, 8, 9, 13.
2. Port `anti-antropik-design` in as a verbatim copy under `vendor/`. The
   locator prefers your installed copy and falls back to the vendored one.
   The proof line will say which was used. Note: copying it "as is" also
   copies the four small defects already listed in `proposals/`.
3. The design-system standard, in three tiers: already measured; newly
   measurable (test first); everything else as a labelled checklist.
4. Packaging for Claude Code, Cowork and Codex, each verified live.
5. A live-site audit mode using the in-app browser. Craft only, with screenshots for the judgment checklist. It keeps the standing line that no tool can tell AI-made from a picture.
6. A fourth evaluation that uses a library, and a placeholder check.
7. Re-run everything, re-package, update the handover.

One question stays open for you at step 2, because it cannot be undone cleanly. Vendor the sibling as-is, including its known defects? Or vendor it with the four fixes applied and labelled? My recommendation is
as-is, with the defects listed, because "as is" was your instruction and
the fixes belong upstream.
