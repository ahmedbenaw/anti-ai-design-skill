# Description loop, 2026-09-10

**Result: no change applied. The loop did not measure anything, and saying so is
the finding.**

## What was run

`skill-creator`'s `run_loop.py` against a 20-query set: 10 that should trigger
this skill, 10 that should not. The non-triggers include the near-misses that
matter. The sharpest is "does this page use any Anthropic brand colours it
should not". That one belongs to the sibling skill, not to this one.

```
python3 -m scripts.run_loop \
  --eval-set evalset.json --skill-path <this skill> \
  --model claude-opus-5 --max-iterations 1 --runs-per-query 1 \
  --holdout 0.4
```

Train 12, test 8. Score 6/12 train, 4/8 test.

## Why the numbers are not usable

Every should-trigger query scored a trigger rate of **0.0**, including
"This page looks like every other AI site, can you fix it". Every should-not
query scored 0.0 as well. A scorer that returns the same number for both sides
is not discriminating; it is stuck.

So the 6/12 and 4/8 are just the non-trigger half passing by default. They do
not say anything about the description.

The cause was measured, not guessed. The harness decides "triggered" by writing
the description into a synthetic slash command. It then watches whether the
model invokes it. One query, run by hand:

```
FIRST TOOL: (none) - no tool use; result reached
```

The model answers the question conversationally and never reaches for a tool at
all. With no tool call there is nothing for the harness to detect, so every
query looks like a non-trigger. This is a property of a one-shot `claude -p` on
this machine, not evidence about the wording.

## What was done about it

Nothing was applied. `best_description` came back byte-identical to the current
one, so there was no gain to adopt even if the measurement had been sound.
A broken scorer is no reason to change the wording. That is the kind of
unmeasured edit this skill exists to argue against.

## What would make this measurable

- Prompts that force a tool call, so there is something to detect. "Build me a
  landing page in `index.html`" gives the model a file to write; "my page looks
  generic" does not.
- Or a harness that reads the transcript for the skill being loaded, rather than
  inferring it from the first tool-use event.

Until one of those is in place, the trigger wording stays as written, and this
file is the record of why.
