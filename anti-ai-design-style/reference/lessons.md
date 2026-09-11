# What this skill got wrong, and what it learned since

The short version lives in `SKILL.md`. This is the long one, kept out of the
skill body so the body stays under its length target.

## From v2, found while building v3

### It measured one distance and called it "distinct."

v2 scored how far a design sat from *generic AI output*. It never asked how close the design sat to *a specific house style*. So its own four pages went through the brand guard too. **Four out of four passed one guard and failed the other.** Escaping the average is not the same as arriving somewhere. The proof line now carries a brand-distance field, and a missing brand guard is a FAIL, not a shrug.

### It trusted its own word lists past their expiry

The cadence rules encoded 2023-24 vocabulary and nothing since. AI vocabulary turns over about every 18 months, so a rule with no era tag is a rule that quietly stops working. Every rule now carries one.

### It graded a phone frame instead of a button

One eval passed "button is at least 44px" against a `min-height: 844px` that was the simulated phone, not the control. A check measuring the wrong element passes forever and tells you nothing.

### Its citations pointed at two different things with the same spelling

`P13` meant a research finding in one file and a source in another. Nothing crashed; the evidence chain just stopped meaning what it said. `scripts/check_citations.py` now fails if a citation stops resolving.

### It never ran its own hooks

Four of the five fired on a field that the event does not provide. They were correct-looking and inert. Reading a rule is not running it.

## Found after v3 shipped, by testing it

### The popular escape from the AI look walks into the brand guard

Iteration 2 of the evaluation: every page built without the skill passed the
AI-look guard and failed the brand guard. Every brand failure was a warm cream
within Delta-E 12 of the brand neutrals. Told to avoid looking generic, the
model reaches for warm-paper editorial, which is the current convergence wave.
The two guards are close to orthogonal. Only the runs that generated a palette
with `generate_palette.py` cleared both.

### A stale-risk marker nobody was scheduled to read

MB2's row said "re-verify before each release". The release happened and
nothing re-verified, because the maintenance checklist never mentioned the
stale rows. Worse, the register claimed MB2 covered two Expo scaffolds. It
covered one. Source M36 fed a rule its literals could not fire. MB4 closes it.
Step 8 of the checklist now exists.

### Ten rules only knew the Tailwind spelling

The corpus is mostly Lovable, Bolt and v0 output, which is Tailwind. Ten of
thirty code rules were written from it and matched only class names. A
hand-coded page carrying the same tell as a CSS property scored 0. Proved with
a red fixture, fixed with a CSS twin per rule, guarded by a clean CSS page.

### A hand-made "AI slop" fixture is evidence about our beliefs

The side-tab accent border, called "the most recognizable AI tell" by another
tool, was counted across 12 verified-generated repos: 2 of 12, with 9 of 12
instances in one project. The page that raised it was hand-authored with no
generator marker. Its three side-tabs recorded what someone thought AI output
looks like. LA8 is down-weighted to 1.

### A passing check is not a working check

`check_citations.py` reported 0 broken while a citation pointed at a rule its
source could not support. A fixture passed while its rule matched nothing
real. Both were green-light failures. The question to ask of every check is
what it would fail to catch.

### A tool's warning is a lead, not a finding

Design-hook messages were written up as findings about delivered pages. The
tool's own detector, run afterwards, returned nothing on every delivered page.
The hook fires on drafts. Run the tool yourself, on the artefact, with a
positive control proving it was switched on.
