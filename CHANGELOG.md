# Changelog

Versions follow the skill's own `plugin.json`. Every scanner verdict prints a
rules fingerprint, so a number quoted in one version can be checked against
the rules that produced it.

## 3.5.1 — 2026-10-28

**Tests and a stale lesson, no behaviour change.** 3.5.0 claimed the session
filter applies to the first timestamp as well as the file names. That half
was true but unpinned. None of the three new cases carried a timestamp, so
`start` was always None and the mtime window never ran.

A fourth case pins it. The parent's line is stamped older than the page and
this session's is stamped newer. Take the start from the parent and the page
looks modified during the session. Take it from this session and the page is
correctly left alone. Checked both ways at the function: one file before the
fix, none after.

`reference/lessons.md` still said a file counts when "two things hold". It is
three now, and the entry says why the two correct rules were not enough.
Where a filter is applied matters as much as what it says.

## 3.5.0 — 2026-10-28

**The Stop hook blamed a session for files another session touched.** A fork
or a compaction copies the parent's history into the child transcript.
`ui_files_from()` read that file as one session. So a forked session
inherited every UI file its parent had ever named. It could then be blocked
over a page it never opened. Measured across this project's three transcripts:
two carried another session's lines, one of them 14,661 of 14,763. Both of
those sessions were credited with three files that belonged to the parent.

This is the 2026-10-11 blame trap reached by a different route, which is the
part worth recording. That fix added two filters, a tool filter and an mtime
window, and both were right. They were computed over the wrong population. Apply a correct window and
a correct tool list to lines that are not the session's, and the answer is
still wrong. The symptom is identical: a block no edit by that session can
clear.

The fix filters every line to the current session's id, for the first
timestamp as well as for the file names. The id comes from the hook payload. It falls back to the transcript's own
filename, which is the id. That was checked across all 15,367 lines of the
session named by this file. A line carrying no id at all still counts. It cannot be attributed, and
calling it foreign would switch the guard off wherever ids are absent.

Three selftest cases pin it. A failing page named only by a foreign line
is ignored. The same page named by the session's own line still blocks. The
filename fallback works when the payload omits the field. The middle case passed before the fix. That is what makes the other two
mean something: the machinery that must keep blocking does keep blocking. No rule changed,
so the fingerprint stays `3c8f23a11db4e800`.

## 3.4.3 — 2026-10-28

**A parser check for the Windows installer, so it stops being the untested
half.** `installer/check-install-ps1.ps1` runs PowerShell's own parser over
`install.ps1` and reports every error it finds. It also checks for CRLF line
endings, a byte-order mark, and a `param()` block that is not the first
executable statement. It exits non-zero on any of those, so it can gate a
release. PowerShell runs on macOS and Linux, so no Windows machine is needed
and the README says where to run it.

Worth recording how the third check was arrived at, because it is a small
lesson in writing assertions. It failed `install.ps1` three times while the
file was correct. First it did not know a `<# .. #>` help block may precede
`param()`. Then a second version had a syntax error of its own. Then it did
not know that `[CmdletBinding()]` may precede `param()` as well, which is in
fact where that attribute belongs. Each failure looked like a finding about
the installer and was a fault in the check. It now strips comments and
leading attributes before deciding, and it still rejects a file with real
code above `param()`.

No rule changed. Fingerprint stays `3c8f23a11db4e800`.

## 3.4.2 — 2026-10-28

**The PowerShell installer has now actually been run.** It had never been
executed since the day it was written. PowerShell runs on macOS, so it was
never as untestable as the note claimed.

What ran, under PowerShell 7.6.9, against a throwaway home directory:

- `-DryRun` listed the plan and wrote nothing. Exit 0, same as the shell
  installer.
- A real install placed the skill, the three commands and both of this
  week's new test pages.
- The hook branch took the right path. `settings.json` was left empty, with
  zero hook entries, which is the single-registration fix from 3.2.2 holding
  in PowerShell and not only in shell.
- Its own verification step ran the skill against its example and reported a
  genuine PASS.
- `-Uninstall` removed the skill, the commands and the Codex copy, leaving
  nothing behind.
- `-Help` exits 0.

Two static results worth recording. The script parses with PowerShell's own
parser with zero errors across 3361 tokens. It contains no PowerShell 7-only
syntax, so its claim to support Windows PowerShell 5.1 is plausible.

**What is still not proven.** None of this ran on Windows. `USERPROFILE`,
native backslash paths and Windows PowerShell 5.1 are untested. The README
says so in those words now, instead of calling the whole script unexecuted.

No rule changed. Fingerprint stays `3c8f23a11db4e800`.

## 3.4.1 — 2026-10-27

**The browser check could never have worked on Windows.** Shipped two
releases ago, found by auditing the PowerShell installer rather than the
Python. A virtual environment keeps its interpreter in `bin/` on macOS and
Linux and in `Scripts/` on Windows. Only `bin/python3` was probed.

So on Windows the venv was unreachable. The check fell back to whichever
interpreter ran the scan. If that one lacked Playwright the answer was
`rendered SKIPPED`, for ever, with nothing to indicate the cause. The setup
instructions added in 3.2.3 were Unix-only too, so there was no way to follow
them and no sign anything was wrong.

Both venv layouts are now probed in both locations, nearest first. Five
selftest cases pin the paths and their order. Reverting to the old Unix-only
list fails two of them, so the test catches the bug as it shipped. The README
carries the PowerShell commands beside the shell ones.

This is a path-construction fault, provable by inspection and held by a test
that runs anywhere. It does not need a Windows machine, which is why it could
be fixed without one. Running `install.ps1` on Windows is still untested.

No rule changed. Fingerprint stays `3c8f23a11db4e800`.

## 3.4.0 — 2026-10-27

**The library-misuse check works. The claim that it does not was wrong.**
Four releases carried a note saying the check had never discriminated. It was
offered as a guard rather than as evidence. That reads as "the check is
broken". It is not what happened.

The reason it never fired is sampling. Exactly one evaluation cell loaded an
animation library. Both pages in that cell used GSAP carefully, so zero was
the correct answer for both. The evaluation workspace
recorded that reason at the time. The README dropped it and kept only the
conclusion.

It is now held to a pair of real pages instead of a minimal fixture. Both
load GSAP and ScrollTrigger heavily. The library being present cannot be what
separates them:

- `examples/library-misuse-example.html` is new and raises five rules. Scroll
  hijacking. A reveal applied to every section at once. An endless tween.
  Overshoot easing. Body copy hidden from screen readers.
- `examples/library-careful-example.html`, real generated output copied byte
  for byte out of the evaluation run, raises none.

Both now ship with the skill. The first version of this test read the careful
page from the evaluation workspace. The installed skill does not have one. So
the selftest passed in the repo and failed once installed. Caught by running
the installed copy rather than trusting the repo.

Swapping the two pages makes the selftest fail in both directions, so the
assertions can fail. The selftest line now states the pair result, which
means the claim is defended by a test rather than by a paragraph.

What is still true, and now said plainly: no page in any evaluation has been
caught by this check. It is a working guard with no field catch to its name.

No rule changed. `rules.json` is untouched and the fingerprint stays
`3c8f23a11db4e800`.

## 3.3.0 — 2026-10-27

**The register's refresh date is now a check, not a note.** The register is
stamped, and the stamp ages. Until now the only thing watching that date was
a paragraph in the README asking someone to remember it.
`check_citations.py` now reads the stamp and prints one line once the
register is eighteen months old. It names the rows to re-read first. It still
exits 0, because a stale register works. It just stops being evidence. Five
selftest cases hold it at both ends of the horizon on a fixed clock, so the
check cannot drift into always-warning or never-warning.

**One limit written down rather than left implied.** The hooks run the
browser check with no network access. A page styled from a CDN reports
`rendered INCONCLUSIVE`, so contrast, tap targets and focus are unmeasured
for that page. That is the intended trade: a hook that fetches from the
network on every stop is worse. Measure one by hand with
`verify_all.py --render --allow-network`. Now in the README's known limits.

No rule changed. Fingerprint stays `3c8f23a11db4e800`.

## 3.2.3 — 2026-10-27

**The browser check had never run.** Contrast, tap-target size and focus
rings went unmeasured on this machine. Nobody noticed. The proof line said
`rendered SKIPPED` instead of failing. A skipped check that reads as a passed
one is the exact failure this skill exists to prevent.

Three things were wrong. Each one alone was enough to hide the other two.

- **The hooks never asked for it.** `verify_all.py` leaves the rendered check
  off unless `--render` is passed. Neither `stop_check.py` nor `hook_scan.py`
  passed it. Both do now. A selftest case asserts it in each file, because
  nothing caught this for three releases.
- **No Python had Playwright in it.** How to set one up is now in the README.
  So is why it belongs beside the skill folder rather than inside it. The
  installer replaces that folder. Anything kept inside is deleted on every
  install.
- **Pillow was missing, and that corrupted a measurement silently.** Without
  it the check cannot sample what is painted behind the text. It falls back
  to the colours in the stylesheet. A number sitting on a block painted by a
  positioned sibling was reported at 1.25:1. What is painted behind those
  glyphs measures 4.89:1. That is a false failure, and it points at the wrong
  fix. Reproduced in two separate environments.

**A browser that cannot start no longer blocks you.** In a sandbox or a
container the browser is installed but refuses to launch. That gives
`rendered ERROR`. Treating it as a failure would block every stop with "fix
what the line names", and no edit to the page can fix it. The stop hook now
reports it and lets you stop. It already handled a brand check that could not
run the same way. The proof line still shows the state, so the measurement is
never quietly counted as a pass.

No rule changed. `rules.json` is untouched and the fingerprint stays
`3c8f23a11db4e800`.

## 3.2.2 — 2026-10-27

**Fixed**
- The installer registered the two hooks a second time. The skill already
  carries `hooks/hooks.json`, which Claude Code loads from the skills folder,
  so writing the same hooks into `settings.json` made each one run twice on
  every stop. Both layers now add nothing when `hooks.json` is present. They also
  strip any entry an older installer left. That heals an existing double
  registration on the next run.
- The README has said "do not also add these hooks to settings.json" since
  2026-10-27 while the installer did exactly that. The code now matches.

Measured after the fix: a full install leaves zero of this skill's entries in
`settings.json`, and the 23 hooks belonging to other tools are untouched.

## 3.2.1 — 2026-10-27

Rules fingerprint `3c8f23a11db4e800`, register 2026.10.1.

**Changed**
- The repository a fix was found in is no longer named. The notes, code
  comments and fixtures now say "a client repo". The product those failures
  came from is outside this skill's scope. It was the case that exposed the
  bugs, not a subject of the rules.
- Fixture URLs point at example.com.

**Why the fingerprint moved without a rule change**
- One of the renamed strings is a comment inside `rules.json`, and the
  fingerprint covers that whole file. No pattern, weight, threshold or tell
  changed. The register stays 2026.10.1 for that reason. Every selftest
  passes unchanged on 3.9.6 and 3.15.1.

## 3.2.0 — 2026-10-27

Rules fingerprint `ceb58447cffcc597`, register 2026.10.1. Brought across from
the installed copy, which was ahead of this repository.

**Fixed**
- Copy check: grades only the words a reader sees. Code inside `.css`, `.jsx`
  and `.tsx` files is no longer read as prose; the strings and screen text in
  it still are.
- Copy check and AI-tell scan: a list a page marks as words it never uses is
  skipped, so a brand book's own ban list stops counting against it.
- Stop hook: a file counts as the session's work only when the session's own
  tool call named it and the file changed after the session began. It used to
  blame a session for files it had merely read or seen mentioned.

**Added**
- `scripts/project_exceptions.py`.

**Note**
- Register the two hooks once, through the skill's own `hooks/hooks.json`.
  A second entry in `settings.json` runs the same hook twice.

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
