# Design brief — fill this in BEFORE generating anything

**TL;DR:** answer 7 short questions. Paste the result into your AI tool
before your first design prompt. This is the single highest-impact fix in
this whole skill. Generic design is what happens when the tool has to guess
taste. This file removes the guessing.

Takes about 10 minutes. No design experience needed. If you can describe
your product to a friend, you can fill this in.

Keep the finished file in your project (name it `DESIGN.md`). Lovable, Cursor, Claude Code and Google Stitch can all be told to follow it.

---

```markdown
# DESIGN.md — [your product name]

## 1. Who is this for, really?
[One sentence. Not "modern teams". Example: "bakery owners in Cairo who
bill cafés and hotels weekly, mostly from a phone."]

## 2. Three things on this page that could ONLY belong to my product
[This kills the swap-the-logo problem. Example: "a sample weekly ledger
with real bread names; prices in EGP; WhatsApp support line."]

## 3. The feeling, in plain words
[Pick 2-3 words YOU would use, not marketing words. Example: "sturdy,
warm, like a well-kept paper ledger." Bonus: name one real thing from
your product's world to steal colours and textures from.]

## 4. Colours: generated, then named
Do not pick hex codes by hand. Hand-picked "warm and tasteful" palettes land on
Claude's own design system (measured: 4 of 4 pages did). Run this instead:
`python3 <anti-antropik-design>/scripts/generate_palette.py --hue [0-360] --temp warm|neutral|cool --chroma low|medium|high --name [Name] --css`
It prints VERDICT: COMPLIANT and 16 ready colours. Paste the ones you use here:
- Background: [#______] (name it, e.g. "slate")
- Text:       [#______]
- Accent:     [#______], used ONLY for buttons and links
- Secondary text: [#______] (the generator already checked its contrast)

## 5. Fonts (two, chosen on purpose)
- Headings: [name] — because [reason]
- Body:     [name] — because [reason]
(Not Inter-by-default. Any font is fine if you chose it for a reason.)

## 6. Never do these (paste as-is, then add your own)
- No purple/indigo gradients; no gradient-filled headline text
- No glow blobs, glassmorphism panels, or decorative blur
- No emoji as icons; no ✨
- No "Get Started" / "Learn More" button pair — name the action
- No invented numbers ("10K+ users", "99.9% uptime") or invented people
- No fade-in-on-scroll on content; respect reduced-motion settings
- No section I can't fill honestly (no fake testimonials, no fake logos)
- Body text at least 16px, contrast at least 4.5:1, lines under 75 characters
- No warm-cream background + bookish serif + terracotta accent together (that
  is Claude's design system, and the escape look AI tools drift to)
- No Poppins, Lora, Georgia, Merriweather, Playfair, Source Serif, Crimson,
  Libre Baskerville, Montserrat, Jost or Futura (brand-guard excluded faces)
- No geometric sans heading over a bookish serif body, whatever the fonts

## 7. What the page must answer, in order
1. [The visitor's first question. Example: "What is this?"]
2. [Second. "How does it work for MY bakery?"]
3. [Third. "What does it cost and what's the catch?"]
Build one section per question. Nothing else.
```

---

**After you fill it in:** every design prompt starts with
"Follow DESIGN.md. Do not deviate from its colours, fonts, or Never list."
When the tool drifts (it will), don't argue in chat. Point it back at the
file. And re-run the scanner after each generation:
`python3 scripts/ai_tell_scan.py <your files>`
