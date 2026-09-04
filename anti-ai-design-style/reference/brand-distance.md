# The second guard: brand distance

**TL;DR:** this skill measures how AI-generated a design looks. It does not
measure how close the design sits to a specific company's brand. Those are two
different failures, and fixing one can cause the other. Run both guards.

## The defect that proved it

The first version of `examples/fixed-example.html` fixed every AI tell this
skill knows about. It scored 0 out of 100. It also used warm cream, a bookish
serif and a terracotta accent.

Ben spotted it: that is Claude's own design language. So the example was
measured with the `anti-antropik-design` skill's scanner:

```
FAIL #F5F1E8
  fails as neutral (2.74 Delta-E from a brand value, effectively identical)
  needs >= 12
FAIL font "georgia"  excluded typeface
VERDICT: NON-COMPLIANT (2 violations)
```

The register had already named this trap. Rule CO6, "the tasteful cream escape
look", says the palette AI tools fled to after purple was called out is now a
tell itself. The example walked into the rule the register describes. Passing
one scanner is not the same as being distinct.

## It was not one bad example. It was every page.

After the example was rebuilt, the three pages the skill produced during its
own eval run were measured the same way. All three failed:

```
clinic.html     FAIL #F3F5F2                        NON-COMPLIANT (1 violation)
budget.html     FAIL #B9B6AC #F1F1EA #FBFBF7        NON-COMPLIANT (3 violations)
deslop.html     FAIL #FBFBF9, georgia, source serif  NON-COMPLIANT (4 violations)
```

So 4 of 4 skill-generated pages passed the AI-look scanner and landed on the
brand anyway. That is the measured reason this guard is a gate, not advice.
The brief now says "generate the palette, then name it", the commands run
`audit_file.py`, and the stop hook refuses "done" without a COMPLIANT line.
The trap is structural: "escape generic AI" and "escape the cream editorial
look" pull in the same direction, straight into the warm off-white, serif,
terracotta corner.

## The two guards, and what each one can see

| Guard | Question it answers | What it cannot see |
|---|---|---|
| `scripts/ai_tell_scan.py` (this skill) | Does this look like generic AI output? | Whether the design sits on top of a specific real brand |
| `anti-antropik-design/scripts/audit_file.py` | Is this provably distant from a named brand? | Whether the design is generic in every other way |

They disagree usefully. A page can be brand-distant and still generic. A page
can be distinctive and still be sitting inside someone's trade dress.

## Run both

```
python3 scripts/ai_tell_scan.py <files>                     # this skill
python3 <anti-antropik>/scripts/exclusion_check.py --selftest
python3 <anti-antropik>/scripts/audit_file.py <files> --suggest
```

Both must pass before you present. `audit_file.py` prints suggested
replacement hex values when it fails, so the fix is usually one substitution.

## Generate the palette, do not pick it by hand

This is the single most useful thing the other skill provides. Instead of
choosing colours and hoping:

```
python3 <anti-antropik>/scripts/generate_palette.py \
  --hue 18 --temp neutral --chroma high --name Kiln --css --out palettes
```

It emits 16 roles in light and dark, checks each one, and prints
`VERDICT: COMPLIANT` with the full distance table. The current
`fixed-example.html` uses exactly this palette. Its accent is a deep oxblood
(`#780025`), which is 27.9 Delta-E from the nearest brand value.

Worth knowing: `--temp warm --chroma high` **failed** when tried, because warm
neutrals plus a clay accent plus warm near-black ink reproduces three brand
signature traits at once. That is not a bug. It is the conjunction rule
working, and it is exactly the trap the first example fell into.

## The typography half

`anti-antropik-design` also excludes typefaces, not just colours. Its list
includes Poppins, Lora and their substitutes, and Georgia is on it. It also
excludes the *structure* of a geometric sans heading over a bookish serif body,
whatever the family names.

Safe structures it names: one grotesque throughout; sans plus mono; a slab
heading over its own sans; a condensed display over a normal width. The current
example uses sans plus mono, which is why it now passes.

## When this second guard matters most

- Brand identity work, logos, style guides, decks and anything client-facing.
- Any time this skill's own advice pushes you toward warm neutrals, editorial
  serifs or a clay accent, which it will, because those are the natural escape
  from the purple era.
- Whenever a page has to be provably not-someone-else's, rather than just
  not-generic.

## If you do not have the other skill installed

The rule CO6 check in `scripts/rules.json` catches the cream-serif-terracotta
conjunction on its own, at low weight. That is a smoke alarm, not a
measurement. For real brand distance you need the Delta-E maths, which lives in
`anti-antropik-design`. Install it alongside this one.
