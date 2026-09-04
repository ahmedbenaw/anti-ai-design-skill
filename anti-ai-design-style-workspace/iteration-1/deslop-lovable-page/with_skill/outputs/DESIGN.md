# DESIGN.md — InvoiceFlow

> **Assumed brief.** You were not around to answer the three brief questions.
> So this was drafted from what the Lovable page already said about the
> product: invoicing software for teams, startup to enterprise, v2.0 with AI
> features, fast, scalable, secure. Change any line you disagree with, then
> ask for a re-run. Every design choice in fixed.html traces back to a line here.

## 1. Who is this for, really?
Founders and finance leads at teams that send invoices every month and want
to see, at a glance, what has been paid. Assumed from the page's own copy:
"startup or enterprise".

## 2. Three things on this page that could ONLY belong to my product
1. A real, readable example invoice as the hero image (the thing the product makes).
2. Money columns set in tabular figures on ruled lines, like a carbon-copy invoice book.
3. Paid / Due status written in words, in ledger green and ink, never colour alone.

## 3. The feeling, in plain words
Steady, tidy, like a well-kept invoice book. Colours and lines are taken
from paper invoices: off-white paper, dark ink, thin ruled lines, one green
stamp.

## 4. Colours (named, with hex codes and measured contrast)
- Background "paper":   #fbfbf9
- Text "ink":           #1c1f1d  (16:1 on paper)
- Accent "ledger green": #1f5f3f  (7.3:1 on paper; white text on it 7.6:1). Buttons and links only.
- Secondary text "pencil": #4f5a55 (6.9:1 on paper)
- Ruled lines "rule":   #cfd8d3  (decorative only)
- Invoice sheet:        #ffffff

## 5. Fonts (two, chosen on purpose)
- Headings and the invoice: IBM Plex Sans, because it was designed for business
  documents and has tabular figures, so money columns line up.
- Body: Source Serif 4, because it was designed for reading paragraphs on screen.

## 6. Never do these
- No purple/indigo gradients; no gradient-filled headline text
- No glow blobs, glassmorphism panels, or decorative blur
- No emoji as icons; no ✨
- No "Get Started" / "Learn More" button pair — name the action
- No invented numbers ("10K+ users", "99.9% uptime") or invented people
- No fake "live" counters or urgency
- No animation except hover/focus feedback, and that inside a reduced-motion check
- No section I can't fill honestly (no fake testimonials, no fake logos)
- Body text at least 16px, contrast at least 4.5:1, lines under 75 characters

## 7. What the page must answer, in order
1. What is this? (hero, with the example invoice)
2. What do I get, and is it for a team my size? (what you get; who it is for)
3. What does it cost, can I cancel, is my data safe, can I get help? (price and the small print)
4. How do I start? (one button)
