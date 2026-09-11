# Retro — the v3 sprint

Written 2026-09-11, after T7 ran. Committed scope was T1, T6, T8, T9, with T7
as stretch. All of it shipped, and T7 with it.

## What the sprint was actually for

The dossiers were written before this sprint and nothing had reached
`rules.json`. Research that never becomes a rule is a reading list. The sprint
closed that gap, and then two more that only showed up once the work started.

## What went well

**Fixture-first held every time.** MB4 was written by adding the fixture,
watching the selftest print `FAIL - mobile fixture missed expected rules:
['MB4']`, and only then writing the regex. That is the whole reason the rule
can be trusted. A rule whose fixture never failed has never been tested.

**Counter-evidence got recorded instead of deleted.** Five literals were
considered for MB4 and rejected. All five are in the register with the reason.
The false-positive fixture makes the rejection permanent: loosen the filter
and the selftest fails.

**The measurement beat the guess, twice.** The 44px touch target was measured
on the button element in a real browser, not inferred from padding. The era
tag came from walking npm versions 51 to 57, not from picking a plausible year.

## What went wrong

**A `[STALE-RISK]` marker with no step behind it.** MB2's row said "re-verify
before each release". The release happened and nothing re-verified, because
the seven-step maintenance checklist never mentioned the stale rows. A warning
nobody is scheduled to read is decoration. Step 8 now exists.

**A citation that resolved and still lied.** M36's `Feeds: MB2` pointed at a
real rule. `check_citations.py` reported 0 broken the whole time, because it
checks that IDs resolve, not that the target can support the claim. A dangling
citation is loud. A mis-aimed one is silent, and it hid a coverage gap for a
whole release.

**Committing while agents were still writing.** A `git add -A` during the eval
runs captured `budget-home.html` mid-flight. Nothing was corrupted, and the
later diff was the agent's own work, but the commit was meaningless. Do not
commit a workspace with live runs in it.

**I wrote up a tool's warnings as findings without running the tool.** The
design hook flagged four things on eval outputs. I put them in a findings file
and committed it. Running that tool's own detector afterwards returned zero
findings on all six artifacts. The hook fires on every write. It was
reporting drafts the agents then fixed. I had even said in the same session
that I would not treat a hook message as a result. A warning is a lead. Run
the tool yourself, on the artifact you are claiming something about, with a
positive control proving it was switched on.

**My own prose failed this skill's copy checker six times.** Every one was a
sentence over 25 words. Fixed every time, never exempted. Once I committed
before running the check and had to amend. Run the check, then commit.

## What to carry forward

1. **`side-tab`.** A verified gap, shown on a page built to show it rather
   than on an eval output: 2 anti-patterns there, 0/100 PASS here. It is not a
   cheap regex. The rule compares one border against the other three, against
   the radius, and against colour neutrality, so it needs the cascade
   resolved. `iteration-2/cross-tool-findings.md` has the experiment and the
   control problem that comes with it.
2. **A fourth eval that uses a library.** `a8` library misuse scored 0 in all
   six runs and never discriminated, because no task here pulls in an
   animation or map library. The assertion is fine; the eval set is missing a
   case.
3. **The description loop still measures nothing.** Every query scored 0.0 on
   both sides because `claude -p` produced no tool call for the harness to
   detect. Fixing the harness is a prerequisite to any description work.
4. **n = 1 per cell.** Repeats would turn directional results into measured
   ones. The brand-guard separation was 3 for 3, which is suggestive and not
   yet a rate.

## The finding worth keeping

The two guards are close to orthogonal, and now there is a reason rather than
a coincidence. Every baseline brand failure was a warm cream inside Delta-E 12
of the brand neutrals. Told to avoid looking generic, the baseline reached for
warm-paper editorial, which is the current convergence wave. The popular
escape from the AI look lands inside the brand violation zone.

A page can satisfy one guard by means of failing the other. That is the
argument for running both, and it is now backed by six runs rather than an
anecdote.
