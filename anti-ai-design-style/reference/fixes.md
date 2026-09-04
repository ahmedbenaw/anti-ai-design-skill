# The fixes, in plain words

**TL;DR:** the scanner tells you WHAT it found. This file shows HOW to fix
each finding, with a small code example where it helps. Rule IDs match the
scanner's output and `tells-register.md`.

One fix beats all the others: fill in `templates/design-brief.md` before
you generate anything. Almost every tell below is what happens when nobody
made a decision. The brief is where you make the decisions.

---

## Colour findings

**CO1: AI purple/indigo accent.**
Ask one question: why this colour? If the answer is "the tool picked it",
pick again. Take it from your product's world. A bakery: crust brown. A
diving app: depth blue. A legal tool: ink and buff. Put the choice in your brief.

**CO2: Gradient headline text.**
```html
<!-- before --> <h1 class="bg-clip-text text-transparent bg-gradient-to-r ...">
<!-- after  --> <h1 class="text-[var(--ink)]">
```
Want emphasis? Make it bigger or bolder. Gradient text also breaks
contrast checking and high-contrast mode.

**CO3: Gradients everywhere.**
Count your gradients. Keep at most one, on one focal element. Zero is fine.

**CO4: Dark + glass + glow combo.**
Dark themes are fine. Build depth with type sizes and two or three flat
surface shades. Not with `bg-white/10 backdrop-blur` panels:
```css
--surface-0: #101214; --surface-1: #191c1f; --surface-2: #22262a;
```

**CO5: Glow blobs.** Delete the blurred blob divs. If the page feels empty
after, the content was thin. Fix the content, not the atmosphere.

**CO6: The cream/serif/terracotta "escape look".**
Warm neutrals are lovely. But this exact combo is the NEW default AI look.
Change at least one part of it (accent, serif, or structure). Write down why.

## Typography findings

**TY2/TY3: Slop font pairings, italic-serif garnish.**
Choose two faces for a reason you can say out loud. Example: a sturdy
sans for headings, because the product is a workhorse. A readable serif
for body, because people read paragraphs here. Then delete the one-word
italic garnish. It is decoration pretending to be a decision.

**TY4: Hero type sandwich.** Set your own type scale in the brief (for
example a 1.25 ratio, 5 to 7 steps). Use its top step for the headline.
Do not copy the template's `text-5xl md:text-7xl font-bold tracking-tight`.

**TY5: ALL-CAPS eyebrows.** Delete any label that adds no information.
`FEATURES` above a heading that says "Features" says it twice. Caps are
also harder to read for dyslexic users.

## Layout findings

**LA1: The SaaS skeleton.** Write down your visitor's first three
questions. Build one section per question, in that order. Cut every section
you cannot fill honestly. A day-old product has no testimonials.

**LA3: Icon tiles above headings.** Replace the icon grid with your
strongest real evidence: a screenshot, a worked example, a number you can
defend. See `examples/fixed-example.html`. It uses a sample ledger instead
of three icon cards.

**LA5: `Get Started` + `Learn More`.** Name the action. "Try it free for a
month". "See prices in EGP". "Book a table". One primary button per screen.

**LA6 / CP3: Round fake stats.** Real number or no number. Show the
product doing its job instead. That is what the fake stats were faking.

**LA8: Coloured side-stripes.** Keep only where the colour means something
(red = error). Delete decorative ones.

**LA9: Border + big shadow "ghost cards".** Pick one depth system: hairline
borders OR soft shadows, at two or three defined levels.

**LA11: min-h-screen everywhere.** Full height on the root wrapper only.
Sections should be as tall as what is in them.

**LA13: Untouched shadcn.** shadcn is fine. Change the tokens:
```css
:root { --primary: <your colour>; --radius: <your choice, 0 is allowed>; }
```
Add one token the defaults do not have. That token is your fingerprint.

## Icon and imagery findings

**IC1: Sparkles/Zap/Shield/Rocket.** Use icons only where they clarify.
If every card needs an icon to look finished, the cards are the problem.

**IC2: Emoji as icons.** Screen readers read them out loud
("sparkles rocket fire"). Use one consistent icon set with labels, or words.

**IC5: Placeholder people.** Never ship invented people. Use real quotes
with permission, or none. An honest "we launched last month" beats a fake
Sarah.

## Motion findings

**MO1: Everything fades in on scroll.** Remove the reveal wiring from body
content. If you keep any entrance animation: hero only, first view only,
and wrapped:
```css
@media (prefers-reduced-motion: no-preference) { .hero { animation: ... } }
```

**MO2/MO3/MO4: hover-grow everywhere, fake pulse, marquees.**
Motion is for feedback (something changed). It is not for proving the site
is alive. Use a static logo row. Pulse only on live data. Show hover by
colour or underline, not growth. Keep interactions under about 200ms.

## Copy findings

**CP1: Buzzwords.** For each one, ask: what does the product actually do?
Write that. "Saves you re-typing invoices" beats `streamlines your
workflow` every time. Objective, specific copy measurably beats
promotional copy. That research is from 1997. It predates AI.

**CP2: AI cadence.** Read the page out loud. Rewrite anything you would
never say to a customer's face, such as `it's not just X, it's Y`.

**CP6: The swap-the-logo test (do this last).**
Put a competitor's logo on your page. If nothing else needs to change, the
page is not yours yet. Go back to the brief.
