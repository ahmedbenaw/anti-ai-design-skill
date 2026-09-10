# Proposals for `anti-antropik-design`

Written 2026-09-10 while building `anti-ai-design-style`, which calls this skill
as its second guard. Nothing here was changed in the installed copy. It is
read-only by agreement, so this file is the whole change request.

Everything below was verified by running or reading the installed copy at
`~/.claude/skills/anti-antropik-design`, not from memory.

## 1. Cross-reference: the two guards measure different distances

Suggested addition to this skill's SKILL.md, near the top.

> **Run `anti-ai-design-style` alongside this one.** They measure two different
> distances and neither implies the other. This skill measures how close a
> design sits to a named brand. That one measures how far it sits from generic
> AI output. Four of four pages generated under that skill passed its own guard
> and failed this one. Passing one guard is not evidence about the other.

The number is from that skill's own iteration-1 evals, n = 1 per cell. It is
directional, not a rate.

## 2. The two implementations report different standard versions

`scripts/exclusion_check.py` line 30:

```
STANDARD_VERSION = "2.0"
```

`scripts/exclusion_check.js` line 21:

```
const STANDARD_VERSION = '1.1';
```

Both write that value into their JSON output as `standard_version`. So the same
page, audited through the two paths, comes back stamped with two different
versions of one standard. Anything keying on the version, a cache or a report,
will read them as different standards.

The font lists in the two files are byte-for-byte the same 37 names, so the
version numbers are the only thing that disagrees. Whichever is right, they
should match, and a test should keep them matching.

## 3. The Files table undercounts the palettes by eight

SKILL.md, Files table:

```
| `palettes/*.css`, `palettes.json` | five pre-verified UI palettes, light and dark |
```

`palettes/` holds 13 `.css` files: aperture, brass, dataviz, deepday, ember,
graphite, ionic, mango, meridian, rubicon, sequoia, voltage, zeolite.

Line 68 of the same file already knows better. It names the newer ones and adds
"plus the earlier five". The Files table just never caught up. A reader who
trusts the table will not go looking for the other eight.

## 4. The pairing check uses a subset of the excluded-font list

This one has teeth, and it is narrower than it first looks.

`audit_file.py` gets the main font check right. Line 288 imports the full list:

```
bad = fam in X.EXCLUDED_FONTS
```

That is all 37 names. But the T2 pairing check, the one that catches "geometric
sans together with bookish serif", uses two local sets defined at lines 73 to
77. Those hold 20 names between them, all of which are in the 37. The other 17 are
missing. On the sans side that includes Gilroy, Proxima Nova, Brandon
Grotesque, Museo Sans and Product Sans. On the serif side, Cardo, EB Garamond,
Vollkorn, Domine and Tiempos Text.

So a page setting headings in Gilroy and body in Cardo raises two font
violations, correctly. It never raises the pairing violation, because neither
name is in the pairing sets. The excluded *structure* goes unreported, even
though both halves of it were caught on their own.

Suggested fix: build the two sets from `X.EXCLUDED_FONTS` instead of re-listing
them. Tag each name in the source list as geometric-sans or bookish-serif, then
derive both sets from the tag. Either way there is one list, and it cannot
drift again.
