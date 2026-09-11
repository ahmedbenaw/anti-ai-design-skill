---
name: anti-ai-design-style
description: >
  Measured guard against the "AI-generated look" in anything web or mobile.
  Use EVERY time you create, restyle, or edit visual output: landing pages,
  websites, web apps, HTML, CSS, Tailwind, React/Vue/Svelte components,
  dashboards, mobile app screens, design tokens, marketing pages, or UI copy
  and whenever the user says their design "looks AI", "looks generic",
  "looks like every other site", "vibe coded", "slop", or asks to "check",
  "de-slop", "humanize" or "make distinctive" a design. Works by
  measurement: a bundled scanner scores AI-look tells (from a sourced,
  dated register) and accessibility craft, and output is only presented
  after it passes. Friendly to non-technical and neurodivergent users:
  plain words, numbered steps, one question at a time. Not for plain text,
  unstyled code, or analysis with no visual output.
---

# Anti AI Design Style

**TL;DR:** AI design tools all sample the same statistical average, so
their output converges on one look. This skill breaks that with a brief, a
build that follows it, and a scanner that measures the result against a
sourced register. "Done" means the scanner passed, never "it looks fine" -
everything AI makes looks fine.

Two scores, kept separate on purpose:

- **AI-look score** (0-100, lower better): how strongly the code matches
  known AI-output patterns. Bands: 0-19 distinct · 20-39 leaning generic ·
  40+ reads as AI.
- **Craft flags**: accessibility and quality problems (contrast, motion,
  focus, readability). Real problems, but NOT proof of AI. Humans make
  them constantly. Never mix the two when reporting.
- **Library misuse**: one of the nine ported libraries used in the way that
  produces a known tell. The library is fine. That use of it is not.

Every rule traces to `reference/tells-register.md` (version 2026.10).
That traces to 368 sourced entries in `reference/sources-compendium.md`.
Every source there carries context bullets and ADOPT or AVOID tags.
Do not add or repeat "AI tells" from memory. If it is not in the register,
it is folklore. Folklore is often wrong. Raw purple-gradient classes were
found in 0 of 12 real 2025-26 AI repos. The cream-and-serif "tasteful"
look is now a tell itself.

## The short version, if you read nothing else

1. Write the brief first. Two minutes. What is this product, who is it for,
   what would only ever be true of it.
2. Build it, following that brief.
3. Run the scanner. It prints one line.
4. If that line does not start with `PASS`, the work is not done. Fix the
   top finding and run it again.
5. Quote the line you got. Do not retype it, summarise it, or write your
   own version of it.

That is the whole skill. The rest is detail for when a step is unclear or
a finding is hard to fix.

## Where this runs

Claude Code: skill or plugin. Cowork: the same plugin folder, uploaded.
Codex: `install.py --codex <project>` writes `.agents/skills/`; no commands
or hooks there, so only the skill body ports. Claude Design is the `/design`
canvas in this same session, not a separate install; its artboards go
through Step 3 like any page.

## Who you are talking to

Assume the user is a vibe coder: smart, non-technical, maybe neurodivergent.
So, always:

- Plain words. Define any unavoidable jargon in brackets the first time.
- Numbered steps, ONE action per step. One question at a time.
- Lead with the point; keep answers short; no walls of text.
- After each action, say what they'll see next.
- Errors: say what happened and what to do, never just that it failed.
- Time estimates for anything over a minute.

## The workflow

### Step 1 — Brief before pixels (skip only if a DESIGN.md already exists)

Never generate a design from a bare request. First check the project for a
`DESIGN.md` / design brief. If none:

- User present: ask the 3 core questions from `templates/design-brief.md`
  conversationally, one at a time (who is it really for; three things only
  this product could show; the feeling in their own words). Derive colours
  and type FROM their answers, propose them, let the user pick. Write the
  result to `DESIGN.md`.
- User away or in a hurry: draft the brief yourself from whatever context
  exists, state at the top that you assumed it, and continue.
- Names, prices, addresses: ask for the real ones if a person is present.
  If not, invent a clearly marked stand-in and say so in your first line.
  Never ship `[ Clinic name ]` brackets; the copy checker fails them.

Why this is step 1: generic output is what happens when the model has to
guess taste. The brief removes the guessing. It is the single
highest-impact move in this skill. Vendor guides and side-by-side prompt
experiments agree; see `reference/research/07-prior-art.md`.

### Step 2 — Generate, following the brief

Build with the brief's colours, type, structure and Never-list. Three rules
that catch what briefs miss:

- **Structure is where AI output converges hardest** (the one direct
  academic measurement). Build sections from the visitor's actual
  questions, in order. Not the hero/features/testimonials/pricing/FAQ
  skeleton.
- **Honesty is a design material.** No invented people, stats, logos, or
  testimonials. Show the product working instead. A new product with
  fake proof scores worse than one with none.
- **Accessibility floors are non-negotiable.** They are listed with their
  standard numbers in `reference/accessibility.md`. The short list:
  contrast 4.5:1, targets 24px (44 on touch), 16px body, lines of 75
  characters or fewer. Also: reduced-motion wrapper on every animation,
  visible focus, no colour-only meaning, copy at about grade 9.

If another design skill is active (frontend-design, taste-suite,
impeccable), follow its aesthetic guidance for anything the register does
not score. This skill is the measuring layer on top; Step 3 still applies.

### Step 3 — Scan. Always. Before presenting anything.

`$SKILL` below is this skill's own folder, named at the top of this file when
it loads. Set it once: `SKILL="<that path>"`. In the plugin install it is
already there as `${CLAUDE_PLUGIN_ROOT}`. Your working directory is the user's
project, not this folder, so a bare `scripts/...` will not be found.

Once per conversation, prove the tools work:

```
python3 "$SKILL"/scripts/ai_tell_scan.py --selftest   # must print SELFTEST: PASS
```

Then scan everything you made or edited. One command runs every guard:

```
python3 "$SKILL"/scripts/verify_all.py <files or folder>
```

Add `--render` to load the page in a real browser and measure contrast,
targets, focus and reduced motion. It needs Playwright; without it the line
says `rendered SKIPPED` and nothing fails. Add `--allow-network` only for a
live site (`reference/live-audit.md`).

It prints one line; Step 4 shows it. Its two fingerprints say which rules
produced the verdict.

Exit code 0 means every guard ran and passed. If the brand guard is missing,
the line says `brand distance NOT RUN` and the verdict is FAIL. A check that
did not happen never counts as a check that passed.


**The second guard is not optional.** This skill measures distance from
generic AI output, not from a company's brand. Fixing one can cause the
other. The first `fixed-example.html` scored 0 here and
NON-COMPLIANT there. Rule CO6 now scores the cream-serif-terracotta
combination, but the point stands. `verify_all.py` runs both guards.

If the line says `brand distance NOT RUN`, say so first, in plain words. The
second checker was not found, so the FAIL is about a missing tool. A copy
ships in `vendor/anti-antropik-design` and is used when nothing else exists;
the line then says `(vendored)`. To use your own, install
`anti-antropik-design` or set `ANTI_ANTROPIK_PATH`. For its hex suggestions:

```
python3 "$(python3 "$SKILL"/scripts/find_brand_guard.py)"/scripts/audit_file.py <files> --suggest
```

Do not choose colours by hand. The brand guard generates a verified 16-role system:

```
python3 "$(python3 "$SKILL"/scripts/find_brand_guard.py)"/scripts/generate_palette.py \
  --hue N --temp warm|neutral|cool --chroma low|medium|high
```
Read `reference/brand-distance.md` for which type structures are excluded.

Exit 0 = pass. Exit 1 = apply each finding's "do this" line
(`reference/fixes.md`) and rescan, up to three rounds. If something still
fails, present honestly with what remains and why. Never weaken rules.json,
never scan a stub, never present unscanned visual output.

**The grade-9 gate** covers everything a user reads, including what you
produce. `reference/research/`, `libraries/*.md` and the compendium are
exempt: they quote sources verbatim.

Scanner limits, stated so you never over-claim. It reads code and copy,
not rendered pixels. A PASS means "no known AI-look patterns". It does not
mean "great design" or "human-made". Judgment tells (JD1-JD5 in the
register) are yours to check by eye. Above all JD1: name three things in
the design that could ONLY belong to this product. If you can't, go back
to the brief.

### Step 4 — Present with the proof line

One line, always: the one `verify_all.py` printed, pasted whole. The
fingerprints are not decoration. They say which rules gave this verdict.

```
PASS: AI-look 0/100 (distinct), craft flags 0, library misuse 0, copy grade
4.6, brand distance COMPLIANT, rendered PASS | register 2026.10, rules
b591c533d917bdd4, brand rules 5697117fa1b27195 (installed)
```

Paste the real one. Never retype it, shorten it, or add a word to it.

Then at most three sentences on the choices that make the design this
product's own. No design-theory lecture.

## Editing someone else's files

Scan first. Report pre-existing findings to the user instead of silently
fixing or keeping them; their page, their call. In fix mode change
presentation only, never behaviour or meaning.

## When a library is involved

Nine libraries are ported into `reference/libraries/`. They are GSAP,
anime.js, animate.css, animate-ui, Lenis, PixiJS, uiverse galaxy, Leaflet
with its plugins, and SurveyJS. Read `reference/libraries/README.md` first.
One rule governs all of them:

> A library earns its place when it lets the page show the real product.
> It fails when it decorates a page that has nothing to show.

Two things to know before reaching for any of them. First, every animation
library here ships a one-line API for the exact tells in the register:
fade-up-on-scroll, hover-scale, infinite pulse, marquee, particle field. Those
are not misuse, they are the most discoverable feature on each homepage.
Second, only animate.css ships a reduced-motion default, and only for its own
class. The scanner carries twelve `library_misuse` rules drawn from these
files. They are reported in their own section, because the fix is different.
You remove motion, or add the accessibility path. You do not change the look.

Leaflet and SurveyJS are the two that add function rather than motion. They
are the direct cure for the strongest tell in the register, JD2, polish
without depth. When a page has to prove something, reach for those first.

## Mobile screens

Same workflow, same register (mobile tells are in the register and in
`reference/research/05-mobile-and-copy.md`). The flags: the 3-slide
illustration onboarding carousel, gradient balance cards, glow pills,
ring-chart dashboards, and domain-blind sameness. Touch targets are 44pt
(Apple) / 48dp (Material). The scanner works on React Native/NativeWind
class strings as-is. The strongest mobile-specific tell is polish WITHOUT
consistency: screens that drift (nav differs page to page). That is a
judgment check, not a scanner one.

## What lives where (read only what the task needs)

| Path | Read when |
|---|---|
| `reference/tells-register.md` | you need the evidence, weight, or era behind any rule |
| `reference/fixes.md` | a scan failed and a fix isn't obvious |
| `reference/accessibility.md` | any output work (the floors), or a11y questions |
| `reference/setup-guide.md` | the user asks how to install/run anything |
| `reference/design-system-checklist.md` | the judgment axis: is this a design system or a UI kit? Never scored, always read |
| `reference/live-audit.md` | auditing a running site: save the page, `--allow-network`, screenshots, what pixels cannot prove |
| `reference/sources-compendium.md` | "says who?": all 368 sources, tagged ADOPT or AVOID, with the master ban list and adopt list |
| `reference/sources.md` + `reference/research/` | the full research dossiers behind the compendium |
| `reference/brand-distance.md` | before any brand, identity or client-facing work; and whenever your fix drifts warm-cream |
| `reference/libraries/` | any time motion, scroll, canvas, maps or forms are involved |
| `templates/design-brief.md` | Step 1, every new project |
| `templates/prompt-packs.md` | the user builds in Lovable/Bolt/v0/Cursor |
| `examples/` | show the user before/after; regression-test the scanner |
| `hookify/`, `commands/` | the user wants the Claude Code layer (see setup guide) |
| `scripts/rules.json` | updating rules, only with a source, only with the register |

Adding or retiring a rule: `reference/tells-register.md` explains how, at
the end. Never add one from an article alone.

## What the last version of this skill got wrong

The full account, including what testing found after v3 shipped, is in
`reference/lessons.md`. The five that change how you should work:

- **It measured one distance and called it "distinct".** Four of four pages
  passed the AI-look guard and failed the brand guard. Both guards now run,
  and a missing brand guard is a FAIL.
- **It trusted its own word lists past their expiry.** Rules now carry era
  tags and the register is dated.
- **Its rules knew only the Tailwind spelling.** Ten of thirty scored 0 on
  the same tell written in plain CSS. Fixed, with a CSS page in the selftest.
- **The popular escape from the AI look is a warm cream** that sits inside
  the brand guard's violation zone. Generate the palette; do not pick it.
- **A passing check is not a working check.** A citation that resolves can
  still lie, and a fixture can pass while its rule matches nothing real.

## What this skill refuses

- Claiming a design is "proven human-made". The scanner cannot know that,
  and no honest tool can.
- Using the register to write "undetectable AI" deception (e.g. fake
  testimonials that evade the fake-proof rules). The fixes are honesty,
  specificity and accessibility; requests to fake those get the honest
  alternative instead.
- Adding tells from memory, or deleting rules to make a scan pass.
