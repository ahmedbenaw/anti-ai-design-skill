# Prompt packs — for Lovable, Bolt, v0, and Cursor

**TL;DR:** you don't need Claude Code to use this skill's rules. Fill in
`design-brief.md` first, then copy the block for your tool. Each block is
ready to paste; replace the [bracketed] parts.

These follow each vendor's own prompting guidance: Lovable knowledge files,
Vercel's "how to prompt v0", Bolt's keyword advice. They also use what the
research found works: explicit bans and reference-first prompting. One warning from the research: **ban lists breed new
defaults.** If the tool swerves into warm-cream-and-serif instead, that's
the known "escape look". Point it back at YOUR brief.

---

## Lovable

Paste your filled-in DESIGN.md into **Settings → Knowledge** (so it applies
to every prompt without restating). Then prompt:

```
Build [the page/screen] for [product].

Follow the design directions in my knowledge file exactly - its colours,
fonts, section order, and its "Never do these" list. Where the knowledge
file and your defaults disagree, the knowledge file wins.

Use my real content, not placeholders: [paste your actual headline, prices,
and copy]. Do not invent testimonials, statistics, or customer names.

Accessibility is required, not optional: body text at least 16px with 4.5:1
contrast, visible keyboard focus, buttons at least 44px tall, all animation
inside a prefers-reduced-motion media query.
```

## Bolt

Bolt responds well to named aesthetics. So name YOURS, not a trend:

```
Build [the page/screen] for [product].

Design direction (follow exactly, do not substitute your own):
[paste sections 3-7 of your DESIGN.md]

Hard bans: no purple or indigo gradients, no gradient text, no glassmorphism,
no glow or blur decorations, no emoji icons, no "Get Started"/"Learn More"
button pair, no invented numbers or people, no scroll-triggered fade-ins.

If you are unsure of a visual choice, choose the plainer option and use my
named colours.
```

## v0

v0's own guidance: describe the product surface, the context of use, and
constraints ("constraints tell v0 what not to invent"):

```
Product surface: [exact components and real data - e.g. "a pricing section
showing one plan at 120 EGP/month with a free first month, and a weekly
ledger sample with 4 rows"].

Context of use: [who, where, on what - e.g. "bakery owners on phones,
often in a delivery van, sometimes in bright sunlight"].

Constraints and taste: follow this design spec exactly:
[paste sections 4-6 of your DESIGN.md]
Change the shadcn theme tokens to my colours and radius - do not ship the
default zinc/slate theme. No placeholder.svg images; use [your assets].
```

## Cursor (and any rules-file editor: Windsurf, Copilot)

Create `.cursor/rules/design.mdc` (or the equivalent rules file) containing
your DESIGN.md, and add at the top:

```
Apply these rules to every UI file you write or edit.

Before declaring any UI task done, run:
  python3 <path-to-skill>/scripts/ai_tell_scan.py <the files you touched>
If it reports FAIL, apply its "do this" lines and re-run until PASS.
Never weaken or delete the scanner rules to make it pass.
```

## Claude Code / Claude (Cowork)

Install the skill itself. It does all of the above automatically. The
scanner and this brief are the portable versions for everywhere else.

---

## When the output still looks generic

1. **Check the brief, not the prompt.** Vague brief in, average design out.
   Sharpen section 2 (the "could only belong to my product" list).
2. **Give references, not adjectives.** "Like a well-kept paper ledger" or
   "like [a real site you admire], but warmer" beats "modern and clean".
3. **Don't iterate forever in the tool.** The research is clear: each AI
   revision pulls the design back toward the average. Lock the direction in
   the brief, regenerate from scratch once, then make small manual edits.
4. **Measure.** Run the scanner. Fix what it names. Stop when it passes,
   not when it "looks fine". Everything the AI makes looks fine.
